var nav_page     = 2;
var nav_position = 0;

//네비게이션 왼쪽 아이콘 클릭시
$("#left-icon").click(function(){
    if(nav_position < 0) nav_position += 910;
    //$("#nav-item-border").css("left",nav_position+"px");
    $('#nav-item-border').animate({
        left:nav_position
    },400);
});
//네비게이션 오른쪽 아이콘 클릭시
$("#right-icon").click(function(){
    
    if(nav_position > (nav_page-1)*-910)nav_position -= 910;
    $('#nav-item-border').animate({
        left:nav_position
    },400);        
});