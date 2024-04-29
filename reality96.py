from ursina import *

def update():
    cube.rotation_y += 1

app = Ursina()
window.fullscreen = False
window.size = (600, 400)
window.title = 'Game Physics Engine'
window.exit_button.visible = False

cube = Entity(model='cube', color=color.red, scale=(1, 1, 1), position=(0, 0, 0))

app.run()
