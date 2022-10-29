class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        #box[i] = [num boxes, num things in box], Trucksize = how many # boxes
        
        #intuition -> sort array by # of units(descending), fill truck size accordingly
        
        sorted_boxes = sorted(boxTypes, key=lambda x: -x[1])
        result = 0
        
        for box in sorted_boxes:
            
            num_boxes, num_units = box
            
            if truckSize > 0:
                
                box_fit = truckSize - num_boxes
                
                if box_fit > 0:
                    result += num_boxes * num_units
                else:
                    result += truckSize * num_units
              
                truckSize -= num_boxes
            
            
        return result