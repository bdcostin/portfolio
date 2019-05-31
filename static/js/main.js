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

document.addEventListener('mousemove', function (event) {
  const x = event.pageX
  const y = event.pageY

  document.querySelectorAll('section div').forEach(div => {
    const dx = div.offsetLeft + 50 - x
    const dy = div.offsetTop + 50 - y
    const dist = Math.sqrt(dx * dx + dy * dy)

    const score = Math.exp(dist * -0.003)

    div.style.transform = 'scale(' + score + ')'
    div.style.fontWeight = 100 + (100 * Math.floor(8 * score))
  })
})
