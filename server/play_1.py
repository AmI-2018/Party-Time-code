import pyglet

music = pyglet.resource.media("song.mp3")
music.play()

pyglet.app.run()