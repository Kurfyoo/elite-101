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

def get_info():
    name = input("What is your name? ").title()
    tb.wait()
    age = int(input("How old are you? "))
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

def submit_resume(name,age):
    link = input("Please paste the link to your resume here: ")
    print("\nProcessing resume...")
    user_resumes = user_resumes.append({"name":name, "age":age, "resume":link})
def speak_to_rep():
    pass
def two():
    pass
def three():
    pass
def exit():
    os.system("clear")
    print("Glad if I could help. Goodbye!")
    sys.exit()

def menu():
    print("How can I help you?\n")
    print("0) submit a resume")
    print("1) speak to a representative")
    print("2) two")
    print("3) three")
    print("4) exit")
    
    choice = None
    while choice not in range(5):
        choice = int(input("\nEnter a number (0-4): "))
    
    if choice == 0:
        submit_resume()
    elif choice == 1:
        speak_to_rep()
    elif choice == 2:
        two()
    elif choice == 3:
        three()
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
        running = menu()
        tb.wait()
if __name__ == "__main__":
    main()