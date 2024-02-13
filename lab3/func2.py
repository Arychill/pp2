# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def is_high_imdb(movie_name):
    for movie in movies:
        if movie["name"] == movie_name:
            return movie["imdb"] > 5.5
    return False
print(is_high_imdb("We Two"))
print(is_high_imdb("Detective"))

def high_imdb_movies(movies_list):
    return [movie for movie in movies_list if is_high_imdb(movie["name"])]
print(high_imdb_movies(movies))

print(" ")

def category_name(category):
    return[movie['name'] for movie in movies if movie["category"] == category]
print(category_name("Thriller"))


def average_imdb_score(movies_list):
    total_score = sum(movie["imdb"] for movie in movies_list)
    return total_score / len(movies_list)
print(average_imdb_score(movies))
    
def average_imdb_score_category(category, movies_list):
    sum = 0
    sum2 = 0
    for movie in movies:
        if movie["category"] == category:
            sum += movie["imdb"]
            sum2 += 1
    return sum / sum2
print(average_imdb_score_category("Thriller", movies))