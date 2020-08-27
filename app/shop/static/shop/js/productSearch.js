import $ from 'jquery';

class ProductSearch {
  constructor() {
    this.productSearchQuery = $('input[name="productSearchQuery"]');
    this.events();
  }

  events() {
    this.productSearchQuery.keydown(this.submitProductSearch.bind(this));
  }

  submitProductSearch(e) {
    var that = this;

    if (e.keyCode == 13) {
      window.location.href = shop_url + '?search=' + that.productSearchQuery.val();
    }
  }
}

export default ProductSearch;
