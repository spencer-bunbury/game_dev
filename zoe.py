import panda3d
import random
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor

class MyGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
class ActorControlExample(ShowBase):
    def __init__(self):
        super().__init__()

        # Load an environment model (optional, for context)
        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)


        # self.actor_picture.loop("walk") # Start an animation

        # Start playing the walk animation
        self.pandaActor.loop("walk")




game = MyGame()
game.run()
