import random

aoq = ["xs", "笑死", "还行", "有毒", "?", "？", "qs", "确实", "草", "艹"]
while(True):
    n = input("你问aoq：")
    num = random.randint(0, len(aoq))
    if num == len(aoq):
        print("aoq没有回复你。" + '\n')
    else:
        print("aoq：" + aoq[num] + '\n')