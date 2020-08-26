import $ from 'jquery';

class ProductList {
  constructor() {
    this.productList = $('.productList')

    if (this.productList.length > 0) {
      this.product_api = domain + '/api/products/'
      this.productAmount = $('.productAmount')

      this.populateProductList()
    }
  }

  populateProductList() {
    var that = this
    var i_tag = ''
    var i_tag_close = ''

    if (current_url.includes('Sport')) {
      var i_tag = '<i>'
      var i_tag_close = '</i>'
    }

    that.productList.each(function() {
      var currentProductList = $(this)
      var amount = currentProductList.data('amount')
      var sort = currentProductList.data('sort')
      var style = currentProductList.data('style')

      if (style == 'slide') {
        var product_wrapper_class = 'feed-product feed-product-slide'

        // currentProductList.append('<div class="feed-padding-left"></div>')
      } else {
        var product_wrapper_class = 'feed-product mb-4'
      }

      var filter = ''
      if (url_params.get('category')) {
        filter = '&category=' + url_params.get('category')
      }

      fetch(that.product_api + '?ordering=' + sort + filter)
      .then((resp) => resp.json())
      .then(function(data) {
        if (amount && amount.length > 0) {
          var products = data.slice(0,amount)
        } else {
          var products = data
        }

        if (products.length == 1) {
          that.productAmount.html(products.length + ' Produkt')
        } else {
          that.productAmount.html(products.length + ' Produkte')
        }

        for (var i in products) {
          var product = products[i]

          if (product.status == 2) {
            if (user == 'AnonymousUser') {
              var wishlistTrigger = `
                <a href="${ login_url }">
                  <button class="btn position-absolute p-1 bg-white-50 circle" style="top: 0.25em; right: 0.25em;">
                    <svg class="bi bi-heart text-dark" height="1.5em" viewBox="0 0 26.593 25.22" xmlns="http://www.w3.org/2000/svg"><path d="M12.267,2.015c6.8-7,23.819,5.246,0,20.985C-11.552,7.262,5.462-4.98,12.267,2.015Z" transform="translate(1.03 1.022)" fill="none" stroke="currentColor" stroke-width="2" fill-rule="evenodd"/></svg>
                  </button>
                </a>
              `
            } else {

              if (1 == 0) {
                var wishlistTrigger = `
                  <button class="btn position-absolute p-1 bg-white-50 circle updateWishlist" data-action="delete" style="top: 0.25em; right: 0.25em;">
                    <svg class="bi bi-heart text-primary" height="1.5em" viewBox="0 0 26.593 25.22" xmlns="http://www.w3.org/2000/svg"><path d="M12.267,2.015c6.8-7,23.819,5.246,0,20.985C-11.552,7.262,5.462-4.98,12.267,2.015Z" transform="translate(1.03 1.022)" fill="currentColor" stroke="currentColor" stroke-width="2" fill-rule="evenodd"/></svg>
                  </button>
                `
              } else {
                var wishlistTrigger = `
                  <button class="btn position-absolute p-1 bg-white-50 circle updateWishlist" data-action="add" style="top: 0.25em; right: 0.25em;">
                    <svg class="bi bi-heart text-dark" height="1.5em" viewBox="0 0 26.593 25.22" xmlns="http://www.w3.org/2000/svg"><path d="M12.267,2.015c6.8-7,23.819,5.246,0,20.985C-11.552,7.262,5.462-4.98,12.267,2.015Z" transform="translate(1.03 1.022)" fill="none" stroke="currentColor" stroke-width="2" fill-rule="evenodd"/></svg>
                  </button>
                `
              }
            }

            var html = `
              <div class="${ product_wrapper_class }">
                <div class="overflow-hidden position-relative feed-product-img">
                  <a href="${ product_url + product.id }">
                    <div class="position-absolute" style="left: 0; top: 0; right: 0; bottom: 0;">
                      <img class="img w-100 h-100" src="${ product.image }" alt="">
                    </div>
                  </a>

                  <div class="wishlistTriggerWrapper">
                    ${ wishlistTrigger }
                  </div>
                </div>
                <a href="${ product_url + product.id }" class="text-decoration-none">
                  <div class="pt-2 pr-2 pl-2">
                    <p class="m-0 p-0 mt-1">${ i_tag + product.name + i_tag_close }</p>
                    <h6 class="m-0 p-0 mt-1 text-small"><span class="text-dark text-strong">€ ${ product.price }</span></h6>
                  </div>
                </a>
              </div>
              `
            currentProductList.append(html)
          }
        }
      })

      if (style == 'slide') {
        currentProductList.append('<div class="feed-padding-right"></div>')
      }
    })
  }
}

export default ProductList;
