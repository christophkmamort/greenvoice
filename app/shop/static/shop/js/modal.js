import $ from 'jquery';

class Modal {
  constructor() {
    this.window = $(window);
    this.trigger = $('.modalTrigger');
    this.events();
  }

  events() {
    this.trigger.on("click", this.toggleModal.bind(this));
    this.window.on("click", this.resetModal.bind(this));
  }

  resetModal(e) {
    var that = this

    that.trigger.each(function() {
      var modal = $($(this).data('modal'))

      if (!modal.is(e.target) && modal.has(e.target).length === 0 && !that.trigger.is(e.target) && that.trigger.has(e.target).length === 0) {
        modal.slideUp()
        setTimeout(function() {
          modal.addClass('d-none')
        }, 500)
      }
    })
  }

  toggleModal(e) {
    var that = this;
    var trigger = $(e.target)
    if (!$(e.target).data('action')) {
      trigger = $(e.target).closest(that.trigger)
    }
    var action = trigger.data('action')
    var modal = $(trigger.data('modal'))

    if (action == 'open') {
      modal.removeClass('d-none').hide().slideDown()

    } else if (action == 'close') {
      modal.slideUp()
    }
  }
}

export default Modal;
