def add_note(): # first func to add new note 
    note = input("Enter your note: ") # user enter the note 
    with open("notes.txt", "a") as file: # create file notes.txt and append in file (write)
        file.write(note + "\n") # write note in line and add new line 

def view_notes(): # view notes you write 
    try:
        with open("notes.txt", "r") as file: # open the notes.txt
            notes = file.readlines() # save the lines of note in var (notes)
            for note in notes: # show the notes in lines 
                print(note.strip())
    except FileNotFoundError: # if no file not exist 
        print("No notes found.")

def delete_note(): # to delete the line of note you want
    view_notes() # show all notes to choces the line 
    note_to_delete = int(input("Enter the note number to delete: ")) - 1 # chose the line where the line in tables strt with 0
    with open("notes.txt", "r") as file: # open the file to read
        notes = file.readlines()

    if 0 <= note_to_delete < len(notes): # cheak of number of notes is correct !!
        del notes[note_to_delete] # delete the note it"s number = note_to_delete
        with open("notes.txt", "w") as file:
            file.writelines(notes)
    else: # if number of note is not correct 
        print("Invalid note number.")

# use app note by call all func.
def notes_app():
    while True:
        print("\n1. Add Note\n2. View Notes\n3. Delete Note\n4. Exit")
        choice = input("Choose an option: ") # chose the option you want 
        
        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# call the app func.
notes_app()
