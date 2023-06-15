import os
import shutil
import threading
import tkinter as tk
from tkinter import filedialog

# Specify the source directory where the downloads are located
downloads_directory = ""

# Specify the destination directories for different file types
image_directory = ""
video_directory = ""
sound_directory = ""
other_directory = ""

def allocate_downloads():
    # Iterate over each file in the downloads directory
    for filename in os.listdir(downloads_directory):
        # Get the full path of the file
        file_path = os.path.join(downloads_directory, filename)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Get the file extension
            file_extension = os.path.splitext(filename)[1].lower()
            
            # Allocate the file to the corresponding folder based on its extension
            if file_extension in ('.jpg', '.jpeg', '.png', '.gif'):
                destination_folder = image_directory
            elif file_extension in ('.mp4', '.avi', '.mkv'):
                destination_folder = video_directory
            elif file_extension in ('.mp3', '.wav', ".flac"):
                destination_folder = sound_directory
            else:
                destination_folder = other_directory
            
            # Create the destination directory if it doesn't exist
            os.makedirs(destination_folder, exist_ok=True)
            
            # Move the file to the destination directory
            shutil.move(file_path, os.path.join(destination_folder, filename))

def select_directory(directory_var):
    directory = filedialog.askdirectory()
    directory_var.set(directory)

def start_allocation():
    global downloads_directory, image_directory, video_directory, sound_directory, other_directory

    downloads_directory = downloads_var.get()
    image_directory = image_var.get()
    video_directory = video_var.get()
    sound_directory = sound_var.get()
    other_directory = other_var.get()

    allocation_thread = threading.Thread(target=allocate_downloads)
    allocation_thread.start()

# Create the main Tkinter window
window = tk.Tk()

# Create StringVars to hold the directory paths
downloads_var = tk.StringVar()
image_var = tk.StringVar()
video_var = tk.StringVar()
sound_var = tk.StringVar()
other_var = tk.StringVar()

# Create UI components
downloads_label = tk.Label(window, text="Downloads Directory:")
downloads_entry = tk.Entry(window, textvariable=downloads_var)
downloads_button = tk.Button(window, text="Select", command=lambda: select_directory(downloads_var))

image_label = tk.Label(window, text="Image Directory:")
image_entry = tk.Entry(window, textvariable=image_var)
image_button = tk.Button(window, text="Select", command=lambda: select_directory(image_var))

video_label = tk.Label(window, text="Video Directory:")
video_entry = tk.Entry(window, textvariable=video_var)
video_button = tk.Button(window, text="Select", command=lambda: select_directory(video_var))

sound_label = tk.Label(window, text="Sound Directory:")
sound_entry = tk.Entry(window, textvariable=sound_var)
sound_button = tk.Button(window, text="Select", command=lambda: select_directory(sound_var))

other_label = tk.Label(window, text="Other Directory:")
other_entry = tk.Entry(window, textvariable=other_var)
other_button = tk.Button(window, text="Select", command=lambda: select_directory(other_var))

start_button = tk.Button(window, text="Start Allocation", command=start_allocation)

# Grid layout for UI components
downloads_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)
downloads_entry.grid(row=0, column=1,  padx=10, pady=10)
downloads_button.grid(row=0, column=2,  padx=10, pady=10)

image_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)
image_entry.grid(row=1, column=1,  padx=10, pady=10)
image_button.grid(row=1, column=2,  padx=10, pady=10)

video_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)
video_entry.grid(row=2, column=1,  padx=10, pady=10)
video_button.grid(row=2, column=2,  padx=10, pady=10)

sound_label.grid(row=3, column=0, sticky="e", padx=10, pady=10)
sound_entry.grid(row=3, column=1,  padx=10, pady=10)
sound_button.grid(row=3, column=2,  padx=10, pady=10)

other_label.grid(row=4, column=0, sticky="e", padx=10, pady=10 )
other_entry.grid(row=4, column=1,  padx=10, pady=10)
other_button.grid(row=4, column=2,  padx=10, pady=10)

start_button.grid(row=5, column=0, columnspan=3, padx=10, pady=20, sticky="we")

# Configure column and row weights for responsive resizing
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(5, weight=1)

# Configure label fonts and colors
label_font = ("Helvetica", 12, "bold")
label_color = "#333333"
downloads_label.config(font=label_font, fg=label_color)
image_label.config(font=label_font, fg=label_color)
video_label.config(font=label_font, fg=label_color)
sound_label.config(font=label_font, fg=label_color)
other_label.config(font=label_font, fg=label_color)

# Configure button colors
button_bg_color = "#4CAF50"
button_fg_color = "white"
downloads_button.config(bg=button_bg_color, fg=button_fg_color)
image_button.config(bg=button_bg_color, fg=button_fg_color)
video_button.config(bg=button_bg_color, fg=button_fg_color)
sound_button.config(bg=button_bg_color, fg=button_fg_color)
other_button.config(bg=button_bg_color, fg=button_fg_color)
start_button.config(bg="#007BFF", fg="white")

# Configure entry field styles
entry_font = ("Helvetica", 12)
entry_bg_color = "#F2F2F2"
entry_fg_color = "#333333"
entry_highlight_color = "#CCCCCC"
entry_width = 40
entry_padx = 10
entry_pady = 6

downloads_entry.config(font=entry_font, bg=entry_bg_color, fg=entry_fg_color, highlightbackground=entry_highlight_color, width=entry_width)

image_entry.config(font=entry_font, bg=entry_bg_color, fg=entry_fg_color, highlightbackground=entry_highlight_color, width=entry_width)

video_entry.config(font=entry_font, bg=entry_bg_color, fg=entry_fg_color, highlightbackground=entry_highlight_color, width=entry_width)

sound_entry.config(font=entry_font, bg=entry_bg_color, fg=entry_fg_color, highlightbackground=entry_highlight_color, width=entry_width)

other_entry.config(font=entry_font, bg=entry_bg_color, fg=entry_fg_color, highlightbackground=entry_highlight_color, width=entry_width)



# Start the Tkinter event loop
window.mainloop()
