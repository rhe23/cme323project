from pathos.multiprocessing import ProcessingPool as Pool
from multiprocessing import Process, Queue
import copy
from generate_data import *

def paradis(data, l, k, p, start, end):
	# This optimization is done because sorting small arrays via
	# comparison sort is quicker
	if end - start < 10:
		tmp = data[start:end]
		tmp.sort()
		data[start:end] = tmp
		return data
	histogram = buildHistogram(data, l, k, p, start, end)
	heads = [start]
	tails = [start + histogram[0]]
	for i in range(1, 10):
		heads.append(heads[i-1] + histogram[i-1])
		tails.append(tails[i-1] + histogram[i])
	
	starts = copy.deepcopy(heads)
	ends = copy.deepcopy(tails)

	for i in range(0, 10):
		while heads[i] < tails[i]:
			v = data[heads[i]]
			b = determineDigitBucket(v, l, k)
			while b != i:
				v, data[heads[b]] = data[heads[b]], v
				heads[b] += 1
				b = determineDigitBucket(v, l, k)
			data[heads[i]] = v
			heads[i] += 1

	if l < k - 1:
		processes = []
	 	queue = Queue()
	 	for i in range(10):
	 		proc = Process(target=paradis, args=(data, l, k, p, starts[i], ends[i]))
	 		processes.append(proc)
	 		proc.start()
	 	for proc in processes:
	 		proc.join()
	return data


def buildHistogram(data, l, k, p, start, end):
	increment = int((end - start) / p)
	if increment <= 2:
		return countHistogram(data, l, k, start, end)
	totalCounts = [0] * 10
	starts = []
	ends = []
	for i in xrange(start, start + increment * p, increment):
		j = i + increment
		if i == start + increment * (p - 1):
			j = end
		starts.append(i)
		ends.append(j)
	individualCounts = Pool(p).map(countHistogram, [data] * 10, [l] * 10, [k] * 10, starts, ends)
	for counts in individualCounts:	
		for i in range(10):
			totalCounts[i] += counts[i]
	return totalCounts


def countHistogram(data, l, k, start, end):
	counts = [0] * 10
	for i in range(start, end):
		digit = determineDigitBucket(data[i], l, k)
		counts[digit] += 1
	return counts

def determineDigitBucket(elem, l, k):
	return (elem / (10 ** (k - l - 1))) % 10  # (l+1)'th MSD 