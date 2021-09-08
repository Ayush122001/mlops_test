import pandas as pd
from sklearn.model_selection import train_test_split
import os
ds = pd.read_csv('wine.csv')
y = pd.get_dummies(ds['quality'],drop_first=True)
y_final = y.values
X = ds[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol']]
X_final = X.values
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
def model_fucn(hp):
    hp_units = hp.Int('units', min_value=32, max_value=512, step=32)
    hp_learning_rate = hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])
    model = Sequential()
    model.add(Dense(units=hp_units,activation='relu',input_shape=(11,)))
    model.add(Dense(units=hp_units,activation='relu'))
    model.add(Dense(units=1,activation='sigmoid'))
    model.compile(optimizer=Adam(learning_rate=hp_learning_rate),loss='binary_crossentropy',metrics=['accuracy'])
    return model
import keras_tuner as kt
# model_fucn = from where model can be created
# objective = what we want to optimized
# max_epochs = for deciding initial models

tuner = kt.Hyperband(
    hypermodel = model_fucn,
    objective = 'val_accuracy',
    max_epochs = 20)
X_train, X_test, y_train, y_test = train_test_split(X_final, y_final, test_size=0.33, random_state=42)
from tensorflow.keras.callbacks import EarlyStopping
# monitor = what to do
# patient = no. of epoch with no improvement 
stop_early = EarlyStopping(monitor='val_loss', patience=3)
tuner.search(X_train, y_train, epochs=10, validation_split=0.2, callbacks=[stop_early])
#tuner.search(X_train, y_train, epochs=50, validation_split=0.2)
best_hps=tuner.get_best_hyperparameters(num_trials=1)[0]
model = tuner.hypermodel.build(best_hps)
model.fit(X_train, y_train, epochs=50)
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
