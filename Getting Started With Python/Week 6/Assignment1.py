def computepay(h,r):
    if h <= 40.0:
    	return (h * r)
    else:
        return (40.0 * r) + (h - 40.0)*1.5*r

# Processing the input
hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter Rate:")
rate = float(rate)

# Done... Now, we must calculate the pay.
p = computepay(hrs, rate)
print("Pay",p)
