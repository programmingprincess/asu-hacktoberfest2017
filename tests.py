import numpy
import sys
sys.path.insert(0, 'sorting')

nums = numpy.random.randint(100, size=20).tolist()
sortedNums = sorted(nums)

try:
    from bubble import bubble
    if(bubble(list(nums)) == sortedNums):
        print "bubblesort success!"
    else:
        print "bubblesort incorrect."
except:
    print "bubblesort function errored or is incomplete."
try:
    from insertion import insertion
    if(insertion(list(nums)) == sortedNums):
        print "insertionsort success!"
    else:
        print "insertionsort incorrect."
except:
    print "insertionsort function errored or is incomplete."
try:
    from merge import mergesort
    if(mergesort(list(nums)) == sortedNums):
        print "mergesort success!"
    else:
        print "mergesort incorrect."
except:
    print "mergesort function errored or is incomplete."
try:
    from quick import quick
    if(quick(list(nums)) == sortedNums):
        print "quicksort success!"
    else:
        print "quicksort incorrect."
except:
    print "quicksort function errored or is incomplete."

try:
    from heap import heap
    if(heap(list(nums)) == sortedNums):
        print "Heap Sort success!"
    else:
        print "Heap Sort incorrect."
except:
    print "Heapsort function errored or is incomplete."

try:
    from bucket import bucket
    if(bucket(list(nums)) == sortedNums):
        print "Bucket Sort success"
    else:
        print "Bucket Sort incorrect"
except:
    print "Bucketsort function errored or is incomplete"
