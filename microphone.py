from talon import Module, actions

mod = Module()

@mod.action_class
class Actions:
    def toggle_microphone():
        """Toggle microphone between none and system default"""
        current_mic = actions.sound.active_microphone()
        if current_mic == "None":
            actions.sound.set_microphone("System Default")
        else:
            actions.sound.set_microphone("None")