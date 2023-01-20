def reta(x,y):
    x2y = 0
    xy  = 0
    x1   = 0
    y1   = 0
    x2  = 0
    m = len(x)
    for i in range(m):
        x2y += (x[i]**2)*y[i]
        xy  += x[i]*y[i]
        x1  += x[i]
        x2  += x[i]**2
        y1  += y[i]
        
    a0 = ( x2*y1 - (xy*x1))  / ((m*x2)-(x1**2))
    a1 = ((m*xy) - (x1*y1)) /  ((m*x2)-(x1**2))
    return a0,a1