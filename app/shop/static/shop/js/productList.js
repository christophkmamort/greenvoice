import $ from 'jquery';

class ProductList {
  constructor() {
    this.productList = $('.productList')

    if (this.productList.length > 0) {
      this.product_api = domain + '/api/products/'
      this.productAmount = $('.productAmount')
      this.productFilter = $('.productFilter')

      if (this.productFilter.length > 0) {
        this.activeFilterAmount = $('.activeFilterAmount')
        this.brand_api = domain + '/api/brand/'
        this.openFilter = $('.openFilter')
        this.filterBrands = $('.filterBrands')
        this.submitProductFilterTrigger = $('.submitProductFilterTrigger')
        this.filterModal = $('#filterModal')
        this.closeFilterModalTrigger = $('.closeFilterModalTrigger')
        this.filterPriceErrorMsg = $('.filterPriceErrorMsg')
        this.filterPriceMin = $('input[name="filterPriceMin"]')
        this.filterPriceMax = $('input[name="filterPriceMax"]')
      }

      this.populateProductList()
      this.events()
    }
  }


  events() {
    this.closeFilterModalTrigger.on('click', this.closeFilterModal.bind(this))
    this.submitProductFilterTrigger.on('click', this.submitProductFilter.bind(this))
    this.filterPriceMin.on('click', this.removeFilterPriceError.bind(this))
    this.filterPriceMax.on('click', this.removeFilterPriceError.bind(this))
  }


  closeFilterModal() {
    var that = this

    that.filterModal.modal('toggle');
  }


  removeFilterPriceError() {
    var that = this

    that.filterPriceMin.removeClass('form-control-error')
    that.filterPriceMax.removeClass('form-control-error')
    that.filterPriceErrorMsg.html('')
  }


  submitProductFilter() {
    var that = this

    var error_codes = 0
    var ordering = '-value'
    var filter = ''

    if (that.productFilter.find('input[name="ordering"]:checked').val()) {
      ordering = that.productFilter.find('input[name="ordering"]:checked').val()
    }
    if (that.productFilter.find('input[name="filterBrand"]:checked').val()) {
      filter += '&brand__name='
      that.productFilter.find('input[name="filterBrand"]:checked').each(function(i) {
        if (i > 0) {
          filter += ','
        }
        filter += $(this).val()
      })
    }

    if (that.filterPriceMin.val().length > 0) {
      filter += '&price__gte=' + that.filterPriceMin.val()
    }
    if (that.filterPriceMax.val().length > 0) {
      filter += '&price__lte=' + that.filterPriceMax.val()
    }

    if (that.filterPriceMin.val().length > 0 && that.filterPriceMax.val().length > 0 && parseInt(that.filterPriceMin.val()) >= parseInt(that.filterPriceMax.val())) {
      that.filterPriceMin.addClass('form-control-error')
      that.filterPriceMax.addClass('form-control-error')
      that.filterPriceErrorMsg.html('Der minimale Preis muss kleiner sein als der maximale Preis.')
      error_codes += 1;
    } else {
      that.filterPriceMin.removeClass('form-control-error')
      that.filterPriceMax.removeClass('form-control-error')
      that.filterPriceErrorMsg.html('')
    }

    if (url_params.get('category__name')) {
      filter += '&category__name=' + url_params.get('category__name')
    }

    if (error_codes == 0) {
      window.location.href = base_url + '?ordering=' + ordering + filter;
    }
  }



  populateProductFilter(active_filters, filter, ordering, products) {
    var that = this

    that.activeFilterAmount.html(active_filters)
    if (active_filters > 0) {
      that.openFilter.removeClass('btn-outline-dark')
      that.openFilter.addClass('btn-outline-primary')
    } else {
      that.openFilter.removeClass('btn-outline-primary')
      that.openFilter.addClass('btn-outline-dark')
    }

    fetch(that.brand_api) // Check if brand has active products and check if brand is active
    .then((resp) => resp.json())
    .then(function(data) {
      var brands = data

      for (var i in brands) {
        var brand = brands[i]
        var checked = ''

        if (filter.includes(brand.name)) {
          checked = 'checked'
        }

        var html = `
          <label class="checkbox">
            <input type="checkbox" name="filterBrand" value="${ brand.name }" ${ checked }>
            <div class="checkbox-box checkbox-box-dark">
              <svg class="bi text-white checkbox-icon" height="0.7em" viewBox="0 0 15 11.942" xmlns="http://www.w3.org/2000/svg"><path d="M16.725,5.158a1.377,1.377,0,1,1,1.966,1.928l-7.329,9.161a1.377,1.377,0,0,1-1.983.037L4.524,11.426A1.377,1.377,0,1,1,6.47,9.48l3.844,3.843L16.69,5.2a.433.433,0,0,1,.037-.04Z" transform="translate(-4.085 -4.745)" fill="currentColor" fill-rule="evenodd"/></svg>
            </div>
            <h6 class="checkbox-text checkbox-text-dark m-0 ml-2">${ brand.name }</h6>
          </label>
        `
        that.filterBrands.append(html)
      }
    })

    if (filter.includes('price__lte')) {
      that.filterPriceMax.val(url_params.get('price__lte'))
    }

    if (filter.includes('price__gte')) {
      that.filterPriceMin.val(url_params.get('price__gte'))
    }

    if (ordering != '-value') {
      that.productFilter.find('input[value="'+ ordering +'"]').prop("checked", true)
    }
  }



  populateProductList() {
    var that = this
    var i_tag  = ''
    var i_tag_close = ''
    if (current_url.includes('Sport')) {
      var i_tag = '<i>'
      var i_tag_close = '</i>'
    }

    that.productList.each(function() {
      var currentProductList = $(this)
      var amount = currentProductList.data('amount')
      var style = currentProductList.data('style')
      var ordering = currentProductList.data('ordering')
      if (!ordering) {
        ordering = '-value'
      }

      var filter = ''
      var active_filters = 0
      if (url_params.get('ordering')) {
        ordering = url_params.get('ordering')
        active_filters += 1
      }
      if (url_params.get('category__name')) {
        filter += '&category__name=' + url_params.get('category__name')
      }
      if (url_params.get('brand__name')) {
        filter += '&brand__name=' + url_params.get('brand__name')
        active_filters += 1
      }
      if (url_params.get('price__lte')) {
        filter += '&price__lte=' + url_params.get('price__lte')
        active_filters += 1
      }
      if (url_params.get('price__gte')) {
        filter += '&price__gte=' + url_params.get('price__gte')
        active_filters += 1
      }

      fetch(that.product_api + '?ordering=' + ordering + filter) // check if products and their brands are active
      .then((resp) => resp.json())
      .then(function(data) {
        if (amount && amount.length > 0) {
          var products = data.slice(0,amount)
        } else {
          var products = data
        }

        that.populateProductFilter(active_filters, filter, ordering, products)

        if (products.length == 1) {
          that.productAmount.html(products.length + ' Produkt')
        } else {
          that.productAmount.html(products.length + ' Produkte')
        }

        for (var i in products) {
          var product = products[i]

          if (product.status == 2) {
            if (user == 'AnonymousUser') {
              var wishlistTrigger = `
                <a href="${ login_url }">
                  <button class="btn position-absolute p-1 bg-white-50 circle" style="top: 0.25em; right: 0.25em;">
                    <svg class="bi bi-heart text-dark" height="1.5em" viewBox="0 0 26.593 25.22" xmlns="http://www.w3.org/2000/svg"><path d="M12.267,2.015c6.8-7,23.819,5.246,0,20.985C-11.552,7.262,5.462-4.98,12.267,2.015Z" transform="translate(1.03 1.022)" fill="none" stroke="currentColor" stroke-width="2" fill-rule="evenodd"/></svg>
                  </button>
                </a>
              `
            } else {

              if (1 == 0) {
                var wishlistTrigger = `
                  <button class="btn position-absolute p-1 bg-white-50 circle updateWishlist" data-action="delete" style="top: 0.25em; right: 0.25em;">
                    <svg class="bi bi-heart text-primary" height="1.5em" viewBox="0 0 26.593 25.22" xmlns="http://www.w3.org/2000/svg"><path d="M12.267,2.015c6.8-7,23.819,5.246,0,20.985C-11.552,7.262,5.462-4.98,12.267,2.015Z" transform="translate(1.03 1.022)" fill="currentColor" stroke="currentColor" stroke-width="2" fill-rule="evenodd"/></svg>
                  </button>
                `
              } else {
                var wishlistTrigger = `
                  <button class="btn position-absolute p-1 bg-white-50 circle updateWishlist" data-action="add" style="top: 0.25em; right: 0.25em;">
                    <svg class="bi bi-heart text-dark" height="1.5em" viewBox="0 0 26.593 25.22" xmlns="http://www.w3.org/2000/svg"><path d="M12.267,2.015c6.8-7,23.819,5.246,0,20.985C-11.552,7.262,5.462-4.98,12.267,2.015Z" transform="translate(1.03 1.022)" fill="none" stroke="currentColor" stroke-width="2" fill-rule="evenodd"/></svg>
                  </button>
                `
              }
            }

            if (style == 'slide') {
              var product_wrapper_class = 'feed-product feed-product-slide'
            } else {
              var product_wrapper_class = 'feed-product mb-4'
            }

            var html = `
              <div class="${ product_wrapper_class }">
                <div class="overflow-hidden position-relative feed-product-img">
                  <a href="${ product_url + product.id }">
                    <div class="position-absolute" style="left: 0; top: 0; right: 0; bottom: 0;">
                      <img class="img w-100 h-100" src="${ product.image }" alt="">
                    </div>
                  </a>

                  <div class="wishlistTriggerWrapper">
                    ${ wishlistTrigger }
                  </div>
                </div>
                <a href="${ product_url + product.id }" class="text-decoration-none">
                  <div class="pt-2 pr-2 pl-2">
                    <p class="m-0 p-0 mt-1">${ i_tag + product.name + i_tag_close }</p>
                    <h6 class="m-0 p-0 mt-1 text-small"><span class="text-dark text-strong">€ ${ product.price }</span></h6>
                  </div>
                </a>
              </div>
              `
            currentProductList.append(html)
          }
        }
      })

      if (style == 'slide') {
        currentProductList.append('<div class="feed-padding-right"></div>')
      }
    })
  }
}

export default ProductList;
