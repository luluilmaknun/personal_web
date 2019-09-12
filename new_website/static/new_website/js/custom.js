$(document).ready(function() {
    $('.navbar-menu-list a').hover(
    function() {
        $(this).find('span').animate({width: 'toggle'}, 1000);
    })
})