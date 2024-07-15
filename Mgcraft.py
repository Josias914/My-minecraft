from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
player = FirstPersonController()
Sky()
boxes = []
for i in range(20):
  for j in range(20):
    box = Button(color=color.white, model='cube', position=(j,0,i),
          texture='pasto.jpg', parent=scene, origin_y=0.5)
    boxes.append(box)

def input(key):
  for box in boxes:
    if box.hovered:
      if key == 'left mouse down':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='piedra.jpg', parent=scene, origin_y=0.5)  
        boxes.append(new)
      if key == 'right mouse dow':
        boxes.remove(new)
        destroy(box)
      if key == '1':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='tablon.jpg', parent=scene, origin_y=0.5)  
        boxes.append(new)
      if key == '2':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='arena.jpg', parent=scene, origin_y=0.5)  
        boxes.append(new)
      if key == '3':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='pasto.jpg', parent=scene, origin_y=0.5)  
        boxes.append(new)
      if key == '4':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='ladrillo.png', parent=scene, origin_y=0.5)  
        boxes.append(new)
      if key == '5':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='vidrio2.png', parent=scene, origin_y=0.5)  
        boxes.append(new)
      if key == '6':
        new = Button(color=color.white, model='quad', position=box.position + mouse.normal,
                    texture='flor.png', parent=scene, origin_y=0.5)  
      if key == '7':
        new = Button(color=color.white, model='quad', position=box.position + mouse.normal,
                    texture='pastoalt2.png', parent=scene, origin_y=0.5)   
        boxes.append(new)
app.run()
 