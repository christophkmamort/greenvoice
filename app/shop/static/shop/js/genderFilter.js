import $ from 'jquery';
import Cookies from 'js-cookie';

class GenderFilter {
  constructor() {
    this.filterWomenTrigger = $('.filterWomenTrigger');
    this.filterMenTrigger = $('.filterMenTrigger');
    // this.filterUnisexTrigger = $('.filterUnisexTrigger');

    this.styleGenderFilter();
    this.events();
  }


  events() {
    this.filterWomenTrigger.on("click", this.filterWomen.bind(this));
    this.filterMenTrigger.on("click", this.filterMen.bind(this));
    // this.filterUnisexTrigger.on("click", this.filterUnisex.bind(this));
  }


  filterWomen() {
    var that = this;

    console.log(Cookies.set('filter_gender', 'women'));
  }


  filterMen() {
    var that = this;

    console.log(Cookies.set('filter_gender', 'men'));
  }


  /*filterUnisex() {
    var that = this;

    console.log(Cookies.set('filter_gender', 'unisex'));
  }*/


  styleGenderFilter() {
    var that = this

    if (Cookies.get('filter_gender')) {
      if (Cookies.get('filter_gender') == 'women') {
        that.filterWomenTrigger.removeClass('btn-outline-info').addClass('btn-primary')
        that.filterMenTrigger.removeClass('btn-primary').addClass('btn-outline-info')
      } else if (Cookies.get('filter_gender') == 'men') {
        that.filterWomenTrigger.removeClass('btn-primary').addClass('btn-outline-info')
        that.filterMenTrigger.removeClass('btn-outline-info').addClass('btn-primary')
      } else if (Cookies.get('filter_gender') == 'unisex') {
        that.filterWomenTrigger.removeClass('btn-primary').addClass('btn-outline-info')
        that.filterMenTrigger.removeClass('btn-primary').addClass('btn-outline-info')
      }
    }
  }
}

export default GenderFilter;
