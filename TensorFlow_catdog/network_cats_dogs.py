import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D, GlobalAveragePooling2D
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time



x = pickle.load(open('x.pickle','rb'))
y = pickle.load(open('y.pickle','rb'))
x = x/255.0


model = tf.keras.models.Sequential()

model.add(Conv2D(16,(5,5), input_shape = x.shape[1:], activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(25,(5,5), input_shape = x.shape[1:], activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(36,(5,5), input_shape = x.shape[1:], activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(49,(5,5), input_shape = x.shape[1:], activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(GlobalAveragePooling2D())
model.add(Dropout(0.5))


model.add(Dense(1, activation = 'sigmoid'))

model.compile(loss='binary_crossentropy',optimizer = 'adam', metrics = ['accuracy'])

model.summary()

model.fit(x, y, batch_size = 32, epochs = 30, validation_split = 0.3)

model.save('catdog_89.model')