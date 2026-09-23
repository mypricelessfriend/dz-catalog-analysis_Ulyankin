import math 
# список фильмов
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
    total = sum(movie["rating"] for movie in movies) # сумма рейтингов в movies
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

    oldest = max(ages)   # самый старый = наибольший возраст
    newest = min(ages)   # самый новый = наименьший возраст
    average = math.ceil(sum(ages) / len(ages))

    return (oldest, newest, average)

def duration_in_hours(minutes):
    '''
    Переводит минуты в формат  "X часов Y минут"
    '''
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"

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

for movie in movies:
    if movie["genre"] == "comedy":
        continue                      # пропускает комедии
    print(movie["title"]) # выводит все НЕ комедии

i = 0
while i < len(movies): # двигает индекс пока не найдет первый шедевр в списке
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
    count = 0 # накопительная переменная
    for movie in movies:
        if movie["duration"] > threshold:
            count += 1 # счетчик выполнения условия
    return count

def normalize_title(title):
    '''
    Приводит строку в формат Title Case
    '''
    words = title.split() # разбивает строку по пробелам
    normalized = []
    for word in words:
        normalized.append(word[0].upper() + word[1:]) # делает первую букву заглавной
    return " ".join(normalized) # собирает строку обратно через пробел
