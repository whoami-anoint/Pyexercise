## Creating an empty set 
b = set()
print(type(b))

## Adding values to an empty set
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set.
b.add((4,5,6))


## Accessing Elements
# b.add([4,5,6]) # Cannot add list to sets
# b.add({4,5,6}) # Cannot add dictionary to sets
print(b)

## Length of the set
print(len(b)) # Prints the length of this set

## Removal of an Item
b.remove(5) # Removes 5 from set b
# b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(b)

# print(b.pop()) Removes an artributry elements from the set and returns the element removed
# print(b.clear()) Empties the set b
# print(b.union()) Return a new set with all items from both sets.
# print(b.intersection()) Returns a set which contains only items in both sets.
