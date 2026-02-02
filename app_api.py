from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import json
from PIL import Image
import io
import os

app = Flask(__name__)

# Chemins vers vos fichiers
MODEL_PATH = "models/agroconnect_model.tflite"
LABELS_PATH = "models/labels.json"

# 1. Chargement sécurisé
if not os.path.exists(MODEL_PATH) or not os.path.exists(LABELS_PATH):
    print("❌ ERREUR : Fichiers modèles introuvables dans /models")
else:
    interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
    interpreter.allocate_tensors()
    with open(LABELS_PATH, 'r') as f:
        labels = json.load(f)
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    print("✅ Modèle et Labels chargés avec succès !")

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier envoyé'}), 400
    
    file = request.files['file']
    img = Image.open(io.BytesIO(file.read())).convert('RGB')
    img = img.resize((224, 224))
    
    img_array = np.array(img, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    interpreter.set_tensor(input_details[0]['index'], img_array)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    
    prediction_idx = str(np.argmax(output_data))
    result = labels.get(prediction_idx, "Inconnu")
    confidence = float(np.max(output_data))

    return jsonify({
        'maladie': result,
        'confiance': f"{confidence*100:.2f}%",
        'status': 'success'
    })

if __name__ == '__main__':
    print("🚀 API AgroConnect lancée sur http://127.0.0.1:5000")
    app.run(debug=False, port=5000)
