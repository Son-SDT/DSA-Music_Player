

import tkinter as tk
from tkinter.ttk import Progressbar
import customtkinter as ctk
import threading
import time
import pygame
from mutagen.mp3 import MP3
import os




class Song:
    def __init__(self, ID, title, artist, filepath):
        self.ID = ID
        self.title = title
        self.artist = artist
        self.filepath = filepath

class SongLibrary:
    def __init__(self, size=10):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def add_song(self, song):
        index = self._hash(song.ID)
        for existing_song in self.hash_table[index]:
            if existing_song.ID == song.ID:
                return  # Song already exists, do not add
        self.hash_table[index].append(song)

    def remove_song(self, ID):
        index = self._hash(ID)
        for i, song in enumerate(self.hash_table[index]):
            if song.ID == ID:
                del self.hash_table[index][i]
                return

    def find_song(self, title, listbox):
        for bucket in self.hash_table:
            for song in bucket:
                if title.lower() in song.title.lower() or title.lower() in song.artist.lower():
                    listbox.insert(tk.END, f"{song.title}, {song.artist}")
                else:
                    listbox.insert(tk.END, None)

    def get_song(self, title):
        for bucket in self.hash_table:
            for song in bucket:
                if title.lower() in song.title.lower() or title.lower() in song.artist.lower():
                    return song
        return None

    def display(self):
        for bucket in self.hash_table:
            for song in bucket:
                print(f"Title: {song.title}, Artist: {song.artist}, File Path: {song.filepath}")

    def display_songs_in_listbox(self, listbox):
        listbox.delete(0, tk.END)
        for bucket in self.hash_table:
            for song in bucket:
                listbox.insert(tk.END, f"{song.title}, {song.artist}")

    def display_empty_listbox(self, listbox):
        listbox.delete(0, tk.END)
        listbox.insert(tk.END, None)
class Node:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.first = None
        self.num = 0
    def add_song(self, song):
        new_node = Node(song)
        if  self.head == None:
            self.head = self.tail = self.current = new_node
            self.first = True
        else:
            self.first = False
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.num +=1        
    def get_current(self):
        return self.current.song
    
    def current_song(self):
        return self.current.song.filepath if self.current else None
    
    def remove_song(self, song, listbox):
        if song.ID == self.current.song.ID:
            if self.current == self.head and self.current == self.tail:
                self.head = self.tail = self.current = None
                self.num = 0
                pygame.mixer.music.stop()
                listbox.delete(0, 0)
                return None
                
            else :
                if self.current.prev:
                    self.current.prev.next = self.current.next

                else :
                    self.head = self.current.next
                    self.current = self.head
                    self.num -= 1
                    pygame.mixer.music.stop()
                    listbox.delete(0, 0)
                    return None
                if self.current.next:
                    self.current.next.prev = self.current.prev

                else :
                    self.tail = self.current.prev
                    self.current = self.tail
                    
                
                if self.current != self.tail:
                    self.current = self.current.next
                
                
            self.num -= 1
            pygame.mixer.music.stop()
            listbox.delete(0, 0)
        else :   
            curr = self.head
            for i in range(self.num):
                if curr.song.ID == song.ID:
                    if curr.prev:
                        curr.prev.next = curr.next
                    else:
                        self.head = curr.next
                    if curr.next:
                        curr.next.prev = curr.prev
                    else:
                        self.tail = curr.prev
                    self.num -= 1
                    break
                curr = curr.next       
        return None
    
    def check_head(self):
        if self.first :
            return True
        else : 
            if self.current == self.head  :
                return True
            else :
                return False
            
    def check_tail(self):
        if self.first :
            return True
        else : 
            if self.current == self.tail  :
                return True
            else :
                return False
    def play_next(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.song
        return None

    def play_previous(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.song
        return None

    def start_playback(self):
        self.current.next = self.current
        

    def display_current_song(self, listbox):
        listbox.delete(0, 0)
        listbox.insert(tk.END,f"{self.current.song.title}, {self.current.song.artist}")
    
    def display_playlist(self, listbox):
        listbox.delete(0, tk.END)
        crr_song = self.head
        for i in range (self.num):
            listbox.insert(tk.END,f"{crr_song.song.title}, {crr_song.song.artist}")
            crr_song = crr_song.next


class MusicManager:
    def __init__(self):
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.music_path = os.path.join(self.current_path, 'Music')
        self.song_library = SongLibrary()
        self.playlist = DoublyLinkedList()
        self.add_song()

    def get_folder_path(self, name):
        return os.path.join(self.current_path, name)

    def get_path_music(self, ID):
        return os.path.join(self.music_path, f"{ID}.mp3")

    def add_song(self):
        list_song = os.listdir(self.music_path)
        for i in list_song :
            ID = i.split('.')[0]
            name, artist = self.get_title_artist(ID)
            path = self.get_path_music(ID)
            song = Song(ID, name, artist,path)
            self.song_library.add_song(song)

    def get_title_artist(self, id):
        artist = {
            "DKE-VU": "Vũ",
            "NLHBQ-VU": "Vũ",
            "1P-ADZ": "Andiez",
            "MMSHVNM-ADZ": "Andiez",
            "BQN-VU": "Vũ",
            "ANR-VU": "Vũ",
            "CDCDS-ADZ": "Andiez",
            "SNT-ADZ": "Andiez",
            "LL-VU": "Vũ",
            "test-SON" : "Sơn",
        }
        name ={
            "DKE-VU": "Đông kiếm em",
            "NLHBQ-VU": "Những lời hứa bỏ quên",
            "1P-ADZ": "Một phút",
            "MMSHVNM-ADZ": "Mãi mãi sẽ hết vào ngày mai",
            "BQN-VU": "Bước qua nhau",
            "ANR-VU": "Anh nhớ ra",
            "CDCDS-ADZ": "Chờ đợi có đáng sợ",
            "SNT-ADZ": "Suýt nữa thì",
            "LL-VU": "Lạ lùng",
            "test-SON" : "test",
        }
        for i in list(name.keys())  :
            if id == i  :
                return name[i], artist[i]
        return None, None
    

    def get_library(self):
        return self.song_library
    def get_playlist(self):
        return self.playlist
    
class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player App - Nguyen Hong Son - ITDSIU21117")
        self.root.geometry("700x550")
        manager = MusicManager()
        self.lb = manager.get_library()
        self.pl = manager.get_playlist()

        pygame.mixer.init()

        self.current_position = 0
        self.paused = False
        self.first = True

        self.init_ui()
        self.init_thread()

    def init_ui(self):
        # Create a label for the music player title
        self.l_music_player = tk.Label(self.root, text="Music Player", font=("TkDefaultFont", 30, "bold"))
        self.l_music_player.pack(pady=1)

        # Create the search box to search titles or artist names
        self.search_box = ctk.CTkEntry(self.root, placeholder_text="Search Song or Artist", width=350,
                                       font=("TkDefaultFont", 18))
        self.search_box.pack(pady=10)
        # Update search box 
        self.search_box.bind("<KeyRelease>", self.on_search_box_change)

        # Create a frame of listbox
        self.lbox_frame = tk.Frame(self.root)
        self.lbox_frame.pack()

        # Create frames within the main frame
        # Frame 1 la left
        self.lbox_frame1 = tk.Frame(self.lbox_frame)
        self.lbox_frame1.pack(padx=5, side=tk.LEFT, pady=20)

        self.lbox_frame11 = tk.Frame(self.lbox_frame1)
        self.lbox_frame11.pack(padx=5, side=tk.LEFT, pady=20)
        # Frame 2 la right
        self.lbox_frame2 = tk.Frame(self.lbox_frame)
        self.lbox_frame2.pack(padx=5, side=tk.LEFT, pady=20)

        # Create listboxes
        # Create a listbox11 to display the playlist
        self.lbox11 = tk.Listbox(self.lbox_frame1, width=33, height=10, font=("TkDefaultFont", 10))
        self.lbox11.pack(padx=10, pady=10)

        # Create a listbox21 to display the song library
        self.lbox21 = tk.Listbox(self.lbox_frame2, width=40, height=8, font=("TkDefaultFont", 16))
        self.lbox21.pack(padx=10, pady=10)
        # Update box sau khi search
        self.lbox21.bind("<KeyRelease>", self.on_search_box_change)

        # Create buttons to add or delete songs in the playlist
        self.btn_add = ctk.CTkButton(self.lbox_frame1, text="Add", width=5, command=lambda: self.add_selected_song(self.lbox21),
                                     font=("TkDefaultFont", 18))
        self.btn_add.pack(side=tk.LEFT, padx=5)

        self.btn_delete = ctk.CTkButton(self.lbox_frame1, text="Delete", width=5, command=lambda: self.delete_song(self.lbox21, self.lbox11),
                                        font=("TkDefaultFont", 18))
        self.btn_delete.pack(side=tk.LEFT, padx=5)

        # Create a frame to hold the control buttons
        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.pack(pady=20)

        # Create control buttons
        self.btn_previous = ctk.CTkButton(self.btn_frame, text="<", width=50, command=self.previous_song,
                                          font=("TkDefaultFont", 25))
        self.btn_previous.pack(side=tk.LEFT, padx=5)

        self.btn_play = ctk.CTkButton(self.btn_frame, text="▶", width=50, command=self.play_music,
                                      font=("TkDefaultFont", 25))
        self.btn_play.pack(side=tk.LEFT, padx=5)

        self.btn_next = ctk.CTkButton(self.btn_frame, text=">", width=50, command=self.next_song,
                                      font=("TkDefaultFont", 25))
        self.btn_next.pack(side=tk.LEFT, padx=5)

        self.crrt_song = tk.Listbox(self.root, width=33, height=1, font=("TkDefaultFont", 12, "bold"))
        self.crrt_song.pack(pady=1)

        # Create a progress bar to indicate the current song's progress
        self.pbar = Progressbar(self.root, length=300, mode="determinate")
        self.pbar.pack(pady=10)
        self.pbar["value"] = None

        self.update_lbox21()

    def init_thread(self):
        # Create a thread to update the progress bar
        self.pt = threading.Thread(target=self.update_progress)
        self.pt.daemon = True
        self.pt.start()

    # Create a thread to update the progress bar 
    # 1 bai hat chia 1000 lan r update lien tuc vao thanh pbar
    def update_progress(self):
        while True:
            if pygame.mixer.music.get_busy() and self.paused:
                self.current_position = pygame.mixer.music.get_pos() / 1000
                self.pbar["value"] = self.current_position
                # Check if the current song has reached its maximum duration
                # Co che chuyen bai sau khi het bai kkk
                if self.pbar["maximum"] - self.current_position < 0.1:
                    self.stop_music()  # Stop the music playback
                    self.pbar["value"] = 0  # Reset the pbar
                    for _ in range(1):
                        time.sleep(1.5)
                        self.pl.play_next()
                        self.play_music()
                self.root.update()
            time.sleep(0.1)

    # Create a def to add the selected song in lib to playlist
    def add_selected_song(self, lbox1):
        selected_indices = lbox1.curselection()
        if selected_indices:
            selected_song = lbox1.get(selected_indices[0])
            name = selected_song.split(",")[0]
            self.pl.add_song(self.lb.get_song(name))
            self.root.after(1, lambda: self.pl.display_playlist(self.lbox11)) # display playlist tu double linked list
            print(f"Added song: {selected_song} to the playlist")
        else:
            print("No song selected.")

    # ten nhu y nghia, create def to play the current song in the playlist
    def play_selected_song(self):
        self.current_position = 0 # tranh truong hop xoa nhac xong add vao ko chay lai tu dau
        self.pl.display_current_song(self.crrt_song)
        full_path = self.pl.current_song()
        pygame.mixer.music.load(full_path)  # Load the selected song
        pygame.mixer.music.play(start=self.current_position)  # Play the song from the current position
        self.paused = False
        audio = MP3(full_path)
        song_duration = audio.info.length
        self.pbar["maximum"] = song_duration  # Set the maximum value of the pbar to the song duration

    # A def to get back the prv song
    def previous_song(self):
        if not self.pl.check_head():
            self.pl.play_previous()
            self.play_selected_song()
            self.pbar["value"] = 0
            self.play_music()

    # A def to get the next song
    def next_song(self):
        if not self.pl.check_tail():
            self.pl.play_next()
            self.play_selected_song()
            self.pbar["value"] = 0
            self.play_music()

    # Button play, the first push will play sound, 
    # then if it is running => stop and opposites
    def play_music(self):
        if self.pl.current_song() is not None :
        
            if self.paused:
                # Pause the currently playing music 
                pygame.mixer.music.pause()
                self.paused = False
                self.first = False
                
            elif self.first == True and self.paused == False:
                # First time to play music
                self.play_selected_song()
                self.paused = True

            else:
                # If the music is paused, unpause it
                pygame.mixer.music.unpause()
                self.paused = True
        

    def stop_music(self):
        pygame.mixer.music.stop()  # Stop the currently playing music
        self.paused = False

    # A def to get the search value
    # If do not search => show normally
    # If search => Make the box empty and show the result
    def get_search_value(self):
        search_value = self.search_box.get()
        if search_value == "":
            SongLibrary.display_songs_in_listbox(self.lb, self.lbox21)
        else:
            SongLibrary.display_empty_listbox(self.lb, self.lbox21)
            SongLibrary.find_song(self.lb, search_value, self.lbox21)
        return search_value

    def on_search_box_change(self, event):
        self.search_box.after(500, self.get_search_value)

    # A def to delete the selected song in the playlist
    def delete_song(self, lbox1, lbox2):
        selected_indices1 = lbox1.curselection()
        selected_indices2 = lbox2.curselection()
        # Xoa song in lib
        if selected_indices1:
            selected_song = lbox1.get(selected_indices1[0])
            name = selected_song.split(",")[0]
            song_id = self.lb.get_song(name).ID
            print(song_id)
            self.lb.remove_song(song_id)
            self.root.after(250, self.update_lbox21)
        # Xoa song in playlist
        elif selected_indices2:
            selected_song = lbox2.get(selected_indices2[0])
            name = selected_song.split(",")[0]
            song = self.lb.get_song(name)
            curr_song = self.pl.get_current()
            self.pl.remove_song(song, self.crrt_song)
            self.pl.display_playlist(lbox2)
            try:
                if curr_song == song:
                    self.pbar["value"] = 0  # Reset the pbar
                    self.play_selected_song()
                    self.play_music()

            except:
                self.pbar["value"] = 0  # Reset the pbar
                self.first = True
                self.paused = False

    # A def to update cai khung khi search 
    def update_lbox21(self):
        self.get_search_value()


# Create the main window
window = tk.Tk()
app = MusicPlayerApp(window)
window.mainloop()
