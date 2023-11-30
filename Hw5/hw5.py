
# Adapted from: https://docs.python.org/3.5/library/heapq.html#priority-queue-implementation-notes
# Adapted from Geeks For Geeks 
# Adapted from StackOverflow



import ast
from collections import defaultdict
import heapq
import itertools
import matplotlib.pyplot as plt
import numpy as np
import os
import re
import time
import unittest
import sys
import pandas as pd

DEBUG = False        # turn on to enable debug prints, False for quiet mode
NUM_RUNS = 20     




def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1



def MST_Kruskal(graph_edges):
    # Initialize data structures
    parent = {}
    rank = {}
    for u, v, w in graph_edges:
        if u not in parent:
            parent[u] = u
            rank[u] = 0
        if v not in parent:
            parent[v] = v
            rank[v] = 0
    
    # Sort the edges by ascending weight
    graph_edges.sort(key=lambda item: item[2])
    
    mst_edges = []
    mst_weight = 0
    
    # Iterate over sorted edges and apply union-find algorithm
    for edge in graph_edges:
        u, v, w = edge
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            mst_edges.append((u, v))
            mst_weight += w
            union(parent, rank, x, y)
    
    return mst_weight, mst_edges






def MST_Prim(graph):
    mst = []  # min span tree edges
    mst_weight = 0  # cumulative weight of all edges in mst
    pq = MinQueue() # min priority queue of all unprocessed vertices

    # create adjacency hash of graph for quick lookup later
    adj_hash = defaultdict(dict)
    for start, end, dist in graph:
        adj_hash[start][end] = dist
        adj_hash[end][start] = dist

    # queue up each vertex with an initial distance of infinity
    for vertex in adj_hash.keys():
        pq.add_task(vertex, np.inf)

    # closest vertex of each node in the MST
    parents = {}

    # set the distance of the first vertex to 0 (start of priority queue)
    first = pq.pop_task()
    pq.add_task(first, 0)

    # go until every vertex is processed
    while pq.values:
        u = pq.pop_task()
        neighbors = adj_hash[u].keys()
        for v in neighbors:
            if v not in pq.values:          # only process vertices still in min queue
                continue
            v_dist = adj_hash[u][v]
            pq_weight = pq.values[v]
            if v_dist < pq_weight:
                pq.add_task(v, v_dist)      # update priority in min queue to the closer
                parents[v] = u              # save the closest parent for building MST

    # build the MST from the parent-child vertex hash
    for vertex, parent in parents.items():
        mst.append((parent, vertex))
        mst_weight += adj_hash[vertex][parent]

    return mst_weight, mst




REMOVED = '<removed-task>'  # placeholder for a removed task
class MinQueue:  # Class to create a min queue with editable priorities
   
    def __init__(self):
        self.pq = []  # list of entries arranged in a heap
        self.entry_finder = {}  # mapping of tasks to entries
        self.counter = itertools.count()  # unique sequence count
        self.values = {}    # quick lookup of priority (allows us to quickly see what vertex is still left)

    def add_task(self, task, priority=0):
        """Add a new task or update the priority of an existing task"""
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)
        self.values[task] = priority

    def remove_task(self, task):
        """Mark an existing task as REMOVED.  Raise KeyError if not found."""
        entry = self.entry_finder.pop(task)
        entry[-1] = REMOVED
        del self.values[task]

    def pop_task(self):
        """Remove and return the lowest priority task. Raise KeyError if empty."""
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not REMOVED:
                del self.entry_finder[task]
                del self.values[task]
                return task
        raise KeyError('pop from an empty priority queue')



















