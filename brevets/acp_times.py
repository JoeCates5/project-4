"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math

#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.


def helperFunction(brevit_length, control, dict, previous_bracket):
    if(control > brevit_length):
        control = brevit_length
    distance = control - previous_bracket
    totalTime = distance / dict.get(previous_bracket)
    control -= distance
    return [control, totalTime]


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    dict = {0:34, 200:32, 400:30, 600:28}
    timeSum = 0
    while(control_dist_km > 0):
        if((control_dist_km <= 1000 and control_dist_km > 600 and brevet_dist_km != 600) or (brevet_dist_km == 1000 and  control_dist_km <= 1200 and control_dist_km > 1000)):
            returnList = helperFunction(brevet_dist_km, control_dist_km, dict, 600)
            control_dist_km = returnList[0]
            timeSum += returnList[1]

        elif((control_dist_km <= 600 and control_dist_km > 400 and brevet_dist_km != 400 ) or (brevet_dist_km == 600 and control_dist_km <= 720 and control_dist_km > 600)):
            returnList = helperFunction(brevet_dist_km, control_dist_km, dict, 400)
            control_dist_km = returnList[0]
            timeSum += returnList[1]

        elif((control_dist_km <= 400 and control_dist_km > 200 and brevet_dist_km != 200 and brevet_dist_km != 300) or (brevet_dist_km == 400 and control_dist_km <= 480 and control_dist_km > 400) ):
            returnList = helperFunction(brevet_dist_km, control_dist_km, dict, 200)
            control_dist_km = returnList[0]
            timeSum += returnList[1]

        elif((brevet_dist_km == 300 and control_dist_km <= 360 and control_dist_km > 300) or (brevet_dist_km == 300 and control_dist_km > 200 and  control_dist_km <= 300)):
            returnList = helperFunction(brevet_dist_km, control_dist_km, dict, 200)
            control_dist_km = returnList[0]
            timeSum += returnList[1]

        elif((control_dist_km <= 200 and control_dist_km > 0) or (brevet_dist_km == 200 and control_dist_km <= 240 and control_dist_km > 200) ):
            returnList = helperFunction(brevet_dist_km, control_dist_km, dict, 0)
            control_dist_km = returnList[0]
            timeSum += returnList[1]

    hours = math.floor(timeSum)
    minutes = round((timeSum - hours) * 60)
    shiftedTime = brevet_start_time.shift(hours=hours, minutes=minutes)
    return shiftedTime




def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    if(control_dist_km == 0):
        shiftedTime = brevet_start_time.shift(hours=1)
        return shiftedTime

    if(control_dist_km >= brevet_dist_km):
        if(brevet_dist_km == 200):
            shiftedTime = brevet_start_time.shift(hours=13.5)
            return shiftedTime
        if(brevet_dist_km == 400):
            shiftedTime = brevet_start_time.shift(hours=27)
            return shiftedTime
        if(brevet_dist_km == 600):
            shiftedTime = brevet_start_time.shift(hours=40)
            return shiftedTime
        if(brevet_dist_km == 1000):
            shiftedTime = brevet_start_time.shift(hours=75)
            return shiftedTime

    dict = {0:15, 200:15 , 400:15, 600:11.428}
    timeSum = 0

    if(control_dist_km <= 60):
        distance = control_dist_km - 0
        timeSum = distance / 20
        timeSum += 1
        hours = math.floor(timeSum)
        minutes = round((timeSum - hours) * 60)
        shiftedTime = brevet_start_time.shift(hours=hours, minutes=minutes)
        return shiftedTime

    while(control_dist_km > 0):
        if((control_dist_km <= 1000 and control_dist_km > 600 and brevet_dist_km != 600) or (brevet_dist_km == 1000 and  control_dist_km <= 1200 and control_dist_km > 1000)):
            returnList = helperFunction(brevet_dist_km, control_dist_km, dict, 600)
            control_dist_km = returnList[0]
            timeSum += returnList[1]

        elif((control_dist_km <= 600 and control_dist_km > 400 and brevet_dist_km != 400 ) or (brevet_dist_km == 600 and control_dist_km <= 720 and control_dist_km > 600)):
            returnList = helperFunction(brevet_dist_km, control_dist_km, dict, 400)
            control_dist_km = returnList[0]
            timeSum += returnList[1]

        elif((control_dist_km <= 400 and control_dist_km > 200 and brevet_dist_km != 200 and brevet_dist_km != 300) or (brevet_dist_km == 400 and control_dist_km <= 480 and control_dist_km > 400) ):
            returnList = helperFunction(brevet_dist_km, control_dist_km, dict, 200)
            control_dist_km = returnList[0]
            timeSum += returnList[1]

        elif((brevet_dist_km == 300 and control_dist_km <= 360 and control_dist_km > 300) or (brevet_dist_km == 300 and control_dist_km > 200 and  control_dist_km <= 300)):
            returnList = helperFunction(brevet_dist_km, control_dist_km, dict, 200)
            control_dist_km = returnList[0]
            timeSum += returnList[1]

        elif((control_dist_km <= 200 and control_dist_km > 0) or (brevet_dist_km == 200 and control_dist_km <= 240 and control_dist_km > 200)):
            returnList = helperFunction(brevet_dist_km, control_dist_km, dict, 0)
            control_dist_km = returnList[0]
            timeSum += returnList[1]

    hours = math.floor(timeSum)
    minutes = round((timeSum - hours) * 60)
    shiftedTime = brevet_start_time.shift(hours=hours, minutes=minutes)
    return shiftedTime
