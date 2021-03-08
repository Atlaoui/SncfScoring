import pandas as pd

base_gares = pd.read_csv('Data/base_gares.csv',sep = ';')
sncf_adresse = pd.read_csv('Data/data_sncf/sncf-gares-et-arrets-transilien-ile-de-france.csv',sep = ';')
sncf_equipements = pd.read_csv('Data/data_sncf/sncf-accessibilite-des-gares-equipements.csv',sep = ';')
sncf_arret = pd.read_csv('Data/data_sncf/lignes_points_arret.csv', sep = ';')

#print(type(sncf_equipements))
#print(sncf_equipements.columns)
#print(sncf_equipements.shape)
#print(sncf_equipements.head(7))
#print(sncf_equipements.tail(8))


#print(sncf_equipements.info())
#print(sncf_equipements.dtypes)
#print(base_gares.describe)
#print(sncf_adresse.describe)
#print(sncf_equipements.describe)
#print(sncf_arret.describe)

#print(sncf_adresse.iloc[3])

#print(sncf_adresse.loc[3])

# Selectionner la colonne 'gare' en utilisant iloc a revoire 
#print(sncf_equipements.iloc[:,1])

# Selectionner la colonne 'gare' en utilisant loc


# Selectionner la 3ème et la 10ème ligne 
# et les colonnes 'gare' et 'ascenceurs' avec iloc

print(sncf_equipements.iloc[1, 8])
