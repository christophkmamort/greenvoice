import $ from 'jquery'

import * as manageOrder from './manageOrder.js'


// Constructor.
var orderCount = $('.orderCount')
if (orderCount) {
  populateOrderCount()
}


var orderList = $('.orderList')
if (orderList) {
  populateOrderList()
}


// Helper functions.
function apiCallOrder(args) {
  var api_order = home_url + '/api/order/'
  var currentElem = args['currentElem']
  var filter = '?ordering=-created'

  return fetch(api_order + filter)
  .then((resp) => resp.json())
  .catch(function(error) {
    console.log(error)
  })
}


// Main functions.
export function populateOrderCount() {
  orderCount.each(function() {
    var currentElem = $(this)
    var args = {
      'currentElem':currentElem,
    }

    apiCallOrder(args).then(function(data) {
      var orders = data

      if (orders.length > 0) {
        for (var i in orders) {
          var order = orders[i]
          var order_items = order.order_items

          if (order_items.length > 0) {
            var order_items_quantity = 0
            for (var i in order_items) {
              var order_item = order_items[i]
              order_items_quantity += order_item.quantity
            }
            currentElem.html(order_items_quantity)
            currentElem.addClass('notifier--active')
          } else {
            var empty = true
          }
        }
      } else {
        var empty = true
      }

      if (empty) {
        currentElem.html('0')
        currentElem.removeClass('notifier--active')
      }
    })
  })
}


export function populateOrderList() {
  orderList.each(function() {
    var currentElem = $(this)
    var args = {
      'currentElem':currentElem,
    }

    apiCallOrder(args).then(function(data) {
      var orders = data

      if (orders.length > 0) {
        for (var i in orders) {
          var order = orders[i]
          var order_items = order.order_items
          var order_items_length = order_items.length

          if (order_items_length > 0) {
            currentElem.html('')

            for (var i in order_items) {
              var order_id = order.id
              var order_item = order_items[i]
              var order_item_id = order_item.id
              var order_item_quantity = order_item.quantity
              var product_manager = order_item.product_option.product_manager
              var product_manager_color_hex = product_manager.color.hex
              var product_manager_color_name = product_manager.color.name
              var product_manager_id = product_manager.id
              var product_name = product_manager.product.name
              var product_option = order_item.product_option
              var product_option_gross = product_option.gross
              var product_option_size = product_option.size.name
              var product_url = home_url + '/shop/product/' + product_manager_id

              var product_images = product_manager.image
              if (product_images.length > 0) {
                var product_title_image = product_images[0].image
              } else {
                var product_brand_images = product_manager.brand_image
                if (product_brand_images.length > 0) {
                  var product_title_image = product_brand_images[0].image
                }
              }

              var html = `
                <div class="row">
                  <a class="col-auto p-0" style="max-height: 110px; max-width: 70px;" href="${ product_url }">
                    <img src="${ product_title_image }" class="img img-fluid w-100 h-100 rounded" alt="${ product_name }">
                  </a>
                  <a class="col d-flex align-items-center justiy-content-start ml-2" href="${ product_url }">
                    <div>
                      <h6 class="m-0">${ product_name }</h6>
                      <p class="m-0">${ order_item_quantity }x € ${ product_option_gross }</p>
                      <p class="m-0" style="color: #${ product_manager_color_hex }">Farbe: ${ product_manager_color_name }</p>
                      <p class="m-0">Größe: ${ product_option_size }</p>
                    </div>
                  </a>
                  <div class="col-auto d-flex align-items-center justiy-content-end p-0">
                    <div>
                      <div >
                        <button class="btn w-100 text-strong updateOrderTrigger" data-action="add">+</button>
                      </div>
                      <div>
                        <button class="btn updateOrderTrigger" data-action="delete">
                          <svg class="svg__bg--dark svg__height--medium" viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M432 32H312l-9.4-18.7A24 24 0 0 0 281.1 0H166.8a23.72 23.72 0 0 0-21.4 13.3L136 32H16A16 16 0 0 0 0 48v32a16 16 0 0 0 16 16h416a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16zM53.2 467a48 48 0 0 0 47.9 45h245.8a48 48 0 0 0 47.9-45L416 128H32z"></path></svg>
                        </button>
                      </div>
                      <div>
                        <button class="btn w-100 text-strong updateOrderTrigger" data-action="remove">-</button>
                      </div>
                    </div>
                  </div>
                </div>
              `
              currentElem.append(html)

              /*
              Trigger manageOrder.
              */
              var updateOrderTrigger = currentElem.find('.updateOrderTrigger')
              updateOrderTrigger.each(function() {
                var currentUpdateOrderTrigger = $(this)
                currentUpdateOrderTrigger.on("click", (function() {
                  return function(e) {
                    var action = currentUpdateOrderTrigger.data('action')
                    var args = {
                      'action':action,
                      'currentElem':currentUpdateOrderTrigger,
                      'order_id':order_id,
                      'order_item_id':order_item_id,
                      'order_item_quantity':order_item_quantity,
                      'order_items_length':order_items_length,
                    }
                    manageOrder.updateOrderManager(args)
                  }
                })())
              })
            }

          } else {
            var empty = true
          }
        }
      } else {
        var empty = true
      }

      if (empty) {
        var html = `
          <p class="text-info">
            Du hast noch keine Artikel zu deinem Warenkorb hinzugefügt.
            <svg class="bi bi-bag text-info ml-1" height="1em" style="margin-top: -0.2em;" viewBox="0 0 24.581 26.25" xmlns="http://www.w3.org/2000/svg"><g transform="translate(-2986 -168.75)"><path id="cart" d="M1,6.145H23.581V22.274A3.226,3.226,0,0,1,20.355,25.5H4.226A3.226,3.226,0,0,1,1,22.274Z" transform="translate(2986 168.5)" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12.29,2.113A4.032,4.032,0,0,0,8.258,6.145H6.645a5.645,5.645,0,0,1,11.29,0H16.323A4.032,4.032,0,0,0,12.29,2.113Z" transform="translate(2986 168.5)" fill="currentColor" stroke="currentColor" stroke-width="0.5"/></g></svg>
          </p>
        `
        currentElem.html(html)
      }
    })
  })
}
