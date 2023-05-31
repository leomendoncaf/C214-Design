from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSortStrategy(SortStrategy):
    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

class SelectionSortStrategy(SortStrategy):
    def sort(self, data):
        n = len(data)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if data[j] < data[min_idx]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
        return data

class MergeSortStrategy(SortStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]
        
        self.sort(left_half)
        self.sort(right_half)
        
        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1
        
        return data

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def sort_data(self, data):
        return self.strategy.sort(data)

# EXEMPLO
data = [7, 2, 5, 1, 8, 3]

sorter = Sorter(BubbleSortStrategy())
sorted_data = sorter.sort_data(data)
print("Bubble Sort:", sorted_data)

sorter.set_strategy(SelectionSortStrategy())
sorted_data = sorter.sort_data(data)
print("Selection Sort:", sorted_data)

sorter.set_strategy(MergeSortStrategy())
sorted_data = sorter.sort_data(data)
print("Merge Sort:", sorted_data)
