import $ from 'jquery';

class Cart {
  constructor() {
    this.updateCartTrigger = $('.updateCartTrigger');
    this.updateCartWrapper = $('.updateCartWrapper');
    this.cartItemsTotal = $('.cartItemsTotal');
    this.cartItem = $('.cartItem');
    this.cartItemTotal = $('.cartItemTotal');
    this.cartItemPrice = $('.cartItemPrice');
    this.cartTotal = $('.cartTotal');
    this.cartItemWrapper = $('.cartItemWrapper');
    this.cartContent = $('.cartContent');
    this.cartActions = $('.cartActions');
    this.events();
  }

  events() {
    this.updateCartTrigger.on("click", this.updateCart.bind(this));
  }

  updateCart(e) {
    var that = this;

    var productId = $(e.target).closest(that.updateCartWrapper).find(that.updateCartTrigger).data('product');
    var action = $(e.target).closest(that.updateCartWrapper).find(that.updateCartTrigger).data('action');

    if (user == 'AnonymousUser') {
      console.log('Not logged in');
    } else {

      var url = '/shop/update-cart/';

      fetch(url, {
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
        var cartItemsTotal = parseFloat(that.cartItemsTotal.html());
        /*if (cartItemsTotal == '') {
          cartItemsTotal = 0;
        }
        console.log(cartItemsTotal);*/

        if (data == 'added') {
          that.cartItemsTotal.html(cartItemsTotal + 1);
        }

        if (currentUrl.indexOf('/shop/product/') >= 0) {
          var width = $(e.target).css('width');
          $(e.target).css({'width':width});
          $(e.target).html(`<svg class="bi mr-1 text-white" height="0.7em" style="margin-top: -0.25em;" viewBox="0 0 15 11.942" xmlns="http://www.w3.org/2000/svg"><path d="M16.725,5.158a1.377,1.377,0,1,1,1.966,1.928l-7.329,9.161a1.377,1.377,0,0,1-1.983.037L4.524,11.426A1.377,1.377,0,1,1,6.47,9.48l3.844,3.843L16.69,5.2a.433.433,0,0,1,.037-.04Z" transform="translate(-4.085 -4.745)" fill="currentColor" fill-rule="evenodd"/></svg> Hinzugefügt`);

          setTimeout(function() {
            $(e.target).css({'width':'auto'});
            $(e.target).html('In den Warenkorb');
          }, 3000);
        }

        // Cart
        else if (currentUrl.indexOf('/shop/cart') >= 0) {
          var cartTotal = parseFloat(that.cartTotal.html());
          var cartItem = $(e.target).closest(that.cartItem);
          var cartItemTotal = parseFloat($(e.target).closest(that.cartItem).find(that.cartItemTotal).html());
          var cartItemPrice = parseFloat($(e.target).closest(that.cartItem).find(that.cartItemPrice).html());

          if (data == 'added') {

            $(e.target).closest(that.cartItem).find(that.cartItemTotal).html(cartItemTotal + 1);
            that.cartTotal.html((cartTotal + cartItemPrice).toFixed(2));

          } else if (data == 'removed') {

            that.cartItemsTotal.html(cartItemsTotal - 1);
            $(e.target).closest(that.cartItem).find(that.cartItemTotal).html(cartItemTotal - 1);
            that.cartTotal.html((cartTotal - cartItemPrice).toFixed(2));

          } else if (data == 'deleted') {

            if (cartItemsTotal == cartItemTotal) {

              that.cartItemWrapper.slideUp();
              that.cartItemsTotal.html(cartItemsTotal - cartItemTotal);
              that.cartContent.append(`<div data-section="cartEmty"><p class="text-info">Du hast noch keine Artikel zu deinem Warenkorb hinzugefügt. <svg class="bi bi-bag text-info ml-1" height="1em" style="margin-top: -0.2em;" viewBox="0 0 24.581 26.25" xmlns="http://www.w3.org/2000/svg"><g transform="translate(-2986 -168.75)"><path id="cart" d="M1,6.145H23.581V22.274A3.226,3.226,0,0,1,20.355,25.5H4.226A3.226,3.226,0,0,1,1,22.274Z" transform="translate(2986 168.5)" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12.29,2.113A4.032,4.032,0,0,0,8.258,6.145H6.645a5.645,5.645,0,0,1,11.29,0H16.323A4.032,4.032,0,0,0,12.29,2.113Z" transform="translate(2986 168.5)" fill="currentColor" stroke="currentColor" stroke-width="0.5"/></g></svg></p></div>`);
              that.cartActions.append(`<div class="seperator mt-5"></div><a href="/shop"><button class="btn btn-primary btn-lg w-100">Weiter stöbern</button></a>`);

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
