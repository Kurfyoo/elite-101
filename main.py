import sys
import os
import toolbox as tb
from resumes import user_resumes

def intro():
    print(
        "██████╗ ██████╗ ███████╗ ██████╗     ██╗    ██████╗  █████╗ ",
        "██╔══██╗██╔══██╗██╔════╝██╔════╝    ███║   ██╔═████╗██╔══██╗",
        "██║  ██║██║  ██║█████╗  ██║         ╚██║   ██║██╔██║╚█████╔╝",
        "██║  ██║██║  ██║██╔══╝  ██║          ██║   ████╔╝██║██╔══██╗",
        "██████╔╝██████╔╝███████╗╚██████╗     ██║██╗╚██████╔╝╚█████╔╝",
        "╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝     ╚═╝╚═╝ ╚═════╝  ╚════╝ ",
        sep = "\n"
    )
    print("\tThe Dunking Doughnuts Employment Chatbot")
    tb.wait()

# returns name (str) and age (int)
def get_info():
    name = input("What is your name? ").title()
    tb.wait()
    try:
        age = int(input("How old are you? "))
    except ValueError:
        print("\nPlease enter a valid age.")
        tb.wait()
        return get_info()
    return name,age

def greet_user(name,age):
    diff = 16 - age
    if diff > 0:
        if diff == 1:
            print(f"Welcome, {name}. You are 1 year younger than my creator!")
        print(f"Welcome, {name}. You are {diff} year(s) younger than my creator!")
    elif diff == 0:
        print(f"Welcome, {name}. My creator's the same age!")
    else: # diff < 0
        if diff == -1:
            print(f"Welcome, {name}. You are 1 year older than my creator!")
        print(f"Welcome, {name}. You are {-diff} years older than my creator!")
    tb.wait()

# option 0 - submit resume
def submit_resume(name,age):
    email = input("Please enter your email address: ")
    link = input("Please paste the link to your resume here: ")
    print("\nProcessing resume...")
    user_resumes.append({"name":name, "age":age,"email":email, "resume":link})
# option 1 - speak to a representative
def speak_to_rep():
    print("PHONE NUMBER: 1-800-DUNKIN")
    print("EMAIL: dunking@gmail.com")
    print("ADDRESS: 123 Coffee St, Caffeine City, CA 90210")
    print("HOURS: 9 AM - 5 PM, Mon - Fri")
    print("\nWe look forward to assisting you!")
# option 2 - view resumes (admin only)
def view_resumes():
    password = input("Enter admin password: ")
    if password == "admin123":
        print("\nSubmitted Resumes:")
        print("-" * 40)
        for resume in user_resumes:
            print(f"Name: {resume['name']}")
            print(f"Age: {resume['age']}")
            print(f"Email: {resume['email']}")
            print(f"Resume Link: {resume['resume']}")
            print("-" * 40)
    else:
        print("Incorrect password. Access denied.")
# option 3 - office rules & expectations
def office_rules():
    print("Office Rules & Expectations:")
    print("-" * 40)
    print("1) Be punctual and reliable.")
    print("2) Maintain a positive attitude.")
    print("3) Follow health and safety guidelines.")
    print("4) Communicate effectively with team members.")
    print("5) Uphold company values and ethics.")
    print("-" * 40)
    print("\nThank you for reviewing our office rules! You've got this!")

def menu(name,age):
    print("How can I help you?\n")
    print("0) submit a resume")
    print("1) speak to a representative")
    print("2) view submitted resumes (admin only)")
    print("3) explore office rules & expectations")
    print("4) exit")
    
    choice = None
    while choice not in range(5):
        choice = int(input("\nEnter a number (0-4): "))
    
    os.system("clear")
    if choice == 0:
        submit_resume(name,age)
    elif choice == 1:
        speak_to_rep()
    elif choice == 2:
        view_resumes()
    elif choice == 3:
        office_rules()
    else:
        return False
    return True

def main():
    os.system("clear")
    intro()
    name,age = get_info()
    tb.wait()
    greet_user(name,age)
    running = True
    while running:
        running = menu(name,age)
        tb.wait()

if __name__ == "__main__":
    main()