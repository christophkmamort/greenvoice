import $ from 'jquery'
import './../../../node_modules/popper.js/dist/popper.min.js'
import './../../../node_modules/bootstrap/dist/js/bootstrap.min.js'

// Populate pages with data from api.
import './js/populateBrandList'
import './js/populateCategoryList'
import './js/populateOrderList'
import './js/populateProductList'
import './js/populateWishlistList'

// Page functionality.
import './js/acceptCookies'

import Accordion from './js/accordion';
import Dropdown from './js/dropdown';
import LoginUser from './js/loginUser';
import ProductDetailMaterialsDoughnut from './js/productDetailMaterialsDoughnut';
import ProductDetailNav from './js/productDetailNav';
import ProductDetailTransparencyMapLocations from './js/productDetailTransparencyMapLocations';
import RegisterUser from './js/registerUser';
import Modal from './js/modal';

var accordion = new Accordion();
var dropdown = new Dropdown();
var loginUser = new LoginUser();
var productDetailMaterialsDoughnut = new ProductDetailMaterialsDoughnut();
var productDetailNav = new ProductDetailNav();
var productDetailTransparencyMapLocations = new ProductDetailTransparencyMapLocations();
var registerUser = new RegisterUser();
var modal = new Modal();

// Scss
import "./app.scss";
