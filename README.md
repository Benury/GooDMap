# 基于地理位置的QQ好友定位服务

由于需要找到某个人，但是只知道对方的QQ号，于是呼开发了一个定位系统，该系统使用百度的精确定位API，能够比较准确的定位，这里我定位了部分QQ好友，该系统能够了解好友在全国范围内的分布情况。

预览
--------
![(http://op3poqi43.bkt.clouddn.com/mymapgitimg.png)]

技术栈
=========
django + mysql 

功能
====

> - 根据IP地址请求百度地图精确定位API，获取地理坐标
> - 使用百度地图API生成地图，并在页面中显示
> - 在页面中可添加好友，添加后自动在地图上标注，并存储到mysql中




使用方法
=========
访问地址：

代码组织架构
===========




Change Log 
===================

v1.0 
-------------

