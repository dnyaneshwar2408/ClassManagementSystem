import sqlite3


con = sqlite3.connect('class.db')
cur = con.cursor()

# con.execute("INSERT INTO studinfo (sid,sname,sphnno,semail,scourse,sdate)  VALUES (1,'raj','7506931269','raj@gmail.com','CCC','19-10-2022')");
# # con.commit()
# con.execute("INSERT INTO signup   VALUES (1,'raj','7506931269','S0nu r@j')");
# con.commit()
# con.execute("delete from studinfo");
# con.commit()
table_list = [a for a in cur.execute("SELECT * FROM signup")]
print(table_list)