class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Start with -1 since the last element always becomes -1
        max_from_right = -1  
        
        # Iterate backwards from the last index down to 0
        for i in range(len(arr) - 1, -1, -1):
            # Save the current element before overwriting it
            current_element = arr[i]  
            
            # Replace current element with the max seen to its right
            arr[i] = max_from_right   
            
            # Update the max seen so far for the next iterations
            if current_element > max_from_right:
                max_from_right = current_element
                
        return arr

        