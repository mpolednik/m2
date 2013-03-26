$(function () {
    if ($('.flashes').is('*')) {
        $('.container').css({opacity: 0.6});
    }
    // Fade flashes 2.5 secs after page load
    $('.flashes').delay(2500).fadeOut(300, function() {
        $('.container').animate({opacity: 1});
    });

    // hide pagination
    $('#pagination').hide();

    // hide #back-top first
    $(".back-top").hide();

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
});
