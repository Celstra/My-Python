#Input a point value based on a chart of prizes
#   Points	         Prize
#   1 - 50	         wooden rabbit
#   51 - 150         no prize
#   151 - 180      	 wafer-thin mint
#   181 - 200	     penguin

points = 174 
#List of current prizes
prize = ["wooden rabbit", "no prize", "wafer-thin mint", "penguin"]

# write your if statement here
if points <= 50:
    result = ("Congratulations! You won a " + prize[0])
elif points <= 150:
    result = ("Oh dear, " + prize[1] + " this time.")
elif points <= 180:
    result = ("Congratulations! You won a " + prize[2])
else:
    result = ("Congratulations! You won a " + prize[3])

print(result)
