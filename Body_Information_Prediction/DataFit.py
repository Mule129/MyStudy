import numpy as np
import pandas as pd
from keras import Sequential, layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer
import tensorflow as tf
import matplotlib.pyplot as plt

with open(r"practicePJ\20221122_ss_PJ\육군 신체측정정보.csv", "r", ) as file:
    data = pd.read_csv(file)
    #print(data)
train_data = data.to_numpy()
x_data, y_data = [], []
for i in train_data:
    x_data.append(i[:7])
    y_data.append(i[7])
train_data = np.array(x_data)
test_data = np.array(y_data)
print(train_data.shape, test_data.shape)

nmr = Normalizer().fit(x_data)
t = nmr.transform(x_data)
x_data = t

train_x, test_x, train_y, test_y = train_test_split(train_data, test_data, random_state=1)
#print(test_y)

model = Sequential()
model.add(layers.Input(7))
model.add(layers.Flatten())
#model.add(layers.Dense(256, activation="relu"))
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(32, activation="relu"))
model.add(layers.Dense(16, activation="relu"))
model.add(layers.Dense(4, activation="relu"))
model.add(layers.Dense(1, activation="relu"))

model.summary()

model.compile(optimizer='RMSprop',loss='mae')
model.fit(train_x, train_y, epochs=20, batch_size=128)

data = model.predict(test_x)
print(data)
print(test_x)

model.save(r"practicePJ\20221122_ss_PJ\save_model\model_1.h5")
#history = model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_squared_error'])

"""W = tf.Variable(tf.random.normal([1]), name="weight")
b = tf.Variable(tf.random.normal([1]), name="bias")
 
hypothesis=train_x*W+b
 
cost = tf.reduce_mean(tf.square(hypothesis - train_y))
sgd = tf.keras.optimizers.SGD(learning_rate=0.01)
 
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(1, input_dim = 8))
 
model.compile(loss='mean_squared_error',optimizer=sgd)
 
model.fit(train_x,train_y,epochs=10)
 """