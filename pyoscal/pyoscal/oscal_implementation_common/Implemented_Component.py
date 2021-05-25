class Implemented_Component:
    """Implemented Component

    The set of components that are implemented in a given system inventory
item.

    Attributes:
        component_uuid (uuid):A reference to a component that is
implemented as part of an inventory item.

        prose (str):Default value holder for raw data in texts

        oscal_property (ARRAY):

        link (ARRAY):

        responsible_party (BY_KEY):

        remarks (str):

    """

    contexts = [
        "oscal-implementation-common",
        "oscal-metadata",
    ]
    parameters = [
        "component_uuid",
    ]
    subcomponents = [
        "prose",
        "oscal_property",
        "link",
        "responsible_party",
        "remarks",
    ]

    def __init__(
        self,
        component_uuid,
        use_name='implemented-component',
        prose=None,
        oscal_property=None,
        link=None,
        responsible_party=None,
        remarks=None,
    ):
        self._component_uuid = None
        self.component_uuid = \
            component_uuid
        self._prose = None
        self.prose = \
            prose
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._responsible_party = None
        self.responsible_party = \
            responsible_party
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if responsible_party is None:
            self.responsible_party = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            component_uuid=obj.get(
                'component_uuid',
                None),
            prose=obj.get(
                'prose',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            responsible_party=obj.get(
                'responsible_party',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.responsible_party = \
            obj.get('responsible_parties')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def component_uuid(self):
        """A reference to a component that is implemented as part of an
        inventory item.
        """
        return self._component_uuid

    @component_uuid.setter
    def component_uuid(self, x):
        self._component_uuid = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, x):
        self._remarks = x

    @property
    def oscal_property(self):
        return self._oscal_property

    @oscal_property.setter
    def oscal_property(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._oscal_property):
            self._oscal_property = []
        if bool(x):
            if x != self._oscal_property:
                self._oscal_property += list(x)

    @property
    def props(self):
        return self._oscal_property

    @props.setter
    def props(self, x):
        self.oscal_property(x)

    @property
    def prop(self):
        return self._oscal_property

    @prop.setter
    def prop(self, x):
        self.oscal_property(x)

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._link):
            self._link = []
        if bool(x):
            if x != self._link:
                self._link += list(x)

    @property
    def links(self):
        return self._link

    @links.setter
    def links(self, x):
        self.link(x)

    @property
    def responsible_party(self):
        return self._responsible_party

    @responsible_party.setter
    def responsible_party(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._responsible_party):
            self._responsible_party = []
        if bool(x):
            if x != self._responsible_party:
                self._responsible_party += list(x)

    @property
    def responsible_parties(self):
        return self._responsible_party

    @responsible_parties.setter
    def responsible_parties(self, x):
        self.responsible_party(x)
