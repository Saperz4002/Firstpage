from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'
if __name__ == '__main__': #para un archivo de ejecucion
    app.run() #para q se mantenga escuchando




