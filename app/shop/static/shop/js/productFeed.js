import $ from 'jquery';

class ProductFeed {
  constructor() {
    this.productWrapper = $('#p-wrap')
    this.productApiListUrl = "http://localhost:8000/api/products/"
    this.outputProductList()
  }

  /*events() {
    this.formTrigger.on("click", this.manageForm.bind(this));
  }*/

  outputProductList(e) {
    var that = this;
    fetch(that.productApiListUrl)
    .then((resp) => resp.json())
    .then(function(data) {
        console.log('Data:', data)

        var list = data;
        for (var i in list) {
          var item = `
            <div>
              ${list[i].title}
            </div>
          `
          console.log(that.productWrapper.html(item))

          that.productWrapper.innerHTML += item
        }
    })
  }
}

export default ProductFeed;
