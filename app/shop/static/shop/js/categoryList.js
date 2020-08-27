import $ from 'jquery';

class CategoryList {
  constructor() {
    this.categoryList = $('.categoryList')
    this.currentCategoryHeader = $('.currentCategoryHeader')

    if (this.categoryList.length > 0 && url_params.get('category__name')) {
      this.populateCurrentCategory()
    }

    if (this.categoryList.length > 0) {
      this.category_api = domain + '/api/category/'

      this.populateCategoryList()
    }
  }

  populateCurrentCategory() {
    var that = this

    that.currentCategoryHeader.each(function() {
      if (url_params.get('category__name') == 'Sport') {
        $(this).html('<i class="text-strong-italic">Nachhaltige ' + url_params.get('category__name') + 'artikel</i>')
      } else {
        $(this).html('Nachhaltige ' + url_params.get('category__name'))
      }
    })
  }

  populateCategoryList() {
    var that = this

    that.categoryList.each(function() {
      var currentCategoryList = $(this)
      var amount = currentCategoryList.data('amount')
      var sort = currentCategoryList.data('sort')
      var style = currentCategoryList.data('style')

      fetch(that.category_api + '?ordering=' + sort)
      .then((resp) => resp.json())
      .then(function(data) {
        if (amount && amount.length > 0) {
          var categories = data.slice(0,amount)
        } else {
          var categories = data
        }

        var filter = ''
        if (url_params.get('brand__name__in')) {
          filter += '&brand__name__in=' + url_params.get('brand__name__in')
        }
        if (url_params.get('price__gte')) {
          filter += '&price__gte=' + url_params.get('price__gte')
        }
        if (url_params.get('price__lte')) {
          filter += '&price__lte=' + url_params.get('price__lte')
        }

        for (var i in categories) {
          var category = categories[i]
          var i_tag = ''
          var i_tag_close = ''

          if (current_url.includes(category.name)) {
            if (style == 'mobile-menu') {
              var html = `
                <li class="border-bottom border-primary p-2">
                  <a href="${ shop_url + '?category__name=' + category.name + filter }">
                    <button class="btn m-0 p-0 w-100">
                      <div class="d-flex align-items-center">
                        <h5 class="text-primary m-0 mr-auto text-regular">${ i_tag + category.name + i_tag_close }</h5>
                        <svg class="bi bi-chevron-right text-primary" height="0.8em" viewBox="0 0 21.181 35.992" xmlns="http://www.w3.org/2000/svg"><path d="M5.233,8.233a2.5,2.5,0,0,1,3.538,0L22,21.462,35.22,8.233a2.5,2.5,0,0,1,3.538,3.538L23.765,26.765a2.5,2.5,0,0,1-3.538,0L5.233,11.772a2.5,2.5,0,0,1,0-3.538Z" transform="translate(-6.818 39.991) rotate(-90)" fill="currentColor" stroke="{{ border }}" stroke-width="1" fill-rule="evenodd"/></svg>
                      </div>
                    </button>
                  </a>
                </li>
                `
            } else {
              if (style == 'nav') {
                if (category.name == 'Sport') {
                  i_tag = '<i>'
                  i_tag_close = '</i>'
                }

                var html = `
                  <a href="${ shop_url + '?category__name=' + category.name + filter }">
                    <button class="btn btn-lg btn-primary ml-2">
                      ${ i_tag + category.name + i_tag_close }
                    </button>
                  </a>
                  `
              }
            }

            currentCategoryList.append(html)
          }
        }

        for (var i in categories) {
          var category = categories[i]
          var i_tag = ''
          var i_tag_close = ''

          if (!current_url.includes(category.name)) {
            if (category.name == 'Sport') {
              i_tag = '<i>'
              i_tag_close = '</i>'
            }

            if (style == 'mobile-menu') {
              var html = `
                <li class="border-bottom border-info p-2">
                  <a href="${ shop_url + '?category__name=' + category.name + filter }">
                    <button class="btn m-0 p-0 w-100">
                      <div class="d-flex align-items-center">
                        <h5 class="text-white m-0 mr-auto text-regular">${ i_tag + category.name + i_tag_close }</h5>
                        <svg class="bi bi-chevron-right text-white" height="0.8em" viewBox="0 0 21.181 35.992" xmlns="http://www.w3.org/2000/svg"><path d="M5.233,8.233a2.5,2.5,0,0,1,3.538,0L22,21.462,35.22,8.233a2.5,2.5,0,0,1,3.538,3.538L23.765,26.765a2.5,2.5,0,0,1-3.538,0L5.233,11.772a2.5,2.5,0,0,1,0-3.538Z" transform="translate(-6.818 39.991) rotate(-90)" fill="currentColor" stroke="{{ border }}" stroke-width="1" fill-rule="evenodd"/></svg>
                      </div>
                    </button>
                  </a>
                </li>
                `
            } else {
              if (style == 'nav') {
                var btn_class = 'btn btn-lg btn-outline-dark ml-2'
              } else {
                var btn_class = 'btn btn-sm btn-outline-dark mr-1 mb-2'
              }

              var html = `
                <a href="${ shop_url + '?category__name=' + category.name + filter }">
                  <button class="${ btn_class }">
                    ${ i_tag + category.name + i_tag_close }
                  </button>
                </a>
                `
            }

            currentCategoryList.append(html)
          }
        }
      })
    })
  }
}

export default CategoryList;