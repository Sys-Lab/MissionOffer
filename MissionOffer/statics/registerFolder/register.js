function getlength(str){
	return str.length;
}
function demo(){
	var a=document.getElementById("usrName").value;
	var len=getlength(a);
	if(a==""){
      alert("用户名不能为空！");
	}
	else if(len>30) {
	  alert("用户名不能超过30个字符");
	}
}