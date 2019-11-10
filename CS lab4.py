from turtle import Turtle
import turtle
class Ball(Turtle):
	def __init__(self,r,color,dx,dy):
		Turtle.__init__(self)
		self.r=r
		self.dx=dx
		self.dy=dy
		self.penup()
		self.shape('circle')
		self.color(color)
		self.shapesize(r/10)
	def	move_x(self,screen_width,screen_height):
			current_x=self.dx
			self.goto(screen_width,screen_height)
			new_x=current_x +dx
			current_y=self.dy
			self.goto(screen_width,screen_height)
			new_y=current_y+dy
			right_side_ball=new_x + r
			left_side_ball=new_x + r
			top_side_ball = new_y + r
			bottom_side_ball = new_y + r
			x = (right_side_ball,left_side_ball)
			y = (top_side_ball,bottom_side_ball) 
			self.goto(x,y)
			ball_size= [left_side,right_side,top_side,bottom_side]
			if ball_sides>screen_width and screen_height:
				ball=Ball(5,'blue','2','3')
				print(ball)