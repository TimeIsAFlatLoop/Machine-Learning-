import numpy as np 

# Dataset: Features - [size in sq ft, number of rooms]
X = np.array([
    [800,2],
    [1000,3],
    [1200,2],
    [1500,4],
    [1800,4]
])

# Feature Scaling: Normalize X by dividing each column by its max value
# Formula used: X_scaled = X / max(X, axis=0)
X = X / np.max(X, axis=0)

# Target values: Prices in thousands
Y = np.array([150,200,210,290,310])

# Initialize weights to 0 for two features
w = np.array([0.0,0.0])

m = len(Y)  # number of training examples
alpha = 0.01  # learning rate
iteration = 1000  # number of iterations for gradient descent

# Gradient Descent Loop
for i in range(iteration):
    # Prediction formula (hypothesis): h(w) = X · w
    pred = np.dot(X, w)
    
    # Error: difference between predicted and actual values
    error = pred - Y 
    
    # Gradient of the cost function (vectorized): (1/m) * X.T · error
    gradients = (1/m) * np.dot(X.T, error)
    
    # Cost function (Mean Squared Error): (1/(2m)) * sum((h(w) - Y)^2)
    cost = (1/(2*m)) * np.sum(error ** 2)
    
    # Update rule for weights: w = w - α * gradient
    w = w - alpha * gradients 
    
    # Print progress every 100 iterations
    if i % 100 == 0:
        print(f"Iteration {i} and prediction {pred} and cost {cost:.4f} and weight {w}")
    

# Predicting a new house price
new_house = np.array([1900, 5])  

# Scale new input using the same max values used in training
max_value = np.array([1800, 4])
scaled = new_house / max_value

# Predict using the trained model
# Formula: h(w) = scaled_input · w
pred = np.dot(scaled, w)

print(f"For new house {pred:.4f}")
