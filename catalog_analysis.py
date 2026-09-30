import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    '''
     Возвращает среднюю оценку по каталогу фильмов,
    округлённую до одного знака.
    '''
    if not movies:
        return 0
    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    '''
    Возвращает кортеж (возраст самого старого фильма,
    возраст самого нового фильма, средний возраст),
    где средний возраст округлён вверх до целого.
    '''
    if not movies:
        return None

    ages = [current_year - movie["year"] for movie in movies]

    oldest = max(ages)
    newest = min(ages)  
    average = math.ceil(sum(ages) / len(ages))

    return (oldest, newest, average)

def duration_in_hours(minutes):
    '''
    Переводит минуты в формат  "X часов Y минут"
    '''
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"

### Этап 2. Условия и match

def rating_tier(rating):
    '''
    Возвращает оценку рейтингу фильма
    '''
    if rating >= 9:
        return "шедевр"
    if rating >= 7:
        return "хорошо"
    if rating >= 5:
        return "средне"
    return "слабо" if rating >= 0 else "некорректно"

def decade_label(year):
    """
    Возвращает оценку по году выпуска.
    """
    match year:
        case y if y > 2020:
            return "новые"
        case y if 2015 <= y <= 2020:
            return "недавние"
        case _:
            return "старые"

### Этап 3. Циклы

for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    print(movie["title"])

i = 0
while i < len(movies):
    if movies[i]["rating"] > 9.0: 
        print(f"Найден шедевр: {movies[i]['title']}")
        break
    i += 1
else:
    print("Шедевров не найдено")

def count_long_movies(movies, threshold=120):
    '''
    Считает количество фильмов длинее threshold минут
    '''
    count = 0
    for movie in movies:
        if movie["duration"] > threshold:
            count += 1
    return count

### Этап 4. Строки

def normalize_title(title):
    '''
    Приводит строку в формат Title Case
    '''
    words = title.split()
    normalized = []
    for word in words:
        normalized.append(word[0].upper() + word[1:])
    return " ".join(normalized) 

def make_slug(title):
    '''
    Превращает название в слаг вида "the-quiet-algorithm".
    '''
    return title.lower().replace(" ", "-")

def format_report_line(movie):

    title = movie["title"]
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres}'

### Этап 5. Списки

def titles_sorted_by_rating(movies):
    '''
    Возвращает список названий фильмов, отсортированных по убыванию рейтинга.
    Исходный список не меняется.
    '''
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]

def top_n_by_rating(movies, n=3):
    '''
    Возвращает список из n кортежей (title, rating) — топ по рейтингу.
    '''
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]

### Этап 6. Словари

def count_by_genre(movies):
    '''
    Возвращает словарь {жанр: количество фильмов}
    '''
    counts = {}
    for movie in movies: 
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts

def actor_filmography(movies):
    '''
    Возвращает словарь {актер: [список названий фильмов]}.
    '''
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography.setdefault(actor, []).append(movie["title"]) 
    return filmography

def above_average_movies(movies):
    '''
    Возвращает словарь {title: rating} только для фильмов
    с рейтингом выше среднего.
    '''
    avg = average_rating(movies)
    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > avg }

### Этап 7. Множества

def all_genres(movies):
    result = set()
    for m in movies:
        result |= set(m["genres"]) 
    return result

def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"]) 

def genres_only_in_one(movies_a, movies_b):
    genres_a = set().union(*(set(m["genres"]) for m in movies_a))
    genres_b = set().union(*(set(m["genres"]) for m in movies_b))
    return genres_a - genres_b

 ### Этап 8. Итераторы и генераторы

def iter_high_rated(movies, min_rating=8.0):
    for m in movies:
        if m["rating"] >= min_rating:
            yield m

for movie in iter_high_rated(movies):
    print(movie["title"], movie["rating"])

total = sum(m["duration_min"] for m in movies if m["rating"] > 7)

### Этап 9. Итоговый отчет

def build_report(movies):
    print("ОТЧЁТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет")
    print()

    print("Топ-3 фильма:")
    
    titles = titles_sorted_by_rating(movies)[:3]
    by_title = {m["title"]: m for m in movies}
    for title in titles:
        print("  " + format_report_line(by_title[title]))
    print()

    print("Фильмов по жанрам:")
    counts = count_by_genre(movies)

    for genre, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {genre} — {n}")
    print()

    
    print("Все жанры каталога: " + ", ".join(sorted(all_genres(movies))))

build_report(movies)