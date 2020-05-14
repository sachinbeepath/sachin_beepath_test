from collections import OrderedDict
import time

class LRU_cache:
    def __init__(self,size,time_limit):
        '''
        Initialize the LRU cache
        
        size: max number of elements allowed in cache
        time_limit: how long an item is allowed to stay in the cache

       '''
        # Use Ordered Dictionary for cache
        self.cache = OrderedDict()
        # Capacity of cache
        self.size = size
        self.time_limit = time_limit
        
    def get(self,key):
        '''
        Access item in cache and move it to the back and update the time 
        it was accessed at.
        
        key: key of item to be retrieved

        '''
        if key in self.cache.keys():
            value = self.cache.pop(key)[0]
            self.cache[key] = (value,time.time())
            return value
        else:
            return "Error: Item Not Found."
        
    def put(self,key,value):
        '''
        Add item to cache or update the value of an existing key. This operation
        clears all expired items
        
        key: key of item to be retrieved
        value: value of item

        '''
        if key in self.cache.keys():
            self.cache.pop(key)
            self.cache[key] = (value,time.time())
        else:
            if len(self.cache.keys()) >= self.size:
                self.cache.popitem(last=False)
            self.cache[key]=(value,time.time())
        self.clear_expired()
    def clear_expired(self):
        '''
        Clears all items in cache that have expired.

        '''
        expired = time.time() - self.time_limit
        ex_flag = True
        
        while ex_flag:
            first = next(iter(self.cache))
            if expired < self.cache[first][1]:
                ex_flag = False
            else:
                self.cache.popitem(last=False)
                
    def __str__(self):
        '''
        Prints all items in the cache as a dictionary.

        '''
        d = {}
        for key, (value, time) in self.cache.items():
            d[key]=value
         
        return str(d)


### Test
    
cache = LRU_cache(5,3) # create cach
print(cache)  
cache.put("a", 1) # add first item
time.sleep(2)
print(cache) 
cache.put("b", 2) # add second item
time.sleep(1.5)
print(cache)  # first item should be expired
cache.put("c", 3)
print(cache)  
cache.put("d", 4)
print(cache)  
cache.put("e", 5)
print(cache)  
cache.put("f", 6)
cache.put("g", 7) # kick out oldest item
print(cache)  
print(cache.get("a")) # get item no longer in cache 
print(cache.get("c")) # get item in cache
time.sleep(4)
cache.clear_expired() # clear all expired items
print(cache)
