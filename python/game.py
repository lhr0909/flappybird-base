import stdlib

# How to fetch states:
# gameObjects variable should have everything you need. For example,
# gameObjects.bird.body -> bird's body properties (position, velocity, etc)
# gameObjects.pipes -> pipes, all pipes are made into a single group, so you need to call
# gameObjects.pipes.children to get each set of pipes (top and bottom)
# Try to read through the pipe creation logic and see if you can figure out how to query the pipes

# use jumpBird() function call to jump the bird, once condition is met.
# makeJumpingDecision() is being called upon every state update in the game.

def makeJumpingDecision():
    print(gameObjects.bird.body.velocity)

window.makeJumpingDecision = makeJumpingDecision
