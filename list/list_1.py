# create a guest list and invite them
guest_list = ['Albert Einstein', 'Isaac Newton', 'Galileo Galilei']

print(f"Dear {guest_list[0]}, I would like to invite you to dinner.")
print(f"Dear {guest_list[1]}, I would like to invite you to dinner.")
print(f"Dear {guest_list[2]}, I would like to invite you to dinner.")

print()
# change the guest who can't come
print(f"{guest_list[0]} can't make it to dinner.")
guest_list[0] = 'Nikola Tesla'

print(f"Dear {guest_list[0]}, I would like to invite you to dinner.")
print(f"Dear {guest_list[1]}, I would like to invite you to dinner.")
print(f"Dear {guest_list[2]}, I would like to invite you to dinner.")

print()
# found a bigger table add guest using insert and append
print("I found a bigger table!")

guest_list.insert(0, 'Marie Curie')
guest_list.insert(int(len(guest_list)/2), 'Charles Darwin')
guest_list.append('Stephen Hawking')

print(f"Dear {guest_list[0]}, I would like to invite you to dinner.")
print(f"Dear {guest_list[1]}, I would like to invite you to dinner.")
print(f"Dear {guest_list[2]}, I would like to invite you to dinner.")
print(f"Dear {guest_list[3]}, I would like to invite you to dinner.")
print(f"Dear {guest_list[4]}, I would like to invite you to dinner.")
print(f"Dear {guest_list[5]}, I would like to invite you to dinner.")

print()
# big table not coming, so we removed guest using pop
print("I can only invite two people to dinner.")

remove_guest_0 = guest_list.pop(0)
print(f"Sorry, ' + {remove_guest_0} + ', I can't invite you to dinner.")
remove_guest_0 = guest_list.pop(0)
print(f"Sorry, ' + {remove_guest_0} + ', I can't invite you to dinner.")
remove_guest_0 = guest_list.pop(0)
print(f"Sorry, ' + {remove_guest_0} + ', I can't invite you to dinner.")
remove_guest_0 = guest_list.pop(0)
print(f"Sorry, ' + {remove_guest_0} + ', I can't invite you to dinner.")

print()
# inform guest list they are still invited
print(f"Dear {guest_list[0]}, You are still invited to the dinner.")
print(f"Dear {guest_list[1]}, You are still invited to the dinner.")

print()
# empty the list
del guest_list[0]
del guest_list[0]
print(guest_list)
