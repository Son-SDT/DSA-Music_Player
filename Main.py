import Function as fc
import os

current_path = os.path.dirname(os.path.abspath(__file__))
def get_FolderPath(name):
    return os.path.join(current_path,name)
music_path = get_FolderPath('Music')
def get_path_music(name):
    return os.path.join(music_path,name+".mp3 ")

s0_id = "DKE-VU"
s0 = fc.Song(s0_id, "Đông Kiếm em","Vũ",get_path_music(s0_id))
s1_id = "NLHBQ-VU"
s1 = fc.Song(s1_id, "Những lời hứa bỏ quên","Vũ",get_path_music(s1_id))
s2_id = "1P-ADZ"
s2 = fc.Song(s2_id, "Một phút","Andiez",get_path_music(s2_id))
s3_id = "MMSHVNM-ADZ"
s3 = fc.Song(s3_id, "Mãi mãi sẽ hết vào ngày mai","Andiez",get_path_music(s3_id))
s4_id = "BQN-VU"
s4 = fc.Song(s4_id, "Bước qua nhau","Vũ",get_path_music(s4_id))
s5_id = "ANR-VU"
s5 = fc.Song(s5_id, "Anh nhớ ra","Vũ",get_path_music(s5_id))
s6_id = "CDCDS-ADZ"
s6 = fc.Song(s6_id, "Chờ đợi có đáng sợ","Andiez",get_path_music(s6_id))
s7_id = "SNT-ADZ"
s7 = fc.Song(s7_id, "Suýt nữa thì","Andiez",get_path_music(s7_id))
s8_id = "LL-VU"
s8 = fc.Song(s8_id, "Lạ lùng","Vũ",get_path_music(s8_id))
s9_id = "test-SON"
s9 = fc.Song(s9_id, "test","Sơn",get_path_music(s9_id))





lb = fc.SongLibrary()
lb.add_song(s0)
lb.add_song(s1)
lb.add_song(s2)
lb.add_song(s3)
lb.add_song(s4)
lb.add_song(s5)
lb.add_song(s6)
lb.add_song(s7)
lb.add_song(s8)
lb.add_song(s9)


pl = fc.DoublyLinkedList()
#lb.display()