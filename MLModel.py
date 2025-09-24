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

# Defines the model with 1 neuron
model = Sequential([Dense(units=1, input_shape=[1])])

# Compiles the model with optimizer and loss function
model.compile(
    optimizer='adam',               # Adam optimizer efficient for small datasets
    loss='mean_squared_error'       # Loss suitable for regression problems
)

# Trains the model on the dataset
history = model.fit(
    inches,                # Input
    cm,                    # Output
    epochs=500,            # Number of times the model sees the entire dataset
    batch_size=10,         # Number of samples per gradient update
    verbose=1              # Shows progress bar during training
)

# Tests the trained model with new sample inputs
test_inches = np.array([[5], [10], [25]])   # Example values to predict
predicted_cm = model.predict(test_inches)

# Prints predicted centimeter values for each test input
for i, inch in enumerate(test_inches):
    print(f"{inch[0]} inches -> {predicted_cm[i][0]:.2f} cm")