import $ from 'jquery'
import './../../../node_modules/popper.js/dist/popper.min.js'
import './../../../node_modules/bootstrap/dist/js/bootstrap.min.js'

// Populate pages with data from api.
import './js/populateProductManager'
import './js/populateWishlistItem'

// Functions
import AcceptCookies from './js/acceptCookies';
import Accordion from './js/accordion';
import Cart from './js/cart';
import Dropdown from './js/dropdown';
import LoginUser from './js/loginUser';
import ProductDetailMaterialsDoughnut from './js/productDetailMaterialsDoughnut';
import ProductDetailNav from './js/productDetailNav';
import ProductDetailTransparencyMapLocations from './js/productDetailTransparencyMapLocations';
import RegisterUser from './js/registerUser';
import Modal from './js/modal';

var modal = new Modal();
var acceptCookies = new AcceptCookies();
var accordion = new Accordion();
var cart = new Cart();
var dropdown = new Dropdown();
var loginUser = new LoginUser();
var productDetailMaterialsDoughnut = new ProductDetailMaterialsDoughnut();
var productDetailNav = new ProductDetailNav();
var productDetailTransparencyMapLocations = new ProductDetailTransparencyMapLocations();
var registerUser = new RegisterUser();

// Scss
import "./app.scss";
