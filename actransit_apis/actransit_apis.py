# actransit_apis.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-01-11 14:48:11
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-02-12 17:26:05


__author__ = 'sidmishraw'

# __PERSONAL_API_KEY__ = '7A94EF436CDBB9F1FB8624E0632CD54B'
__PERSONAL_API_KEY__ = None

# The base URL for the AC Transit APIs
__BASE_URL__ = 'https://api.actransit.org/transit'


# for processing JSON
from json import dumps
from json import loads
from json import JSONDecoder
from json import JSONEncoder

# Pyhton wrapper classes for the APIs
from api_classes import ACTransitStop
from api_classes import ACTransitPrediction

# for processing the requests(sending)
from urllib.request import urlopen
from urllib.request import Request

# for processing the response(receiving)
import urllib.response

# gonna use the webbrowser to ping me when theh bus is nearby
import webbrowser


# Call this method first to start using the library
# Needs the User's personal API KEY generated from ACTransit's dev website.
def set_api_key(api_key):
  '''
  Sets the API key for the APIs to use.
  By default the API key is set to None and this needs to be set before using the
  functionality of this library.
  '''

  global __PERSONAL_API_KEY__ 

  __PERSONAL_API_KEY__ = api_key
  return



#
# API wrappers for AC Transit
#

# GET stops
# Retrieve all of AC Transit's currently active stops.
def get_stops():
  '''
  Gets all currently activ stops of the ACTransit system.
  :return: [ACTransitStop] - Returns a list of ACTransitStop objects
  which are populated after calling the ACTransit API.
  '''
  global __PERSONAL_API_KEY__

  url = '{}/stops/?token={}'.format(__BASE_URL__, __PERSONAL_API_KEY__)
  json_obj = None
  json_decoder = JSONDecoder()
  with urlopen(url) as req:
    json_obj = str(req.read(), encoding = 'utf-8')
  json_obj = json_decoder.decode(json_obj)
  ac_transit_stops = []
  for obj in json_obj:
    ac_transit_stops.append(ACTransitStop(obj))
  return ac_transit_stops




# GET stops/{latitude}/{longitude}/{distance}/{routeName}
# Retrieve all active stops within a certain radius (in feet) 
# of the given point. The default search radius is 500 feet.
def get_active_stops(latitude, longitude, search_radius = 500):
  '''
  Retrieve all active stops within a certain radius (in feet) \
  of the given point. The default search radius is 500 feet.
  '''

  pass



# GET stops/{latitude}/{longitude}?distance={distance}&routeName={routeName}
# Retrieve all active stops within a certain radius (in feet) 
# of the given point. The default search radius is 500 feet.
def get_active_stops_type2(latitude, longitude, search_radius = 500):
  '''
  Retrieve all active stops within a certain radius (in feet) \
  of the given point. The default search radius is 500 feet.
  '''
  
  pass




# GET stops/{stopId}/predictions  
# Retrieve vehicle predictions for a particular stop.
def get_predictions(stopId):
  '''
  Retrieve vehicle predictions for a particular stop.
  '''

  pass




def main():
  '''
  main function does nothing since this is going to be a library module.\
  This cannot be run standalone as the main module. If run as main module, \
  this script does nothing.
  '''
  # because this is going to be a library module
  # the main function should do nothing if this module is executed as
  # the main module.
  pass




if __name__ == '__main__':
  main()