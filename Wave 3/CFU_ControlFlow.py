#Question: What type of loop should we use? For Loop
#For Loop

#You need to write a loop that takes the numbers in a given list named num_list:
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

#Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.

#Would you use a while or a for loop to write this code? For Loop


## Please use this space to test and run your code
count = 0
sum_num = 0
for num in num_list :
    if count == 5:
        break
    if num != 1 and num % 2 != 0 :
        sum_num += num
        count += 1
print (count)
print (sum_num)

