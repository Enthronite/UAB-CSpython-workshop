try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception:
    print ("Unknown error occurred")

print ("We can run after an error!")
