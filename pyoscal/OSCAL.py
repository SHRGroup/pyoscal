from .core.OSCAL import OSCAL


class Oscal:

    def __init__(self):
        pass

    def export(self):
        oscal = OSCAL()
        oscal.add_model(self.oscal)
        return oscal.export(uuid=str(self.oscal.uuid))
