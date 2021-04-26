<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<title>漏洞检测平台</title>
<link rel="stylesheet" href=".././layui/css/layui.css">
<link rel="stylesheet" href=".././static/index.css">
<link rel="icon" href=".././favicon.ico" type="image/x-icon" />
</head>
<script src=".././static/index.js"></script>
<script src=".././static/jquery.min.js"></script>
<body class="layui-layout-body">
<div class="layui-layout layui-layout-admin">
  <div class="layui-header">
    <div class="layui-logo"><font style="color: white">导航</font></div>
    <ul class="layui-nav layui-layout-right">
      <li class="layui-nav-item">
      </li>
    </ul>
  </div>
  
  <div class="layui-side layui-bg-black">
    <div class="layui-side-scroll">
      <!-- 左侧导航区域（可配合layui已有的垂直导航） -->
      <ul class="layui-nav layui-nav-tree"  lay-filter="test">
        <li class="layui-nav-item layui-nav-itemed">
          <a href="javascript:;">扫描</a>
          <dl class="layui-nav-child">
          	<dd>端口扫描</dd>
            <dd>目录扫描</dd>
          </dl>
        </li>
        <li class="layui-nav-item layui-nav-itemed">
          <a href="javascript:;">辅助工具</a>
            <dl class="layui-nav-child">
            <dd>嗅探识别</dd>
            </dl>
        </li>
      </ul>
    </div>
  </div>
  
  <div class="layui-body" id="pocTest" style="padding: 15px;">
   <font face="黑体" size="5px">
      <?php
      set_time_limit(0);
      @$url=$_POST["url"];
      @$way=$_POST["way"];
      $aa="python ./YnScan.py ";
      if ($way=="指纹识别+存活子域名检测"){
      	  #全部检测
          $payload=$aa."-u ".$url;
          $output = exec($payload,$out,$code);
          if ($code==0){
            if (count($out)>3){
              echo "程序执行完毕，结果返回如下：<br>";  //返回数据太多，打印不好看
              echo '<a href="Output/link.txt" ">存活子域名</a><br>';
              echo '<a href="Output/fingerprint.txt" ">指纹识别</a><br>';
            }else{
              echo "无结果<br>";
            }
            }else{
              echo "错误！请检查输入参数是否正确<br>";
            }
      }
      elseif($way=="web指纹识别"){
	      #单一检测
        $path="./YnScan.py -u ".$url." -m webanalyzer";
        $aa = "python ".$path;
        $output = exec($aa,$out,$code);
        if ($code==0){
          if (count($out)>3){
            foreach ($out as $value) {
              echo iconv('gbk','utf-8',$value);
              echo "<br>";}    
          }elseif(count($out)==1){
            foreach ($out as $value) {
              echo iconv('gbk','utf-8',$value);
              echo "<br>";} 
          }else{
            echo "无结果<br>";
          }
          }else{
            echo "错误！请检查输入参数是否正确<br>";
            foreach ($out as $value) {
              echo iconv('gbk','utf-8',$value);
              echo "<br>";} 
          }
      }else{
        $payload="-u ".$url." -m subdomain,checkurl";
        $kk=exec($aa.$payload,$out,$code);
        if ($code==0){
          if (count($out)>8){ 
            echo "程序执行完毕，结果返回如下：<br>";    //返回数据太多，打印不好看
            echo '<a href="Output/link.txt" ">存活子域名</a><br>';
          }else{
            echo "无结果<br>";
          }
          }else{
            echo "错误！请检查输入参数是否正确<br>";
          }
      }
      ?>
      <input type="button" name="Submit" class="layui-btn" style="font-size: 18px;padding-left:10px " value="返回主页" onclick="javascript:history.go(-1)" /> 
</font>

  </div>
  
</div>
<script src=".././layui/layui.all.js"></script>
</body>
</html>