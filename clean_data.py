import os
import shutil

dataset_path = 'clean_data' 
cultures_africaines = [
    'Corn', 'Tomato', 'Cassava', 'Potato', 'Pepper_bell', 'Squash'
]

def clean_dataset(path):
    if not os.path.exists(path):
        print(f"Erreur : Le dossier {path} n'existe pas.")
        return

    print("--- Début du nettoyage du dataset ---")
    dossiers = os.listdir(path)
    
    for folder in dossiers:
        
        is_useful = any(culture in folder for culture in cultures_africaines)
        
        if not is_useful:
            folder_path = os.path.join(path, folder)
            print(f"Suppression du dossier inutile : {folder}")
            shutil.rmtree(folder_path) 
            
    print("--- Nettoyage terminé ! ---")
    print(f"Dossiers restants : {os.listdir(path)}")

if __name__ == "__main__":
    clean_dataset(dataset_path)