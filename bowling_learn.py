import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from load_data import load_data

(XTrain, YTrain) = load_data('bowling_data_5000.csv')
(XTest, YTest) = load_data('bowling_data_3000.csv')

model = Sequential()
model.add(Dense(21, input_dim=21, kernel_initializer='normal', activation='relu'))
model.add(Dense(21, kernel_initializer='normal', activation='relu'))
model.add(Dense(10, kernel_initializer='normal', activation='sigmoid'))
model.add(Dense(10, kernel_initializer='random_uniform', activation='relu'))
model.add(Dense(1, kernel_initializer='normal', activation='linear'))
model.compile(loss='logcosh', optimizer='adam')

print(XTrain)
print(YTrain)

model.fit(XTrain, YTrain, epochs=500, verbose=True)

ev = model.evaluate(XTest, YTest)
print(ev)

yP = model.predict(XTest)

for i in range(5):
    print("{}: {} Ist: {} <-> Soll: {}\n".format(i, XTest[i], yP[i], YTest[i]))


