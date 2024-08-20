
import tkinter as tk

# this import END that I got is supported by VScode while I was coding and got stuck which is linked with the problem the define add song(): below which I will explain

from tkinter.constants import ACTIVE, END, FALSE
import pygame

# The Mp3 file music player I learned that is new to me is filedialog which I will use down here

from tkinter import filedialog

#This is the usual section that we always have for GUI except I added a little icon next to the title

window = tk.Tk()
window.title("Porter Robinson Nurture Album")
window.iconbitmap("Mp3icon.ico")
window.geometry("1200x700")
    
# Nurture Background (Background for the music player)

bg = tk.PhotoImage(file="Porter_Robinsons_Nurture.png")
bg_label = tk.Label(window, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# I learned this command from a youtube tutorial which I will include in the bibliography below
# This would help to initialize Pygame Mixer

pygame.mixer.init()

# Functions for adding any outside songs that you like to the album (note that user need to download mp3 file and add into the Nurture Album)
# This section is really hard for where it's completely new for me to learn how to insert songs from my files into the list box
# I also learned intialdir and filetypes and askopenfile name for the user to ask the program to add song in mp3 file to the plalist which is fron the same youtube tutorial (cite is provided below the program)

def add_song():

    song = filedialog.askopenfilename(initialdir='Nurture Album/', title='choose your songs', filetypes=(("mp3 Files", "*.mp3"), ))
    
    # However in here as I ran the program and it shows all of the path of the song's file in my pc so I have to cut until it only shows the song's name
    # I learned cutting the songs' names from the code.my youtube tutorial in lecture #87 which I will include in bibliography
    # Please note that this is my computer path for the music file which can be different when compare to your computer path
    
    song = song.replace("C:/Users/Dempsey/Downloads/CSULA Classes/CS 1010/GUI Project/Nurture Album/", "")
    song = song.replace(".mp3", "")
    
    # Finally with these two lines of 30 and 31, it will help to cut out file names and the .mp3 and giving just the name of the song
    # I put "END" here because I want every new songs that is selected to be at the end of the list (as the command at the beginning explanation)
    
    Nurture_album.insert(END, song)
    
 # I Defined the play button here in order for the song to actually play when clicking on it

def play():
    
    song = Nurture_album.get(ACTIVE)
    
    # "ACTIVE" help the program to play the song when it is cliked or hightlighted on the list box
    
    song = f"C:/Users/Dempsey/Downloads/CSULA Classes/CS 1010/GUI Project/Nurture Album/{song}.mp3"
    
    # I have to put the path of the file back here for the program in order to regconize the song and start playing it without showing the whole path file in the song's name
    # Here is when Pygame will actually help the program to load the music and the specific songs
    # I also learned this from the same youtube turorial that I've been researching
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

# This here will be the define section for the stop button for the user to stop the music and the song that is playing

def stop():

    pygame.mixer.music.stop()

    #This selection_clear command would help to clear the song that is "ACTIVE" or playing as defined above
    
    Nurture_album.selection_clear(ACTIVE)

# Global Pause Varible
# I learned that this global pause would help inside and outside of the function programs
# Since the prorgram first running, the songs are not paused so give it a false would help the program to regconize the pause command
# I will also include the Pause button functions sources that I learned at the end of the program

global paused
paused = False

# Pause button function will be here, it will also unpause if the button is clicked one more time

def pause(is_paused):

    global paused
    paused = is_paused
    
    # This is really confusing and tricky for as trying to make the pause and unpause command since Making it become a false and true meaning to workout.
    # In here an if-else statement would help because if pause is true, it will pause, if pause is false it will unpause.
    
    if paused:
        # Unpause function
        pygame.mixer.music.unpause()
        paused = False
    else:
        # Pause function
        pygame.mixer.music.pause()
        paused = True

    # What I learned here is that I have to tried to make the program think that it is false when it's paused and true when it's unpaused where it would help to pause and unpause the music.

# This will be the function for forwarding to the next songs in the playlist

def skip_song():
    
    # the curselection helps the program to get the current song in the album listbox
    
    next_song = Nurture_album.curselection()
    
    # this here is where I learned from assignments of for-loops lab and also from the youtube tutorial to make the program skip songs based on number.
    
    next_song = next_song[0]+1
    song = Nurture_album.get(next_song)
    
    # I pasted the computer path of the song down here again for the program to know the song's title
    
    song = f"C:/Users/Dempsey/Downloads/CSULA Classes/CS 1010/GUI Project/Nurture Album/{song}.mp3"
    
    #Loading songs after structuring the song's title
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Here I have a problem where the song already moved on to the next one but the selection is still in the previous song
    # Which causing the program to move forward to only one next song and can't move on to two or three other next songs
    # The goal now is to move the bar forward to next song that is playing
    
    Nurture_album.selection_clear(0, END)
    
    # Here I was trying make the new song activates
    
    Nurture_album.activate(next_song)
    Nurture_album.selection_set(next_song, last=None)
    
    # with the last=None I was researching and learned from codemy which will be include in the citations

# This section will be about moving the song back to the previous songs
# For this section, all I did was doing the same thing from the forwarding songs section above but instead adding(+1), I use subtract(-1)

def past_song():
    next_song = Nurture_album.curselection()
    next_song = next_song[0]-1
    song = Nurture_album.get(next_song)
    song = f"C:/Users/Dempsey/Downloads/CSULA Classes/CS 1010/GUI Project/Nurture Album/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    Nurture_album.selection_clear(0, END)
    Nurture_album.activate(next_song)
    Nurture_album.selection_set(next_song, last=None)


# This is the Playlist box (I learned from listbox in widget assignments)

Nurture_album = tk.Listbox(window,selectmode=tk.SINGLE, bg="AntiqueWhite",fg="black", font=("Times New Roman", 16), width=100, height=15)
Nurture_album.insert(1,"Blossom")
Nurture_album.insert(2,"do-re-mi-fa-so-la-ti-do")
Nurture_album.insert(3,"dullscythe")
Nurture_album.insert(4,"Get Your Wish")
Nurture_album.insert(5,"Lifelike")
Nurture_album.insert(6,"Look at the Sky")
Nurture_album.insert(7,"Mirror")
Nurture_album.insert(8,"Mother")
Nurture_album.insert(9,"Musician")
Nurture_album.insert(10,"Something Comforting")
Nurture_album.insert(11,"Sweet Time")
Nurture_album.insert(12,"Trying to Feel Alive")
Nurture_album.insert(13,"Unfold")
Nurture_album.insert(14,"Wind Tempos")
Nurture_album.pack(pady=60)

# These are the pictures of the control buttons for adjusting songs
# I defined these pictures for the buttons here which I downloaded these images from the citations below

forward_button_pictures = tk.PhotoImage(file="Skip-forward.png")
backward_button_pictures = tk.PhotoImage(file="Skip-backward.png")
pause_button_pictures = tk.PhotoImage(file="Pause.png")
play_button_pictures = tk.PhotoImage(file="Play.png")
stop_button_pictures = tk.PhotoImage(file="Stop.png")


# Player Control Frame

frame_control = tk.Frame(window)
frame_control.pack()

# Button Creation for the Player Control Buttons 

forward_button = tk.Button(frame_control, image=forward_button_pictures, borderwidth=0, command = skip_song)
backward_button = tk.Button(frame_control, image=backward_button_pictures, borderwidth=0, command = past_song)
pause_button = tk.Button(frame_control, image=pause_button_pictures, borderwidth=0, command = lambda: pause(paused)) # I learn that in tkinter whenever we need to pass in things into command button we need to have lambda so I used it here from what I learned (pause tutorial tkinter)
play_button = tk.Button(frame_control, image=play_button_pictures, borderwidth=0, command = play)
stop_button = tk.Button(frame_control, image=stop_button_pictures, borderwidth=0, command = stop)

forward_button.grid(row=0, column=3, padx=20)
backward_button.grid(row=0, column=1, padx=20)
pause_button.grid(row=0, column=2, padx=20)
play_button.grid(row=0, column=0, padx=20)
stop_button.grid(row=0, column=4, padx=20)

#This will be the album songs menu

Nurture_menu = tk.Menu(window)
window.config(menu=Nurture_menu)

# Songs Adding for the user

add_Nurture_songs = tk.Menu(Nurture_menu)
Nurture_menu.add_cascade(label="Add Songs", menu=add_Nurture_songs)
add_Nurture_songs.add_command(label="Add any songs you like to the playlist", command = add_song)

window.mainloop()

# Bibliography

# Icons:
#https://icon-icons.com/icon/music/31107
#https://icon-icons.com/icon/skip-forward/25033
#https://icon-icons.com/icon/skip-backward/25034
#https://icon-icons.com/icon/pause/25040
#https://icon-icons.com/icon/stop/25030
#https://icon-icons.com/icon/play/25038

# Color Background for listbox tkinter:
#http://cs111.wellesley.edu/~cs111/archive/cs111_spring15/public_html/labs/lab12/tkintercolor.html

# Citations and all the credits towarding for the learning sources throughout the project:

# Pygame setup for Python Tutorial:
#https://www.youtube.com/watch?v=EKjALzLLgVs

# Using Images for tkinter Background:
#https://www.youtube.com/watch?v=WurCpmHtQc4

# All of the sources credits for making music player down here is from Code.my

# Build music on GUI, play and stop buttons ideas:
#https://www.youtube.com/watch?v=djDcVWbEYoE&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=86
#https://www.youtube.com/watch?v=88IJCBKlAPA&t=154s

#Buttons for pause, backward and forward buttons ideas:
#https://www.youtube.com/watch?v=xknYbrbdKnA&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=88
#https://www.youtube.com/watch?v=dCXKxgj70R0&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=89

# Porter Robinson's Music and his "Nurture" Album:
#https://porterrobinson.com/
#https://www.youtube.com/watch?v=cAJ4FOZWTRM&list=PLfiMjLyNWxeZdzg5XuoPAggaPJu_TYf_6


# Finally, I want to say that I am really thankful for this project and all of the credits and sources that I've been learning from
# And I'm also grateful for Professor Richard and David who have been teaching and giving me this project in this semester for Computer Science.
# As this project is really meaningful to me since I got to do what I love and express my taste of music from my favorite musician.
# I wish everyone a Merry Christmas and Happy New Year :D!

# please click 'run code' or 'debug python file' if 'run python file' doesn't work

