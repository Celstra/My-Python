start_num = 5#provide some start number
end_num = 100#provide some end number that you stop when you hit
count_by = 1#provide some number to count by

# write a condition to check that end_num is larger than start_num before looping
if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."
# write a while loop that uses break_num as the ongoing number to
#   check against end_num
else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by
    result = break_num

print(result)
