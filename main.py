import tkinter
from pytube import YouTube
import customtkinter

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        videoStream = ytObject.streams.get_highest_resolution()

        # Update the title label with video title
        title.configure(text=ytObject.title, text_color="white")

        # Update the finished label to indicate download started
        finishedLabel.configure(text="Downloading...", text_color="orange")

        # Download the video
        videoStream.download()

        # Update the finished label to indicate download completion
        finishedLabel.configure(text="Downloaded", text_color="green")
    except Exception as e:
        # Handle exceptions appropriately, for simplicity, just print the error
        finishedLabel.configure(text="Error downloading video", text_color="red")

def on_progress(stream, chunk, bytesRemaining):
    total_size = stream.filesize
    bytesDownloaded = total_size - bytesRemaining
    percentage_of_completion = int(bytesDownloaded / total_size * 100)

    # Update progress percentage label and progress bar
    progress_percentage.configure(text=f"{percentage_of_completion}%")
    progressBar.set(percentage_of_completion)

# Set the appearance mode and default color theme
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# Create the main application window
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Download")

# Create and pack the title label
title = customtkinter.CTkLabel(app, text="Insert a YouTube Link")
title.pack(padx=10, pady=10)

# Create an entry widget for the YouTube link
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finishedLabel = customtkinter.CTkLabel(app, text="")
finishedLabel.pack()

# Progress Percentage
progress_percentage = customtkinter.CTkLabel(app, text="0%")
progress_percentage.pack()

# Progress Bar
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Create a button for initiating the download
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Start the main event loop
app.mainloop()
