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

    $(document).on('click', '#arrowBack', function(){
        $('body').css('overflow', 'auto');
        $('#content-side').css('transform', 'translateX(100%)');
        $('#sidebar').css('transform', 'translateX(-100%)');
        $(".button-bottom-container").show(1000);
        $('.curtain').css('top', 'auto');
    });

    $('#sidebarCollapse').on('click', function(){
        $('.overlay').animate({width: "toggle"});
        $('#sidebar').animate({width: "toggle"});
    });

    $('.overlay').on('click', function(){
        $('#sidebar').animate({width: "toggle"});
        $('.overlay').animate({width: "toggle"});
    });
})
