This class is to integrate the PagerDuty API with TP-Link SmartBulbs. In it's
current state it checks a PagerDuty service for any triggered incidents. If the
outputted json returns an incident it changes the SmartBulb from green to red.

Features:
- MultiThreaded: it can poll multiple services and respond to multiple lights
simultaneously
- HSV colors can be overwrote for custom color definitions
- Service Polling occurs every 30 seconds but this value can be overrode as well

Supported Devices:

Currently this has only been tested with the TP-Link LB130 but other TP Link
devices should work as well, and will be tested in the future

Usage:

PDService1 = ServiceThread(threadID=1,
                          serviceID='serviceID',
                          hostAddress='LIGHTIP',
                          authToken='AUTHTOKEN')
<br>                          
PDService2 = ServiceThread(threadID=1,
                          serviceID='serviceID',
                          hostAddress='LIGHTIP',
                          authToken='AUTHTOKEN')                        
