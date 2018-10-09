#Input a point value based on a chart of prizes
#   Points	         Prize
#   1 - 50	         wooden rabbit
#   51 - 150         no prize
#   151 - 180      	 wafer-thin mint
#   181 - 200	     penguin

points = 174

# establish the default prize value to None
prize = None

# use the points value to assign prizes to the correct prize names
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 180:
    prize = "penguin"

# use the truth value of prize to assign result to the correct prize
if prize:
    result = "Congratualtions! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)
