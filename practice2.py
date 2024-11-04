import csv
import ast
from multiprocessing.managers import Value

rows = []
with open('top_50_2023.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    header = next(csv_reader)
    print(header)
    for row in csv_reader:
        rows.append(row)

print(rows)

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

danceability = header.index('danceability')
print(danceability)
sum_dance = 0

counter_floats_danceability = 0
for row in rows:

    if is_float(row[danceability]):
        sum_dance += float(row[danceability])
        counter_floats_danceability += 1
print(sum_dance / counter_floats_danceability)

for row in rows:
    row[4] = ast.literal_eval(row[4])
print(rows)

GENRES = 4
genres_dict = {}
for row in rows:
    for genre in row[GENRES]:
        if genre in genres_dict:
            genres_dict[genre] += 1
        else:
            genres_dict[genre] = 1
print(genres_dict)
top_three = sorted(genres_dict.items(), key = lambda x: x[1], reverse = True)
print(top_three[:3])
# 2 3 5

# 2
livenessINDEX = header.index('liveness')
energyINDEX = header.index('energy')


sum_liveness = 0
counter_liveness = 0
for row in rows:
    if is_float(row[energyINDEX]) and float(row[energyINDEX]) > 0.5 and is_float(row[livenessINDEX]):
        sum_liveness += float(row[livenessINDEX])
        counter_liveness += 1
print(sum_liveness / counter_liveness)


# 3
artistINDEX = header.index('artist_name')
artist_dict = {}
for row in rows:
    artist = row[artistINDEX]
    try:
        artist_dict[artist] += 1
    except Exception:
        artist_dict[artist] = 1

print(artist_dict)
top_artist = sorted(artist_dict.items(), key = lambda x: x[1], reverse = True)[:1]
print(top_artist[0])


# 5
releaseINDEX = header.index('album_release_date')
year_songs_dict = {}

for row in rows:
    row[releaseINDEX] = row[releaseINDEX].split('-')
    try:
        year_songs_dict[row[releaseINDEX][0]] += 1
    except Exception:
        year_songs_dict[row[releaseINDEX][0]] = 1

print(year_songs_dict)
top_year = sorted(year_songs_dict.items(), key = lambda x: x[1])
print(f'The most songs was released in year: {top_year[-1][0]}')
