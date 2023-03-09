from typing import List
from random import randint
import random
# My name: Bryant Munyao


# User Information
USERNAME = "MusicFan'03"
PASSWORD = "hunter1"
users_playlists = [2019386, 5343409, 9082438]
subscriber_count = 10

# Site Policies
MAX_PASSWORD_ATTEMPTS_ALLOWED = 3
MAX_VIDEOS_OUTPUTTED_AT_ONCE = 5

users_playlists = [2019386, 5343409, 9082438]
top_hits_playlist = [5390161, 7736243, 8267507, 4922599, 4559658, 9897626, 1461025, 7434914, 6093037, 6438692, 8117542, 
5746821, 9566779, 5718817, 2459304, 5610524, 6980497, 4547223, 9086699]
top_2010s_playlist = [3720918, 6382983, 1012930, 1109274, 2981023, 7394792]
my_mix = [6382983, 2981023, 9086699]

# Dictionaries
playlist_id_to_video_list = {2019386 : top_hits_playlist, 5343409: top_2010s_playlist, 9082438: my_mix}
playlist_id_to_title = {2019386 : "Top Hits", 5343409: "Top 2010s", 9082438: "My Mix"}
playlist_title_to_id = {"Top Hits": 2019386, "Top 2010s": 5343409, "My Mix": 9082438}

# Videos (key = Video ID, value = Video Title)
video_id_to_title = {
5390161 : "Who Want Smoke",
7736243 : "INDUSTRY BABY",
8267507 : "STAY",
1012930 : "Style",
1109274 : "bad guy",
2981023 : "Blank Space",
4922599 : "Love Nwantiti Remix",
4559658 : "Essence (Official Video)",
9897626 : "Pepas",
5610524 : "Outside (Better Days)",
6980497 : "Lo Siento BB:/",
4547223 : "Face Off",
9086699 : "Heat Waves",
3720918 : "Despacito",
9086691 : "Royals",
1461025 : "Fancy Like",
7434914 : "Way 2 Sexy",
6093037 : "Corta Venas",
6438692 : "Need to Know",
8117542 : "MONEY",
5746821 : "Wild Side ",
9566779 : "Knife Talk",
1683724 : "Life Support",
5718817 : "Save Your Tears",
2459304 : "Ghost",
6382983 : "Love Yourself",
7394792 : "7 rings",
}

# Playlists (in the form of lists of video IDs)
def get_shuffled_playlist(video_list: List[int]) -> List[int]:
    shuffled_playlist = random.shuffle(video_list)
    return shuffled_playlist


def display_full_playlist(playlist_id: int) -> None:
    keep_track_of_songs_in_playlist = 0
    output_playlist = True
    song_playlist = playlist_id_to_video_list[playlist_id]
    print("*" * len(playlist_id_to_title[playlist_id]))
    print(playlist_id_to_title[playlist_id])
    print("*" * len(playlist_id_to_title[playlist_id]))
    while output_playlist is True:
        if len(song_playlist) - keep_track_of_songs_in_playlist > MAX_VIDEOS_OUTPUTTED_AT_ONCE:
            for x in range(MAX_VIDEOS_OUTPUTTED_AT_ONCE):
                print(video_id_to_title[song_playlist[keep_track_of_songs_in_playlist]]) 
                keep_track_of_songs_in_playlist += 1
            question = input("...Do you want to see more? ")
            if question == "no":
                output_playlist is False
                break
            elif question == "yes":
                continue
            else:
                print('Error.')
                break
        else:
            for x in range(len(song_playlist) - keep_track_of_songs_in_playlist):
                print(video_id_to_title[song_playlist[keep_track_of_songs_in_playlist]])
                keep_track_of_songs_in_playlist += 1
                output_playlist = False

# This prints out a playlist title and video count.
def display_playlist_preview(playlist_id: int) -> None:
    print(playlist_id_to_title[playlist_id])
    print(len(playlist_id_to_video_list[playlist_id]), "videos")


# Tip: Call display_playlist_preview from this, for each playlist.
def display_personal_homepage() -> None:
    print('{}'.format(USERNAME))
    print('{} subscribers'.format(subscriber_count))
    print()
    for playlist_title in users_playlists:
        display_playlist_preview(playlist_title)
        print()


def do_playlist_action(playlist_id: int, choice: int) -> None:
    global action_1,action_2
    action_1 = 1
    action_2 = 2
    song_playlist = playlist_id_to_video_list[playlist_id]
    if playlist_id in users_playlists:
        if choice == action_1:
            get_shuffled_playlist(song_playlist)
        elif choice == action_2:
            if len(song_playlist) > 0:
                song_playlist.remove(song_playlist[0]) 
            if len(playlist_id_to_video_list[playlist_id]) == 0:
                del song_playlist
                playlist_title_to_id.pop(playlist_id_to_title[playlist_id])
                playlist_id_to_video_list.pop(playlist_id, None)


        

def main_playlist_interface() -> None:
    user_option = 0
    action_4 = 4
    while user_option != action_4:
        user_choice = input('Which playlist do you want to see? ')
        if user_choice in playlist_title_to_id:
            playlist_id = playlist_title_to_id[user_choice]
            display_full_playlist(playlist_id)
            user_option = int(input('Actions: 1 for shuffle, 2 for shorten, 4 for exit. '))
            do_playlist_action(playlist_id, user_option)
            if user_option != action_1 and user_option != action_2 and user_option != action_4:
                print('Error.')
                break
            if user_option == action_4:
                break
        else:
            print('Error.')
            break

            

# This asks the user for their username and password, and returns whether the login is successful.
def user_login() -> bool:
    if login_username == USERNAME and login_password == PASSWORD:
        return True
        display_personal_homepage()
        main_playlist_interface()
    else:
        return False

#####################################################
print("> YouTube")
successful_login = False


attempts = 1 
while attempts <= MAX_PASSWORD_ATTEMPTS_ALLOWED:     
    login_username = input("Username: ")     
    login_password = input("Password: ")     
    user_login()     
    if user_login() == True:         
        attempts = MAX_PASSWORD_ATTEMPTS_ALLOWED + 1 
        successful_login = user_login
    elif user_login() == False and attempts <= 2:         
        print("Try again.")      
    else:         
        print("Access Denied.")     
    attempts += 1
        

    #############
if successful_login:
    print(len(USERNAME) * '*')
    display_personal_homepage()
    main_playlist_interface()
