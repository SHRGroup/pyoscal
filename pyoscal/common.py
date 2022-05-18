from uuid import uuid4
from datetime import datetime


def createUUID():
    return str(uuid4())


def getToday(fmt='iso'):
    now = datetime.now()
    if fmt == 'iso':
        return now.isoformat()
    elif fmt == 'day':
        return now.strftime('%Y%m%d')
    else:
        return now


def get_prose(obj, name, default=""):
    try:
        return getattr(obj, name).prose
    except Exception:
        return default


def get_prop(obj, name, default="", prop_class="", prose=False):
    matched = []
    try:
        for prop in obj.prop:
            filters = [prop.name.prose == name]
            if prop_class:
                filters += [prop.oscal_class.prose == prop_class]
            if all(filters):
                if not prose:
                    matched += [prop.value.prose]
                else:
                    matched += [prop.prose]
        if len(matched) == 1:
            return matched[0]
        else:
            return matched
    except Exception:
        return default
