//아이디 체크
$("#check-btn").click(function(){
    userIdCheck(); 
});
$("#user-id").focusout(function(){
    userIdCheck(); 
});
$("#pwd2").focusout(function(){
    pwCompare();
});
function pwCompare(){
    if($("#pwd").val() != $("#pwd2").val()){
        $("#pw-error-text").css("display","block");
        return false;
    }else{
        $("#pw-error-text").css("display","none");
        return true;
    }
}
function userIdCheck(){
    var result=false;

    if($("#user-id").val() != ''){
        $.ajax({
            type : "POST",
            url : "{% url 'idCheck' %}",
            async: false,
            data : {
                'csrfmiddlewaretoken': '{{ csrf_token }}',
                'id_check' : $("#user-id").val(),
            }, 
            success : function(response)
            {
            
            if(response['msg'])
                $("#id_error_text").text("아이디 사용 가능합니다.").css("color","#0081ff");
            else 
                $("#id_error_text").text("아이디 사용 불가능합니다.").css("color","red");

                result = response['msg'];    
            },
        });
        
        return result;
    }
}
//유효성검사
function isValid(){
    
    if(!userIdCheck()){ 
        alert("중복된 아이디 입니다."); 
        return false; 
    } 
    
    if(!pwCompare()){ 
        alert("비밀번호가 일치하지 않습니다."); 
        return false;
    }
    
    return true;
}