from gamebuino_meta import begin, waitForUpdate, display, color, buttons, collide

# Ball initial settings
ball_size = 3
ball_x_position = 20
ball_y_position = 20
ball_x_speed = 2
ball_y_speed = 2

# Player initial settings
player_height = 12
player_width = 3
player_x_position = 10
player_y_position = 30
player_y_speed = 2

# Score
score = 0

while True:
    waitForUpdate()
    display.clear()

    # If you press the UP or DOWN buttons, move the player up or down
    if buttons.repeat(buttons.UP, 0):
        player_y_position = player_y_position - player_y_speed

    if buttons.repeat(buttons.DOWN, 0):
        player_y_position = player_y_position + player_y_speed

    # Move the ball
    ball_x_position = ball_x_position + ball_x_speed
    ball_y_position = ball_y_position + ball_y_speed

    # Change the ball's direction if it touches a border of the screen
    # Top border
    if ball_y_position <= 0:
        ball_y_speed = -ball_y_speed
    # Bottom border
    if ball_y_position >= 64 - ball_size:
        ball_y_speed = -ball_y_speed
    # Right border
    if ball_x_position + ball_size >= 80:
        ball_x_speed = -ball_x_speed

    # Increase the score and change the ball's direction if the ball touches the player
    if collide.rectRect(ball_x_position, ball_y_position, ball_size, ball_size, 
            player_x_position, player_y_position, player_width, player_height):
        ball_x_position = ball_x_position - ball_x_speed
        ball_x_speed = -ball_x_speed
        score = score + 1

    # Reset the score if the ball touches the left border of the screen
    if ball_x_position <= 0:
        score = 0
        ball_x_speed = -ball_x_speed

    # Display ball
    display.fillRect(ball_x_position, ball_y_position, ball_size, ball_size)
    
    # Display player
    display.fillRect(player_x_position, player_y_position,
        player_width, player_height)
        
    # Display Score
    display.setColor(color.BROWN)
    display.print("SCORE: ")
    display.print(score)
    display.print("\n")
    
    if score == 0:
        display.setColor(color.WHITE)
        display.print("GAME OVER!")