
def inPlaceRadixSort(data, l, k, start, end):
	if end - start < 10:
		tmp = data[start:end]
		tmp.sort()
		data[start:end] = tmp
		return data
	histogram = countHistogram(data, l, k, p, start, end)
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
	 	for i in range(10):
	 		inPlaceRadixSort(data, l, k, p, starts[i], ends[i])
	return data

def countHistogram(data, l, k, start, end):
	counts = [0] * 10
	for i in range(start, end):
		digit = determineDigitBucket(data[i], l, k)
		counts[digit] += 1
	return counts

def determineDigitBucket(elem, l, k):
	return (elem / (10 ** (k - l - 1))) % 10  # (l+1)'th MSD 