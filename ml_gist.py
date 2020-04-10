import numpy as np
from sklearn.model_selection import train_test_split

X = np.random.random((1000, 5))
Y = np.random.random((1000, 1))
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

#################################################
#################################################

import numpy as np
from sklearn.model_selection import StratifiedKFold

X = np.random.random((1000, 5))
Y = np.concatenate([np.ones((800, 1)), np.zeros((200, 1))], axis=0)
skf = StratifiedKFold(n_splits=10)
train_inds, test_inds = list(skf.split(X, Y))[0]
X_train, X_test = X[train_inds], X[test_inds]
Y_train, Y_test = Y[train_inds], Y[test_inds]

#################################################
#################################################

from keras.preprocessing.text import text_to_word_sequence

text = 'Hello world!'
tokens = text_to_word_sequence(text)

#################################################
#################################################

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split

model = Sequential()
model.add(Dense(8, input_dim=5 , activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

X = np.random.random((1000, 5)) - 0.5
Y = np.all(X[:, [1, 3]] > 0, axis=1).astype(float)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

model.fit(X_train, Y_train, batch_size=32, epochs=500, validation_data=(X_test, Y_test))

