#!/usr/local/bin/python3

from pyHS100 import SmartBulb
import requests
import threading
import time

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
            self.bulb.hsv = color

        return color

    def pollService(self, serviceID):
        header = {
                    'Authorization': 'Token token={}'.format(self.authToken)
                 }
        url = "https://api.pagerduty.com/incidents?statuses%5B%5D=triggered&statuses%5B%5D=acknowledged&service_ids%5B%5D={}&time_zone=UTC&include%5B%5D=services".format(self.serviceID)

        response = requests.get(url, headers=header)
        event = response.json()
        if event['incidents']:
            self.changeStatus(self.red)
        else:
            self.changeStatus(self.green)

    def run(self):
        while True:
            self.pollService(self.serviceID)
            time.sleep(30)
