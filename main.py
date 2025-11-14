# imports
import toolbox as tb
from resumes import user_resumes
from email.utils import parseaddr
from urllib.parse import urlparse

# validation functions
## checks if a URL is valid
def valid_url(u):
    p = urlparse(u); return p.scheme in ("http","https") and p.netloc
## checks if an email is valid
def valid_email(e):
    return '@' in parseaddr(e)[1]

# starting intro
## prints the intro screen
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
    print("\tthe dunking doughnuts employment chatbot")
    tb.wait()
## returns name (str) and age (int)
def get_info():
    name = input("WHAT IS YOUR FIRST AND LAST NAME? ").title()
    tb.wait()
    while True:
        try:
            age = int(input("HOW OLD ARE YOU? "))
            break
        except ValueError:
            print("\nplease enter a valid age.")
            tb.wait()
    return name,age # after validation
## greets user based on age difference with creator (16 years old)
def greet_user(name,age):
    diff = 16 - age
    if diff > 0:
        if diff == 1:
            print(f"welcome, {name}. you are 1 year younger than my creator!")
        else:
            print(f"welcome, {name}. you are {diff} year(s) younger than my creator!")
    elif diff == 0:
        print(f"welcome, {name}. my creator's the same age!")
    else: # diff < 0
        if diff == -1:
            print(f"welcome, {name}. you are 1 year older than my creator!")
        else:
            print(f"welcome, {name}. you are {-diff} years older than my creator!")
    tb.wait()

# options menu
## option 0 - submit resume
def submit_resume(name,age):
    email = input("PLEASE ENTER YOUR EMAIL ADDRESS: ")
    while not valid_email(email):
        print("invalid email format. Please try again.")
        email = input("PLEASE ENTER YOUR EMAIL ADDRESS: ")
    
    link = input("PLEASE PASTE THE LINK TO YOUR RESUME HERE: ")
    while not valid_url(link):
        print("invalid URL format. Please try again.")
        link = input("PLEASE PASTE THE LINK TO YOUR RESUME HERE: ")
    
    print("\nprocessing resume...")
    user_resumes.append({"name":name, "age":age,"email":email, "resume":link})
## option 1 - speak to a representative
def speak_to_rep():
    print("phone: 1-800-DUNKIN")
    print("email: dunking@gmail.com")
    print("address: 123 Coffee St, Caffeine City, CA 90210")
    print("hours: 09:00 - 17:00, mon - fri")
    print("\nwe look forward to assisting you!")
## option 2 - view resumes (admin only)
def view_resumes():
    password = input("ENTER ADMIN PASSWORD: ")
    if password == "admin123":
        print("\nsubmitted resumes:")
        print("-" * 40)
        if user_resumes:
            for resume in user_resumes:
                print(f"name: {resume['name']}")
                print(f"age: {resume['age']}")
                print(f"email: {resume['email']}")
                print(f"resume: {resume['resume']}")
                print("-" * 40)
        else:
            print("no resumes submitted yet.")
            print("-" * 40)
    else:
        print("incorrect password. access denied.")
## option 3 - office rules & expectations
def office_rules():
    print("office rules & expectations:")
    print("-" * 40)
    print("1) be punctual and reliable.")
    print("2) maintain a positive attitude.")
    print("3) follow health and safety guidelines.")
    print("4) communicate effectively with team members.")
    print("5) uphold company values and ethics.")
    print("-" * 40)
    print("\nthank you for reviewing our office rules! you've got this!")

# main loop
## displays the menu and handles user choices
def menu(name,age):
    print("how can I help you?\n")
    print("0) submit a resume")
    print("1) speak to a representative")
    print("2) view submitted resumes (admin only)")
    print("3) explore office rules & expectations")
    print("4) exit")
    
    choice = None
    while True:
        try:
            choice = int(input("\nENTER A NUMBER (0-4): "))
            if choice in range(5):
                break
        except ValueError:
            pass
        print("please enter a number between 0 and 4.")
    
    tb.clear()
    if choice == 0:
        submit_resume(name,age)
    elif choice == 1:
        speak_to_rep()
    elif choice == 2:
        view_resumes()
    elif choice == 3:
        office_rules()
    else:
        print("thank you for using DDEC, goodbye!")
        return False
    return True
## main function
def main():
    tb.clear()
    intro()
    name,age = get_info()
    tb.wait()
    greet_user(name,age)
    running = True
    while running:
        running = menu(name,age)
        tb.wait()
## main execution
if __name__ == "__main__":
    main()