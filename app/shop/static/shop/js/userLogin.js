import $ from 'jquery';

class UserLogin {
  constructor() {
    this.loginUserForm = $('#loginUserForm');
    this.loginUserTrigger = $('#loginUserTrigger');
    this.loginEmail = $('input[name ="loginEmail"]');
    this.loginPassword = $('input[name ="loginPassword"]');
    this.loginUserMessage = $('#loginUserMessage');
    this.events();
  }

  events() {
    this.loginUserTrigger.on("click", this.validateLoginUser.bind(this));
    this.loginEmail.on("click", this.removeLoginEmailError.bind(this));
    this.loginPassword.on("click", this.removeLoginPasswordError.bind(this));
  }

  validateLoginUser() {
    var that = this;

    var errors = 0;
    var messages = 0;
    if (that.loginEmail.val().length == 0) {
      that.loginEmail.addClass('form-control-error');
      errors += 1;
      if (messages == 0) {
        that.loginUserMessage.html('Bitte fülle alle notwendigen Felder aus.');
        messages += 1
      }
    }
    if (that.loginEmail.val() && new RegExp(/^(("[\w-+\s]+")|([\w-+]+(?:\.[\w-+]+)*)|("[\w-+\s]+")([\w-+]+(?:\.[\w-+]+)*))(@((?:[\w-+]+\.)*\w[\w-+]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][\d]\.|1[\d]{2}\.|[\d]{1,2}\.))((25[0-5]|2[0-4][\d]|1[\d]{2}|[\d]{1,2})\.){2}(25[0-5]|2[0-4][\d]|1[\d]{2}|[\d]{1,2})\]?$)/i).test(that.loginEmail.val()) == false) {
      that.loginEmail.addClass('form-control-error');
      errors += 1;
      if (messages == 0) {
        that.loginUserMessage.html('Bitte gib deine gültige E-Mail Adresse an.');
        messages += 1
      }
    }
    if (that.loginPassword.val().length == 0) {
      that.loginPassword.addClass('form-control-error');
      errors += 1;
      if (messages == 0) {
        that.loginUserMessage.html('Bitte gib dein gültiges Passwort ein.');
        messages += 1
      }
    }

    if (errors == 0) {
      that.loginEmail.removeClass('form-control-error');
      that.loginPassword.removeClass('form-control-error');

      that.loginUserForm.submit();
    }
  }

  removeLoginEmailError() {
    var that = this;

    that.loginEmail.removeClass('form-control-error');
  }

  removeLoginPasswordError() {
    var that = this;

    that.loginPassword.removeClass('form-control-error');
  }
}

export default UserLogin;
