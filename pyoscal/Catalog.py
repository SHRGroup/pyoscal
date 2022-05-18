from .core.oscal_catalog import (
    Group, Control
)
from .OSCAL import Oscal
from .common import get_prose


class Catalog(Oscal):

    def __init__(
        self,
        obj=None
    ):

        if obj:
            self.oscal = obj
            return

    def get_part(self, cOrP, name):
        text = ""
        for part in cOrP.part:
            if part.name.prose == name:
                text += self.get_part(part, 'item')
                if part.prose:
                    text += part.prose
        text = text.replace('<p>', '').replace('</p>', '')
        return text

    def control2dict(self, control):
        c_details = {
            'id': control.id.prose,
            'title': control.title.prose,
            'guidance': self.get_part(control, 'guidance'),
            'statement': self.get_part(control, 'statement'),
            'children': [self.control2dict(c) for c in control.control]
        }
        if control.parameter:
            c_details['parameters'] = [
                dict(
                    id=p.id.prose,
                    label=get_prose(p, 'label')
                )
                for p in control.parameter]
        else:
            c_details['parameters'] = []
        return c_details

    def get_controls(self, grpOrCtrl):
        return_value = []
        if isinstance(grpOrCtrl, list):
            for gOrC in grpOrCtrl:
                return_value += self.get_controls(gOrC)
        elif isinstance(grpOrCtrl, Group.Group):
            for group in grpOrCtrl.group:
                return_value += self.get_controls(group)
            for control in grpOrCtrl.control:
                return_value += self.get_controls(control)
        elif isinstance(grpOrCtrl, Control.Control):
            return [self.control2dict(grpOrCtrl)]
        return return_value

    @property
    def controls(self):
        return_value = {}
        for group in self.oscal.group:
            return_value[group.title.prose] = self.get_controls(group)
        for control in self.oscal.control:
            return_value['root'] = self.get_controls(control)
        return return_value
