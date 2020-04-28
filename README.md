# Hazelcast Data Demands Assignment
In this exercise we’re going to pretend that you run a videogame server in Python (server.py). You also have a separate Python management app that you use to see what’s going on on the server (app.py). This server and management app could be in any supported language, but Python is easy to work with so we’re going to use that.

You have millions of players who have played on your server, so you don’t really want to have to query your players table in your MySQL database to see if they are waiting in the game so you decide to use Hazelcast. In your game, you can start a minigame from your own app that will randomly pull 3 players out of the game and put them into the minigame. Once they have played the minigame, they are no longer available to play again. The starter code can be found here:

To test, make sure a hazelcast server is running on your machine, then run in separate windows ‘python app.py’ and ‘python server.py’. Note that restarting the server will manually clear out the available players and the active mini games, as it would in a real game. 

## Completing the “Server” and the Application
Your solutions won’t require very much code. Hazelcast is meant to be simple to use across multiple clients. Attach a screenshot after each step of the following.

1. First, you want to be able to add players to a list called ‘available-players’, and view the list on your website.
 * Complete the function ‘addPlayer’ in server.py to add the player’s name to the list. Should give a success message if successful.
 * Complete the function ‘getPlayers’ in app.py. It should print out all players in the ‘available-players’ list.

2. Now, you want to be able to create a new active game from your management app. There must be 3 players available to start a new game. When the game starts, the game should be added to the map ‘active-games’ with a key that is an ID, and a value that is the game mode. 3 random players should be removed from the ‘available-players’ list.
 * Complete the function “startNewGame” in app.py that adds the id and game mode to the ‘active-games’ map and removes 3 players from the ‘available-players’ list. There must be 3 available players to start a new game. If there are less than 3 players, print that out and don’t start the new game. Should print out the new key and value with a success message if successful.
 * Complete the function “getActiveGames” in app.py. It should out the keys and the values of all active games in the.

3. Now when the game is over you want to remove it from the map. 
 * Complete the ‘endGame’ function in server.py to remove a minigame from the map given it’s key. Test that it works by calling getting all the games in app.py
	
## Testing your programs:
1. Add 5 players to available-players (server.py)
2. List the current players (app.py). Attach a screenshot
3. Create a new game (app.py). Attach a screenshot of the output.
4. List the current players (app.py). How many are there? Attach a screenshot //should be 2
5. Exit app.py and restart it.
6. List the active games. How many are there? Attach a screenshot //should be 1
7. Try to create a new game, what happens? Attach a screenshot //should not allow
8. Remove the game you added. Attach a screenshot.
9. List active games. How many are there? Attach a screenshot.

 
