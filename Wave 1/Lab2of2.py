#1. What is the length of the string variable verse?
#2. What is the index of the first occurrence of the word 'and' in verse?
#3. What is the index of the last occurrence of the word 'you' in verse?
#4. What is the count of occurrences of the word 'you' in the verse?


verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
length_of_verse = len(verse)
print ('The length of verse is {}'.format(length_of_verse))

index_of_and = verse.find('and')
print ("The index of the first occurence of the word 'and' is {}".format(index_of_and) )

index_of_you = verse.rfind('you')
print ("The index of the last occurence of the word 'you' is {}".format(index_of_you) )


occurence = verse.count('you')
print ("The occurence of the word 'you' is {}".format(occurence))
# Bonus: practice using .format() to output your answers in descriptive messages!