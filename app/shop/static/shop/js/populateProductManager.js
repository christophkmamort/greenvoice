import $ from 'jquery'

import * as manageWishlist from './manageWishlist.js'
import * as manageOrder from './manageOrder.js'


// Constructor.
var productList = $('.productList')
if (productList) {
  populateProductList()
}

var productCount = $('.productCount')
if (productCount) {
  populateProductCount()
}


// Functions.
function apiCallProductManger(args) {
  /*
  Api call to get matching product-managers.
  */
  var api_product_manager = home_url + '/api/product-manager/'
  var currentElem = args['currentElem']
  var filter = ''

  var currentElemOrder = currentElem.data('order')
  if (!currentElemOrder) {
    currentElemOrder = '-value'
  }
  filter += '?ordering=' + currentElemOrder

  return fetch(api_product_manager + filter)
  .then((resp) => resp.json())
  .catch(function(error) {
    console.log(error)
  })
}


function populateProductCount() {
  /*
  Populate product-count with number of matching product-managers from api call.
  */
  productCount.each(function() {
    var currentElem = $(this)
    var args = {
      'currentElem':currentElem,
    }

    currentElem.html('')

    apiCallProductManger(args).then(function(data) {
      var product_managers = data

      if (product_managers.length > 0) {
        currentElem.html(product_managers.length)
      }
    })
  })
}


function populateProductList(args) {
  /*
  Populate product-list with matching product-managers from api call.
  */
  productList.each(function(index) {
    var currentElem = $(this)
    var args = {
      'currentElem':currentElem,
    }

    currentElem.html('')

    apiCallProductManger(args).then(function(data) {
      var product_managers = data

      if (product_managers.length > 0) {
        var currentElemQuantity = currentElem.data('quantity')
        var index = args['index']
        if (currentElemQuantity) { // TODO: Find way to query this in api call (speed).
          /*
          Only display specified amount of products.
          */
          var product_managers = data.slice(0,currentElemQuantity)
        }

        for (var i in product_managers) {
          var product_manager = product_managers[i]
          var product_options = product_manager.product_option

          if (product_options) {
            /*
            Get product options from product-manager.
            */
            var product_option_gross_prices = []
            var product_option_sizes = []
            var product_option_ids = []

            for (var x in product_options) {
              var product_option = product_options[x]
              var product_status = product_option.status

              if (product_status == 2) { // Add logic to check stock (if stock management is on).
                var product_option_gross = product_option.gross
                if (product_option_gross) {
                  product_option_gross_prices.push(product_option_gross)
                }
                var product_option_size = product_option.size.name
                if (product_option_gross && product_option_size) {
                  product_option_sizes.push(product_option_size)
                  product_option_ids.push(product_option.id)
                }
              }
            }

            if (product_option_gross_prices.length > 0 && product_option_sizes.length > 0) {
              /*
              Get product images from product-manager.
              */
              var product_images = product_manager.image
              if (product_images.length > 0) {
                var product_title_image = product_images[0].image
              } else {
                var product_brand_images = product_manager.brand_image
                if (product_brand_images.length > 0) {
                  var product_title_image = product_brand_images[0].image
                }
              }

              if (product_title_image) {
                /*
                Get all product details from product-manager.
                */
                var porduct_color = product_manager.color.name
                product_option_gross_prices.sort(function(a, b) { return a-b })
                var product_gross_from = product_option_gross_prices[0]
                var product_gross_info = ''
                if (product_option_gross_prices.length > 1 && product_gross_from != product_option_gross_prices[-1]) {
                  product_gross_info = 'ab '
                }
                var product_manager_id = product_manager.id
                var product_name = product_manager.product.name
                var product_url = home_url + '/shop/product/' + product_manager.id

                if (porduct_color && product_name) {
                  /*
                  Display product data in current product list.
                  */
                  var product_wrapper_class = 'feed-product mb-4'
                  var product_in_wishlist = product_manager.wishlist_item
                  if (product_in_wishlist.length > 0) {
                    var product_wishlist_item_id = product_in_wishlist[0]
                  }

                  var currentElemStyle = currentElem.data('style')
                  if (currentElemStyle == 'slide') {
                    /*
                    Html classes for product slide.
                    */
                    product_wrapper_class = 'feed-product feed-product-slide'
                  }

                  var html = `
                    <div class="${ product_wrapper_class }">
                      <div class="overflow-hidden position-relative feed-product-img">
                        <a href="${ product_url }">
                          <div class="position-absolute" style="left: 0; top: 0; right: 0; bottom: 0;">
                            <img class="img w-100 h-100" src="${ product_title_image }" alt="">
                          </div>
                        </a>

                        <div class="position-absolute updateWishlistTriggerWrapper" data-unique="productList${ product_manager_id }" style="top:0.5em; right:0.5em;">
                        </div>
                      </div>
                      <a href="${ product_url }" class="text-decoration-none">
                        <div class="pt-2 pr-2 pl-2">
                          <p class="m-0 p-0 mt-1">${ product_name }</p>
                          <h6 class="m-0 p-0 mt-1 text-small"><span class="text-dark text-strong">${ product_gross_info }€ ${ product_gross_from }</span></h6>
                          </div>
                        </div>
                      </a>

                      <div class="d-flex updateOrderTriggerWrapper" data-unique="productList${ product_manager_id }">
                      </div>
                    </div>
                  `
                  currentElem.append(html)

                  var updateOrderTriggerWrapper = $(`.updateOrderTriggerWrapper[data-unique="productList${ product_manager_id }"]`)
                  var argsPopulateUpdateOrderTrigger = {
                    'currentElem':updateOrderTriggerWrapper,
                    'product_option_sizes':product_option_sizes,
                    'product_option_ids':product_option_ids,
                  }
                  populateUpdateOrderTriggerWrapper(argsPopulateUpdateOrderTrigger)

                  var updateWishlistTriggerWrapper = $(`.updateWishlistTriggerWrapper[data-unique="productList${ product_manager_id }"]`)
                  var argsPopulateUpdateWishlistTrigger = {
                    'currentElem':updateWishlistTriggerWrapper,
                    'product_manager_id':product_manager_id,
                    'product_wishlist_item_id':product_wishlist_item_id,
                  }
                  populateUpdateWishlistTriggerWrapper(argsPopulateUpdateWishlistTrigger)
                }
              }
            }
          }
        }
      }
    })
  })
}


export function populateUpdateOrderTriggerWrapper(args) {
  /*
  Populate and manage populateUpdateOrderTriggerWrapper.
  */
  var currentElem = args['currentElem']
  var product_options_html = ''
  var product_option_ids = args['product_option_ids']
  var product_option_sizes = args['product_option_sizes']

  for (var i in product_option_sizes) {
    var product_option_size = product_option_sizes[i]
    var product_option_id = product_option_ids[i]

    product_options_html += `
      <label class="checkbox form-check m-0 p-1 pt-1">
        <input class="form-check-input" type="radio" name="productOption" value="${ product_option_id }" data-option="${ product_option_size }">
        <h6 class="checkbox-text checkbox-text-strong m-0 ml-2 text-regular text-small">${ product_option_size }</h6>
      </label>
    `
  }

  var html = `
    <div class="dropdown">
      <button id="productOptionIndicator" class="btn btn-sm btn-outline-info dropdown-toggle productOptionIndicator" type="button" data-toggle="dropdown">Größe</button>
      <div class="dropdown-menu border border-info p-0" aria-labelledby="productOptionIndicator">
        ${ product_options_html }
      </div>
    </div>
    <button class="ml-2 btn btn-sm btn-primary updateOrderTrigger" data-action="add">In den Warenkorb</button>
  `
  currentElem.html(html)

  /*
  Display current selected size.
  */
  var productOptionIndicator = currentElem.find('.productOptionIndicator')
  var productOptionInput = currentElem.find('input[name="productOption"]')
  productOptionInput.change(function() {
    if($(this).is(':checked')) {
      productOptionIndicator.removeClass('btn-outline-info').removeClass('btn-outline-danger').addClass('btn-outline-primary')
      productOptionIndicator.html($(this).data('option'))
    }
  })

  /*
  Trigger manageOrder.
  */
  var updateOrderTrigger = currentElem.find('.updateOrderTrigger')
  updateOrderTrigger.on("click", (function() {
    return function(e) {
      var action = updateOrderTrigger.data('action')
      var product_option_id = currentElem.find('input[name="productOption"]:checked').val()
      if (!product_option_id) {
        productOptionIndicator.removeClass('btn-outline-info').addClass('btn-outline-danger')
        return
      } else {
        productOptionIndicator.removeClass('btn-outline-danger').addClass('btn-outline-info')
      }

      var args = {
        'action':action,
        'currentElem':updateOrderTrigger,
        'product_option_id':product_option_id,
      }
      manageOrder.updateOrder(args)
    }
  })())
}


export function populateUpdateWishlistTriggerWrapper(args) {
  /*
  Populate and manage updateWishlistTriggerWrapper.
  */
  var currentElem = args['currentElem']
  var product_manager_id = args['product_manager_id']
  var product_wishlist_item_id = args['product_wishlist_item_id']

  var wishlist_html = ''
  if (user == 'AnonymousUser') {
    wishlist_html += `<a href="${ login_url }">`
  }
  wishlist_html += `
    <button class="btn p-0 wishlist updateWishlistTrigger" data-unique="productList${ product_manager_id }" data-action="add">
      <svg class="bi bi-heart text-dark wishlist__icon wishlist__icon--outline" viewBox="0 0 26.593 25.22" xmlns="http://www.w3.org/2000/svg"><path d="M12.267,2.015c6.8-7,23.819,5.246,0,20.985C-11.552,7.262,5.462-4.98,12.267,2.015Z" transform="translate(1.03 1.022)" fill="none" stroke="currentColor" stroke-width="2" fill-rule="evenodd"/></svg>
      <svg class="bi bi-heart text-primary wishlist__icon wishlist__icon--filled d-none" viewBox="0 0 26.593 25.22" xmlns="http://www.w3.org/2000/svg"><path d="M12.267,2.015c6.8-7,23.819,5.246,0,20.985C-11.552,7.262,5.462-4.98,12.267,2.015Z" transform="translate(1.03 1.022)" fill="currentColor" stroke="currentColor" stroke-width="2" fill-rule="evenodd"/></svg>
    </button>
  `
  if (user == 'AnonymousUser') {
    wishlist_html += `</a>`

  } else if (product_wishlist_item_id) {
    wishlist_html = `
      <button class="btn p-0 wishlist updateWishlistTrigger" data-unique="productList${ product_manager_id }" data-action="delete">
        <svg class="bi bi-heart text-primary wishlist__icon wishlist__icon--filled" viewBox="0 0 26.593 25.22" xmlns="http://www.w3.org/2000/svg"><path d="M12.267,2.015c6.8-7,23.819,5.246,0,20.985C-11.552,7.262,5.462-4.98,12.267,2.015Z" transform="translate(1.03 1.022)" fill="currentColor" stroke="currentColor" stroke-width="2" fill-rule="evenodd"/></svg>
      </button>
    `
  }
  currentElem.html(wishlist_html)

  /*
  Trigger manageWishlist.
  */
  var updateWishlistTriggerWrapper = currentElem
  var updateWishlistTrigger = $(`.updateWishlistTrigger[data-unique="productList${ product_manager_id }"]`)
  updateWishlistTrigger.on("click", (function(updateWishlistTrigger, updateWishlistTriggerWrapper, product_manager_id) {
    return function(e) {
      var action = updateWishlistTrigger.data('action')
      var args = {
        'action':action,
        'currentElem':updateWishlistTriggerWrapper,
        'product_manager_id':product_manager_id,
        'product_wishlist_item_id':product_wishlist_item_id,
      }
      manageWishlist.updateWishlist(args)
    }
  })(updateWishlistTrigger, updateWishlistTriggerWrapper, product_manager_id))
}
