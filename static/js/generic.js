$('.flashes').delay(2500).fadeOut(300)

$(function(){
  $('.row').masonry({
    // options
    itemSelector : '.unit',
    columnWidth : 240
  });
});
