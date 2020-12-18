import re

with open("input.txt","r") as f:
    data =[i.rstrip().replace(" ", "") for i in f.readlines()]

class sol(int):
    def __mul__(self, x):
        return sol(int(self) + x)
    def __add__(self, x):
        return sol(int(self) + x)
    def __sub__(self, x):
        return sol(int(self) * x)

def p1(exp : str):
    exp = re.sub(r"(\d+)",r"sol(\1)",exp)
    exp = exp.replace("*", "-")
    return eval(exp,{},{"sol":sol})

print(f"Part 1: {sum(p1(i) for i in data)}")

def p2(exp : str):
    exp = re.sub(r"(\d+)",r"sol(\1)",exp)
    exp = exp.replace("*", "-")
    exp = exp.replace("+", "*")
    return eval(exp,{},{"sol":sol})

print(f"Part 2: {sum(p2(i) for i in data)}")

