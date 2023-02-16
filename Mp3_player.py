from pygame import mixer
from tkinter import *
from tkinter import filedialog
import random

root = Tk()
root.geometry("600x150")

mixer.init()

# Create an empty list to hold the songs in the queue
queue = []
song_count = 0

def pause():
    global queue
    mixer.music.pause()

def play():
    global queue, song_count
    # If the queue is not empty, play the first song in the queue
    if queue:
        song_path = queue[0]
        mixer.music.load(song_path)
        mixer.music.play()
        song_count += 1
        # Remove the first song from the queue
        del queue[0]
        # Update the label text
        song_label.config(text=f"Playing: {song_path} (song {song_count})")
    else:
        mixer.music.play()

def resume():
    global queue
    mixer.music.unpause()

def select_song():
    global queue
    song_path = filedialog.askopenfilename()
    queue.append(song_path)

def shuffle_queue():
    global queue
    random.shuffle(queue)

def skip():
    global queue
    # Stop any music that's currently playing
    mixer.music.stop()
    # If the queue is not empty, play the first song in the queue
    if queue:
        play()

def quit():
    global queue
    # Stop any music that's currently playing
    mixer.music.stop()
    # Close the window
    root.destroy()

Label(root, text="Advanced Mp3 Player", font="Poppins 30 bold").pack()
song_label = Label(root, text="", font="lucidia 12 bold")
song_label.pack()

Button(text="Select Song", command=select_song).place(x=50, y=100)
Button(text="Add to Queue", command=select_song).place(x=130, y=100)
Button(text="Play", command=play).place(x=220, y=100)
Button(text="Pause", command=pause).place(x=260, y=100)
Button(text="Resume", command=resume).place(x=310, y=100)
Button(text="Shuffle Queue", command=shuffle_queue).place(x=410, y=100)
Button(text="Skip", command=skip).place(x=370, y=100)
Button(text="Quit", command=quit).place(x=505, y=100)

root.mainloop()
