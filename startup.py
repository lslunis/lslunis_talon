from talon import actions, app


def on_ready():
    actions.sound.set_microphone("None")


app.register("ready", on_ready)
