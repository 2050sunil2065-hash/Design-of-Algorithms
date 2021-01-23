#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
import matplotlib.pyplot as plt
import time
Rx = [1,2,5,3,9,7] #Rx is a random list


# In[2]:


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList)//2
        left = myList[:mid]
        right = myList[mid:]
        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1
            
            
            
        


# In[3]:


def bubbleSort(myList):
    for passnum in range(len(myList)-1,0,-1):
        for i in range(passnum):
            temp = myList[i]
            myList[i] = myList[i + 1]
            myList[i+1] = temp
            


# In[4]:


def selectionSort(myList):
    for i in range(len(myList)):
        min_idx = i
        for j in range(i + 1, len(myList)):
            if myList[min_idx] > myList[j]:
                min_idx = j
        myList[i], myList[min_idx] = myList[min_idx], myList[i]


# In[30]:


# Python program for implementation of heap Sort 
  
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
        
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 


# In[6]:



  
 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key


# In[7]:


def quickSort(array):

 n = len(array)
 array = array

 def quickSortRecursion(low, high):
   if(low >= high):
     return
     
   mid = ( int )( ( low + high ) / 2 )

   # Finding Median
   if( ( ( array[low] <= array[mid] ) and ( array[mid] <= array[high] ) ) or ( ( array[high] <= array[mid] ) and ( array[mid] <= array[low] ) ) ):
     pass
   elif( ( ( array[mid] <= array[low] ) and ( array[low] <= array[high] ) ) or ( ( array[high] <= array[low] ) and ( array[low] <= array[mid] ) ) ):
     temp = array[low]
     array[low] = array[mid]
     array[mid] = temp
   elif( ( ( array[low] <= array[high] ) and ( array[high] <= array[mid] ) ) or ( ( array[mid] <= array[high] ) and ( array[high] <= array[low] ) ) ):
     temp = array[high]
     array[high] = array[mid]
     array[mid] = temp

   pivot = array[ mid ]
   array[ mid ] = array[ high ]

   i = low
   j = high - 1
   while( i <= j ):
     while( i < high and array[i] <= pivot ):
       i += 1
     while( j >= low and array[j] >= pivot ):
       j -= 1

     if( i < j ):
       temp = array[ i ]
       array[ i ] = array[ j ]
       array[ j ] = temp
       i += 1
       j -= 1

   array[ high ] = array[ j + 1 ]
   array[ j + 1 ] = pivot

   quickSortRecursion(low, j)
   quickSortRecursion(j + 2, high)
   return array
 
 quickSortRecursion(0, n-1)
 return array


# In[17]:


print("Merge sort in action")
y1=[]
result1 =[]

for x in range(1000,5000,1000):
    mylist = [ random.randint(0, x) for i in range(x)]
    start=time.time()
    mergeSort(mylist)
#print(myList)
    time.sleep(1)
    end = time.time()
#print(f"Runtime taken: {end-start}")
    t = "{0:.4f}".format(1000*(end - start))
    print("Time :" + str(1000*(end - start)) + "ms")
    result1.append(float(1000*(end - start)))
    y1.append(x)
print(result1)
print(y1)
plt.figure(figsize=(5,5))
plt.xlabel("Array Size")
plt.ylabel("Time Taken To Execute")
plt.plot(y1,result1)
plt.legend(["mergeSort"])
plt.show()


# In[18]:



print("Bubble sort in action.")
result2 = []
y2 = []
for x in range(1000,5000,1000):
    mylist = [ random.randint(0, x) for i in range(x)]
    start=time.time()
    bubbleSort(mylist)
#print(myList)
    time.sleep(1)
    end = time.time()
#print(f"Runtime taken: {end-start}")
    t = "{0:.4f}".format(1000*(end - start))
    print("Time :" + str(1000*(end - start)) + "ms")
    result2.append(float(1000*(end - start)))
    y2.append(x)
print(result2)
print(y2)
plt.figure(figsize=(5,5))
plt.xlabel("Array Size")
plt.ylabel("Time Taken To Execute")
plt.plot(y2,result2)
plt.legend(["bubbleSort"])
plt.show()


# In[19]:


print("selection sort in action")
result3 = []
y3 = []
for x in range(1000,5000,1000):
    mylist = [ random.randint(0, x) for i in range(x)]
    start=time.time()
    selectionSort(mylist)
#print(myList)
    time.sleep(1)
    end = time.time()
#print(f"Runtime taken: {end-start}")
    t = "{0:.4f}".format(1000*(end - start))
    print("Time :" + str(1000*(end - start)) + "ms")
    result3.append(float(1000*(end - start)))
    y3.append(x)
print(result3)
print(y3)
plt.figure(figsize=(5,5))
plt.xlabel("Array Size")
plt.ylabel("Time Taken To Execute")
plt.plot(y3,result3)
plt.legend(["selectionSort"])
plt.show()


# In[20]:


print("Heap sort in action")
result4 = []
y4 = []
for x in range(1000,5000,1000):
    mylist = [ random.randint(0, x) for i in range(x)]
    start=time.time()
    heapSort(mylist)
#print(myList)
    time.sleep(1)
    end = time.time()
#print(f"Runtime taken: {end-start}")
    t = "{0:.4f}".format(1000*(end - start))
    print("Time :" + str(1000*(end - start)) + "ms")
    result4.append(float(1000*(end - start)))
    y4.append(x)
print(result4)
print(y4)
plt.figure(figsize=(5,5))
plt.xlabel("Array Size")
plt.ylabel("Time Taken To Execute")
plt.plot(y4,result4)
plt.legend(["HeapSort"])
plt.show()



# In[21]:


print("Insertion sort in action")
result5 = []
y5 = []

for x in range(1000,5000,1000):
    mylist = [ random.randint(0, x) for i in range(x)]
    start=time.time()
    insertionSort(mylist)
#print(myList)
    time.sleep(1)
    end = time.time()
#print(f"Runtime taken: {end-start}")
    t = "{0:.4f}".format(1000*(end - start))
    print("Time :" + str(1000*(end - start)) + "ms")
    result5.append(float(1000*(end - start)))
    y5.append(x)
print(result5)
print(y5)
plt.figure(figsize=(5,5))
plt.xlabel("Array Size")
plt.ylabel("Time Taken To Execute")
plt.plot(y5,result5)
plt.legend(["InsertionSort"])
plt.show()


# In[22]:


print("quick sort in action")
result6 = []
y6 = []
for x in range(1000,5000,1000):
    mylist = [ random.randint(0, x) for i in range(x)]
    start=time.time()
    bubbleSort(mylist)
#print(myList)
    time.sleep(1)
    end = time.time()
#print(f"Runtime taken: {end-start}")
    t = "{0:.4f}".format(1000*(end - start))
    print("Time :" + str(1000*(end - start)) + "ms")
    result6.append(float(1000*(end - start)))
    y6.append(x)
print(result6)
print(y6)
plt.figure(figsize=(5,5))
plt.xlabel("Array Size")
plt.ylabel("Time Taken To Execute")
#plt.axis([1000,1010, 1000, 5000])
plt.plot(y6,result6)
plt.legend(["quickSort"])
plt.show()


# In[29]:


plt.plot(y1,result1)
plt.plot(y2,result2)
plt.plot(y3,result3)
plt.plot(y4,result4)
plt.plot(y5,result5)
plt.plot(y6,result6)
plt.xlabel("Array Size")
plt.ylabel("Time Taken To Execute")
plt.legend(["mergeSort", "bubbleSort","selectionSort","heapSort","insertionSort","quickSort"])


# In[27]:


mergeSort(Rx)
bubbleSort(Rx)
selectionSort(Rx)
heapSort(Rx)
insertionSort(Rx)
quickSort(Rx)


# In[ ]:




