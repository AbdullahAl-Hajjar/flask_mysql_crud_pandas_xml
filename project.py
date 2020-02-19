"""
https://github.com/raghavpatnecha/Excel-Flask
modified by : Abdullah Al-Hajjar
Student #: 040656012
"""

from flask import *
import pandas as pd
import os
import re
import lxml
import mysql.connector
# import MySQL Connector/Python 8.0.18 Oracle driver
from sqlalchemy import create_engine
# Import create_engine method from SQLAlchemy
conn = mysql.connector.connect(user='cst8333', password='cst8333',
                              host='127.0.0.1',
                              database='cheese')
# Create an object that connects to the MySQL database
engine = create_engine('mysql+mysqlconnector://cst8333:cst8333@localhost:3306/cheese', echo=False)
# Create an Engine object based on the URL for Object relational mapping
app = Flask(__name__)
print('Abdullah Al-Hajjar Student#: 040656012')
# Creating an object of the Flask web application framework

@app.route("/")
def show_tables():
    df = pd.read_csv('canadianCheeseDirectory.csv')
    # Read the CSV file
    df.to_sql(con=engine, name='canadiancheese', if_exists='replace', index=True)
    # Persist all data from the CSV to the database
    return render_template('index.html',tables=[re.sub(' table', '" id="example', df.to_html(classes='table'))], titles = ['Excel Data to Flask'])
    # Render the index.html

@app.route('/insert', methods= ['POST','GET'])
# Annotation for the insert url path
def insert():
    CheeseId = request.form['0']
    CheeseNameEn = request.form['1']
    CheeseNameFr = request.form['2']
    ManufacturerNameEn= request.form['3']
    ManufacturerNameFr = request.form['4']
    ManufacturerProvCode= request.form['5']
    ManufacturingTypeEn= request.form['6']
    ManufacturingTypeFr= request.form['7']
    WebSiteEn= request.form['8']
    WebSiteFr= request.form['9']
    FatContentPercent= request.form['10']
    MoisturePercent= request.form['11']
    ParticularitiesEn= request.form['12']
    ParticularitiesFr= request.form['13']
    FlavourEn= request.form['14']
    FlavourFr= request.form['15']
    CharacteristicsEn= request.form['16']
    CharacteristicsFr= request.form['17']
    RipeningEn= request.form['18']
    RipeningFr= request.form['19']
    Organic= request.form['20']
    CategoryTypeEn= request.form['21']
    CategoryTypeFr= request.form['22']
    MilkTypeEn= request.form['23']
    MilkTypeFr= request.form['24']
    MilkTreatmentTypeEn= request.form['25']
    MilkTreatmentTypeFr= request.form['26']
    RindTypeEn= request.form['27']
    RindTypeFr= request.form['28']
    LastUpdateDate= request.form['29']
    # Retreives all data inserted on the webpage by the user.

    df = pd.DataFrame({'CheeseId':[CheeseId],'CheeseNameEn': [CheeseNameEn], 'CheeseNameFr':[CheeseNameFr], 'ManufacturerNameEn':[ManufacturerNameEn],
                        'ManufacturerNameFr':[ManufacturerNameFr], 'ManufacturerProvCode':[ManufacturerProvCode],
                        'ManufacturingTypeEn': ManufacturingTypeEn, 'ManufacturingTypeFr':ManufacturingTypeFr, 'WebSiteEn':WebSiteEn, 'WebSiteFr':WebSiteFr,
                        'FatContentPercent':FatContentPercent, 'MoisturePercent':[MoisturePercent],'ParticularitiesEn': [ParticularitiesEn],
                        'ParticularitiesFr': [ParticularitiesFr],'FlavourEn': [FlavourEn], 'FlavourFr':[FlavourFr],'CharacteristicsEn': [CharacteristicsEn],
                        'CharacteristicsFr':[CharacteristicsFr], 'RipeningEn':[RipeningEn],
                         'RipeningFr':[RipeningFr], 'Organic':[Organic],'CategoryTypeEn': [CategoryTypeEn],
                         'CategoryTypeFr':[CategoryTypeFr], 'MilkTypeEn':[MilkTypeEn], 'MilkTypeFr':[MilkTypeFr],'MilkTreatmentTypeEn': [MilkTreatmentTypeEn],
                        'MilkTreatmentTypeFr':[MilkTreatmentTypeFr], 'RindTypeEn':[RindTypeEn],
                        'RindTypeFr': [RindTypeFr], 'LastUpdateDate':[LastUpdateDate]})
    # Store all the data into a pandas dataframe
    df2 = pd.read_csv('canadianCheeseDirectory.csv')
    # Create a pandas object with the current CSV file
    df2 = df2.append(df, sort=False, ignore_index=True)
    # Append all new data inserted by the user to the new pandas dataframe object
    df2.to_csv('canadianCheeseDirectory.csv', index=None, header=True, encoding='utf-8')
    # Overwrite new CSV to canadiancheeseDirectory
    return redirect('/')
    # Return to Root page and runs all Methods within that route

@app.route('/save', methods= ['POST','GET'])
# # Annotation for the save url path
def save():
    url = 'http://127.0.0.1:8050/'
    # Creat an object of local host and port url
    urll = request.get_data()
    # Create an object that retrieves the new data upon clicking the dave button
    data = pd.read_html(urll)
    # Creating a pandas object of that retrieved data
    data[0].drop('Unnamed: 0', axis=1).to_csv('canadianCheeseDirectory.csv', index=None, header=True, encoding='utf-8')
    # Removed the Unnamed column that was created upon request  and then Overwrites the CSV file
    return redirect('/')
    # Returns the Root and calls all functions within that path

@app.route('/results', methods= ['POST','GET'])
def  search():
    df3 = pd.DataFrame()
    url = 'http://127.0.0.1:8050/'
    # Creat an object of local host and port url
    urll = request.get_data()
    # Create an object that retrieves the new data upon clicking the dave button
    search_word = urll.decode("utf-8")
    # Creating a pandas object of that retrieved data
    words_array = search_word.split()
    df = pd.read_csv('canadianCheeseDirectory.csv')
    for w in words_array:
        for index, row in df.iterrows():
            if(str(row['CheeseNameEn']).startswith(w) or str(row['CheeseNameFr']).startswith(w) or str(row['ManufacturerNameEn']).startswith(w) or str(row['ManufacturerNameFr']).startswith(w) or str(row['ManufacturerProvCode']).startswith(w) or
                         str(row['ManufacturingTypeEn']).startswith(w) or str(row['ManufacturingTypeFr']).startswith(w)or str(row['WebSiteEn']).startswith(w) or str(row['WebSiteFr']).startswith(w) or str(row['FatContentPercent']).startswith(w) or
                         str(row['MoisturePercent']).startswith(w) or str(row['ParticularitiesEn']).startswith(w) or str(row['ParticularitiesFr']).startswith(w) or str(row['FlavourEn']).startswith(w) or str(row['FlavourFr']).startswith(w) or
                         str(row['CharacteristicsEn']).startswith(w) or str(row['CharacteristicsFr']).startswith(w) or str(row['RipeningEn']).startswith(w) or str(row['RipeningFr']).startswith(w) or str(row['Organic']).startswith(w) or str(row['CategoryTypeEn']).startswith(w) or
                         str(row['CategoryTypeFr']).startswith(w) or str(row['MilkTypeEn']).startswith(w) or str(row['MilkTypeFr']).startswith(w) or str(row['MilkTreatmentTypeEn']).startswith(w) or str(row['MilkTreatmentTypeFr']).startswith(w) or
                         str(row['RindTypeEn']).startswith(w) or str(row['RindTypeFr']).startswith(w) or str(row['LastUpdateDate']).startswith(w)):

                df2  = pd.DataFrame({'CheeseId':[row['CheeseId']],'CheeseNameEn': [row['CheeseNameEn']], 'CheeseNameFr':[row['CheeseNameFr']], 'ManufacturerNameEn':[row['ManufacturerNameEn'] ],
                            'ManufacturerNameFr':[row['ManufacturerNameFr']], 'ManufacturerProvCode':[row['ManufacturerProvCode']],
                            'ManufacturingTypeEn': [row['ManufacturingTypeEn']], 'ManufacturingTypeFr':[row['ManufacturingTypeFr'] ], 'WebSiteEn':[row['WebSiteEn']] , 'WebSiteFr':[row['WebSiteFr']],
                            'FatContentPercent':[row['FatContentPercent']] , 'MoisturePercent':[row['MoisturePercent']],'ParticularitiesEn': [row['ParticularitiesEn']],
                            'ParticularitiesFr': [row['ParticularitiesFr']],'FlavourEn': [row['FlavourEn']], 'FlavourFr':[row['FlavourFr']],'CharacteristicsEn': [row['CharacteristicsEn']],
                            'CharacteristicsFr':[row['CharacteristicsFr']], 'RipeningEn':[row['RipeningEn']],
                             'RipeningFr':[row['RipeningFr']], 'Organic':[row['Organic']],'CategoryTypeEn': [row['CategoryTypeEn']],
                             'CategoryTypeFr':[row['CategoryTypeFr']], 'MilkTypeEn':[row['MilkTypeEn']], 'MilkTypeFr':[row['MilkTypeFr']],'MilkTreatmentTypeEn': [row['MilkTreatmentTypeEn']],
                            'MilkTreatmentTypeFr':[row['MilkTreatmentTypeFr']], 'RindTypeEn':[row['RindTypeEn']],
                            'RindTypeFr': [row['RindTypeFr']], 'LastUpdateDate':[row['LastUpdateDate']]})
                df3 = df3.append(df2)
            df3.to_csv('test.csv', index=None, header=True, encoding='utf-8')

    return redirect('/')
    # Returns the Root and calls all functions within that path

if __name__ == "__main__":
    # Verifies that this program is not run by a child class o
    app.run(
        port=8050,
        host='127.0.0.1'
    )
    # Flask Object calls the run method with a specific localhost address and port number
