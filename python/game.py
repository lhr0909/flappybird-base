import stdlib

game = window.game

def createPipe():
    gap = 300
    # creating a group without putting into the game, yet
    pipe = game.make.group()
    topPipe = pipe.create(0, 0, 'topPipe')
    bottomPipe = pipe.create(0, 960 + gap, 'bottomPipe')

    pipe.x = game.width
    pipe.y = game.rnd.integerInRange(-900, -360)

    game.physics.arcade.enable(pipe)

    # set the property to everything in the group
    pipe.setAll('body.immovable', true)
    pipe.setAll('outOfBoundsKill', true)

    # when you add return, you can put equal sign '=' to the left
    return pipe


def preload():
    game.load.image('background', 'assets/background.png')
    game.load.image('topPipe', 'assets/top_pipe.png')
    game.load.image('bottomPipe', 'assets/bottom_pipe.png')

    game.load.spritesheet('bird', 'assets/bird.png', 156, 129)

def create():
    window.background = game.add.tileSprite(0, 0, game.width, 960, 'background')
    # stretch background so the size matches the screen
    window.background.scale.setTo(1, game.height / 960)

    game.physics.startSystem(Phaser.Physics.ARCADE)
    game.world.enableBody = True

    window.bird = game.add.sprite(game.width / 4, game.height / 4, 'bird')
    window.bird.scale.setTo(0.3, 0.3)
    window.bird.enableBody = True
    # creating a flying animation, notice assets/bird.png has a few birds,
    # here we slice the image into 3 parts and play the slices in order of
    # 0, 1, 2, 1 every 10 milliseconds
    window.bird.animations.add('flying', [0, 1, 2, 1], 10, True)
    window.bird.animations.play('flying')

    window.pipes = game.add.group()

    pipe = createPipe()
    pipe.x = game.width / 5 * 4
    window.pipes.add(pipe)

    window.pipeCounter = 100


def update():
    if window.pipeCounter > 0:
        window.pipeCounter = window.pipeCounter - 1
    else:
        newPipe = createPipe()
        window.pipes.add(newPipe)

        window.pipeCounter = 100
    pass

def render():
    pass

window.gameState = {
  "preload": preload,
  "create": create,
  "update": update,
  "render": render
}
