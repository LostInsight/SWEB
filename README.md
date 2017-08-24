# SWEB
个人使用的ShadowsocksR的WEB面板。集成修改配置，开启，关闭为一体的管理功能的网页面板。

## 安装

```shell
wget -N --no-check-certificate  https://raw.githubusercontent.com/ishkong/SWEB/master/install.sh && bash install.sh
```

### 申明
因为原作者已经删除了代码，这个代码为原作者第一版代码的简易修改，仅修改了安装文件，可以直接安装使用。支持的系统应该为 Centos6 Debian8

### 已知的问题并且不打算修复
修改 55R 配置，面页可能会返回502，但实际修改成功
修改 面板信息，面页可能会无回复，但实际修改成功
遇到以上两种情况，手动返回首页即可 http://your IP/cgi-bin/index.py

同时预告一下，雨落大大明年可能会重写一个类似的项目。仅为可能。
