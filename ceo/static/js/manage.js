
check_slide();


$(".menu-on-off").click(function(){
    slide($(this),$(this).attr("on-off")); 
});
$(".menu-item").click(function(){
    var keyword = $(this).attr("value");
    if(keyword == "레시피등록") location.href="/manager/write/recipe";
    else if(keyword == "레시피관리") location.href="manage_recipe.html";
    else if(keyword == "보관방법작성") location.href="/manager/write/storage";
    else location.href="manage_storage.html";

});
function check_slide(){
    
    for(var el of $(".menu-on-off")){
        if($(el).attr("on-off").toLowerCase() == "on") slide(el,"off");
    }
}
function slide(el,sw){
    
    if(sw.toLowerCase() == "on"){
        $(el).next("ul").css("display","none");
        $(el).attr("on-off","off");
        $(el).children("i").attr("class","glyphicon glyphicon-chevron-right");
    }else{
        $(el).next("ul").css("display","block");
        $(el).attr("on-off","on");
        $(el).children("i").attr("class","glyphicon glyphicon-chevron-down");
    }
}