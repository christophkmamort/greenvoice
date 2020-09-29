export function categoryButtonSm(args) {
  var category_name = args['category_name']
  var category_url = args['category_url']
  var url_param_category__name = args['url_param_category__name']

  var btn_css = `btn-outline-dark`
  if (category_name == url_param_category__name) {
    btn_css = `btn-primary`
  }

  var html = `
    <a href="${ category_url }">
      <button class="btn btn-sm mr-1 mb-2 ${ btn_css }">
        ${ category_name }
      </button>
    </a>
  `
  return html
}


export function categoryButtonLg(args) {
  var category_name = args['category_name']
  var category_url = args['category_url']
  var url_param_category__name = args['url_param_category__name']

  var btn_css = `btn-outline-dark`
  if (category_name == url_param_category__name) {
    btn_css = `btn-primary`
  }

  var html = `
    <a href="${ category_url }">
      <button class="btn btn-lg ml-2 ${ btn_css }">
        ${ category_name }
      </button>
    </a>
  `
  return html
}


export function categoryButtonMobileMenu(args) {
  var category_name = args['category_name']
  var category_url = args['category_url']

  var html = `
    <li class="border-bottom border-white p-2">
      <a href="${ category_url }">
        <button class="btn m-0 p-0 w-100">
          <div class="d-flex align-items-center">
            <h5 class="text-white m-0 mr-auto text-regular">${ category_name }</h5>
            <svg class="bi bi-chevron-right text-white" height="0.8em" viewBox="0 0 21.181 35.992" xmlns="http://www.w3.org/2000/svg"><path d="M5.233,8.233a2.5,2.5,0,0,1,3.538,0L22,21.462,35.22,8.233a2.5,2.5,0,0,1,3.538,3.538L23.765,26.765a2.5,2.5,0,0,1-3.538,0L5.233,11.772a2.5,2.5,0,0,1,0-3.538Z" transform="translate(-6.818 39.991) rotate(-90)" fill="currentColor" stroke="2" stroke-width="1" fill-rule="evenodd"/></svg>
          </div>
        </button>
      </a>
    </li>
  `
  return html
}


export function categoryBreadcrumbs(args) {
  var category_name = args['category_name']
  var category_url = args['category_url']

  var breadcrumb_item_class = 'breadcrumb-item'
  if (1 == 0) {
    var breadcrumb_item_class = 'breadcrumb-item active'
  }

  var html = `
    <li class="${ breadcrumb_item_class }"><a href="${ category_url }">${ category_name }</a></li>
  `
  return html
}
