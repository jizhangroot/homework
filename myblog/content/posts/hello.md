---
layout: post
tags: ["笔记", "Hzx"]
title: "Linux学习笔记"
date: 2022-12-13T07:28:17+08:00
math: false
draft: false
---
### 一、目录结构
Linux的目录结构，/etc存放着系统配置文件的目录，/home是除root外的其它用户的目录，/dev存放设备文件，dev存放设备文件，boot存启动文件，tmp是临时目录，usr存放库文件，文档，命令，用户数据等，var存放变化的文件，如日志文件等，
| 目录名 | 解析 |
|--|--|
|  bin| 存放普通用户可执行命令 |
|etc|系统的配置文件|
| root | 超级用户目录 |
|dev|系统的一些设备文件，驱动等|
| boot | 系统的启动文件 |
|tmp|临时文件存放目录|
| usr | 存放用户的应用程序和文件 |
|var|存放一些变化的文件，如程序日志等|
| home| 普通用户的目录|
|run|存放进程产生的临时文件|
|mnt| 临时的挂载文件系统|
|sbin| 存放系统管理员才能执行的命令|


### 二、文件命令

### ls
列出该目录下的子目录与文件，常用参数：
-a 以.开头的隐藏项目也列出
-l  列出目录的详细信息，可直接使用ll
```bash
$  ls -a
```
```bash
$ ll
```
![](https://huatu.98youxi.com/markdown/work/uploads/upload_585c8c2a6f53753ffb404e48ffec65f3.png)
### pwd
显示当前所处目录
```bash
$ pwd
```
![](https://huatu.98youxi.com/markdown/work/uploads/upload_6b0fade7528cae8a16db05ec946a1c8a.png)

### cd
切换工作的目录，可使用相对路径与绝对路径，相对路径切换多个目录可以使用../..这种格式
```bash
$  cd
```
![](https://huatu.98youxi.com/markdown/work/uploads/upload_ade6f8ed03d38bd6c06186ef2f11b5c3.png)
### touch、mkdir
**touch**是不存在文件则创建文件，存在则修改文件时间。
**mkdir**是创建目录
```bash
$ touch <文件名>
```
```bash
$ mkdir <目录名>
```
### cat、tail、head、tail、od、tee、more、less
1. **cat** 直接输出文件的全部内容
2. **head** 输出文件开头的内容、-n 指定行数
3. **tail** 输出文件末尾的内容，-n输出尾n行
```bash
$ cat <文件名>
```
### rm、cp、mv
1. **rm**删除某个文件，常用rm -r 用于删除目录
2. **cp**复制文件，-r可以复制目录
3. **mv**移动文件
```bash
$ rm -rf <目录名>
```
```bash
$ cp -r <原目录路径> <新目录路径>
```
```bash
$ mv -r <原目录路径> <新目录路径>
```
### find、grep、xargs
1. **find**，搜索文件命令，可通过通配符搜索某个文件
2. **grep**，以正则表达式进程全局查找匹配行
3.  **xargs**，命令传递参数的过滤器，可将管道或标准输入数据转换成命令行参数，也可从文件中读取数据

### tar、zip、uzip、gzip
1.**tar**将文件打包或压缩或解包，压缩文件后缀有gz、bz、xz，常用参数 -c产生.tar打包文件，-x解包、-zjJ分别以gz、bz2、xz打包或解包文件。
2.**zip**将文件打包，常用-r递归打包目录
3.**uzip**将文件解包
4.**gzip**压缩命令，只能压缩文件，不能压缩目录
```bash
$ tar [选择] xxx.tar.gz 打包的内容
```

### Linux重定向与管道
shell命令有三种标准文件：
1. 标准输入文件，使用<或<<
2. 标准输出文件，使用>或>>
3. 标准错误输出文件，使用2>或2>>
注：双符号表示追加

管道：
1. | 将上一次的输出作为下一次的输入
2. || 当左边命令为假，右边命令才会执行
3. & 表示任务在后台执行
4. &&前一条命令执行成功才会执行后门的命令
5. ;隔开命令，从左到右执行

应用实例：在hello.txt文件中，查找 "yes" 所在行，并且显示行号
```bash
$ cat hello.txt | grep -ni yes
```

### 三、Vim编辑器
一个强大的文本编辑器，常用的操作如下

| 命令 | 操作 |
|--|--|
| k/j | 向上或下查找 |
| gg | 移动到文件的第一行 |
| G | 移动到文件的最后一行 |
| /word | 搜索某个字符串，n表示到下一个 |
| n | 光标向下移动n行 |
| 0或$ | 移动到当前行首字符或尾字符 |
| dd/ggdG | 删除当前行，ndd表示连续删除后n行，ggdG表示删除全部 |
| yy | 复制当前行，nyy表示复制下面n行 |
| p/P | 将复制内容在下一行粘贴上/在上一行粘贴上 |
| u | 还原上一次操作 |
| ctrl+r | 重复上一次动作 |
| i | 光标前插入文本 |
| x | 删除光标字符 |
| R+word | 连续替换多个字符 |
| :%s/old/new/g | 有$替换整个文档的内容，无%替换该行全部，去掉g表示替换首个 |
| set nu | 显示行数 |


### 四、进程管理
### 1. 基本介绍
在Linux中，每个执行的程序（代码）都称为一个进程。每一个进程都分配一个ID号。
每一个进程，都会对应一个父进程，而这个父进程可以复制多个子进程。例如www服务器
每个进程都可能以两种方式存在的。前台与后台（守护进程），所谓前台进程就是用户目前的屏幕上可以进行操作的。后台进程则是实际在操作，但由于屏幕上无法看到的进程，通常使用后台方式执行。
一般系统的服务都是以后台进程的方式存在，而且都会常驻在系统中。直到关机才能结束。

### 2. 查看进程的相关指令
| 命令 | 操作 |
| -------- | -------- |
| ps     | 查看目前系统中，有哪些正在执行的进程，以及这些进程执行的情况，可以不加任何参数     |
| ps -a     | 显示当前终端的所有进程信息     |
| ps -u     | 以用户的格式显示进程信息     |
| ps -x    | 显示后台进程运行的参数     |
| ps -aux     | 查看详细信息  太多可以使用more分页查看  ps -aux | more     |

### 3.定时任务
一般linux的定时任务都会存放在/etc/crontab中

 1. linux可通过crontab设置定时任务，常用参数-e 设置任务，-l 查看任务计划
设置任务的时间格式为：
	分钟 小时 日期 月份 星期   命令 
```bash
$ crontab -e
```
```bash
$ */1 * * * * ls -l /etc/ > /tmp/to.txt
//表示每分钟执行ls -l /etc/ > /tmp/to.txt命令
```

### 五、磁盘管理
### 1.基本命令
|  命令 | 操作 |
| -------- | -------- |
| lsblk     | 列出所有存储装置     |
| blkid     | 列出装置的UUID，文件系统等参数     |
| parted /dev/vda print     | 列出/dev/vda的分区参数以及分区格式     |
| gdisk dev/vda     | 对dev/vda进行分区     |
### 2.磁盘分区操作

#### 1.添加虚拟磁盘
![](https://huatu.98youxi.com/markdown/work/uploads/upload_38ed72a0f767a3dc2ff2a17213aa9efe.png)
#### 2.磁盘分区
![](https://huatu.98youxi.com/markdown/work/uploads/upload_769516586ba75215bcb968bdb6cd493e.png)

#### 3. 磁盘挂载
![](https://huatu.98youxi.com/markdown/work/uploads/upload_2944d3573c9f1e673a181554dc613124.png)

![](https://huatu.98youxi.com/markdown/work/uploads/upload_166ea9f355068382ae75a798c31a89e3.png)

#### 4.非交互式磁盘分区
![](https://huatu.98youxi.com/markdown/work/uploads/upload_0fb654e9a4537aa1e9b09c515e4bb427.png)

#### 5.逻辑卷
LVM-逻辑卷管理是Linux环境中对磁盘分区进行管理的一种机制，是建立在硬盘和分区之上、文件系统之下的一个逻辑层，用于提高磁盘分区管理的灵活性

常用命令
|命令|解释|
|--|--|
|pvcreate  /DEV|创建物理卷|
|pvs|查看物理卷|
|pvremove /DEV|删除物理卷|
|vgcreate VGNAME /DEV|创建卷组|
|vgextend /DEV|扩展卷组|
|vgreduce VGNAME /DEV|收缩卷组|
|vgremove VGNAME|删除卷组|
|lvcreate -L 10G -n LVNAME VGNAME|创建指定逻辑卷大小和逻辑卷名称的名称|
|lvs|查看逻辑卷
|lvextend -L +10G /DEV|增加10G逻辑卷大小|
|lvremove /DEV/VGNAME/LVNAME|删除逻辑卷|

### 六、Shell脚本编程
#### 符号变量
|符号| 介绍 |
|--|--|
|# |注释符|
|$|变量符|
|'' |单引号字符，全部普通字符|
|""|双引号字符，可以包括特殊字符如反引号`，变量符$|
|$?|返回上一个变量返回值|
|$#|传送给shell程序位置参数的数量|
|$0|当前执行的进程名|
|$!|后台运行的最后一个进程号|
|$$|当前进程的进程号|
|$n|第n个参数|
|$@|全部位置参数|
|$()|获取命令输出结果|
|``|获取命令输出结果|
|$(())|算数拓展运算符|
|-eq、-ne、-lt、le、-gt、-ge|表示相等、不等于、小于、小于或等于、大于、大于或等于|
|[]|条件表达式|
|-d|是否是目录，如 if [-f a.sh]|
|-f|是否是普通文件，如if [-d a.txt]|
|-a、-o |逻辑和与逻辑或|

### 六、关于git
#### git是分布式的版本控制系统，是一种代码管理工具，能够方便程序员在编写代码，未完成时候能够保存但却不影响项目的运行。


**git**的常用命令：
|命令  |解释|
|--|--|
|git init |初始化git仓库|
|git config user.name name|设置目标用户名|
|git config user.email email|设置目标邮箱|
|git config --list|查看配置信息|
|git add 文件名|将文件添加到暂存区|
|git checkout|暂存区内容恢复到工作区|
|git commit -m "提交说明"|将文件从暂存区添加到仓库区|
|git log|查看提交日志|
|git reset --hard 版本号|将代码恢复到已经提交的某一个版本|
|git branch 分支名|创建分支|
|git checkout -b 分支名称|切换分支|
|git branch -d 分支名称|删除分支|
|git push URL master|将缓存区内容提交到远程仓库|
|git pull|将远程代码下载到本地|
|git remote add 仓库别名 仓库地址|为远程仓库添加别名|
|git push -u 别名  分支|将缓存区内容提交到仓库|

