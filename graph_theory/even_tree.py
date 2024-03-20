#!/bin/python3

import math
import os
import random
import re
import sys

def traverseForest(route_table, current_node):
    if current_node in route_table:
        ttl_brnch_node = 0
        res = 0
        for adj_node in route_table[current_node]:
            print(f"Current node in {current_node}, traversing to node {adj_node}")
            branch_node, prev_res = traverseForest(route_table, adj_node)
            ttl_brnch_node += branch_node
            if (branch_node % 2 == 0):
                print("EDGES CAN BE RECUDED")
                res += 1
            res += prev_res
            print(f"Current traversed node {branch_node}, Do backward to {current_node}")
            print(f"CAN BE REDUCED {res}")
        if current_node != 1:
            return ttl_brnch_node + 1, res
        else:
            return res
    else:
        print(f"Leaf {current_node} Reached")
        return 1, 0 #ret leaf node and possible edges reduced (0 because it is a leaf)
        
    

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    route_table = {}
    res = 0
    for idx in range(t_edges):
        if t_to[idx] not in route_table:
            route_table[t_to[idx]] = [t_from[idx]]
        else:
            route_table[t_to[idx]].append(t_from[idx])
    print(route_table)
    res = traverseForest(route_table, 1)
    return res

if __name__ == '__main__':
    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)
    print(res)