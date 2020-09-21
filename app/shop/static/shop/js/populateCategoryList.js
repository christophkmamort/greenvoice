import $ from 'jquery'


// Constructor.
var categoryList = $('.categoryList')
if (categoryList) {
  populateAllCategoryLists()
}


// Helper functions.
function apiCallCategories(args) {
  var currentElem = args['currentElem']
  var currentElemType = currentElem.data('type')

  var filter = '?ordering=-value&product__isnull=False'
  if (currentElemType == 'mainCatNav') {
    filter += '&parent__isnull=true'
  }

  return fetch(home_url + '/api/taxonomy-category/' + filter)
  .then((resp) => resp.json())
  .catch(function(error) {
    console.log(error)
  })
}


export function populateAllCategoryLists() {
  categoryList.each(function() {
    var args = {
      'currentElem':$(this),
    }
    populateCategoryList(args)
  })
}


// Functions.
function populateCategoryList(args) {
  var currentElem = args['currentElem']
  var currentElemStyle = currentElem.data('style')

  apiCallCategories(args).then(function(data) {
    var categories = data

    if (categories) {
      for (var i in categories) {
        var category = categories[i]
        var category_name = category.name
        var category_url = shop_url + '?category__name=' + category_name // + filter

        if (currentElemStyle == 'vertical') {
          var html = `
            <li class="border-bottom border-white p-2">
              <a href="${ category_url }">
                <button class="btn m-0 p-0 w-100">
                  <div class="d-flex align-items-center">
                    <h5 class="text-white m-0 mr-auto text-regular">${ category_name }</h5>
                    <svg class="bi bi-chevron-right text-white" height="0.8em" viewBox="0 0 21.181 35.992" xmlns="http://www.w3.org/2000/svg"><path d="M5.233,8.233a2.5,2.5,0,0,1,3.538,0L22,21.462,35.22,8.233a2.5,2.5,0,0,1,3.538,3.538L23.765,26.765a2.5,2.5,0,0,1-3.538,0L5.233,11.772a2.5,2.5,0,0,1,0-3.538Z" transform="translate(-6.818 39.991) rotate(-90)" fill="currentColor" stroke="2" stroke-width="1" fill-rule="evenodd"/></svg>
                  </div>
                </button>
              </a>
            </li>
          `


        } else if (currentElemStyle == 'horizontal') {
          var html = `
            <a href="${ category_url }">
              <button class="btn btn-lg btn-outline-dark ml-2">
                ${ category_name }
              </button>
            </a>
          `
        }
        currentElem.append(html)
      }
    }
  })
}
