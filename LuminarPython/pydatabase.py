import pymysql
db = pymysql.connect(host='localhost', user='root', password='Root', db='db1')

# prepare cursor object using cursor() method
cur1 = db.cursor()
sql = "select count(Name) from stdnew"
cur1.execute(sql)
print("The number of students is =", count)
db.commit()
