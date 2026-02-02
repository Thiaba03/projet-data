def calculer_rendement_agroconnect(culture, surface_ha):
    donnees_cultures = {
        "Maïs": {"densite": 55000, "poids_moyen": 0.3},
        "Tomate": {"densite": 25000, "poids_moyen": 2.5},
        "Manioc": {"densite": 10000, "poids_moyen": 2.0}
    }
    if culture in donnees_cultures:
        c = donnees_cultures[culture]
        total = (surface_ha * c["densite"] * c["poids_moyen"]) / 1000
        return round(total, 2)
    return 0

ma_surface = 1.5
ma_culture = "Tomate"
resultat = calculer_rendement_agroconnect(ma_culture, ma_surface)

print(f"\n--- OUTIL D'ESTIMATION AGROCONNECT ---")
print(f"Culture selectionnee : {ma_culture}")
print(f"Surface declaree : {ma_surface} hectares")
print(f"Rendement estime : {resultat} Tonnes\n")
