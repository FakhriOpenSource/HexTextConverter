import tkinter as tk
from tkinter import messagebox

# Function to convert text to hexadecimal
def text_to_hexadecimal():
    text = text_entry.get()
    if not text:
        messagebox.showwarning("Input Error", "Please enter some text first!")
        return
    
    hex_values = [format(ord(char), '02x') for char in text]
    hex_string = ' '.join(hex_values)
    
    # Display result in the text box
    hex_output_text.delete(1.0, tk.END)  # Clear previous result
    hex_output_text.insert(tk.END, hex_string)

# Function to convert hexadecimal to text
def hexadecimal_to_text():
    hex_string = hex_entry.get()
    if not hex_string:
        messagebox.showwarning("Input Error", "Please enter some hexadecimal first!")
        return
    
    try:
        hex_values = hex_string.split(' ')
        text_chars = [chr(int(hv, 16)) for hv in hex_values]
        text_string = ''.join(text_chars)
    except ValueError:
        messagebox.showerror("Format Error", "Hexadecimal values must be separated by spaces and consist of valid hex digits.")
        return
    
    # Display result in the text box
    text_output_text.delete(1.0, tk.END)  # Clear previous result
    text_output_text.insert(tk.END, text_string)

# Function to copy hexadecimal result to clipboard
def copy_hex_to_clipboard():
    result = hex_output_text.get(1.0, tk.END).strip()
    if result:
        root.clipboard_clear()
        root.clipboard_append(result)
        messagebox.showinfo("Copied", "Text to hexadecimal result copied to clipboard!")

# Function to copy text result to clipboard
def copy_text_to_clipboard():
    result = text_output_text.get(1.0, tk.END).strip()
    if result:
        root.clipboard_clear()
        root.clipboard_append(result)
        messagebox.showinfo("Copied", "Hexadecimal to text result copied to clipboard!")

# Create main window
root = tk.Tk()
root.title("Text <-> Hexadecimal Converter")
root.geometry("700x600")
root.configure(bg="black")

# Button color and text color
button_color = "#4CAF50"
text_color = "white"

# Custom font
font_title = ("Helvetica", 16, "bold")
font_text = ("Helvetica", 12)

# Input text
tk.Label(root, text="Enter Text:", bg="black", fg="white", font=font_text).pack(pady=5)
text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=5)

# Button to convert text to hexadecimal
convert_text_button = tk.Button(root, text="Convert Text to Hexadecimal", command=text_to_hexadecimal, bg=button_color, fg=text_color)
convert_text_button.pack(pady=5)

# Output for text to hexadecimal conversion
tk.Label(root, text="Text to Hexadecimal Result:", bg="black", fg="white", font=font_text).pack(pady=5)
hex_output_text = tk.Text(root, height=5, wrap='none')  # Disable word wrap
hex_output_text.pack(fill=tk.X, padx=5)
hex_scrollbar_x = tk.Scrollbar(root, orient='horizontal', command=hex_output_text.xview)
hex_output_text.config(xscrollcommand=hex_scrollbar_x.set)
hex_scrollbar_x.pack(fill=tk.X)

# Button to copy hexadecimal result
copy_hex_button = tk.Button(root, text="Copy Hexadecimal Result", command=copy_hex_to_clipboard, bg="#2196F3", fg=text_color)
copy_hex_button.pack(pady=5)

# Input hexadecimal
tk.Label(root, text="Enter Hexadecimal (separated by spaces):", bg="black", fg="white", font=font_text).pack(pady=5)
hex_entry = tk.Entry(root, width=50)
hex_entry.pack(pady=5)

# Button to convert hexadecimal to text
convert_hex_button = tk.Button(root, text="Convert Hexadecimal to Text", command=hexadecimal_to_text, bg=button_color, fg=text_color)
convert_hex_button.pack(pady=5)

# Output for hexadecimal to text conversion
tk.Label(root, text="Hexadecimal to Text Result:", bg="black", fg="white", font=font_text).pack(pady=5)
text_output_text = tk.Text(root, height=5, wrap='none')  # Disable word wrap
text_output_text.pack(fill=tk.X, padx=5)
text_scrollbar_x = tk.Scrollbar(root, orient='horizontal', command=text_output_text.xview)
text_output_text.config(xscrollcommand=text_scrollbar_x.set)
text_scrollbar_x.pack(fill=tk.X)

# Button to copy text result
copy_text_button = tk.Button(root, text="Copy Text Result", command=copy_text_to_clipboard, bg="#2196F3", fg=text_color)
copy_text_button.pack(pady=5)

# Run the application
root.mainloop()
