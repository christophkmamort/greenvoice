export function checkbox(args) {
  var name = args['name']
  var value = args['value']

  var html = `
    <label class="checkbox">
      <input type="checkbox" name="productFilterBrands" value="${ value }">
      <div class="checkbox-box checkbox-box-dark">
        <svg class="text-white checkbox-icon" height="0.7em" viewBox="0 0 15 11.942" xmlns="http://www.w3.org/2000/svg"><path d="M16.725,5.158a1.377,1.377,0,1,1,1.966,1.928l-7.329,9.161a1.377,1.377,0,0,1-1.983.037L4.524,11.426A1.377,1.377,0,1,1,6.47,9.48l3.844,3.843L16.69,5.2a.433.433,0,0,1,.037-.04Z" transform="translate(-4.085 -4.745)" fill="currentColor" fill-rule="evenodd"/></svg>
      </div>
      <h6 class="checkbox-text checkbox-text-dark m-0 ml-2">${ name }</h6>
    </label>
  `
  return html
}
