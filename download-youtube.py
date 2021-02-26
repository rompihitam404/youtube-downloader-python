#<-- Script Download video/mp3 youtube -->
#<-- code by: rompihitam.org -->
from __future__ import unicode_literals
from pytube import YouTube 
import youtube_dl
import os, sys, time

#<-- Menampilkan menu pilihan -->
def menu():
    print("""
    \33[0;32m##################################################
    \33[0;32m##################################################
    \33[0;32m###                   \33[31;1m ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   \33[0;32m###
    \33[0;32m###\33[37;1m  ██  ██           \33[31;1m▄█      ████  ████████▄  \33[0;32m###
    \33[0;32m###\33[37;1m  ██▄▄██           \33[31;1m████  ██████  █████████  \33[0;32m###
    \33[0;32m###\33[37;1m  ▀████▀ ████ █  █ \33[31;1m████  █ ██ █ ▄▄ █  ▄▄██  \33[0;32m###
    \33[0;32m###\33[37;1m    ██   █  █ █▄▄█ \33[31;1m████  █    █ ▀▀ █  ▄▄██  \33[0;32m###
    \33[0;32m###\33[37;1m    ██   ▀▀▀▀ ▀▀▀▀ \33[31;1m▀███▄▄█▄▄▄▄█▄▄▄▄█▄▄▄▄█▀  \33[0;32m###
    \33[0;32m###                   \33[31;1m  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀    \33[0;32m###
    \33[0;32m###                              \33[37;1mDownloader!   \33[0;32m###
    \33[0;32m###          \33[37;1m<-- code by: rompihitam.org -->   \33[0;32m###
    \33[0;32m##################################################
    \33[0;32m##################################################
    \33[0;36m[+]============================================[+]
    \33[0;36m[+]===================[Menu]===================[+]
    \33[0;36m[+] \33[1;33m[1] \33[37;1mDownload youtube mp3                   \33[0;36m[+]
    \33[0;36m[+] \33[1;33m[2] \33[37;1mDownload youtube video                 \33[0;36m[+]
    \33[0;36m[+] \33[1;33m[3] \33[37;1mAbout                                  \33[0;36m[+]
    \33[0;36m[+] \33[1;33m[4] \33[37;1mExit                                   \33[0;36m[+]
    \33[0;36m[+]============================================[+]
    \33[0;36m[+]============================================[+]
    """)
    #<-- input user -->
    pilih  = input("\33[1;33m[-]\33[37;1mPilih menu --> ")
    if pilih == "1":
        print("""
        \33[0;32m##################################################
        \33[0;32m##################################################
        \33[0;32m###                   \33[31;1m ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   \33[0;32m###
        \33[0;32m###\33[37;1m  ██  ██           \33[31;1m▄█      ████  ████████▄  \33[0;32m###
        \33[0;32m###\33[37;1m  ██▄▄██           \33[31;1m████  ██████  █████████  \33[0;32m###
        \33[0;32m###\33[37;1m  ▀████▀ ████ █  █ \33[31;1m████  █ ██ █ ▄▄ █  ▄▄██  \33[0;32m###
        \33[0;32m###\33[37;1m    ██   █  █ █▄▄█ \33[31;1m████  █    █ ▀▀ █  ▄▄██  \33[0;32m###
        \33[0;32m###\33[37;1m    ██   ▀▀▀▀ ▀▀▀▀ \33[31;1m▀███▄▄█▄▄▄▄█▄▄▄▄█▄▄▄▄█▀  \33[0;32m###
        \33[0;32m###                     \33[31;1m▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀    \33[0;32m###
        \33[0;32m###                              \33[37;1mDownloader!   \33[0;32m###
        \33[0;32m###          \33[37;1m<-- code by: rompihitam.org -->   \33[0;32m###
        \33[0;32m##################################################
        \33[0;32m##################################################
        """)
        print("\33[1;33m[1] \33[37;1mDownload youtube mp3")
        class Download(object):
            def __init__(self, url):
                self.url = url
                self.save_path = os.path.join(os.path.expanduser('~'), 'Downloads')
                self.song()

            def song(self):
                opts = {
                    'Verbose' : True,
                    'fixup' : 'detect_or_warn',
                    'format' : 'bestaudio/bes',
                    'postprocessors' : [{
                        'key' : 'FFmpegExtractAudio',
                        'preferredcodec' : 'mp3',
                        'preferredquality' :'1411',
                    }],
                    'extractaudio' : True,
                    'outtmpl' : self.save_path + '/%(title)s.%(ext)s',
                    'noplaylist' : True
                }
                ydl = youtube_dl.YoutubeDL(opts)
                ydl.download([self.url])

        if __name__ == '__main__':
            url = input("\33[1;33m[-] \33[37;1mMasukkan url\n --> ")
            animation = ("|/-\\")
            for i in range(100):
                time.sleep(0.1)
                sys.stdout.write("\rSedang memulai proses download --> " + animation[i % len(animation)])
                sys.stdout.flush()
            Download(url)
            print("\n\nDownload selesai!!")
            time.sleep(1)
            menu()

    elif pilih == "2":
        print("""
        \33[0;32m##################################################
        \33[0;32m##################################################
        \33[0;32m###                   \33[31;1m ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   \33[0;32m###
        \33[0;32m###\33[37;1m  ██  ██           \33[31;1m▄█      ████  ████████▄  \33[0;32m###
        \33[0;32m###\33[37;1m  ██▄▄██           \33[31;1m████  ██████  █████████  \33[0;32m###
        \33[0;32m###\33[37;1m  ▀████▀ ████ █  █ \33[31;1m████  █ ██ █ ▄▄ █  ▄▄██  \33[0;32m###
        \33[0;32m###\33[37;1m    ██   █  █ █▄▄█ \33[31;1m████  █    █ ▀▀ █  ▄▄██  \33[0;32m###
        \33[0;32m###\33[37;1m    ██   ▀▀▀▀ ▀▀▀▀ \33[31;1m▀███▄▄█▄▄▄▄█▄▄▄▄█▄▄▄▄█▀  \33[0;32m###
        \33[0;32m###                     \33[31;1m▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀    \33[0;32m###
        \33[0;32m###                              \33[37;1mDownloader!   \33[0;32m###
        \33[0;32m###          \33[37;1m<-- code by: rompihitam.org -->   \33[0;32m###
        \33[0;32m##################################################
        \33[0;32m##################################################
        """)
        print("\33[1;33m[2] \33[37;1mDownload youtube video")
        link = input("\33[1;33m[-] \33[37;1mMasukkan url \n--> ")
        yt   = YouTube(link)
        
        #<-- Keterangan video -->
        print("Title: ", yt.title)
        print("Number of views: ", yt.views)
        print("Length of video: ", yt.length, "seconds")
        print("Description: ", yt.description)
        print("Ratings: ", yt.rating)

        #<-- Mendapatkan resolusi terbaik -->
        ys = yt.streams.get_highest_resolution()

        #<-- Memulai downloads -->
        animation = ("|/-\\")
        for i in range(100):
            time.sleep(0.1)
            sys.stdout.write("\rSedang memulai proses download -- > " + animation[i % len(animation)])
            sys.stdout.flush()

        ys.download()
        print("\n\nDownload selesai!!")
        time.sleep(1)
        menu()

    elif pilih == "4":
        print("Terimakasih telah menggunakan tools ini!")
        time.sleep(1)
        sys.exit()

    elif pilih == "3":
        print("""
        [+]============================================[+]
        [+]                   About                    [+]
        [+]============================================[+]
        [+] [-] Author      : Muhammad Reza Pahlepi    [+]
        [+] [-] Youtube     : Rompi Hitam              [+]
        [+] [-] Instagram   : reza_tinkywinky          [+]
        [+] [-] github      : github.com/rompihitam404 [+]
        [+] [-] site        : rompihitam.org           [+]
        [+]============================================[+]
        [+]============================================[+]
        """)
        back = input("\33[1;33m[99] \33[37;1mUntuk kembali --> ")
        if back == "99":
            menu()

        else:
            print("Nomor yang Anda masukkan salah!")
            time.sleep(1)
            sys.exit()

    else:
        print("Nomor yang Anda masukkan salah!")
        time.sleep(1)
        menu()

menu()
