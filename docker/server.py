#!/usr/bin/env python
#-*- coding:utf8 -*-   #支持汉字
import socket   #导入socket模块
s = socket.socket()   #s等于socket模块中的socket类
host = '127.0.0.1'   #socket模块中gethostname()函数能够得到当前主机名
port = 1286 #端口
s.bind((host,port))  #使用bind方法后，在调用listen方法监听某个地址；
s.listen(5)   #listen方法只有一个参数，表示服务器未处理的连接数（允许的排队长度）
c,addr = s.accept()   #accept方法会返回一个格式为（client，address）的元组，client是客户端套接字，address是地址
print ("Got connection from") , addr   #打印出目前连接的地址
while True:
    Data = c.recv(1024) #接收信息
    if not Data:break   #如果客户端传输过来的信息为空，关闭连接
    print  (Data)   #打印客户端传来的信息
    c.send(Data)  #把客户端传来的信息传给客户端
s.close()   #关闭套接字，可以把close写在循环外面，这样就可以一直通信，直到客户端主动断开
