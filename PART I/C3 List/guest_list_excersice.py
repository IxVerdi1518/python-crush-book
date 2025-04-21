#3.4
guest_list=['samantha', 'glamis', 'wilmer']
message="I invite you to come at Pizza's Restaurant: "
print(message+guest_list[0].title())
print(message+guest_list[1].title())
print(message+guest_list[2].title())

#3.5
print("The person who can't come to the dinner is: "+guest_list[1].title())
guest_list[1]='daniel'
print(message+guest_list[0].title())
print(message+guest_list[1].title())
print(message+guest_list[2].title())

#3.6
important_message='Appreciate you time, but we need to modify the table where we can stay'
print(important_message)
guest_list.insert(0,'camila')
guest_list.insert(2,'cristian')
guest_list.append('benja')
print(message+guest_list[0].title())
print(message+guest_list[1].title())
print(message+guest_list[2].title())
print(message+guest_list[3].title())
print(message+guest_list[4].title())
print(message+guest_list[5].title())

#3.7
important_message="Soory for this message, but we won't go for the dinner!, "
person_cancel=guest_list.pop()
print(important_message+person_cancel.title())
person_cancel=guest_list.pop()
print(important_message+person_cancel.title())
person_cancel=guest_list.pop(-2)
print(important_message+person_cancel.title())
person_cancel=guest_list.pop(-2)
print(important_message+person_cancel.title())
del guest_list[0]
del guest_list[0]
print(guest_list)