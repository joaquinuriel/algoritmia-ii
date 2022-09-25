def initCounter(initial = 0):
    counter = int(initial)
    def inc(n = 1):
        global counter
        counter += n
        return counter
    return counter, inc

init = initCounter()