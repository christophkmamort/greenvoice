import $ from 'jquery'

import * as filterElementsHtml from './templates/filterElements.js'
import { apiCallBrand } from './populateBrandList.js'


// Constructor.
var productFilterModalTrigger = $('.productFilterModalTrigger')
if (productFilterModalTrigger) {
  var productFilter = $('.productFilter')
  if (productFilter) {
    populateAllProductFilters()
    $('.productFilter').closest('.productFilterWrapper').modal('show')
  }
}


// Helper functions.
function populateAllProductFilters() {
  productFilter.each(function () {
    var args = {
      'currentElem':$(this),
    }
    populateProductFilter(args)
  })
}


// Functions.
function populateProductFilter(args) {
  var currentElem = args['currentElem']

  /*
  Vor current filter & category selection:
    - brands
    - max price
    - min price
    - sort
    - colors
  */

  // currentElem.html('')

  // Brands.
  apiCallBrand(args).then(function(data) {
    var brands = data
    var productFilterBrands = currentElem.find('.productFilterBrands')

    if (brands) {
      productFilterBrands.html('')

      var html = `
        <div data-section="filterBrands">
          <h5 class="text-white">Marke (${ brands.length })</h5>
          <div class="seperator mt-3"></div>
          <div class="max-height-25vh overflow-auto">
      `
      productFilterBrands.append(html)

      for (var i in brands) {
        var brand = brands[i]
        var brand_name = brand.name

        var args = {
          'name':brand_name,
          'value':brand_name,
        }
        productFilterBrands.append(filterElementsHtml.checkbox(args))
      }

      var html = `
          </div>
        </div>
        <hr class="bg-info mt-4 mb-4">
      `
      productFilterBrands.append(html)
    }
  })


  // Options.


}
