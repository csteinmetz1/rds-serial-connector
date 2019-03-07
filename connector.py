import json
import time
import sched
import serial
import urllib.request

class Connector:

    def __init__(self):
        # WSBF now playing api
        self.api = 'https://wsbf.net/api/shows/now.php'
        self.data = {}
        self.msg = ""
        self.new = False

        # setup serial connection
        self.serial = None

        # setup event scheduler
        self.sched = sched.scheduler(time.time, time.sleep)
        self.update()
        self.sched.run() 

    def get_now_playing(self):
        with urllib.request.urlopen(self.api) as now:
            new_data = json.loads(now.read().decode())

        # save data on change and set flag 
        if new_data != self.data:
            self.data = new_data
            self.new = True
        
    def construct_msg(self):
        self.msg = f"DPS={self.data['lb_track_name']} - {self.data['lb_artist']}\n"

    def transmit_msg(self):
        print(self.msg)		# send serial msg to 730
        self.new = False 	# set flag back

    def update(self):
        self.get_now_playing()
        if self.new:
            self.construct_msg()
            self.transmit_msg()
        self.sched.enter(10, 1, self.update) # update every 10 sec

if __name__ == '__main__':
    c = Connector()
