#Pizza's size X
x = [6, 8, 12, 14, 18] 
#Pizza's prices  
y = [350, 775, 1150,1395,1675]
m, b = 0,0
alpha = 0.01 
iterations = 10000
n = len(x)

for _ in range(iterations):
    gd_m = 0
    gd_b = 0 
    cost = 0
    for i in range(n):
        pred_y = m * x[i] + b 
        errors = y[i] - pred_y
        cost += (errors) ** 2 
        gd_m +=(-1/n) * x[i] * errors
        
        gd_b += (-1/n) * errors
        
    m = m - alpha * gd_m
    b = b - alpha * gd_b
    cost = cost / (2*n)
print(f"Cost {cost}")    
size = 17
pred_y = m * size + b
print(round(pred_y))
