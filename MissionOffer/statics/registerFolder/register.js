function getlength(str){
        return str.length;
      }
      function demo(){
        document.getElementById("read").style.background="url(/statics/registerFolder/read_select.png)";
      }
      function demo1(){
        document.getElementById("man").style.background="url(/statics/registerFolder/checkbox_select.png)";
        document.getElementById("woman").style.background="url(/statics/registerFolder/checkbox.png)";
        document.getElementById("keepsecret").style.background="url(/statics/registerFolder/checkbox.png)";
      }
      function demo2(){
        document.getElementById("woman").style.background="url(/statics/registerFolder/checkbox_select.png)";
        document.getElementById("man").style.background="url(/statics/registerFolder/checkbox.png)";
        document.getElementById("keepsecret").style.background="url(/statics/registerFolder/checkbox.png)";
      }
      function demo3(){
        document.getElementById("keepsecret").style.background="url(/statics/registerFolder/checkbox_select.png)";
        document.getElementById("man").style.background="url(/statics/registerFolder/checkbox.png)";
        document.getElementById("woman").style.background="url(/statics/registerFolder/checkbox.png)";
      }
      function input1(){
        document.getElementById("input1_explain").style.display="block";
      }
      function input1_judge(){
        var a=document.getElementById("uN").value;
        if(a==""){
          document.getElementById("input1_p").innerHTML="";
          document.getElementById("input1_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input1_p").style.top="230px";
          document.getElementById("input1_explain").innerHTML="邮箱不能为空！";
          document.getElementById("input1_explain").style.color="red";
          document.getElementById("input1_explain").style.top="230px";
        }
        else{
          document.getElementById("input1_p").innerHTML="";
          document.getElementById("input1_p").style.background="url(/statics/registerFolder/2.jpg)";
          document.getElementById("input1_p").style.top="225px";
          document.getElementById("input1_explain").innerHTML="";
        };
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
        }
        else if(/ /g.test(a)){
          document.getElementById("input2_p").innerHTML="";
          document.getElementById("input2_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input2_p").style.top="320px";
          document.getElementById("input2_explain").innerHTML="密码不能含有空格!";
          document.getElementById("input2_explain").style.top="320px";
          document.getElementById("input2_explain").style.color="red";
        }
        else if(b<6||b>16){
          document.getElementById("input2_p").innerHTML="";
          document.getElementById("input2_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input2_p").style.top="320px";
          document.getElementById("input2_explain").innerHTML="密码长度为6-16！";
          document.getElementById("input2_explain").style.top="320px";
          document.getElementById("input2_explain").style.color="red";
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
        if(a==""){
          document.getElementById("input4_p").innerHTML="";
          document.getElementById("input4_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input4_p").style.top="510px";
          document.getElementById("input4_explain").innerHTML="昵称不能为空!";
          document.getElementById("input4_explain").style.top="515px";
          document.getElementById("input4_explain").style.color="red";
        }
        else if(/ /g.test(a)||re.test(a)){
          document.getElementById("input4_p").innerHTML="";
          document.getElementById("input4_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input4_p").style.top="510px";
          document.getElementById("input4_explain").innerHTML="昵称不能含有空格和非法字符!";
          document.getElementById("input4_explain").style.top="515px";
          document.getElementById("input4_explain").style.color="red";
        }
        else if(b<6||b>16){
          document.getElementById("input4_p").innerHTML="";
          document.getElementById("input4_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input4_p").style.top="510px";
          document.getElementById("input4_explain").innerHTML="昵称长度为6-16！";
          document.getElementById("input4_explain").style.top="515px";
          document.getElementById("input4_explain").style.color="red";
        }
        else{
          document.getElementById("input4_p").innerHTML="";
          document.getElementById("input4_p").style.background="url(/statics/registerFolder/2.jpg)";
          document.getElementById("input4_p").style.top="510px";
          document.getElementById("input4_explain").innerHTML="";
        };
      }
      function input5(){
        document.getElementById("input5_explain").style.display="block";
      }
      function input5_judge(){
        var a=document.getElementById("sN").value;
        if(a==""){
          document.getElementById("input5_p").innerHTML="";
          document.getElementById("input5_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input5_p").style.top="675px";
          document.getElementById("input5_explain").innerHTML="学号不能为空！";
          document.getElementById("input5_explain").style.color="red";
          document.getElementById("input5_explain").style.top="680px";
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
        if(a==""){
          document.getElementById("input6_p").innerHTML="";
          document.getElementById("input6_p").style.background="url(/statics/registerFolder/1.jpg)";
          document.getElementById("input6_p").style.top="770px";
          document.getElementById("input6_explain").innerHTML="手机号不能为空！";
          document.getElementById("input6_explain").style.color="red";
          document.getElementById("input6_explain").style.top="775px";
        }
        else{
          document.getElementById("input6_p").innerHTML="";
          document.getElementById("input6_p").style.background="url(/statics/registerFolder/2.jpg)";
          document.getElementById("input6_p").style.top="770px";
          document.getElementById("input6_explain").innerHTML="";
        };
      }