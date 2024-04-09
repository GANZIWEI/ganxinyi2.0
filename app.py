from flask import Flask, render_template ,jsonify

app = Flask(__name__)

stupid_person_collection = [
    {
        'id': 1,
        'Name': 'Gan Xin Yi',
        'Problem': 'Brain',
        'Stupid index': '60%',
        'html': '/Gxyidoitface.html',
    },
    {
        'id': 2,
        'Name': 'Amelia',
        'Problem': 'Hand',
        'Stupid index': '75%',  # Corrected
        'html': '/amelia.html',
    },
    {
        'id': 3,
        'Name': 'Bonjour__',
        'Problem': 'Body Interupt',
        'Stupid index': '80%',
        'html': '/bonjour.html',
    },
    {
        'id': 4,
        'Name': 'Gan Gan',
        'Problem': 'Face Problem',
        'Stupid index': '100%',
        'html': '/gangan.html',
    }
]


@app.route("/")
def hello_world():
    return render_template('home.html', persons=stupid_person_collection)

@app.route("/person")
def list_job():
    return jsonify(stupid_person_collection)

@app.route("/button")
def button_job():
    return render_template('button.html',debug=True)

@app.route("/Gxyidoitface.html")
def gxy_idoit_face():
    return render_template('Gxyidoitface.html')

@app.route("/amelia.html")
def amelia_idoit_face():
    return render_template('amelia.html')

@app.route("/bonjour.html")
def bonjour_idoit_face():
    return render_template('bonjour.html')

@app.route("/gangan.html")
def gangan_idoit_face():
    return render_template('gangan.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
