me_and_my_friend       = {"Dorin", "Radjamhathaprajapatijaayeshkumar"}

my_friends             = ["John", "Marry", "Jane"]
my_best_friend_friends = ("Marry", "Pete", "Oliver", "Mia")

# people_to_exclude      = {"Nobody"}
people_to_exclude      = set()
exlude_count           = 0

from os import system
########################################
print("Don't wanna go? Enter your name below")
while True:
    exlude_count += 1
    exclude_name = input(str(exlude_count) + ") >> ")
#    people_to_exclude.discard("Nobody")
    people_to_exclude.add(exclude_name)
    if exclude_name == "":
        break
system('cls')

########################################
trip_people_list = me_and_my_friend.union(
    my_friends,
    my_best_friend_friends
)

trip_people_list = trip_people_list.difference(people_to_exclude)
trip_people_list = list(trip_people_list)

print(len(trip_people_list), "are going along:")

# HW1: 

# 6 are going along:
# 1. Jane
# 2. Dorin
# 3. Radj
# ....
# HW2*: 
#    enter the manes of people to exlude from the keyboard

print()
for participant in range(len(trip_people_list)):
    print(participant+1,") ", trip_people_list[participant])

print()
print(len(people_to_exclude)-1, "won't go:")
for name in people_to_exclude:
    print(name)