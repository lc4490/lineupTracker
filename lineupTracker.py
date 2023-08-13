#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
def main():
    teams = {
        "ATL": "Hawks",
        "BOS": "Celtics",
        "BKN": "Nets",
        "CHA": "Hornets",
        "CHI": "Bulls",
        "CLE": "Cavaliers",
        "DAL": "Mavericks",
        "DEN": "Nuggets",
        "DET": "Pistons",
        "GSW": "Warriors",
        "HOU": "Rockets",
        "IND": "Pacers",
        "LAC": "Clippers",
        "LAL": "Lakers",
        "MEM": "Grizzlies",
        "MIA": "Heat",
        "MIL": "Bucks",
        "MIN": "Timberwolves",
        "NOP": "Pelicans",
        "NYK": "Knicks",
        "OKC": "Thunder",
        "ORL": "Magic",
        "PHI": "76ers",
        "PHX": "Suns",
        "POR": "Trail Blazers",
        "SAC": "Kings",
        "SAS": "Spurs",
        "TOR": "Raptors",
        "UTA": "Jazz",
        "WAS": "Wizards"
    }
    team = input("Which team would you like to track? (Use three letter code) ")
    sample = int(input("How many games would you like to track? "))
    bigsoup = BeautifulSoup(requests.get("https://popcornmachine.net").text, features="lxml")
    urls = ["https://popcornmachine.net/"+t["href"] for t in bigsoup.find_all("a") if t["href"].startswith("gf") and team in t["href"]][:sample]
    lineups = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features="lxml")
        data = soup.find_all('p',{'class':'text1'})
        for i in data:
            temp = str(i).split("<br/>")[:]
            time = temp[0].split(" ")
            temp = temp[-6:]
            temp[-1]=temp[-1][:-4]
            temp.append(subtractTime(time[3],time[6]))
            if temp[0].startswith(teams[team]):
                temp[0]=int(temp[0][-2:])
                lineups.append(temp)
                
    finalLineups = []
    for lineup in lineups:
        dup=False
        lineupSet = set(lineup[1:-1])
        if("D\x92Angelo Russell" in lineupSet):
            lineupSet.remove("D\x92Angelo Russell")
            lineupSet.add("D'Angelo Russell")
        for l in finalLineups:
            if(lineupSet == l[0]):
                l[1] += int(lineup[0])
                l[2] = addTime(l[2], lineup[-1])
                dup = True
        if(not dup):
            finalLineups.append([lineupSet, int(lineup[0]), lineup[-1]])
    finalLineups = Sort(finalLineups)
    options = input("\n1 - Print all lineups\n2 - Print five best and five worst lineups\n3 - Find lineups of specific players\n4 - Remove lineups with specific players\n")
    print('')
    if options=="1":
        prettyPrint(finalLineups)
    elif options=="2":
        prettyPrint(finalLineups[:5]+finalLineups[-5:])
    elif options=="3":
        p = set(input("Enter player or players separated by commas:\n").split(","))
        prettyPrint(findSubset(p,finalLineups))
    elif options=="4":
        p = set(input("Enter player or players separated by commas:\n").split(","))
        prettyPrint(removeSubset(p, finalLineups))
    
def addTime(time1, time2):
    min1, sec1 = time1.split(":")
    min2, sec2 = time2.split(":")
    seconds_delta = int(min1)*60 + int(sec1) + (int(min2)*60 + int(sec2))
    minutes_delta = str(seconds_delta // 60)
    seconds_delta = str(seconds_delta % 60)
    if len(minutes_delta)<2:
        minutes_delta = "0"+str(minutes_delta)
    if len(seconds_delta)<2:
        seconds_delta = "0" + str(seconds_delta)
    return minutes_delta+ ":" +seconds_delta

def subtractTime(time1, time2):
    min1, sec1 = time1.split(":")
    min2, sec2 = time2.split(":")
    seconds_delta = int(min1)*60 + int(sec1) - (int(min2)*60 + int(sec2))
    minutes_delta = str(seconds_delta // 60)
    seconds_delta = str(seconds_delta % 60)
    if len(minutes_delta)<2:
        minutes_delta = "0"+str(minutes_delta)
    if len(seconds_delta)<2:
        seconds_delta = "0" + str(seconds_delta)
    return minutes_delta+ ":" +seconds_delta

def prettyPrint(lineups):
    for s in lineups:
        print(s)
        
def Sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][1] < sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li

def comp(lineuptotals):
    lineups = []
    for lineup in lineuptotals:
        dup = False
        for l in lineups:
            # print(lineup)
            # print(l[0])
            if(lineup[0] == l[0]):
                l[1] += int(lineup[1])
                dup = True
        if(not dup):
            lineups.append(lineup)
    return lineups
    
def findSubset(sub, lineuptotals):
    lineups = []
    count = 0
    for lineup in lineuptotals:
        if sub.issubset(lineup[0]):
            lineups.append(lineup)
            count += lineup[1]
    return lineups

def removeSubset(sub, lineuptotals):
    lineups = []
    for lineup in lineuptotals:
        if not sub.issubset(lineup[0]):
            lineups.append(lineup)
    return lineups

def prettyPrint(lineups):
    for s in lineups:
        print(s)

if __name__=='__main__':
    main()