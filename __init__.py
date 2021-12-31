from mycroft import MycroftSkill, intent_file_handler


class ClosedDoors(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('doors.closed.intent')
    def handle_doors_closed(self, message):
        self.speak_dialog('doors.closed')


def create_skill():
    return ClosedDoors()

