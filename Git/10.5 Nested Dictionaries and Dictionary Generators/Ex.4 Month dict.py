# A dictionary of all elements of the months dictionary in which the key and value are swapped.
months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
          7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

result = {value: key for key, value in months.items()}
print(result)