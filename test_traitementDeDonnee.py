import unittest
import traitementDeDonnee as traitementDeDonnee
# Chemin du fichier client
pathOfClientFile="/Users/kenore/Data/formation/dev-python/client.txt"
# Le nombre de donnée par enregistrement
dataNumberForEachLin=4
# Le nom du fichier client
fileName = "client.txt"
class TestTraitementDonnee(unittest.TestCase):
    #  Test qui permet de valider le nom du fichier
    def test_get_file_name(self):
        self.assertEqual(traitementDeDonnee.get_file_name(pathOfClientFile),fileName)
    #  Test qui permet de vérifier si le fichier existe
    def test_isExisteFile(self):
        self.assertTrue(traitementDeDonnee.isExisteFile(pathOfClientFile))
    #  Test qui permet de vérifier si le fichier est vide
    def test_isEmptyFile(self):
        self.assertTrue(traitementDeDonnee.isEmptyFile(pathOfClientFile))
    #  Test qui permet de vérifier le nombre de donnée par ligne
    def test_checkDataNumberForEachLine(self):
        self.assertNotEqual(traitementDeDonnee.checkDataNumberForEachLine(pathOfClientFile),dataNumberForEachLin)

if __name__ == '__main__':
    unittest.main()
