import $ from 'jquery';
import Cookies from 'js-cookie';

class Order {
  constructor() {
    this.orderList = $('.orderList')
    if (this.orderList) {
      this.order_api = home_url + '/api/order/'
      this.order_item_api = home_url + '/api/order-item/'

      this.orderCount = $('.orderCount')
      this.orderSum = $('.orderSum')

      this.populateOrderCount()
      this.populateOrderSum()
      this.populateOrderList()
    }
  }


  populateOrderCount() {
    var that = this

    that.orderCount.each(function() {
      var current_elem = $(this)
      current_elem.html('0')

      var current_elem_type = current_elem.data('type')

      if (user != 'AnonymousUser') {
        var filter = ''
        if (current_elem_type == 'cart') {
          /*
          Get draft order.
          */
          filter = '?status=1'
        }

        fetch(that.order_api + filter)
        .then((resp) => resp.json())
        .then(function(data) {
          var orders = data
          if (orders.length > 0) {
            var order = orders[0]
            var order_items = order.order_items
            var order_items_count = ''

            for (var i in order_items) {
              var order_item = order_items[i]
              order_items_count += order_item.quantity
            }

            current_elem.html(order_items_count)

          }
        })

      } else {
        // TODO: Create cookie logic here.
      }
    })
  }


  populateOrderSum() {
    var that = this

    that.orderSum.each(function() {
      var current_elem = $(this)
      current_elem.html('')

      var current_elem_type = current_elem.data('type')

      if (user != 'AnonymousUser') {
        var filter = ''
        if (current_elem_type == 'cart') {
          /*
          Get draft order.
          */
          filter = '?status=1'
        }

        fetch(that.order_api + filter)
        .then((resp) => resp.json())
        .then(function(data) {
          var orders = data
          if (orders.length > 0) {
            var order = orders[0]
            var order_items = order.order_items
            var order_gross = ''
            var order_delivery_gross = 0

            for (var i in order_items) {
              var order_item = order_items[i]
              order_gross += order_item.quantity * order_item.product_option.gross
            }

            var order_total = (parseFloat(order_gross) + parseFloat(order_delivery_gross)).toFixed(2)
            var order_tax_total = ((parseFloat(order_delivery_gross) + parseFloat(order_gross)) * 0.2).toFixed(2)
            order_gross = parseFloat(order_gross).toFixed(2)
            order_delivery_gross = parseFloat(order_delivery_gross).toFixed(2)

            var html = `
              <h6 class="m-0">Summe: € ${ order_gross }</h6>
              <h6 class="m-0">Versandkosten: € ${ order_delivery_gross }</h6>
              <hr class="bg-dark mt-1 mb-1">
              <h5 class="m-0">Gesamtsumme: € ${ order_total }</h5>
              <h6 class="m-0 text-info">inkl. Mwst. i.H.v.: € ${ order_tax_total }</h6>
            `
            current_elem.html(html)

          } else {
            current_elem.html('')
          }
        })

      } else {
        // TODO: Add cookie logic here!!
      }
    })
  }


  populateOrderList() {
    var that = this

    that.orderList.each(function(index) {
      var current_elem = $(this)
      current_elem.html('')

      var current_elem_type = current_elem.data('type')

      if (user != 'AnonymousUser') {
        var filter = ''
        if (current_elem_type == 'cart') {
          /*
          Get draft order.
          */
          filter = '?status=1'
        }

        fetch(that.order_api + filter)
        .then((resp) => resp.json())
        .then(function(data) {
          var orders = data
          if (orders.length > 0) {
            var order = orders[0]
            var order_items = order.order_items
            var order_items_length = order_items.length

            for (var i in order_items) {
              var order_item = order_items[i]
              var product_name = order_item.product_option.product_manager.product.name
              var product_option_gross = order_item.product_option.gross
              var order_item_quantity = order_item.quantity

              var html = `
                <div class="d-flex align-items-center wishlistItem">
                  <h6 class="m-0">${ product_name }</h6>
                  <p class="m-0 ml-2">€ ${ product_option_gross }</p>
                  <p class="m-0 ml-2">(${ order_item_quantity })</p>
                  <button class="btn ml-3 updateOrder" data-unique="orderList${ index + i + '1' }" data-action="add">+</button>
                  <button class="btn btn-sm btn-danger updateOrder" data-unique="orderList${ index + i + '2' }" data-action="delete">Delete</button>
                  <button class="btn updateOrder" data-unique="orderList${ index + i + '3' }" data-action="remove">-</button>
                </div>
              `
              current_elem.append(html)

              var args = {
                'order-item': order_item,
                'order-items-length':order_items_length,
              }

              var x = 0
              while (x < 3) {
                x++
                var updateOrder = $(`.updateOrder[data-unique="orderList${ index + i + x }"]`)
                updateOrder.on("click", (function(e) {
                  var action = $(e.target).data('action')
                  that.updateOrder(e, action, args)
                }))
              }
            }

          }
        })

      } else {
        // TODO: Add logic for guest user (with cookies).
      }
    })
  }

  // https://stackoverflow.com/questions/39175922/how-to-access-a-method-from-a-class-from-another-class
  updateOrder(e, action, args) {
    var that = this

    if (args) {
      if (user != 'AnonymousUser') {

        if (action == 'add') {
          /*
          Add new order-item/increase order-item quantity.
          */
          var filter = '?status=1'
          fetch(that.order_api + filter)
          .then((resp) => resp.json())
          .then(function(data) {
            var orders = data
            if (orders.length > 0) {
              var order = orders[0]
              var order_items = order.order_items
            } else {
              // Create new one!
              console.log('Create new one!')
            }

          })


        } else if (action == 'remove') {
          /*
          Decrease order-item quantity.
          */


        } else if (action == 'delete') {
          /*
          Delete order/order-item logic.
          */
          var order_item = args['order-item']
          var order_items_length = args['order-items-length']

          if (order_items_length <= 1) {
            /*
            Delete order and with it order-item.
            */
            var order_id = order_item.order
            fetch(that.order_api + order_id + '/', {
              method:'DELETE',
              headers:{
                'Content-type':'application/json',
                'X-CSRFToken':csrftoken,
              },
            })
            .then(function(response) {
              that.populateOrderCount()
              that.populateOrderSum()
              that.populateOrderList()
            })
          } else {
            /*
            Delete order-item.
            */
            var order_item_id = order_item.id
            fetch(that.order_item_api + order_item_id + '/', {
              method:'DELETE',
              headers:{
                'Content-type':'application/json',
                'X-CSRFToken':csrftoken,
              },
            })
            .then(function(response) {
              that.populateOrderCount()
              that.populateOrderSum()
              that.populateOrderList()
            })
          }
        }


      } else {
        // Add cookie logic here.
        if (action == 'add') {
          /*
          Add new order-item/increase order-item quantity.
          */


        } else if (action == 'remove') {
          /*
          Decrease order-item quantity.
          */


        } else if (action == 'delete') {
          /*
          Delete order-item.
          */

        }
      }
    }
  }


}

export default Order;
