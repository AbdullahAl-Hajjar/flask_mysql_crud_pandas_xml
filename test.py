"""
    Written by Abdullah Al-Hajjar
    CST8333
    Student #040656012
"""

import unittest
import pandas as pd
class  test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        try:
            df3 = pd.DataFrame()
            df = pd.read_csv('canadianCheeseDirectory.csv')
            search_word = 'Bufflo Cow Creamy and fresh, this delicious locally-made cheese offers the traditional taste of Italy Pasteurized'
            words_array = search_word.split()
            for w in words_array:
                for index, row in df.iterrows():
                    if (str(row['CheeseNameEn']).startswith(w) or str(row['CheeseNameFr']).startswith(w) or str(
                            row['ManufacturerNameEn']).startswith(w) or str(row['ManufacturerNameFr']).startswith(
                            w) or str(row['ManufacturerProvCode']).startswith(w) or
                            str(row['ManufacturingTypeEn']).startswith(w) or str(row['ManufacturingTypeFr']).startswith(
                                w) or str(row['WebSiteEn']).startswith(w) or str(row['WebSiteFr']).startswith(w) or str(
                                row['FatContentPercent']).startswith(w) or
                            str(row['MoisturePercent']).startswith(w) or str(row['ParticularitiesEn']).startswith(
                                w) or str(row['ParticularitiesFr']).startswith(w) or str(row['FlavourEn']).startswith(
                                w) or str(row['FlavourFr']).startswith(w) or
                            str(row['CharacteristicsEn']).startswith(w) or str(row['CharacteristicsFr']).startswith(
                                w) or str(row['RipeningEn']).startswith(w) or str(row['RipeningFr']).startswith(
                                w) or str(row['Organic']).startswith(w) or str(row['CategoryTypeEn']).startswith(w) or
                            str(row['CategoryTypeFr']).startswith(w) or str(row['MilkTypeEn']).startswith(w) or str(
                                row['MilkTypeFr']).startswith(w) or str(row['MilkTreatmentTypeEn']).startswith(
                                w) or str(row['MilkTreatmentTypeFr']).startswith(w) or
                            str(row['RindTypeEn']).startswith(w) or str(row['RindTypeFr']).startswith(w) or str(
                                row['LastUpdateDate']).startswith(w)):
                        df2 = pd.DataFrame({'CheeseId': [row['CheeseId']], 'CheeseNameEn': [row['CheeseNameEn']],
                                            'CheeseNameFr': [row['CheeseNameFr']],
                                            'ManufacturerNameEn': [row['ManufacturerNameEn']],
                                            'ManufacturerNameFr': [row['ManufacturerNameFr']],
                                            'ManufacturerProvCode': [row['ManufacturerProvCode']],
                                            'ManufacturingTypeEn': [row['ManufacturingTypeEn']],
                                            'ManufacturingTypeFr': [row['ManufacturingTypeFr']],
                                            'WebSiteEn': [row['WebSiteEn']], 'WebSiteFr': [row['WebSiteFr']],
                                            'FatContentPercent': [row['FatContentPercent']],
                                            'MoisturePercent': [row['MoisturePercent']],
                                            'ParticularitiesEn': [row['ParticularitiesEn']],
                                            'ParticularitiesFr': [row['ParticularitiesFr']],
                                            'FlavourEn': [row['FlavourEn']], 'FlavourFr': [row['FlavourFr']],
                                            'CharacteristicsEn': [row['CharacteristicsEn']],
                                            'CharacteristicsFr': [row['CharacteristicsFr']],
                                            'RipeningEn': [row['RipeningEn']],
                                            'RipeningFr': [row['RipeningFr']], 'Organic': [row['Organic']],
                                            'CategoryTypeEn': [row['CategoryTypeEn']],
                                            'CategoryTypeFr': [row['CategoryTypeFr']],
                                            'MilkTypeEn': [row['MilkTypeEn']], 'MilkTypeFr': [row['MilkTypeFr']],
                                            'MilkTreatmentTypeEn': [row['MilkTreatmentTypeEn']],
                                            'MilkTreatmentTypeFr': [row['MilkTreatmentTypeFr']],
                                            'RindTypeEn': [row['RindTypeEn']],
                                            'RindTypeFr': [row['RindTypeFr']],
                                            'LastUpdateDate': [row['LastUpdateDate']]})
                        df3 = df3.append(df2)
        except IOError:
            print('Cannot Uploadfile')
            # print(df3)
        self.data = str(df3)
# Setup the testing by creating a connection to the database and retrieving a record

    def  test(self):
        print('Abdullah Al-Hajjar Student number : 040656012')
        record = "1944,Mozzarina di Bufala,Mozzarina di Bufala,Saputo,Saputo,QC,Industrial,Industrielle,http://www.saputo.com/?langType=4105,http://www.saputo.com/?langType=3084,19.0,64.0,Made from 100% pasteurised buffalo milk and is rich in calcium, and low in sodium and cholesterol.,Faite Ã 100 % de lait de bufflonne frais, est riche en calcium et faible en sodium et en cholestÃ©rol. Savourez l'Italie grÃ¢ce au goÃ»t frais et crÃ©meux de ce somptueux fromage d'ici,Creamy and fresh, this delicious locally-made cheese offers the traditional taste of Italy.,Savourez l'Italie grÃ¢ce au goÃ»t frais et crÃ©meux de ce somptueux fromage.,,,0,Fresh Cheese,PÃ¢te fraÃ®che,Buffalo Cow,Bufflonne,Pasteurized,PasteurisÃ©,No Rind,Sans croÃ»te,2016-02-03"
        self.assertEqual(self.data, record)
# Comparing the expectation of  the record with the actual retrieved object from the database