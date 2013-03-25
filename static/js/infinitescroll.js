$(function () {
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

    $container.infinitescroll({
        navSelector  : "#pagination",            
        nextSelector : "#pagination a:first",    
        itemSelector : ".item",
        loading: {
            finishedMsg: finishedMsg,
            msgText: msgText,
            img: '/static/img/loading.gif',
        }
    },
    // trigger Masonry as a callback
    function( newElements ) {
        // hide new items while they are loading
        var $newElems = $( newElements ).css({ opacity: 0 });
        // ensure that images load before adding to masonry layout
        $newElems.imagesLoaded(function(){
            // show elems now they're ready
            $newElems.animate({opacity: 1});
            $container.masonry('appended', $newElems, true); 
        });
    });
});
