'use strict'

const $ = require('jquery')

$(document).scroll(function () {
  const yAxis = $(this).scrollTop()
  const windowWidth = $(window).width()
  if ((yAxis < 350) && (windowWidth > 1000)) {
    $('.sidenav-icons-spacing').fadeOut()
    $('.title').fadeOut()
  } else {
    $('.sidenav-icons-spacing').fadeIn()
    $('.title').fadeIn()
  }
})

$(document).ready(function () {
  const windowWidth = $(window).width()
  if (windowWidth < 1000) {
    $('.sidenav').remove()
    $('.main').css({ 'margin-left': '15px', 'margin-right': '15px' })
    $('.footer').css({ 'margin-right': '15px' })
    $('.plato-speaks').css({ 'margin-left': '70px', 'margin-top': '10px' })
  } else {
    $('.container').hide()
  }
})

$(document).ready('.accordion').on('click', '.accordion-header', function () {
  $(this)
    .toggleClass('active')
    .next()
    .slideToggle()
})
