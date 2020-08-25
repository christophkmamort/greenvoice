import $ from 'jquery';

class CategoryList {
  constructor() {
    this.categoryList = $('.categoryList')

    if (this.categoryList.length > 0) {
      this.category_api = domain + '/api/category/'

      this.populateCategoryList()
    }
  }

  populateCategoryList() {
    var that = this;

    that.categoryList.each(function() {
      var currentCategoryList = $(this)
      var amount = currentCategoryList.data('amount')
      var sort = currentCategoryList.data('sort')

      // currentCategoryList.append('<div class="feed-padding-left"></div>')

      fetch(that.category_api + '?ordering=' + sort)
      .then((resp) => resp.json())
      .then(function(data) {
        if (amount.length > 0) {
          var categories = data.slice(0,amount)
        } else {
          var categories = data
        }

        for (var i in categories) {
          var category = categories[i]

          if (category.name == 'Sport') {
            var html = `
              <a href="#">
                <button class="btn btn-sm btn-outline-dark mr-1 mb-2">
                  <i>${ category.name }</i>
                </button>
              </a>
              `
          } else {
            var html = `
              <a href="#">
                <button class="btn btn-sm btn-outline-dark mr-1 mb-2">
                  ${ category.name }
                </button>
              </a>
              `
          }

          currentCategoryList.append(html)
        }
      })

      // currentCategoryList.append('<div class="feed-padding-right"></div>')
    })
  }
}

export default CategoryList;
