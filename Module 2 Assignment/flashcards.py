import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os
from PIL import Image, ImageTk


class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App") #window title
        self.root.geometry("800x600")  #window size
        self.root.configure(bg='white')  #background color
        self.file_name = 'flashcards.csv'  #csv filename
        self.create_widgets() #create widgets
        self.load_image() #loads image
        self.load_image1()  #loads image
    
    def load_image(self):
        image = Image.open('NewLogo.png')  #opens image
        resized = image.resize((200, 200))  #resizes image
        self.newimage = ImageTk.PhotoImage(resized)
        self.label = tk.Label(self.root, image=self.newimage)  #displays new resized image
        self.label.place(x=30, y=30)

    def load_image1(self):
        image1= Image.open('NewLogo1.png')  #opens image
        resized1 = image1.resize((200, 200))
        self.newimage1 = ImageTk.PhotoImage(resized1)
        self.label1 = tk.Label(self.root, image=self.newimage1)
        self.label1.place(x=570, y=30)

    def create_widgets(self): # creates GUI widgets
        buttons = [
            ("Add Flashcard", self.add_flashcard),  #button to add flashcard
            ("View Flashcards", self.view_flashcards),  #button to view flashcards
            ("Delete Flashcard", self.delete_flashcard),  #button to delete flashcard
            ("Quit", self.root.quit)  #button to quit
        ]
        for text, command in buttons:
            button = tk.Button(self.root, text=text, command=command)  #creates buttons 
            button.pack(pady=30)  #adds padding between buttons

    def add_flashcard(self):  #adds flashcard to csv file
        question = simpledialog.askstring("Input", "Enter the question:")  #asks user to enter question
        if question:
            answer = simpledialog.askstring("Input", "Enter the answer:")  #asks user to enter answer
            if answer:
                with open(self.file_name, mode='a', newline='') as file:  #appends question and answer to csv file
                    csv.writer(file).writerow([question, answer])
                messagebox.showinfo("Success", "Flashcard added!")  #displays success message

    def view_flashcards(self):  #displays all flashcards in a message box
        if not os.path.exists(self.file_name):
            messagebox.showwarning("Warning", "No flashcards found.")  #if no flashcards are found, a warning message is displayed
            return

        with open(self.file_name, mode='r') as file:  #reads flashcards from csv file
            flashcards = [f"Q: {row[0]} | A: {row[1]}" for row in csv.reader(file) if len(row) >= 2]

        if not flashcards:
            messagebox.showwarning("Warning", "No flashcards available.")  #if no flashcards are available, a warning message is displayed
        else:
            flashcards = flashcards[1:]  # Remove the header row
            messagebox.showinfo("Flashcards", "\n".join(flashcards))

    def delete_flashcard(self):  #deletes flashcard based on question
        question_to_delete = simpledialog.askstring("Input", "Enter the question of the flashcard to delete:")
        if question_to_delete:
            with open(self.file_name, mode='r') as file:  #reads flashcards from csv file
                rows = list(csv.reader(file))  #converts csv file to list
            header, flashcards = rows[0], rows[1:]  #separates header and flashcards

            remaining = [row for row in flashcards if row[0] != question_to_delete]  #deletes flashcard based on question
            if len(remaining) < len(flashcards):  #checks if flashcard was deleted
                with open(self.file_name, mode='w', newline='') as file:
                    writer = csv.writer(file)  #writes remaining flashcards to csv file
                    writer.writerow(header)  
                    writer.writerows(remaining)
                messagebox.showinfo("Success", "Flashcard deleted!")
            else:
                messagebox.showwarning("Warning", "Flashcard not found.")

if __name__ == "__main__":  #runs the app
    root = tk.Tk()  #creates window
    app = FlashcardApp(root)  #creates app
    root.mainloop()  #runs app

