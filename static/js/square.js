$(function() {
    $('#navigation a').stop().animate({'right':'-85px'},1000);

    $('#navigation > li').hover(
        function () {
            $('a',$(this)).stop().animate({'right':'-2px'},200);
        },
        function () {
            $('a',$(this)).stop().animate({'right':'-85px'},200);
        }
    );
});