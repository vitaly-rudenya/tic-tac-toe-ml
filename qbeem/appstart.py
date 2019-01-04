from keras.models import Sequential
from keras.layers import *
from qbeem.games import TicTacToe
from keras.optimizers import *
from qbeem.agent import Agent

from keras import backend as K
K.set_image_dim_ordering('th')

grid_size = 3
nb_frames = 4
nb_actions = 9

model = Sequential()
model.add(Conv2D(16, (3, 3), padding='same', activation='relu', input_shape=(nb_frames, grid_size, grid_size)))
#model.add(Conv2D(32, (1, 1), activation='relu'))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(nb_actions))
model.compile(RMSprop(), 'MSE')

snake = TicTacToe()

agent = Agent(model=model, memory_size=-1, nb_frames=nb_frames)
agent.train(snake, batch_size=64, nb_epoch=10000, gamma=0.8)
agent.play(snake)