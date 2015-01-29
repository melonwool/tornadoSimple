# tornadoSimple
## 说明
使用tornado,简单写了个留言板，后续有时间会添加一些其他内容
## 需要的包
 - MySQL-python==1.2.5
 - pymongo==2.7.2
 - PyYAML==3.11
 - tornado==4.0.2
 - torndb==0.3

## 需要的服务
 - tornado
 - redis
 - mongodb

## 启动方式
 - 建议部署 virtualenv 
 - python httpd.py --logging=debug --port=8000 --debug=1
