export function cartItem(args) {
  var order_item_quantity = args['order_item_quantity']
  var order_item_id = args['order_item_id']
  var product_name = args['product_name']
  var product_manager_color_hex = args['product_manager_color_hex']
  var product_manager_color_name = args['product_manager_color_name']
  var product_option_gross = args['product_option_gross']
  var product_option_size = args['product_option_size']
  var product_title_image = args['product_title_image']
  var product_url = args['product_url']
  var shop_url = args['shop_url']

  var html = `
    <div class="container">
      <div class="row">
        <a class="col-auto p-0" style="max-height: 110px; max-width: 70px;" href="${ product_url }">
          <img src="${ product_title_image }" class="img img-fluid w-100 h-100 rounded" alt="${ product_name }">
        </a>
        <a class="col d-flex align-items-center justiy-content-start ml-2" href="${ product_url }">
          <div>
            <h6 class="m-0">${ product_name }</h6>
            <p class="m-0">${ order_item_quantity }x € ${ product_option_gross }</p>
            <p class="m-0" style="color: #${ product_manager_color_hex }">Farbe: ${ product_manager_color_name }</p>
            <p class="m-0">Größe: ${ product_option_size }</p>
          </div>
        </a>
        <div class="col-auto d-flex align-items-center justiy-content-end p-0">
          <div>
            <div >
              <button class="btn w-100 text-strong updateOrderTrigger" data-action="add" data-unique="orderList${ order_item_id }">+</button>
            </div>
            <div>
              <button class="btn updateOrderTrigger" data-action="delete" data-unique="orderList${ order_item_id }">
                <svg class="svg svg--sm svg__fill--info" viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M432 32H312l-9.4-18.7A24 24 0 0 0 281.1 0H166.8a23.72 23.72 0 0 0-21.4 13.3L136 32H16A16 16 0 0 0 0 48v32a16 16 0 0 0 16 16h416a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16zM53.2 467a48 48 0 0 0 47.9 45h245.8a48 48 0 0 0 47.9-45L416 128H32z"></path></svg>
              </button>
            </div>
            <div>
              <button class="btn w-100 text-strong updateOrderTrigger" data-action="remove" data-unique="orderList${ order_item_id }">-</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  `
  return html
}


export function cartItemNull(args) {
  var html = `
    <p class="text-info">
      Du hast noch keine Artikel zu deinem Warenkorb hinzugefügt.
      <svg class="bi bi-bag text-info ml-1" height="1em" style="margin-top: -0.2em;" viewBox="0 0 24.581 26.25" xmlns="http://www.w3.org/2000/svg"><g transform="translate(-2986 -168.75)"><path id="cart" d="M1,6.145H23.581V22.274A3.226,3.226,0,0,1,20.355,25.5H4.226A3.226,3.226,0,0,1,1,22.274Z" transform="translate(2986 168.5)" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12.29,2.113A4.032,4.032,0,0,0,8.258,6.145H6.645a5.645,5.645,0,0,1,11.29,0H16.323A4.032,4.032,0,0,0,12.29,2.113Z" transform="translate(2986 168.5)" fill="currentColor" stroke="currentColor" stroke-width="0.5"/></g></svg>
    </p>
  `
  return html
}


export function cartTotal(args) {
  var checkout_url = args['checkout_url']
  var order_total_gross = args['order_total_gross']

  var html = `
    <hr class="bg-info mt-5">
    <div class="seperator mt-4"></div>

    <div class="row">
      <h5 class="col m-0">Summe:</h5>
      <h5 class="col text-right m-0">€ ${ order_total_gross }</h5>
    </div>
    <p class="text-smaller text-info">*zzgl. Versandkosten</p>

    <div class="seperator mt-4"></div>

    <a href="${ checkout_url }"><button class="btn btn-primary btn-lg w-100">Zur Kassa</button></a>
  `
  return html
}


export function cartTotalNull(args) {
  var html = `
    <div class="seperator mt-5"></div>
    <hr class="bg-info">
    <div class="seperator mt-4"></div>

    <a href="${ shop_url }"><button class="btn btn-primary btn-lg w-100">Weiter Einkaufen</button></a>
  `
  return html
}
