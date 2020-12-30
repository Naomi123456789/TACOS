from flask import Flask, render_template, request, json, url_for, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'sepherot_naomi'
app.config['MYSQL_DATABASE_PASSWORD'] = 'AxFeFfWKF1'
app.config['MYSQL_DATABASE_DB'] = 'sepherot_naomiBD'
app.config['MYSQL_DATABASE_HOST'] = 'nemonico.com.mx'
mysql = MySQL(app)

def buscarU(_user):
    if _user:
        conn = mysql.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM USERS WHERE MAIL = '"+_user+"'"
        try: 
            cursor.execute(query,(_user))
            data = cursor.fetchall()
            if data:
                return data[0][2]
            else:
                return False
        except:
            cursor.close()
            conn.close()
            return redirect(url_for('errorr')) 
            
    else: 
            return redirect(url_for('errorr'))   

def local(_nombrel,_direccion, _dinero, _interese, _comentarios,nombre1):

    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        query = "INSERT INTO C_locals (NAME, ADRESS, MONEY, INTEREST, COMMENTS) VALUES ('"+_nombrel+"', '"+_direccion+"' '"+_dinero+"' '"+_interese+"' '"+ _comentarios+"')"
        cursor.execute(query)
        data = cursor.fetchall()

        if len(data)==0:
            conn.commit()
            return True
        else:
            return False

    except:
        cursor.close()
        conn.close()
        return redirect(url_for('errorr')) 
            
 


def validar(user, _contrasena):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlvalidarProcedure = "SELECT MAIL FROM C_users where MAIL= ""'"+user+"'"
        print(sqlvalidarProcedure)
        cursor.execute(sqlvalidarProcedure)
        data = cursor.fetchall()

        if data:
            sqlvalidar2Procedure = "SELECT PASSWORD FROM C_users where MAIL= ""'"+user+"'"
            print(sqlvalidar2Procedure)
            cursor.execute(sqlvalidar2Procedure)
            data2 = cursor.fetchall()
            print("real")
            print(data2)
            data2=str(data2)

            _contrasena=str("(('"+_contrasena+"',),)")
            print(_contrasena)
            
            
            if data2 == _contrasena:
                return True
            else:
                return False

        else:
            return False 


    except:
        return False 
        
    finally:
        cursor.close()
        conn.close()

 