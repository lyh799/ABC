import pymysql
import json

kucuen_sa = 0
# 打开数据库连接
conf = json.load(open(r"C:\Users\Administrator\Desktop\项目\超市系统\conf.json"))  # 配置信息
db = pymysql.connect(conf["db_server"], conf["db_user"], conf["db_password"], conf["db_name"])
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 进货
def tiaojia():

    print("请选择您要进行的操作：1.添加新商品，2.进货")
    sr=input(">>>>")
    if sr=="1":
        uname = input("请输入商品名称:")
        jinjia = int(input("请输入添加商品价格:"))
        shoujia = int(input("请输入售价："))
        jinhuo = int(input("请输入进货数量："))
        kucuen = int(input("请输入库存数量："))
        # SQL 插入语句
        sql = "insert into chaoshi (uname,jinjia,shoujia,jinhuo,kucuen) values('%s',%s,%s,%s,%s)" % \
                (uname,jinjia,shoujia,jinhuo,kucuen)

        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 如果发生错误则回滚
        db.rollback()
        # 关闭数据库连接
        db.close()
    if sr == "2":
        tiaojia1()

def tiaojia1():
    uname = input("请输入商品名称:")
    kucuen = int(input("请输入要入库数量："))
    # SQL 插入语句
    sql = "update chaoshi set kucuen=kucuen+{} where uname='{}'".format(kucuen,uname)
    cursor.execute(sql)
    db.commit()
    db.close()   


# 删除
def delete():
    print("请选择您要进行的操作:1.删除某一种商品,\
        2.删除所有商品")
    de = input(">>>>")
    if de == "1":
        uname = input("请输入您要删除的商品名称：")
         # SQL 插入语句
        sql = "delete from chaoshi where uname='%s'"%uname
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 如果发生错误则回滚
        db.rollback()
        # 关闭数据库连接
        db.close()
         # truncate
    if de == "2":
        delete1()

def delete1():
    sql = "truncate chaoshi  "
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    # 如果发生错误则回滚
    db.rollback()
    # 关闭数据库连接
    db.close()

# 查询
def query():
    print("请选择您要进行的操作：1.查询单一商品，\
        2.查询所有商品(输入*)")
    que = input(">>>>")
    if que =="1":
        uname = input("请输入您要查询的商品名称：")
        sql = "select * from chaoshi where uname='%s'"%uname
    if que == "2":
        sql = "select * from chaoshi"
        # 执行sql语句
    cursor.execute(sql)
    abc = cursor.fetchall()
    for row in abc:
        cid = row[0]
        uname = row[1]
        jinjia = row[2]
        shoujia = row[3]
        jinhuo = row[4]
        kucuen = row[5]
    # 提交到数据库执行
    db.commit()
    print ("cid=%s,uname='%s',jinjia=%s,shoujia=%s,jinhuo=%s,kucuen=%s" % \
            (cid, uname, jinjia, shoujia, jinhuo, kucuen ))
    # 如果发生错误则回滚
    db.rollback()
    # 关闭数据库连接
    db.close()

def sale():
    global kucuen_sa
    while True:
        print("请选择您要进行的操作：1.商品出售，\
            2.查看销售额\
            3.退出")
        sa = input(">>>>")
        if sa == "1":
            uname = input("请输入要出售的商品名称：")
            kucuen = int(input("请输入要出售的个数："))
            sql = "update chaoshi set kucuen=kucuen-{} where uname='{}' ".format(kucuen,uname)
            kucuen_sa += kucuen
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            # 如果发生错误则回滚
            db.rollback()
            # 关闭数据库连接
            db.close()
        if sa == "2":
            sql = "select AVG(shoujia-jinjia) from chaoshi where shoujia-jinjia "
            # 执行sql语句
            cursor.execute(sql)
            data = cursor.fetchone()
            dat=int(data[0])*kucuen_sa
            # 提交到数据库执行
            db.commit()
            print(" 销售额为 :%s" % dat)
            # 如果发生错误则回滚
            db.rollback()
            # 关闭数据库连接
            db.close()
        if sa == "3":
            break
# sale()






