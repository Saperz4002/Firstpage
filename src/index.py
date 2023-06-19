from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__': #para un archivo de ejecucion
    app.run(debug = True) #para q se mantenga escuchando
    #En un modo de prueba




