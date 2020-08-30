import $ from 'jquery';
import Cookies from 'js-cookie';

class BrandList {
  constructor() {
    this.brandList = $('.brandList')

    if (this.brandList.length > 0) {
      this.brand_api = home_url + '/api/brand/'

      this.populateBrandList()
    }
  }

  populateBrandList() {
    var that = this;

    that.brandList.each(function() {
      var currentBrandList = $(this)
      var amount = currentBrandList.data('amount')
      var ordering = currentBrandList.data('ordering')
      if (!ordering) {
        ordering = '-value'
      }

      var gender = ''
      if (Cookies.get('filter_gender') == 'unisex') {
        gender += '&gender__in=1'
      } else if (Cookies.get('filter_gender') == 'women') {
        gender += '&gender__in=1,2'
      } else if (Cookies.get('filter_gender') == 'men') {
        gender += '&gender__in=1,3'
      }

      fetch(that.brand_api + '?ordering=' + ordering + gender + '&status=2&product__isnull=False')
      .then((resp) => resp.json())
      .then(function(data) {
        if (amount.length > 0) {
          var brands = data.slice(0,amount)
        } else {
          var brands = data
        }

        for (var i in brands) {
          var brand = brands[i]

          if (brand.status == 2) {
            var html = `
              <div class="feed-brand mr-4">
                <a href="${ shop_url + '?brand__name__in=' + brand.name }" class="text-decoration-none">
                  <div class="d-flex justify-content-center align-items-center">
                    <div class="mw-100">
                      <img src="${ brand.logo }" class="img img-fluid img-thumbnail circle w-100 h-100" alt="">
                      <div class="pt-2">
                        <h6 class="m-0 p-0 text-center">${ brand.name }</h6>
                        <p class="m-0 p-0 mt-2 text-info text-center text-smaller" style="line-height: 1.2em;">#Bekleidung #Schuhe</p>
                      </div>
                    </div>
                  </div>
                </a>
              </div>
              `
            currentBrandList.append(html)
          }
        }
      })

      currentBrandList.append('<div class="feed-padding-right"></div>')
    })
  }
}

export default BrandList;
