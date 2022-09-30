import random

aoq = ["xs", "还行", "有毒", "?", "qs", "艹", "笑死", "确实", "？"]
while(True):
    n = input("你问aoq:")
    num = random.randint(0, len(aoq))
    if num == len(aoq):
        print("aoq没有回复你" + '\n')
    else:
        print("aoq回复了：" + aoq[num] + '\n')