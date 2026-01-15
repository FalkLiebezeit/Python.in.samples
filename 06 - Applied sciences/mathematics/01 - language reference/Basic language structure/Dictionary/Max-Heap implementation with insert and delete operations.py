class Heap:
    """
    Max-Heap implementation with insert and delete operations.
    Maintains the heap property after each operation.
    """

    def __init__(self):
        # Initialize the heap as an empty list
        self.heap_array = []

    def display_heap(self):
        """Display the heap as a 1-D array."""
        print(self.heap_array)

    def parent(self, i):
        """Return the index of the parent node for node i."""
        return (i - 1) // 2

    def insert(self, k):
        """
        Insert a new value into the heap and restore heap property.
        Args:
            k (int): Value to insert.
        """
        self.heap_array.append(k)
        self.fix_up(len(self.heap_array) - 1)
        self.display_heap()

    def fix_up(self, i):
        """
        Move the node at index i up to restore heap property.
        Args:
            i (int): Index of the node to move up.
        """
        while i > 0 and self.heap_array[self.parent(i)] < self.heap_array[i]:
            p = self.parent(i)
            self.heap_array[p], self.heap_array[i] = self.heap_array[i], self.heap_array[p]
            i = p

    def fix_down(self, i):
        """
        Move the node at index i down to restore heap property.
        Args:
            i (int): Index of the node to move down.
        """
        n = len(self.heap_array)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < n and self.heap_array[left] > self.heap_array[largest]:
                largest = left
            if right < n and self.heap_array[right] > self.heap_array[largest]:
                largest = right

            if largest == i:
                break

            self.heap_array[i], self.heap_array[largest] = self.heap_array[largest], self.heap_array[i]
            i = largest

    def delete(self, i):
        """
        Delete the element at index i from the heap and restore heap property.
        Args:
            i (int): Index of the element to delete.
        """
        n = len(self.heap_array)
        if n == 0 or i >= n:
            return None
        # Swap with last element and remove it
        self.heap_array[i], self.heap_array[n - 1] = self.heap_array[n - 1], self.heap_array[i]
        self.heap_array.pop()
        # Restore heap property
        if i < len(self.heap_array):
            self.fix_down(i)
            self.fix_up(i)
        self.display_heap()

# --- Testing the Heap class ---
if __name__ == "__main__":
    h1 = Heap()
    h1.insert(50)   # [50]
    h1.insert(10)   # [50, 10]
    h1.insert(30)   # [50, 10, 30]
    h1.delete(1)    # [50, 30]
    h1.insert(20)   # [50, 30, 20]
    h1.insert(80)   # [80, 50, 20, 30]
    h1.delete(2)    # [80, 50, 30]
    h1.insert(70)   # [80, 70, 30, 50]