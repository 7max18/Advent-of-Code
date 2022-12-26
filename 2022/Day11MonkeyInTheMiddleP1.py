# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 00:08:41 2022

@author: MaxKo
"""
class Monkey:
    inspections = 0
    def __init__(self, items, operation, test, trueTarget, falseTarget):
        self.items = items
        self.operation = operation
        self.test = test
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget
    def InspectAndThrow(self, monkeyArr):
        for item in self.items[:]:
            operator = self.operation[0]
            if operator == "add":
                item += self.operation[1]
            elif operator == "mul":
                item *= self.operation[1]
            elif operator == "pow":
                item *= item
            self.inspections += 1
            item = item // 3
            if item % self.test == 0:
                monkeyArr[self.trueTarget].items.append(item)
            else:
                monkeyArr[self.falseTarget].items.append(item)
        self.items = []

monkeys = []
# monkeys.append(Monkey([79, 98], ("mul", 19), 23, 2, 3))
# monkeys.append(Monkey([54, 65, 75, 74], ("add", 6), 19, 2, 0))
# monkeys.append(Monkey([79, 60, 97], ("pow", 0), 13, 1, 3))
# monkeys.append(Monkey([74], ("add", 3), 17, 0, 1))

monkeys.append(Monkey([63, 84, 80, 83, 84, 53, 88, 72], ("mul", 11), 13, 4, 7))
monkeys.append(Monkey([67, 56, 92, 88, 84], ("add", 4), 11, 5, 3))
monkeys.append(Monkey([52], ("pow", 0), 2, 3, 1))
monkeys.append(Monkey([59, 53, 60, 92, 69, 72], ("add", 2), 5, 5, 6))
monkeys.append(Monkey([61, 52, 55, 61], ("add", 3), 7, 7, 2))
monkeys.append(Monkey([79, 53], ("add", 1), 3, 0, 6))
monkeys.append(Monkey([59, 86, 67, 95, 92, 77, 91], ("add", 5), 19, 4, 0))
monkeys.append(Monkey([58, 83, 89], ("mul", 19), 17, 2, 1))

for roundNum in range(0, 20):
    for monkey in monkeys:
        monkey.InspectAndThrow(monkeys)

activity1 = 0
activity2 = 0

for monkey in monkeys:
    if monkey.inspections > activity2:
        if monkey.inspections > activity1:
            activity2 = activity1
            activity1 = monkey.inspections
        else:
            activity2 = monkey.inspections

monkeyBusiness = activity1 * activity2

print(monkeyBusiness)

