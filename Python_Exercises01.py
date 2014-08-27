# coding=utf-8
"""有一百个人，分别从1一直到100。现在有人拿枪从第一个开始枪毙，每枪毙一个跳过一个，一直到一轮完成。接着在活着的人里面再次枪毙第一个，间隔一个再枪毙一个，
请问最后活着的是这一百个人里的第几个人？"""
def who_survie(people):
    alive = range(1, people+1)
    while len(alive) > 1:
        alive = alive[1::2]
    return alive[0]
print who_survie(1000000000)


