from pythonds.basic import Queue
def hotLine(namelist,num):
    simqueue=Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()
print(hotLine(["babu","devi","subha","kane","able","jeffrey"],7))
