users_list = ["angel","eduardo","mike","admin","javier"]

current_user = input("who r u?\n")
#users_list = []
if users_list:
	if current_user == "admin":
		print("Hello admin, would u like to see a status report?")
	else:
		print(f"Hello {current_user.title()}, thank you for being here again") 
else:
	print("fist we need to get some users!")



#-----------------------------------------------------------------------------

new_users_list = ["philip", "Mike", "Donald", "Duke"]

new_users_list_copy = []
for user in new_users_list:
	new_users_list_copy.append(user.lower())

for user in new_users_list_copy:
	if (user in users_list):
		print(f"Sorry, but {new_users_list[new_users_list_copy.index(user)]} have already been used")
	else:
		print(f"U can use {new_users_list[new_users_list_copy.index(user)]}, is nice to me")
