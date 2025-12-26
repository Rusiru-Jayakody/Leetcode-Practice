import ast
class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []
      
    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.min_stk:
            self.min_stk.append(val)
        elif self.min_stk[-1] < val:
            self.min_stk.append(self.min_stk[-1])
        else:
            self.min_stk.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]
        

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = MinStack()
    operations = input().split()   #Input operators as -->  MinStack, push , pop ...
    values_str = input()           #Input values as --> [], [2], [-5], []
    values = ast.literal_eval(values_str)
    results = []
    obj = None

    for op, val in zip(operations, values):
        if op == "MinStack":
            obj = MinStack()
            results.append(None)
        elif op == "push":
            obj.push(val[0])
            results.append(None)
        elif op == "pop":
            obj.pop()
            results.append(None)
        elif op == "top":
            results.append(obj.top())
        elif op == "getMin":
            results.append(obj.getMin())

print(results)
        