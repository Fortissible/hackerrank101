#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#
def traverse(graph, queues, visited_table, res, step):
    new_queues = []
    for queue in queues:
        adj_nodes = graph[queue] # Get all adjacent node from queue

        for adj_node in adj_nodes: # Loop through all adjacent node
            if visited_table[adj_node] == 0: # If adjacent node never visited, append to new queue
                new_queues.append(adj_node) 

        visited_table[queue] = 1
        if queue not in res:
            res[queue] = step*6

    # print(f"step {step} with queue {new_queues}")
    # fptr.write(f"step {step} with queue {new_queues}\n")
    new_queues = set(new_queues)
    if len(new_queues) > 0:
        traverse(graph, new_queues, visited_table, res, step+1)
        

def bfs(n, m, edges, s):
    queues = [s]
    graph = {}
    visited_table = {}
    res = {}
    results = []
    for node in range(1, n+1):
        graph[node] = []
        visited_table[node] = 0
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    visited_table[s] = 1
    traverse(graph, queues, visited_table, res, 0)
    for visit_key in visited_table:
        if visited_table[visit_key] == 0:
            res[visit_key] = -1
    for res_key in sorted(res):
        if res_key != s:
            results.append(res[res_key])
    return results

if __name__ == '__main__':
    fptr = open('./output01.txt', 'w')
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()