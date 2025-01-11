import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from typing import List
import random
#My name is Bryant Munyao

# User Information
USERNAME = "MusicFan'03"
PASSWORD = "hunter1"
users_playlists = [2019386, 5343409, 9082438]
subscriber_count = 10

# Dictionaries
playlist_id_to_video_list = {
    2019386: [5390161, 7736243, 8267507, 4922599, 4559658, 9897626, 1461025, 7434914, 6093037, 6438692, 8117542, 
              5746821, 9566779, 5718817, 2459304, 5610524, 6980497, 4547223, 9086699],
    5343409: [3720918, 6382983, 1012930, 1109274, 2981023, 7394792],
    9082438: [6382983, 2981023, 9086699]
}
playlist_id_to_title = {2019386: "Top Hits", 5343409: "Top 2010s", 9082438: "My Mix"}
video_id_to_title = {
    5390161: "Who Want Smoke", 7736243: "INDUSTRY BABY", 8267507: "STAY", 1012930: "Style", 1109274: "bad guy",
    2981023: "Blank Space", 4922599: "Love Nwantiti Remix", 4559658: "Essence (Official Video)", 9897626: "Pepas",
    5610524: "Outside (Better Days)", 6980497: "Lo Siento BB:/", 4547223: "Face Off", 9086699: "Heat Waves",
    3720918: "Despacito", 1461025: "Fancy Like", 7434914: "Way 2 Sexy", 6093037: "Corta Venas", 6438692: "Need to Know",
    8117542: "MONEY", 5746821: "Wild Side", 9566779: "Knife Talk", 5718817: "Save Your Tears", 2459304: "Ghost",
    6382983: "Love Yourself", 7394792: "7 rings"
}

# Utility Functions
def get_shuffled_playlist(video_list: List[int]) -> List[int]:
    shuffled_playlist = video_list[:]
    random.shuffle(shuffled_playlist)
    return shuffled_playlist

# GUI Functions
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == USERNAME and password == PASSWORD:
        login_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)
        show_homepage()
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")

def show_homepage():
    homepage_label.config(text=f"Welcome, {USERNAME}!\n{subscriber_count} Subscribers")
    playlist_listbox.delete(0, tk.END)
    for playlist_id in users_playlists:
        title = playlist_id_to_title[playlist_id]
        count = len(playlist_id_to_video_list[playlist_id])
        playlist_listbox.insert(tk.END, f"{title} ({count} videos)")

def display_playlist(event):
    selected = playlist_listbox.curselection()
    if not selected:
        return
    index = selected[0]
    playlist_id = users_playlists[index]
    videos = playlist_id_to_video_list[playlist_id]
    playlist_title = playlist_id_to_title[playlist_id]
    video_titles = [video_id_to_title[vid] for vid in videos]
    video_listbox.delete(0, tk.END)
    playlist_label.config(text=playlist_title)
    for title in video_titles:
        video_listbox.insert(tk.END, title)

def shuffle_playlist():
    selected = playlist_listbox.curselection()
    if not selected:
        messagebox.showwarning("No Playlist Selected", "Please select a playlist.")
        return
    index = selected[0]
    playlist_id = users_playlists[index]
    videos = get_shuffled_playlist(playlist_id_to_video_list[playlist_id])
    playlist_id_to_video_list[playlist_id] = videos
    display_playlist(None)

# GUI Setup
root = tk.Tk()
root.title("YouTube Playlist Manager")
root.geometry("800x600")

# Frames
login_frame = tk.Frame(root)
main_frame = tk.Frame(root)

# Login Frame
tk.Label(login_frame, text="YouTube", font=("Arial", 24)).pack(pady=20)
tk.Label(login_frame, text="Username:").pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()
tk.Label(login_frame, text="Password:").pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()
tk.Button(login_frame, text="Login", command=login).pack(pady=10)

login_frame.pack(fill="both", expand=True)

# Main Layout
# Sidebar
sidebar = tk.Frame(main_frame, bg="#808080", width=200) 
sidebar.pack(side="left", fill="y")

tk.Label(sidebar, text="Playlists", bg="#000000", font=("Arial", 14)).pack(pady=10)
playlist_listbox = tk.Listbox(sidebar)
playlist_listbox.pack(fill="both", expand=True, padx=10, pady=10)
playlist_listbox.bind("<<ListboxSelect>>", display_playlist)

# Content Area
content = tk.Frame(main_frame)
content.pack(side="right", fill="both", expand=True)

homepage_label = tk.Label(content, text="", font=("Arial", 18))
homepage_label.pack(pady=10)

playlist_label = tk.Label(content, text="", font=("Arial", 16), fg="blue")
playlist_label.pack()

video_listbox = tk.Listbox(content, height=20)
video_listbox.pack(fill="both", expand=True, padx=10, pady=10)

action_frame = tk.Frame(content)
action_frame.pack(pady=10)
tk.Button(action_frame, text="Shuffle Playlist", command=shuffle_playlist).pack(side="left", padx=5)

root.mainloop()
