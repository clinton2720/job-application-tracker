import json
from tabulate import tabulate


print("\n-----------Job Application Tracker-----------")


#main for input for job title, application date, method of aplication, url
def main():
    while True:
        try:    
            choice = int(input("\n\nEnter action number: \n1) Add\n2) Update\n3) Delete\n4) List\n5) Exit\nNumbered input: "))
        except ValueError:
            print("Invalid input.")
            continue

        match choice:
            case 1:
                add()
            case 2:
                update()
            case 3:
                delete()
            case 4:
                list_out()
            case 5:
                break


#functions for applications and writing to csv file


def load():
    try:
        with open("job_app.json", "r") as json_file:
            file = json.load(json_file)
    except FileNotFoundError:
        return []
    return file



def save(new_data):
    with open("job_app.json", "w") as f:
        json.dump(new_data, f, indent=4)



'''to get input from user in form of int or str'''
def get_user_input(prompt, expected_type=str):
    while True:
        if expected_type is str:
            return input(prompt).strip()
        elif expected_type is int:
            try:
                return int(input(prompt).strip())
            except ValueError:
                print("Invalid input. Type a number.")
                continue

 
'''to get input for the applications'''
def get_application_input():
    company = input("Enter company name: ").strip()
    role_name = input("Enter role name: ").strip()
    date_applied = input("Enter date applied: ").strip()
    status = input("Enter status: ").strip()
    return {
        "id": None,
        "company": company,
        "role_name": role_name,
        "date_applied": date_applied,
        "status": status
    }



'''to confirm actions, expects prompt and type-int, yes/no'''
def confirm(prompt, expected_type = None):
    while True:

        if expected_type == int:
            try:
                return int(input(prompt).strip())
            except ValueError:
                print("Invalid Input")
                continue

        elif expected_type == "y/n":
            user_input = input(prompt).strip().lower()
            if user_input in ("yes", "y"):
                return True
            elif user_input in ("no", "n"):
                return False
            else:
                print("Invalid input.")
                continue
        else:
            user_input = input(prompt).strip()
            if user_input:
                return user_input
            print("Input cant be blank.")
            

'''to pretty print applications'''
def pretty_print(data):
    print(tabulate(data, showindex=False, tablefmt="grid", headers="keys"))



'''to add/create new applications'''
def add():
    next_id = 1
    add_app = load()
    ids = [app["id"] for app in add_app]
    if ids:
        next_id = max(ids) + 1
    application = get_application_input()
    application["id"] = next_id # type: ignore
    pretty_print([application])
    if confirm("Are you sure you want to add?(Y,n): ", expected_type="y/n"):
        add_app.append(application)
        save(add_app)
        print("\n\nLoaded!\n\n\n")



'''to update existing applications, have to rewrite all data for application to update, cant update just one field'''
def update():

    job_id = get_user_input("Enter job ID you want to update: ", expected_type=int) # type: ignore
    
    updated_app = list()
    apps = load()
    found_app = False

    for app in apps:

        if app["id"] == job_id:
            found_app = True
            print(tabulate([app], headers="keys", showindex=False, tablefmt="simple_grid"))
            new_app = get_application_input()
            new_app["id"] = job_id  # type: ignore
            pretty_print([new_app])

            if confirm("Are you sure you want to update?(Y/n): ", expected_type="y/n"):
                updated_app.append(new_app)
            else:
                updated_app.append(app)

        else:
            updated_app.append(app)
            
    if found_app is True:
        save(updated_app)
        print("\nUpdated!\n")
    else:
        print("Not found. Try again!")



'''to delete application'''
def delete():
    new_list = [] #Creating new list to overwrite main application list excluding user selection
    
    selection = get_user_input("Enter job ID you want to delete: ", expected_type=int)


    application_list = load()
    for app in application_list:
        if selection == app["id"]: # type: ignore
            pretty_print([app])
            if confirm("Are you sure you want to delete?(Y/n): ", expected_type="y/n"):
                continue
            else:
                new_list.append(app)
        else:
            new_list.append(app)

    save(new_list)

    print("\n\nDone!")



'''to list out all applications'''
def list_out():
    applications = load()
    print("\n\n")
    pretty_print(applications)



if __name__ == "__main__":
    main()