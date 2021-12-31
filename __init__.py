from mycroft import MycroftSkill, intent_file_handler


class ClosedDoors(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('doors.closed.intent')
    def handle_doors_closed(self, message):
        self.speak_dialog('The house garage door is open')
        self.speak_dialog('The shop garage door is open')
        self.speak_dialog('The art door is open')
        self.speak_dialog('The chicken door is open')


def create_skill():
    return ClosedDoors()

