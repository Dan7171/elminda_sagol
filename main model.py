import pandas as pd
import numpy as np
import datetime as dt
import sklearn

clinical_data = pd.read_excel('files\BY_clinical_data_Sagol.xlsx')
eeg_data = pd.read_csv('files\zscores_Sagol.csv')
print(clinical_data.sample)
print(eeg_data.sample)