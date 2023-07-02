import mysql.connector as sqlcn
db=sqlcn.connect(host="127.0.0.1",user="root",password="System",database="campus")
if(db.is_connected):
    print("Successful")
else:
    print("Not Successful")
    
cur=db.cursor()


#cur.execute(sql)
sql="""CREATE TABLE if not exists customer
       (cid int(2) PRIMARY KEY,
       cname varchar(25),
       cadd  varchar(55)
       )"""
sq="""Insert into customer(cid,cname,cadd)
    Values
    (6,'riya','kolkata')"""
cur.execute(sq)
db.commit()
print("record inserted")
