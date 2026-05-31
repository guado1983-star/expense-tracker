# Create the shopping list with at least 5 items
shopping = ["milk", "eggs", "cheese", "apples", "bananas"]

# Print the first item
print("First item:", shopping[0])

# Print the last item using negative indexing
print("Last item:", shopping[-1])

# Add "bread" to the end
shopping.append("bread")

# Remove the second item (index 1)
shopping.pop(1)

# Print the final list and its length
print("Final shopping list:", shopping)
print("Length of list:", len(shopping))