
"""
Python Basic Lab 2-0
Compute distance between
2 cities using latitude & longitude

get_cities()
    making dict {key:= name : val:= loc}
        loc:= (lat, lon) <- tuple

get_city_by_name(cities, name)
    get loc from cities <- using DB from get_cities

city_dist()
    interact with user
"""
import math


"""
just copy & paste 2 functions 
from distEarth.py
- radian(d
- dist_between_loc(loc1, loc2)
"""
# convert degree to radian
def radian(d):
    """
    just copy and paste from distEarth.py
    """
    return math.radians(d)


# distance between loc1 & loc2
# using latitude & longitude
def dist_between_loc(loc1, loc2):
    """
    just copy and paste from distEarth.py
    """
    # earth's radius
    r = 6371000  # meter

    # convert latitudes of loc1 and loc2 to radian
    lat1, lat2 = radian(loc1[0]), radian(loc2[0])
    lon1, lon2 = radian(loc1[1]), radian(loc2[1])

    # convert difference of longitudes to radian
    #   : compute difference in degree form
    cos_theta = (math.sin(lat1)*math.sin(lat2) 
                + math.cos(lat1)*math.cos(lat2)*math.cos(radian(math.degrees(lon2) - math.degrees(lon1))))

    # cos(theta) : theta - radian of two location

    # get theta by acos
    theta = (math.acos(cos_theta))

    # radius * theta = distance (r * 2pi = circumference of circle)
    return r * theta


# from 'cities.txt' get
# name of city                  <- str      : key
# (latitide, longitude) loc     <- tuple    : val
# => make cities                <- dict
def get_cities():
    """
    :return: cities <- dict {key:= name : val:= loc}
                    loc:= (lat, lon) <- tuple
    """
    # try to open file : 'cities.txt'
    try:
        fi = open('./cities.txt')

    except:
        print("There no file!!")
        exit(0)

    # make cities
    cities = dict()
    # read info from file line by line
    for line in fi:
        # split the line
        splited_line = line.split('\t')
        for i, word in enumerate(splited_line):
            splited_line[i] = word.rstrip(',')
        # get city name without country name
        # print(splited_line)
        if not cities.get(splited_line[0], 0):
            cities[splited_line[0]] = (float(splited_line[-2]), float(splited_line[-1]))
        # get latitude & longitude

        # store info in names & locs
    # print(cities)
    # return names & locs
    return cities


# get location (lat, lon) by name
def get_city_by_name(cities, name):
    """
    :param cities: dict {key:= name : val:= loc}
    :param name: name of city to find
    :return: loc <- (latitude, longitude) : tuple
    """
    # check name is in cities
    # if there are no such name, return None
    
    return cities.get(name, None)


# interface
def city_dist():
    """
    :return: None
    """
    # call 'the get_cities' to get a DB
    cities = get_cities()
    # while user enter 'EXITprogram' processing
    while True:
        # call input() with out parameter
        city = input()
        # be careful '\n' : using strip()
        city = city.strip('\n')
        # if 'EXITprogram' stop the program
        if city == 'EXITprogram':
            break
        # get two locs using 'get_city_by_name'
        names = city.split(', ')
        print(names)
        name1 = get_city_by_name(cities, names[0])
        name2 = get_city_by_name(cities, names[1])
        
        # CAUTION : two city names separated by ', '

        # if loc1 and loc2 in cities's name print dist
        if name1 and name2:
            dist_between_loc(dist_between_loc(cities(name1), cities(name2)))
        elif not name1:
            print('There are no city: ', names[0])
        elif not name2:
            print('There are no city: ', names[1])

        # else print 'There are no ~' (~ : wrong name)

    # exit the program
    # CAUTION : if user enter 'EXITprogram', then print 'exit'
    get_cities()
    print('exit')
    exit(0)


if __name__ == '__main__':
    city_dist()
