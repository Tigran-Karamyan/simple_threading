import concurrent.futures
import pandas as pd
import string
import time
import os

# import dataset
df = pd.read_csv('lyrics-data.csv').reset_index()

# convert df to dict
df_to_dict = {key: value for (key, value) in zip(df.index, df.Lyric)}

filename = list(df_to_dict.keys())
lyrics = list(df_to_dict.values())

# lyrics to separate txt files
def lyrics_to_txt(filename, lyrics):
    #print(f"Converting {filename}... ")
    with open(f"tmp/{filename}.txt", "w+", encoding="utf-8") as file:
        file.write(str(lyrics))

# threading
t1 = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(lyrics_to_txt, filename, lyrics)

t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')

# No threading
t1 = time.perf_counter()
for f, l in zip(filename, lyrics):
    lyrics_to_txt(f, l)

t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')
