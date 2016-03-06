$(document).ready(function(){
	$("#publish").click(function(){
		var a = $(".footer").offset().top;
		var b = a+50;
		$(".all-coin").css("height",b);
		$(".all-coin").css("display","block");
		$(".publish-task").css("display","block");
	});

	$("#close").click(function(){
		$(".publish-task").css("display","none");
		$(".all-coin").css("display","none");
	});
	$("#dropdown").click(function(){
		$(".task-choice-box").css("display","block");
	});
	$("#lost-find-choice").mouseover(function(){
		$("#lost-find-choice").css("background-color","red");
	});
	$("#lost-find-choice").mouseout(function(){
		$("#lost-find-choice").css("background-color","white");
	});
	$("#lost-find-choice").click(function(){
		$("#task-type").html("寻找失物");
		$(".task-choice-box").css("display","none");
	});
	$("#dining-choice").mouseover(function(){
		$("#dining-choice").css("background-color","red");
	});
	$("#dining-choice").mouseout(function(){
		$("#dining-choice").css("background-color","white");
	});
	$("#dining-choice").click(function(){
		$("#task-type").html("食堂带饭");
		$(".task-choice-box").css("display","none");
	});
	$("#super-choice").mouseover(function(){
		$("#super-choice").css("background-color","red");
	});
	$("#super-choice").mouseout(function(){
		$("#super-choice").css("background-color","white");
	});
	$("#super-choice").click(function(){
		$("#task-type").html("超市购物");
		$(".task-choice-box").css("display","none");
	});
	$("#print-choice").mouseover(function(){
		$("#print-choice").css("background-color","red");
	});
	$("#print-choice").mouseout(function(){
		$("#print-choice").css("background-color","white");
	});
	$("#print-choice").click(function(){
		$("#task-type").html("文印中心");
		$(".task-choice-box").css("display","none");
	});
	$("#out-choice").mouseover(function(){
		$("#out-choice").css("background-color","red");
	});
	$("#out-choice").mouseout(function(){
		$("#out-choice").css("background-color","white");
	});
	$("#out-choice").click(function(){
		$("#task-type").html("校外任务");
		$(".task-choice-box").css("display","none");
	});
	$("#other-choice").mouseover(function(){
		$("#other-choice").css("background-color","red");
	});
	$("#other-choice").mouseout(function(){
		$("#other-choice").css("background-color","white");
	});
	$("#other-choice").click(function(){
		$("#task-type").html("其他");
		$(".task-choice-box").css("display","none");
	});

	$("#publish-btn").click(function(){
		var is_publish = false;
		var title = $("#title").val();
		var tasktype = $("#task-type").html();
		var description = $("#description").val();
		var pay = $("#pay").val();
		var cash = $("#cash").val();
		var date = $("#date").val();
		if(title==""){
			alert("标题不能为空");
			is_publish = false;
		}else if(title.length>14){
			alert("标题最多7个字");
			is_publish = false;
		}else if(description.length>200){
			alert("描述最多100个字");
			is_publish = false;
		}else if(pay==""||cash==""){
			alert("请输入悬赏和押金");
			is_publish = false;
		}else if(date==""){
			alert("请输入有效日期");
			is_publish = false;
		}else{
			is_publish = true;
		}
		if(is_publish){
			$.post('hello.php',{
				'title' : title,
				'task-type' : tasktype,
				'description' : description,
				'pay' : pay,
				'cash' : cash,
				'date' : date
			});
		}

	});
	$("#all-change").click(function(){
		$("#all-change").attr("src","../main/img/all_pressed.png");
		$("#lost-find-change").attr("src","../main/img/lost-find.png");
		$("#dining-change").attr("src","../main/img/dining.png");
		$("#super-change").attr("src","../main/img/super.png");
		$("#print-change").attr("src","../main/img/print.png");
		$("#out-change").attr("src","../main/img/out.png");
		$("#other-change").attr("src","../main/img/other.png");
		$("#task-type-condition").html("0");
		$.post('hello.php',{
			"task-type-condition" : $("#task-type-condition").html(),
			"task-condition" : $("#task-condition").html()
		});
	});
	$("#lost-find-change").click(function(){
		$("#all-change").attr("src","../main/img/all.png");
		$("#lost-find-change").attr("src","../main/img/lost-find_pressed.png");
		$("#dining-change").attr("src","../main/img/dining.png");
		$("#super-change").attr("src","../main/img/super.png");
		$("#print-change").attr("src","../main/img/print.png");
		$("#out-change").attr("src","../main/img/out.png");
		$("#other-change").attr("src","../main/img/other.png");
		$("#task-type-condition").html("1");
		$.post('hello.php',{
			"task-type-condition" : $("#task-type-condition").html(),
			"task-condition" : $("#task-condition").html()
		});
	});
	$("#dining-change").click(function(){
		$("#all-change").attr("src","../main/img/all.png");
		$("#lost-find-change").attr("src","../main/img/lost-find.png");
		$("#dining-change").attr("src","../main/img/dining_pressed.png");
		$("#super-change").attr("src","../main/img/super.png");
		$("#print-change").attr("src","../main/img/print.png");
		$("#out-change").attr("src","../main/img/out.png");
		$("#other-change").attr("src","../main/img/other.png");
		$("#task-type-condition").html("2");
		$.post('hello.php',{
			"task-type-condition" : $("#task-type-condition").html(),
			"task-condition" : $("#task-condition").html()
		});
	});
	$("#super-change").click(function(){
		$("#all-change").attr("src","../main/img/all.png");
		$("#lost-find-change").attr("src","../main/img/lost-find.png");
		$("#dining-change").attr("src","../main/img/dining.png");
		$("#super-change").attr("src","../main/img/super_pressed.png");
		$("#print-change").attr("src","../main/img/print.png");
		$("#out-change").attr("src","../main/img/out.png");
		$("#other-change").attr("src","../main/img/other.png");
		$("#task-type-condition").html("3");
		$.post('hello.php',{
			"task-type-condition" : $("#task-type-condition").html(),
			"task-condition" : $("#task-condition").html()
		});
	});
	$("#print-change").click(function(){
		$("#all-change").attr("src","../main/img/all.png");
		$("#lost-find-change").attr("src","../main/img/lost-find.png");
		$("#dining-change").attr("src","../main/img/dining.png");
		$("#super-change").attr("src","../main/img/super.png");
		$("#print-change").attr("src","../main/img/print_pressed.png");
		$("#out-change").attr("src","../main/img/out.png");
		$("#other-change").attr("src","../main/img/other.png");
		$("#task-type-condition").html("4");
		$.post('hello.php',{
			"task-type-condition" : $("#task-type-condition").html(),
			"task-condition" : $("#task-condition").html()
		});
	});
	$("#out-change").click(function(){
		$("#all-change").attr("src","../main/img/all.png");
		$("#lost-find-change").attr("src","../main/img/lost-find.png");
		$("#dining-change").attr("src","../main/img/dining.png");
		$("#super-change").attr("src","../main/img/super.png");
		$("#print-change").attr("src","../main/img/print.png");
		$("#out-change").attr("src","../main/img/out_pressed.png");
		$("#other-change").attr("src","../main/img/other.png");
		$("#task-type-condition").html("5");
		$.post('hello.php',{
			"task-type-condition" : $("#task-type-condition").html(),
			"task-condition" : $("#task-condition").html()
		});
	});
	$("#other-change").click(function(){
		$("#all-change").attr("src","../main/img/all.png");
		$("#lost-find-change").attr("src","../main/img/lost-find.png");
		$("#dining-change").attr("src","../main/img/dining.png");
		$("#super-change").attr("src","../main/img/super.png");
		$("#print-change").attr("src","../main/img/print.png");
		$("#out-change").attr("src","../main/img/out.png");
		$("#other-change").attr("src","../main/img/other_pressed.png");
		$("#task-type-condition").html("6");
		$.post('hello.php',{
			"task-type-condition" : $("#task-type-condition").html(),
			"task-condition" : $("#task-condition").html()
		});
	});

	$("#condition-all").click(function(){
		$("#condition-all").css("color","#66CC66");
		$("#condition-take").css("color","black");
		$("#condition-ing").css("color","black");
		$("#condition-finished").css("color","black");
		$("#task-condition").html("0");
		$.post('hello.php',{
			"task-type-condition" : $("#task-type-condition").html(),
			"task-condition" : $("#task-condition").html()
		});
	});
	$("#condition-take").click(function(){
		$("#condition-all").css("color","black");
		$("#condition-take").css("color","#66CC66");
		$("#condition-ing").css("color","black");
		$("#condition-finished").css("color","black");
		$("#task-condition").html("1");
		$.post('hello.php',{
			"task-type-condition" : $("#task-type-condition").html(),
			"task-condition" : $("#task-condition").html()
		});
	});
	$("#condition-ing").click(function(){
		$("#condition-all").css("color","black");
		$("#condition-take").css("color","black");
		$("#condition-ing").css("color","#66CC66");
		$("#condition-finished").css("color","black");
		$("#task-condition").html("2");
		$.post('hello.php',{
			"task-type-condition" : $("#task-type-condition").html(),
			"task-condition" : $("#task-condition").html()
		});
	});
	$("#condition-finished").click(function(){
		$("#condition-all").css("color","black");
		$("#condition-take").css("color","black");
		$("#condition-ing").css("color","black");
		$("#condition-finished").css("color","#66CC66");
		$("#task-condition").html("3");
		$.post('hello.php',{
			"task-type-condition" : $("#task-type-condition").html(),
			"task-condition" : $("#task-condition").html()
		});
	});
});