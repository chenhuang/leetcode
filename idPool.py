#! /usr/bin/python
# data structure that supports the assign and release of IDs

class Solution:
    def __init__(self, capacity):
        self.used_id = set()
        self.unused_id = []
        self.capacity = capacity
        self.max_id = 0

    def assign_id(self):
        if len(self.unused_id) == 0:
            if self.max_id < self.capacity:
                self.max_id += 1
                self.used_id.append(self.max_id)
            else:
                return -1
        else:
            return self.used_id.pop(0)

    def release_id(self, id):
        if id not in self.used_id():
            return False
        else:
            self.usused_id.append(id)
            self.used_id.remove(id)
            return True

