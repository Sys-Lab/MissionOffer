function left_input1(){
	document.getElementById("my_information_input1").style.borderRight="0px";
	document.getElementById("my_task_input2").style.borderRight="1px solid rgb(100,200,100)";
	document.getElementById("main_task").style.display="none";
	document.getElementById("main_information").style.display="block";
}
function left_input2(){
	document.getElementById("my_information_input1").style.borderRight="1px solid rgb(100,200,100)";
	document.getElementById("my_task_input2").style.borderRight="0px";
	document.getElementById("main_task").style.display="block";
	document.getElementById("main_information").style.display="none";
}
function information1(){
	document.getElementById("task_published_details").style.display="block";
	document.getElementById("task_gotten_details").style.display="none";
	document.getElementById("task_done_details").style.display="none";
	document.getElementById("task_watch_details").style.display="none";
	document.getElementById("task_gotten").style.top="310px";
	document.getElementById("task_done").style.top="369px";
	document.getElementById("task_watch").style.top="418px";
}
function information2(){
	document.getElementById("task_published_details").style.display="none";
	document.getElementById("task_gotten_details").style.display="block";
	document.getElementById("task_done_details").style.display="none";
	document.getElementById("task_watch_details").style.display="none";
	document.getElementById("task_gotten").style.top="100px";
	document.getElementById("task_done").style.top="380px";
	document.getElementById("task_watch").style.top="439px";
}
function information3(){
	document.getElementById("task_published_details").style.display="none";
	document.getElementById("task_gotten_details").style.display="none";
	document.getElementById("task_done_details").style.display="block";
	document.getElementById("task_watch_details").style.display="none";
	document.getElementById("task_gotten").style.top="100px";
	document.getElementById("task_done").style.top="159px";
	document.getElementById("task_watch").style.top="430px";
}
function information4(){
	document.getElementById("task_published_details").style.display="none";
	document.getElementById("task_gotten_details").style.display="none";
	document.getElementById("task_done_details").style.display="none";
	document.getElementById("task_watch_details").style.display="block";
	document.getElementById("task_gotten").style.top="100px";
	document.getElementById("task_done").style.top="159px";
	document.getElementById("task_watch").style.top="218px";
}