#Notepad
class Notepad:
    def __init__(self):
        self.notes=[]
    def add_note(self,note):
        self.notes.append({"note":note,"completed":False})
    def delete_note(self,note_number):
        try:
            del self.notes[note_number -1]
        except IndexError:
            print("Invalid note number.")
    def mark_completed(self,note_number):
        try:
            self.notes[note_number -1]["Comleted"]=True
        except IndexError:
            print("Invalid Note Number.")
    def view_notes(self):
        for i, note in enumerate(self.notes,start=1):
            status= "Completed" if note["completed" ]else "Not Completed Note"   
            print(f"{i}. {note['note']} -{status}")

def main():
    notepad=Notepad()

    while True:
        print("\n  Notepad App  ")
        print("1.New Note")
        print("2.Delete Note")
        print("3.Mark Note As Completed")
        print("4.View Notes")
        print("5.Exit")
        choice= input("Choose an option : ")
        if choice=="1":
            note= input("Enter New Note : ")
            notepad.add_note(note)
        elif choice =="2":
            note_number= int(input("Enter the note number to delete : "))
            notepad.delete_note(note_number)
        elif choice =="3":
            note_number= int(input("Enter the note number to mark as completed: "))
            notepad.mark_completed(note_number)  
        elif choice =="4":
            notepad.view_notes()
        elif choice =="5":
            break
        else:
            print("Invalid option. Please try again.")
if __name__=="__main__":
    main()                          
