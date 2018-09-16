import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

dataframe = pd.read_csv('Amazon_Unlocked_Mobile.csv')

dataframe = dataframe.sample(frac=0.1,random_state=10)

dataframe.dropna(inplace=True)

dataframe = dataframe[dataframe['Rating']!=3]

dataframe['positive'] = np.where(dataframe['Rating']>3,1,0)

x_train,x_test,y_train,y_test=train_test_split(dataframe['Reviews'], dataframe['positive'], random_state=0)

vect=CountVectorizer().fit(x_train)

x_train_vectorized = vect.transform(x_train)

clf = LogisticRegression()
clf.fit(x_train_vectorized,y_train)

pickle.dump(clf, open("clf_model.pk", 'wb'))
