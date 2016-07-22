#
import csv
#class User():

with open('ml-100k/u.user') as f: # automatically closes the file when done
    reader = csv.reader(f, delimiter = '\t')
    #headers = next(reader)
    users_list = []
    for row in reader:
        users_list.append(row)
