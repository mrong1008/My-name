[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/xv5VlzUo)
# Lab 8

In this lab, we are going to keep exploring something fun. It may not directly link to any specific programming knowledge, but can bring Python closer to real-world problems. 

Another goal is to make you feel more comfortable with code that you do not familiar with. It is very unlikely for you to understand the existing code related to PyGame. So do I. But you can read the code and try to briefly understand them or only understand the part that you need to modify.

We are going to develop a Ping Pong game. Yes, this can be your first graphical game. 

## Game Description

**The Game World** We consider a space that has a width of 800 units and a height of 600 units. We consider a unit to be a pixel on your screen. The x-axis is horizontal and the y-axis is vertical. The origin (0,0) is at the top left corner. When we write a tuple to represent a point, we use the (x,y) format.

**The Ball** There is a single ball in the game. The ball has a radius of 10 pixels. We use a tuple to represent the ball's status. The tuple includes two other tuples. The first tuple is the position of the ball. The second tuple is the velocity of the ball. The velocity is a vector that has both x and y components. So `ball = ((X, Y), (Vx, Vy), Radius)` where `X` and `Y` are the x and y coordinates of the ball, and `Vx` and `Vy` are the x and y components of the velocity. The radius can stay as 10 pixels.

**Ball Initialization** The ball is initialized at the center of the game world (400, 300). The initial velocity is (2, 1);

**Ball Movement** The ball moves by adding velocity to the position. For example, if the ball is at (100, 100) and the velocity is (2, 1), then the ball will move to (102, 101).

**Ball Bouncing** The ball will bounce when it hits the wall. When the ball hits the left or right wall, the x component of the velocity will be reversed. When the ball hits the top or bottom wall, the y component of the velocity will be reversed.

**Paddles** There are two paddles in the game. Each paddle has a width of some pixels and a height of some pixels. The paddles are placed at the left and right edge of the game world. The paddles are controlled by the players. The left paddle is controlled by the left player (w and s keys) and the right paddle is controlled by the right player (up and down arrows). The game uses a list of two to represent the paddle status, with the first element being the left paddle and the second element being the right paddle. Each paddle status is a tuple, with the first element being the center position of the paddle (on the y-axis), the second element being the width of the paddle, and the third element being the height of the paddle. So `paddle=(Y, W, H)` where `Y` is the y coordinate of the paddle, `W` is the width of the paddle, and `H` is the height of the paddle. Note that the x coordinate of the paddle is fixed. The center of the left paddle is always at x=0+W/2 and the center of the right paddle is always at x=800-W/2.

**Paddle Movement** The paddles move if the player presses the corresponding key. If the left player presses the w key, the left paddle will move up by 5 pixels. If the left player presses the s key, the left paddle will move down by 5 pixels. If the right player presses the up arrow, the right paddle will move up by 5 pixels. If the right player presses the down arrow, the right paddle will move down by 5 pixels. 

**Win/Lose** If the ball hits the left wall, the right player wins. If the ball hits the right wall, the left player wins. We keep a score tuple `(L, R)` to represent the score of the game. The first element is the score of the left player and the second element is the score of the right player. The initial score is (0, 0). If the left player wins, the score becomes (1, 0). If the right player wins, the score becomes (0, 1). 

**Summary** Overall, we can represent the game in a dictionary. 

```python
game = {
	"world": (W, H),
	"ball": ((X, Y), (Vx, Vy), Radius),
	"paddle_left": (Y, W, H),
	"paddle_right": (Y, W, H),
	"score": (L, R)
}
```

## Problems

### Problem 1: Ball Movement (25pt)

Write a function `move_ball` that takes a `game` dictionary as an argument. The function should move the ball by adding the velocity to the position. The function should return the updated `game` dictionary. Note that here, we do not need a concept of delta-t. We assume that the game plays with 60 frames per second. So the delta-t is always 1/60. The velocity is in pixels per 1/60 second.

### Problem 2: Wall Collision Detection (25pt)

Write a function `detect_wall_collision` that takes the game status as an argument and returns a string. The string is either "left", "right", "top", "bottom". The return string can be empty if the ball is not hitting any wall. Note that the ball can hit two walls at the same time. For example, if the ball hits both the left and top walls, the function should return "left|top" or "top|left".

### Problem 3: Wall Bouncing (25pt)

Implement the `wall_reflection` function, which takes the game status as an argument and returns the updated game status. This function can call the `detect_wall_collision` function. If the ball hits the left or right wall, the x component of the velocity should be reversed. If the ball hits the top or bottom wall, the y component of the velocity should be reversed.

Also, if the ball hits the left or the right wall, the score should be updated. If the ball hits the left wall, the right player wins (score[1] +1). If the ball hits the right wall, the left player wins (score[0] +1).

### Problem 4: Move Paddle (25pt)

Implement the `move_paddle` function. The function takes two strings as arguments. The first is the paddle, which can be either `left` or `right`. The second is the direction, which can be either `up` or `down`. The specified paddle should move by 5 pixels in the given direction. The function should return the updated game status.

### Problem 5: Paddle Bouncing (25pt Bonus)

Implement the `paddle_reflection` function. The function takes the game status as an argument and returns the updated game status. If the ball hits the left paddle, the x component of the velocity should be reversed. If the ball hits the right paddle, the x component of the velocity should be reversed. If you need to define a `detect_paddle_collision` function, you can do so.

### Problem 6: Play the Game (25pt Bonus)

Run the game with `python3 solution.py`. Record the screen for 1-2 min. Upload the gameplay video to YouTube (or Google Drive) and include the link in your submission.
