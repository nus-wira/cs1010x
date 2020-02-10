#
# CS1010X --- Programming Methodology
#
# Sidequest 12.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import json

# Reading json file
def read_json(filename):
    """
    Reads a json file and returns a list of modules
    To find out more about json, please google ;)

    For example, cs1010x-fbdata.json contains:

    {
       "members": {
          "data": [
             {
                "name": "Aadit Kamat",
                "id": "1003982836283025"
             },
             {
                "name": "Rakshit Gogia",
                "id": "10204299775189027"
             },
             ...
          ]
       },
       "description": "This is the official FB Group for ...",
       "name": "CS1010X",
       "feed": {
          "data": [
             {
                "message": "Might be useful for the business analytics ...",
                "from": {
                   "name": "Ben Leong",
                   "id": "10152805891837166"
                },
                "name": "Machine Learning with Python - BDU"
                "id": "409054432560329_1002582839874149",
                "likes": {
                   "data": [
                      {
                         "id": "10208170707289199",
                         "name": "Lim Kian Hwee"
                      },
                      {
                         "id": "10204292869386114",
                         "name": "Siidheesh Theivasigamani"
                      },
                      ...
                   ]
                },
                ...
             },
             ...
          ]
       },
       "id": "409054432560329"
    }

    """
    datafile = open(filename, 'r',  encoding='utf-8')
    return json.loads(datafile.read())

# CS1010X Facebook Group Data as a dictionary object
fb_data = read_json('cs1010x-fbdata.json')

##########
# Task a #
##########

def count_comments(data):
    # Returns the total number of comments
    count = 0
    for feed in data["feed"]["data"]:
        if "comments" in feed:
            count += len(feed["comments"]["data"])
    return count

print("Number of Comments in CS1010X: ", count_comments(fb_data))

##########
# Task b #
##########

def count_likes(data):
    # Returns the total number of likes (in feed posts and comments)
    count = 0
    for feed in data["feed"]["data"]:
        if "likes" in feed:
            count += len(feed["likes"]["data"])
        if "comments" in feed:
            for comment in feed["comments"]["data"]:
                count += comment["like_count"]
    return count

print("Number of Likes in CS1010X: ", count_likes(fb_data))

##########
# Task c #
##########

def create_member_dict(data):
    # Lookup table where key is id and value is member data object
    table = {}
    for member in data["members"]["data"]:
        table[member["id"]] = member.copy()
        del table[member["id"]]["id"]
    return table

member_dict = create_member_dict(fb_data)
print(member_dict["10205702832196255"])

# Q: Why did we choose the id of the member data object to be the key?
# A: The id of each member will not change over time.

# Q: It is inappropriate to use the name as the key. What will happen if we use the name as the key of member_dict?
# A: If the member changes their name, the key will be unusable.

##########
# Task d #
##########

def posts_freq(data):
    # Returns a dict where key is fb_id and value is number of posts in feed
    table = {}
    for feed in data["feed"]["data"]:
        if "from" in feed:
            if feed["from"]["id"] in table:
                table[feed["from"]["id"]] += 1
            else:
                table[feed["from"]["id"]] = 1
    return table

print("Posts Frequency: ", posts_freq(fb_data))

##########
# Task e #
##########

def comments_freq(data):
    # Returns a dict where key is fb_id and value is number of comments in feed
    table = {}
    for feed in data["feed"]["data"]:
        if "comments" in feed:
            for comment in feed["comments"]["data"]:
                if comment["from"]["id"] not in table:
                    table[comment["from"]["id"]] = 1
                else:
                    table[comment["from"]["id"]] += 1

    return table

print("Comments Frequency: ", comments_freq(fb_data))

##########
# Task f #
##########

def likes_freq(data):
    # Returns a dict where key is fb_id and value is number of likes in feed              
    table = {}
    for feed in data["feed"]["data"]:
        if "likes" in feed:
            for like in feed["likes"]["data"]:
                if like["id"] in table:
                    table[like["id"]] += 1
                else:
                    table[like["id"]] = 1

    return table

print("Likes Frequency: ", likes_freq(fb_data))

##########
# Task g #
##########

def popularity_score(data):
    # Returns a dict where key is fb_id and value is the number of likes
    # a person's posts and comments have
    table = {}
    for feed in data["feed"]["data"]:
        if "likes" in feed:
            if len(feed["likes"]["data"]) != 0:
                if feed["from"]["id"] in table:
                    table[feed["from"]["id"]] += len(feed["likes"]["data"])
                else:
                    table[feed["from"]["id"]] = len(feed["likes"]["data"])
        if "comments" in feed:
            for comment in feed["comments"]["data"]:
                if comment["like_count"] != 0:
                    if comment["from"]["id"] in table:
                        table[comment["from"]["id"]] += comment["like_count"]
                    else:
                        table[comment["from"]["id"]] = comment["like_count"]
    return table

print("Popularity Score: ", popularity_score(fb_data))

##########
# Task h #
##########

def member_stats(data):
    # Expand the member dict to include the keys:
    # 'posts_count', 'comments_count' and 'likes_count'
    posts, comments, likes = posts_freq(data), comments_freq(data), likes_freq(data)
    table = create_member_dict(data)
    for idn in table:
        table[idn]["posts_count"] = 0
        table[idn]["comments_count"] = 0
        table[idn]["likes_count"] = 0
        if idn in posts:
            table[idn]["posts_count"] = posts[idn]
        if idn in comments:
            table[idn]["comments_count"] = comments[idn]
        if idn in likes:
            table[idn]["likes_count"] = likes[idn]
    return table

stats = member_stats(fb_data)
print(stats["10152805891837166"])

##########
# Task i #
##########

def activity_score(data):
    stats = member_stats(data)
    table = {}
    for idn in stats:
        table[idn] = 3 * stats[idn]["posts_count"] + 2 * stats[idn]["comments_count"] + stats[idn]["likes_count"]
    return table

scores = activity_score(fb_data)
print(scores["10153020766393769"]) # => 30
print(scores["857756387629369"]) # => 8


##########
# Task j #
##########

def active_members_of_type(data, k, type_fn):
    # This is a higher order function, where type is a function and
    # can be either posts_freq, comments_freq, likes_freq, etc
    # and filters out the pairs that have frequency >= k
    table = type_fn(data)
    member_dict = create_member_dict(data)
    lst = []
    for idn in table:
        if table[idn] >= k and idn in member_dict:
            lst.append([member_dict[idn]["name"], table[idn]])

    lst.sort()
    lst.sort(key=lambda x:x[1], reverse=True)
    return lst

print(active_members_of_type(fb_data, 2, posts_freq))

print(active_members_of_type(fb_data, 20, comments_freq))

print(active_members_of_type(fb_data, 40, likes_freq))

print(active_members_of_type(fb_data, 20, popularity_score))

print(active_members_of_type(fb_data, 80, activity_score))




########### DO NOT REMOVE THE TEST BELOW ###########

def gradeit():
    print("\n*** Facebook Stalker Autograding ***")
    print('==================')
    answers = json.loads(open('grading.json', 'r',  encoding='utf-8').read())
    total, correct = 0, 0
    def pass_or_fail(code, answer):
        nonlocal total
        total += 1
        if code == answer:
            nonlocal correct
            correct += 1
            return 'Passed!'
        else:
            return 'Failed.'
            
    print('Testing count_comments... ', pass_or_fail(count_comments(fb_data), answers['count_comments']))
    print('Testing count_likes... ', pass_or_fail(count_likes(fb_data), answers['count_likes']))
    print('Testing create_member_dict... ', pass_or_fail(create_member_dict(fb_data), answers['create_member_dict']))
    print('Testing posts_freq... ', pass_or_fail(posts_freq(fb_data), answers['posts_freq']))
    print('Testing comments_freq... ', pass_or_fail(comments_freq(fb_data), answers['comments_freq']))
    print('Testing likes_freq... ', pass_or_fail(likes_freq(fb_data), answers['likes_freq']))
    print('Testing popularity_score... ', pass_or_fail(popularity_score(fb_data), answers['popularity_score']))
    print('Testing member_stats... ', pass_or_fail(member_stats(fb_data), answers['member_stats']))
    print('Testing activity_score... ', pass_or_fail(activity_score(fb_data), answers['activity_score']))
    print('Testing members with >= 1 posts... ', pass_or_fail(active_members_of_type(fb_data, 1, posts_freq), answers['active_posters']))
    print('Testing members with >= 4 comments... ', pass_or_fail(active_members_of_type(fb_data, 4, comments_freq), answers['active_commenters']))
    print('Testing members with >= 4 likes... ', pass_or_fail(active_members_of_type(fb_data, 4, likes_freq), answers['active_likers']))
    print('Testing members who have >= 3 likes... ', pass_or_fail(active_members_of_type(fb_data, 3, popularity_score), answers['popular']))
    print('Testing members with an activity score of >= 10... ', pass_or_fail(active_members_of_type(fb_data, 10, activity_score), answers['overall_active']))
    print('==================')
    print('Grades: ' + str(correct) + '/' + str(total) + '\n')

gradeit()
