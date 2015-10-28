var isValidate=false;
function getlength(str){
        return str.length;
      }
      function demo1(){
        document.getElementById("woman").checked=false;
        document.getElementById("keepsecret").checked=false;
      }
      function demo2(){
        document.getElementById("man").checked=false;
        document.getElementById("keepsecret").checked=false;
      }
      function demo3(){
        document.getElementById("man").checked=false;
        document.getElementById("woman").checked=false;
      }
      function input1(){
        document.getElementById("input1_explain").style.display="block";
      }
      function input1_judge(){
        var a=document.getElementById("uN").value;
        var isajax=false;
        if(a==""){
          document.getElementById("input1_p").innerHTML="";
          document.getElementById("input1_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input1_p").style.top="230px";
          document.getElementById("input1_explain").innerHTML="邮箱不能为空！";
          document.getElementById("input1_explain").style.color="red";
          document.getElementById("input1_explain").style.top="230px";
          document.getElementById("uN").focus();
          isValidate=false;
          isajax=false;
          return;
        }
        else{
          isajax=true;
          return;
        }
        if(isajax){
          $.get('', {
             '' : document.getElementById('uN').value
              }, function(document.getElementById("uN")) {
                if (document.getElementById("uN")) {
                   document.getElementById("input1_p").innerHTML="";
                   document.getElementById("input1_p").style.background="url(/statics/registerFolder/2.jpg)";
                   document.getElementById("input1_p").style.top="225px";
                   document.getElementById("input1_explain").innerHTML="";
                   return;
                   } else {
                   document.getElementById("input1_p").innerHTML="";
                   document.getElementById("input1_p").style.background="url(/statics/registerFolder/1.jpg)";
                   document.getElementById("input1_p").style.top="230px";
                   document.getElementById("input1_explain").innerHTML="该邮箱已注册！";
                   document.getElementById("input1_explain").style.color="red";
                   document.getElementById("input1_explain").style.top="230px";
                   document.getElementById("uN").focus();
                   isValidate=false;
                   return;
                   }
            });
        }  
      }
      function input2(){
        document.getElementById("input2_explain").style.display="block";
      }
      function input2_judge(){
        var a=document.getElementById("pW").value;
        var b=getlength(a);
        if(a==""){
          document.getElementById("input2_p").innerHTML="";
          document.getElementById("input2_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input2_p").style.top="320px";
          document.getElementById("input2_explain").innerHTML="密码不能为空!";
          document.getElementById("input2_explain").style.top="320px";
          document.getElementById("input2_explain").style.color="red";
          document.getElementById("pW").focus();
          isValidate=false;
        }
        else if(/ /g.test(a)){
          document.getElementById("input2_p").innerHTML="";
          document.getElementById("input2_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input2_p").style.top="320px";
          document.getElementById("input2_explain").innerHTML="密码不能含有空格!";
          document.getElementById("input2_explain").style.top="320px";
          document.getElementById("input2_explain").style.color="red";
          document.getElementById("pW").focus();
          isValidate=false;
        }
        else if(b<6||b>16){
          document.getElementById("input2_p").innerHTML="";
          document.getElementById("input2_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input2_p").style.top="320px";
          document.getElementById("input2_explain").innerHTML="密码长度为6-16！";
          document.getElementById("input2_explain").style.top="320px";
          document.getElementById("input2_explain").style.color="red";
          document.getElementById("pW").focus();
          isValidate=false;
        }
        else{
          document.getElementById("input2_p").innerHTML="";
          document.getElementById("input2_p").style.background="url(/statics/registerFolder/2.jpg)";
          document.getElementById("input2_p").style.top="320px";
          document.getElementById("input2_explain").innerHTML="";
        };
      }
      function input3(){
        document.getElementById("input3_explain").style.display="block";
      }
      function input3_judge(){
        var a=document.getElementById("rP").value;
        var b=document.getElementById("pW").value;
        if(b!=a){
          document.getElementById("input3_p").innerHTML="";
          document.getElementById("input3_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input3_p").style.top="420px";
          document.getElementById("input3_explain").innerHTML="密码不正确!";
          document.getElementById("input3_explain").style.color="red";
          document.getElementById("input3_explain").style.top="420px";
          isValidate=false;
        }
        else{
          document.getElementById("input3_p").innerHTML="";
          document.getElementById("input3_p").style.background="url(/statics/registerFolder/2.jpg)";
          document.getElementById("input3_p").style.top="420px";
          document.getElementById("input3_explain").innerHTML="";
        }
      }
      function input4(){
        document.getElementById("input4_explain").style.display="block";
      }
      function input4_judge(){
        var a=document.getElementById("nN").value;
        var b=getlength(a);
        var re=/[^\w\u4e00-\u9fa5]/g;
        var isajax=false;
        if(a==""){
          document.getElementById("input4_p").innerHTML="";
          document.getElementById("input4_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input4_p").style.top="510px";
          document.getElementById("input4_explain").innerHTML="昵称不能为空!";
          document.getElementById("input4_explain").style.top="515px";
          document.getElementById("input4_explain").style.color="red";
          document.getElementById("nN").focus();
          isajax=false;
          isValidate=false;
        }
        else if(/ /g.test(a)||re.test(a)){
          document.getElementById("input4_p").innerHTML="";
          document.getElementById("input4_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input4_p").style.top="510px";
          document.getElementById("input4_explain").innerHTML="昵称不能含有空格和非法字符!";
          document.getElementById("input4_explain").style.top="515px";
          document.getElementById("input4_explain").style.color="red";
          document.getElementById("nN").focus();
          isajax=false;
          isValidate=false;
        }
        else if(b<6||b>16){
          document.getElementById("input4_p").innerHTML="";
          document.getElementById("input4_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input4_p").style.top="510px";
          document.getElementById("input4_explain").innerHTML="昵称长度为6-16！";
          document.getElementById("input4_explain").style.top="515px";
          document.getElementById("input4_explain").style.color="red";
          document.getElementById("nN").focus();
          isajax=false;
          isValidate=false;
        }
        else{
          isajax=true;
        }
        if(isajax){
          $.get('', {
             '' : document.getElementById('nN').value
              }, function(document.getElementById("nN")) {
                if (document.getElementById("nN")) {
                   document.getElementById("input4_p").innerHTML="";
                   document.getElementById("input4_p").style.background="url(/statics/registerFolder/2.jpg)";
                   document.getElementById("input4_p").style.top="510px";
                   document.getElementById("input4_explain").innerHTML="";
                   return;
                   } else {
                   document.getElementById("input4_p").innerHTML="";
                   document.getElementById("input4_p").style.background="url(1.jpg)";
                   document.getElementById("input4_p").style.top="230px";
                   document.getElementById("input4_explain").innerHTML="该邮箱已注册！";
                   document.getElementById("input4_explain").style.color="red";
                   document.getElementById("input4_explain").style.top="515px";
                   document.getElementById("nN").focus();
                   isValidate=false;
                   return;
                   }
            });
        }
      }
      function input5(){
        document.getElementById("input5_explain").style.display="block";
      }
      function input5_judge(){
        var a=document.getElementById("sN").value;
        var b=getlength(a);
        if(a==""){
          document.getElementById("input5_p").innerHTML="";
          document.getElementById("input5_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input5_p").style.top="675px";
          document.getElementById("input5_explain").innerHTML="学号不能为空！";
          document.getElementById("input5_explain").style.color="red";
          document.getElementById("input5_explain").style.top="680px";
          document.getElementById("sN").focus();
          isValidate=false;
        }
        else if(b!=13){
          document.getElementById("input5_p").innerHTML="";
          document.getElementById("input5_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input5_p").style.top="675px";
          document.getElementById("input5_explain").innerHTML="学号格式不正确!";
          document.getElementById("input5_explain").style.top="680px";
          document.getElementById("input5_explain").style.color="red";
          document.getElementById("sN").focus();
          isValidate=false;
        }
        else{
          document.getElementById("input5_p").innerHTML="";
          document.getElementById("input5_p").style.background="url(/statics/registerFolder/2.jpg)";
          document.getElementById("input5_p").style.top="675px";
          document.getElementById("input5_explain").innerHTML="";
        };
      }
      function input6(){
        document.getElementById("input6_explain").style.display="block";
      }
      function input6_judge(){
        var a=document.getElementById("pN").value;
        var b=getlength(a);
        if(a==""){
          document.getElementById("input6_p").innerHTML="";
          document.getElementById("input6_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input6_p").style.top="770px";
          document.getElementById("input6_explain").innerHTML="手机号不能为空！";
          document.getElementById("input6_explain").style.color="red";
          document.getElementById("input6_explain").style.top="775px";
          document.getElementById("pN").focus();
          isValidate=false;
        }
        else if(b!=11){
          document.getElementById("input6_p").innerHTML="";
          document.getElementById("input6_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input6_p").style.top="770px";
          document.getElementById("input6_explain").innerHTML="手机号格式不正确！";
          document.getElementById("input6_explain").style.top="775px";
          document.getElementById("input6_explain").style.color="red";
          document.getElementById("pN").focus();
          isValidate=false;
        }
        else{
          document.getElementById("input6_p").innerHTML="";
          document.getElementById("input6_p").style.background="url(/statics/registerFolder/2.jpg)";
          document.getElementById("input6_p").style.top="770px";
          document.getElementById("input6_explain").innerHTML="";
        };
      }
      function input_textarea(){
        var a = document.getElementById("it").value;
        var b = getlength(a);
        if(b<20||b>40){
          document.getElementById("biginput_p").innerHTML="";
          document.getElementById("biginput_p").style.background="url(/statics/registerFolder/1.jpg)"
          document.getElementById("biginput_explain").style.display="block";
          isValidate="false";
        }
        else{
          document.getElementById("biginput_p").innerHTML="";
          document.getElementById("biginput_p").style.background="url(/statics/registerFolder/2.jpg)"
          document.getElementById("biginput_explain").style.display="none";
        }
      }
      function submit(){
        return isValidate;
      }
