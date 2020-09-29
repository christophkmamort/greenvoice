import $ from 'jquery'

import * as categoryListHtml from './templates/categoryList.js'


// Constructor.
var categoryBreadcrumbs = $('.categoryBreadcrumbs')
if (categoryBreadcrumbs) {
  populateAllCategoryBreadcrumbs()
}


var categoryList = $('.categoryList')
if (categoryList) {
  populateAllCategoryLists()
}


// Helper functions.
function apiCallCategories(args) {
  var currentElem = args['currentElem']
  var currentElemOrder = '-value'
  var currentElemDataOrder = args['currentElemDataOrder']
  if (currentElemDataOrder) {
    currentElemOrder = currentElemDataOrder
  }
  var currentElemType = args['currentElemType']
  var url_param_category__name = args['url_param_category__name']

  var filter = '?ordering=' + currentElemOrder
  filter += '&product__isnull=False'
  if (currentElemType == 'mainCatNav' || currentElemType == 'variableCatNav' && !url_param_category__name) {
    filter += '&parent__isnull=true'

  }
  // TODO: Stock check (filter += '&product_option__stock=')

  return fetch(home_url + '/api/taxonomy-category/' + filter)
  .then((resp) => resp.json())
  .catch(function(error) {
    console.log(error)
  })
}


function populateAllCategoryBreadcrumbs() {
  categoryBreadcrumbs.each(function() {
    var args = {
      'currentElem':$(this),
    }
    populateCategoryBreadcrumbs(args)
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
  var currentElemType = currentElem.data('type')
  var currentElemDataOrder = currentElem.data('order')
  var url_param_category__name = url_params.get('category__name')

  args['currentElemDataOrder'] = currentElemDataOrder
  args['currentElemType'] = currentElemType
  args['url_param_category__name'] = url_param_category__name

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
      currentElem.html('')

      if (currentElemType == 'variableCatNav') {
        for (var i in categories) {
          /*
          Check if active category has children.
          */
          var category = categories[i]
          var category_name = category.name

          if (category_name == url_param_category__name) {
            var category_children_length = category.children.length
            var category_url_parent = category.parent
          }
        }

        for (var i in categories) {
          var category = categories[i]
          var category_name = category.name
          var category_parent = category.parent

          if (url_param_category__name) {
            if (category_parent) {
              var category_parent_name = category_parent.name
            }

            if (category_children_length > 0) {
              /*
              Display child categories of currently active category.
              Only if current category has child categories.
              */
              if (!category_parent || category_parent_name != url_param_category__name) {
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

      for (var i in categories) {
        var category = categories[i]
        var category_name = category.name
        var category_url = shop_url + '?category__name=' + category_name // + filter

        var args = {
          'category_name': category_name,
          'category_url': category_url,
          'url_param_category__name':url_param_category__name,
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


function populateCategoryBreadcrumbs(args) {
  var currentElem = args['currentElem']
  var url_param_category__name = url_params.get('category__name')

  args['url_param_category__name'] = url_param_category__name

  apiCallCategories(args).then(function(data) {
    var categories = data

    if (categories) {
      currentElem.html('')
      currentElem.removeClass('d-none')

      /*for (var i in categories) {
        var category = categories[i]
        var category_name = category.name
        var category_parent = category.parent
        if (category_parent) {
          var category_parent_name = category.parent.name
        }

        if (category_name != url_param_category__name && category_parent_name == url_param_category__name) {
          categories.splice(i, 1);

        } else if () {

        }

        console.log(category_name)

        // var category_url = shop_url + '?category__name=' + category_name // + filter

        var args = {
          'category_name': category_name,
          'category_url': category_url,
          'url_param_category__name':url_param_category__name,
        }

        currentElem.append(categoryListHtml.categoryBreadcrumbs(args))
      }*/
    }
  })
}
