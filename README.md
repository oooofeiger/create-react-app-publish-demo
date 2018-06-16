## create-react-app-publish-demo
记一次create-react-app的demo发布，github+pm2一键更新部署

## 环境配置
本地和远程服务器均需要nodejs、pm2、git，因服务器配置不同，有些步骤可能有差别。

## 操作步骤

- [将本地项目添加到github](#将本地项目添加到github)
- [创建node服务](创建node服务)
- [配置pm2](#配置pm2)
- [发布应用](#发布应用)
- [配置域名指向和nginx反向代理](#配置域名指向和nginx反向代理)
- [本地资源更新同步到线上](#本地资源更新同步到线上)



## 将本地项目添加到github
先在github新建一个仓库，ssh密钥配置好，免得后面需要重复输入帐号密码，远程服务器也要配置ssh密钥
然后在本地新建一个空文件夹并进入该文件夹，在该路径下打开cmd并输入：
* `git init`
然后将本地项目复制到该文件夹内，然后
* `git add .`
* `git commit -m ""`
* `git remote add origin 仓库地址`
* `git push -u origin/master` 因为创建仓库时新建了license文件，所以这一步可能会失败，我们需要先拉取github上的文件：`git fetch`，
然后合并分支 `git merge origin/master`，会进入vim模式，直接按shift+:然后输入wq!退出，最后再`git push -u origin/master`


##创建node服务
因为项目中需要请求外部api所以在项目根目录下创建一个node服务server.js作为入口，server.js配置如下：
```
var express = require('express');
var path = require('path');
var app = new express();

app.use(express.static(__dirname))
app.use('*',function(req,res){
  res.sendFile(path.resolve(__dirname,'build/index.html'))
})
app.listen(8090);
console.log('app is running at port 8090')

```


## 配置pm2
在项目根目录下创建ecosystem.json文件，详细的配置信息可以去[pm2官网](http://pm2.keymetrics.io/docs/usage/quick-start/)查看。
ecosystem.json文件配置如下:
```
{
  "apps": [
    {
      "name": "graphcompany", //项目名
      "script": "build/server.js",  //node服务的入口文件
      "env": {
        "COMMEN_VARIABLE": "true"
      },
      "env_production": {
        "NODE_ENV": "production"
      }
    }
  ],
  "deploy": {
    "production": {
      "user": "maanger",   //服务器的帐号
      "host": ["127.30.65"],  // ip
      "ref": "origin/master",  //github的项目分支
      "repo": "git@github.com:oooofeiger/create-react-app-publish-demo.git", // 仓库地址
      "path": "/home/manager/www/GraphCompany/production",  //拉取的代码将会存放的位置
      "ssh_options": "StrictHostKeyChecking=no",  //取消ssh验证
      "env": {
        "NODE_ENV": "production"
      }
    }
  }
}
```
因为代码存放的位置文件夹还不存在，我们还需要创建，在manager目录下创建www
```sh
sudo mkdir -p www/GraphCompany
```
现在我们可以将项目从github上传到远程服务器了，在本地项目根路径下的cmd中输入
```sh
pm2 deploy ecosystem.json production setup
```
如果出现了报错"mkdir:cannot create directory"则是权限问题，我们需要修改GrapCompany的权限，在远端服务器/www路径下输入命令
```sh
sudo chomd 777 GrapCompany
```
然后再执行一次发布命令即可。成功之后可以在远端服务器中/home/manager/www/GraphCompany/路径下查看拉取的资源

## 发布应用
现在我们可以发布应用了，本地命令行中输入
```sh
pm2 deploy ecosystem.json production
```
这一步可能会报错"pm2: command not found"，是因为pm2在服务器上是非交互的ssh连接方式，我们需要修改服务器端的.bashrc文件，在manager根目录下
输入：
```sh
sudo vi .bashrc
```
将case到esac之间的代码注释掉，然后shift+:输入wq!保存并返回，再重新再加载该文件：
```sh
source .bashrc
```
完成这一步之后就可以切回本地终端再发布一次，如果再有错误就检查下ecosystem.json文件配置是否正确。发布成功后可以在服务器中输入pm2 list查看发布
应用的状态。到此应用就算发布完成了，但是我们在线上任然不能看到我们的项目，这时就要配置我们的域名指向了。


## 配置域名指向和nginx反向代理
在阿里云控制台中找到云解析DNS栏目，选择其中的解析设置，添加一个域名指向，然后切到服务器nginx目录，一般是/etc/nginx，进入conf.d新增或者修改nginx配置，配置样例如下：
```
upstream graphcompany {
	server 127.0.0.1:8090;
}

server{
	listen 80;
	server_name graphcompany.feiger.com.cn;

	location / {
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
		proxy_set_header Host $http_host;
		proxy_set_header X-Nginx-Proxy true;
		proxy_pass http://graphcompany;
		proxy_redirect off;
	}

	location /api {
                proxy_pass http://localhost:5000/;
        }
}

```
此时应该就能访问设置的域名了，如果出现502那么有可能是服务器防火墙问题，需要将8090端口开放。到此部署就已完成了


## 本地资源更新同步到线上
如果本地资源更新了怎么同步到服务器呢？只需要两步即可完成：
1.首先更新资源到github：
```sh
git add .
git commit -m ""
git push
```
2.pm2指令一键更新部署
```sh
pm2 deploy ecosystem.json production
```
这样就可以同步更新到服务器了！
