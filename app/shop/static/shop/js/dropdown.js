import $ from 'jquery';

class Dropdown {
  constructor() {
    this.window = $(window);
    this.trigger = $('.dropdown-toggle');
    this.arrowDown = $('.arrow-down');
    this.arrowUp = $('.arrow-up');
    this.events();
  }

  events() {
    this.trigger.on("click", this.toggleArrow.bind(this));
    this.arrowDown.on("click", this.activateArrow.bind(this));
    this.arrowUp.on("click", this.resetArrow.bind(this));
    this.window.on("click", this.resetArrow.bind(this));
  }

  toggleArrow(e) {
    var that = this;
    if ($(e.target).find(that.arrowDown).hasClass('d-none')) {
      $(e.target).find(that.arrowDown).removeClass('d-none');
      $(e.target).find(that.arrowUp).addClass('d-none');
      that.arrowDown.addClass('text-dark');
    } else {
      $(e.target).find(that.arrowDown).addClass('d-none');
      $(e.target).find(that.arrowUp).removeClass('d-none');
    }
  }

  activateArrow(e) {
    var that = this;
    $(e.target).closest(that.trigger).find(that.arrowDown).addClass('d-none');
    $(e.target).closest(that.trigger).find(that.arrowUp).removeClass('d-none');
  }

  resetArrow(e) {
    var that = this;
    that.arrowDown.removeClass('d-none');
    that.arrowUp.addClass('d-none');
    that.arrowDown.removeClass('text-dark');
  }
}

export default Dropdown;
