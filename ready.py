from talon import actions, app


def on_ready():
    actions.mode.enable("command")
    actions.mode.enable("dictation")


app.register("ready", on_ready)
