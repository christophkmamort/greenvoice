import $ from 'jquery'

import * as populateProductManager from './populateProductManager.js'
import * as populateWishlistItem from './populateWishlistItem.js'


// Functions.
export function updateWishlist(args) {
  var action = args['action']
  var currentElem = args['currentElem']
  var product_manager_id = args['product_manager_id']
  var product_wishlist_item_id = args['product_wishlist_item_id']
  var wishlist_item_api = home_url + '/api/wishlist-item/'

  if (user != 'AnonymousUser') {
    if (action == 'add') {
      var product_manager_id = args['product_manager_id']

      fetch(wishlist_item_api, {
        method:'POST',
        headers:{
          'Content-type':'application/json',
          'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
          'product_manager':product_manager_id,
        })
      })
      .then((resp) => resp.json())
      .then(function(response) {
        var args = {
          'currentElem':currentElem,
          'product_manager_id':product_manager_id,
          'product_wishlist_item_id':response.id
        }
        populateProductManager.populateWishlistTriggerWrapper(args)
        populateWishlistItem.populateWishlistCount()
        populateWishlistItem.populateWishlistList()
      })
      .catch(function(error) {
        console.log(error)
      })

    } else if (action = 'delete') {
      var wishlist_item_id = args['wishlist_item_id']

      fetch(wishlist_item_api + product_wishlist_item_id + '/', {
        method:'DELETE',
        headers:{
          'Content-type':'application/json',
          'X-CSRFToken':csrftoken,
        },
      })
      .then(function(response) {
        var args = {
          'currentElem':currentElem,
          'product_manager_id':product_manager_id,
        }
        populateProductManager.populateWishlistTriggerWrapper(args)
        populateWishlistItem.populateWishlistCount()
        populateWishlistItem.populateWishlistList()
      })
      .catch(function(error) {
        console.log(error)
      })
    }
  }
}
