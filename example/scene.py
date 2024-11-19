from manim import *
from numpy import array as vec

class Ball(Circle):
    def __init__(self, position=vec([0,0,0]), velocity=vec([0,0,0]), acceleration=vec([0,0,0]), **kwargs):
        Circle.__init__(self, ** kwargs)
        self.t = 0

        self.move_to(position)
        self.position_fun = None

        self.velocity = velocity
        self.velocity_fun = None

        self.acceleration = acceleration
        self.acceleration_fun = None

        self.mass = PI * self.radius ** 2

    def update_ball(self, dt):
        if self.position_fun:
            self.move_to(self.position_fun(self.t))

        elif self.velocity_fun:
            self.velocity = self.velocity_fun(self.t)
            self.shift(self.velocity * dt)

        elif self.acceleration_fun:
            self.acceleration = self.acceleration_fun(self.t)
            self.velocity = self.velocity + self.acceleration * dt
            self.shift(self.velocity * dt)

        else:
            self.velocity = self.velocity + self.acceleration * dt
            self.shift(self.velocity * dt)

        self.t += dt

    def setup_funs(self, position_fun=None, velocity_fun=None, acceleration_fun=None):
        if acceleration_fun:
            self.acceleration_fun = acceleration_fun

        if velocity_fun:
            self.velocity_fun = velocity_fun
            self.acceleration_fun = None

        if position_fun:
            self.position_fun = position_fun
            self.velocity_fun = None
            self.acceleration_fun = None


class BouncingBall(Scene):
    
    def construct(self):
        config.frame_width = 100
        
        balls: list[Ball] = [Ball(radius=3, velocity=vec([0,0,0]))]
    
        def ball_position_fun(t):
            return vec([np.cos(t) * 10, np.sin(t) * 10, 0])
        
        def ball_velocity_fun(t):
            return vec([-np.sin(t) * 10, np.cos(t) * 10, 0])
        
        def ball_acceleration_fun(t):
            return vec([-np.cos(t) * 10, -np.sin(t) * 10, 0])
        
        for ball in balls:
            ball.set_fill(RED, opacity=0.5)
            ball.move_to(ball_position_fun(0))
            ball.velocity = ball_velocity_fun(0)
            # ball.setup_funs(position_fun=ball_position_fun)
            # ball.setup_funs(velocity_fun=ball_velocity_fun)
            ball.setup_funs(acceleration_fun=ball_acceleration_fun)
        
        self.play(
            *[FadeIn(ball) for ball in balls],
        )
        
        for ball in balls:
            ball.add_updater(lambda _, dt: ball.update_ball(dt))
            self.add(ball)

        self.wait(6)
        for ball in balls:
            ball.clear_updaters()
        self.wait(3)

