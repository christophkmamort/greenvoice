import $ from 'jquery'

import * as manageWishlist from './manageWishlist.js'
import * as manageOrder from './manageOrder.js'
import * as productListHtml from './templates/productList.js'


// Constructor.
var productList = $('.productList')
if (productList) {
  populateAllProductLists()
}
export function populateAllProductLists() {
  productList.each(function(index) {
    var args = {
      'currentElem':$(this),
      'index':index,
    }
    populateProductList(args)
  })
}


var productCount = $('.productCount')
if (productCount) {
  populateAllProductCounts()
}
export function populateAllProductCounts() {
  productCount.each(function() {
    var args = {
      'currentElem':$(this),
    }
    populateProductCount(args)
  })
}


// Helper functions.
function apiCallProductManger(args) {
  /*
  Api call get product-managers.
  */
  var api_product_manager = home_url + '/api/product-manager/'
  var currentElem = args['currentElem']
  var currentElemOrder = '-value'
  var currentElemDataOrder = currentElem.data('order')
  if (currentElemDataOrder) {
    currentElemOrder = currentElemDataOrder
  }

  var filter = '?ordering=' + currentElemOrder
  filter += '&product__brand__status=2' // Check if brand is active.
  filter += '&product_option__status=2' // Check if has active products.
  // TODO: Stock check (filter += '&product_option__stock=')

  return fetch(api_product_manager + filter)
  .then((resp) => resp.json())
  .catch(function(error) {
    console.log(error)
  })
}


// Functions.
function populateProductCount(args) {
  /*
  Display number of matching product-managers for api query.
  */
  var currentElem = args['currentElem']

  currentElem.html('')

  apiCallProductManger(args).then(function(data) {
    var product_managers = data

    if (product_managers.length > 0) {
      currentElem.html(product_managers.length) // + '+'
    }
  })
}


function populateProductList(args) {
  /*
  Populate product-list with matching product-managers from api query.
  */
  var currentElem = args['currentElem']
  var index = args['index']

  currentElem.html('')

  apiCallProductManger(args).then(function(data) {
    var product_managers = data

    if (product_managers.length > 0) {
      var currentElemStyle = currentElem.data('style')
      /*
      ==== ==== ==== ====
      TODO: Find way to query this in api call (speed).
      */
      var currentElemQuantity = currentElem.data('quantity')
      if (currentElemQuantity) {
        product_managers = data.slice(0,currentElemQuantity)
      }
      /*
      End.
      ==== ==== ==== ====
      */

      for (var i in product_managers) {
        var product_manager = product_managers[i]

        /*
        Get `product images` from product-manager.
        */
        var product_images = product_manager.image
        var product_title_image = false
        if (product_images.length > 0) {
          product_title_image = product_images[0].image
        } else {
          var product_brand_images = product_manager.brand_image
          if (product_brand_images.length > 0) {
            product_title_image = product_brand_images[0].image
          }
        }

        if (product_title_image) {
          var product_options = product_manager.product_option

          if (product_options) {
            /*
            Retrive product-options.
            */
            var product_options_gross_array = []
            var product_options_size_array = []
            var product_options_id_array = []

            for (var x in product_options) {
              var product_option = product_options[x]
              var product_status = product_option.status

              // TODO: Check stock (if on).
              if (product_status == 2 /* && product_stock_management = false || 
                product_status == 2 && product_stock_management = true && product_stock > 0 */) {
                var product_option_gross = product_option.gross
                var product_option_size = product_option.size.name
                if (product_option_gross && product_option_size) {
                  product_options_gross_array.push(product_option_gross)
                  product_options_size_array.push(product_option_size)
                  product_options_id_array.push(product_option.id)
                }
              }
            }

            if (product_options_gross_array.length > 0 && product_options_size_array.length > 0) {
              /*
              Get all `product details` from product-manager.
              */
              var porduct_color = product_manager.color.name
              product_options_gross_array.sort(function(a, b) { return a-b })
              var product_gross_from = product_options_gross_array[0]
              var product_gross_info_txt = ''
              if (product_options_gross_array.length > 1 && product_gross_from != product_options_gross_array[-1]) {
                product_gross_info_txt = 'ab '
              }
              var product_manager_id = product_manager.id
              var product_name = product_manager.product.name
              var product_url = home_url + '/shop/product/' + product_manager.id

              if (porduct_color && product_name) {
                /*
                Populate currentElem with `product data`.
                */
                var product_in_wishlist = product_manager.wishlist_item
                var product_wishlist_item_id = false
                if (product_in_wishlist.length > 0) {
                  product_wishlist_item_id = product_in_wishlist[0]
                }

                var product_wrapper_class = 'feed-product mb-4'
                if (currentElemStyle == 'slide') {
                  product_wrapper_class = 'feed-product feed-product-slide'
                  if (i == 0) {
                    currentElem.append(productListHtml.marginLeft())
                  }
                }

                var args = {
                  'product_gross_from':product_gross_from,
                  'product_gross_info_txt':product_gross_info_txt,
                  'product_manager_id':product_manager_id,
                  'product_name':product_name,
                  'product_title_image':product_title_image,
                  'product_url':product_url,
                  'product_wrapper_class':product_wrapper_class,
                }
                currentElem.append(productListHtml.productItem(args))

                /*<div class="d-flex updateOrderTriggerWrapper" data-unique="productList${ product_manager_id }">
                </div>*/
                var updateOrderTriggerWrapper = $(`.updateOrderTriggerWrapper[data-unique="productList${ product_manager_id }"]`)
                var argsPopulateUpdateOrderTrigger = {
                  'currentElem':updateOrderTriggerWrapper,
                  'product_options_size_array':product_options_size_array,
                  'product_options_id_array':product_options_id_array,
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

      if (currentElemStyle == 'slide') {
        currentElem.append(productListHtml.marginRight())
      }
    }
  })
}


export function populateUpdateOrderTriggerWrapper(args) {
  /*
  Populate and manage populateUpdateOrderTriggerWrapper.
  */
  var currentElem = args['currentElem']
  var product_options_html = ''
  var product_options_id_array = args['product_options_id_array']
  var product_options_size_array = args['product_options_size_array']

  for (var i in product_options_size_array) {
    var product_option_size = product_options_size_array[i]
    var product_option_id = product_options_id_array[i]

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
      manageOrder.updateOrderManager(args)
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
