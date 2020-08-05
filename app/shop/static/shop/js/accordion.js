import $ from 'jquery';

class Accordion {
  constructor() {
    this.window = $(window);
    this.trigger = $('.accordion-toggle');
    this.arrowDown = $('.accordion-down');
    this.arrowUp = $('.accordion-up');
    this.events();
  }

  events() {
    this.trigger.on("click", this.toggleArrow.bind(this));
  }

  toggleArrow(e) {
    var that = this;
    if ($(e.target).closest(that.trigger).find(that.arrowDown).hasClass('d-none')) {
      $(e.target).closest(that.trigger).find(that.arrowDown).removeClass('d-none');
      $(e.target).closest(that.trigger).find(that.arrowUp).addClass('d-none');
    } else {
      that.arrowDown.removeClass('d-none');
      that.arrowUp.addClass('d-none');
      $(e.target).closest(that.trigger).find(that.arrowDown).addClass('d-none');
      $(e.target).closest(that.trigger).find(that.arrowUp).removeClass('d-none');
    }
  }
}

export default Accordion;
