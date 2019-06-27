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
    $('.top-nav').remove()
    $('.container').removeClass('hide-container')
    $('.main').removeClass('full-spacing')
    $('.main').addClass('small-spacing')
    $('.footer').css({ 'margin-right': '15px' })
    $('.plato-speaks').css({ 'margin-left': '70px', 'margin-top': '10px' })
  } else {
    $('.container').hide()
  }
})

$(document).ready(function () {
  const windowWidth = $(window).width()
  if (windowWidth > 1500) {
    $('.sidenav').css({ 'margin-left': '670px' })
  }
})
