import math 

x = [1,2,3,4,5]
y = [0,0,0,1,1]
m,b = 0.1,0.1
n = len(x)
alpha = 0.001
iterations = 1000

for _ in range(iterations):
    cross_entropy = 0
    gd_m,gd_b = 0,0
    
    for i in range(n):
        z = m * x[i] + b 
        predY = 1 / (1 + math.exp(-z))
        predY = max(min(predY, 1 - 1e-15), 1e-15)  # Add this line
        error = predY - y[i]
        cross_entropy += - (y[i] * math.log(predY) + (1 - y[i]) * math.log(1 - predY)) / n
        gd_m += (-1/n) * x[i] * error
        gd_b += (-1/n) * error
        
    m -= alpha * gd_m
    b -= alpha * gd_b
        
print(f"prediction {predY}")
print(f"Cost {cross_entropy}")
print(f"weight is {m:.2f} and bias {b:.2f}")
        
study_hour = 32 
z = m * study_hour + b 
pred = 1 / (1 + math.exp(-z))
print(f"Nigga got {pred} chances to pass")      
