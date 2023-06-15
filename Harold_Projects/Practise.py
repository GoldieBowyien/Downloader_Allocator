from tkinter import Tk, Entry, Button
from tkinter import ttk

# Create a Tkinter window
window = Tk()

# Create a ttk Style object
style = ttk.Style()

# Configure the style to have rounded corners
style.configure("Rounded.TEntry", borderwidth=0, relief="solid", padding=10)
style.configure("Rounded.TButton", borderwidth=0, relief="solid", padding=10)

# Create UI components with rounded corners
downloads_entry = Entry(window, style="Rounded.TEntry")
image_entry = Entry(window, style="Rounded.TEntry")
video_entry = Entry(window, style="Rounded.TEntry")
sound_entry = Entry(window, style="Rounded.TEntry")
other_entry = Entry(window, style="Rounded.TEntry")

start_button = Button(window, text="Start", style="Rounded.TButton")

# Place the UI components in the window using grid
downloads_entry.grid(row=0, column=0, padx=10, pady=10)
image_entry.grid(row=1, column=0, padx=10, pady=10)
video_entry.grid(row=2, column=0, padx=10, pady=10)
sound_entry.grid(row=3, column=0, padx=10, pady=10)
other_entry.grid(row=4, column=0, padx=10, pady=10)
start_button.grid(row=5, column=0, padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()
