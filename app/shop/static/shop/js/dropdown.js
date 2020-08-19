import $ from 'jquery';

class Dropdown {
  constructor() {
    this.window = $(window);
    this.dropdown = $('.dropdown');
    this.dropdownToggle = $('.dropdownToggle');
    this.arrowDown = $('.arrowDown');
    this.arrowUp = $('.arrowUp');
    this.checkbox = $('.checkbox');
    this.dropdownOption = $('.dropdownOption');
    this.events();
  }

  events() {
    this.dropdownToggle.on("click", this.toggleArrow.bind(this));
    this.window.on("click", this.resetArrow.bind(this));
    this.dropdownOption.on("click", this.selectOption.bind(this));
  }

  selectOption(e) {
    var that = this;
    var dorpdownSelected = $(e.target).closest(that.dropdown).find(that.dropdownToggle).find('p');
    var dropdownOptionValue = $(e.target).closest(that.checkbox).find('p').html();

    dorpdownSelected.html(dropdownOptionValue);
    dorpdownSelected.addClass('text-dark');
  }

  toggleArrow(e) {
    var that = this;
    var dropdownArrowDown = $(e.target).closest(that.dropdown).find(that.arrowDown);
    var dropdownArrowUp = $(e.target).closest(that.dropdown).find(that.arrowUp);

    if (dropdownArrowDown.hasClass('d-none')) {
      dropdownArrowDown.removeClass('d-none');
      dropdownArrowUp.addClass('d-none');
      that.arrowDown.addClass('text-dark');
    } else {
      dropdownArrowDown.addClass('d-none');
      dropdownArrowUp.removeClass('d-none');
    }
  }

  resetArrow() {
    var that = this;

    that.arrowDown.removeClass('d-none');
    that.arrowUp.addClass('d-none');
    that.arrowDown.removeClass('text-dark');
  }
}

export default Dropdown;
