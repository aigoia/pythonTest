from pyray import *
from ball import Ball
from paddle import Paddle
from cpu_paddle import CpuPaddle
from setting import *

# Screen dimensions
screen_width = 1280
screen_height = 800

# Initialize game objects
ball = Ball(screen_width // 2, screen_height // 2, 12, 7, 7)
player = Paddle(screen_width - 35, screen_height // 2 - 60, 25, 120, 12)
cpu = CpuPaddle(10, screen_height // 2 - 60, 25, 120, 6)

def main():
    init_window(screen_width, screen_height, "Pong")
    set_target_fps(60)

    while not window_should_close():
        # Update game logic
        ball.update()
        player.update()
        cpu.update(ball.y)

        # Ball collision with paddles
        if check_collision_circle_rec((ball.x, ball.y), ball.radius,
                                      (player.x, player.y, player.width, player.height)):
            ball.speed_x *= -1
        if check_collision_circle_rec((ball.x, ball.y), ball.radius,
                                      (cpu.x, cpu.y, cpu.width, cpu.height)):
            ball.speed_x *= -1

        # Draw everything
        begin_drawing()
        clear_background(Green)
        draw_line(screen_width // 2, 0, screen_width // 2, screen_height, WHITE)

        ball.draw()
        player.draw()
        cpu.draw()

        draw_text(str(ball.cpu_score), screen_width // 4 - 20, 20, 80, WHITE)
        draw_text(str(ball.player_score), 3 * screen_width // 4 - 20, 20, 80, WHITE)

        end_drawing()

    close_window()

if __name__ == "__main__":
    main()