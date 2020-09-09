import $ from 'jquery';
import Cookies from 'js-cookie';

class UserGroupFilter {
  constructor() {
    this.filterWomenTrigger = $('.filterWomenTrigger');
    this.filterMenTrigger = $('.filterMenTrigger');

    this.styleGenderFilter();
    this.events();
  }


  events() {
    this.filterWomenTrigger.on("click", this.filterWomen.bind(this));
    this.filterMenTrigger.on("click", this.filterMen.bind(this));
  }


  filterWomen() {
    var that = this;

    console.log(Cookies.set('user_group', 'women'));
  }


  filterMen() {
    var that = this;

    console.log(Cookies.set('user_group', 'men'));
  }


  styleGenderFilter() {
    var that = this

    if (Cookies.get('user_group')) {
      if (Cookies.get('user_group') == 'women') {
        that.filterWomenTrigger.removeClass('btn-outline-info').addClass('btn-primary')
        that.filterMenTrigger.removeClass('btn-primary').addClass('btn-outline-info')
      } else if (Cookies.get('user_group') == 'men') {
        that.filterWomenTrigger.removeClass('btn-primary').addClass('btn-outline-info')
        that.filterMenTrigger.removeClass('btn-outline-info').addClass('btn-primary')
      } else if (Cookies.get('user_group') == 'unisex') {
        that.filterWomenTrigger.removeClass('btn-primary').addClass('btn-outline-info')
        that.filterMenTrigger.removeClass('btn-primary').addClass('btn-outline-info')
      }
    }
  }
}

export default UserGroupFilter;
