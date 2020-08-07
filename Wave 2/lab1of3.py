# Use this playground to experiment with list methods, using Test Run

play_list = [1,2,3,4,5]
set_list = set(play_list)

play_list.append(7)
print (play_list)

play_list.pop()
print (play_list)

play_list.sort(reverse = True)
print(play_list)

new_list = ['sun','moon']
print (play_list + new_list)

print ('@'.join(new_list))