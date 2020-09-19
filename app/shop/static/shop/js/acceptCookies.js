import $ from 'jquery'
import Cookies from 'js-cookie'


// Constructor.
var cookieNotice = $('.cookieNotice')
if (cookieNotice) {
  var acceptCookieNoticeTrigger = $('.acceptCookieNoticeTrigger')
  if (acceptCookieNoticeTrigger) {
    var args = {
      'cookieNotice':cookieNotice,
      'acceptCookieNoticeTrigger':acceptCookieNoticeTrigger,
    }
    cookieNoticeEvents(args)
  }
}


// Functions.
function cookieNoticeEvents(args) {
  var acceptCookieNoticeTrigger = args['acceptCookieNoticeTrigger']
  acceptCookieNoticeTrigger.on("click", function() {
    acceptCookieNotice(args);
  })
}


function acceptCookieNotice(args) {
  var cookieNotice = args['cookieNotice']

  Cookies.set('acceptCookieNotice', true)
  cookieNotice.slideUp()
}
