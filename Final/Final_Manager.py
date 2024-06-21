import Function as fc
import os

class MusicManager:
    def __init__(self):
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.music_path = os.path.join(self.current_path, 'Music')
        self.song_library = []
        self.playlist = fc.DoublyLinkedList()
        self.num = 0
        self.lb = fc.SongLibrary()
        self.add_song()

    def get_folder_path(self, name):
        return os.path.join(self.current_path, name)

    def get_path_music(self, ID):
        return os.path.join(self.music_path, f"{ID}.mp3")

    def add_song(self):
        list_song = os.listdir(self.music_path)
        for i in list_song :
            ID = i.split('.')[0]
            name, artist = self.get_name(ID)
            path = self.get_path_music(ID)
            Song = fc.Song(ID, name, artist,path)
            self.lb.add_song(Song)
        


    def get_name(self, id):
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
        return self.lb
    def get_playlist(self):
        return self.playlist
    
 
