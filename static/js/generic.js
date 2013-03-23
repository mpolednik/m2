// Fade flashes 2.5 secs after page load
$('.flashes').delay(2500).fadeOut(300);

// Highlight images on mouse oever
$('.item').mouseover(function () {
    $(this).css('background-color', '#ccc'); 
    $(this).css('border', '1px solid #adadad'); 
}).mouseout(function () {
    $(this).css('background-color', '#efefef'); 
    $(this).css('border', '1px solid #e7e7e7'); 
});

// Initiate masonry
var $container = $('.masonry');
$container.imagesLoaded(function(){
  $container.masonry({
    itemSelector : '.item',
  });
});
