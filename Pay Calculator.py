# simplified pay calculator

hrs = input("Enter Hours:")
rate = input("Rate Per Hour:")

try:
    f_hrs = float(hrs)
    f_rate = float(rate)
except:
    print('Error, please enter numerical value')
    quit()

def computepay(f_hrs,f_rate):
    if f_hrs <= 40:
        pay = f_hrs * f_rate
        return pay
    elif f_hrs > 40:
        pay = (40 * f_rate) + (f_hrs - 40) * (f_rate * 1.5)
        return pay

p = computepay(f_hrs, f_rate)

print("Pay", p)
