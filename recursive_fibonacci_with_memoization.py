watermelon={0:0,1:1,2:1}

def fibonacci(n):
    if n in watermelon:
        return watermelon[n]
    else:
        watermelon[n] = fibonacci(n-1)+fibonacci(n-2)
        return watermelon[n]
        
print(fibonacci(50))
