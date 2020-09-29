import $ from 'jquery'

import * as categoryListHtml from './templates/categoryList.js'


// Constructor.
var categoryList = $('.categoryList')
if (categoryList) {
  populateAllCategoryLists()
}


// Helper functions.
function apiCallCategories(args) {
  var currentElem = args['currentElem']
  var currentElemOrder = '-value'
  var currentElemDataOrder = currentElem.data('order')
  if (currentElemDataOrder) {
    currentElemOrder = currentElemDataOrder
  }
  var currentElemType = currentElem.data('type')

  var filter = '?ordering=' + currentElemOrder
  filter += '&product__isnull=False'
  if (currentElemType == 'mainCatNav') {
    filter += '&parent__isnull=true'

  } else if (currentElemType == 'variableCatNav') {
    console.log('test')
  }


  // TODO: Stock check (filter += '&product_option__stock=')

  return fetch(home_url + '/api/taxonomy-category/' + filter)
  .then((resp) => resp.json())
  .catch(function(error) {
    console.log(error)
  })
}


function populateAllCategoryLists() {
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
    /*
    ==== ==== ==== ====
    TODO: Find way to query this in api call (speed).
    */
    var currentElemQuantity = currentElem.data('quantity')
    if (currentElemQuantity) {
      categories = data.slice(0,currentElemQuantity)
    }
    /*
    End.
    ==== ==== ==== ====
    */

    if (categories) {
      var category_url_param = url_params.get('category__name')

      for (var i in categories) {
        var category = categories[i]
        var category_name = category.name
        var category_url = shop_url + '?category__name=' + category_name // + filter

        var args = {
          'category_name': category_name,
          'category_url': category_url,
          'category_url_param':category_url_param,
        }

        if (currentElemStyle == 'buttonSm') {
          var html = categoryListHtml.categoryButtonSm(args)

        } else if (currentElemStyle == 'buttonLg') {
          var html = categoryListHtml.categoryButtonLg(args)

        } else if (currentElemStyle == 'mobileMenu') {
          var html = categoryListHtml.categoryButtonMobileMenu(args)

        }

        currentElem.append(html)
      }
    }
  })
}




function populateCategoryListOld(args) {
  var currentElem = args['currentElem']
  var currentElemStyle = currentElem.data('style')
  var currentElemType = currentElem.data('type')

  apiCallCategories(args).then(function(data) {
    var categories = data

    if (categories) {
      /*
      Filter categories.
      */
      if (currentElemType == 'variableCatNav') {
        var category_url_param = url_params.get('category__name')

        for (var i in categories) {
          /*
          Check if active category has children.
          */
          var category = categories[i]
          var category_name = category.name

          if (category_name == category_url_param) {
            var category_children_length = category.children.length
            var category_url_parent = category.parent
          }
        }

        for (var i in categories) {
          var category = categories[i]
          var category_name = category.name
          var category_parent = category.parent

          if (category_url_param) {
            if (category_parent) {
              var category_parent_name = category_parent.name
            }

            if (category_children_length > 0) {
              /*
              Display child categories of currently active category.
              Only if current category has child categories.
              */
              if (!category_parent || category_parent_name != category_url_param) {
                categories.splice(i, 1);
              }

            } else {
              /*
              Display siblings of current category and mark active category.
              Only if no more child categories for current category.
              */
              if (category_parent != category_url_parent) {
                categories.splice(i, 1);
              }
            }

          } else {
            /*
            Display main categories only.
            */
            if (category_parent != null) {
              categories.splice(i, 1);
            }
          }
        }
      }

      /*
      Display categories.
      */
      for (var i in categories) {
        var category = categories[i]
        var category_name = category.name
        var category_url = shop_url + '?category__name=' + category_name // + filter

        var args = {
          'category_name': category_name,
          'category_url': category_url,
          'category_url_param':category_url_param,
        }

        if (currentElemStyle == 'buttonSm') {
          var html = categoryListHtml.categoryButtonSm(args)

        } else if (currentElemStyle == 'buttonLg') {
          var html = categoryListHtml.categoryButtonLg(args)

        } else if (currentElemStyle == 'mobileMenu') {
          var html = categoryListHtml.categoryButtonMobileMenu(args)

        }

        currentElem.append(html)
      }
    }
  })
}
