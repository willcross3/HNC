import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")
        self.root.geometry("800x600")
        self.file_name = 'flashcards.csv'  # Assume this file already exists
        self.create_widgets()

    def create_widgets(self):
        """Create GUI widgets."""
        buttons = [
            ("Add Flashcard", self.add_flashcard),
            ("View Flashcards", self.view_flashcards),
            ("Delete Flashcard", self.delete_flashcard),
            ("Quit", self.root.quit)
        ]
        for text, command in buttons:
            button = tk.Button(self.root, text=text, command=command)
            button.pack(pady=10)

    def add_flashcard(self):
        """Add a flashcard to the CSV file."""
        question = simpledialog.askstring("Input", "Enter the question:")
        if question:
            answer = simpledialog.askstring("Input", "Enter the answer:")
            if answer:
                with open(self.file_name, mode='a', newline='') as file:
                    csv.writer(file).writerow([question, answer])
                messagebox.showinfo("Success", "Flashcard added!")

    def view_flashcards(self):
        """Display all flashcards in a message box."""
        if not os.path.exists(self.file_name):
            messagebox.showwarning("Warning", "No flashcards found.")
            return

        with open(self.file_name, mode='r') as file:
            flashcards = [f"Q: {row[0]} | A: {row[1]}" for row in csv.reader(file)][1:]

        messagebox.showinfo("Flashcards", "\n".join(flashcards) if flashcards else "No flashcards available.")

    def delete_flashcard(self):
        """Delete a flashcard based on the question."""
        question_to_delete = simpledialog.askstring("Input", "Enter the question of the flashcard to delete:")
        if question_to_delete:
            with open(self.file_name, mode='r') as file:
                rows = list(csv.reader(file))
            header, flashcards = rows[0], rows[1:]

            remaining = [row for row in flashcards if row[0] != question_to_delete]
            if len(remaining) < len(flashcards):
                with open(self.file_name, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
                    writer.writerows(remaining)
                messagebox.showinfo("Success", "Flashcard deleted!")
            else:
                messagebox.showwarning("Warning", "Flashcard not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()