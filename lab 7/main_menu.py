
from file_editor import file_reader, data_writter, data_store

def combination_function():
    """  Reads a file
        ,write user input to a file 
        ,saves user data in a json format
        ,Validates all user inputs to ensure correctness. 
        ,Ensures all exceptions are handled gracefully. 
        ,Provides a menu system to navigate between the tasks.
    """
    user_choice = input("Choose an option:\n" \
                        "1. Read a file\n" \
                        "2. Write to a file\n" \
                        "3. Store data to JSON \n" \
                        "4. Exit\n" \
                        "Choose an option (1, 2, 3 or 4): ")
    if user_choice == '1':      
        file_reader()
    elif user_choice == '2':
        data_writter()      
    elif user_choice == '3':
        data_store()
    elif user_choice == '4':
        print("Goodbye!")
        return
    combination_function()


combination_function()

