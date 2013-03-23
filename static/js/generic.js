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

// hide #back-top first
$("#back-top").hide();

// Back to top
$(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
        $('.back-top').fadeIn();
    } else {
        $('.back-top').fadeOut();
    }
});

// scroll body to 0px on click
$('.back-top a').click(function () {
    $('body,html').animate({
        scrollTop: 0
        }, 800);
        return false;
});
