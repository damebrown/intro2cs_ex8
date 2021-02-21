############################################################
# Imports
############################################################
import game_helper as gh
from car import Car, Direction


############################################################
# Constants
############################################################

# place your constants here

############################################################
# Class definition
############################################################


class Board():
	"""
	A class representing a rush hour board.
	"""

	def __init__(self, cars, exit_board, size=6):
		"""
		Initialize a new Board object.
		:param cars: A list (or dictionary) of cars.
		:param size: Size of board (Default size is 6).
		"""
		self.size = size
		self.exit_board = exit_board
		self.cars = []

	def add_car(self, car):
		"""
		Add a single car to the board.
		:param car: A car object
		:return: True if a car was successfully added, or False otherwise.
		"""
		if car.orientation == 1:
			if car.location[1] + car.length < 6:
				Board.cars.append(car)
				print('car was added successfully')
				return True
			else:
				print('car location is not valid, car was\'\t appended')
				return False
		elif car.orientation == 0:
			if car.location[0] + car.length < 6:
				Board.cars.append(car)
				print('car was added successfully')
				return True
			else:
				print('car location is not valid, car was\'\t appended')
				return False

	def is_empty(self, location):
		"""
		Check if a given location on the board is free.
		:param location: x and y coordinations of location to be check
		:return: True if location is free, False otherwise
		"""
		# implement your code here (and then delete the next line - 'pass')
		if not 0 <= location[0] < self.size and not 0 <= location[
			1] < self.size:
			return False
		for car in self.cars:
			if car.orientation == 1:
				for dis in range(car.location[0],
				                 car.location[0] + (car.length + 1)):
					if location == dis:
						return False
					else:
						return True
			elif car.orientation == 0:
				for dis in range(car.location[1],
				                 car.location[1] + (car.length + 1)):
					if location == dis:
						return False
					else:
						return True

	def move(self, car, direction):
		"""
		Move a car in the given direction.
		:param car: A Car object to be moved.
		:param direction: A Direction object representing desired direction
			to move car.
		:return: True if movement was possible and car was moved, False
		otherwise.
		"""
		# implement your code here (and then delete the next line - 'pass')
		if car in Board.cars:
			pass
		else:
			print('No existing car')
			return False
		if car.orientation == 1:
			if direction != Direction.LEFT or direction != Direction.RIGHT:
				print('direction is no valid')
				return False
		elif car.orientation == 0:
			if direction != Direction.UP or direction != Direction.DOWN:
				print('direction is no valid')
				return False
		for location in range(car.location, car.location+car.length+1)
			if is_empty(self, location):
				if car.orientation == 0:
					if direction == Direction.UP:
						car.location[0] += 1
						return True
					else:
						car.location[0] -= 1
						return True
				elif car.orientation == 1:
					if direction == Direction.RIGHT:
						car.location[1] += 1
						return True
					else:
						car.location[1] -= 1
						return True
			else:
				print('Car was not moved')
				return False


	def __repr__(self):
		"""
		:return: Return a string representation of the board.
		"""
		# implement your code here (and then delete the next line - 'pass')
		pass
