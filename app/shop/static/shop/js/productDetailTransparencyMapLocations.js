import $ from 'jquery';

class ProductDetailTransparencyMapLocations {
  constructor() {
    this.transparencyMap = $('#productDetailTransparencyMap');
    if (this.transparencyMap.length > 0) {
      this.transparencyMapCountries = this.transparencyMap.data('countries').split('; ');
      this.transparencyMapCoordinates = this.transparencyMap.data('coordinates').split('; ');
      this.transparencyMapColor = this.transparencyMap.find('input').css('background-color').split('(')[0] +'a('+ this.transparencyMap.find('input').css('background-color').split('(')[1].split(')')[0] +', 0.5)';
      this.percentTop;
      this.percentLeft;
      this.transparencySetMapLocations();
    }
  }

  transparencySetMapLocations(e) {
    var that = this;

    // Countries
    $.each(that.transparencyMapCountries, function() {
      $('#'+ this).css({'fill':that.transparencyMapColor});
    });

    // Locations
    var coordinateSystemTopArray = ["84:60:0:26", "60:30:26:47.3", "30:0:47.3:64.6", "0:-30:64.6:81.7", "-30:-55:81.7:100"];
    var coordinateSystemLeftArray = ["-170:-150:0:5.5", "-150:-120:5.5:13.8", "-120:-90:13.8:22.1", "-90:-60:22.1:30.4", "-60:-30:30.4:38.7", "-30:0:38.7:47.1", "0:30:47.1:55.4", "30:60:55.4:63.7", "60:90:63.7:72.1", "90:120:72.1:80.4", "120:150:80.4:88.65", "150:180:88.65:96.9", "-180:-170:96.9:100"];

    $.each(that.transparencyMapCoordinates, function(index) {
      var coordinates = this.split(', ');

      // Calc top % position on svg map
      $.each(coordinateSystemTopArray, function() {
        var coordinatesTop = this.split(':');
        if (parseFloat(coordinatesTop[0]) >= parseFloat(coordinates[0]) && parseFloat(coordinates[0]) > parseFloat(coordinatesTop[1])) {
          that.percentTop = (parseFloat(coordinatesTop[2]) - parseFloat(coordinatesTop[3])) / (parseFloat(coordinatesTop[0]) - parseFloat(coordinatesTop[1])) * (parseFloat(coordinatesTop[0]) - parseFloat(coordinates[0])) * -1 + parseFloat(coordinatesTop[2]);
        }
      });

      // Calc left % position on svg map
      $.each(coordinateSystemLeftArray, function() {
        var coordinatesLeft = this.split(':');
        if (parseFloat(coordinatesLeft[0]) <= parseFloat(coordinates[1]) && parseFloat(coordinates[1]) < parseFloat(coordinatesLeft[1])) {
          that.percentLeft = (parseFloat(coordinatesLeft[2]) - parseFloat(coordinatesLeft[3])) / (parseFloat(coordinatesLeft[0]) - parseFloat(coordinatesLeft[1])) * (parseFloat(coordinatesLeft[0]) - parseFloat(coordinates[1])) * -1 + parseFloat(coordinatesLeft[2]);
        }
      });

      that.transparencyMap.append(`<div class="bg-primary text-white circle d-flex align-items-enter justify-content-center" style="height: 1.3em; width: 1.3em; position: absolute; top: `+ that.percentTop +`%; left: `+ that.percentLeft +`%; transform: translate(-0.65em, -0.65em); font-size: 0.8em;">`+ (index + 1) +`</div>`);
    });
  }
}

export default ProductDetailTransparencyMapLocations;
