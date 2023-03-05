#
#Note:
#This program will not work without a proper api key
#


import tkinter as tk
import openai
openai.api_key = "confidential" #Note: Will not work without a proper api key

# Create the main window
root = tk.Tk()
root.title("GPT-3")

# Create a Label to display the static text
static_text = "Enter the prompt:"
label = tk.Label(root, text=static_text)
label.pack()

# Create a Text widget to display user input
text_box = tk.Text(root, height=5, width=50, wrap="word")
text_box.pack()


# Enable text selection and copying in the Text widget
def select_text(event):
    text_box.tag_add(tk.SEL, "1.0", tk.END)
    text_box.tag_config(tk.SEL, background="yellow", foreground="black")
text_box.bind("<Control-Key-a>", select_text)

# Create a button to display the user input as copyable text
def display_text():
    input_text = text_box.get("1.0", tk.END)
    prompt = str(input_text)
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=500)
    output_label.config(text=response["choices"][0]["text"])

button = tk.Button(root, text="Submit", command=display_text)
button.pack()

# Create a Label to display the copyable text
output_label = tk.Label(root, text="")
output_label.pack()

# Start the main event loop
root.mainloop()
