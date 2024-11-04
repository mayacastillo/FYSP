import pandas as pd
import os


directory = 'C:/Users/corgionmymind/Downloads/OASIS3_data_files/UDSd2-Form_D2/resources/csv/files'

dataframes = []

for filename in os.listdir(directory):

    if filename.endswith('.csv'):
        df = pd. read_csv(os.path.join(directory, filename))
        dataframes.append (df)

clinical_data = pd.concat (dataframes, ignore_index=True)

demographic_data = pd. read_csv('path/to/demographic_file.csv') # need to change this to demographic file path

final_data = pd.merge(clinical_data, demographic_data, on='id', how='left')

final_data.to_csv('combined_data.csv', index=False)

print (final_data.head ())
