cube = lambda x: x**3

def fibonacci(n):
    l = [0,1]
    for i in range(2,n):
         l.append(l[i-2] + l[i-1])
    return(l[0:n])
