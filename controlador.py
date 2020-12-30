from flask import Flask, render_template, request,  g, session, redirect, url_for
from flaskext.mysql import MySQL
import Modelo as Modelo

app = Flask(__name__)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config["DEBUG"] = True

@app.before_request
def before_request():
   g.user = None
   if 'user' in session:
      g.user = Modelo.buscarU(session['user'])

@app.route("/register")
def register():
    try:
        return render_template('register.html')
    except:
        return render_template('register.html')

@app.route("/pagos")
def pagos():
    try:
        return render_template('pagos.html')
    except:
        return render_template('pagos.html')

@app.route("/mispagos")
def mispagos():
    try:
        return render_template('mispagos.html')
    except:
        return render_template('mispagos.html')


@app.route("/")
def login():
    try:
        print("login1")
        return render_template('login.html')
    except:
        return render_template('login.html')
        
 
@app.route('/login',methods=['GET','POST'])
def lo():
    try: 
        if g.user:
            session.pop('user', None)  

        if request.method=='POST':
            session.pop('user', None)
            user = request.form['correo']
            _contrasena = request.form['contrasena']

            _bool=Modelo.validar(user, _contrasena)
            session['user'] = user
            print(_bool)
   
        if _bool == True:
            session['user'] = user
            return redirect(url_for('register'))
            

        if _bool == False:
            session['user'] = user
            return render_template('login.html', alert='Tu contraseña o usuario es incorrecto') 
    except:
        return redirect(url_for('Login')) 
            
    finally:
            print("Lets go!")

@app.route('/log')
def Login():
    return render_template('login.html', alert='Tu contraseña o usuario es incorrecto')


@app.route("/editar",methods=['POST','GET'])
def postedit():
    try:
        
        _nombrel = request.form.get('nombrel')
        _direccion = request.form.get('direccion')
        _dinero = request.form.get('dinero')
        _interese = request.form.get('interese')
        _comentarios = request.form.get('comentarios')
        nombre1 = session['user']
        _bool = Modelo.local(_nombrel,_direccion, _dinero, _interese, _comentarios,nombre1)
        
        if _bool == True:
            nombre1 = session['user']
            return redirect(url_for('postedit'))           

        if _bool == False:
           return redirect(url_for('errorr')) 
    except:
       return redirect(url_for('errorr'))

@app.route("/errorr")
def errorr():
    try:
        return render_template("Error.html")
    except:
        return redirect(url_for('errorr')) 


if __name__ == "__main__":
    app.run()
    app.run(debug=True)