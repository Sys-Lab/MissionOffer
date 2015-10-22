 function getlength(str){
        return str.length;
      }
 document.getElementById("sbm").onclick=function(){
        var isValidate=false;
        var re=/[^\w\u4e00-\u9fa5]/g;
        var a=document.getElementById("usrName").value;
        var len=getlength(a);
        if(a==""||len>30){
          document.getElementById("dengluf").style.display="block";
          document.getElementById("empty").style.display="block";
          document.getElementById("usrname_false").style.display="none";
          return;
        }
        else if(re.test(a)){
          document.getElementById("dengluf").style.display="block";
          document.getElementById("false").style.display="block";
          document.getElementById("empty").style.display="none";
          return;
        }
        else{
          isValidate=true;
        }

        if(isValidate){
          $.post('', {
            'username' : document.getElementById('UN').value,
            'password' : document.getElementById('PW').value
            }, function(user) {
              console.log(user);
              if (user) {
                location = '';
              } else {
                document.getElementById("password_false").style.display="block";
              }
          });
        }
      }
