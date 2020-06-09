hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

if h <= 40.0:
    pay = h * r
else:
    pay = 40.0 * r + ((h - 40.0) * 1.5 * r)
print(pay)
