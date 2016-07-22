#
import csv
#class Movie():

with open('ml-100k/u.item', encoding='latin_1') as f: # automatically closes the file when done
    reader = csv.reader(f, delimiter = '\t')
    #headers = next(reader)
    movies_list = []
    for row in reader:
        movies_list.append(row)
)
