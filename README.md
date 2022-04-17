# **Tic Tac Toe**

I have decided to make a Tic Tac Toe game as my third project using python. This game allows two users to play a game of Tic Tac Toe agianst each other.
The game is a two player game. A player wins by lining up three X's or three O's in a row either horizontally, diagonally or vertically.

ALL IMAGES WHERE TAKEN FROM THE TERMINAL DUE TO HEROKU GITHUB INTEGRATION BEING DOWN. 

ERROR EXPLAINED BELOW IN DEPLOYMENT SECTION. STUDENT SUPPORT HAS BEEN CONTACTED

## **Feautures of the Game**

- ### **Start of Game**

  - The game begins by asking the user to input a number between 1-9.
  - This prompts the user to make their first move.

    ![Beginning of game](assets/images/game1.PNG)

- ### **Invalid Input Handling**

  - When a user inputs a letter the code raises a ValueError
  - This explains that the user has input a letter and prompts the user once agian to enter a number between 1-9

    ![Letter has been entered](assets/images/game2.PNG)


  - When a user inputs a number higher than 9 or lower than 1 a ValueError.
  - This explains how the number is too high and the user must enter a number between 1-9.
  - The propmt to enter a number enters again.

    ![Too high of a number](assets/images/game3.PNG)


- ### **Quit Function**

  - The user has the ability to stop playing the game at any moment by pressing q
  - This causes the game to break out of the while loop and stop the game

    ![Quit game function](assets/images/quit-game.PNG)


- ### **Correct input recieved**

  - When a correct input has been recieved an X or an O is placed on the board
  - X takes the first turn and after that its O's turn
  - The users take turns placing their character on the board
  - After each turn the character switches

    ![Game in motion](assets/images/game4.PNG)

    ![Game switching between X and O](assets/images/game-switch.PNG)

- ### **User Wins Game**

  - When a user wins the game a congratulations prompt appears and the game loop stops with break.
  - The prompt tells you whether X's or O's wont the game.
  - The board is shown to show how the user won the game.

  ![User wins game](assets/images/game5.PNG)

