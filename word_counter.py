import tkinter as tk
from tkinter import messagebox

# Function to count the number of words
def count_words(text):
    """
    This function takes a string as input and returns the number of words.
    It splits the text into words using spaces as delimiters.
    """
    words = text.split()  # Split the text into a list of words
    return len(words)     # Return the number of words in the list

# Function to handle the button click event
def on_submit():
    # Get the input text from the text widget
    user_input = text_input.get("1.0", "end-1c").strip()

    # Error handling: Check if the input is empty
    if not user_input:
        messagebox.showerror("Error", "Please enter some text!")
    else:
        # Count the words using the count_words function
        word_count = count_words(user_input)
        # Display the word count in the result label
        result_label.config(text=f"Word Count: {word_count}")

# Create the main application window
app = tk.Tk()
app.title("Word Counter")  # Set the title of the window
app.geometry("400x300")    # Set the size of the window

# Create and place a label for instructions
instruction_label = tk.Label(app, text="Enter your sentence or paragraph below:", font=("Arial", 12))
instruction_label.pack(pady=10)

# Create a text input widget
text_input = tk.Text(app, height=10, width=40, font=("Arial", 12))
text_input.pack(pady=10)

# Create a submit button
submit_button = tk.Button(app, text="Count Words", command=on_submit, font=("Arial", 12))
submit_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(app, text="Word Count: 0", font=("Arial", 12))
result_label.pack(pady=10)

# Run the application
app.mainloop()
