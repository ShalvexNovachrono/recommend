import json

userInput = json.load(open("userInput.json"))

USERS = json.load(open("users.json"))

MOD = json.load(open("mod.json"))

#Rank_USERS_Based_On_Favorite_Genre_And_Watched_Movies
RUBFGWM = [] 

#Genre
for MainUserInput in userInput["likeGenre"]:
    for userS in USERS:
        name_found = False
        for i in range(len(RUBFGWM)):
            if userS["name"] == RUBFGWM[i]["name"]:
                name_found = True
                break
        
        if not name_found:
            user = {
                "name": userS["name"],
                "GenreCommonWith": [],
                "GenreRank": 0,
                "MovieCommonWith": [],
                "MovieRank": 0,
                "AlsoWatchedThisMovie": [],
                "AlsoWatchedThisMovieRank": 0,
                "TotalRank": 0
            }
            RUBFGWM.append(user)

for u in USERS:
    for r in RUBFGWM:
        if u["name"] == r["name"]:
            for g in userInput["likeGenre"]:
                for uG in u["likeGenre"]:
                    if uG == g:
                        r["GenreCommonWith"].append(g)
                        r["GenreRank"] += 1
                        r["TotalRank"] += 1

for u in USERS:
    for r in RUBFGWM:
        if u["name"] == r["name"]:
            for m in userInput["likedMoviesGenre"]:
                for uM in u["likedMoviesGenre"]:
                    if uM["movieName"] == m["movieName"]:
                        for mod in MOD:
                            if mod["movieName"] == m["movieName"]:
                                movieItem = {
                                    "movieName": m["movieName"],
                                    "movieGenre": mod["movieGenre"],
                                    "GenreSimilarToUserInNeed": mod["GenreSimilarToUserInNeed"],
                                    "watchedCount": mod["watchedCount"],
                                    "RankOfThisMovie": mod["rank"]
                                }
                                r["MovieCommonWith"].append(movieItem)
                                r["MovieRank"] += mod["rank"]
                                r["TotalRank"] += mod["rank"]   

            for uM in u["likedMoviesGenre"]:
                for mod in MOD:
                    name_found = False
                    for W in range(len(r["AlsoWatchedThisMovie"])):
                        if uM["movieName"] == r["AlsoWatchedThisMovie"][W]["movieName"]:
                            name_found = True    
                            break
                    
                    if not name_found:
                        name_found = False
                        for MovieCommonWith in r["MovieCommonWith"]:
                            if MovieCommonWith["movieName"] == uM["movieName"]:
                                name_found = True

                        if not name_found:
                            if uM["movieName"] == mod["movieName"]:
                                movieItem = {
                                    "movieName": mod["movieName"],
                                    "movieGenre": mod["movieGenre"],
                                    "watchedCount": mod["watchedCount"],
                                    "RankOfThisMovie": mod["rank"]
                                }
                                r["AlsoWatchedThisMovie"].append(movieItem)
                                
                                r["AlsoWatchedThisMovieRank"] += mod["rank"]  
                                r["TotalRank"] += mod["rank"]  


RUBFGWM = sorted(RUBFGWM, key=lambda x: x["TotalRank"], reverse=True)
formatted_data = json.dumps(RUBFGWM, indent=4)
with open("RUBFGWM.json", "w") as f:
    f.write(formatted_data)



