# AgroConnect Africa - Module IA
Développé par : Membre C

## Contenu :
- train_model.py : Script d'entraînement (Précision 93%)
- yield_estimation.py : Calculateur de rendement (Tonnes/ha)
- models/agroconnect_model.tflite : Modèle optimisé pour mobile (< 3s)

## Utilisation :
1. Activer le venv : .\venv\Scripts\activate
2. Calculer rendement : python yield_estimation.py

En parallèle, `yield_estimation.py` calcule une estimation de récolte indépendamment du modèle IA.

---

## 📁 Contenu du dépôt

| Fichier | Rôle |
|---|---|
| `clean_data.py` | Nettoie le dataset PlantVillage : ne garde que les cultures africaines ciblées |
| `train_model.py` | Entraîne le modèle de reconnaissance des maladies (précision ≈ 93 %) |
| `convert_to_tflite.py` | Convertit le modèle entraîné au format léger TensorFlow Lite (< 3 s d'inférence) |
| `app_api.py` | API Flask qui reçoit une photo et renvoie le diagnostic |
| `yield_estimation.py` | Calculateur de rendement (tonnes/ha) selon la culture et la surface |
| `models/` | Contient le modèle final `agroconnect_model.tflite` et les labels |
| `PlantVillage/` | Dataset d'images utilisé pour l'entraînement |

---

## 🧰 Prérequis

- Python 3.x
- Bibliothèques : `tensorflow`, `flask`, `numpy`, `pillow`

Installation :
```bash
pip install tensorflow flask numpy pillow
```

---

## 🚀 Utilisation

**1. Activer l'environnement virtuel**
```bash
.\venv\Scripts\activate
```

**2. (Optionnel) Nettoyer le dataset**
```bash
python clean_data.py
```

**3. Entraîner le modèle**
```bash
python train_model.py
```

**4. Convertir le modèle pour mobile**
```bash
python convert_to_tflite.py
```

**5. Lancer l'API de prédiction**
```bash
python app_api.py
```
L'API est disponible sur `http://127.0.0.1:5000/predict` (requête `POST` avec une image dans le champ `file`).

**6. Calculer un rendement estimé**
```bash
python yield_estimation.py
```

---

## 📊 Résultats

- Précision du modèle : **~93 %**
- Temps d'inférence sur mobile : **< 3 secondes**
- Format de sortie de l'API : JSON (`maladie`, `confiance`, `status`)

---

## 🔭 Pistes d'amélioration

- Entraînement sur plus d'epochs avec `EarlyStopping`
- Quantification du modèle TFLite pour réduire encore sa taille
- Sécurisation de l'API (authentification, limite de taille des fichiers)
- Connexion de `yield_estimation.py` à l'API pour un usage complet depuis l'application
