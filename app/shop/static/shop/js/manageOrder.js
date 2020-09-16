import $ from 'jquery'

import * as populateOrderList from './populateOrderList.js'


export function updateOrderManager(args) {
  var action = args['action']
  var currentElem = args['currentElem']
  var order_api = home_url + '/api/order/'
  var order_item_api = home_url + '/api/order-item/'
  var product_option_id = args['product_option_id']
  // home_url + '/api/order-item/' + args['order_item_id'] + '/'

    var oder_item_id = args['oder_item_id']

    if (action == 'add') {
      if (oder_item_id) {
        /*
        Increase order-item quantity.
        */
        var order_item_quantity = args['order_item_quantity'] + 1
        fetch(order_item_api + order_item_id + '/', {
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
          populateOrderList.populateOrderCount()
          populateOrderList.populateOrderList()
        })
        .catch(function(error) {
          console.log(error)
        })


      } else {
        /*
        Create new order item.
        */
        var filter = '?status=1'
        fetch(order_api + filter)
        .then((resp) => resp.json())
        .then(function(data) {
          var orders = data

          if (orders.length == 0) {
            fetch(order_api, {
              method:'POST',
              headers:{
                'Content-type':'application/json',
                'X-CSRFToken':csrftoken,
              },
            })
            .then((resp) => resp.json())
            .then(function(response) {
              var order_id = response.id

              fetch(order_item_api, {
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
                populateOrderList.populateOrderCount()
                populateOrderList.populateOrderList()
              })
              .catch(function(error) {
                console.log(error)
              })
            })
            .catch(function(error) {
              console.log(error)
            })

          } else {
            var order_id = orders[0].id

            fetch(order_item_api, {
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
              populateOrderList.populateOrderCount()
              populateOrderList.populateOrderList()
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

}


function createOrderItem(args) {
  if (user != 'AnonymousUser') {
    
  }
}


function createOrder(args) {

}


function increaseOrderItemQuantity(args) {
  /*
  Increase order-item quantity by one.
  */
  if (user != 'AnonymousUser') {
    var api_order_item = args['api_order_item']
    var order_item_quantity = args['order_item_quantity'] + 1

    fetch(api_order_item, {
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
      populateOrderList.populateOrderCount()
      populateOrderList.populateOrderList()
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
      var api_order_item = args['api_order_item']

      fetch(api_order_item, {
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
        populateOrderList.populateOrderCount()
        populateOrderList.populateOrderList()
      })
      .catch(function(error) {
        console.log(error)
      })
    }
  }
}


function deleteOrderItem(args) {
  var order_items_length = args['order_items_length'] - 1

  if (user != 'AnonymousUser') {
    if (order_items_length == 0) {
      /*
      Delete complete order.
      */
      deleteOrder(args)

    } else {
      /*
      Delete order-item.
      */
      var api_order_item = args['api_order_item']

      fetch(api_order_item, {
        method:'DELETE',
        headers:{
          'Content-type':'application/json',
          'X-CSRFToken':csrftoken,
        },
      })
      .then(function(response) {
        populateOrderList.populateOrderCount()
        populateOrderList.populateOrderList()
      })
      .catch(function(error) {
        console.log(error)
      })
    }
  }
}


function deleteOrder(args) {
  /*
  Delete complete order.
  */
  var api_order = args['api_order']

  fetch(api_order, {
    method:'DELETE',
    headers:{
      'Content-type':'application/json',
      'X-CSRFToken':csrftoken,
    },
  })
  .then(function(response) {
    populateOrderList.populateOrderCount()
    populateOrderList.populateOrderList()
  })
  .catch(function(error) {
    console.log(error)
  })
}
