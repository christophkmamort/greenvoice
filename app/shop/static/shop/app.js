import $ from 'jquery';
import './../../../node_modules/popper.js/dist/popper.min.js';
import './../../../node_modules/bootstrap/dist/js/bootstrap.min.js';
import  './../../../node_modules/bootstrap-slider/dist/bootstrap-slider.min.js';


import Accordion from './js/accordion';
import Dropdown from './js/dropdown';
import ProductDetailMaterialsDoughnut from './js/productDetailMaterialsDoughnut';
import ProductDetailNav from './js/productDetailNav';
import ProductDetailTransparencyMapLocations from './js/productDetailTransparencyMapLocations';


var accordion = new Accordion();
var dropdown = new Dropdown();
var productDetailMaterialsDoughnut = new ProductDetailMaterialsDoughnut();
var productDetailNav = new ProductDetailNav();
var productDetailTransparencyMapLocations = new ProductDetailTransparencyMapLocations();



$("#filterPriceSlider").slider({});
$("#filterPriceSlider").on("slide", function(slideEvt) {
	$("#filterPriceMin").text(slideEvt.value[0]);
  $("#filterPriceMax").text(slideEvt.value[1]);
});



// Scss
import "./app.scss";
