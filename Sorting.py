class Sorting:

    # order of N^2
    # Stable
    # Inplace
    @staticmethod
    def bubble_sort(nums):

        print('\nBubble Sorting:\n')
        for i in range(len(nums)-1):
            for j in range(0, len(nums)-i-1, 1):
                if nums[j] > nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        return nums

    # order of n^2
    # not a stable
    # better than merge /quick sort for small arrays
    # less write operations than insertion sort
    @staticmethod
    def selection_sort(nums):

        print('\nSelection Sort:\n')
        for i in range(len(nums)-1):
            index = i
            for j in range(i+1, len(nums), 1):
                if nums[j] < nums[index]:
                    index = j
            if index != i:
                temp = nums[index]
                nums[index] = nums[i]
                nums[i] = temp
        return nums

    # order of n^2
    # stable
    # Adaptive
    # Inplace
    @staticmethod
    def insertion_sort(nums):

        print('\nInsertion Sort:\n')
        for i in range(len(nums)):
            j = i
            while j>0 and nums[j-1]>nums[j]:
                temp = nums[j]
                nums[j] = nums[j-1]
                nums[j-1] = temp
                j = j - 1
        return nums

    # order of n log n
    # Not a stable
    # Inplace
    @staticmethod
    def quick_sort(nums, low, high):

        if low >= high:
            return

        pivot_index = Sorting.partition(nums, low, high)
        Sorting.quick_sort(nums, low, pivot_index-1)
        Sorting.quick_sort(nums, pivot_index+1, high)

        return nums

    # Stable
    # Order n log n
    # Not Inplace
    @staticmethod
    def merge_sort(nums):

        if len(nums) == 1:
            return nums

        middle_index = len(nums)//2
        left_half = nums[:middle_index]
        right_half = nums[middle_index:]
        left_half = Sorting.merge_sort(left_half)
        right_half = Sorting.merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i = i + 1
            else:
                nums[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            nums[k] = left_half[i]
            i = i + 1
            k = k + 1
        while j < len(right_half):
            nums[k] = right_half[j]
            j = j + 1
            k = k + 1

        return nums

    @staticmethod
    def partition(nums, low, high):

        pivot_index = (low+high)//2
        nums = Sorting.swap(nums, pivot_index, high)
        i = low
        for j in range(low, high, 1):
            if nums[j] <= nums[high]:
                nums = Sorting.swap(nums, i, j)
                i = i + 1
        Sorting.swap(nums, i, high)

        return i

    @staticmethod
    def swap(array, i, j):

        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        return array


if __name__ == "__main__":

    array_to_sort = [1, 10, -2, -22, -1, -5]

    print(Sorting.bubble_sort(array_to_sort))
    print(Sorting.selection_sort(array_to_sort))
    print(Sorting.insertion_sort(array_to_sort))
    print('\nQuick Sort:\n')
    print(Sorting.quick_sort(array_to_sort, 0, len(array_to_sort)-1))
    print('\nMerge Sort\n')
    print(Sorting.merge_sort(array_to_sort))
