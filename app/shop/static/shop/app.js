import $ from 'jquery'
import './../../../node_modules/popper.js/dist/popper.min.js'
import './../../../node_modules/bootstrap/dist/js/bootstrap.min.js'

// Api
// import BrandList from './js/brandList';
// import CategoryList from './js/categoryList';
// import UserGroupFilter from './js/userGroupFilter';
// import ProductList from './js/productList';
// import ProductSearch from './js/productSearch';

// var brandList = new BrandList();
// var categoryList = new CategoryList();
// var userGroupFilter = new UserGroupFilter();
// var productList = new ProductList();
// var productSearch = new ProductSearch();


// Populate pages with data from api.
import './js/populateProductManager'
import './js/populateWishlistItem'


// Manage user interactions with api.



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

// Testing
import './js/test';

// Scss
import "./app.scss";
