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
        if (isset($url)){
          $payload="-u ".$url;
          $u="python ./Core/dirsearch.py ";
          $k=exec($u.$payload,$out,$code);
          if ($code==0){
            if (count($out)<10){
              foreach ($out as $value){
                echo iconv('gbk','utf-8',$value);
                echo "<br>";}
            }else{
              echo "结果较长，已转换为页面显示<br>";
              echo '<a href="Output/result.html" ">目录扫描结果</a><br>';

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