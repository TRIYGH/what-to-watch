# movie
#   this is the main engine / starting point
from movie_lib import *

######  get user a good suggestion  ######

all_suggestions = []
umu = get_unrated_movies_for_user('55')
mwr = movies_to_search_filter(25)
combined = set(umu) & set(mwr)
for each in combined:
    all_suggestions.append(each)

top_suggestions = top_ten_movies(10, all_suggestions)
print("\nYou should watch these movies:\n")
x = 0
while x < len(top_suggestions):
    print(find_movie_by_ID(top_suggestions[x])," has an average rating of:\t{:0.2f}".format(top_suggestions[x+1]))
    x += 2

#===============================================================
