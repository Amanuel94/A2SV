class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        vertices = set(range(n))
        
        for edge in edges:
            
            vertices.discard(edge[-1])
            
        return list(vertices)
