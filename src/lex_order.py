def order(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] > b[i]:
            return True
        if a[i] < b[i]:
            return False
            
    return len(a) >= len(b)

a = input()
b = input()
print(order(a, b))