import $ from 'jquery';
import './../../../node_modules/popper.js/dist/popper.min.js';
import './../../../node_modules/bootstrap/dist/js/bootstrap.min.js';


// Api
import BrandList from './js/brandList';
import CategoryList from './js/categoryList';
import ProductList from './js/productList';

var brandList = new BrandList();
var categoryList = new CategoryList();
var productList = new ProductList();


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
