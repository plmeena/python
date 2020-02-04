class Sorting():

    @staticmethod
    def bubble_sort(elements):
        n = len(elements)
        # Traverse entire array
        for i in range(n):
            for j in range(0, n - i - 1):
                # Every iteration will bubble largest element at the end, so exclude already
                # sorted elements(n-i-1)
                if elements[j] > elements[j + 1]:
                    Sorting.swap(elements, j, j + 1)

    @staticmethod
    def selection_sort(elements):
        n = len(elements)
        # Traverse entire array
        for i in range(n):
            minindex = i;
            for j in range(i, n):
                if elements[j] < elements[minindex]:
                    minindex = j
                    # Every iteration will find minimum element from unsorted array and place in sorted array's next
                    # location

            Sorting.swap(elements, i, minindex)

    @staticmethod
    def insertion_sort(elements):
        n = len(elements)
        # Traverse entire array
        for i in range(1, n):
            j = i - 1
            key = elements[i];
            # Store key to compare and swap with all the elements of sorted array to find right place
            while j >= 0 and key < elements[j]:
                Sorting.swap(elements, j + 1, j)
                j = j - 1

    @staticmethod
    def quick_sort(elements, low, high):
        if low < high:
            pi = Sorting.partitioning_position(elements, low, high)
            Sorting.quick_sort(elements, low, pi - 1)
            Sorting.quick_sort(elements, pi + 1, high)

    @staticmethod
    def partitioning_position(elements, low, high):
        pivot = elements[high];
        i = low
        j = high
        while i < j:  # Keep trying till left reference crosses right reference

            while i < j and elements[i] <= pivot:  # Keep moving left reference to
                #  right till both reference crosses each other and
                # element greater than pivot found
                i = i + 1
            while j > i and elements[
                j] >= pivot:  # Keep moving right reference to left
                # till both reference crosses each other and element less than pivot found
                j = j - 1

            if i < j:
                Sorting.swap(elements, i, j)

        Sorting.swap(elements, i, high)

        return i

    @staticmethod
    def partition(arr, low, high):
        i = (low - 1)  # index of smaller element
        pivot = arr[high]  # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    @staticmethod
    def merge_sort(elements, low, high):
        if low < high:
            mid = (low + high) // 2
            Sorting.merge_sort(elements, low, mid)
            Sorting.merge_sort(elements, mid + 1, high)
            Sorting.merge(elements, low, mid, high)

    @staticmethod
    def merge(elements, low, mid, high):

        temp = [0] * (high - low + 1)

        i = low
        j = mid + 1
        k = 0
        while i <=mid and j <= high :
            if elements[i] < elements[j]:
                temp[k] = elements[i]
                k += 1
                i += 1
            else:
                temp[k] = elements[j]
                k += 1
                j += 1

        for l in range(i, mid+1):
            temp[k] = elements[l]
            k += 1

        for m in range(j, high+1):
            temp[k] = elements[m]
            k += 1

        for n in range(0, high-low+1):
            elements[n + low] = temp[n]

    @staticmethod
    def swap(elements, i, j):
        temp = elements[i]
        elements[i] = elements[j]
        elements[j] = temp

    @staticmethod
    def print_elements(elements):
        for element in enumerate(elements):
            print(element)

# numbers = [5, 4, 7, 2, 3, 8, 9, 10]
numbers = [5, 4, 7, 2, 3, 8, 9, 10, -1, -3, 100, 50, 60, 34, 904, -87, -30, 0, 1, 5, 7]
# Sorting.bubble_sort(numbers)
# Sorting.selection_sort(numbers)
# Sorting.insertion_sort(numbers)
Sorting.merge_sort(numbers, 0, len(numbers) - 1)
# Sorting.quick_sort(numbers, 0, len(numbers) - 1)
Sorting.print_elements(numbers)
