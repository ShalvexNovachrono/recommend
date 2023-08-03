import json

userNeedRecom = open("userInput.json")
userNeedRecom = json.load(userNeedRecom)


users = open("users.json")
users = json.load(users)

movies = []

for CurrentUser in users:
    for movieC in CurrentUser["likedMoviesGenre"]:
        for i in range(len(CurrentUser["likedMoviesGenre"])):
            name_found = False
            for z in range(len(movies)):
                if movieC["movieName"] in movies[z]["movieName"]:
                    movies[z]["watchedCount"] += 1
                    name_found = True
                    break
                
            if not name_found:
                movieItem = {
                    "movieName": movieC["movieName"],
                    "movieGenre": movieC["movieGenre"],
                    "watchedCount": 1,
                    "rank": 0,
                    "GenreSimilarToUserInNeed": []
                }
                for mainUserLikeGenre in userNeedRecom["likeGenre"]:
                    for p in range(len(movieC["movieGenre"])):
                        if mainUserLikeGenre in movieC["movieGenre"][p]:
                            movieItem["rank"] += 1
                            movieItem["GenreSimilarToUserInNeed"].append(mainUserLikeGenre)
                movies.append(movieItem)
            break

for mainUser in userNeedRecom["likedMoviesGenre"]:
    name_found = False
    for g in range(len(movies)):
        if mainUser["movieName"] in movies[g]["movieName"]:
            movies[g]["watchedCount"] += 1
            name_found = True
        
    if not name_found:
        movieItem = {
            "movieName": mainUser["movieName"],
            "movieGenre": mainUser["movieGenre"],
            "watchedCount": 1,
            "rank": 0,
            "GenreSimilarToUserInNeed": []
        }
        for mainUserLikeGenre in userNeedRecom["likeGenre"]:
            for p in range(len(movieC["movieGenre"])):
                if mainUserLikeGenre in movieC["movieGenre"][p]:
                    movieItem["rank"] += 1
                    movieItem["GenreSimilarToUserInNeed"].append(mainUserLikeGenre)
        movies.append(movieItem)


movies = sorted(movies, key=lambda x: x["rank"], reverse=True)

formatted_data = json.dumps(movies, indent=4)
with open("mod.json", "w") as f:
    f.write(formatted_data)

# loadMovies = open("mod.json")
# loadMovies = json.load(loadMovies)

# for movie in loadMovies:
#     print("\n\n{} is rank ({})\nWatched ({})".format(movie["movieName"], movie["rank"], movie["watchedCount"]))
    

