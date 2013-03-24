var get_sms_cnt = function () {
    $.getJSON('/ajax/smsstate', function(data) {
        $('.state').html(data.state)
    });
}

var timer = setInterval(get_sms_cnt, 5000)
