var divheader = document.getElementById("divheader");
        var divbg = document.getElementById("divbg");
        var diveditcontent = document.getElementById("diveditcontent");
        var selects = document.getElementsByTagName("select");
        var divcontent = document.getElementById("divcontent");
        function Show(Key) {

            divbg.style.display = "";
            divbg.style.width = document.body.offsetWidth;  //浏览器宽度(滚动条+clientwidth+边框）
            divbg.style.height = document.body.offsetHeight;

            diveditcontent.style.display = "";
            diveditcontent.style.top = "50px";   //弹出窗口位置
            diveditcontent.style.left = "100px";


            for (var i = 0; i < selects.length; i++) {
                selects[i].style.display = "none";      //遮住下拉框
            }

            divcontent.innerHTML = "<iframe frameborder=0 scrolling=no src='PriceEdit.aspx?Key=" + Key + "' width='100%' height='100%'></iframe>";
            //嵌入页

        }
        function Hide() {
            //隐藏窗口
            document.location = location.reload();
            divbg.style.display = "none";
            diveditcontent.style.display = "none";

            for (var i = 0; i < selects.length; i++) {
                selects[i].style.display = "";
            }


        }
        divheader.onmousedown = Down;
        //以下是拉窗口自由移动
        var th;
        var tw;
        function Down(e) {

            var event = window.event || e;
            th = event.clientY - parseInt(diveditcontent.style.top.replace(/px/, ""), 10);
            tw = event.clientX - parseInt(diveditcontent.style.left.replace(/px/, ""), 10);
            document.onmousemove = Move;
            document.onmouseup = Up;
            document.onmouseout = Up;
            function Move(e) {

                var event = window.event || e;
                var top = event.clientY - th;
                var left = event.clientX - tw;
                top = top < 0 ? 0 : top;
                top = top > document.body.offsetHeight - 220 ? document.body.offsetHeight - 220 : top;

                left = left < 0 ? 0 : left;
                left = left > document.body.offsetWidth - 630 ? document.body.offsetWidth - 630 : left;

                diveditcontent.style.top = top + "px";
                diveditcontent.style.left = left + "px";
            }

            function Up() {
                document.onmousemove = null;
            }
        }