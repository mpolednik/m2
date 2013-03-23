// Fade flashes 2.5 secs after page load
$('.flashes').delay(2500).fadeOut(300);

// Initiate masonry
var $container = $('.masonry');
$container.imagesLoaded(function(){
    $container.masonry({
        itemSelector: '.item',
        columnWidth: function( containerWidth ) {
            return containerWidth / 4;
        }
    });
});
