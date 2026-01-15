Day 1: Player Sprite and Actions



TEACH 1: Explain how Pygame works. Explain the concepts of the "game loop" and the draw and update functions



TEACH 2: Introduce **variables**. Explain the var = value format and how we can use a variable later after we define it



1. Assign the screen width and height
2. Create a player spaceship by using the Actor constructor

 	a) Reposition the player's spaceship, using the WIDTH and HEIGHT variables where applicable

3\. Draw the spaceship to the screen in the draw function



TEACH 3: Introduce **Booleans** and **if-statements**. Explain how we can use if-statements to dictate how we our program can behave



4\. In the update method, code the spaceship to be able to move when certain buttons are pressed

5\. Use the fill method to give the screen a background color



TEACH 4: Introduce **AND, OR,** and **NOT**. Explain how they can be used to make more complex if-statements



6\. Update the player movement to prevent the player from going off the screen



TEACH 5: Introduce **lists**. Explain that lists are used to store a collection of information together under one name. Explain that we can add and remove elements from a list (don't provide examples)



7\. Create a list of bullets in the game initialization section that will be used to store our player's bullets

8\. Use an if-statement to allow the player spaceship to shoot bullets when the space bar is pressed

 	a) Create a new Actor of the bullet

 	b) Add the bullet to our list of bullets

9\. "Attempt" to draw the bullets on the screen, and present the idea of using a for loop



TEACH 6: Introduce **for loops**. Explain that they can be used to do something with every element in a provided list



10\. Use a for loop to draw every bullet onto the screen

11\. In the update method, use a for loop to allow your bullets to move

 	a) Use an if-statement to remove the bullet from the list if it is too far off the screen

12\. Initialize a bullet cooldown variable to prevent the player from shooting a "beam"

13\. "Attempt" to update the bullet shooting function to allow the player only to shoot when the cooldown is at 0

 	a) Use an if-statement to decrease the cooldown if it isn't at 0

 	b) Use an AND statement to shoot only when the countdown is at 0

 	c) Change the bullet cooldown variable whenever you shoot a bullet



TEACH 7: Introduce **global** variables. Explain that if you want to directly change a variable that we initialized at the start of the program by using "=", we need to say **global var**



14\. Include the global bullet cooldown variable



TEACH 8: Introduce the **elif statement**. Explain that it can be used to check a second if-statement if the first one is False



15\. Rewrite the bullet shooting code to become an elif-statement





Day 2: Enemy Sprite and Actions



1. Create a single enemy and draw it to the screen. Update it's position to be at the top of the screen
2. In the update function, create code that allows the enemy to move towards the player



TEACH 9: Introduce the **random** module. Explain the randint and choice functions.



3\. Update the enemy code so that the enemy spawns in a random location

4\. In the update function, create code that allows the enemy to shoot at you

 	a) You can copy and paste the code that allows the player to shoot and their bullets to move

 	b) You will need to use a different list for the enemies bullets and a different cooldown variable (make sure it is global)

 	c) Make sure that the bullet moves the right way



TEACH 10: Introduce **functions**. Explain that they are sections of code that we can give a name to so that we can call them at any time we want



5\. Move the enemy creation code into a new function

6\. Create a list that will store all of the enemies that we create

 	a) Now, when we create an enemy, append the enemy to that list

 	b) Use for loops to let the enemies be drawn, move, and shoot

 	c) When moving the enemies, remove them from the list if they are off screen

7\. Use a clock scheduler to allow the enemies to spawn at a regular interval



TEACH 11: Introduce **collidelist**. Explain that you can check if a single object is overlapping any element in a list. If it is overlapping, using this function returns the index of the element. Otherwise, it returns -1.



8\. Use a for loop and the collidelist method to check if the player shot an enemy

&nbsp;	a) Use an if-statement to check if the enemy was shot

&nbsp;	b) Remove your bullet and the enemy from their respective list

9\. Add a (global) score variable that allows you to count how many enemies you destroyed

10\. Use the collidelist method to check if one of the enemies shot you. You do NOT need a for loop for this

11\. Add a Boolean variable that changes when you got shot by an enemy

12\. Update the draw function to display a "GAME OVER" screen when an enemy shoots the player. This needs an if-statement

13\. Use another collidelist method to check if the player ran into one of the enemies. End the game if they did

14\. Update the shooting method to only allow the player to shoot ONLY when the game isn't over. You should also clear the player's bullets list when they die



DAY 3: Customizations/Challenges



1. Instead of dying immediately, give the player a certain number of lives
2. Let the enemies move faster as you score more points
3. Change the code so that different coloured enemies spawn
4. Include meteors in the game. You cannot shoot these meteors and they will instantly end your game
5. Give different coloured enemies different coloured bullets. These bullets might have a different speed
6. Create power-ups that drop from the enemies. This might allow you to shoot faster, give you extra lives/shield, stop time, etc.
