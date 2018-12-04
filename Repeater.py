repeater = None
data = []
count = 0
sum = 0

while True:
    if repeater is not "done":
        repeater = input("Enter a number: ")
        try:
            if repeater == "done":
                break
            repeater = int(repeater)
            #begins to add the number in data set together
            sum += repeater
            #adds inputs to the data set
            data.append(repeater)
            #counts number in data set
            count = count + 1
        except:
            print ('Invalid input')

average = (sum / count)
print ("Sum: " + str(sum), "Count: " + str(count), "Average: " + str(average))
