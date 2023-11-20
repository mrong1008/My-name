import solution


def test_ball_move():
    game = {"ball": ((0, 0), (1, 1), 10)}
    expected_game = {"ball": ((1, 1), (1, 1), 10)}
    assert solution.ball_move(game) == expected_game


def test_detect_wall_collision():
    game = {"ball": ((0, 0), (1, 1), 10), "world": (500, 500)}
    assert solution.detect_wall_collision(game) == "left|top"

    game = {"ball": ((500, 500), (1, 1), 10), "world": (500, 500)}
    assert solution.detect_wall_collision(game) == "right|bottom"

    game = {"ball": ((250, 0), (1, 1), 10), "world": (500, 500)}
    assert solution.detect_wall_collision(game) == "top"

    game = {"ball": ((0, 250), (1, 1), 10), "world": (500, 500)}
    assert solution.detect_wall_collision(game) == "left"

    game = {"ball": ((250, 500), (1, 1), 10), "world": (500, 500)}
    assert solution.detect_wall_collision(game) == "bottom"

    game = {"ball": ((500, 250), (1, 1), 10), "world": (500, 500)}
    assert solution.detect_wall_collision(game) == "right"

    game = {"ball": ((250, 250), (1, 1), 10), "world": (500, 500)}
    assert solution.detect_wall_collision(game) == ""


def test_wall_reflection():
    # Test left wall collision
    game = {"ball": ((10, 50), (-5, 5), 10), "world": (500, 500), "score": (0, 0)}
    expected_game = {
        "ball": ((10, 50), (5, 5), 10),
        "world": (500, 500),
        "score": (0, 1),
    }
    assert solution.wall_reflection(game) == expected_game

    # Test right wall collision
    game = {"ball": ((490, 50), (5, 5), 10), "world": (500, 500), "score": (0, 0)}
    expected_game = {
        "ball": ((490, 50), (-5, 5), 10),
        "world": (500, 500),
        "score": (1, 0),
    }
    assert solution.wall_reflection(game) == expected_game

    # Test top wall collision
    game = {"ball": ((250, 10), (1, -1), 10), "world": (500, 500), "score": (0, 0)}
    expected_game = {
        "ball": ((250, 10), (1, 1), 10),
        "world": (500, 500),
        "score": (0, 0),
    }
    assert solution.wall_reflection(game) == expected_game

    # Test bottom wall collision
    game = {"ball": ((250, 490), (1, 1), 10), "world": (500, 500), "score": (0, 0)}
    expected_game = {
        "ball": ((250, 490), (1, -1), 10),
        "world": (500, 500),
        "score": (0, 0),
    }
    assert solution.wall_reflection(game) == expected_game

    # Test no collision
    game = {"ball": ((250, 250), (1, 1), 10), "world": (500, 500), "score": (0, 0)}
    expected_game = {
        "ball": ((250, 250), (1, 1), 10),
        "world": (500, 500),
        "score": (0, 0),
    }
    assert solution.wall_reflection(game) == expected_game


def test_move_paddle():
    game = {"paddle_left": (0, 10, 50)}
    expected_game = {"paddle_left": (-5, 10, 50)}
    assert solution.move_paddle(game, "left", "up") == expected_game

    game = {"paddle_right": (490, 10, 50)}
    expected_game = {"paddle_right": (495, 10, 50)}
    assert solution.move_paddle(game, "right", "down") == expected_game


def test_paddle_reflection():
    # Test left paddle collision
    game = {
        "world": (500, 500),
        "ball": ((10, 50), (-5, 5), 10),
        "paddle_left": (50, 10, 100),
        "paddle_right": (50, 10, 100),
    }
    expected_game = {
        "world": (500, 500),
        "ball": ((10, 50), (5, 5), 10),
        "paddle_left": (50, 10, 100),
        "paddle_right": (50, 10, 100),
    }
    assert solution.paddle_reflection(game) == expected_game

    # Test right paddle collision
    game = {
        "world": (500, 500),
        "ball": ((490, 50), (5, 5), 10),
        "paddle_left": (50, 10, 100),
        "paddle_right": (50, 10, 100),
    }
    expected_game = {
        "world": (500, 500),
        "ball": ((490, 50), (-5, 5), 10),
        "paddle_left": (50, 10, 100),
        "paddle_right": (50, 10, 100),
    }
    assert solution.paddle_reflection(game) == expected_game

    # Test no collision
    game = {
        "world": (500, 500),
        "ball": ((250, 250), (1, 1), 10),
        "paddle_left": (50, 10, 100),
        "paddle_right": (50, 10, 100),
    }
    expected_game = {
        "world": (500, 500),
        "ball": ((250, 250), (1, 1), 10),
        "paddle_left": (50, 10, 100),
        "paddle_right": (50, 10, 100),
    }
    assert solution.paddle_reflection(game) == expected_game



test_ball_move()  # pass
print('ball_move() passes the test!')
test_move_paddle()  # pass
print('move_paddle() passes the test!')
test_wall_reflection()  # pass
print('wall_reflection() passes the test!')
test_detect_wall_collision() # pass
print('detect_wall_collision() passes the test!')
test_paddle_reflection() # pass
print('paddle_reflection() tests pass!')
print('All tests pass!')