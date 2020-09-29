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
  var currentElemOrder = '-value'
  var currentElemDataOrder = currentElem.data('order')
  if (currentElemDataOrder) {
    currentElemOrder = currentElemDataOrder
  }


  var filter = '?ordering=' + currentElemOrder
  filter += '&status=2'
  filter += '&product__product_manager__product_option__status=2'
  // TODO: Stock check (filter += '&product_option__stock=')

  return fetch(api_brand + filter)
  .then((resp) => resp.json())
  .catch(function(error) {
    console.log(error)
  })
}


function populateBrandList() {
  brandList.each(function(index) {
    var currentElem = $(this)
    var args = {
      'currentElem':currentElem,
    }

    currentElem.html('')

    apiCallBrand(args).then(function(data) {
      var brands = data

      if (brands.length > 0) {
        var currentElemQuantity = currentElem.data('quantity')
        var currentElemStyle = currentElem.data('style')
        if (currentElemQuantity) { // TODO: Find way to query this in api call (speed).
          brands = data.slice(0,currentElemQuantity)
        }

        if (currentElemStyle = 'slide') {
          var html = `<div class="feed-padding-left"></div>`
          currentElem.append(html)
        }

        for (var i in brands) {
          var brand = brands[i]
          var brand_name = brand.name
          var brand_logo = brand.logo

          var brand_category_names = []
          var brand_products = brand.product
          for (var x in brand_products) {
            var brand_product = brand_products[x]
            var brand_product_categories = brand_product.category
            for (var y in brand_product_categories) {
              var brand_product_category = brand_product_categories[y]
              if (brand_product_category.parent == null) {
                var brand_category_name = '#' + brand_product_category.name
                if (!brand_category_names.includes(brand_category_name)) {
                  brand_category_names.push(brand_category_name);
                }
              }
            }
          }
          brand_category_names.toString(' ')

          var html = `
            <div class="feed-brand mr-4">
              <a href="${ shop_url + '?brand__name__in=' + brand_name }" class="text-decoration-none">
                <div class="d-flex justify-content-center align-items-center">
                  <div class="mw-100">
                    <img src="${ brand_logo }" class="img img-fluid img-thumbnail circle w-100 h-100" alt="${ brand_name }">
                    <div class="pt-2">
                      <h6 class="m-0 p-0 text-center">${ brand_name }</h6>
                      <p class="m-0 p-0 mt-2 text-info text-center text-smaller" style="line-height: 1.2em;">${ brand_category_name }</p>
                    </div>
                  </div>
                </div>
              </a>
            </div>
          `
          currentElem.append(html)
        }

        if (currentElemStyle = 'slide') {
          var html = `<div class="feed-padding-right"></div>`
          currentElem.append(html)
        }

      }
    })
  })
}
