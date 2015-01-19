#! /usr/bin/python
# Dropbox interview question:
# Input: a directory location
# Output: a list of sublists, each sublist contains files with similar content
# Solution:
# 1. Sharding: partition the files based on their file size.
# 2. Hashing, each file generates a signature, cluster files with the same signature, the goal of hashing is to put files with similar content together, in a compressed way.
#   potential problem: collision. Solution: compare signature and content.
# 3. Hashing methods: 
#   a. md5, 
#   b. by number of lines, 
#   c. randomly sample data points and use as the signature.
# 4. Improvements:
#   a. store content of the clusters on locally, and use a cache of the content when needed, the design of the cache could be the LRU cache. 
#   b.  
# 5. 
# 
import os
import glob

class Solution:
    def __init__(self):
        self.partitions = {}
        self.cache = LRUCache()

    def recursive_file_gen(self, loc):
        # glob, system call find, or google some python library.
        return files

    def get_sign(self, content):
        # generate signature using md5 or some other hashing methods
        # or filesize + first 100 bytes + last 100 bytes
        # or, in the worst case: content of the file.
        return content

    def compare_content(self, key, value):
        return 

    def insert_cluster(self, partition, sign, content, file_name):
        pos = self.cache.lookup(content)
        if pos:
            pos.append(file_name)
        else:
            if partition not in self.partitions.keys():
                self.partitions[partition] = {}
            if sign not in self.partitions[partition].keys():
                self.partitions[partition][sign] = [[content]]
            
            for l in self.partitions[partition][sign]:
                if self.compare_content(content, l[0]):
                    l[0].append(file_name)
                    self.cache.update(content, l)
                    return
            
            self.partitions[partition][sign].append([content, file_name])
            self.cache.update(content, self.partitions[partition][sign][-1])

    # Distribution of the file size would be Zipf, so sharding by something else? 
    def sharing(self, content):
        size = len(content)
        size /= 100

        # return file size
        return size

    def get_clusters(self):
        result = []
        for partition in partitions.keys():
            for sign in partitions[partition].keys():
                for cluster in partitions[partition][sign]:
                    result.append(sign[1:])

        return result

    def cluster_files(self, loc):
        file_lists = self.recursive_file_gen(loc)
        clusters = {}

        for fle in file_lists:
            fin = open(fle, "r")
            cnt = fin.read()
            fin.close()

            # Determine the partition, so that the file can be processed by the hash function in that partition
            #  
            partition = self.sharding(cnt)
            sign = self.get_sign(cnt)
            self.insert_cluster(partition, sign, content, fle)

        return self.get_clusters()

