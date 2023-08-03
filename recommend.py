import subprocess
import json
import time



subprocess.run(["python", "MOD.py"])
time.sleep(1)
subprocess.run(["python", "RUBFGWM.py"])
time.sleep(1)


RUBFGWM = json.load(open("RUBFGWM.json"))

YouShouldWatch = []
WatchedByOthersWithDifferentTaste = []


RESET = '\033[0m'       # Reset all attributes
RED = '\033[91m'        # Red text
GREEN = '\033[92m'      # Green text
YELLOW = '\033[93m'     # Yellow text
BLUE = '\033[94m'       # Blue text
MAGENTA = '\033[95m'    # Magenta text
CYAN = '\033[96m'       # Cyan text
WHITE = '\033[97m'      # White text

count = 0
for r in RUBFGWM:
    count+=1
    rec = False
    print(("{} ) " + MAGENTA + "{} is " + YELLOW + "Rank [{}]" + RESET ).format(count, r["name"], r["TotalRank"]) + RESET)
    print((CYAN + "     Genre Rank ({})" + RESET + "\n        Similar Genre To User:").format(r["GenreRank"]))
    for genre in r["GenreCommonWith"]:
        print(("              " + RED + ">>> " + RESET + " {}").format(genre))
    
    
    print((CYAN + "     Movie Rank ({})" + RESET + "\n        Movie Common With:").format(r["MovieRank"]))
    print_ = True
    for MovieCommonWith in r["MovieCommonWith"]:
        print_ = False
        
        rec = True
        movieGenre = ""
        for M in MovieCommonWith["movieGenre"]:
            if movieGenre != "":
                movieGenre += ", "
            movieGenre += M 

        
        movieGenreSimilarToUserInNeed = ""
        for M in MovieCommonWith["GenreSimilarToUserInNeed"]:
            if movieGenreSimilarToUserInNeed != "":
                movieGenreSimilarToUserInNeed += ", "
            movieGenreSimilarToUserInNeed += M 
        print(("              " + RED + ">>> " + RESET + YELLOW + "Rank [{}] " + RESET + BLUE + " Watched: " + RESET + RED + "[{}]" + RESET + BLUE + " Movie Title: " + RESET + RED + "[{}]" + RESET + BLUE + " Genre: " + RESET + RED + "[{}]" + RESET + BLUE +" Movie Genre Similar to User Genre: " + RESET + RED + "[{}]" + RESET).format(MovieCommonWith["RankOfThisMovie"], MovieCommonWith["watchedCount"], MovieCommonWith["movieName"], movieGenre, movieGenreSimilarToUserInNeed))
    
    if print_ == True:
        print("              " + RED +">>> [None]" + RESET)


    print((CYAN + "     Other Movie Rank ({})" + RESET + "\n        Also Watched This Movie:").format(r["AlsoWatchedThisMovieRank"]))
    print_ = True
    for AlsoWatchedThisMovie in r["AlsoWatchedThisMovie"]:
        print_ = False
        movieGenre = ""
        for M in AlsoWatchedThisMovie["movieGenre"]:
            if movieGenre != "":
                movieGenre += ", "
            movieGenre += M 

        print(("              " + RED + ">>> " + RESET + YELLOW + "Rank [{}] " + RESET + BLUE + " Watched: " + RESET + RED + "[{}]" + RESET + BLUE + " Movie Title: " + RESET + RED + "[{}]" + RESET + BLUE + " Genre: " + RESET + RED + "[{}]" + RESET).format(AlsoWatchedThisMovie["RankOfThisMovie"], AlsoWatchedThisMovie["watchedCount"], AlsoWatchedThisMovie["movieName"], movieGenre))
        if rec:
            YouShouldWatch.append(AlsoWatchedThisMovie)
        else:
            WatchedByOthersWithDifferentTaste.append(AlsoWatchedThisMovie)  

    if print_ == True:
        print("              " + RED +">>> [None]" + RESET)

    print("\n")

RUBFGYouShouldWatchWM = sorted(YouShouldWatch, key=lambda x: x["RankOfThisMovie"], reverse=True)
print("You should watch:")
count = 0
for movie in YouShouldWatch:
    count += 1
    Genre = ""
    for G in movie["movieGenre"]:
        if Genre != "":
            Genre += ", "
        Genre += G
    print((YELLOW + "Rank [{}] " + RESET + RED +"[{}] "+ RESET + BLUE  + "Viewed" + RESET + " [{}] " + BLUE  + "Genre: " + RESET + "[{}]").format(count, movie["movieName"], movie["watchedCount"], Genre))
     


print("\n\nAfter the recommendation watch this:")

for movie in WatchedByOthersWithDifferentTaste:
    count += 1
    Genre = ""
    for G in movie["movieGenre"]:
        if Genre != "":
            Genre += ", "
        Genre += G
    print((YELLOW + "Rank [{}] " + RESET + RED +"[{}] "+ RESET + BLUE  + "Viewed" + RESET + " [{}] " + BLUE  + "Genre: " + RESET + "[{}]").format(count, movie["movieName"], movie["watchedCount"], Genre))
     