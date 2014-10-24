#! /usr/bin/env python
# Identify the top ten most frequent URLs in a visit log. 

import os
import re
import sys
import heapq

class Solution:
    # INPUT: an array of URLs, and n is the number of URLs we are going to identify.
    def top_urls_no_tie(self, array, n):
        # Build a hash to count the number of times an URL has been visited: 
        url_count = {}
        for url in array:
            if url not in url_count.keys():
                url_count[url] = 0
            url_count[url] += 1

        # Now compute the top most frequent URLs:  
        top_urls = []
        for url in url_count.keys():
            if len(top_urls) < n:
                heapq.heappush(top_urls,(url_count[url], url))
            else:
                heapq.heappushpop(top_urls,(url_count[url], url))

        results = [i[1] for i in top_urls]
        return results
    
    def top_urls_tie(self, array, n):
        # Build a hash to count the number of times an URL has been visited: 
        url_count = {}
        for url in array:
            if url not in url_count.keys():
                url_count[url] = 0
            url_count[url] += 1

        # Now compute the most frequency, and build hashs to store URls with the same frequency:
        count_url = {}
        top_frequency = []

        for url in url_count.keys():
            freq = url_count[url]
            if freq not in count_url.keys():
                count_url[freq] = []
            count_url[freq].append(url)
            if len(top_frequency) < n:
                heapq.heappush(top_frequency,freq)
            else:
                heapq.heappushpop(top_frequency,freq)

        result = []
        for freq in top_frequency:
            result.extend(count_url[freq])
            
        return result

if __name__ == "__main__":
    s = Solution()
    print s.top_urls_no_tie(['a','a','a','a','a','b','b','c','c','c','c','d','aaa','aaa','dddd','f','f','f','e','e','e','e','e'],1)
    print s.top_urls_tie(['a','a','a','a','a','b','b','c','c','c','c','d','aaa','aaa','dddd','f','f','f','e','e','e','e','e'],1)
        

        
        
