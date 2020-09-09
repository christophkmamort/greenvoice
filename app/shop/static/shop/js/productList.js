import $ from 'jquery';
import Cookies from 'js-cookie';

class ProductList {
  constructor() {
    this.productList = $('.productList')

    if (this.productList.length > 0) {
      this.product_manager_api = home_url + '/api/product-manager/'
      this.productAmount = $('.productAmount')

      this.populateProductList()
    }
  }

  populateProductList() {
    var that = this

    that.productList.each(function() {
      var currentProductList = $(this)
      var amount = currentProductList.data('amount')
      var style = currentProductList.data('style')
      var ordering = currentProductList.data('ordering')
      if (!ordering) {
        ordering = '-value'
      }

      var filter = ''
      var active_filters = 0
      if (url_params.get('ordering')) {
        ordering = url_params.get('ordering')
        active_filters += 1
      }
      if (url_params.get('category__name')) {
        filter += '&category__name=' + url_params.get('category__name')
      }
      if (url_params.get('brand__name__in')) {
        filter += '&brand__name__in=' + url_params.get('brand__name__in')
        active_filters += 1
      }
      if (url_params.get('price__lte')) {
        filter += '&price__lte=' + url_params.get('price__lte')
        active_filters += 1
      }
      if (url_params.get('price__gte')) {
        filter += '&price__gte=' + url_params.get('price__gte')
        active_filters += 1
      }

      var gender = ''
      if (Cookies.get('user_group') == 'unisex') {
        gender += '&gender__in=1'
      } else if (Cookies.get('user_group') == 'women') {
        gender += '&gender__in=1,2'
      } else if (Cookies.get('user_group') == 'men') {
        gender += '&gender__in=1,3'
      }

      var search = ''
      if (url_params.get('search')) {
        search += '&search=' + url_params.get('search')
      }

      fetch(that.product_manager_api + '?ordering=' + ordering + filter + gender + search + '&product__status=2&product__brand__status=2')
      .then((resp) => resp.json())
      .then(function(data) {
        if (amount && amount.length > 0) {
          var product_managers = data.slice(0,amount)
        } else {
          var product_managers = data
        }

        if (product_managers.length == 1) {
          that.productAmount.html(product_managers.length + ' Produkt')
        } else {
          that.productAmount.html(product_managers.length + ' Produkte')
        }

        for (var i in product_managers) {
          var product_manager = product_managers[i]
          var porduct_color = product_manager.color.name
          var product_options = product_manager.product_option
          var product_option_prices = []
          var product_option_sizes = []
          for (var x in product_options) {
            var product_option = product_options[x]
            product_option_prices.push(product_option.gross)
            product_option_sizes.push(product_option.size.name)
          }
          product_option_prices.sort(function(a, b) { return a-b })
          var product_price_from = product_option_prices[0]
          var product_price_info = ''
          if (product_option_prices[0] < product_option_prices[-1]) {
            product_price_info = 'ab '
          }
          var images = product_manager.image[0]
          if (images) {
            var title_image = images.image
          }
          if (!title_image) {
            var images = product_manager.brand_image[0]
            if (images) {
              var title_image = images.image
            }
          }

          if (title_image && product_manager.product.name && product_price_from) {
            if (style == 'slide') {
              var product_wrapper_class = 'feed-product feed-product-slide'
            } else {
              var product_wrapper_class = 'feed-product mb-4'
            }

            if (user == 'AnonymousUser') {
              var wishlist_trigger = `
                <a href="${ login_url }">
                  <button class="btn position-absolute p-1 bg-white-50 circle" style="top: 0.25em; right: 0.25em;">
                    <svg class="bi bi-heart text-dark" height="1.5em" viewBox="0 0 26.593 25.22" xmlns="http://www.w3.org/2000/svg"><path d="M12.267,2.015c6.8-7,23.819,5.246,0,20.985C-11.552,7.262,5.462-4.98,12.267,2.015Z" transform="translate(1.03 1.022)" fill="none" stroke="currentColor" stroke-width="2" fill-rule="evenodd"/></svg>
                  </button>
                </a>
              `
            } else {

              if (1 == 0) {
                var wishlist_trigger = `
                  <button class="btn position-absolute p-1 bg-white-50 circle updateWishlist" data-action="delete" style="top: 0.25em; right: 0.25em;">
                    <svg class="bi bi-heart text-primary" height="1.5em" viewBox="0 0 26.593 25.22" xmlns="http://www.w3.org/2000/svg"><path d="M12.267,2.015c6.8-7,23.819,5.246,0,20.985C-11.552,7.262,5.462-4.98,12.267,2.015Z" transform="translate(1.03 1.022)" fill="currentColor" stroke="currentColor" stroke-width="2" fill-rule="evenodd"/></svg>
                  </button>
                `
              } else {
                var wishlist_trigger = `
                  <button class="btn position-absolute p-1 bg-white-50 circle updateWishlist" data-action="add" style="top: 0.25em; right: 0.25em;">
                    <svg class="bi bi-heart text-dark" height="1.5em" viewBox="0 0 26.593 25.22" xmlns="http://www.w3.org/2000/svg"><path d="M12.267,2.015c6.8-7,23.819,5.246,0,20.985C-11.552,7.262,5.462-4.98,12.267,2.015Z" transform="translate(1.03 1.022)" fill="none" stroke="currentColor" stroke-width="2" fill-rule="evenodd"/></svg>
                  </button>
                `
              }
            }

            var html = `
              <div class="${ product_wrapper_class }">
                <div class="overflow-hidden position-relative feed-product-img">
                  <a href="${ product_url + product_manager.id }">
                    <div class="position-absolute" style="left: 0; top: 0; right: 0; bottom: 0;">
                      <img class="img w-100 h-100" src="${ title_image }" alt="">
                    </div>
                  </a>

                  <div class="wishlist_triggerWrapper">
                    ${ wishlist_trigger }
                  </div>
                </div>
                <a href="${ product_url + product_manager.id }" class="text-decoration-none">
                  <div class="pt-2 pr-2 pl-2">
                    <p class="m-0 p-0 mt-1">${ product_manager.product.name }</p>
                    <h6 class="m-0 p-0 mt-1 text-small"><span class="text-dark text-strong">${ product_price_info }€ ${ product_price_from }</span></h6>
                  </div>
                </a>
              </div>
              `
            currentProductList.append(html)
          }
        }
      })
    })
  }
}

export default ProductList;
