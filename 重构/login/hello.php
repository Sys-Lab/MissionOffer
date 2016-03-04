// <?php
//   $name = $_POST['name'];
//   $number = $_POST['student_number'];
//   $age = $_POST['age'];
//   $DOCUMENT_ROOT = $_SERVER['DOCUMENT_ROOT'];
//   $outputstring = $name."\t".$number."\t".$age;

//   @ $fp = fopen("$DOCUMENT_ROOT/../php/test_php.txt",'rb');

//   // // flock($fp,LOCK_UN);
//   if(!$fp){
//   	echo "error";
//   	exit;
//   }

//   // fwrite($fp,$outputstring,strlen($outputstring));
//   // // flock($fp,LOCK_UN);
//   // fclose($fp);
//   while(!feof($fp)){
//   	$order = fgets($fp,999);
//   	echo $order."<br>";
//   }
// ?>