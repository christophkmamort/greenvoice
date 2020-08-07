import $ from 'jquery';
import Cookies from 'js-cookie';

class AcceptCookies {
  constructor() {
    this.cookieNotice = $('#cookieNotice');
    this.acceptCookiesTrigger = $('#acceptCookiesTrigger');
    this.events();
  }

  events() {
    this.acceptCookiesTrigger.on("click", this.acceptCookies.bind(this));
  }

  acceptCookies() {
    var that = this;

    console.log(Cookies.set('cookies_accepted', true));
    that.cookieNotice.slideUp();
  }
}

export default AcceptCookies;
