import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

# Generates the data (in -> cm)
inches = np.linspace(0, 100, 100)           # Creates 100 numbers (0 - 100)
cm = inches * 2.54                                          # Converts inches to centimeters

# Shapes data for Keras (samples, features)
inches = inches.reshape(-1, 1)
cm = cm.reshape(-1, 1)