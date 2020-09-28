export function marginLeft() {
  var html = `<div class="feed-padding-left"></div>`
  return html
}


export function marginRight() {
  var html = `<div class="feed-padding-right"></div>`
  return html
}


export function productItem(args) {
  var product_gross_from = args['product_gross_from']
  var product_gross_info_txt = args['product_gross_info_txt']
  var product_manager_id = args['product_manager_id']
  var product_name = args['product_name']
  var product_title_image = args['product_title_image']
  var product_url = args['product_url']
  var product_wrapper_class = args['product_wrapper_class']

  var html = `
    <div class="${ product_wrapper_class }">
      <div class="overflow-hidden position-relative feed-product-img">
        <a href="${ product_url }">
          <div class="position-absolute" style="left: 0; top: 0; right: 0; bottom: 0;">
            <img class="img w-100 h-100" src="${ product_title_image }" alt="">
          </div>
        </a>

        <div class="position-absolute updateWishlistTriggerWrapper" data-unique="productList${ product_manager_id }" style="top:0.5em; right:0.5em;">
        </div>
      </div>
      <a href="${ product_url }" class="text-decoration-none">
        <div class="pt-2 pr-2 pl-2">
          <p class="m-0 p-0 mt-1 text-truncate">${ product_name }</p>
          <h6 class="m-0 p-0 mt-1 text-small"><span class="text-dark text-strong">${ product_gross_info_txt }€ ${ product_gross_from }</span></h6>
          </div>
        </div>
      </a>
    </div>
  `
  return html
}
