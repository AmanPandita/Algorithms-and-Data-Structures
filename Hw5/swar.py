
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





def locate_leader(cluster_heads, element):
    if cluster_heads[element] == element:
        return element
    return locate_leader(cluster_heads, cluster_heads[element])

def merge_clusters(cluster_heads, cluster_sizes, element1, element2):
    root1 = locate_leader(cluster_heads, element1)
    root2 = locate_leader(cluster_heads, element2)

    if cluster_sizes[root1] < cluster_sizes[root2]:
        cluster_heads[root1] = root2
    elif cluster_sizes[root1] > cluster_sizes[root2]:
        cluster_heads[root2] = root1
    else:
        cluster_heads[root2] = root1
        cluster_sizes[root1] += 1

def MST_Kruskal(edges_list):
    # Establish cluster heads and sizes
    cluster_heads = {}
    cluster_sizes = {}
    for start, end, cost in edges_list:
        if start not in cluster_heads:
            cluster_heads[start] = start
            cluster_sizes[start] = 0
        if end not in cluster_heads:
            cluster_heads[end] = end
            cluster_sizes[end] = 0
    
    # Order edges by their cost
    edges_list.sort(key=lambda edge: edge[2])
    
    mst_edges_collected = []
    total_cost = 0
    
    # Go through ordered edges to build the MST
    for edge in edges_list:
        start, end, cost = edge
        leader_start = locate_leader(cluster_heads, start)
        leader_end = locate_leader(cluster_heads, end)
        if leader_start != leader_end:
            mst_edges_collected.append((start, end))
            total_cost += cost
            merge_clusters(cluster_heads, cluster_sizes, leader_start, leader_end)
    
    return total_cost, mst_edges_collected





def MST_Prim(graph_structure):
    spanning_tree_edges = []  # Edges in the minimum spanning tree
    total_weight = 0  # Total weight of all edges in the spanning tree
    vertices_queue = PriorityQueue()  # Priority queue for the vertices

    # Create a dictionary to store adjacency info for quick access
    adjacency = defaultdict(dict)
    for src, dest, weight in graph_structure:
        adjacency[src][dest] = weight
        adjacency[dest][src] = weight

    # Initialize all vertices in the priority queue with infinite distance
    for vertex in adjacency:
        vertices_queue.insert(vertex, float('inf'))

    # Record the nearest vertex in the spanning tree
    nearest_vertices = {}

    # Start with the first vertex in the queue and set its distance to 0
    initial_vertex = vertices_queue.extract()
    vertices_queue.insert(initial_vertex, 0)

    # Process vertices until all are included in the spanning tree
    while vertices_queue.entries:
        current = vertices_queue.extract()
        for neighbour in adjacency[current]:
            if neighbour not in vertices_queue.entries:
                continue
            edge_weight = adjacency[current][neighbour]
            current_priority = vertices_queue.entries[neighbour]
            if edge_weight < current_priority:
                vertices_queue.insert(neighbour, edge_weight)
                nearest_vertices[neighbour] = current

    # Construct the minimum spanning tree from the nearest vertices information
    for node, closest in nearest_vertices.items():
        spanning_tree_edges.append((closest, node))
        total_weight += adjacency[node][closest]

    return total_weight, spanning_tree_edges

MARKER = '<removed>'  # Flag for removed tasks
class PriorityQueue:
    def __init__(self):
        self.heap = []  # Heap of entries
        self.task_map = {}  # Map of tasks to entries
        self.sequence = itertools.count()  # Unique sequence number
        self.entries = {}  # Map of tasks to their priorities for quick reference

    def insert(self, task, priority=0):
        """Insert a new task or update the priority of an existing one"""
        if task in self.task_map:
            self.discard(task)
        seq = next(self.sequence)
        entry = [priority, seq, task]
        self.task_map[task] = entry
        heapq.heappush(self.heap, entry)
        self.entries[task] = priority

    def discard(self, task):
        """Mark a task as removed or raise KeyError if not found"""
        entry = self.task_map.pop(task)
        entry[-1] = MARKER
        del self.entries[task]

    def extract(self):
        """Remove and return the task with the lowest priority"""
        while self.heap:
            priority, seq, task = heapq.heappop(self.heap)
            if task != MARKER:
                del self.task_map[task]
                del self.entries[task]
                return task
        raise KeyError('pop from an empty priority queue')
