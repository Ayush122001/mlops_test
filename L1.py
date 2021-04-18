import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

def layers(model):
    model.add(Dense(units = 100,input_shape=(11,),activation='relu'))
    model.add(Dense(units = 4,activation='relu'))
    return model