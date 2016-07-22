#
import csv
#class Rating():

with open('ml-100k/u.data') as f: # automatically closes the file when done
    reader = csv.reader(f, delimiter = '\t')
    headers = next(reader)
    ratings_list = []
    for row in reader:
            ratings_list.append(row)

print(ratings_list)
