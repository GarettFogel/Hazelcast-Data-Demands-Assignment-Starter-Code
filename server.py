import hazelcast
# Create hazelcast client on connected to cluster on localhost
hz = hazelcast.HazelcastClient()
availablePlayersList = hz.get_list("available-players").blocking()
activeGamesMap = hz.get_map("active-games").blocking()
def addPlayer (name):
    #TODO
def endGame (key):
    #TODO

flag = True
print("Welcome to your fake game server!")
while flag:
    print() 
    print("Options: ")
    print("1. Add new player to available list")
    print("2. End Minigame")
    print("3. Exit")
    choice = input("Enter the number of your choice: ").lower()
    if choice == '1':
        playerName = input("Enter the player's name: ")
        addPlayer(playerName)
    elif choice == '2':
        removeID = input("Enter the ID of the minigame you wish to end: ")
        endGame(removeID)
    elif choice == '3':
        flag = False
    else:
        print("Invalid option!")
availablePlayersList.clear()
activeGamesMap.clear()
print("Goodbye!")