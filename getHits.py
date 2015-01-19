#! /usr/bin/python

import os
import sys
import threading
import time

class Solution:
    def __init__:
        self.count = {}
        self.last_cleaned_time = None
        self.interval = 300

    def hit():
        cur_time = int(time.time())
        if cur_time not in self.count.keys():
            self.count[cur_time] = 0
        self.count[cur_time] += 1

        if self.last_cleaned_time is None:
            self.last_cleaned_time = cur_time
        else:
            if self.last_cleaned_time < cur_time - self.interval:
                for i in range(self.last_cleaned_time, cur_time - self.interval + 1):
                    if i in self.count.keys():
                        self.count.pop(i)
                self.last_cleaned_time = cur_time - self.interval
            

    def getHits():
        cur_time = int(time.time())
        hits = 0
        for i in range(cur_time - self.interval + 1, cur_time + 1):
            if i in self.count.keys():
                hits += self.count[i]
        return hits
            

