import $ from 'jquery';
var Chart = require('chart.js');

class ProductDetailMaterialsDoughnut {
  constructor() {
    this.productDetailInfoMaterialsChart = $('#productDetailInfoMaterialsChart');
    this.productDetailInfoMaterial = $('.productDetailInfoMaterial');
    if (this.productDetailInfoMaterialsChart.length > 0) {
      this.buildProductDetailInfoMaterialsDoughnut();
    }
  }

  buildProductDetailInfoMaterialsDoughnut() {
    var that = this;
    var themeColors = that.productDetailInfoMaterialsChart.data('colors').split(', ');
    var productMaterials = [];
    var productMaterialsAmount = [];
    that.productDetailInfoMaterial.each(function(i) {
      productMaterials.push($(this).data('material'));
      productMaterialsAmount.push($(this).data('amount'));

      // Set color of dots
      $(this).closest('.d-flex').find('svg').css({'fill':themeColors[i]});
    });

    var productDetailInfoMaterialsDoughnut = new Chart(productDetailInfoMaterialsChart, {
        type: 'doughnut',
    		data: {
    			labels: productMaterials,
    			datasets: [
    				{
    					backgroundColor: themeColors,
    					data: productMaterialsAmount,
              borderWidth: 4,
              borderColor: "#FCFAFA",
    	      }
    			],
    		},
        options: {
    			cutoutPercentage: 70,
    			legend: {
            display: false,
        	},
    			tooltips: {
             enabled: false,
        	},
    		},
    });
  }
}

export default ProductDetailMaterialsDoughnut;
