from tkinter import *
from PIL import Image
root = Tk()

root.title("MP3 Player")
root.geometry("500x400")

def add_song():
	pass

def add_many_songs():
	pass
#playlist box
playlist_box = Listbox(root,bg = "black" , fg = "yellow",width=60)
playlist_box.pack(pady=20)

#define button images

back_btn_img = PhotoImage(file="images/backward1.png")
forward_btn_img =PhotoImage(file = "images/forward1.png")
play_btn_img =PhotoImage(file = "images/play1.png")
pause_btn_img =PhotoImage(file = "images/pause1.png")
stop_btn_img =PhotoImage(file = "images/stop1.png")
#button frames
control_frame = Frame(root)
control_frame.pack(pady=20)
#buttons

back_button = Button(control_frame,image = back_btn_img,borderwidth= 0)
forward_button = Button(control_frame,image = forward_btn_img,borderwidth= 0)
play_button = Button(control_frame,image = play_btn_img,borderwidth= 0)
pause_button = Button(control_frame,image = pause_btn_img,borderwidth= 0)
stop_button = Button(control_frame,image = stop_btn_img,borderwidth= 0)

back_button.grid(row=0,column =0,padx = 10)
stop_button.grid(row=0,column =1,padx = 10)
forward_button.grid(row=0,column =2,padx = 10)
play_button.grid(row=0,column =3,padx = 10)
pause_button.grid(row=0,column =4,padx = 10)

#create menu
my_menu = Menu(root)
root.config(menu = my_menu)

#Create add song menu dropdown
add_song_menu = Menu(my_menu,tearoff =0)
my_menu.add_cascade(label="Add Songs",menu=add_song_menu)
#add one song to the playlist
add_song_menu.add_command(label="Add One Song To Playlist",command=add_song)
#add many songs to the playlist
add_song_menu.add_command(label="Add Many Songs To Playlist",command=add_many_songs)




root.mainloop()