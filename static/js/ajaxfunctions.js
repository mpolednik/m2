var vote = function (path, id, rating) {
    var data = {'id': id,
                'rating': rating};

    $.getJSON(path, data, function(result) {
        $('#vote_'+id).html(result.rating);
        if (result.rated == 1) {
            var element = $('#upvote_'+id);
            element.addClass('upvoted');
        } else if (result.rated == -1) {
            var element = $('#downvote_'+id);
            element.addClass('downvoted');
        } else {
            var element = $('#downvote_'+id);
            element.removeClass('downvoted');
            var element = $('#upvote_'+id);
            element.removeClass('upvoted');
        }
    });
};

var delete_comment = function (id) {
    $.getJSON('/ajax/delete_comment/'+id, function(result) {
        $('#delete_'+id).hide();
        $('#actions_'+id).hide();
        var element = $('#'+id);
        element.html('<span class="note">'+result.text+'</span>');
    });
};
