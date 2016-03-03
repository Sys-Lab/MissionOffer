$(document).ready(function(){

    $("#remmber-password").click(function(){
    	var sta = $(".sta-checked-one").html();
    	console.log(sta);
  		if(sta==0){
  			$("#remmber-password").attr("src","../login/img/checked_out.png");
  			$(".sta-checked-one").html("1");
  		}else if(sta==1){
  			$("#remmber-password").attr("src","../login/img/checked.png");
  			$(".sta-checked-one").html("0");
  		}
    });
    $("#auto-login").click(function(){
    	var sta = $(".sta-checked-two").html();
    	console.log(sta);
  		if(sta==0){
  			$("#auto-login").attr("src","../login/img/checked_out.png");
  			$(".sta-checked-two").html("1");
  		}else if(sta==1){
  			$("#auto-login").attr("src","../login/img/checked.png");
  			$(".sta-checked-two").html("0");
  		}
    });

	$("#btn-login").click(function(){
		var is_post = false;
		var re = /[^\w\u4e00-\u9fa5]/g;
		var num = /^[0-9]*$/;
		var a = $("#username").val();
		//console.log(a);
		var length_a = a.length;
		//console.log(length_a);
		if(a==""){
			$("#name_error-show").html("账号不能为空！");
			$(".error-username").css("display","block");
		}else if(!num.test(a)||length_a!=13){
			$(".error-username").css("display","block");
			$("#name_error-show").html("账号必须为13位纯数字");
		}else{
			$(".error-username").css("display","none");
			is_post = true;
		}
		if(is_post){
			$.post('', {
            'username' : $("#username").val(),
            'password' : $("#password").val(),
            'auto_one' : $(".sta-checked-one").html(),
            'auto_two' : $(".sta-checked-two").html()
            }, function(result) {
              //console.log(result);
              if (result['success']) {
                location = '/index/';
              } else {
              	$("#password_error-show").html(result['reason']);
                $(".error-password").css("display","none");
              }
            });
		}
	});
});

