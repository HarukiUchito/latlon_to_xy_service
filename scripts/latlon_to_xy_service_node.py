#!/usr/bin/env python
# -*- coding: utf-8 -*-
from latlon_to_xy_service.srv import *
import rospy
import pyproj

import sys

EPSG4612 = pyproj.Proj("+init=EPSG:4612")
EPSG2451 = pyproj.Proj("+init=EPSG:2451")

def callback(req):
    #print "recieved new lon/lat %s, %s"%(req.longitude, req.latitude)
    ry, rx = pyproj.transform(EPSG4612, EPSG2451, req.longitude,req.latitude)
    #print "converted to x/y %s, %s"%(rx, ry)

    return ConvLatLonResponse(rx, ry)


def main():
    rospy.init_node('latlon_to_xy_service', anonymous=True)

    s = rospy.Service('latlon_to_xy_service', ConvLatLon, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException: pass

