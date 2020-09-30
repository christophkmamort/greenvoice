// 3rd party
import $ from 'jquery'
import './../../../node_modules/popper.js/dist/popper.min.js'
import './../../../node_modules/bootstrap/dist/js/bootstrap.min.js'

// Custom
import './js/acceptCookies'
import './js/populateBrandList'
import './js/populateCategoryList'
import './js/populateOrderList'
import './js/populateProductFilter'
import './js/populateProductList'
import './js/populateWishlistList'

import Accordion from './js/accordion';
import Dropdown from './js/dropdown';
import Modal from './js/modal';
import UserLogin from './js/userLogin';
import UserRegister from './js/userRegister';

var accordion = new Accordion();
var dropdown = new Dropdown();
var modal = new Modal();
var userLogin = new UserLogin();
var userRegister = new UserRegister();


/*import ProductDetailMaterialsDoughnut from './js/productDetailMaterialsDoughnut';
import ProductDetailNav from './js/productDetailNav';
import ProductDetailTransparencyMapLocations from './js/productDetailTransparencyMapLocations';

var productDetailMaterialsDoughnut = new ProductDetailMaterialsDoughnut();
var productDetailNav = new ProductDetailNav();
var productDetailTransparencyMapLocations = new ProductDetailTransparencyMapLocations();*/


// Scss
import "./app.scss";

// Webpack browser sync
if (module.hot) {
  module.hot.accept()
}
