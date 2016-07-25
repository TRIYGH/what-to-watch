# movie
#   this is the main engine / starting point
from movie_lib import *

######  get user a good suggestion  ######

# all_suggestions = []
# umu = get_unrated_movies_for_user('55')
# mwr = movies_to_search_filter(25)
# combined = set(umu) & set(mwr)
# for each in combined:
#     all_suggestions.append(each)
#
# top_suggestions = top_ten_movies(10, all_suggestions)
# print("\nYou should watch these movies:\n")
# x = 0
# while x < len(top_suggestions):
#     print(find_movie_by_ID(top_suggestions[x])," has an average rating of:\t{:0.2f}".format(top_suggestions[x+1]))
#     x += 2
print(all_rating_for_a_user('111'))
print(all_rating_for_a_user('32'))
input()
#========================   STEP 5   ============================
u1 = input("user 1 :")
u1lorm = get_all_users_ratings_and_movies(u1)

u2 = input("user 2 :")
u2lorm = get_all_users_ratings_and_movies(u2)

u1_dict = make_udict(u1lorm)
u2_dict = make_udict(u2lorm)

edist = match_users_by_movies_rated(u1_dict, u2_dict)

input()
print(u1_dict)

input()
print(u2_dict)

# ===============================================================
#       Compare all users to this one:
u1 = input("give me a user to find their best matches: ")
u1lorm = get_all_users_ratings_and_movies(u1)
u1_dict = make_udict(u1lorm)

x = 943
eucl_scores_list = []
eucl_scores_dict = {}
extra_copy_eucl_scores_dict = {}

for i in range(x):
    if (i+1) != int(u1):
        u2lorm = get_all_users_ratings_and_movies(str(i+1))
        u2_dict = make_udict(u2lorm)
        eucl_score = match_users_by_movies_rated(u1_dict, u2_dict)
        eucl_scores_dict[(i+1)] = eucl_score

print(eucl_scores_dict,"^^^^^^^^^^^^^^^^^")

#============ DEEP SHALLOW COPY PROBLEM ===============
for i in range(x):
    if (i+1) != int(u1):
        u2lorm = get_all_users_ratings_and_movies(str(i+1))
        u2_dict = make_udict(u2lorm)
        eucl_score = match_users_by_movies_rated(u1_dict, u2_dict)
        extra_copy_eucl_scores_dict[(i+1)] = eucl_score

# for each in eucl_scores_list:

best_fit = get_max_euclidean_scores(eucl_scores_dict)
# best_fit = {}
# i = 0
# while i < 10:
#     v=list(eucl_scores_dict.values())
#     k=list(eucl_scores_dict.keys())
#     key = k[v.index(max(v))]
#     print(k[v.index(max(v))])
#     best_fit[i] = k[v.index(max(v))]    #should use a list instead
#     del eucl_scores_dict[key]
#     i += 1
#
print(best_fit,"\n")

def loop_thru(uX, uU_list, uM_list, uR_list, each, umu1):
    z = 0
    for every in uX:
        if every[0] not in umu1:
            every.remove
        else:
            z += 1
            if z > 10:
                for i in range(10):
                    uU_list.append(each) #,uX[i]  #list[640, [1,4]]
                    uM_list.append(uX[i][0])
                    uR_list.append(uX[i][1])
                break
    return uU_list, uM_list, uR_list


umu1 = get_unrated_movies_for_user(u1) #[1][2][6][9]
uX_list = []
uU_list = []
uM_list = []
uR_list = []
#get top ten movies each similar user rated top ten
for each in best_fit:
    uX = get_all_users_ratings_and_movies(each) #[1,4][122,5]
    uX.sort(key=lambda x: x[1])
    uX.reverse()
    uU_list, uM_list, uR_list = (loop_thru(uX, uU_list, uM_list, uR_list, each, umu1))

print(uU_list, uM_list, uR_list)
input()

print(uX_list)
print(extra_copy_eucl_scores_dict)

similar_list = []
count = 1
for each in best_fit:
    similar_list.append(extra_copy_eucl_scores_dict[int(each)])
print(similar_list)

for i in range(10):
    for j in range(10):
        sim = similar_list[i] * int(uR_list[(i*10)+j])
        print("movie: {}  with user: {} scores a: {}".format(uM_list[(i*10)+j],uU_list[(i*10)+j], sim))


    #mts = movies_to_search_filter(9)
    #top_ten_movies(10, mts)
