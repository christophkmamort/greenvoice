import $ from 'jquery';

class UserRegister {
  constructor() {
    this.registerUserForm = $('#registerUserForm');
    this.registerUserTrigger = $('#registerUserTrigger');
    this.registerEmail = $('#registerEmail');
    this.registerPassword1 = $('#registerPassword1');
    this.registerPassword2 = $('#registerPassword2');
    this.registerHoney = $('input[name="registerHoney"]');
    this.registerUserMessage = $('#registerUserMessage');
    this.events();
  }

  events() {
    this.registerUserTrigger.on("click", this.validateregisterUser.bind(this));
    this.registerEmail.on("click", this.removeRegisterEmailError.bind(this));
    this.registerPassword1.on("click", this.removeRegisterPassword1Error.bind(this));
    this.registerPassword2.on("click", this.removeRegisterPassword2Error.bind(this));
  }

  validateregisterUser() {
    var that = this;

    if (that.registerHoney.val().length == 0) {
      var errors = 0;
      var messages = 0;
      if (that.registerEmail.val().length == 0) {
        that.registerEmail.addClass('form-control-error');
        errors += 1;
        if (messages == 0) {
          that.registerUserMessage.html('Bitte fülle alle notwendigen Felder aus.');
          messages += 1
        }
      }
      if (that.registerEmail.val() && new RegExp(/^(("[\w-+\s]+")|([\w-+]+(?:\.[\w-+]+)*)|("[\w-+\s]+")([\w-+]+(?:\.[\w-+]+)*))(@((?:[\w-+]+\.)*\w[\w-+]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][\d]\.|1[\d]{2}\.|[\d]{1,2}\.))((25[0-5]|2[0-4][\d]|1[\d]{2}|[\d]{1,2})\.){2}(25[0-5]|2[0-4][\d]|1[\d]{2}|[\d]{1,2})\]?$)/i).test(that.registerEmail.val()) == false) {
        that.registerEmail.addClass('form-control-error');
        errors += 1;
        if (messages == 0) {
          that.registerUserMessage.html('Bitte gib eine gültige E-Mail Adresse an.');
          messages += 1
        }
      }
      if (that.registerPassword1.val().length <= 7) {
        that.registerPassword1.addClass('form-control-error');
        errors += 1;
        if (messages == 0) {
          that.registerUserMessage.html('Dein Passwort muss mindestens 8 Zeichen lang.');
          messages += 1
        }
      }
      if (that.registerPassword1.val() != that.registerPassword2.val()) {
        that.registerPassword1.addClass('form-control-error');
        that.registerPassword2.addClass('form-control-error');
        if (messages == 0) {
          that.registerUserMessage.html('Die beiden Passwörter stimmen nicht überein.');
          messages += 1
        }
        errors += 1;
      }

      if (errors == 0) {
        that.registerEmail.removeClass('form-control-error');
        that.registerPassword1.removeClass('form-control-error');
        that.registerPassword2.removeClass('form-control-error');
        that.registerUserMessage.html('');

        that.registerUserForm.submit();
      }
    }
  }

  removeRegisterEmailError() {
    var that = this;

    that.registerEmail.removeClass('form-control-error');
    that.registerUserMessage.html('');
  }

  removeRegisterPassword1Error() {
    var that = this;

    that.registerPassword1.removeClass('form-control-error');
    that.registerPassword2.removeClass('form-control-error');
    that.registerUserMessage.html('');
  }

  removeRegisterPassword2Error() {
    var that = this;

    that.registerPassword1.removeClass('form-control-error');
    that.registerPassword2.removeClass('form-control-error');
    that.registerUserMessage.html('');
  }
}

export default UserRegister;
