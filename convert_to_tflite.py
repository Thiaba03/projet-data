import tensorflow as tf
import os

# Chemins absolus pour éviter les erreurs
base_dir = r'C:\AgroIA'
h5_path = os.path.join(base_dir, 'models', 'agroconnect_model.h5')
tflite_path = os.path.join(base_dir, 'models', 'agroconnect_model.tflite')

print(f"🔄 Tentative de lecture de : {h5_path}")

if os.path.exists(h5_path):
    # Charger le modèle
    model = tf.keras.models.load_model(h5_path)
    
    # Configurer le convertisseur
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    
    # Lancer la conversion
    tflite_model = converter.convert()
    
    # Écriture forcée du fichier
    with open(tflite_path, 'wb') as f:
        f.write(tflite_model)
        f.flush()
        os.fsync(f.fileno()) # Force Windows à écrire sur le disque
        
    size = os.path.getsize(tflite_path)
    print(f"✅ Conversion TERMINEE !")
    print(f"Taille du fichier genere : {size / (1024*1024):.2f} Mo")
else:
    print(f"❌ ERREUR : Le fichier {h5_path} est introuvable.")
