import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import os
def layers(model):
    model.add(Dense(units = 480,input_shape=(11,),activation='relu'))
    model.add(Dense(units = 240,activation='relu'))
    model.add(Dense(units = 120,activation='relu'))
    model.add(Dense(units = 60,activation='relu'))
    model.add(Dense(units = 30,activation='relu'))
    model.add(Dense(units = 15,activation='relu'))
    model.add(Dense(units = 4,activation='relu'))
    return model

ds  = pd.read_csv("wine.csv")
X = ds[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol']]
y = ds['quality']
y=pd.get_dummies(y,drop_first=True)
#0=bad
#1=good
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.1,random_state=20)
model = Sequential()
model = layers(model)
model.add(Dense(units = 1,activation='sigmoid'))
model.compile(loss='binary_crossentropy' ,optimizer=Adam(learning_rate=0.00001))
model.fit(x_train,y_train, validation_data=( x_test,y_test), epochs=100, verbose=0)
import numpy as np
yhat = (model.predict([x_test]))
yhat = np.round(yhat)
y_test = y_test.to_numpy()
count = 0
n = 0
total = len(yhat)
while n < total:
    if y_test[n] == yhat[n]:
        count = count + 1
    n = n+1
accuracy = (count*100)/total
print(accuracy)
model.save("final.h5")
os.system("echo {} > a.txt".format(accuracy))	
