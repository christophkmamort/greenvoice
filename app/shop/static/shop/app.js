import './../../../node_modules/popper.js/dist/popper.min.js';
import './../../../node_modules/bootstrap/dist/js/bootstrap.min.js';
var Chart = require('chart.js');
import  './../../../node_modules/bootstrap-slider/dist/bootstrap-slider.min.js';

import Accordion from './js/accordion';
import Dropdown from './js/dropdown';

var accordion = new Accordion();
var dropdown = new Dropdown();

$("#filterPriceSlider").slider({});
$("#filterPriceSlider").on("slide", function(slideEvt) {
	$("#filterPriceMin").text(slideEvt.value[0]);
  $("#filterPriceMax").text(slideEvt.value[1]);
});

var myDoughnutChart = new Chart(productInfoMaterialsChart, {
    type: 'doughnut',
		data: {
			labels: ["BIO-Baumwolle", "Hanf", "Recyceltes PET"],
			datasets: [
				{
					backgroundColor: ["#404040", "#BFBFBF","#7FC6A4"],
					data: [50,35,15],
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

// Scss
import "./app.scss";
