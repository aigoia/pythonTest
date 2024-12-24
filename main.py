import asyncio
from pyray import *
from ball import Ball
from paddle import Paddle
from cpu_paddle import CpuPaddle
from setting import *

is_init = False

ball = Ball(screen_width // 2, screen_height // 2, ball_size, ball_speed, ball_speed)
player = Paddle(screen_width - paddle_width - paddle_margin, (screen_height - paddle_height) // 2, paddle_width, paddle_height, player_speed)
cpu = CpuPaddle(paddle_margin, (screen_height - paddle_height) // 2, paddle_width, paddle_height, cpu_speed)

async def init_game():
    init_window(screen_width, screen_height, game_name)
    set_target_fps(frame)
    
    await countdown()
    global is_init
    is_init = True
    
async def check_game():    
    if  ball.check_out_of_bounds():
        await countdown()
    
async def countdown(start = init_count):
    for i in range(start, 0, -1):
        begin_drawing()
        
        clear_background(Snow)
        draw_text(f"{i}", get_screen_width() // 2 - score_margin, get_screen_height() // 2 - score_margin * 2, scoreSize, Mint)
        
        if is_init:
            draw_text(str(ball.cpu_score), screen_width // 4 - score_margin, score_margin, scoreSize, Mint)
            draw_text(str(ball.player_score), 3 * screen_width // 4 - score_margin, score_margin, scoreSize, Mint)
        
        end_drawing()
        await asyncio.sleep(count_time) 

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
    clear_background(Mint)
    draw_line(screen_width // 2, 0, screen_width // 2 + 1, screen_height, Snow)
    draw_line(screen_width // 2, 0, screen_width // 2 - 1, screen_height, Snow)

    ball.draw()
    player.draw()
    cpu.draw()

    draw_text(str(ball.cpu_score), screen_width // 4 - score_margin, score_margin, scoreSize, Snow)
    draw_text(str(ball.player_score), 3 * screen_width // 4 - score_margin, score_margin, scoreSize, Snow)

    end_drawing()
    
async def main():
    print("Hello Pong!")
    await init_game()

    while not window_should_close():
        await check_game()
        update_game()  
        draw_game() 
        
    close_window()

if __name__ == "__main__":
    asyncio.run(main())
