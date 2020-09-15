import $ from 'jquery'


export function updateOrder(args) {
  var action = args['action']
  var currentElem = args['currentElem']
  var order_api = home_url + '/api/order/'
  var order_item_api = home_url + '/api/order-item/'
  var product_option_id = args['product_option_id']

  console.log(action)
}
