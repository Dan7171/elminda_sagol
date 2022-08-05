import pandas as pd
import numpy as np
import datetime as dt
import sklearn

clinical_data = pd.read_excel('files\BY_clinical_data_Sagol.xlsx')
eeg_data = pd.read_csv('files\zscores_Sagol.csv')
#print(clinical_data.sample)
#print(eeg_data.sample)

reformat_dates(clinical_data) #implement 
reformat_dates(eeg_data) # implement
unite_same_day_visits_to_the_first(clinical_data) #implement 
unite_same_day_visits_to_the_first(eeg_data)#implement 

visits = clinical_data.merge(eeg_data, how = 'outer', on = ['date', 'subject']) #outer or inner? check it
unite_close_visits_to_one(visits) #implement


def reformat_dates(db): #from any date string to one format with date only- ("2.3.2020 12:25:59" -> "2\3\2020")
    #use strptime() to convert the input string to date object and than back to string in the desired format
    pass
def unite_same_day_visits_to_the_first(db): # deleting from data visists of a subject who visited more than once in a day, and leaving just the first visit
    pass

def unite_close_visits_to_one(db):# uniting to a single visit, visits that that the time between them is less than 't' 
#for cases that eeg record is and clinic visit are very close in time- at most t days.
    pass 