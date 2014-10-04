#! /usr/bin/env python

import os
import re
import sys


# topological sort
# The idea of topological sorting is to iteratively identify "sink" nodes: nodes with outdegree of zero, and update the graph by remove the sink nodes.
# In order to do that, need to keep a table of nodes' outdegree, and update the table accordingly. 
# One approach is to keep a table of edges and reverse the graph's edges, then the question becomes to remove nodes with 0 indegree, then propagate and update the graph. 
#

# edges is a hash of edges, each key is a node_id, value is a list of node_ids. 
class topological_sorting:
    def t_sorting(self, edges):
        reversed_edges = {}
        in_degree = {}

        # reverse the graph, compute the indegree
        for source_node in edges.keys():
            edges = edges[node]
            for target_node in edges:
                if target_node not in reversed_edges.keys():
                    reversed_edges[target_node] = []
                    in_degree[target_node] = 0
                reversed_edges[target_node].append(source_node)
                in_degree[target_node] += 1

            if source_node not in reversed_edges.keys():
                reversed_edges[source_node] = []
                in_degree[target_node] = 0

        # iterate the graph and identify nodes with 0 indegree:
        queue = []

        for node in in_degree.keys():
            if in_degree[node] == 0:
                queue.append(node)

        # output list
        while len(queue) > 0:
            node = queue.pop(0)
            output_list.append(node)
            for child in reversed_edges[node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)

        return output_list
                
                
            
            

        
            
            
            

        




