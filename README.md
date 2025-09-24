# Simple Machine Learning Model: Inches to Centimeters

## Overview
This project demonstrates a simple neural network with **1 neuron** that learns a **linear relationship** between inches and centimeters (`cm = inches × 2.54`).  
It is designed as a beginner-friendly exercise to show how even a single neuron can approximate a mathematical formula using TensorFlow/Keras.

## Project Structure
- `MLModel.py` - Python script defining and training the neural network.
- `README.md` - Project overview and instructions.


## Features
- Generates a dataset of inches and their corresponding centimeter values.
- Defines a **1-neuron neural network**.
- Trains the model on the dataset.
- Tests the model with new inputs.
- Visualizes the predicted vs actual values.

## Installation
1. Install required packages:
   ```bash
   pip install tensorflow numpy matplotlib
   ```
2. Run the Python script:
   ```bash
   python MLModel.py
   ```
3. Check predictions for sample inputs and view the plot.

## Results
The model accurately predicts centimeters from inches after training. The red line in the plot shows the network's predictions against the actual data points.
