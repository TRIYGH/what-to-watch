#
import csv
#class Rating():

with open('ml-100k/u.data') as f: # automatically closes the file when done
    reader = csv.reader(f, delimiter = '\t')
    ratings_list = []
    for row in reader:
        ratings_list.append(row)

count = 1           #build blank dict
tempDict = {}
while count < 1683:
    tempDict[str(count)] = []
    count += 1

for each in ratings_list:   #why does this kill ratings_list too ??
    each.pop(3)
    each.pop(0)
    r = int(each[1])
    tempDict[each[0]].append(r)

count = 1
num_ratings = []
for each in tempDict:
    num_ratings.append(len(tempDict[str(count)]))
    count += 1

with open('ml-100k/u.data') as f: # automatically closes the file when done
    reader = csv.reader(f, delimiter = '\t')
    ratings_list = []
    for row in reader:
        ratings_list.append(row)
 
