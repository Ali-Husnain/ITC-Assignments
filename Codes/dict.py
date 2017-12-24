##  CODE FOR get_types_counts() FUNCTION GOES HERE ###
def get_types_counts(dic):
    dic1 = {}
    for k in dic:
        dic1[k] = len(dic[k])
    return dic1


### CODE FOR get_types() FUNCTION GOES HERE ###
def get_types(dic):
    lst = []
    for k in dic:
        lst.append(k)
    return lst



### CODE FOR get_author_count() FUNCTION GOES HERE ###
def get_author_count(dic,name,v=''):

    if v =='':
        counter  = 0

        for key in dic:
            i = 0
            while i < len(dic[key]):

                author  = dic[key][i]['author']['username']
                i+=1
                if author == name:
                    counter+=1

        return counter
    else:
        counter = 0
        i = 0
        while i < len(dic[v]):
            author = dic[v][i]['author']['username']
            i+=1
            if author == name:
                counter+=1
        return counter






if __name__ == '__main__':
    d = {
            "articles": [{
                "slug": "how-to-train-your-mule",
                "title": "How to train your mule",
                "description": "Ever wonder how?",
                "body": "It takes a Jacobian",
                "tagList": ["mules", "training"],
                "createdAt": "2016-02-18T03:22:56.637Z",
                "updatedAt": "2016-02-18T03:48:35.824Z",
                "favoritesCount": 0,
                "author": {
                  "username": "jake",
                  "bio": "I work at statefarm",
                  "following": False
                }
            }, {
                "slug": "and another article",
                "body": "I'm getting bored",
                "tagList": ["bored", "article"],
                "createdAt": "2016-02-18T03:22:56.637Z",
                "updatedAt": "2016-02-18T03:48:35.824Z",
                "favoritesCount": 20,
                "author": {
                  "username": "cap",
                  "following": True
                }
            }],
            "tweets": [{
                "body": "See my article on training mules.",
                "author": {
                  "username": "jake"
                }
            }]
        }

    print get_types(d)
    print get_types_counts(d)
    print get_author_count(d, 'cap')

    print get_author_count(d, 'jake', ['articles', 'tweets'])