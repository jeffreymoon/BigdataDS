
"""
distEarth : compute distance between
2 location using latitude & longitude

-> using math library

radian(d)
    convert degree to radian

dist_between_loc(loc1, loc2)
    compute distance between 2 locations

loc_dist()
    interface that interacts with user
"""
import math
import sys


# convert degree to radian
def radian(d):
    """
    :param d: degree
    :return: radian that converted from degree
    """

    return math.radians(d)


# distance between loc1 & loc2
# using latitude & longitude
def dist_between_loc(loc1, loc2):
    """
    :param loc1: (latitude, longitude)
    :param loc2: (latitude, longitude)
        -> tuple that contains latitude at index 0,
                               longitude at index 1
    :return: distance between 2 location
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


# interact with user
def loc_dist():
    """
    get two location (pair of latitude & longitude)
        loc := tuple contains lat & lon
    print distance between 2 locations
    :return: None
    """
    # call input() function without parameter
    # get first loc's latitude & longitude
    loca1 = [float(a) for a in sys.stdin.readline().split()]
    loca2 = [float(a) for a in sys.stdin.readline().split()]

    # store at tuple
    # loc1 = (37.455813, 126.954699)
    loc1 = (loca1[0], loca1[1])

    # get second loc's latitude & longitude

    # store at tuple
    # loc2 = (37.266653, 126.999386)
    loc2 = (loca2[0], loca2[1])

    # print distance between 2 locations
    print(dist_between_loc(loc1, loc2))


if __name__ == '__main__':
    loc_dist()
