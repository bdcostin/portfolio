'use strict'

var $ = require('jquery')

$(document).scroll(function () {
  var yAxis = $(this).scrollTop()
  if (yAxis > 350) {
    $('.sidenav-icons-spacing').fadeIn()
    $('.title').fadeIn()
  } else {
    $('.sidenav-icons-spacing').fadeOut()
    $('.title').fadeOut()
  }
})

$(document).ready('.accordion').on('click', '.accordion-header', function () {
  // will (slide) toggle the related panel.
  $(this)
    .toggleClass('active')
    .next()
    .slideToggle()
})
