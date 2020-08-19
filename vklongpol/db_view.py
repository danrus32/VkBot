import sqlite3
db = sqlite3.connect("DroidALLIN/Users.db")
sql = db.cursor()

for value in sql.execute("SELECT * FROM  Users"):
    print(value)
