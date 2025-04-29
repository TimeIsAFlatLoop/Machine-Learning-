x = 0.6 
y = 0.14 
m = 0 
b = 0
alpha = 0.1 

iteration = 100

for i in range(iteration):
    pred_y = m * x + b  
    error = y - pred_y 
    loss = error ** 2 
    
    gradient_m = -2 * x * error
    gradient_b = -2 * error 
    
    m = m - alpha * gradient_m
    b = m - alpha * gradient_b 
    
    print(f"Iteration {i+1}")
    print(f"Predict Y {pred_y:.2f}")
    
    print(f"Loss {loss:.2f}")
    
    print(f"gradient m {gradient_m:.2f}")
    
    print(f"gradient b {gradient_b:.2f}")
    print(f"updated m {m:.2f}")
    
    print(f"updated b {b:.2f}")
    
    
    
    
    
    
