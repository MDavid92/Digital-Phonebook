import json


print("Digital Phonebook")

with open("contacts.json", "r") as f:
    data = json.load(f)

sorted_json = json.dumps(data, sort_keys=True)

def check_answer(allowed, answer):
    if answer in allowed:
	    return "answer_allowed"
    else:
	    return "not_allowed"

def delete_profile():
    contact_name = input("Enter Contact Name: ")
    contacts = json.loads(open('contacts.json').read())

    try:
        contacts.pop(contact_name)
        json.dump(contacts, open('contacts.json', 'w'))
        print("Profile has been deleted")
        data.pop(contact_name)
        check_database()
    except KeyError:
        print(" ")
        print("Contact Not Found")
        check_database()

def check_database():
    main_menu_ans = 0
    allowed = ["1", "2", "3", "4"]
    print("""
Profiles in database
     """)
    for name in sorted(data):
        print(name)
    print(
"""
  CHOOSE ACTION
1. View profile
2. Delete profile
3. Update profile
4. Back to main menu"""

    )
    print(" ")
    while check_answer(allowed, main_menu_ans) != "answer_allowed":
        ans = input("Enter the number of the chosen action: ")
        if ans == "1":
            contact()
        elif ans == "2":
            delete_profile()
        elif ans == "3":
            update_profile()
        elif ans == "4":
            main_menu()



def contact():
    print("  ")
    name = input("Please enter name: ")
    print("  ")
    print("Name: " + str(data[name]['Name']))
    print("Address: " + str(data[name]['Address']))
    print("Phone: " + str(data[name]['Phone']))
    print("E-mail: " + str(data[name]['E-mail']))
    print("LinkedIn: " + str(data[name]['LinkedIn']))
    print("""
Press Enter to continue: """)
    input()
    check_database()

def adding_profile():
    name = input("Enter name: ")
    if name in data.keys():
        print("Profile already exists. Enter a different name.\n")
        main_menu()
    else:
        address = input("Enter address: ")
        phone = input("Enter phone number: ")
        email = input("Enter e-mail address: ")
        linkedin = input("Enter LinkedIn profile: ")
        my_dict = data
        my_dict1 = {"Name": name, "Address": address, "Phone": phone, "E-mail": email, "LinkedIn": linkedin }

        my_dict[name] = my_dict1

        y = json.dumps(my_dict)

        with open("contacts.json", "w") as outfile:
            outfile.write(y)
        print("Profile has been added!")
        main_menu()




def update_profile():
    name = input("Enter profile name: ")
    print("Press Enter to ignore.")
    name1 = input("Enter updated name: ")
    if name1 == "":
        address = input("Enter updated address: ")
        if address == "":
            print("skipped")
        else:
            d2 = {"Address": address}
            data[name].update(d2)
        phone = input("Enter updated phone number: ")
        if phone == "":
            print("skipped")
        else:
            d3 = {"Phone": phone}
            data[name].update(d3)
        email = input("Enter updated e-mail address: ")
        if email == "":
            print("skipped")
        else:
            d4 = {"E-mail": email}
            data[name].update(d4)
        linkedin = input("Enter updated LinkedIn profile: ")
        if linkedin == "":
            print("skipped")
        else:
            d5 = {"LinkedIn": linkedin}
            data[name].update(d5)
        main_menu()
    else:
        address1 = input("Enter address: ")
        if address1 == "":
            address1 = data[name]["Address"]
        phone1 = input("Enter phone number: ")
        if phone1 == "":
            phone1 = data[name]["Phone"]
        email1 = input("Enter e-mail address: ")
        if email1 == "":
            email1 = data[name]["E-mail"]
        linkedin1 = input("Enter LinkedIn profile: ")
        if linkedin1 == "":
            linkedin1 = data[name]["LinkedIn"]
        my_dict = data
        my_dict1 = {"Name": name1, "Address": address1, "Phone": phone1, "E-mail": email1, "LinkedIn": linkedin1}

        my_dict[name1] = my_dict1

        y = json.dumps(my_dict)

        with open("contacts.json", "w") as outfile:
            outfile.write(y)

        contacts = json.loads(open('contacts.json').read())
        contacts.pop(name)
        json.dump(contacts, open('contacts.json', 'w'))
        data.pop(name)
        print("Profile has been modified!")
        check_database()

def quit_q():
    main_menu_ans = 0
    allowed = ["1", "2", "3", "4"]
    while check_answer(allowed, main_menu_ans) != "answer_allowed":
        ansq = input("Are you sure? y/n")
        if ansq == "n":
            main_menu()
        elif ansq == "y":
            quit()

def main_menu():
    main_menu_ans = 0
    allowed = ["1", "2", "3"]
    print("""
    1. Search in database
    2. Add profile
    3. Quit
    """)
    while check_answer(allowed, main_menu_ans) != "answer_allowed":
        ans = input("Enter the number of the chosen option: ")
        if ans == "1":
            check_database()
        elif ans == "2":
            adding_profile()
        elif ans == "3":
            quit_q()




main_menu()