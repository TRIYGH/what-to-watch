#W2D4 weekend hw

import csv
import Rating

#Find all ratings for a movie by id
    # need to open file for u.data
def ratings_by_ID(mID):
    # with open('ml-100k/u.data') as f: # automatically closes the file when done
    #     reader = csv.reader(f, delimiter = '\t')
    # print(Rating.ratings_list)
    # Input()
    # print(Rating.tempList)
    # input()
    all_ratings_for_specific_movie = []
    for row in Rating.ratings_list:
        if row[0] == mID:
            all_ratings_for_specific_movie.append(row[1])    #get rating
    return all_ratings_for_specific_movie


#Find the average rating for a movie by id
    #use lists above
def calc_avg_rating(mID):
    all_ratings_for_specific_movie = ratings_by_ID(mID)
    x = 0
    for each in all_ratings_for_specific_movie:
        x += int(each)
    average_rating = x/len(all_ratings_for_specific_movie)
    #print ("{0:.2f}".format(average_rating,))
    return average_rating


def num_of_ratings_per_movie(which_movie):
    num_ratings = Rating.num_ratings
    return (num_ratings[which_movie - 1])


#show me the top x movies with at least y reviews
def top_ten_movies(top, min_num_reviews):

    num_reviews = Rating.tempDict
    count = 1
    movies_to_search = []

    while count < 1683:
        if (len(num_reviews[str(count)])) >= min_num_reviews:
            movies_to_search.append(str(count))
        count += 1

# ---- this gets any movies with a 4.0 rating or above ----
    # top_movie = []
    # for each in movies_to_search:
    #     if float(calc_avg_rating(num_reviews[each])) >= 4.0:
    #         top_movie.append(each)
# ---------------------------------------------------------

    top_movies_dict = {}

    for each in movies_to_search:
        avg = calc_avg_rating(each)
        top_movies_dict[each] = avg

    top_movie_avgs_list = sorted(top_movies_dict.values(),reverse=True)

    top_movies_WITH_avgs_list = []
    count = 0
    while count < top:
        for each in top_movies_dict:
            if top_movies_dict[each] == top_movie_avgs_list[count]:
                top_movies_WITH_avgs_list.append(each)
                top_movies_WITH_avgs_list.append(top_movie_avgs_list[count])
        count += 1

    return top_movies_WITH_avgs_list


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
            if row[0] == uID:
                specific_user_total_ratings.append(row[2])    #get rating

    #print("This is user 55's ratings\n",specific_user_total_ratings)
    return specific_user_total_ratings


def get_unrated_movies_for_user(uID):
    with open('ml-100k/u.data') as f: # automatically closes the file when done
        reader = csv.reader(f, delimiter = '\t')
        ratings_list = []
        for row in reader:
            ratings_list.append(row)

        pop_list = []
        for each in ratings_list:
            if each[0] == uID:
                pop_list.append(each[1])

        unwatched_movies = []
        x = 1
        while x < 1683:
            unwatched_movies.append(str(x))
            x += 1

        for each in pop_list:
            unwatched_movies.pop(int(each))

    return unwatched_movies
