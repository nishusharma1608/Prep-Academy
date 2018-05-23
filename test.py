import sqlite3 as sql

conn = sql.connect("project.db")

cur = conn.cursor()
# cur.execute("DROP TABLE students")
# cur.execute("CREATE TABLE students (RegdNo TEXT PRIMARY KEY, name TEXT NOT NULL, password TEXT NOT NULL)")
# print "Table created successfully"
# cur.execute("INSERT INTO students VALUES (\"IH201685006\", \"Chaitanya\", \"asc123\")")
# cur.execute("INSERT INTO students VALUES (\"IH201685065\", \"Mahesh\", \"mahesh123\")")
# cur.execute("INSERT INTO students VALUES (\"IH201685097\", \"Likhitha\", \"likhitha123\")")
# cur.execute("INSERT INTO students VALUES (\"IH201685066\", \"Nishu\", \"nishu123\")")
# cur.execute("INSERT INTO students VALUES (\"IH201685020\", \"Kavya\", \"kavya123\")")
# cur.execute("INSERT INTO students VALUES (\"IH201685028\", \"Jahnavi\", \"jahnavi123\")")
# cur.execute("INSERT INTO students VALUES (\"IH201685085\", \"Sandeep\", \"sandeep123\")")
# conn.commit()
# cur.execute("SELECT RegdNo FROM students where RegdNo in (?,?)",('IH201685006','IH201685006'))

# print "Selection successful"
# result=cur.fetchall()
# print result
# cur.execute("CREATE TABLE Appearances (RegdNo TEXT NOT NULL, name TEXT NOT NULL, Company TEXT NOT NULL, PRIMARY KEY (RegdNo,Company))")
# print "Created another table"
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685006\", \"Chaitanya\", \"AmEx\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685065\", \"Mahesh\", \"Amazon\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685097\", \"Likhitha\", \"Oracle\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685020\", \"kavya\", \"Microsoft\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685028\", \"janavi\", \"TCS\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685085\", \"Sandeep\", \"Facebook\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685066\", \"Nishu\", \"Google\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685006\", \"Chaitanya\", \"IBM\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685065\", \"Mahesh\", \"AmEx\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685097\", \"Likhitha\", \"JP Morgan\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685020\", \"kavya\", \"Google\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685028\", \"janavi\", \"Amazon\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685085\", \"Sandeep\", \"Flipkart\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685066\", \"Nishu\", \"Microsoft\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685006\", \"Chaitanya\", \"Nvidia\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685065\", \"Mahesh\", \"Magnitude\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685097\", \"Likhitha\", \"VMware\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685020\", \"kavya\", \"TCS\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685028\", \"janavi\", \"CTS\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685085\", \"Sandeep\", \"IBM\")")
# cur.execute("INSERT INTO Appearances VALUES (\"IH201685066\", \"Nishu\", \"Nvidia\")")

# conn.commit()
# cur.execute("SELECT * FROM Appearances")
# result=cur.fetchall()
# print result
# cur.execute("CREATE TABLE Company (name TEXT NOT NULL, requirement TEXT NOT NULL, PRIMARY KEY (name,requirement))")
# print "Created Company table"
# cur.execute("INSERT INTO Company VALUES ( \"AmEx\",\"c++\")")
# cur.execute("INSERT INTO Company VALUES ( \"Amazon\",\"c++\")")
# cur.execute("INSERT INTO Company VALUES (\"Oracle\",\"c++\")")
# cur.execute("INSERT INTO Company VALUES (\"Microsoft\",\"c++\")")
# cur.execute("INSERT INTO Company VALUES ( \"TCS\",\"java\")")
# cur.execute("INSERT INTO Company VALUES (\"AmEx\",\"java\")")
# cur.execute("INSERT INTO Company VALUES ( \"AmEx\",\"data structures\")")
# cur.execute("INSERT INTO Company VALUES ( \"Amazon\",\"Java\")")
# cur.execute("INSERT INTO Company VALUES (\"Oracle\",\"Java\")")
# cur.execute("INSERT INTO Company VALUES (\"Microsoft\",\"Java\")")
# cur.execute("INSERT INTO Company VALUES ( \"TCS\",\"Data base\")")
# cur.execute("INSERT INTO Company VALUES (\"Micro soft\",\"data structures\")")
# cur.execute("INSERT INTO Company VALUES ( \"TCS\",\"java\")")
# cur.execute("INSERT INTO Company VALUES (\"AmEx\",\"java\")")
# cur.execute("INSERT INTO Company VALUES ( \"AmEx\",\"data structures\")")
# cur.execute("INSERT INTO Company VALUES ( \"Nvidia\",\"Java\")")
# cur.execute("INSERT INTO Company VALUES (\"IBM\",\"Java\")")
# cur.execute("INSERT INTO Company VALUES (\"JP morgon\",\"data structures\")")
# cur.execute("INSERT INTO Company VALUES ( \"VMware\",\"OS\")")
# cur.execute("INSERT INTO Company VALUES (\"Magnitude\",\"OS\")")
# cur.execute("INSERT INTO Company VALUES ( \"Google\",\"java\")")
# cur.execute("INSERT INTO Company VALUES (\"Flipkart\",\"java\")")
# cur.execute("INSERT INTO Company VALUES ( \"Nvidia\",\"data structures\")")
# cur.execute("INSERT INTO Company VALUES ( \"CTS\",\"Java\")")
# cur.execute("INSERT INTO Company VALUES (\"VMware\",\"Java\")")
# cur.execute("INSERT INTO Company VALUES (\"IBM\",\"c++\")")
# cur.execute("INSERT INTO Company VALUES ( \"Flipkart\",\"Data base\")")
# cur.execute("INSERT INTO Company VALUES (\"Facebook\",\"data structures\")")
cur.execute("CREATE TABLE students (RegdNo TEXT PRIMARY KEY, name TEXT NOT NULL, password TEXT NOT NULL)")
conn.commit()
cur.execute("SELECT * FROM Company")
result=cur.fetchall()
print result
conn.close()