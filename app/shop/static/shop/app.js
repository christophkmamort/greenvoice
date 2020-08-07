import $ from 'jquery';
import './../../../node_modules/popper.js/dist/popper.min.js';
import './../../../node_modules/bootstrap/dist/js/bootstrap.min.js';
import  './../../../node_modules/bootstrap-slider/dist/bootstrap-slider.min.js';


import AcceptCookies from './js/acceptCookies';
import Accordion from './js/accordion';
import Dropdown from './js/dropdown';
import LoginUser from './js/loginUser';
import ProductDetailMaterialsDoughnut from './js/productDetailMaterialsDoughnut';
import ProductDetailNav from './js/productDetailNav';
import ProductDetailTransparencyMapLocations from './js/productDetailTransparencyMapLocations';
import RegisterUser from './js/registerUser';


var acceptCookies = new AcceptCookies();
var accordion = new Accordion();
var dropdown = new Dropdown();
var loginUser = new LoginUser();
var productDetailMaterialsDoughnut = new ProductDetailMaterialsDoughnut();
var productDetailNav = new ProductDetailNav();
var productDetailTransparencyMapLocations = new ProductDetailTransparencyMapLocations();
var registerUser = new RegisterUser();



$("#filterPriceSlider").slider({});
$("#filterPriceSlider").on("slide", function(slideEvt) {
	$("#filterPriceMin").text(slideEvt.value[0]);
  $("#filterPriceMax").text(slideEvt.value[1]);
});



// Scss
import "./app.scss";
