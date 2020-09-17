import $ from 'jquery'


// Constructor.
var brandList = $('.brandList')
if (brandList) {
  populateBrandList()
}


// Functions.
function apiCallBrand(args) {
  /*
  Api call to get matching product-managers.
  */
  var api_brand = home_url + '/api/brand/'
  var currentElem = args['currentElem']
  var filter = ''

  var currentElemOrder = currentElem.data('order')
  if (!currentElemOrder) {
    currentElemOrder = '-value'
  }
  filter += '?ordering=' + currentElemOrder
  filter += '&status=2' // Check if brand is active.
  filter += '&product_option__status=2' // Check if has active products.
  // TODO: Add check if product is in stock!! (filter += '&product_option__stock=')

  return fetch(api_brand + filter)
  .then((resp) => resp.json())
  .catch(function(error) {
    console.log(error)
  })
}


populateBrandList() {

}
