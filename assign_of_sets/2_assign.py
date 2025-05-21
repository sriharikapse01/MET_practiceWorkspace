# Take a set of games and remove "Throw ball" from the set 
# without throwing any error if it is does not exist in the set.
games = {"badminton" , "cricket" , "chess"}

games.discard("Throw ball")

print(games)