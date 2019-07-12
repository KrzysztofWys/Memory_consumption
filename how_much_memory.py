# Howmuch memory need different types of data; the results will in bytes
# Or: why generated objects can be interessant ?
from sys import getsizeof
# first calculation is made for generated objects
milion_positions_genobject = (x*10 for x in range(1000000))
print(type(milion_positions_genobject), " takes  ",
      getsizeof(milion_positions_genobject), "bytes")
# second calculation is made for sets
milion_positions_set = set(x*10 for x in range(1000000))
print(type(milion_positions_set), " takes  ",
      getsizeof(milion_positions_set), "bytes")
# third calculation is made for lists
milion_positions_list = list(x*10 for x in range(1000000))
print(type(milion_positions_list), " takes  ",
      getsizeof(milion_positions_list), "bytes")
