class heap_sort:
    def heap_sort(self, arr):
        le = len(arr)
        a = (le)//2
        # leaf_nodes = [i for i in range(a, le)]
        internal_nodes = [i for i in range(a)]
        internal_nodes.reverse()

        for i in internal_nodes:
            self.sort_triangle(arr, i)
            # untill we reach root node
            # i is the parent nodeits child are 2*i+1 and 2*i+2

        internal_nodes.reverse()
        for i in internal_nodes:
            # untill we reach root node
            # i is the parent nodeits child are 2*i+1 and 2*i+2
            self.sort_triangle(arr, i)

    def sort_triangle(self, arr, i):
        n = len(arr)
        max = i
        left = 2*i+1
        right = 2*i+2
        if left < n and arr[i] < arr[left]:
            max = left
        # else:
        #     max = i
        if right < n and arr[max] < arr[right]:
            max = right
        if max != i:
            # temp = arr[i]
            # arr[i] = arr[max]
            # arr[max] = temp
            # swap
            arr[i], arr[max] = arr[max], arr[i]
        else:
            return

    def heap_del(self, arr):
        self.heap_sort(arr)
        # global q
        temp = arr[0]
        arr[0] = arr[-1]
        le = len(arr)
        arr.pop()
        q.append(temp)

    def print_heap(self, arr):
        m = 0
        le = len(arr)
        i = 0
        while m < le:
            k = 2**i
            for j in range(k):
                if m < le:
                    print(arr[m], end=" ")
                    m += 1
                else:
                    break
            i += 1
            print("")


q = []
heap = heap_sort()
# arr = [15, 20, 7, 9, 30]
# arr = [15, 5, 20, 1, 17, 10, 30]
arr = [15, 5, 20, 1, 17, 10, 30, 76, 3, 29]
# arr = [11, 6, 5, 0, 8, 2, 7]
a = len(arr)
# heap.print_heap(arr)
# heap.print_heap(arr)
heap.heap_sort(arr)
heap.print_heap(arr)
# for i in range(a):
#     heap.heap_del(arr)
# print(q)
