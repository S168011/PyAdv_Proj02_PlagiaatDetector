months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
months = [f"{i}: {month[0:3].upper()}" for i, month in enumerate(months, start=1) if len(month) <= 5]

print(months)