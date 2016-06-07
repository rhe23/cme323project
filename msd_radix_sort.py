

def msdRadixSort(data, l, maxDigits):
	if len(data) < 10:
		return data.sort()

	radix = 10
	divisor = int(10 ** (maxDigits - l - 1))
	buckets = [[] for _ in range(radix)]
	for elem in data:
		digitAtPos = (elem / divisor) % radix
		buckets[digitAtPos].append(elem)
	divisor /= radix
	if l < maxDigits - 1:
		for i in range(radix):
			if len(buckets[i]) > 0:
				buckets[i] = msdRadixSort(buckets[i], l+1, maxDigits)
	data = [elem for bucket in buckets for elem in bucket] 
	return data
