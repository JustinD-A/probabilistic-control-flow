import random

class P_Obj:
  def __init__(self, name, probability):
    self.name = name
    self.p = probability

def p_print(obj):
    if obj.p > 1 or obj.p < 0: print("Input needs to be between 0 and 1.")
    elif random.random() < obj.p: print(True)
    else: print(False)

if __name__ == "__main__":
    firstObj = P_Obj("first", .8)
    for i in range(9):
        p_print(firstObj)