from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exercices_base1')
def exercices_base1():
    return render_template('exercices_base1.html')

@app.route('/exercices_base2')
def exercices_base2():
    return render_template('exercices_base2.html')

@app.route('/exercices_base3')
def exercices_base3():
    return render_template('exercices_base3.html')

@app.route('/exercices_base4')
def exercices_base4():
    return render_template('exercices_base4.html')

@app.route('/tp1')
def tp1():
    return render_template('tp1.html')

@app.route('/maison')
def maison():
    return render_template('maison.html')

@app.route('/vallet')
def vallet():
    return render_template('vallet.html')

@app.route('/carre')
def carre():
    return render_template('c')

if __name__ == '__main__':
    app.run(debug=True)
