#!/usr/bin/python
# coding=utf-8

import pymysql

try:
    # 打开数据库连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='password', db='apads')

    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()

    # SQL 查询语句
    sql = "select c.ownerId, c.codeId,s.platForm,s.appId,s.style,s.size,s.adCount,s.imgCount,s.adSlotId,s.online  \
            from appcode c, appstyle s \
            where  \
            c.codeId = s.codeId  \
            and c.configStatus = 1  \
            and c.publishStatus = 1  \
            and c.logicDelFlg = 0 \
            and s.styleEnable = 1 \
            and s.appId IS NOT NULL \
            and s.adSlotId IS NOT NULL"

    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        codeId = row[1]
        # 打印结果
        print(codeId)
except Exception as e:
    print(e)

# 关闭数据库连接
conn.close()
