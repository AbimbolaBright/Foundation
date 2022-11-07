#from pyexpat import model
#from re import T
from ursina import*
app= Ursina()
camera.orthographic =True
camera.fov =10
car = Entity(
    model='quad',
    texture='assets\car1',
    Collider='box',
    scale=(1 ,1),
    rotation_z=-90
)
def update():
    car.x-=held_keys['a']*5*time.dt
    car.x-=held_keys['b']*5*time.dt
    app.run()