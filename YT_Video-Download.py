# By: Aidan Biggs
# AKA AT Vloggers
#
# Please do not claim this as your own.
#
# If you remove this it means you break the Code of Use found here:
# https://at-vloggers.weebly.com/code-of-use.html


# Import pytube, system, tkinter, and time
from pytube import YouTube
import sys
from tkinter import messagebox
import time

# Note: print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") is equivalent to screen clear
# WARNING: REQUIRES THAT YOU HAVE pytube AND tkinter!!

# Asks if user agrees to Code of Use
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("=================")
print("  YouTube Video")
print("    Downloader")
print(" By: Aidan Biggs")
print(" AKA AT Vloggers")
print("=================")
print("")
print("Code of Use:\n")
print("You may only use this if you give proper credit to the owner of the project: AIDAN BIGGS")
print("Please don't be that guy that no one likes who always steals everyone's work.")
print("DO NOT CLAIM AS ONES OWN!!")
print("By typing 1(yes), you agree to not claim this project as your own.")
print("")
print("If you find any of my code without the Code of Use, contact me at atvloggers.video@gmail.com")
print("\nNOTE: Program will exit if you do not except!")
print("Do you agree to the Code of Use?")
print("\n1 = YES\n2 = NO\n")
cou = int(input("1 or 2: "))
if cou == 2:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("=================")
    print("  YouTube Video")
    print("    Downloader")
    print(" By: Aidan Biggs")
    print(" AKA AT Vloggers")
    print("=================")
    print("")
    print("EXITING..")
    sys.exit()

# Sets video ID as variable
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("=================")
print("  YouTube Video")
print("    Downloader")
print(" By: Aidan Biggs")
print(" AKA AT Vloggers")
print("=================")
print("")
print("Video ID is https://www.youtube.com/watch?v=kEK_6dh2EIg")
print("                                            ^^^^^^^^^^^")
print("                                             This part")
print("\n\n\n")
ytho = str(input("Video ID: "))
yt = YouTube("https://www.youtube.com/watch?v="+ytho)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("=================")
print("  YouTube Video")
print("    Downloader")
print(" By: Aidan Biggs")
print(" AKA AT Vloggers")
print("=================")
print("")
print("Show mp4 files only?")
print("\n1 = yes\n2 = no\n")
mponly = int(input("1 or 2: "))
if mponly == 1:
    streams = yt.streams.filter(progressive=True, file_extension='mp4').all()
else:
    streams = yt.streams.filter(progressive=True).all()


# Gets export options
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("=================")
print("  YouTube Video")
print("    Downloader")
print(" By: Aidan Biggs")
print(" AKA AT Vloggers")
print("=================")
print("")
l = 1
for v in streams:
    print("\n#"+str(l)+" "+str(v))
    l += 1

# Sets export number as variable
n = int(input("Export option: "))
dvid = streams[n-1]

# Sets file destination as variable
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("=================")
print("  YouTube Video")
print("    Downloader")
print(" By: Aidan Biggs")
print(" AKA AT Vloggers")
print("=================")
print("")
destination = str(input("Enter video save destination: "))
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("D")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("DO")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("DOW")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("DOWN")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("DOWNL")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("DOWNLO")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("DOWNLOA")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("DOWNLOAD")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("DOWNLOADI")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("DOWNLOADIN")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("DOWNLOADING")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("DOWNLOADING.")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("DOWNLOADING..")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("DOWNLOADING...")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("DOWNLOADING....")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("DOWNLOADING.....")
dvid.download(destination)

# Displays success info
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("=================")
print("  YouTube Video")
print("    Downloader")
print(" By: Aidan Biggs")
print(" AKA AT Vloggers")
print("=================")
print("")
print("Downloaded:\n"+yt.title+"\n\nThumbnail:\n"+yt.thumbnail_url+"\n\nDescription:\n"+yt.description+"\n\nLength(sec):\n"+yt.length)
messagebox.showinfo("DOWNLOAD COMPLETE", "============\n  YouTube Video  \n    Downloader \n By: Aidan Biggs \n AKA AT Vloggers \n============\n\nDownloaded:\n"+yt.title+"\n\nThumbnail:\n"+yt.thumbnail_url)