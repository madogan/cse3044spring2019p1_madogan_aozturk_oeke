$(document).ready(function(){
    if (window.location.pathname.includes("/experts")) {
        $(".nav li[class=active]").toggleClass("active");
        $("#btn-experts").addClass("active");
    } else if (window.location.pathname.includes("/about")) {
        $(".nav li[class=active]").toggleClass("active");
        $("#btn-about").addClass("active");
    } else if (window.location.pathname.includes("/q_a")) {
        $(".nav li[class=active]").toggleClass("active");
        $("#btn-q_a").addClass("active");
    } else if (window.location.pathname == "/" || window.location.pathname.includes("/index")) {
        $(".nav li[class=active]").toggleClass("active");
        $("#btn-index").addClass("active");
    }
});
