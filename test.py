from generate_data import *
from naive_radix_sort import *
from naive_merge_sort import *
from msd_radix_sort import *
from inplace_radix_sort import *
from paradis import *
import copy
import time

def testSortingFunction(funcName, sortingFunction, args):
	start = time.time()
	sortedData = sortingFunction(*args)
	end = time.time()
	print "%s complete. Time elapsed - %.4fs" % (funcName, end - start)
	isSorted = all(sortedData[i] <= sortedData[i+1] for i in range(len(sortedData)-1))
	print "Valid sorted list check: %r" % isSorted

def mergeVsRadixTests():
	test1()
	test2()
	test3()

def experiments():
	test4()
	test5()
	test6()
	test7()

def test1():
	data = generateData(1000000, 0, 9999)
	dataCopy = copy.deepcopy(data)
	testSortingFunction("Naive radix sort", naiveRadixSort, (dataCopy, 4))

	dataCopy = copy.deepcopy(data)
	testSortingFunction("Naive mergesort", naiveMergeSort, (dataCopy,))

def test2():
	data = generateData(100000, 0, 9.99e15)
	dataCopy = copy.deepcopy(data)
	testSortingFunction("Naive radix sort", naiveRadixSort, (dataCopy, 16))

	dataCopy = copy.deepcopy(data)
	testSortingFunction("Naive mergesort", naiveMergeSort, (dataCopy,))

def test3():
	data = generateData(100000, 0, 9.99e15)
	dataCopy = copy.deepcopy(data)
	testSortingFunction("Naive radix sort", naiveRadixSort, (dataCopy, 16))

	dataCopy = copy.deepcopy(data)
	testSortingFunction("Naive mergesort", naiveMergeSort, (dataCopy,))

def test4():
	data = generateData(1000000, 0, 9999)
	dataCopy = copy.deepcopy(data)
	testSortingFunction("Naive radix sort", naiveRadixSort, (dataCopy, 4))
	dataCopy = copy.deepcopy(data)
	testSortingFunction("MSD radix sort", msdRadixSort, (dataCopy, 0, 4))
	dataCopy = copy.deepcopy(data)
	testSortingFunction("In-place parallel radix sort", inPlaceRadixSort, (dataCopy, 0, 4, 0, 1000000))
	dataCopy = copy.deepcopy(data)
	testSortingFunction("PARADIS", paradis, (dataCopy, 0, 4, 10, 0, 1000000))

def test5():
	data = generateData(1000000, 0, 9.99e15)
	dataCopy = copy.deepcopy(data)
	testSortingFunction("Naive radix sort", naiveRadixSort, (dataCopy, 16))
	dataCopy = copy.deepcopy(data)
	testSortingFunction("MSD radix sort", msdRadixSort, (dataCopy, 0, 16))
	dataCopy = copy.deepcopy(data)
	testSortingFunction("In-place parallel radix sort", inPlaceRadixSort, (dataCopy, 0, 16, 0, 1000000))
	dataCopy = copy.deepcopy(data)
	testSortingFunction("PARADIS", paradis, (dataCopy, 0, 16, 10, 0, 1000000))

def test6():
	data = generateData(1000000, 0, 9999)
	dataCopy = copy.deepcopy(data)
	testSortingFunction("Naive radix sort", naiveRadixSort, (dataCopy, 4))
	dataCopy = copy.deepcopy(data)
	testSortingFunction("MSD radix sort", msdRadixSort, (dataCopy, 0, 4))
	dataCopy = copy.deepcopy(data)
	testSortingFunction("In-place parallel radix sort", inPlaceRadixSort, (dataCopy, 0, 4, 0, 1000000))
	dataCopy = copy.deepcopy(data)
	testSortingFunction("PARADIS", paradis, (dataCopy, 0, 4, 10, 0, 1000000))

def test7():
	data = generateData(10000000, 0, 9.99e15)
	dataCopy = copy.deepcopy(data)
	testSortingFunction("Naive radix sort", naiveRadixSort, (dataCopy, 16))
	dataCopy = copy.deepcopy(data)
	testSortingFunction("MSD radix sort", msdRadixSort, (dataCopy, 0, 16))
	dataCopy = copy.deepcopy(data)
	testSortingFunction("In-place parallel radix sort", inPlaceRadixSort, (dataCopy, 0, 16, 0, 10000000))
	dataCopy = copy.deepcopy(data)
	testSortingFunction("PARADIS", paradis, (dataCopy, 0, 16, 10, 0, 10000000))

def test7():
	data = generateData(10000000, 0, 9999)
	dataCopy = copy.deepcopy(data)
	testSortingFunction("Naive radix sort", naiveRadixSort, (dataCopy, 4))
	dataCopy = copy.deepcopy(data)
	testSortingFunction("MSD radix sort", msdRadixSort, (dataCopy, 0, 4))
	dataCopy = copy.deepcopy(data)
	testSortingFunction("In-place parallel radix sort", inPlaceRadixSort, (dataCopy, 0, 4, 0, 10000000))
	dataCopy = copy.deepcopy(data)
	testSortingFunction("PARADIS", paradis, (dataCopy, 0, 4, 10, 0, 10000000))

#mergeVsRadixTests()
#experiments()


