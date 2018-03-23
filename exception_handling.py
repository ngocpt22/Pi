def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'Divide to zero is not allowed'

print(divide(1,0))