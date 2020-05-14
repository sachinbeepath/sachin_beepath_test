## Ormuco Technical Test 

## Question B

def compare_version(v1,v2):
    '''
      Consumes a two strings, v1 and v2, representing the version of an item 
      and determines which is grater.
      
      compare_version: Str Str  -> Str
     
      
      Examples:
          compare_version('1.0',1.1) => "'1.1' is greater than '1.0'."
          compare_version('1.0',1.1) => "'1.1' is greater than '1.0'."
          
          Requires:
              v1 and v2 to be unique
   '''
    
    # split strings into integers delimited by '.'
    if v1 == v2:
        return "Both strings are the same."
    version1 = v1.split(".")
    version2 = v2.split(".")
    
    if len(v1) >= len(v2):
        version1 = v1.split(".")
        version2 = v2.split(".")
    else:
        version1 = v2.split(".")
        version2 = v1.split(".")
        
    
    # run through each segment of the shortest string
    
    for i in range(len(version2)):
        if int(version1[i]) > int(version2[i]):
            return '.'.join(version1) + " is greater than " + '.'.join(version2)
        elif int(version1[i]) < int(version2[i]):
            return '.'.join(version2) + " is greater than " + '.'.join(version1)
        else:
            if i+1 == len(version2) and len(version1) > len(version2):
                return '.'.join(version1) + " is greater than " + '.'.join(version2)
            
            
### Tests
            
# same length same major version number
print(compare_version("10.0.3","10.1.1"))

# same length different major version number
print(compare_version("9.10.1","10.1.9"))

# different length same major version number
print(compare_version("10","10.1"))

# different length different major version number
print(compare_version("9.10.1","12"))

# same length same major and minor version number
print(compare_version("10.1.0","10.1.1"))

# different length same major and minor version number
print(compare_version("7.4","7.4.1"))

# same version number
print(compare_version("7.4","7.4"))
