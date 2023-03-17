from creator import auto_create
from creator import update_entries
from creator import set_api_key
from creator import set_dall_e_endpoint
from quality_of_life import clear
from dotenv import load_dotenv
from dotenv import find_dotenv

import time
import os

load_dotenv(find_dotenv())

while True:
    clear()
    print("*************************DALL E IMAGE GENERATOR***************************")
    print("*")
    print("* Menu:")
    print("* 1. Generate image automatically")
    print("* 2. Supply suggestion manually")
    print("* 3. Create a new list for suggestions (supply a json array)")
    print("* 4. Fill in/change your API key for DALL-E")
    print(
        "* 5. Change endpoint for DALL-E (APP only tested with : https://api.openai.com/v1/images/generations)"
    )
    print("* 6. show env values")
    print("* 7. Quit this application")
    print("* ? for general help")
    print("*")
    print("*************************DALL E IMAGE GENERATOR***************************")
    choice = input("Enter your choice: ")

    if choice == "1":
        print(auto_create())
        time.sleep(6)
    elif choice == "2":
        suggestion = input("Enter your suggestion: ")
        print(auto_create(suggestion))
        time.sleep(6)
    elif choice == "3":
        updateList = input("paste new list here")
        print(update_entries(updateList))

    elif choice == "4":
        api_key = input(
            "enter DALL-E apiKey (https://platform.openai.com/account/api-keys)"
        )
        print(set_api_key(api_key))

    elif choice == "5":
        dall_e_endpoint = input(
            "enter DALL-E endpoint (https://openai.com/blog/dall-e-api-now-available-in-public-beta)"
        )
        print(set_dall_e_endpoint(dall_e_endpoint))
    
    elif choice == "6":
            print("5 seconds before i return to main menu")
            print(f"API key = {os.environ.get('API_KEY')}")
            print(f"API endpoint = {os.environ.get('API_ENDPOINT')}")
            time.sleep(6)

    elif choice == "7":
            print("Quitting...")
            break
    
    elif choice == "?":
        clear()
        print ("***** General Info ******")
        print ("1. This image generator has only been testetd with DALL-E, when using another endpoint expect strange behaviour.")
        print ("2. When you use a json list, a random entry will be picked and the entry removed so you will not have duplicates.")
        print ("Press return to go back to main")
        input()

    else:
        print("Invalid choice. Please choose an option from the menu.")
