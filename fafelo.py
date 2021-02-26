# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:10:01 2021

@author: John
"""

from elo import rate_1vs1, Rating
import csv


resultsFile = open("faf_results_csv.csv", newline='', encoding="utf-8")
ratingFile = open("faf_ratings.txt", newline='', encoding="utf-8")


reader = csv.reader(resultsFile, delimiter=' ', quotechar='|')
ratingReader = csv.reader(ratingFile, delimiter=' ', quotechar='|')

writer = csv.writer(ratingFile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)  

ratings = []
def findPlayer(player):
    for frow in ratings:
        if frow[0] == player:
            return True
    return False

def getPlayerRating(player):
    for frow in ratings:
        if frow[0] == player:
            return frow[1]
    return -1  

def setPlayerRating(player, rating):
    for frow in ratings:
        if frow[0] == player:
            frow[1] = rating

def whoWon(score):
    score1,score2 = score.split("-")
    if score1 > score2:
        return 1
    elif score2 > score1:
        return 2
    else:
        return -1
    

for row in ratingReader:
    ratings.append(row)
        
with open('faf_results_csv.csv', newline='') as csvfile:
    for row in reader:
        #print(', '.join(row))
        #test = row[0]
        print(row)
        info = row[0].split(",")
        player1 = info[0]
        player2 = info[1]
        score = info[2]
        player1Found = findPlayer(player1)
        player2Found = findPlayer(player2)
        winner = whoWon(score)
        if not player1Found:
            ratings.append([player1, 1000])
        if not player2Found:
            ratings.append([player2, 1000])
        if winner == 1:
            rating1, rating2 = rate_1vs1(getPlayerRating(player1), getPlayerRating(player2))
        elif winner == 2:
            rating2, rating1 = rate_1vs1(getPlayerRating(player2), getPlayerRating(player1))
        else:
            print("error")
        setPlayerRating(player1, rating1)
        setPlayerRating(player2, rating2)
        
f = open('faf_ratings.txt', 'r+')        
f.truncate(0)
f.close()
     
ratingAppendFile = open("faf_ratings.txt", 'a', newline='', encoding="utf-8")
appendWriter = csv.writer(ratingAppendFile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)       
for row in ratings:
    appendWriter.writerow(row)        
                    


