import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models
import os

# 1. Configuration des paramètres
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
# Chemins basés sur votre structure de dossiers
TRAIN_DIR = 'PlantVillage/train'
VAL_DIR = 'PlantVillage/val'

# Créer le dossier 'models' s'il n'existe pas pour éviter les erreurs d'enregistrement
if not os.path.exists('models'):
    os.makedirs('models')

# 2. Préparation des données (Data Augmentation)
# On normalise les images et on ajoute des variations pour simuler le plein soleil/ombre
datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=25,
    zoom_range=0.2,
    brightness_range=[0.8, 1.2],
    horizontal_flip=True
)

print("📸 Chargement des images d'entraînement...")
train_gen = datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

print("📸 Chargement des images de validation...")
val_gen = datagen.flow_from_directory(
    VAL_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# 3. Création du modèle (Architecture MobileNetV2 pour la rapidité < 3s)
# On utilise le transfert learning pour gagner en précision
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False  # On gèle la base pour un entraînement rapide

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(train_gen.num_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 4. Lancement de l'entraînement
print(f"🚀 Lancement de l'entraînement pour {train_gen.num_classes} maladies...")
# On commence par 3 époques pour tester la rapidité
history = model.fit(
    train_gen, 
    validation_data=val_gen, 
    epochs=3 
)

# 5. Sauvegarde du modèle final
model.save('models/agroconnect_model.h5')
print("\n✅ Félicitations ! Modèle sauvegardé sous : models/agroconnect_model.h5")