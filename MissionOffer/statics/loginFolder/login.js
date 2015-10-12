function getlength(str){
	return str.length;
}
function demo(){
	var a=document.getElementById("usrName").value;
	var len=getlength(a);
	if(a==""){
	  alert("用户名不能为空");
      return false;
	}
	else if(len>30) {
	  alert("用户名不能超过30个字符");
	  return false;
	}
}
function demo1(){
	var a=document.getElementById("usrName").value;
	var len=getlength(a);
	if(a==""){
      return false;
	}
	else if(len>30) {
	  return false;
	}
}
