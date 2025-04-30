#Pizza's size X
x = [0.6, 0.8, 0.12, 0.14, 0.18] 
#Pizza's prices  
y = [350, 775, 1150,1395,1675]
m, b = 0.0,0.0
alpha = 0.1 
iterations = 100
n = len(x)

for _ in range(iterations):
    gd_m = 0.0
    gd_b = 0.0 
    
    for i in range(n):
        pred_y = m * x[i] + b 
        errors = y[i] - pred_y
        
        gd_m +=(-1/n) * x[i] * errors
        
        gd_b += (-1/n) * errors
        
        m = m - alpha * gd_m
        b = m - alpha * gd_b
        
size = 17/10 
pred_y = m * size + b
print(round(pred_y))
