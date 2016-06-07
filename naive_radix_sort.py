import copy

def naiveRadixSort(data, maxDigits):
	radix = 10
	divisor = 1
	for digitPos in range(maxDigits):
		buckets = [[] for _ in range(radix)]
		for elem in data:
			digitAtPos = (elem / divisor) % radix
			buckets[digitAtPos].append(elem)
		divisor *= radix
		data = [elem for bucket in buckets for elem in bucket]
	return data

