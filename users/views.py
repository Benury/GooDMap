#/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from django.http import HttpResponse
import json
import pymysql
from webgl import WGL

import sys
reload(sys)
sys.setdefaultencoding('utf8')
class IndexView(View):
    def get(self, request):

        return render(request, 'index.html', {})




class MapView(View):
    def get(self,request):
        conn = pymysql.connect(host="127.0.0.1", user="root", port=3306, passwd="123456", db="article_splider",
                               charset="utf8")
        cursor = conn.cursor()
        sql = "select ipaddr, username from ipmap"
        cursor.execute(sql)
        result = cursor.fetchall()
        result = list(result)
        resdata = []
        for item in result:
            point = WGL().getPoint(item[0])
            point = point["result"]["location"]
            x = point["lng"]
            y = point["lat"]
            name = item[1]
            resdata.append({'x':x,'y':y,'name':name})
        cursor.close()
        # 关闭连接
        conn.close()
        return HttpResponse(json.dumps(resdata), content_type='application/json')
    def post(self, request):
        ip1 = request.POST["ip"]
        name1 = request.POST["name"]
        name1 = name1.encode("utf-8")

        data = WGL().getPoint(ip1)
        if "status" in data:
            data = data["result"]["location"]
            conn = pymysql.connect(host="127.0.0.1", user="root",port=3306, passwd="123456", db="article_splider", charset="utf8")
            cursor = conn.cursor()
            sql = "insert into ipmap(ipaddr,username,x,y) VALUES ('{0}','{1}',{2},{3}) ON DUPLICATE KEY UPDATE ipaddr=VALUES(ipaddr), x=VALUES (x), y = VALUES (y)".format(ip1,name1,data["lng"],data["lat"])
            cursor.execute(
                sql
            )
            conn.commit()
            cursor.close()
            # 关闭连接
            conn.close()
            return HttpResponse(json.dumps({'x': data["lng"], 'y': data["lat"], 'name': name1}),
                            content_type='application/json')
        # 保存到数据库中
        # else:
        #     return HttpResponse(json.dumps({}), content_type='application/json')
