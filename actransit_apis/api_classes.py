# api_classes.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-02-12 17:12:58
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-02-13 16:14:41



'''
This module contains all the classes used by the API.
These classes provide the interfacing between JSON object returned by AC Transist's
APIs.
The main intention is to eliminate the API calling and focusing on the use of the data instead.
This library will let you concerntrate on your business logic and not worry about the client/consumer
for the ACTransit's APIs.

Note - These classes are only for reading, since they are not going to allow you to change any data.
For modifying data, please create another wrapper on these classes.
'''


# STOPS
# JSON object example - 
# {
#     "StopId": 58123,
#     "Name": "3rd St:Santa Clara Av",
#     "Latitude": 37.7732681,
#     "Longitude": -122.2882275,
#     "ScheduledTime": null
#   }
class ACTransitStop(object):
  '''
  This is the implementation of the object model used by ACTransit for their \
  Stops JSON object.
  '''

  def __init__(self, json_obj):
    '''
    Takes the JSON obj (decoded to python dict) and extracts the stopId, \
    name, latitude, longitude and \
    scheduled_time as the input\
    arguments to make this object.
    '''

    self.__json__ = json_obj
    self.__stopId = json_obj['StopId']
    self.__name = json_obj['Name']
    self.__latitude = json_obj['Latitude']
    self.__longitude = json_obj['Longitude']
    self.__scheduled_time = json_obj['ScheduledTime']

  @property
  def stopId(self):
    '''
    The stopId as per AC Transit system.

    :return: int
    '''

    return self.__stopId

  @property
  def name(self):
    '''
    The name of the stop as per the AC Transit system.

    :return: string
    '''

    return self.__name
  
  @property
  def latitude(self):
    '''
    The latitude of the stop as per the AC Transit system.

    :return: float
    '''

    return self.__latitude

  @property
  def longitude(self):
    '''
    The longitude of the stop as per the AC Transit system.

    :return: float
    '''

    return self.__longitude

  @property
  def scheduled_time(self):
    '''
    The scheduled time for the bus as per the AC Transit system.
    The time a vehicle is scheduled to depart from this stop. 
    Note: The 'date' part of this variable is unimportant, use only the Time.

    :return: date-string 
    '''

    return self.__scheduled_time

  def __repr__(self):
    '''
    repr() calls this method.

    :return: string
    '''

    return 'ACTransitStop({})'.format(repr(self.__json__))





# Predictions
# JSON example -
# {
#     "StopId": 56707,
#     "TripId": 5155418,
#     "VehicleId": 5021,
#     "RouteName": "19",
#     "PredictedDelayInSeconds": 540,
#     "PredictedDeparture": "2017-01-11T17:31:00",
#     "PredictionDateTime": "2017-01-11T17:10:41"
#   }
class ACTransitPrediction(object):
  '''
  This is the implementation of the object model used by ACTransit for their \
  Predictions JSON object.
  '''

  def __init__(self, json_obj):
    '''
    Takes the json_object representation(python dict) as the input and\
    initializes the prediction object.
    '''

    self.__json__ = json_obj
    self.__stopId = json_obj['StopId']
    self.__tripId = json_obj['TripId']
    self.__vehicleId = json_obj['VehicleId']
    self.__route_name = json_obj['RouteName']
    self.__predicted_delay_in_secs = json_obj['PredictedDelayInSeconds']
    self.__predicted_departure = json_obj['PredictedDeparture']
    self.__predicted_date_time = json_obj['PredictionDateTime']

  @property
  def stopId(self):
    '''
    The stopId as per AC Transit system.
    :return: int
    '''

    return self.__stopId

  @property
  def tripId(self):
   '''
   The tripId of the prediction as per the AC Transit system.
   :return: int
   '''

    return self.__tripId

  @property
  def vehicleId(self):
   '''
   The vehicleId of the prediction as per the AC Transit system.
   :return: int
   '''

    return self.__vehicleId

  @property
  def route_name(self):
    '''
    The route name of the prediction as per the AC Transit system.
    :return: string
    '''

    return self.__route_name

  @property
  def predicted_delay_in_seconds(self):
    '''
    The predicted delay in seconds as per the AC Transit system.
    :return: int
    '''

    return self.__predicted_delay_in_secs

  @property
  def predicted_departure(self):
    '''
    The predicted departure as per the AC Transit system.
    The estimated arrival time for the stop. 
    The accuracy of this prediction is closely tied to the PredictionDateTime.
    The closer PredictionDateTime is to the current time, the more accurate this will be. 

    for eg - "2017-01-11T17:31:00"

    :return: datestring (date in string format)
    '''

    return self.__predicted_departure

  @property
  def predicted_date_time(self):
    '''
    The predicted data and time as per AC Transit system.
    The timestamp which the vehicle reported its deviation. 
    Prediction accuracy will diminish as this value gets further in the past.

    for eg - "2017-01-11T17:31:00"

    :return: datestring (date in string format)
    '''

    return self.__predicted_date_time

  def __repr__(self):
    '''
    called by the repr()

    :return: string
    '''

    return 'ACTransitPrediction({})'.format(repr(self.__json__))




# Vehicle
# Wrapper class for holding the realtime information regarding a particular vehicle
# Sample JSON object for the incoming response from ACTransit -
# 
# {
#   "VehicleId": 1,
#   "CurrentTripId": 2,
#   "Latitude": 1.0,
#   "Longitude": 1.0,
#   "Heading": 1,
#   "TimeLastReported": "2017-02-12T18:42:34.7670857-08:00"
# }
class ACTransitVehicle(object):
  '''
  A wrapper class for holding the vehicle information in the ACTransit response JSON.
  Real time informationr regarding a particular vehicle.
  '''

  def __init__(self, json_obj):
    '''
    Initialize the ACTransitVehicle from the JSON object received in the response
    '''

    self.__json__ = json_obj
    self.__vehicle_id = json_obj['VehicleId']
    self.__current_trip_id = json_obj['CurrentTripId']
    self.__latitude = json_obj['Latitude']
    self.__longitude = json_obj['Longitude']
    self.__heading = json_obj['Heading']
    self.__time_last_reported = json_obj['TimeLastReported']


  @property
  def vehicle_id(self):
    '''
    The ID of the vehicle

    :return: int
    '''

    return self.__vehicle_id

  @property
  def current_trip_id(self):
    '''
    The ID of the Trip that the vehicle is currently servicing.

    :return: int
    '''

    return self.__current_trip_id

  @property
  def latitude(self):
    '''
    Latitude coordinate of the vehicle

    :return: float
    '''

    return self.__latitude

  @property
  def longitude(self):
    '''
    Longitude coordinate of the vehicle

    :return: float
    '''

    return self.__longitude

  @property
  def heading(self):
    '''
    The direction the vehicle is currently facing.

    :return: int
    '''

    return self.__heading

  @property
  def time_last_reported(self):
    '''
    Timestamp information for when this vehicle was last reported.

    for eg - "2017-02-12T18:42:34.7670857-08:00"

    :return: datestring (date in string format)
    '''

    return self.__time_last_reported

  def __repr__(self):
    '''
    called by repr()

    :return: string
    '''

    return 'ACTransitVehicle({})'.format(repr(self.__json__))




# GTFSScheduleInfo
# Sample JSON example -
#
# {
#   "UpdatedDate": "2017-02-13T11:19:49.9671828-08:00",
#   "EarliestServiceDate": "2017-02-13T11:19:49.9671828-08:00",
#   "LatestServiceDate": "2017-02-13T11:19:49.9671828-08:00"
# }
class ACTransitGtfsScheduleInfo(object):
  '''
  Wrapper class for the GtfsScheduleInfo JSON response object from ACTransit.
  '''

  def __init__(self, json_obj):
    '''
    Initializes the ACTransitGtfsScheduleInfo object from incoming JSON response
    '''

    self.__json__ = json_obj
    self.__updated_date = json_obj['UpdatedDate']
    self.__earliest_service_date = json_obj['EarliestServiceDate']
    self.__latest_service_date = json_obj['LatestServiceDate']

  @property
  def updated_date(self):
    '''
    The date the GTFS schedule date was last updated.

    for eg - "2017-02-13T11:19:49.9671828-08:00"

    :return: datestring (date in string format)
    '''

    return self.__updated_date

  @property
  def earliest_service_date(self):
    '''
    The first date serviced by the current schedule.

    for eg - "2017-02-13T11:19:49.9671828-08:00"

    :return: datestring (date in string format)
    '''

    return self.__earliest_service_date

  @property
  def latest_service_date(self):
    '''
    The last date serviced by the current schedule.

    for eg - "2017-02-13T11:19:49.9671828-08:00"

    :return: datestring (date in string format)
    '''

    return self.__latest_service_date

  def __repr__(self):
    '''
    called by the repr()

    :return: string
    '''

    return 'ACTransitGtfsScheduleInfo({})'.format(repr(self.__json__))




# ServiceNotice
#
# Sample JSON reponse object from ACTransit - 
# {
#   "PostDate": "2017-02-13T00:57:45.0014771-08:00",
#   "Title": "sample string 1",
#   "NoticeText": "sample string 2",
#   "Url": "sample string 3",
#   "ImpactedRoutes": [
#     "sample string 1",
#     "sample string 2"
#   ]
# }
class ACTransitServiceNotice(object):
  '''
  The wrapper object for ServiceNotice JSON object response from ACTransit APIs.
  This provides information regarding possible delays, detours and/or changes to service.
  '''

  def __init__(self, json_obj):
    '''
    Initializes the ACTransitServiceNotice object from the JSON response object from ACTransit.
    '''

    self.__json__ = json_obj
    self.__post_date = json_obj['PostDate']
    self.__title = json_obj['Title']
    self.__notice_text = json_obj['NoticeText']
    self.__url = json_obj['Url']
    self.__impacted_routes = json_obj['ImpactedRoutes']

  @property
  def post_date(self):
    '''
    The date the notice was posted.

    for eg - "2017-02-13T00:57:45.0014771-08:00"

    :return: datestring (date in string format)
    '''

    return self.__post_date

  @property
  def title(self):
    '''
    The title of the Notice.

    :return: string
    '''

    return self.__title

  @property
  def notice_text(self):
    '''
    The text in the Service Notice, the description.

    :return: string
    '''

    return self.__notice_text

  @property
  def url(self):
    '''
    The URL to the service notice on ACTransit's website.

    :return: string
    '''

    return self.__url

  @property
  def impacted_routes(self):
    '''
    A list of the route names that are impacted by this service notice.
    
    for eg - ["sample string 1", "sample string 2"]

    :return: list(string)
    '''

    return self.__impacted_routes

  def __repr__(self):
    '''
    called by the repr()

    :return: string
    '''
    
    return 'ACTransitServiceNotice({})'.format(repr(self.__json__))




# Route
#
# Sample JSON response object from ACTransit -
#
# {
#   "RouteId": "sample string 1",
#   "Name": "sample string 2",
#   "Description": "sample string 3"
# }
class ACTransitRoute(object):
  '''
  The wrapper for the Route JSON response object from ACTransit APIs.
  It holds the route information.
  '''

  def __init__(self, json_obj):
    '''
    Initializes the ACTransitRoute object from the JSON object from response.
    '''

    self.__json__ = json_obj
    self.__route_id = json_obj['RouteId']
    self.__name = json_obj['Name']
    self.__description = json_obj['Description']

  @property
  def route_id(self):
    '''
    The ID of the route

    :return: string
    '''

    return self.__route_id

  @property
  def name(self):
    '''
    The name of the route as seen by public.

    :return: string
    '''

    return self.__name

  @property
  def description(self):
    '''
    Additional information regarding the route.

    :return: string
    '''

    return self.__description

  def __repr__(self):
    '''
    called by the repr()

    :return: string
    '''

    return 'ACTransitRoute({})'.format(repr(self.__json__))
















