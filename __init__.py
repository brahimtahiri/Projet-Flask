from flask import Flask
from flask import render_template
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    result = val_user * val_user
    pair = "impair"

    if result % 2 == 0:
        pair = "pair"

    return "<h2>Le carré de votre valeur est : </h2>" + str(result) + ", le résultat est " + pair