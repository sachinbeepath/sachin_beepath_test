## Ormuco Technical Test 

## Question A

def overlap(line1,line2):
    '''
      Consumes a two lines on the x-axis, l1 and l2, as tuples (x1,x2) and (x3,x4) and returns 
      a string indicating whether or not the two lines over lap.
      
      overlap: Tpl Tpl  -> Str
     
      
      Examples:
          overlap((3,6),(4,8)) => "The two lines overlap."
          overlap((3,6),(7,14)) => "The two lines do not overlap."
   '''
    # first transform the lines so the points are in increasing order 
    ordered_line1 = (min(line1),max(line1))
    ordered_line2 = (min(line2),max(line2))
    
    # compare the beginning of one line to the end of the other
    if ordered_line1[0] <= ordered_line2[1] and ordered_line2[0] <= ordered_line1[1]:
        return "The two lines overlap."
    else:
        return "The two lines do not overlap."


### Tests

# beginning of second line is smaller than the end of first
x1, x2 = (1,4)
x3, x4 = (3,5)
print("x1:",x1, "x2:",x2,"x3:",x3, "x4:",x4,overlap((x1,x2),(x3,x4)))

# beginning of second line equals the end of first
x1, x2 = (-1,2)
x3, x4 = (2,3)
print("x1:",x1, "x2:",x2,"x3:",x3, "x4:",x4,overlap((x1,x2),(x3,x4)))

# beginning of second line is equal to beginning of first
x1, x2 = (6,3)
x3, x4 = (3,4)
print("x1:",x1, "x2:",x2,"x3:",x3, "x4:",x4,overlap((x1,x2),(x3,x4)))

# end of second line is equal than the end of first
x1, x2 = (2,5)
x3, x4 = (-3,5)
print("x1:",x1, "x2:",x2,"x3:",x3, "x4:",x4,overlap((x1,x2),(x3,x4)))

# second line is within first
x1, x2 = (0,9)
x3, x4 = (3,6)
print("x1:",x1, "x2:",x2,"x3:",x3, "x4:",x4,overlap((x1,x2),(x3,x4)))

# beginning of second line is greater than the end of first
x1, x2 = (0,10)
x3, x4 = (13,11)
print("x1:",x1, "x2:",x2,"x3:",x3, "x4:",x4,overlap((x1,x2),(x3,x4)))

# ending of second line is smaller than the beginning of first
x1, x2 = (12,20)
x3, x4 = (5,10)
print("x1:",x1, "x2:",x2,"x3:",x3, "x4:",x4,overlap((x1,x2),(x3,x4)))
