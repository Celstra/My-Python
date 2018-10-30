score = input("Enter Score: ")

try:
    f_score = float(score)
except:
    print('Invalid Score: Your score must be between 0.0 and 1.0')
    quit()

if f_score >= 0.9 and f_score <= 1.0:
    print('A')
elif f_score >= 0.8 and f_score < 0.9:
    print('B')
elif f_score >= 0.7 and f_score < 0.8:
    print('C')
elif f_score >= 0.6 and f_score < 0.7:
    print('D')
elif f_score < 0.6 and f_score > 0:
    print('F')
else:
    print('Invalid Score: Your score must be between 0.0 and 1.0')
    quit()
