import $ from 'jquery';

class Test {
  constructor() {
    var domain = window.location.protocol + '//' + window.location.hostname
    if (domain.includes('localhost')) { domain = 'http://localhost:8000' }

    this.cartFeed = $('.cartFeed')
    this.order_api = domain + '/api/order/'
    this.order_item_api = domain + '/api/order-item/'

    this.productFeed = $('.productFeed')
    this.productsApi = domain + '/api/products/'

    this.populateCartFeed()
    this.populateProductFeed()
  }


  addCartItem(order_id, item, product_id) {
    var that = this

    if (item == null) {
      fetch(that.order_item_api, {
        method:'POST',
        headers:{
          'Content-type':'application/json',
          'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
          'quantity':1,
          'order':order_id,
          'product':product_id,
        })
      })
      .then((resp) => resp.json())
      .then(function(response) {
        console.log(response)
      })

    } else {
      var quantity = item.quantity + 1
      var order_item_api = that.order_item_api + item.id + '/'

      fetch(order_item_api, {
        method:'PUT',
        headers:{
          'Content-type':'application/json',
          'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
          'quantity':quantity
        })
      })
      .then((resp) => resp.json())
      .then(function(response) {
        console.log(response)
      })

    }
  }


  removeCartItem(item) {
    var that = this

    if (item.quantity <= 1) {
      that.deleteCartItem(item)
    } else {
      var quantity = item.quantity - 1
      var order_item_api = that.order_item_api + item.id + '/'

      fetch(order_item_api, {
        method:'PUT',
        headers:{
          'Content-type':'application/json',
          'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
          'quantity':quantity
        })
      })
      .then((resp) => resp.json())
      .then(function(response) {
        console.log(response)
      })
    }

  }


  deleteCartItem(item) {
    var that = this
    var order_item_api = that.order_item_api + item.id + '/'

    fetch(order_item_api, {
      method:'DELETE',
      headers:{
        'Content-type':'application/json',
        'X-CSRFToken':csrftoken,
      }
    })
    // .then((resp) => resp.json())
    .then(function(response) {
      console.log(response)
    })
  }


  // Create/edit cart add/remove items
  updateCart(e, product) { // product
    var that = this
    var action = $(e.target).data('action')


    fetch(that.order_api)
    .then((resp) => resp.json())
    .then(function(data) {
      var orders = data
      var order_id = null
      var item = null
      var product_id = product.id

      if (orders) {
        for (var i in orders) {
          var order = orders[i]
          order_id = order.id
          var items = order.items

          if (order.status == 1) {

            var items_in_cart = 0
            for (var x in items) {
              if (items[x].product.id == product_id) {
                item = items[x]
                items_in_cart = items_in_cart + item.quantity
              }
            }

            if (action == 'add') {
              that.addCartItem(order_id, item, product_id)
            } else if (action == 'delete') {
              that.deleteCartItem(item)
            } else if (action == 'remove') {
              that.removeCartItem(item)
            }

          }
        }
      }

      if (order_id == null && action == 'add') {
        fetch(that.order_api, {
          method:'POST',
          headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
          },
          body:JSON.stringify({
            'status':1,
          })
        })
        .then((resp) => resp.json())
        .then(function(response) {
          console.log(response)
          order_id = response.id
          that.addCartItem(order_id, item, product_id)
        })
      }
    })
  }



  populateProductFeed() {
    var that = this

    that.productFeed.each(function() {
      var currentFeed = $(this)
      var sort = $(this).data('sort')
      var amount = parseInt($(this).data('amount'))

      fetch(that.productsApi + '?ordering=' + sort)
      .then((resp) => resp.json())
      .then(function(data) {

        var products = data.slice(0,amount)

        for (var i in products) {
          var product = `
              <div class="mt-4">
                <div class="d-flex">
                  <img src="${products[i].image}" class="img img-fluid" alt="test" style="width: 5em; height: 5em;">
                  <div class="mx-3 w-50">
                    name: ${products[i].name}<br>
                    price: ${products[i].price}
                  </div>
                  <div>
                    <button class="btn btn-primary updateCart" data-action="add">Add</button>
                  </div>
                </div>
                <hr class="bg-info">
              </div>
            `
          currentFeed.append(product)

          var updateCart = $($('.updateCart[data-action="add"]')[i])
          updateCart.on("click", (function(product) {
            return function(e) {
              that.updateCart(e, product)
            }
          })(products[i]))
        }
      })
    })
  }


  populateCartFeed() {
    var that = this

    fetch(that.order_api)
    .then((resp) => resp.json())
    .then(function(data) {

      var orders = data
      for (var i in orders) {
        if (orders[i].status == 1) {

          var order = orders[i].items
          for (var x in order) {

            var item = `
                <div class="mt-4">
                  <div class="d-flex">
                    <img src="${order[x].product.image}" class="img img-fluid" alt="test" style="width: 5em; height: 5em;">
                    <div class="mx-3 w-50">
                      name: ${order[x].product.name}<br>
                      price: ${order[x].product.price}<br>
                      amount: ${order[x].quantity}
                    </div>
                    <div class="d-flex align-items-center">
                      <div>
                        <button class="btn btn-danger updateCart" data-action="delete">Delete</button><br>
                        <button class="btn mt-2 text-strong w-100 updateCart" data-action="remove">-</button>
                      </div>
                    </div>
                  </div>
                  <hr class="bg-info">
                </div>
              `
            that.cartFeed.append(item)

            var updateCart = $($('.updateCart[data-action="delete"]')[x])
            updateCart.on("click", (function(product) {
              return function(e) {
                that.updateCart(e, product)
              }
            })(order[x].product))

            var updateCart = $($('.updateCart[data-action="remove"]')[x])
            updateCart.on("click", (function(product) {
              return function(e) {
                that.updateCart(e, product)
              }
            })(order[x].product))
          }
        }
      }

    })

  }


}

export default Test;
