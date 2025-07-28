import pygame
import sys

WIDTH, HEIGHT = 800, 600
FIELD_COLOR = (0, 128, 0)
WHITE = (255, 255, 255)
BROWN = (150, 75, 0)
GOAL_WIDTH = 200
GOAL_POST_WIDTH = 10
GOAL_POST_HEIGHT = 100
BALL_SIZE = 20
BALL_SPEED = 10
MOVE_SPEED = 5


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("NFL Field Goal")
    clock = pygame.time.Clock()

    # Ball starts at bottom center
    ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2,
                       HEIGHT - BALL_SIZE - 10,
                       BALL_SIZE, BALL_SIZE)
    ball_moving = False

    score = 0

    goal_x = WIDTH // 2 - GOAL_WIDTH // 2
    crossbar_y = 150

    font = pygame.font.SysFont(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not ball_moving:
                    ball_moving = True

        keys = pygame.key.get_pressed()
        if not ball_moving:
            if keys[pygame.K_LEFT] and ball.left > 0:
                ball.x -= MOVE_SPEED
            if keys[pygame.K_RIGHT] and ball.right < WIDTH:
                ball.x += MOVE_SPEED
        else:
            ball.y -= BALL_SPEED
            if ball.y <= crossbar_y:
                if goal_x + GOAL_POST_WIDTH < ball.centerx < goal_x + GOAL_WIDTH - GOAL_POST_WIDTH:
                    score += 1
                ball_moving = False
                ball.x = WIDTH // 2 - BALL_SIZE // 2
                ball.y = HEIGHT - BALL_SIZE - 10
            elif ball.y + BALL_SIZE < 0:
                ball_moving = False
                ball.x = WIDTH // 2 - BALL_SIZE // 2
                ball.y = HEIGHT - BALL_SIZE - 10

        screen.fill(FIELD_COLOR)

        # Draw goal posts
        left_post = pygame.Rect(goal_x, crossbar_y, GOAL_POST_WIDTH, GOAL_POST_HEIGHT)
        right_post = pygame.Rect(goal_x + GOAL_WIDTH - GOAL_POST_WIDTH,
                                 crossbar_y, GOAL_POST_WIDTH, GOAL_POST_HEIGHT)
        crossbar = pygame.Rect(goal_x, crossbar_y, GOAL_WIDTH, GOAL_POST_WIDTH)
        pygame.draw.rect(screen, WHITE, left_post)
        pygame.draw.rect(screen, WHITE, right_post)
        pygame.draw.rect(screen, WHITE, crossbar)

        pygame.draw.ellipse(screen, BROWN, ball)

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
