---
layout: post
tags: ["作业","Hzx"]
title: "大作业完成步骤记录"
date: 2022-12-13T07:28:17+08:00
math: false
draft: false
---
# socket
### 使用容器技术Docker，将socket客户端和服务端分别运行在不同的容器中，实现socket客户端和服务端之间的信息传递。
1. 使用 ubuntu 镜像启动两个容器

![](https://huatu.98youxi.com/markdown/work/uploads/upload_6f8bcb4e8d27b55d361b917faa6169e5.png)

2. 分别启动进入容器
```bash
$ docker start <容器 ID>
$ docker attach <容器 ID>
```
3. 在容器中运行服务端和客户端代码
### 服务端代码
![](https://huatu.98youxi.com/markdown/work/uploads/upload_70c6f19368ffe291dca6d382bf5f8a9c.png)
### 客户端代码
![](https://huatu.98youxi.com/markdown/work/uploads/upload_7722dcfdd839b63c2f8778b04522cbc3.png)

4. 实现服务端客户端之间的信息传递

![](https://huatu.98youxi.com/markdown/work/uploads/upload_a9d290f97a308e33216c77e06e6531a6.png)

![](https://huatu.98youxi.com/markdown/work/uploads/upload_39120a1b3a565a96dba49d67db4f59f6.png)

# Hugo
### 	使用Hugo，生成静态网站，部署到Nginx服务器
1. 安装Hugo，创建个人网站
```bash
$ hugo new site myblog
```
![](https://huatu.98youxi.com/markdown/work/uploads/upload_c4320578d22fc5ee16247d85922f953c.png)

2. 到hugo主题商店拉取模板，放在themes目录
```bash
$ git clone https://github.com/xslingcn/vno-hugo.git themes/vno-hugo
```
3. 创建文章，使用Markdown语法编写网站内容
```bash
$ hugo new posts/hello.md
```
![](https://huatu.98youxi.com/markdown/work/uploads/upload_6b6b2143a29f0bbada17276d73da4685.png)

4. 预览网站
```bash
$ hugo server
```
![](https://huatu.98youxi.com/markdown/work/uploads/upload_aec2f6d9ba484a104ab1ef7758fa68b9.png)

5. 创建容器，将网站相关文件拷贝到容器里

![](https://huatu.98youxi.com/markdown/work/uploads/upload_1505703da10ecbee0351c2a464475277.png)

6.	将静态网站部署到Nginx服务器
```bash
$ hugo -D
使用hugo -t <模板名>建立public文件
```
```bash
$ sudo cp public/* /var/www/html -r
将public文件放至nginx的/var/www/html目录
```
![](https://huatu.98youxi.com/markdown/work/uploads/upload_74780fba05eafd9fd6182f5465b2dbaa.png)


7. 启动nginx服务，测试可以正常访问

![](https://huatu.98youxi.com/markdown/work/uploads/upload_1d600d01c017effef562e72aa400a4a9.png)

