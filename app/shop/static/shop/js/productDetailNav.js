import $ from 'jquery';

class ProductDetailNav {
  constructor() {
    this.productDetailNavColorSelectedText = $('#productDetailNavColorSelectedText');
    this.productDetailNavColorChoose = $('.productDetailNavColorChoose');
    this.productDetailCurrentSizeIndicator = $('#productDetailCurrentSizeIndicator');
    this.productDetailNavSizeChoose = $('.productDetailNavSizeChoose');
    if (this.productDetailNavColorSelectedText.length > 0) {
      this.events();
    }
  }

  events() {
    this.productDetailNavColorChoose.on("click", this.productDetailNavColorSet.bind(this));
    this.productDetailNavSizeChoose.on("click", this.productDetailNavSizeSet.bind(this));
  }

  productDetailNavColorSet(e) {
    var that = this;
    var selectedColorName = $(e.target).closest('label').find('input').data('color');
    var selectedColorCode = $(e.target).closest('label').find('div').css('background-color');
    that.productDetailNavColorSelectedText.html(selectedColorName);
    that.productDetailNavColorSelectedText.css({'color':selectedColorCode});
  }

  productDetailNavSizeSet(e) {
    var that = this;
    var current_size = $(e.target).closest('label').find('h6').html();
    that.productDetailCurrentSizeIndicator.html(current_size);
    that.productDetailCurrentSizeIndicator.removeClass('btn-outline-info');
    that.productDetailCurrentSizeIndicator.addClass('btn-outline-primary');
  }
}

export default ProductDetailNav;
