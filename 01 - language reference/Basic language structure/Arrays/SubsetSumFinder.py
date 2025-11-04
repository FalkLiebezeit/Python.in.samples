class SubsetSumFinder:
    """
    Class to find whether a subset of a given array sums up to a target value.
    Uses a backtracking algorithm to explore possible subsets.
    """
    
    def __init__(self):
        self.subset_count = 0  # Tracks total valid subsets found
        self.current_subset = []  # Stores the current subset being explored
    
    def subset_sum(self, numbers, current_sum, index, target):
        """
        Recursively finds subsets that sum to the target value using backtracking.
        
        :param numbers: List of numbers to search within
        :param current_sum: Running sum of the selected subset
        :param index: Current index in the list
        :param target: Desired sum
        """
        
        # Base case: If subset sum matches the target
        if current_sum == target:
            print(f"Subset found => {self.current_subset}")
            self.subset_count += 1
            
            # Continue searching for additional subsets
            if index < len(numbers):
                self.subset_sum(numbers, current_sum - numbers[index - 1], index, target)
            return  # Return to avoid unnecessary execution
        
        # Generate possible subsets
        for i in range(index, len(numbers)):
            self.current_subset.append(numbers[i])  # Include current number
            self.subset_sum(numbers, current_sum + numbers[i], i + 1, target)  # Recursively search further
            self.current_subset.pop()  # Remove last element to backtrack


# Driver code
numbers1 = [1, 3, 5, 2, 7]
target1 = 10
solver1 = SubsetSumFinder()
solver1.subset_sum(numbers1, 0, 0, target1)
print(f"Total subsets found: {solver1.subset_count}")

numbers2 = [1, 3, 7, 5, 9, 11]
target2 = 12
solver2 = SubsetSumFinder()
solver2.subset_sum(numbers2, 0, 0, target2)
print(f"Total subsets found: {solver2.subset_count}")