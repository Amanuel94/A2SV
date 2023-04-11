"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
                
        for employee in employees:
            if employee.id == id:
                return self.dfs(employee, set(), employees)
            
            
    def findEmp(self, id, employees):
        for employee in employees:
            if employee.id == id:
                return employee
        
                
        
        
        
        
    def dfs(self, employee, vis, employees):
        total = employee.importance
        vis.add(employee.id)
        for subordinate in employee.subordinates:
            if subordinate not in vis:
                total+=self.dfs(self.findEmp(subordinate, employees), vis, employees)
        return total