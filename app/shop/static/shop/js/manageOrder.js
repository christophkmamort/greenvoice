import $ from 'jquery'

import * as populateOrderList from './populateOrderList.js'


export function updateOrderManager(args) {
  /*
  Manage order actions.
  */
  var action = args['currentElem'].data('action')
  var api_order = home_url + '/api/order/'
  var order_item_id = args['order_item_id']

  var argsUpdateOrderManager = {
    'api_order':api_order,
    'api_order_detail':api_order + args['order_id'] + '/',
    'api_order_item':home_url + '/api/order-item/',
    'api_order_item_detail':home_url + '/api/order-item/' + order_item_id + '/',
    'order_item_quantity':args['order_item_quantity'],
    'order_items_length':args['order_items_length'],
    'product_option_id':args['product_option_id'],
  }

  if (action == 'add') {
    if (order_item_id) {
      /*
      Increase order-item quantity by one.
      */
      increaseOrderItemQuantity(argsUpdateOrderManager)

    } else {
      /*
      Create new order item.
      */
      if (user != 'AnonymousUser') {
        var filter = '?status=1'
        fetch(api_order + filter)
        .then((resp) => resp.json())
        .then(function(data) {
          var orders = data

          if (orders.length == 0) {
            createOrder(argsUpdateOrderManager)

          } else {
            var order_id = orders[0].id
            args['order_id'] += order_id
            createOrderItem(argsUpdateOrderManager)

          }
        })
        .catch(function(error) {
          console.log(error)
        })
      }
    }

  } else if (action == 'remove') {
    /*
    Decrease order-item quantity by one/delete order-item/delete order.
    */
    decreaseOrderItemQuantity(argsUpdateOrderManager)

  } else if (action == 'delete') {
    /*
    Delete order-item/delete order.
    */
    deleteOrderItem(argsUpdateOrderManager)

  }
}


function createOrderItem(args) {
  /*
  Create new order-item.
  */
  if (user != 'AnonymousUser') {
    var api_order_item = args['api_order_item']
    var order_id = args['order_id']
    var product_option_id = args['product_option_id']

    var filter = '?product_option=' + product_option_id
    fetch(api_order_item + filter)
    .then((resp) => resp.json())
    .then(function(data) {
      var order_items = data

      if (order_items.length > 0) {
        var order_item = order_items[0]
        args['api_order_item_detail'] = api_order_item + order_item.id + '/'
        args['order_item_quantity'] = order_item.quantity
        increaseOrderItemQuantity(args)

      } else {
        fetch(api_order_item, {
          method:'POST',
          headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
          },
          body:JSON.stringify({
            'order':order_id,
            'product_option':product_option_id,
            'quantity':1,
          })
        })
        .then((resp) => resp.json())
        .then(function(response) {
          populateOrderList.populateAllOrderCounts()
          populateOrderList.populateAllOrderLists()
          populateOrderList.populateAllOrderTotals()
        })
        .catch(function(error) {
          console.log(error)
        })

      }
    })
    .catch(function(error) {
      console.log(error)
    })
  }
}


function createOrder(args) {
  /*
  Create new order.
  */
  var api_order = args['api_order']

  fetch(api_order, {
    method:'POST',
    headers:{
      'Content-type':'application/json',
      'X-CSRFToken':csrftoken,
    },
  })
  .then((resp) => resp.json())
  .then(function(response) {
    args['order_id'] = response.id
    createOrderItem(args)
  })
  .catch(function(error) {
    console.log(error)
  })
}


function increaseOrderItemQuantity(args) {
  /*
  Increase order-item quantity by one.
  */
  if (user != 'AnonymousUser') {
    var api_order_item_detail = args['api_order_item_detail']
    var order_item_quantity = args['order_item_quantity'] + 1

    fetch(api_order_item_detail, {
      method:'PUT',
      headers:{
        'Content-type':'application/json',
        'X-CSRFToken':csrftoken,
      },
      body:JSON.stringify({
        'quantity':order_item_quantity,
      })
    })
    .then((resp) => resp.json())
    .then(function(response) {
      populateOrderList.populateAllOrderCounts()
      populateOrderList.populateAllOrderLists()
      populateOrderList.populateAllOrderTotals()
    })
    .catch(function(error) {
      console.log(error)
    })
  }
}


function decreaseOrderItemQuantity(args) {
  var order_item_quantity = args['order_item_quantity'] - 1

  if (order_item_quantity == 0) {
    /*
    Delete order/order-item.
    */
    deleteOrderItem(args)

  } else {
    /*
    Decrease order-item quantity by one.
    */
    if (user != 'AnonymousUser') {
      var api_order_item_detail = args['api_order_item_detail']

      fetch(api_order_item_detail, {
        method:'PUT',
        headers:{
          'Content-type':'application/json',
          'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
          'quantity':order_item_quantity,
        })
      })
      .then((resp) => resp.json())
      .then(function(response) {
        populateOrderList.populateAllOrderCounts()
        populateOrderList.populateAllOrderLists()
        populateOrderList.populateAllOrderTotals()
      })
      .catch(function(error) {
        console.log(error)
      })
    }
  }
}


function deleteOrderItem(args) {
  if (user != 'AnonymousUser') {
    /*
    Delete order-item/delete order.
    */
    var order_items_length = args['order_items_length'] - 1
    if (order_items_length == 0) {
      /*
      Delete order.
      */
      deleteOrder(args)

    } else {
      /*
      Delete order-item.
      */
      var api_order_item_detail = args['api_order_item_detail']

      fetch(api_order_item_detail, {
        method:'DELETE',
        headers:{
          'Content-type':'application/json',
          'X-CSRFToken':csrftoken,
        },
      })
      .then(function(response) {
        populateOrderList.populateAllOrderCounts()
        populateOrderList.populateAllOrderLists()
        populateOrderList.populateAllOrderTotals()
      })
      .catch(function(error) {
        console.log(error)
      })
    }
  }
}


function deleteOrder(args) {
  /*
  Delete order.
  */
  var api_order_detail = args['api_order_detail']

  fetch(api_order_detail, {
    method:'DELETE',
    headers:{
      'Content-type':'application/json',
      'X-CSRFToken':csrftoken,
    },
  })
  .then(function(response) {
    populateOrderList.populateAllOrderCounts()
    populateOrderList.populateAllOrderLists()
    populateOrderList.populateAllOrderTotals()
  })
  .catch(function(error) {
    console.log(error)
  })
}
