import sys

import menu_text
import crud
from queries import create_tables,logut_all
import auth


def show_auth_menu():
    print(menu_text.auth_menu)
    option = input("Enter your option: ")

    if option == "1":
        if auth.register():
            print("Check your email we send a verification code. Activate your email by menu 3.")
        else:
            print("Something went wrong")

    elif option == "2":
        if auth.login():
            print("Welcome to main menu")
            show_main_menu()
        else:
            print("Something went wrong")

    elif option == "3":
        auth.activate_email()

    elif option == "4":
        sys.exit()

    else:
        print("Invalid option")
    return show_auth_menu()



def show_main_menu():

    print(menu_text.main_menu)
    option = input("Enter your option: ")

    if option == "1":
      result = crud.show_tweets()
      print(result)

    elif option == "2":
       result = crud.add_tweet()
       print(result)
    
    elif option == "3":
        result = crud.update_tweet()
        print(result)

    elif option == "4":
       result = crud.delete_tweet()
       print(result)

    elif option == "5":
       result = crud.show_my_tweets()
       print(result)
    
    elif option == "6":
        sys.exit()

    else:
        print("Invalid option")
    return show_main_menu()



if __name__ == "__main__":
    create_tables()
    logut_all()
    show_auth_menu()
