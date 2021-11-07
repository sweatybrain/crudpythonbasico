import sqlite3
class sqlitedb():
    def createDB(self):
        dbcon = sqlite3.connect('usuario.db')
        cur = dbcon.cursor()
        cur.execute("CREATE TABLE usuarios( user_id TEXT PRIMARY KEY,nome TEXT,cpf INTEGER)")
        dbcon.commit()
        dbcon.close()


    def createuser(self,user_id,nome,cpf):
        dbcon = sqlite3.connect('usuario.db')
        cur = dbcon.cursor()
        cur.execute("INSERT INTO usuarios VALUES(?,?,?)",(user_id,nome,cpf))
        dbcon.commit()
        dbcon.close()
    
    def updateuser(self,user_id,nome,cpf):
        dbcon = sqlite3.connect('usuario.db')
        cur = dbcon.cursor()
        cur.execute("UPDATE usuarios SET nome=?,cpf=? WHERE user_id = ?",(nome,cpf,user_id))
        dbcon.commit()
        dbcon.close()

    def deleteuser(self,user_id):
        dbcon = sqlite3.connect('usuario.db')
        cur = dbcon.cursor()
        cur.execute("DELETE FROM usuarios WHERE user_id = ?",(user_id,))
        dbcon.commit()
        dbcon.close()

    def selectuser(self,user_id):
        dbcon = sqlite3.connect('usuario.db')
        cur = dbcon.cursor()
        cur.execute("SELECT * FROM usuarios WHERE user_id = ?",(user_id,))
        rows = cur.fetchall()
        dbcon.close()
        return rows

db = sqlitedb()
try:
    db.createDB()
except:
    print("print banco já criado")

db.createuser(1,"marcio", 5621757920)
print(db.selectuser(1))
db.updateuser(1,"joão",10101010)
print(db.selectuser(1))
db.deleteuser(1)
print(db.selectuser(1))
