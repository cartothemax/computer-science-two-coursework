"""
File: countfig.py
Prints the number of calls of a recursive Fibonacci
function with problem sizes that double.
"""

class Counter(object):
    """Tracks a count."""

    def __init__(self):
        self._number = 0

    def increment(self):
        self._number +=1

    def __str__(self):
        return str(self._number)

def fib(n, counter):
    """Count the number of calls of the Fibonacci
    function."""

    counter.increment()
    if n < 3:
        return 1
    else:
        return fib(n-1, counter) + fib(n-2, counter)

    problemSize = 2
    print "%12s%15s" % ("Problem size", "calls")
    for count in xrange(5):
        counter = Counter()

        #the start of the algorithm
        fib(problemSize, counter)
        #end of algorithm

        print "%12s%15s" % (prolemSize, counter)
        prolemSize *= 2
