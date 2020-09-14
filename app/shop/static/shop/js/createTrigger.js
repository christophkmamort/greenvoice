import $ from 'jquery'
import * as test from './test.js'


function createTrigger(args) {
  var currentElem = args['currentElem']
  var index = args['index']

  currentElem.append(`<button class="btn btn-primary triggerLog" data-unique="${ index }">Test log</button>`)

  var triggerLog = $(`.triggerLog[data-unique="${ index }"]`)
  triggerLog.on("click", function() {
    var txt = 'This is working!'
    test.logTxt(txt)
  })
}

var triggerArea = $('.triggerArea')
if (triggerArea) {
  triggerArea.each(function(index) {
    var args = {
      'index': index,
      'currentElem': $(this),
    }
    createTrigger(args)
  })
}
