#W2D4 weekend hw

import csv

#Find all ratings for a movie by id
    # need to open file for u.data
def ratings_by_ID(mID):
    with open('ml-100k/u.data') as f: # automatically closes the file when done
        reader = csv.reader(f, delimiter = '\t')
        all_ratings_for_specific_movie = []
        for row in reader:
            if row[1] == mID:
                all_ratings_for_specific_movie.append(row[2])    #get rating
    return all_ratings_for_specific_movie

#Find the average rating for a movie by id
    #use lists above
def calc_avg_rating(mID):
    all_ratings_for_specific_movie = ratings_by_ID(mID)
    x = 0
    for each in all_ratings_for_specific_movie:
        x += int(each)
    average_rating = x/len(all_ratings_for_specific_movie)
    print ("{0:.2f}".format(average_rating,))
    return average_rating


#Find the name of a movie by id
def find_movie_by_ID(mID):
    with open('ml-100k/u.item', encoding='latin_1') as f: # automatically closes the file when done
        reader = csv.reader(f, delimiter = '\t')

        movie_name = ""

        for row in reader:
            movie_ID = ""
            temp_str = str(row)
            str_list = list(temp_str)
            idx = str_list.index('|')   #find index of delimiter
            for i in range(2, idx):
                movie_ID += str_list[i] #put ID in string
            if mID == movie_ID:
                idx += 1
                for i in range(idx):
                    str_list.pop(0)     #delete the ID
                idx = str_list.index('|')
                for i in range(idx):
                    movie_name += str_list[i]   #build name
                done = True
            else:
                continue

            if done == True:
                break

    return movie_name


# Find all ratings for a user
def all_rating_for_a_user(uID):
    with open('ml-100k/u.data') as f: # automatically closes the file when done
        reader = csv.reader(f, delimiter = '\t')
        specific_user_total_ratings = []
        for row in reader:
            if row[0] == '55':
                specific_user_total_ratings.append(row[2])    #get rating

    print("This is user 55's ratings\n",specific_user_total_ratings)
    return specific_user_total_ratings
