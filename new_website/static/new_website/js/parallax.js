$(function() {
    var parallax_layers = 6;

    $(window).scroll(function() {
        var count = 0;

        $('div[class*=parallax__layer__]').each(function() {
            var x = (parallax_layers - count) / 10;
            var transform = 'translateY(-' + ($(window).scrollTop() * count / parallax_layers) + 'px)';
            $(this).css('transform', transform);

            if(count == 6) {
                $('.parallax__layer_after').css('transform', transform);
            }
            count++;
        });
    })
})
