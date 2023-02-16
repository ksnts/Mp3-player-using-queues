from pygame import mixer
from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("600x300")

mixer.init()

# Create an empty list to hold the songs in the queue
queue = []

def pause():
    mixer.music.pause()

def play():
    # If the queue is not empty, play the first song in the queue
    if queue:
        song_path = queue[0]
        mixer.music.load(song_path)
        mixer.music.play()
        # Remove the first song from the queue
        del queue[0]
    else:
        mixer.music.play()

def resume():
    mixer.music.unpause()

def select_song():
    song_path = filedialog.askopenfilename()
    queue.append(song_path)

def skip():
    # Stop any music that's currently playing
    mixer.music.stop()
    # If the queue is not empty, play the first song in the queue
    if queue:
        play()

def quit():
    # Stop any music that's currently playing
    mixer.music.stop()
    # Close the window
    root.destroy()

Label(root, text="Welcome to music player", font="lucidia 30 bold").pack()

Button(text="Select Song", command=select_song).place(x=150, y=100)
Button(text="Add to Queue", command=select_song).place(x=250, y=100)
Button(text="Play", command=play).place(x=310, y=100)
Button(text="Pause", command=pause).place(x=380, y=100)
Button(text="Resume", command=resume).place(x=450, y=100)
Button(text="Skip", command=skip).place(x=520, y=100)
Button(text="Quit", command=quit).place(x=570, y=100)

root.mainloop()

