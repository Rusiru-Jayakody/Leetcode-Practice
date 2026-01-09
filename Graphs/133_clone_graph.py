
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']):
        if not node:
            return None
        o_to_n = {}
        seen = set()
        stk = [node]
        seen.add(node)

        while stk:
            n1 = stk.pop()
            o_to_n[n1] = Node(val = n1.val)
            for nei in n1.neighbors:
                if nei not in seen:
                    stk.append(nei)
                    seen.add(nei)

        for old_node, new_node in o_to_n.items():
            for nei in old_node.neighbors:
                new_nei = o_to_n[nei]
                new_node.neighbors.append(new_nei)

        return o_to_n[node]
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

#Function to create the original graph
def create_original_graph(root, edges):
    if not edges:
        return root
    d = {root.val : root}
    for u,v in edges:
        if u not in d:
            node1 = Node(val = u)
            d[u] = node1
        if v not in d:
            node2 = Node(val = v)
            d[v] = node2
        d[v].neighbors.append(d[u])
        d[u].neighbors.append(d[v])
    return root

#Return the edgelist
def return_edgelist(g):
    edges = []
    visited_nodes = set()
    seen_edges = set()
    stk = [g]
    visited_nodes.add(g)

    while stk:
        node = stk.pop()
        for nei in node.neighbors:
            edge = (node.val, nei.val)
            rev_edge = (nei.val, node.val)
            if rev_edge not in seen_edges:
                edges.append(f"({node.val} <--> {nei.val})")
                seen_edges.add(edge)
            if nei not in visited_nodes:
                visited_nodes.add(nei)
                stk.append(nei)
    return edges


        
if __name__ == "__main__":

    sol = Solution()
    #Input root value
    print("Input root value")
    n = int(input())
    root = Node(val = n)
    print("Enter no of edges")
    no_of_edges = int(input())
    edges = []
    print("Enter the edges line by line as 2 space separated integers")
    for _ in range(no_of_edges):
        edges.append(list(map(int,input().split())))
    graph = create_original_graph(root,edges)
    clone_graph = sol.cloneGraph(graph)
    original_edges = return_edgelist(graph)
    cloned_edges = return_edgelist(clone_graph)

    print(f"Original graph : {original_edges}")
    print(f"Cloned graph   : {cloned_edges}")
        