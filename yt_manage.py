# yt name --> 30 mints
# a kind of to do list
from prettytable import PrettyTable
import json

def gether_data():
    try :
        with open('yt_data.txt', 'r') as fl:
            file_data =  json.load(fl)
            return file_data 
    
    except FileNotFoundError :
        return []

def adition_meth (videos):
    with open('yt_data.txt', 'w') as fl :
        json.dump(videos , fl)    

def list_yt_vd (videos):
    for index,video in enumerate(videos, start = 1):
        print()

    print(videos)

    tab = PrettyTable(["Name", "Time"])
    for row in videos:
        tab.add_row([row["name"], row["time"]])
    print(tab)
    
    tab = PrettyTable(("ID","Name", "Time"))
    
    for x,row in enumerate(videos, start = 1):
        tab.add_row((x,row["name"], row["time"]))
    # print(f"{tab} \t {tab1}")
    print(tab)

def add_yt_vd (videos):
    vd_name = input("Enter name of video : ")
    vd_time = input("Enter duartion of video : ")
    videos.append({'name' : vd_name , 'time' :vd_time})
    adition_meth(videos)

def update_yt_vd():
    pass
    
def delete_yt_vd():
    pass

def main():
    videos = gether_data()
    # print(videos)
    while True:
        print("\n *********** YOUTUBE MANAGER *********** \n")
        print('1. List ALL youtube video \n2. ADD youtube video \n3. UPDATE youtube video \n4. REMOVE youtube video \n5. EXIT ')
        print("\n **************************************** \n")
    
        choice = input('\nEnter your choice : ')
        
        match choice :
            case '1':
                # list all videos
                list_yt_vd(videos)

            case '2':
                # Add YT video
                add_yt_vd(videos)
                
            case '3':
                # update YT video
                update_yt_vd()
                
            case '4':
                # remove YT video
                delete_yt_vd()
                
            case '5':
                # exit
                break
                
            case _:
                print("\n INVALID CHOICE !!! ^_^ \n")

if __name__ == '__main__':
    main()