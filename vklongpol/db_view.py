import sqlite3
db = sqlite3.connect("DroidALLIN/Users.db")
sql = db.cursor()

for value in sql.execute("SELECT * FROM  Users"):
    print(value)
sql.execute(f'UPDATE Users SET user_id == ? WHERE Balance  = ?',('498475069',50))
db.commit()