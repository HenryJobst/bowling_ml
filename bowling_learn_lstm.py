from keras.models import Sequential
from keras.layers import LSTM, Bidirectional, Dense
from load_data import load_data

(XTrain, YTrain) = load_data('bowling_data_5000.csv')
(XTest, YTest) = load_data('bowling_data_3000.csv')
(XVal, YVal) = load_data('bowling_data_3000_val.csv')

# set up input dimension
data_dim = 1
timesteps = 22
num_classes = 1

# reshape our data to use in the model
XTrain = XTrain.reshape(5000, 21, 1)
YTrain = YTrain.reshape(5000, 1)

XTest = XTest.reshape(3000, 21, 1)
YTest = YTest.reshape(3000, 1)

XVal = XVal.reshape(3000, 21, 1)
YVal = YVal.reshape(3000, 1)

model = Sequential()
model.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=(timesteps, data_dim))))
model.add(Bidirectional(LSTM(32, return_sequences=True)))
model.add(Bidirectional(LSTM(32)))
model.add(Dense(1, activation='linear'))
model.compile(loss='logcosh', optimizer='adam')

# start training
model.fit(XTrain, YTrain,
          epochs=100, batch_size=1000,
          validation_data=(XVal, YVal))

ev = model.evaluate(XTest, YTest)
print(ev)

yP = model.predict(XTest)

for i in range(5):
    print("{}: {} Ist: {} <-> Soll: {}\n".format(i, XTest[i], yP[i], YTest[i]))
