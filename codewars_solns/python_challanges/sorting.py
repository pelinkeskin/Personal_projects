myarr=[6, 3, 0, 5]


def sort_buble_sort(myarr):
    n=len(myarr)
    for i in range(n):
        swapped=False
        for j in range(n-i-1):
            if myarr[j]>myarr[j+1]:
                myarr[j],myarr[j+1]=myarr[j+1],myarr[j]
                swapped=True
        if swapped == False:
            break
    return myarr
print("buble_sort \n",sort_buble_sort(myarr))

myarr=[6, 3, 0, 5]
def selection_sort(myarr):
    n=len(myarr)
    for i in range(n):
        min_ind=i
        for j in range(i+1,n):
            if myarr[min_ind]>myarr[j]:
               min_ind=j
        myarr[i],myarr[min_ind]=myarr[min_ind],myarr[i]
    return myarr
print("selection_sort \n",selection_sort(myarr))

myarr=[6, 3, 0, 5]
def mergesort(myarr):
    if len(myarr)>1:
        mid = len(myarr)//2
        L=myarr[:mid]
        R=myarr[mid:]
        mergesort(L)
        mergesort(R)
        i=j=k=0
        while i<len(L) and j < len(R):
            if L[i]<R[j]:
                myarr[k]=L[i]
                i+=1
            else: 
                myarr[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            myarr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            myarr[k]=R[j]
            j+=1
            k+=1
        return myarr
print("merge_sort \n",mergesort(myarr))

myarr=[6, 3, 0, 5]
def quicksort(myarr):
    def partition(arr,low,high):
        pivot=arr[high]
        i=low-1
        for j in range(low,high):
            if arr[j]<=pivot:
                i=i+1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[high]=arr[high],arr[i+1]
        return i+1
    
    def sort(arr,low,high):
        if low<high:
            pi=partition(arr,low,high)
            sort(arr,low,pi-1)
            sort(arr,pi+1,high)
            
    sort(myarr,0,len(myarr)-1)
    return myarr

print("quicksort \n",quicksort(myarr))