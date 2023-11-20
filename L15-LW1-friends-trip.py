me_and_my_friend       = {"Dorin", "Radjamhathaprajapatijaayeshkumar"}

my_friends             = {"John", "Marry", "Jane"}
my_best_friend_friends = {"Marry", "Pete", "Oliver", "Mia"}

people_to_exclude      = {"Pete", "Marry"}


########################################
trip_people_list = me_and_my_friend.union(
    my_friends,
    my_best_friend_friends
)

trip_people_list = trip_people_list.difference(people_to_exclude)

print(len(trip_people_list), "are going along")
print(trip_people_list)