import numpy as np

print('')
print('Use the code "a = np.array([[14,365],[25,99]])"')
print('Then type "Python(a)"')

def Python(a):
    for n in range(len(a)):
        
        b = np.polyfit(a[:,0], a[:,1],n)
        c = np.polyval(b, a[:,0])
        d = np.linalg.norm(a[:,1] - c)
        e = [n,d]
        
        if n==0:
            
            f = e
            
        elif f[1] >= e[1]:
            
            g = e[0]
            
    d = np.polyfit(a[:,0],a[:,1],g)
    
    print('Coefficients:',d)
    