## Flask_demo

#### 功能介绍：
    
    基于Flask的web后台，实时监控摄像头信息；

    包括：
    摄像机播放；
    信息存储查询；
    循环绘图显示，实时更新，文件导出；

#### 文件介绍：

    MySQLExplanation.docx：导出CSV时数据库的配置以及存储路径信息；
    
    camera_cfg.json：摄像头RTSP数据流；
    
    config.py：配置文件；
    
    start.py：运行此文件，程序启动；
    
    requirements.txt：需要安装的依赖库；
    
    database.sql：数据库中的用到的数据表；
    
    app/routes.py：路由文件；
    
    app/models.py：数据库模型文件；
    
    app/forms.py：前端表单文件；
