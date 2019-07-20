<?php
function ArkaFunc($str){
    $strlength=strlen($str);
    $split=ceil($strlength/3);
    $num=3;
    $k=0;
    $s=3;
    $r=4;
    for($l=0;$l<=$split-2;$l++){
        $s=$s+$r;
        for($i=0;$i<=$split-1;$i++){
            $stage[0][$i]=substr($str,$k,$num);
            $k=$k+$num; 
            $num++;   
            
        }
        $num=$num-1;
        $string=array_filter($stage[0]);
        echo join(",",$string);
        echo "\n";
        $i=0;
        $k=0;
        $num=$s;
        $r=$r-1;
    }
}
//jalankan
$str=readline("Masukan String :");
ArkaFunc($str);
//ini  program berbasis CLI, Jalankan di secara online
//masukan string sesuai dengan soal
//https://repl.it/languages/php_cli