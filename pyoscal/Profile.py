from .OSCAL import Oscal


class Profile(Oscal):

    def __init__(
        self,
        obj=None
    ):

        if obj:
            self.oscal = obj
            return
