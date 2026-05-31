from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model_tiba = joblib.load("model_tiba.pkl")
model_berangkat = joblib.load("model_berangkat.pkl")

def menit_ke_jam(menit):
    jam = int(menit // 60)
    mnt = int(menit % 60)
    return f"{jam:02d}:{mnt:02d} WIB"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    X = [[
        int(data["cuaca"]),
        int(data["gelombang"]),
        int(data["hari"]),
        int(data["penumpang"])
    ]]

    tiba = model_tiba.predict(X)[0]
    berangkat = model_berangkat.predict(X)[0]

    jam_tiba = menit_ke_jam(tiba)
    jam_berangkat = menit_ke_jam(berangkat)

    kapasitas = 35
    jumlah_kapal = int(np.ceil(int(data["penumpang"]) / kapasitas))

    return jsonify({
        "jam_tiba": jam_tiba,
        "jam_berangkat": jam_berangkat,
        "jumlah_kapal": jumlah_kapal,
        "penumpang": data["penumpang"]
    })

if __name__ == "__main__":
    app.run(debug=True)