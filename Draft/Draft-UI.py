import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
import customtkinter as ctk
from mutagen.mp3 import MP3
import threading
import pygame
import time
import os
import Function as fc
import Draft_Manager as m


# Initialize pygame mixer
pygame.mixer.init()

# Store the current position of the music
current_position = 0
paused = False
def update_progress():
    global current_position, pbar
    while True:
        if pygame.mixer.music.get_busy() and paused:
            current_position = pygame.mixer.music.get_pos() / 1000
            pbar["value"] = current_position
            # Check if the current song has reached its maximum duration
            if pbar["maximum"] - current_position < 0.1:
                stop_music() # Stop the music playback
                pbar["value"] = 0 # Reset the pbar
                for i in range (1):
                    time.sleep(1.5)
                    m.pl.play_next()
                    play_music()
            window.update() 
        time.sleep(0.1)

# Create a thread to update the progress bar
pt = threading.Thread(target=update_progress)
pt.daemon = True
pt.start()

def add_selected_song(lbox1, lbox2):
    global current_position, paused
    
    # Get the selected index
    selected_indices = lbox1.curselection()
    
    if selected_indices:
        # Get the selected song
        selected_song = lbox1.get(selected_indices[0])
        
        name = selected_song.split(",")[0]
        
        # Add the song to the playlist
        m.pl.add_song(m.lb.get_song(name), lbox2)
        window.after(1, m.pl.display_playlist(lbox11) 
)

        print(f"Added song: {selected_song} to the playlist")
    else:
        print("No song selected.")

def play_selected_song():
    current_position = 0 # tranh truong hop xoa nhac xong add vao ko chay lai tu dau

    m.pl.display_current_song(crrt_song)
    full_path = m.pl.current_song()
    pygame.mixer.music.load(full_path) # Load the selected song
    pygame.mixer.music.play(start=current_position) # Play the song from the current position
    paused = False
    audio = MP3(full_path)
    song_duration = audio.info.length
    pbar["maximum"] = song_duration # Set the maximum value of the pbar  to the song duration
       
def previous_song():
    if m.pl.check_head() == False:
        m.pl.play_previous()
        play_selected_song()

def next_song():
    if m.pl.check_tail() == False:
        m.pl.play_next()
        play_selected_song()

first = True
def play_music():
    global paused,first
    if m.pl.current_song() is not None :
        
        if paused:
            # Pause the currently playing music 
            pygame.mixer.music.pause()
            paused = False
            first = False
            
        elif first == True and paused == False:
            # If the music is not paused, play the selected song
            play_selected_song()
            paused = True

        else:
            # If the music is paused, unpause it
            pygame.mixer.music.unpause()
            paused = True
               
def stop_music():
    global paused
    # Stop the currently playing music and reset the progress bar
    pygame.mixer.music.stop()
    paused = False

# refresh the available music list
def get_search_value():
    search_value = search_box.get()
    if search_value =="":
        fc.SongLibrary.display_songs_in_listbox(m.lb, lbox21)
    else :
        fc.SongLibrary.display_empty_listbox(m.lb, lbox21)
        fc.SongLibrary.find_song(m.lb, search_value , lbox21)
    return search_value
    
#set time to refresh
def on_search_box_change(event):
    search_box.after(500, get_search_value)

def delete_song(lbox1, lbox2):
    global paused,first

    selected_indices1 = lbox1.curselection()
    selected_indices2 = lbox2.curselection()
    if selected_indices1:
        # Get the selected song
        selected_song = lbox1.get(selected_indices1[0])    
        name = selected_song.split(",")[0]
        id = m.lb.get_song(name).ID
        print(id)
        m.lb.remove_song(id)
        window.after(250, update_lbox21)
    elif selected_indices2 : 
        selected_song = lbox2.get(selected_indices2[0])
        name = selected_song.split(",")[0]
        song = m.lb.get_song(name)
        curr_song = m.pl.get_current()
        m.pl.remove_song(song,crrt_song)
        m.pl.display_playlist(lbox2)
        try :
            if curr_song == song :
                pbar["value"] = 0 # Reset the pbar
                play_selected_song()
            
        except:
            pbar["value"] = 0 # Reset the pbar
            first = True 
            paused = False

# Create the main window
window = tk.Tk()
window.title("Music Player App - Nguyen Hong Son - ITDSIU21117")
window.geometry("700x550")

# Create a label for the music player title
l_music_player = tk.Label(window, text="Music Player", font=("TkDefaultFont", 30, "bold"))
l_music_player.pack(pady=1)

#Create the search box to search titles or artist names
search_box = ctk.CTkEntry(window, placeholder_text="Search Song or Artist",  width=350,
                         font=("TkDefaultFont", 18))
search_box.pack(pady=10)

# Bind the `on_search_box_change` function to the `<KeyRelease>` event
search_box.bind("<KeyRelease>", on_search_box_change)

# Create a frame of listbox
lbox_frame = tk.Frame(window)
lbox_frame.pack()

# Create a frame of listbox1
lbox_frame1 = tk.Frame(lbox_frame)
lbox_frame1.pack(padx = 5, side = tk.LEFT, pady=20)

# Create a frame of listbox11
lbox_frame11 = tk.Frame(lbox_frame1)
lbox_frame11.pack(padx = 5, side = tk.LEFT, pady=20)

# Create a frame of listbox2
lbox_frame2 = tk.Frame(lbox_frame)
lbox_frame2.pack(padx = 5, side = tk.LEFT, pady=20)

# Create a listbox11 to display the playlist
lbox11 = tk.Listbox(lbox_frame1, width=33, height= 10, font=("TkDefaultFont", 10))
lbox11.pack(padx = 10, pady=10)

# Create a listbox21 to display the available songs
lbox21 = tk.Listbox(lbox_frame2, width=40, height= 8, font=("TkDefaultFont", 16))
lbox21.pack(padx = 10, pady=10)
lbox21.bind("<KeyRelease>", on_search_box_change)

# Create a button to add or delete song in playlist 
btn_add = ctk.CTkButton(lbox_frame1, text="Add",  width=5, command=lambda: add_selected_song (lbox21,lbox11),
                         font=("TkDefaultFont", 18))
btn_add.pack(side=tk.LEFT, padx=5)

btn_delete = ctk.CTkButton(lbox_frame1, text="Delete",  width=5, command= lambda: delete_song(lbox21,lbox11),
                         font=("TkDefaultFont", 18))
btn_delete.pack(side=tk.LEFT, padx=5)

# Create a frame to hold the control buttons
btn_frame = tk.Frame(window)
btn_frame.pack(pady=20)

# Create a button to go to the previous song
btn_previous = ctk.CTkButton(btn_frame, text="<", width=50, command= previous_song, 
                            font=("TkDefaultFont", 25))
btn_previous.pack(side=tk.LEFT, padx=5)

# Create a button to play the music
btn_play = ctk.CTkButton(btn_frame, text="▶",  width=50, command= play_music,
                         font=("TkDefaultFont", 25))
btn_play.pack(side=tk.LEFT, padx=5)

# Create a button to go to the next song
btn_next = ctk.CTkButton(btn_frame, text=">",  width=50, command= next_song,
                         font=("TkDefaultFont", 25))
btn_next.pack(side=tk.LEFT, padx=5)

crrt_song = tk.Listbox(window,width= 33, height=1, font=("TkDefaultFont", 12, "bold"))
crrt_song.pack(pady=1)

# Create a progress bar to indicate the current song's progress
pbar = Progressbar(window, length=300, mode="determinate")
pbar.pack(pady=10)
pbar["value"] = None

def update_lbox21():
    get_search_value()
window.after(250, update_lbox21)
window.mainloop()




