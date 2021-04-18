import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import L1.py

ds  = pd.read_csv("wine.csv")
X = ds[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol']]
y = ds['quality']
model = Sequential()
model = L1.layers(model)
model.add(Dense(units = 1,activation='sigmoid'))
model.compile(loss='binary_crossentropy' ,optimizer=Adam(learning_rate=0.00001))
model.fit(x_train,y_train, validation_data=(x_test,y_test), epochs=10, verbose=0)
accuracy = model.evaluate(x_test, y_test, verbose=0)
accuracy = accuracy*100
model.save("final.h5")
os.system("echo 'accuracy' > a.txt")	
	