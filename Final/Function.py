
import tkinter as tk
import pygame


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

        



