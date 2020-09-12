import $ from 'jquery';

class Test {
  constructor() {
    /*var home_url = window.location.protocol + '//' + window.location.hostname
    if (home_url.includes('localhost')) { home_url = 'http://localhost:8000' }

    this.cartFeed = $('.cartFeed')
    this.order_api = home_url + '/api/order/'
    this.order_item_api = home_url + '/api/order-item/'

    this.productFeed = $('.productFeed')
    this.productsApi = home_url + '/api/products/'

    this.populateCartFeed()
    this.populateProductFeed()*/

    this.brandList = $('.brandList')
    if (this.brandList) {
      this.brand_api = home_url + '/api/brand/'
      this.populateBrandList()
    }

    this.productList = $('.productList')
    if (this.productList) {
      this.product_manager_api = home_url + '/api/product-manager/'
      this.order_api = home_url + '/api/order/'
      this.populateProductList()
    }

    this.wishlistCount = $('.wishlistCount')
    if (this.wishlistCount) {
      this.wishlist_item_api = home_url + '/api/wishlist-item/'
      this.countWishlistItems()
    }

    this.wishlistList = $('.wishlistList')
    if (this.wishlistList) {
      this.wishlist_item_api = home_url + '/api/wishlist-item/'
      this.order_api = home_url + '/api/order/'
      this.populateWishlistList()
    }

    this.orderCount = $('.orderCount')
    if (this.orderCount) {
      this.order_item_api = home_url + '/api/order-item/'
      this.countOrderItems()
    }

    this.orderList = $('.orderList')
    if (this.orderList) {
      this.order_api = home_url + '/api/order/'
      this.populateOrderList()
    }
  }


  populateBrandList() {
    var that = this

    that.brandList.each(function() {
      var current_list = $(this)

      fetch(that.brand_api)
      .then((resp) => resp.json())
      .then(function(data) {
        var brands = data

        if (brands) {
          for (var i in brands) {
            var brand = brands[i]

            if (brand.status == 2) {
              var html = `
                <div>
                  <h6>${ brand.name }</h6>
                </div>
                `
              current_list.html(html)
            }
          }
        }
      })
    })
  }


  populateProductList() {
    var that = this

    that.productList.each(function(index) {
      var current_list = $(this)

      fetch(that.product_manager_api)
      .then((resp) => resp.json())
      .then(function(data) {
        var product_managers = data

        if (product_managers) {
          for (var i in product_managers) {
            var product_manager = product_managers[i]
            var product_options = product_manager.product_option

            // TODO: Add logic to check if products are in stock/available.

            if (product_options) {
              var porduct_color = product_manager.color.name
              var product_option_prices = []
              var product_option_sizes = []
              var product_options_html = '<div class="seperator mt-1"></div>'

              for (var x in product_options) {
                var product_option = product_options[x]
                var product_status = product_option.status

                if (product_status == 2) {
                  var product_option_size = product_option.size.name
                  var product_option_id = product_option.id
                  product_option_prices.push(product_option.gross)
                  product_option_sizes.push(product_option_size)

                  product_options_html += `
                    <label class="checkbox form-check m-0 p-1">
                      <input class="form-check-input productOption" type="radio" name="productOption" value="${ product_option_id }">
                      <h6 class="checkbox-text checkbox-text-strong m-0 ml-1 text-small text-regular">${ product_option_size }</h6>
                    </label>
                  `
                }
              }
              product_options_html += '<div class="seperator mt-1"></div>'

              if (product_option_prices.length > 0
              && product_option_sizes.length > 0) {
                var product_images = product_manager.image

                if (product_images.length > 0) {
                  var title_image = product_manager.image[0].image
                } else {
                  var product_brand_images = product_manager.brand_image
                  if (product_brand_images.length > 0) {
                    var title_image = product_manager.brand_image[0].image
                  }
                }

                if (title_image) {
                  product_option_prices.sort(function(a, b) { return a-b })
                  var product_prices_from = product_option_prices[0]
                  if (product_prices_from < product_option_prices[-1]) {
                    product_prices_from = 'ab ' + product_prices_from
                  }
                  var product_name = product_manager.product.name
                  var wishlist_item = product_manager.wishlist_item

                  var wishlist_item_id = ''
                  if (wishlist_item[0]) {
                    var wishlist_item_id = wishlist_item[0]
                    var wishlist_html = `
                      <button class="btn p-0 wishlist updateWishlist" data-unique="productList${ index + i }" data-action="delete">
                        <svg class="bi bi-heart text-primary wishlist__icon wishlist__icon--filled" viewBox="0 0 26.593 25.22" xmlns="http://www.w3.org/2000/svg"><path d="M12.267,2.015c6.8-7,23.819,5.246,0,20.985C-11.552,7.262,5.462-4.98,12.267,2.015Z" transform="translate(1.03 1.022)" fill="currentColor" stroke="currentColor" stroke-width="2" fill-rule="evenodd"/></svg>
                      </button>
                    `
                  } else {
                    var wishlist_html = `
                      <button class="btn p-0 wishlist updateWishlist" data-unique="productList${ index + i }" data-action="add">
                        <svg class="bi bi-heart text-dark wishlist__icon wishlist__icon--outline" viewBox="0 0 26.593 25.22" xmlns="http://www.w3.org/2000/svg"><path d="M12.267,2.015c6.8-7,23.819,5.246,0,20.985C-11.552,7.262,5.462-4.98,12.267,2.015Z" transform="translate(1.03 1.022)" fill="none" stroke="currentColor" stroke-width="2" fill-rule="evenodd"/></svg>
                        <svg class="bi bi-heart text-primary wishlist__icon wishlist__icon--filled d-none" viewBox="0 0 26.593 25.22" xmlns="http://www.w3.org/2000/svg"><path d="M12.267,2.015c6.8-7,23.819,5.246,0,20.985C-11.552,7.262,5.462-4.98,12.267,2.015Z" transform="translate(1.03 1.022)" fill="currentColor" stroke="currentColor" stroke-width="2" fill-rule="evenodd"/></svg>
                      </button>
                    `
                  }

                  // TODO: Add logic to check if product is order.

                  var html = `
                    <div>
                      <div class="d-flex">
                        <div class="position-relative">
                          <div class="position-absolute" style="right: 0.5em; top: 0.5em;">
                            ${ wishlist_html }
                          </div>
                          <img src="${ title_image }" style="height: 10em;">
                        </div>
                        <div class="ml-3">
                          <h6>${ product_name }</h6>
                          <p>
                            € ${ product_prices_from }
                            <br>
                            ${ porduct_color }
                            <br>
                          </p>
                          <div class="d-flex">

                            <div class="dropdown">
                              <button class="btn btn-sm btn-outline-info dropdown-toggle productOptionIndicator" type="button" id="productDetailNavSizeDropdown" data-toggle="dropdown">
                                Größe
                              </button>
                              <div class="dropdown-menu border border-info p-0" aria-labelledby="productOptionDropdown">
                                ${ product_options_html }
                              </div>
                            </div>

                            <button class="btn btn-sm btn-primary ml-2 updateOrder" data-action="add" data-unique="productList${ index + i }">Add to cart</button>
                          </div>
                        </div>
                      </div>
                    </div>
                    `
                  current_list.html(html)

                  var product_option_id = '' // Add real product option selector here!!
                  var updateWishlist = $($(`.updateWishlist[data-unique="productList${ index + i }"]`))
                  updateWishlist.on("click", (function(product_manager) {
                    return function(e) {
                      that.updateWishlist(e, product_manager, product_option_id, wishlist_item_id)
                    }
                  })(product_manager))

                  var updateOrder = $($(`.updateOrder[data-unique="productList${ index + i }"]`))
                  updateOrder.on("click", (function(e) {
                    product_option_id = $('input[name="productOption"]:checked').val()
                    that.updateOrder(e, product_option_id)
                  }))
                }
              }
            }
          }
        }
      })
    })
  }


  countWishlistItems() {
    var that = this

    if (user != 'AnonymousUser') {
      fetch(that.wishlist_item_api)
      .then((resp) => resp.json())
      .then(function(data) {
        var wishlist_items = data
        if (wishlist_items.length > 0) {
          var wishlist_count = wishlist_items.length
          that.wishlistCount.html(wishlist_count)
        }
      })
    }
  }


  populateWishlistList() {
    var that = this

    that.wishlistList.each(function(index) {
      var current_list = $(this)

      if (user != 'AnonymousUser') {
        fetch(that.wishlist_item_api)
        .then((resp) => resp.json())
        .then(function(data) {
          var wishlist_items = data
          var html = ''

          if (wishlist_items.length > 0) {
            for (var i in wishlist_items) {
              var wishlist_item = wishlist_items[i]
              var product_manager = wishlist_item.product_manager
              var product_name = product_manager.product.name

              var html = `
                <div class="d-flex align-items-center wishlistItem">
                  <h6 class="m-0">${ product_name }</h6>
                  <button class="btn btn-sm btn-danger ml-3 updateWishlist" data-unique="wishlistList${ index + i }" data-action="delete">Delete</button>
                </div>
              `
              current_list.html(html)

              var product_option = ''
              var wishlist_item_id = wishlist_item.id
              var updateWishlist = $($(`.updateWishlist[data-unique="wishlistList${ index + i }"]`))
              updateWishlist.on("click", (function(product_manager) {
                return function(e) {
                  that.updateWishlist(e, product_manager, product_option, wishlist_item_id)
                }
              })(product_manager))
            }
          } else {
            var html = `
              <div>
                <h6>Deine Wunschliste ist noch leer.</h6>
              </div>
            `
            current_list.html(html)
          }
        })

      } else {
        var html = `
          <div>
            <h6>Melde dich zuerst an um deine Wunschliste zu verwenden.</h6>
          </div>
        `
        current_list.html(html)
      }
    })
  }


  updateWishlist(e, product_manager, product_option, wishlist_item_id) {
    var that = this
    var action = $(e.target.closest('.updateWishlist')).data('action')

    // Add.
    if (action == 'add' && product_manager) {
      var product_manager_id = product_manager.id

      fetch(that.wishlist_item_api, {
        method:'POST',
        headers:{
          'Content-type':'application/json',
          'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
          'product_manager':product_manager_id,
          'product_option':product_option,
        })
      })
      .then((resp) => resp.json())
      .then(function(response) {
        console.log(response)
        that.populateProductList()
        that.countWishlistItems()
        that.populateWishlistList()
      })

    // Delete.
    } else if (action == 'delete' && wishlist_item_id) {
      fetch(that.wishlist_item_api + wishlist_item_id + '/', {
        method:'DELETE',
        headers:{
          'Content-type':'application/json',
          'X-CSRFToken':csrftoken,
        },
      })
      .then(function(response) {
        console.log(response)
        that.populateProductList()
        that.countWishlistItems()
        that.populateWishlistList()
      })

    }
  }


  countOrderItems() {
    var that = this

    /*if (user != 'AnonymousUser') {
      fetch(that.order_item_api)
      .then((resp) => resp.json())
      .then(function(data) {
        var order_items = data
        if (order_items.length > 0) {
          var order_count = ''
          for (var i in order_items) {
            order_item = order_items[i]
            // order_count += order_item.quantity
          }
          that.orderCount.html(order_count)
        }
      })
    } else {
      // Add cookie logic here!!
    }*/
  }


  populateOrderList() {
    var that = this;

    /*that.orderList.each(function() {
      var current_list = $(this)
      var current_list_style = current_list.data('style')

      if (user != 'AnonymousUser') {
        var filter = ''
        if (current_list_style == 'cart') {
          filter = '?status=1'
        }

        fetch(that.order_api + filter)
        .then((resp) => resp.json())
        .then(function(data) {
          var orders = data

          if (orders.length > 0) {

          } else {
            var html = `
              <div>
                <h6>Dein Warenkorb ist noch leer.</h6>
              </div>
            `
            current_list.html(html)
          }
        })
      } else {
        // Get cart/order cookies
      }
    })*/
  }


  updateOrder(e, product_option_id) {
    var that = this

    if (product_option_id) {
      var action = $(e.target.closest('.updateOrder')).data('action')

      if (action == 'add') {
        if (user != 'AnonymousUser') {
          fetch(that.order_api + '?status=1')
          .then((resp) => resp.json())
          .then(function(data) {
            var orders = data

            if (orders) {
              var order = orders[0]

              if (order) {
                var order_items = order.order_items

                if (order_items.length > 0) { // == 1
                  // update amount of item.

                } else {
                  fetch(that.order_item_api, {
                    method:'POST',
                    headers:{
                      'Content-type':'application/json',
                      'X-CSRFToken':csrftoken,
                    },
                    body:JSON.stringify({
                      'order':order.id,
                      'product_option':product_option_id,
                      'quantity':1,
                    })
                  })
                  .then((resp) => resp.json())
                  .then(function(response) {
                    console.log(response)
                    // that.countOrderItems()
                    // that.populateOrderList()
                  })

                }
              }
            }
          })

        } else {
          // Make add to cart logic with cookies here.
        }
      }
    }
  }


  /*addOrderItem(oder_id, product_option_id, exists) {
    var that = this

    if (exists) {
      /*
      Increase quantity of order item.
      */
      // First get then increase.

      /*fetch(that.order_item_api + product_option_id + '/', {
        method:'POST',
        headers:{
          'Content-type':'application/json',
          'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
          'quantity':1,
          'order':order_id,
          'product_option':product_option_id,
        })
      })
      .then((resp) => resp.json())
      .then(function(response) {
        console.log(response)
      })

    } else {
      /*
      Create new order item.
      */

      /*console.log(oder_id)
      console.log(product_option_id)
    }
  }*/







  addCartItemOLD(order_id, item, product_id) {
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


  removeCartItemOLD(item) {
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


  deleteCartItemOLD(item) {
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
  updateCartOLD(e, product) { // product
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



  populateProductFeedOLD() {
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
          currentFeed.html(product)

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


  populateCartFeedOLD() {
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
            that.cartFeed.html(item)

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
