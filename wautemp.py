# jsb/plugs/myplugs/wautemp.py
#
#
# author: g. dawes
 
from jsb.lib.examples import examples
from jsb.lib.commands import cmnds
from jsb.utils.url import geturl2
from jsb.imports import getjson

import urllib2
import logging
import sys

def get_temp(bot, ievent):
    """No arguments - just fetch the temp. """
    try:
        thermopage = geturl2('http://www.met.wau.nl/veenkampen/data/C_current.txt',timeout=10).split()
        currentline = thermopage[-1]
        data = currentline.split(',')
        temp = str(round(float(data[2]),1))
        humid = str(round(float(data[8]),1))
        precip = data[19]
        pressure = str(float(data[21]))
        windspeed = str(round(float(data[22]),1))
        windangle = float(data[26])+11.25
        winddir = ''
        if windangle>0 and windangle<= 22.5: winddir = 'N'
        if windangle>22.5 and windangle<= 45: winddir = 'NNE'
        if windangle>45 and windangle<= 67.5: winddir = 'NE'
        if windangle>67.5 and windangle<= 90: winddir = 'ENE'
        if windangle>90 and windangle<= 112.5: winddir = 'E'
        if windangle>112.5 and windangle<= 135: winddir = 'ESE'
        if windangle>135 and windangle<= 157.5: winddir = 'SE'
        if windangle>157.5 and windangle<= 180: winddir = 'SSE'
        if windangle>180 and windangle<= 202.5: winddir = 'S'
        if windangle>202.5 and windangle<= 225: winddir = 'SSW'
        if windangle>225 and windangle<= 247.5: winddir = 'SW'
        if windangle>247.5 and windangle<= 270: winddir = 'WSW'
        if windangle>270 and windangle<= 292.5: winddir = 'W'
        if windangle>292.5 and windangle<= 315: winddir = 'WNW'
        if windangle>315 and windangle<= 337.5: winddir = 'NW'
        if windangle>337.5 and windangle<= 360: winddir = 'NNW'
        if windangle>360 and windangle<= 382.5: winddir = 'N'
        ievent.reply(temp+' C, '+humid+'% humidity, '+windspeed+' m/s '+winddir+', '+precip+' mm precipitation, '+pressure+' kPa.')
    except urllib2.URLError:
        ievent.reply('Cannot read from server.')        
    except:
        ievent.reply('What is this madness? '+ str(sys.exc_info()[0]))
 

cmnds.add("wau-temp", get_temp, ["OPER", "USER", "GUEST"])
examples.add("wau-temp", "Get temperature from the WAU service.", "wau-temp")
