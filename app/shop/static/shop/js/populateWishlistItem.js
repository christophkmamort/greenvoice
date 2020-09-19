import $ from 'jquery'

import * as manageWishlist from './manageWishlist.js'


// Constructor.
var wishlistList = $('.wishlistList')
if (wishlistList) {
  populateWishlistList()
}

var wishlistCount = $('.wishlistCount')
if (wishlistCount) {
  populateWishlistCount()
}


// Functions.
function apiCallWishlistItem(args) {
  /*
  Api call to get all user wishlist-items.
  */
  var api_wishlist_item = home_url + '/api/wishlist-item/'
  var currentElem = args['currentElem']
  var filter = '?ordering=-created'

  return fetch(api_wishlist_item + filter)
  .then((resp) => resp.json())
  .catch(function(error) {
    console.log(error)
  })
}


export function populateWishlistCount() {
  wishlistCount.each(function() {
    var currentElem = $(this)
    var args = {
      'currentElem':currentElem,
    }

    apiCallWishlistItem(args).then(function(data) {
      var wishlist_items = data
      var currentElemStyle = currentElem.data('style')

      currentElem.html('')

      if (currentElemStyle == 'bracket') {
        currentElem.append('(')
        currentElem.removeClass('text-info').addClass('text-primary')
      }

      if (wishlist_items.length > 0) {
        currentElem.append(wishlist_items.length)
        currentElem.addClass('notifier--active')
      } else {
        currentElem.append('0')
        currentElem.removeClass('notifier--active')
      }

      if (currentElemStyle == 'bracket') {
        currentElem.append(')')
      }
    })
  })
}


export function populateWishlistList() {
  wishlistList.each(function() {
    var currentElem = $(this)
    var args = {
      'currentElem':currentElem,
    }

    currentElem.html('')

    if (user != 'AnonymousUser') {
      apiCallWishlistItem(args).then(function(data) {
        var wishlist_items = data

        if (wishlist_items.length > 0) {
          for (var i in wishlist_items) {
            /*
            Get wishlist-item data.
            */
            var wishlist_item = wishlist_items[i]
            var product_manager = wishlist_item.product_manager

            var product_options = product_manager.product_option

            var product_gross_prices = []
            var product_sizes = []

            for (var x in product_options) {
              var product_option = product_options[x]
              var product_status = product_option.status

              if (product_status == 2) { // Add logic to check stock (if stock management is on).
                var product_option_gross = product_option.gross
                if (product_option_gross) {
                  product_gross_prices.push(product_option_gross)
                }
                var product_option_size = product_option.size.name
                if (product_option_size) {
                  product_sizes.push(product_option_size)
                }
              }
            }

            var product_images = product_manager.image
            if (product_images.length > 0) {
              var product_title_image = product_images[0].image
            } else {
              var product_brand_images = product_manager.brand_image
              if (product_brand_images.length > 0) {
                var product_title_image = product_brand_images[0].image
              }
            }

            product_gross_prices.sort(function(a, b) { return a-b })
            var product_gross_from = product_gross_prices[0]
            var product_gross_info = ''
            if (product_gross_prices.length > 1 && product_gross_from != product_gross_prices[-1]) {
              product_gross_info = 'ab '
            }
            var product_manager_id = product_manager.id
            var product_manager_color_hex = product_manager.color.hex
            var product_manager_color_name = product_manager.color.name
            var product_name = product_manager.product.name
            var product_url = home_url + '/shop/product/' + product_manager.id

            var html = `
              <div class="row mt-4">
                <a class="col-auto p-0" style="max-height: 105px; max-width: 70px;" href="${ product_url }">
                  <img src="${ product_title_image }" class="img img-fluid w-100 h-100 rounded" alt="${ product_name }">
                </a>
                <a class="col d-flex align-items-center justiy-content-start ml-2" href="${ product_url }">
                  <div>
                    <h6 class="m-0">${ product_name }</h6>
                    <p>${ product_gross_info }€ ${ product_gross_from }</p>
                    <p class="m-0 mt-3">Farbe: <span style="color: #${ product_manager_color_hex }">${ product_manager_color_name }</span></p>
                  </div>
                </a>
                <div class="col-auto d-flex align-items-center justiy-content-end p-0">
                  <button class="btn updateWishlistTrigger" data-unique="wishlistList${ product_manager_id }" data-action="delete">
                    <svg class="svg svg--sm svg__fill--info" viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M432 32H312l-9.4-18.7A24 24 0 0 0 281.1 0H166.8a23.72 23.72 0 0 0-21.4 13.3L136 32H16A16 16 0 0 0 0 48v32a16 16 0 0 0 16 16h416a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16zM53.2 467a48 48 0 0 0 47.9 45h245.8a48 48 0 0 0 47.9-45L416 128H32z"></path></svg>
                  </button>
                </div>
              </div>
            `
            currentElem.append(html)

            /*
            Trigger manageWishlist.
            */
            var product_wishlist_item_id = wishlist_item.id
            var updateWishlistTriggerWrapper = $(`.updateWishlistTriggerWrapper[data-unique="productList${ product_manager_id }"]`)
            var updateWishlistTrigger = $(`.updateWishlistTrigger[data-unique="wishlistList${ product_manager_id }"]`)
            updateWishlistTrigger.on("click", (function(updateWishlistTrigger, updateWishlistTriggerWrapper, product_manager_id, product_wishlist_item_id) {
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
            })(updateWishlistTrigger, updateWishlistTriggerWrapper, product_manager_id, product_wishlist_item_id))
          }

        } else {
          var html = `
            <p class="text-info">Du hast noch keine Artikel zu deiner Wunschliste hinzugefügt. <svg class="bi bi-heart text-info ml-1" height="1em" style="margin-top: -0.2em;" viewBox="0 0 26.593 25.22" xmlns="http://www.w3.org/2000/svg"><path d="M12.267,2.015c6.8-7,23.819,5.246,0,20.985C-11.552,7.262,5.462-4.98,12.267,2.015Z" transform="translate(1.03 1.022)" fill="none" stroke="currentColor" stroke-width="2" fill-rule="evenodd"/></svg></p>
          `
          currentElem.html(html)
        }
      })

    } else {
      var html = `<h6>Melde dich an um die Wunschliste zu verwenden.</h6>`
      currentElem.html(html)
    }
  })
}
