from pyray import *
from ball import Ball
from paddle import Paddle
from cpu_paddle import CpuPaddle
from setting import *

ball = Ball(screen_width // 2, screen_height // 2, ball_size, ball_speed, ball_speed)
player = Paddle(screen_width - paddle_width - paddle_margin, (screen_height - paddle_height) // 2, paddle_width, paddle_height, player_speed)
cpu = CpuPaddle(paddle_margin, (screen_height - paddle_height) // 2, paddle_width, paddle_height, cpu_speed)

def init_game():
    init_window(screen_width, screen_height, game_name)
    set_target_fps(frame)

def update_game():
    ball.update()
    player.update()
    cpu.update(ball.y)

    if check_collision_circle_rec((ball.x, ball.y), ball.radius,
                                  (player.x, player.y, player.width, player.height)):
        ball.speed_x = ball.speed_x * -1
    if check_collision_circle_rec((ball.x, ball.y), ball.radius,
                                  (cpu.x, cpu.y, cpu.width, cpu.height)):
        ball.speed_x = ball.speed_x * -1

def draw_game():
    begin_drawing()
    clear_background(Green)
    draw_line(screen_width // 2, 0, screen_width // 2, screen_height, WHITE)

    ball.draw()
    player.draw()
    cpu.draw()

    draw_text(str(ball.cpu_score), screen_width // 4 - score_margin, score_margin, scoreSize, WHITE)
    draw_text(str(ball.player_score), 3 * screen_width // 4 - score_margin, score_margin, scoreSize, WHITE)

    end_drawing()

def main():
    print("Hello Pong!")
    init_game()

    while not window_should_close():
        update_game()
        draw_game()

    close_window()

if __name__ == "__main__":
    main()