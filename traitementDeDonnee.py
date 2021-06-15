import sys
import os
# Le chemin du fichier client
pathOfClientFile="/Users/kenore/Data/formation/dev-python/client.txt"
# Le separateur des données clients
separator=","
# Le nombre de donnée par enregistrement
dataNumberForEachLin=4
# Fonction qui permet de récupérer le nom du fichier 
#   -Paramètre d'entrée : le chemin du fichier
#   -Donnée retour      : le nom du fichier
def get_file_name(filePath) :
    fileName = os.path.basename(filePath)
    print("le nom du fichier :",fileName)
    return fileName
# Fonction qui permet de vérifier si le  fichier existe
#   -Paramètre d'entrée : le chemin du fichier
#   -Donnée retour      :  True si le fichier existe si non False
def isExisteFile(filePath) :
    exist = False
    if os.path.exists(filePath) :
        exist = True
    print (" le fichier est présent ",exist)
    return exist
# Fonction qui permet de vérifier si le  fichier est vide
#   -Paramètre d'entrée : le chemin du fichier
#   -Donnée retour      :  True si le fichier existe si non False
def isEmptyFile(filePath) :
    isEmpty = False
    if os.path.getsize(filePath) > 0 :
        isEmpty=True
    print("taille du fichier:",isEmpty)
    return isEmpty
# Fonction qui permet de vérifier le nombre de donnée par ligne
#   -Paramètre d'entrée : le chemin du fichier
#   -Donnée retour      :  True si le fichier existe si non False
def checkDataNumberForEachLine(filePath) : 
    checkDataNumber = True
    with open (filePath, 'r') as filin :
        lignes = filin.readlines ()
        for ligne in lignes :
            datas = ligne.split(separator)
            if len(datas) < dataNumberForEachLin : 
                print(datas)
                checkDataNumber = False
                return checkDataNumber
                
if __name__ == '__main__':    
    isExisteFile(pathOfClientFile)
    get_file_name(pathOfClientFile)
    isEmptyFile(pathOfClientFile)
    print(checkDataNumberForEachLine(pathOfClientFile))
