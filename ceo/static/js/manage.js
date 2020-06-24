
check_slide();


$(".menu-on-off").click(function(){
    slide($(this),$(this).attr("on-off")); 
});
$(".menu-item").click(function(){
    var keyword = $(this).attr("value");
    if(keyword == "레시피등록") location.href="/manager/write/recipe";
    else if(keyword == "레시피관리") location.href="/manager/manage/recipe";
    else if(keyword == "보관방법작성") location.href="/manager/write/storage";
    else if(keyword == "보관방법관리") location.href="/manager/show/storage";
    else if(keyword == "관리자등록") location.href="/manage/register";
    else if(keyword == "관리자관리") alert('아직 구현하지 않은 페이지 입니다.');
    else alert('오류가 발생했습니다.');
    

});
function check_slide(){
    
    for(var el of $(".menu-on-off")){
        console.log(el);
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