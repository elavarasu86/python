player: list[str] = ['Sachin', 'Dravid', 'Yuvaraj']
print(player)

# Append Method: Adds the new player info at the end.
player.append('Ganguly')
print(player)

# Copy Method: Copies the contact into new variable. New variable maintain its own data. If you do change it will affect both.
Copy_player: list[str] = player.copy()
Copy_player.remove('Ganguly')
print(Copy_player)

# Count Method:
cnt = player.count('Sachin')
print('Total number of players with Name Sachine is ', cnt)

# Extend Method:
subPlayers: list[str] = ['Parthiv', 'Balaji']
player.extend(subPlayers)
print(player)

# Index() Method:
print(player.index('Balaji'))

# Insert method:
player.insert(1, 'Dhoni')
print(player)

# Pop Method: Will remove last player from the list.
print(player.pop())

#Remove Method:
player.remove('Yuvaraj')
print(player)

#Reverse
print(player.reverse())

#Sort
print(player.sort())

# Clear Method: Clears all the information in the list.
player.clear()
print(player)
