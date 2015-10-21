 function getlength(str){
        return str.length;
      }
      function demo(){
        var re=/[^\w\u4e00-\u9fa5]/g;
        var a=document.getElementById("usrName").value;
        var len=getlength(a);
        if(a==""||len>30){
          document.getElementById("dengluf").style.display="block";
          document.getElementById("empty").style.display="block";
          document.getElementById("usrname_false").style.display="none";
          return false;
        }
        else if(re.test(a)){
          document.getElementById("dengluf").style.display="block";
          document.getElementById("false").style.display="block";
          document.getElementById("empty").style.display="none";
          return false;
        };
      }

 $(document).ready(function(){
   $("#sbm").click(function(){
     $.ajax({
      type:"POST",
      url:"/loginCheck/",
      data:{
        'UN':$("#usrName").val(),
        'PW':$("#passWord").val()
      }
      dataType:"json",
      success:function(data){
        if(data.success){}
        else{
          $("#password_false").css('display','block');
          $("#denglut").css('display','block');
        }
      },
      error:function(data){
        alert("错误"+jqXHR.status);
      }
     })；
   });
 });
