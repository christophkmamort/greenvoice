import $ from 'jquery';

class Test {
  constructor() {
    var domain = window.location.protocol + '//' + window.location.hostname
    if (domain.includes('localhost')) { domain = 'http://localhost:8000' }

    this.cartFeed = $('.cartFeed')
    this.orderApi = domain + '/api/order/'

    this.productFeed = $('.productFeed')
    this.productsApi = domain + '/api/products/'

    this.populateCartFeed()
    this.populateProductFeed()

    // this.addToCartTrigger = $('.addToCart')
    // console.log(this.addToCartTrigger)
    this.addToCartTrigger = $('<button class="btn btn-primary addToCart">Add</button>')

    // this.events()
  }


  /* events() {
    this.addToCartTrigger.on("click", this.addToCart.bind(this))
  } */


  addToCart() {
    console.log('working')
  }


  populateProductFeed() {
    var that = this

    that.productFeed.each(function() {
      var sort = $(this).data('sort')
      var amount = parseInt($(this).data('amount'))

      fetch(that.productsApi + '?ordering=' + sort)
      .then((resp) => resp.json())
      .then(function(data) {

        var products = data.slice(0,amount)

        for (var i in products) {

          that.productFeed.append(`
              <div class="mt-4">
                <h6>Product feed ${i}</h6>
                <div class="d-flex">
                  <img src="${products[i].image}" class="img img-fluid" alt="test" style="height: 5em;">
                  <div class="mx-3">
                    name: ${products[i].name}<br>
                    price: ${products[i].price}
                  </div>
                  <div>
                    ${that.addToCartTrigger[0].outerHTML}
                  </div>
                </div>
              </div>
            `)

          // Make this stuff work!!
          $('.addToCart').on("click", function(){console.log('working')})

        }
      })
    })
  }


  populateCartFeed() {
    var that = this

    fetch(that.orderApi)
    .then((resp) => resp.json())
    .then(function(data) {

      var orders = data
      for (var i in orders) {

        if (orders[i].status == 1) {

          var cart = orders[i].items
          for (var c in cart) {

            that.cartFeed.append(`
                <div>
                  <h6>Cart product ${c}</h6>
                  name: ${cart[c].product.name}<br>
                  price: ${cart[c].product.price}<br>
                  amount: ${cart[c].quantity}
                </div>
              `)

          }
        }

      }


    })
  }
}

export default Test;
