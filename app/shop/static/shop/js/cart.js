import $ from 'jquery';

class Cart {
  constructor() {
    this.updateCartTrigger = $('.updateCartTrigger');
    this.cartItemsTotal = $('.cartItemsTotal');
    this.cartItem = $('.cartItem');
    this.cartItemTotal = $('.cartItemTotal');
    this.cartItemPrice = $('.cartItemPrice');
    this.cartTotal = $('.cartTotal');
    this.cartItemWrapper = $('.cartItemWrapper');
    this.cartContent = $('.cartContent');
    this.events();
  }

  events() {
    this.updateCartTrigger.on("click", this.updateCart.bind(this));
  }

  updateCart(e) {
    var that = this;

    var productId = $(e.target).data('product');
    var action = $(e.target).data('action');

    if (user == 'AnonymousUser') {
      console.log('Not logged in');
    } else {

      var redirect = '/shop/update-cart/';

      fetch(redirect, {
        method:'POST',
  			headers:{
  				'Content-Type':'application/json',
  				'X-CSRFToken':csrftoken,
  			},
  			body:JSON.stringify({'productId': productId, 'action': action})
      })
      .then((response) => {
        return response.json();
		   })
      .then((data) => {

        console.log(data);

        if ($(e.target).html() == 'In den Warenkorb') {
          var width = $(e.target).css('width');
          $(e.target).css({'width':width});
          $(e.target).html(`<svg class="bi mr-1 text-white" height="0.7em" style="margin-top: -0.25em;" viewBox="0 0 15 11.942" xmlns="http://www.w3.org/2000/svg"><path d="M16.725,5.158a1.377,1.377,0,1,1,1.966,1.928l-7.329,9.161a1.377,1.377,0,0,1-1.983.037L4.524,11.426A1.377,1.377,0,1,1,6.47,9.48l3.844,3.843L16.69,5.2a.433.433,0,0,1,.037-.04Z" transform="translate(-4.085 -4.745)" fill="currentColor" fill-rule="evenodd"/></svg> Hinzugefügt`);

          setTimeout(function() {
            $(e.target).css({'width':'auto'});
            $(e.target).html('In den Warenkorb');
          }, 500);
        }

        // Cart
        if (currentUrl.indexOf('cart') >= 0) {
          var cartItemsTotal = parseFloat(that.cartItemsTotal.html());
          var cartTotal = parseFloat(that.cartTotal.html());
          var cartItem = $(e.target).closest(that.cartItem);
          var cartItemTotal = parseFloat($(e.target).closest(that.cartItem).find(that.cartItemTotal).html());
          var cartItemPrice = parseFloat($(e.target).closest(that.cartItem).find(that.cartItemPrice).html());

          if (data == 'added') {

            that.cartItemsTotal.html(cartItemsTotal + 1);
            cartItemTotal.html(cartItemTotal + 1);
            that.cartTotal.html((cartTotal + cartItemPrice).toFixed(2));

          } else if (data == 'removed') {

            that.cartItemsTotal.html(cartItemsTotal - 1);
            cartItemTotal.html(cartItemTotal - 1);
            that.cartTotal.html((cartTotal - cartItemPrice).toFixed(2));

          } else if (data == 'deleted') {

            if (cartItemsTotal == cartItemTotal) {

              that.cartItemWrapper.fadeOut();
              that.cartContent.append(`<div data-section="cartEmty"><p class="text-info">Du hast noch keine Artikel zu deinem Warenkorb hinzugefügt. {% include 'shop/templates/svg/bag.svg' with class='text-info ml-1' height='1em' style='margin-top: -0.2em;' only %}</p></div>`);

            } else {

              that.cartItemsTotal.html(cartItemsTotal - cartItemTotal);
              that.cartTotal.html((cartTotal - cartItemPrice * cartItemTotal).toFixed(2));
              cartItem.slideUp();

            }

          }
        }

      });

    }
  }
}

export default Cart;
