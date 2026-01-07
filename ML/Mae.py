import numpy as np

x = np.array([2, 3, 4, 5, 6])
y = np.array([5, 6, 7, 9, 13])

m = 0.0
c = 0.0
alpha = 0.001
k= 50
n = len(x)

for i in range(k):
    y_pred = m * x + c
    error  = y - y_pred   
    
    mae = (1/n) * np.sum(np.abs(error))   

    dm = (-1/n) * np.sum(x * np.sign(error))   
    dc = (-1/n) * np.sum(np.sign(error))       

    m = m - alpha * dm
    c = c - alpha * dc

    print(f"Iteration {i+1}")
    print(f"  y_pred   = {y_pred}")
    print(f"  error    = {error}")
    print(f"  dm       = {dm:.4f}, dc = {dc:.4f}")
    print(f"  m        = {m:.4f}, c = {c:.4f}")
    print(f"  MAE      = {mae:.4f}")
    print("G"*40)
