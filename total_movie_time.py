import omdb
import json
import re


def movieslist(filename):
    with open(filename, "r", encoding="utf8") as file:
        return file.readlines()


movies = movieslist("movies.txt")
print("--------------------------------")
print("Total movies watched:", len(movies))

totaltime = 0
notfound = []

for movie in movies:
    moviename = re.sub("[^\w ,':]", "", movie.strip())
    res = omdb.request(t=moviename, apikey='71706981')
    movie = json.loads(res.content)

    if movie['Response'] == 'True':
        time = str(movie['Runtime']).replace(' min', '')
        if time.isdigit():
            time = int(time)
            totaltime += time
    else:
        notfound.append(moviename)

print("--------------------------------")
print("Totaltime:", totaltime)
print("--------------------------------")
print("Not found movies", notfound)
print("--------------------------------")
