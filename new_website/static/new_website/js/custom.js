$(document).ready(function() {
    $('.navbar-menu-list a').hover(
    function() {
        $(this).find('span').animate({width: 'toggle'}, 1000);
    })

    $(document).on('click', '.button-bottom-container', function(){
        $('.curtain').css('top', '0');
        $(".button-bottom-container").hide(3000);
        $('#sidebar').css('transform', 'translateX(0)');
        $('#content-side').css('transform', 'translateX(0)');
        $('body').css('overflow', 'hidden');
    })
})
