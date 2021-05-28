# fafTournamentElo

faf_ratings.txt contains the current list of ratings of various players
faf_results_csv.csv is the csv used to generate the ratings
fafelo.py contains the python code used to calculate the elo ratings for FAF players.

How to use:

1. Download the repo
2. Replace faf_results_csv.csv with a csv containing a new series of games
3. Run fafelo.py


The data set currently includes 196 games from:

* 2019 LotS
* 2020 Summer Inviational
* 2020 Fall Invitational
* 2020 LotS
* MapGen Tournament
* 2021 Spring Invitational
* 2021 April League Invitational

Qualifier tournaments are generally excluded from the dataset.