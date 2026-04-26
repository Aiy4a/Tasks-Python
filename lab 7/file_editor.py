from pathlib import Path
import json 

def file_reader():
    
    """Takes a file path as input and prints its contents if found"""
    path = input("Enter the file path: ")
    path = Path(path)
    try:
        content = path.read_text()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        user_input = input("Would you like to try again? (y/n)?").lower()
        if user_input == 'y':
            file_reader()
        else:
            return
    else:
        print(f"Contents of '{path}': ")   
        print(content) 



def data_writter():
    
    """Asks for the file b=name and data to write into it"""
    file_name = input("Enter the file name: ")
    path = Path(file_name)
    data = input("Enter the text to save: ")

    try:
        path.write_text(data) 
    except PermissionError:
        print(f"Error: Permission denied to write to '{file_name}'")
    else:
        print(f"Data saved successfully to '{file_name}'")
        print(f"Contents of '{file_name}': ")
        print(path.read_text())
        
        



    

   

def data_store( file_name , data):
    
    """Saves user data into a file in jason format"""
    path = Path(file_name + ".json")
    try:
        json.dump(data, path.open('w')) #this opens file and takes data to write in it 
        
        ## if dumps where used:
        #path.write_text( json.dumps(data) ) --> would convert data to json string and then write it to the file

    except IOError:
        print(f"Error: {file_name} could not be written.")
    else:
        print(f"Data saved successfully to '{file_name}.json'")
        print(f"Contents of '{file_name}.json': ")
        print(json.load(path.open('r')))  # this opens file and reads data from it 

        ## if load where used: 
        #json.loads(path.read_text())--> would read the text from the file and then load it as json


data = { 
    "name": "Alice",  
    "age": 25, 
    "city": "New York"
}
