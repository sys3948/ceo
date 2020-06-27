var price = 0;

$("#food-select").change(function() {
    if($(this).val() != "재료선택"){
        $("#food-meta").css("display","block");
        var food_price = parseInt($("#food-select > option:selected").attr("price"));
        // var price = parseInt($("#total").text()) + food_price;
        price += food_price;
        $("#total").text(price);
        var number = $(".food").length + 1;
        var tag = "<li class='food'>\
                        <span style='margin-left:11px;'><b class='food-num'>"+number+"</b>.&nbsp;&nbsp;"+$(this).val()+"</span>\
                        <span><input type='number' value='1' min='1' class='num' price='"+food_price+"'></span>\
                        <span class='price'>"+food_price+"원</span>\
                        <span class='glyphicon glyphicon-trash text-center delete-food' style='cursor:pointer;'></span>\
                </li>";
        $("#food-list").append(tag);
    }
});
$(document).on("click",".delete-food",function(){
    price -= $(this).prev("span.price").text().replace("원", "");
    $(this).parent("li").remove();
    if($(".food").length == 0){
        $("#food-meta").css("display","none");

    }else{
        $("#total").text(price);
    }
    var n = 1;
    for(var num of $(".food-num")){
        $(num).text(n)
        n++;
    }

});

$(document).on("change",".num",function(){
    price = getToatal();
    $("#total").text(price);
});
function getToatal(){
    var sum = 0;
    for(var n of $(".num")){
        sum+=(parseInt($(n).val())*parseInt($(n).attr("price")));
    }
    return sum;
}