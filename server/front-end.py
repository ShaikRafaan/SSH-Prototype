import webbrowser
def open_website(choice):
    websites = {
        "1": "http://localhost:8000/docs#/OrderManagement/",
        "2": "http://localhost:8000/docs#/Accommodations",
        "3": "http://localhost:8000/docs#/Supermarkets",
        "4": "http://localhost:8000/docs#/Products",
        "5": "http://localhost:8000/docs#/users"
    }
    if choice in websites:
        webbrowser.open(websites[choice])
    else:
        print("Invalid choice. Please select a valid option.")
print("Select an option to open a Feature:")
print("1. Order Management")
print("2. Accommodations")
print("3. Supermarkets")
print("4. Products")
print("5. Users")

user_choice = input("Enter the number of your choice: ")
open_website(user_choice)
