def largestRectangleArea(heights):
    stack = []
    max_area = 0
        
    # Adding 0 handles the case for computing
    # remaining rectangles in the stack.
    heights.append(0)
    print(heights)
    for idx, curr_rectangle in enumerate(heights):
        print(idx,curr_rectangle)
        print(stack)
        while stack and heights[stack[-1]] > curr_rectangle:
            print(stack[-1])
            popped_rectangle = heights[stack.pop()]
            print(popped_rectangle,"Inside Popped Rectangle")
            # This ternary operator handles the case when we popped the 
            # current shortest rectangle (head of the stack). If so, then
            # the largest area (w/ this rectangle) should be:
            # this rectangle * index of the current rectangle.
            width = idx if not stack else idx - stack[-1] - 1
            print(width,"Inside")
            curr_area = popped_rectangle * width
            max_area = max(max_area, curr_area)
            
        stack.append(idx)
        
    return max_area



#print(largestRectangleArea([2,1,5,6,2,3]))

print(largestRectangleArea([1,2]))

