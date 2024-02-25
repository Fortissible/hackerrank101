# Class to represent a graph 
class Graph: 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
  
    # Function to add an edge to graph 
    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w]) 
  
    # A utility function to find set of an element i 
    # (truly uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] != i: 
  
            # Reassignment of node's parent 
            # to root node as 
            # path compression requires 
            parent[i] = self.find(parent, parent[i]) 
        return parent[i] 
  
    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 
  
        # Attach smaller rank tree under root of 
        # high rank tree (Union by Rank) 
        if rank[x] < rank[y]: 
            parent[x] = y 
        elif rank[x] > rank[y]: 
            parent[y] = x 
  
        # If ranks are same, then make one as root 
        # and increment its rank by one 
        else: 
            parent[y] = x 
            rank[x] += 1
  
    # The main function to construct MST 
    # using Kruskal's algorithm 
    def KruskalMST(self): 
  
        # This will store the resultant MST 
        result = [] 
  
        # An index variable, used for sorted edges 
        i = 0
  
        # An index variable, used for result[] 
        e = 0
  
        # Sort all the edges in 
        # non-decreasing order of their 
        # weight 
        self.graph = sorted(self.graph, 
                            key=lambda item: item[2]) 
  
        parent = [] 
        rank = [] 
  
        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
  
        # Number of edges to be taken is less than to V-1 
        while e < self.V - 1: 
  
            # Pick the smallest edge and increment 
            # the index for next iteration 
            u, v, w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent, v) 
  
            # If including this edge doesn't 
            # cause cycle, then include it in result 
            # and increment the index of result 
            # for next edge 
            if x != y: 
                e = e + 1
                result.append([u, v, w]) 
                self.union(parent, rank, x, y) 
            # Else discard the edge 
  
        minimumCost = 0
        print("Edges in the constructed MST") 
        for u, v, weight in result: 
            minimumCost += weight 
            print("%d -- %d == %d" % (u, v, weight)) 
        print("Minimum Spanning Tree", minimumCost) 

# def isValidEdge(visit_cnt, edge):
#     if visit_cnt[edge[1]] == 0:
#         return True
#     else:
#         return False
        
# def kruskals(g_nodes, g_from, g_to, g_weight):
#     res_mst = 0
#     visit_cnt = {}
#     covered_edges = []
#     weight_mapping = {}
#     for idx, weight in enumerate(g_weight):
#         if weight in weight_mapping:
#             weight_mapping[weight].append([g_from[idx], g_to[idx]])
#         else:
#             weight_mapping[weight] = [[g_from[idx], g_to[idx]]]
#         visit_cnt[g_from[idx]] = 0
#         visit_cnt[g_to[idx]]= 0
        
#     sorted_weight_mapping = dict(sorted(weight_mapping.items()))
#     for weight_map in sorted_weight_mapping:
#         for edge in sorted_weight_mapping[weight_map]:
#             if len(covered_edges) == g_nodes-1:
#                 continue
#             if isValidEdge(visit_cnt, edge):
#                 print(f"ADDED EDGES {edge[0]}-{edge[1]} TO THE GRAPH NODES ")
#                 visit_cnt[edge[1]] += 1
#                 res_mst += weight_map
#                 covered_edges.append(edge)
#                 print(f"CURRENT COVERED NODES {covered_edges}")
#             else:
#                 print(f"CYCLE DETECTED FOR EDGES {edge[0]}-{edge[1]}")
#     return res_mst

def kruskals(g_nodes, g_from, g_to, g_weight):
    g = Graph(g_nodes)  
    for idx in range(len(g_from)):
        g.addEdge(g_from[idx]-1, g_to[idx]-1, g_weight[idx])
    print(g.graph)
    # Function call 
    g.KruskalMST()

if __name__ == '__main__':

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    print(res)