#!/usr/local/bin/python3

from pyHS100 import SmartBulb
import requests
import threading

class ServiceThread(threading.Thread):
    green = (120, 76, 80)
    red = (0, 100, 100)
    yellow = (60, 100, 100)

    def __init__(self, threadID, serviceID, hostAddress, authToken):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.serviceID = serviceID
        self.bulb = SmartBulb(hostAddress)
        self.authToken = authToken

    def changeStatus(self, color):
        if self.bulb.is_color:
            self.bulb.hsv = self.color

        return self.color

    def pollService(self, serviceID):
        header = {
                    'Authorization': 'Token token={}'.format(self.authToken)
                 }
        url = "https://api.pagerduty.com/incidents?statuses%5B%5D=triggered&service_ids%5B%5D={}&time_zone=UTC&include%5B%5D=services".format(self.serviceID)

        response = requests.get(url, headers=header)
        event = response.json()
        if event['incidents']:
            self.changeStatus(ServiceThread.red)
        else:
            self.changeStatus(ServiceThread.green)

    def run(self):
        while True:
            try:
                self.pollService(self.serviceID)
                time.sleep(30)
            except:
                pass
