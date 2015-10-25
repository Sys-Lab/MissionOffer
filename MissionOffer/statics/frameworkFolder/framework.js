    function all_demo(){
      document.getElementById("all_a").style.color="#64C864";
      document.getElementById("ing_a").style.color="#979797";
      document.getElementById("done_a").style.color="#979797";
      document.getElementById("get_a").style.color="#979797";
    }
    function ing_demo(){
      document.getElementById("ing_a").style.color="#64C864";
      document.getElementById("all_a").style.color="#979797";
      document.getElementById("done_a").style.color="#979797";
      document.getElementById("get_a").style.color="#979797";
      document.getElementById("task_condition").name="进行中";
    }
    function done_demo(){
      document.getElementById("done_a").style.color="#64C864";
      document.getElementById("all_a").style.color="#979797";
      document.getElementById("ing_a").style.color="#979797";
      document.getElementById("get_a").style.color="#979797";
      document.getElementById("task_condition").name="已完成";
    }
    function get_demo(){
      document.getElementById("done_a").style.color="#979797";
      document.getElementById("all_a").style.color="#979797";
      document.getElementById("ing_a").style.color="#979797";
      document.getElementById("get_a").style.color="#64C864";
      document.getElementById("task_condition").name="待接收";
    }
    function lost_p(){
      document.getElementById("boss1022").src="/statics/frameworkFolder/lost1_pressed.png";
      document.getElementById("boss1033").src="/statics/frameworkFolder/dining.png";
      document.getElementById("boss1044").src="/statics/frameworkFolder/super.png";
      document.getElementById("boss1055").src="/statics/frameworkFolder/print.png";
      document.getElementById("boss1066").src="/statics/frameworkFolder/out.png";
      document.getElementById("boss102").style.left="30%";
      document.getElementById("boss103").style.left="25%";
      document.getElementById("boss104").style.left="23%";
      document.getElementById("boss105").style.left="21.5%";
      document.getElementById("boss106").style.left="22%";
      document.getElementById("classify").name="寻找失物";
    }
    function ding_p(){
      document.getElementById("boss1022").src="/statics/frameworkFolder/lost_pressed.png";
      document.getElementById("boss1033").src="/statics/frameworkFolder/dining_pressed.png";
      document.getElementById("boss1044").src="/statics/frameworkFolder/super.png";
      document.getElementById("boss1055").src="/statics/frameworkFolder/print.png";
      document.getElementById("boss1066").src="/statics/frameworkFolder/out.png";
      document.getElementById("boss102").style.left="21%";
      document.getElementById("boss103").style.left="34%";
      document.getElementById("boss104").style.left="23%";
      document.getElementById("boss105").style.left="21.5%";
      document.getElementById("boss106").style.left="22%";
      document.getElementById("classify").name="食堂带饭";
    }
    function super_p(){
      document.getElementById("boss1022").src="/statics/frameworkFolder/lost_pressed.png";
      document.getElementById("boss1033").src="/statics/frameworkFolder/dining.png";
      document.getElementById("boss1044").src="/statics/frameworkFolder/super_pressed.png";
      document.getElementById("boss1055").src="/statics/frameworkFolder/print.png";
      document.getElementById("boss1066").src="/statics/frameworkFolder/out.png";
      document.getElementById("boss102").style.left="21%";
      document.getElementById("boss103").style.left="25%";
      document.getElementById("boss104").style.left="32%";
      document.getElementById("boss105").style.left="21.5%";
      document.getElementById("boss106").style.left="22%";
      document.getElementById("classify").name="超市购物";
    }
    function print_p(){
      document.getElementById("boss1022").src="/statics/frameworkFolder/lost_pressed.png";
      document.getElementById("boss1033").src="/statics/frameworkFolder/dining.png";
      document.getElementById("boss1044").src="/statics/frameworkFolder/super.png";
      document.getElementById("boss1055").src="/statics/frameworkFolder/print_pressed.png";
      document.getElementById("boss1066").src="/statics/frameworkFolder/out.png";
      document.getElementById("boss102").style.left="21%";
      document.getElementById("boss103").style.left="25%";
      document.getElementById("boss104").style.left="23%";
      document.getElementById("boss105").style.left="30.5%";
      document.getElementById("boss106").style.left="22%";
      document.getElementById("classify").name="文印中心";
    }
    function out_p(){
      document.getElementById("boss1022").src="/statics/frameworkFolder/lost_pressed.png";
      document.getElementById("boss1033").src="/statics/frameworkFolder/dining.png";
      document.getElementById("boss1044").src="/statics/frameworkFolder/super.png";
      document.getElementById("boss1055").src="/statics/frameworkFolder/print.png";
      document.getElementById("boss1066").src="/statics/frameworkFolder/out_pressed.png";
      document.getElementById("boss102").style.left="21%";
      document.getElementById("boss103").style.left="25%";
      document.getElementById("boss104").style.left="23%";
      document.getElementById("boss105").style.left="21.5%";
      document.getElementById("boss106").style.left="31%";
      document.getElementById("classify").name="校外任务";
    }
    function dp(){
      document.getElementById("display").style.display="block";
      document.getElementById("publish").style.display="block";
    }
    function pd(){
      document.getElementById("display").style.display="none";
      document.getElementById("publish").style.display="none";
    }
