# Write your code here :-)
from pgzhelper import *

WIDTH = 1536
HEIGHT = 768

tile_nums = [[]]
background = []
roads = []

car = Actor("car_yellow_small_1")
car.scale = 0.5
car.angle = -90
car.center = (40, 300)

# create background grass
for i in range(0, WIDTH, 64):
    for j in range(0, HEIGHT, 64):
        tile = Actor("land_grass04")
        tile.scale = 0.5
        tile.topleft = (i, j)
        background.append(tile)

for i in range(0, WIDTH, 64):
    road = Actor("road_asphalt12")
    road.scale = 0.5
    road.midleft = (i, 300)
    roads.append(road)

def draw():
    for tile in background:
        tile.draw()

    for road in roads:
        road.draw()

    car.draw()

def update():
    pass
