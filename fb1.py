# This has all the user needs in using the program
import requests
from facebook import Message, Client, ThreadType
import threading
import json
import time
import sys
import os

class SpamBot:
    def __init__(self):
        print("--- Welcome to FacebookSpam ---")
        # login
        token_path = str(input("Token File: "))
        file = open(token_path,"r")
        token = json.load(file)
        self.client = Client(token)
        # config
        self.config = {"msgFriends":False,
                       "msgGroups":False,
                       "multipleFriends":False,
                       "name":False,
                       "namelist":[],
                       "id":False,
                       "idlist":[],
                       "messageFile":[],
                       "repeat":1,
                       "delay":0}
        # get profile info
        uid = token.get("c_user")
        user = self.client.fetchUserInfo(uid)[uid]
        print(f"Succesfully logged in Profile Name: {user.name}")

        # options start
        self.StartOptions()
        self.SecondOptions()
        self.getPrompt()
        if self.config["name"]:
            self.searchName()
        else:
            self.searchID()

        # spam start
        threads = []
        if self.config["name"]:
            for user in self.config["namelist"]:
                threads.append(threading.Thread(target=self.spam_mesage, args=([user])))
                if not self.config["multipleFriends"]:
                    self.spam_mesage(user)
        else:
            for id in self.config["idlist"]:
                threads.append(threading.Thread(target=self.spam_mesage, args=([user])))
                if not self.config["multipleFriends"]:
                    self.spam_mesage(id)
        if self.config["multipleFriends"]:
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
        sys.exit("PROGRAM COMPLETE")

    # start option
    def StartOptions(self):
        print("1. Send Message to Friend")
        print("2. Send in Group")
        print("3. Multiple Friends ( Threading )")
        while True:
            chosen = str(input("choose: "))
            if chosen.isdigit():
                chosen = int(chosen)
                if chosen > 0 and chosen <= 3:
                    break
        self.config["msgFriends"] = True if chosen == 1 else False
        self.config["msgGroups"] = True if chosen == 2 else False
        self.config["multipleFriends"] = True if chosen == 3 else False

    # second option
    def SecondOptions(self):
        print("1. Through Name")
        print("2. Through Conversation ID")
        while True:
            chosen = str(input("choose: "))
            if chosen.isdigit():
                chosen = int(chosen)
                if chosen > 0 and chosen <= 2:
                    break
        self.config["name"] = True if chosen == 1 else False
        self.config["id"] = True if chosen == 2 else False

    # third option
    def getPrompt(self):
        while True: # get message
            message_path = str(input("Select your msg File: "))
            if os.path.isfile(message_path):
                file = open(message_path,"r").read().split("\n")
                for text in file:
                    self.config["messageFile"].append(text)
                break
            else:
                print("File not in path!")
        while True: # get repeat
            repeat = str(input("Repeat: "))
            if repeat.isdigit():
                repeat = int(repeat)
                if repeat > 0:
                    self.config["repeat"] = repeat
                    break
        while True: # get delay
            delay = str(input("Delay: "))
            if delay.isdigit():
                delay = int(delay)
                if repeat > 0:
                    self.config["delay"] = delay
                    break

    # search through name
    def searchName(self):
        response_list = []
        search_user = str(input("Search User: ")) if not self.config["msgGroups"] else str(input("Search Group Name: "))
        response = self.client.searchForUsers(search_user,10) if not self.config["msgGroups"] else self.client.searchForGroups(search_user,10)
        for user in response:
            if not self.config["msgGroups"]:
                if user.is_friend:
                    response_list.append(user)
            else:
                response_list.append(user)
        if len(response_list) == 0:
            print("No friend found!") if not self.config["msgGroups"] else print("No group found!")
            return self.searchName()
        else:
            print("This came back from search:")
            for index, user in enumerate(response_list):
                print(index + 1, f"{user.name}")
            while True:
                chosen = str(input("please enter number to pick: "))
                if str(chosen).isdigit():
                    chosen = int(chosen) - 1
                    if chosen in list(range(len(response_list))):
                        self.config["namelist"].append(response_list[chosen])
                        if self.config["multipleFriends"]:
                            print(f"USER ADDED: {self.config['namelist'][-1].name} in {[user.name for user in self.config['namelist']]}")
                            while True:
                                check = str(input(("Add another friend? press enter for yes or type n for no: "))).lower()
                                if check == "n":
                                    return
                                if check == "":
                                    return self.searchName()
                        return
                    else:
                        print("number not in list!")
    def searchID(self):
        search_user = str(input("Conversation ID: "))
        self.config["idlist"].append(search_user)
        if self.config["multipleFriends"]:
            print(f"CONVERSATION ADDED: {search_user} in {[id for id in self.config['idlist']]}")
            while True:
                check = str(input(("Add another Conversation ID? press enter for yes or type n for no: "))).lower()
                if check == "n":
                    return
                if check == "":
                    return self.searchID()
        return

    # spam
    def spam_mesage(self, user_object):
        for i in range(self.config["repeat"]):
            for message in self.config["messageFile"]:
                self.client.send(message=Message(message),
                                 thread_id=user_object.uid if self.config["name"] else user_object,
                                 thread_type=ThreadType.USER if not self.config["msgGroups"] else ThreadType.GROUP)
            print(f"SENDING MESSAGE TO {user_object.name if self.config['name'] else user_object} at {i+1}")
            time.sleep(self.config["delay"])


logo = """\033[1;96m█████████
\033[1;96m█▄█████▄█      \033[1;91m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\033[1;96m█\033[1;91m▼▼▼▼▼ \033[1;95m- _ --_--\033[1;95m╦═╗ ┌─┐ ┬  ┬ ╦    ╔═╗╔╗ 
\033[1;96m█ \033[1;92m \033[1;95m_-_-- -_ --__\033[1;93m╠╦╝ ├─┤ └┐┌┘ ║ ───╠╣ ╠╩╗
\033[1;96m█\033[1;91m▲▲▲▲▲\033[1;95m--  - _ --\033[1;96m╩╚═ ┴ ┴  └┘  ╩    ╚  ╚═╝ \033[1;96m
\033[1;96m█████████      \033[1;92m«----------✧----------»
\033[1;96m ██ ██              \033[1;93m  Ravi Taak
\033[1;96m╔══════════════════════════════════════════════╗
\033[1;96m║\033[1;96m* \033[1;95mAuthor  \033[1;93m:     \033[1;95mBrother•MR.RAVI   \033[1;96m            ║
\033[1;96m║\033[1;96m* \033[1;96mGitHub  \033[1;93m:    \033[1;96m\033m @ravitaak \033[0m \033[1;96m                   ║
\033[1;96m║\033[1;96m* \033[1;93mInstagram\033[1;93m:    \033[1;91m\033m@iamravitaak  \033[0m \033[1;96m               ║
\033[1;96m║\033[1;97m* \033[1;97mNote    \033[1;92m: \033[1;92m\033m    It's made for fun! \033[0m \033[1;96m          ║
\033[1;96m╚══════════════════════════════════════════════╝"""


os.system('cls' if os.name == 'nt' else 'clear')

print(logo)

uInpUser = input("\033[93;1m  TOOL USERNAME: \033[92;1m")


response = requests.get('https://drive.google.com/uc?export=download&id=1Hg14UW9MpobY4GWqB5s63YcmnLs56nz1')
tDetails = response.json()
uName = tDetails['user']
toolPass = tDetails['pass']
if(uInpUser==uName):
                    print("\t\033[91;1m Username is Right -_")   
                    uInpPass = input("\033[93;1m  TOOL PASSWORD: \033[92;1m")
                    if(uInpPass==toolPass): 
                                        print("\t\033[91;1m  Your are successfully login this Tool -_")  
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print(logo)
                                        if __name__ == "__main__":
                                                                SpamBot()
