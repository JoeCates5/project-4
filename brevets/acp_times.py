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
#


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
    if(control_dist_km == 0):
        return brevet_start_time
    totalTime = 0
    while(control_dist_km > 0):
        if((control_dist_km <= 1000 and control_dist_km > 600 and brevet_dist_km != 600) or (brevet_dist_km == 1000 and  control_dist_km <= 1200 and control_dist_km > 1000)):
            print("hello")
            if(control_dist_km > 1000):
                control_dist_km = 1000
            dist = 1000 - control_dist_km if 1000 - control_dist_km != 0 else 400
            distance = 400 - dist if 400 - dist != 0 else 400
            totalTime += distance / 28
            control_dist_km -= distance

        elif((control_dist_km <= 600 and control_dist_km > 400 and brevet_dist_km != 400 ) or (brevet_dist_km == 600 and control_dist_km <= 720 and control_dist_km > 600)):
            if(control_dist_km > 600):
                control_dist_km = 600
            dist = 600 - control_dist_km if 600 - control_dist_km != 0 else 200
            distance = 200 - dist if 200 - dist != 0 else 200
            totalTime += distance / 30
            control_dist_km -= distance

        elif((control_dist_km <= 400 and control_dist_km > 200 and brevet_dist_km != 300 and brevet_dist_km != 200 ) or (brevet_dist_km == 400 and control_dist_km <= 480 and control_dist_km > 400) ):
            if(control_dist_km > 400):
                control_dist_km = 400
            dist = 400 - control_dist_km if 400 - control_dist_km != 0 else 200
            distance = 200 - dist if 200 - dist != 0 else 200
            totalTime += distance / 32
            control_dist_km -= distance

        elif(brevet_dist_km == 300 and control_dist_km <= 360 and control_dist_km > 300):
            if(control_dist_km > 300):
                control_dist_km = 300
            dist = 300 - control_dist_km if 300 - control_dist_km != 0 else 100
            distance = 200 - dist if 200 - dist != 0 else 100
            totalTime += distance / 32
            control_dist_km -= (100 + (control_dist_km - 300))

        elif((control_dist_km <= 200 and control_dist_km > 0) or (brevet_dist_km == 200 and control_dist_km <= 240 and control_dist_km > 200) ):
            if(control_dist_km > 200):
                totalTime += 200 / 34
                control_dist_km -= control_dist_km
            else:
                totalTime += control_dist_km / 34
                control_dist_km = 0


    hours = math.floor(totalTime)
    minutes = round((totalTime - hours) * 60)
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
    totalTime = 0
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



    while(control_dist_km > 0):
        if((control_dist_km <= 1000 and control_dist_km > 600 and brevet_dist_km != 600 ) or (brevet_dist_km == 1000 and  control_dist_km <= 1200 and control_dist_km > 1000)):
            if(control_dist_km > 1000):
                control_dist_km = 1000

            dist = 1000 - control_dist_km if 1000 - control_dist_km != 0 else 400
            distance = 400 - dist if 400 - dist != 0 else 400
            totalTime += distance / 11.428
            control_dist_km -= distance

        elif((control_dist_km <= 600 and control_dist_km > 400 and brevet_dist_km != 400 ) or (brevet_dist_km == 600 and  control_dist_km <= 720 and control_dist_km > 600 )):
            if(control_dist_km > 600):
                control_dist_km = 600
            dist = 600 - control_dist_km if 600 - control_dist_km != 0 else 200
            distance = 200 - dist if 200 - dist != 0 else 200
            totalTime += distance / 15
            control_dist_km -= distance

        elif((control_dist_km <= 400 and control_dist_km > 200 and brevet_dist_km != 200 ) or (brevet_dist_km == 400 and  control_dist_km <= 480 and control_dist_km > 400) ):
            if(control_dist_km > 400):
                control_dist_km = 400

            dist = 400 - control_dist_km if 400 - control_dist_km != 0 else 200
            distance = 200 - dist if 200 - dist != 0 else 200
            totalTime += distance / 15
            control_dist_km -= distance

        elif(brevet_dist_km == 300 and control_dist_km <= 360 and control_dist_km > 300):
            totalTime += 300 / 32
            control_dist_km -= (100 + (control_dist_km - 300))

        elif((control_dist_km <= 200 and control_dist_km > 0) or (brevet_dist_km == 200 and control_dist_km <= 240 and control_dist_km > 200)):
            if(control_dist_km > 200):
                totalTime += 200 / 15
                control_dist_km -= control_dist_km
            else:
                totalTime += control_dist_km / 15
                control_dist_km = 0

    hours = math.floor(totalTime)

    minutes = round((totalTime - hours) * 60)

    shiftedTime = brevet_start_time.shift(hours=hours, minutes=minutes)
    return shiftedTime
