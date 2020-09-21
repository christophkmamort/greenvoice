import $ from 'jquery'

import * as manageOrder from './manageOrder.js'
import * as orderListHtml from './templates/orderList.js'


// Constructor.
var orderCount = $('.orderCount')
if (orderCount.length > 0) {
  populateAllOrderCounts()
}
export function populateAllOrderCounts() {
  orderCount.each(function() {
    var args = {
      'currentElem':$(this),
    }
    populateOrderCount(args)
  })
}


var orderList = $('.orderList')
if (orderList.length > 0) {
  populateAllOrderLists()
}
export function populateAllOrderLists() {
  console.log('running')
  orderList.each(function() {
    var args = {
      'currentElem':$(this),
    }
    populateOrderList(args)
  })
}


var orderTotal = $('.orderTotal')
if (orderTotal.length > 0) {
  populateAllOrderTotals()
}
export function populateAllOrderTotals() {
  orderTotal.each(function() {
    var args = {
      'currentElem':$(this),
    }
    populateOrderTotal(args)
  })
}


// Helper functions.
function apiCallOrder(args) {
  var currentElem = args['currentElem']
  var currentElemType = currentElem.data('type')

  var filter = '?ordering=-created'
  if (currentElemType == 'cart') {
    filter += '&status=1'
  }

  return fetch(home_url + '/api/order/' + filter)
  .then((resp) => resp.json())
  .catch(function(error) {
    console.log(error)
  })
}


// Functions.
export function populateOrderCount(args) {
  var currentElem = args['currentElem']
  var currentElemStyle = currentElem.data('style')
  var currentElemType = currentElem.data('type')

  currentElem.html('')

  if (user != 'AnonymousUser') {
    apiCallOrder(args).then(function(data) {
      var orders = data
      var order_items_quantity = 0

      if (currentElemStyle == 'bracket') {
        currentElem.append('(')
      }

      if (orders.length > 0) {
        for (var i in orders) {
          var order = orders[i]
          var order_items = order.order_items

          if (order_items.length > 0) {
            if (currentElemStyle == 'bracket') {
              currentElem.removeClass('text-info').addClass('text-primary')
            }

            for (var i in order_items) {
              var order_item = order_items[i]
              order_items_quantity += order_item.quantity
            }
            currentElem.append(order_items_quantity).addClass('notifier--active')
          }
        }
      } else {
        /*
        Cart is empty.
        */
        currentElem.append(order_items_quantity).removeClass('notifier--active')
      }

      if (currentElemStyle == 'bracket') {
        currentElem.append(')')
      }
    })
  }
}


export function populateOrderList(args) {
  var currentElem = args['currentElem']
  var currentElemType = currentElem.data('type')

  currentElem.html('')

  if (user != 'AnonymousUser') {
    apiCallOrder(args).then(function(data) {
      var orders = data

      if (orders.length > 0) {
        for (var i in orders) {
          var order = orders[i]
          var order_items = order.order_items

          if (order_items.length > 0) {
            for (var x in order_items) {
              var order_item = order_items[x]
              var order_item_id = order_item.id
              var order_item_quantity = order_item.quantity
              var product_manager = order_item.product_option.product_manager
              var product_option = order_item.product_option

              var product_images = product_manager.image
              if (!product_images.length > 0) {
                var product_images = product_manager.brand_image
              }
              if (product_images) {
                var product_title_image = product_images[0].image
              }

              var args = {
                'order_item_quantity':order_item_quantity,
                'order_item_id':order_item_id,
                'product_name':product_manager.product.name,
                'product_manager_color_hex':product_manager.color.hex,
                'product_manager_color_name':product_manager.color.name,
                'product_option_gross':product_option.gross,
                'product_option_size':product_option.size.name,
                'product_title_image':product_title_image,
                'product_url':home_url + '/shop/product/' + product_manager.id,
              }

              if (currentElemType == 'cart') {
                currentElem.append(orderListHtml.cartItem(args))

                var args = {
                  'order_id':order.id,
                  'order_item_id':order_item_id,
                  'order_item_quantity':order_item_quantity,
                  'order_items_length':order_items.length,
                }
                var updateOrderTriggers = currentElem.find(`.updateOrderTrigger[data-unique="orderList${ order_item_id }"]`)

                updateOrderTriggers.each(function() {
                  var updateOrderTrigger = $(this)
                  updateOrderTrigger.on("click", (function(args) {
                    return function(e) {
                      args['currentElem'] = updateOrderTrigger
                      manageOrder.updateOrderManager(args)
                    }
                  })(args))
                })
              }
            }
          }
        }

      } else {
        /*
        Cart is empty.
        */
        currentElem.append(orderListHtml.cartItemNull(args))
      }
    })
  }
}


export function populateOrderTotal(args) {
  var currentElem = args['currentElem']
  var currentElemType = currentElem.data('type')

  currentElem.html('')

  if (user != 'AnonymousUser') {
    apiCallOrder(args).then(function(data) {
      var orders = data

      if (orders.length > 0) {
        for (var i in orders) {
          var order = orders[i]
          var order_items = order.order_items

          if (order_items.length > 0) {
            var order_total_gross = 0

            for (var x in order_items) {
              var order_item = order_items[x]
              var order_item_gross = order_item.product_option.gross
              var order_item_quantity = order_item.quantity
              order_total_gross += order_item_gross * order_item_quantity
            }

            var args = {
              'order_total_gross':Math.round(order_total_gross * 100) / 100,
            }

            if (currentElemType == 'cart') {
              args['checkout_url'] = home_url + '/shop/checkout'
              currentElem.append(orderListHtml.cartTotal(args))
            }
          }
        }

      } else {
        /*
        Cart is empty.
        */
        var args = {
          'shop_url':shop_url,
        }
        currentElem.append(orderListHtml.cartTotalNull(args))
      }
    })
  }
}
