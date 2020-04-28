import hazelcast
# Create hazelcast client on connected to cluster on localhost
hz = hazelcast.HazelcastClient()
availablePlayersList = hz.get_list("available-players").blocking()
activeGamesMap = hz.get_map("active-games").blocking()

def getPlayers ():
    #TODO
def startNewGame (id, gameMode):
    #TODO
def getActiveGames():
    #TODO


flag = True
print("Welcome to your game management app!")
while flag:
    print()
    print("Options: ")
    print("1. Get Players")
    print("2. Start New Minigame")
    print("3. Get Active Minigames")
    print("4. Exit")
    choice = input("Enter the number of your choice: ").lower()
    if choice == '1':
        print("Availible players are: ")
        getPlayers()
    elif choice == '2':
        addID = input("Enter the ID of the minigame you wish to add: ")
        gameMode = input("Enter the game mode:")
        startNewGame(addID, gameMode)
    elif choice == '3':
        print("Active games are: ")
        getActiveGames()
    elif choice == '4':
        flag = False
    else:
        print("Invalid option!")
print("Goodbye!")