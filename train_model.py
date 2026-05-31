import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset CSV
df = pd.read_csv("dataset_canti.csv")

# ======================
# PREPROCESSING
# ======================

# Encoding manual (biar bisa dipakai ML)
mapping_cuaca = {
    "Cerah": 0,
    "Berawan": 1,
    "Hujan": 2
}

mapping_gelombang = {
    "Rendah": 0,
    "Sedang": 1,
    "Tinggi": 2
}

mapping_hari = {
    "Senin": 0,
    "Selasa": 0,
    "Rabu": 0,
    "Kamis": 0,
    "Jumat": 0,
    "Sabtu": 1,
    "Minggu": 1
}

df["cuaca"] = df["cuaca"].map(mapping_cuaca)
df["gelombang"] = df["gelombang"].map(mapping_gelombang)
df["hari"] = df["hari"].map(mapping_hari)

# ======================
# KONVERSI JAM KE MENIT
# ======================

def time_to_minutes(t):
    jam, menit = map(int, t.split(":"))
    return jam * 60 + menit

df["tiba"] = df["jam_tiba"].apply(time_to_minutes)
df["berangkat"] = df["jam_berangkat"].apply(time_to_minutes)

# ======================
# FEATURE & TARGET
# ======================

X = df[["cuaca", "gelombang", "hari", "penumpang"]]
y_tiba = df["tiba"]
y_berangkat = df["berangkat"]

# ======================
# TRAIN MODEL
# ======================

model_tiba = RandomForestRegressor(n_estimators=100, random_state=42)
model_berangkat = RandomForestRegressor(n_estimators=100, random_state=42)

model_tiba.fit(X, y_tiba)
model_berangkat.fit(X, y_berangkat)

# ======================
# SIMPAN MODEL
# ======================

joblib.dump(model_tiba, "model_tiba.pkl")
joblib.dump(model_berangkat, "model_berangkat.pkl")

print("✅ Model berhasil dibuat dari dataset CSV!")