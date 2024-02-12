import sqlite3

conn=sqlite3.connect("afternoon.db")
print("Opened database successfully")
conn.execute("INSERT INTO EMPLOYEES VALUES (1,'ANNA KURIA',45 ,340000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2,'STEPHEN NJOROGE',56 ,190000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3,'BERNICE KIMANI',24,67900.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4,'TERRY TERER',35 ,320000.00)")


conn.commit()
print("Employee inserted successfully")
conn.close()
