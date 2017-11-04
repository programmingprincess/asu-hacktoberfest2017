import numpy

def bucket(numbers):
    if len(numbers) < 0:
        return numbers
    
    # list of buckets to sort
    buckets = []

    # creating buckets to sort
    for _ in range(0,10):
        buckets.append([])
    
    # going through each element in numbers array
    for num in numbers:
        # sorting into appropriate bucket
        for x in range(0, 10):
            if num >= x*10 and num <= (x*10)+9:
                buckets[x].append(num)
                break

    results = []

    # sorting each bucket and appedning results
    for bucket in buckets:
        results += sort_bucket(bucket)
    
    return results
    
def sort_bucket(numbers):
    # Using a insertion sort to sort each bucket
    for i in range(1, len(numbers)):
        j = i
        while j > 0 and numbers[j-1] > numbers[j]:
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            j -= 1
    return numbers


nums = numpy.random.randint(100, size=20).tolist()
bucket(nums)