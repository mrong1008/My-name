import pygame

game = {
    "world": (800, 600),
    "ball": ((400, 300), (2, 1), 10),
    "paddle_left": (300, 10, 60),
    "paddle_right": (300, 10, 60),
    "score": (0, 0),
}


def ball_move(game):
    # Take the ball's current position and speed from the game
    (ball_x, ball_y), (vx, vy), radius = game["ball"]

    # Change the ball's position based on its speed
    game["ball"] = ((ball_x + vx, ball_y + vy), (vx, vy), radius)
    return game



def detect_paddle_collision(ball_pos, ball_radius, paddle_y, paddle_dimensions, world_width):
    # Get the ball's position and size
    ball_x, ball_y = ball_pos
    paddle_width, paddle_height = paddle_dimensions

    # Calculate where the left and right paddles are
    left_paddle_x = paddle_width
    right_paddle_x = world_width - paddle_width

    # Check if the ball has hit the left or right paddle
    left_collision = (ball_x - ball_radius <= left_paddle_x and paddle_y <= ball_y <= paddle_y + paddle_height)
    right_collision = (ball_x + ball_radius >= right_paddle_x and paddle_y <= ball_y <= paddle_y + paddle_height)

    # Return which paddle was hit, if any
    if left_collision:
        return "left"
    elif right_collision:
        return "right"
    return None


def paddle_reflection(game):
    # Get the ball and paddles' details from the game
    ball_pos, ball_vel, ball_radius = game["ball"]
    paddle_left_pos, paddle_right_pos = game["paddle_left"][0], game["paddle_right"][0]
    paddle_dimensions_left = game["paddle_left"][1:]
    paddle_dimensions_right = game["paddle_right"][1:]
    world_width = game["world"][0]

    # Check if the ball has hit either paddle
    collision_left = detect_paddle_collision(ball_pos, ball_radius, paddle_left_pos, paddle_dimensions_left, world_width)
    collision_right = detect_paddle_collision(ball_pos, ball_radius, paddle_right_pos, paddle_dimensions_right, world_width)

    # If the ball hit a paddle, make it bounce back
    if collision_left or collision_right:
        ball_vel = (-ball_vel[0], ball_vel[1])

    # Update the ball's details in the game
    game["ball"] = (ball_pos, ball_vel, ball_radius)
    return game



def wall_reflection(game):
    # Check if the ball has hit any wall
    collision_flags = detect_wall_collision(game)

    # Get the ball's current position and speed
    (x, y), (vx, vy), radius = game["ball"]

    # Make the ball bounce off the wall and update the score if needed
    if "left" in collision_flags:
        vx = -vx
        game["score"] = (game["score"][0], game["score"][1] + 1)
    elif "right" in collision_flags:
        vx = -vx
        game["score"] = (game["score"][0] + 1, game["score"][1])
    if "top" in collision_flags or "bottom" in collision_flags:
        vy = -vy

    # Update the ball's position and speed in the game
    game["ball"] = ((x, y), (vx, vy), radius)
    return game



def detect_wall_collision(game):
    collisions = []
    x, y = game["ball"][0]
    radius = game["ball"][2]
    width, height = game["world"]

    # Check for collisions with each wall
    if x - radius <= 0:
        collisions.append("left")
    elif x + radius >= width:
        collisions.append("right")
    if y - radius <= 0:
        collisions.append("top")
    elif y + radius >= height:
        collisions.append("bottom")

    return "|".join(collisions)


def move_paddle(game, side, direction):
    # Get the current position of the specified paddle
    y = game[f"paddle_{side}"][0]
    width = game[f"paddle_{side}"][1]
    height = game[f"paddle_{side}"][2]
    # Determine the direction to move the paddle
    dy = -5 if direction == "up" else 5

    # Update the paddle's position
    game[f"paddle_{side}"] = (y + dy, width, height)
    return game


def render(screen, game):
    screen.fill((0, 0, 0))

    ball_pos, ball_vel, ball_r = game["ball"]
    paddle_left = game["paddle_left"]
    paddle_right = game["paddle_right"]

    pygame.draw.circle(screen, (255, 255, 255), ball_pos, ball_r)
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (0, paddle_left[0], paddle_left[1], paddle_left[2]),
    )
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (
            game["world"][0] - paddle_right[1],
            paddle_right[0],
            paddle_right[1],
            paddle_right[2],
        ),
    )

    # Draw scores on center-top of the screen
    font = pygame.font.SysFont("Arial", 30)
    score = game["score"]
    score_text = f"{score[0]} : {score[1]}"
    text = font.render(score_text, True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (game["world"][0] // 2, 30)
    screen.blit(text, text_rect)

    pygame.display.flip()


def main():
    global game

    pygame.init()
    screen = pygame.display.set_mode(game["world"])
    pygame.display.set_caption("Ping Pong")
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        game = ball_move(game)
        game = paddle_reflection(game)
        game = wall_reflection(game)

        # Move paddle if up/down/w/s are pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            game = move_paddle(game, "right", "up")
        elif keys[pygame.K_DOWN]:
            game = move_paddle(game, "right", "down")
        elif keys[pygame.K_w]:
            game = move_paddle(game, "left", "up")
        elif keys[pygame.K_s]:
            game = move_paddle(game, "left", "down")

        render(screen, game)


if __name__ == "__main__":
    main()
