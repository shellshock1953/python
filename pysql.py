import MySQLdb
db = MySQLdb.connect(host="localhost", user="root", passwd="mysql.157345", db="first", charset='utf8')

cursor = db.cursor()
sql = """select fname from members where member_id=1;"""
cursor.execute(sql)
data =  cursor.fetchall()

print (data[0][1])
