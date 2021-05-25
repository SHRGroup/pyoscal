class Inventory_Item:
    """Inventory Item

    A single managed inventory item within the system.

    Attributes:
        uuid (uuid):A globally unique identifier that can be used to
reference this inventory item entry elsewhere in an OSCAL
document. A UUID should be consistently used for a given
resource across revisions of the document.

        prose (str):Default value holder for raw data in texts

        description (markup-multiline):A summary of the inventory
item stating its purpose within the system.

        oscal_property (ARRAY):

        link (ARRAY):

        responsible_party (BY_KEY):

        implemented_component (ARRAY):The set of components that are
implemented in a given system inventory item.

        remarks (str):

    """

    contexts = [
        "oscal-implementation-common",
        "oscal-metadata",
    ]
    parameters = [
        "uuid",
    ]
    subcomponents = [
        "prose",
        "description",
        "oscal_property",
        "link",
        "responsible_party",
        "implemented_component",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        description,
        use_name='inventory-item',
        prose=None,
        oscal_property=None,
        link=None,
        responsible_party=None,
        implemented_component=None,
        remarks=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._prose = None
        self.prose = \
            prose
        self._description = None
        self.description = \
            description
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._responsible_party = None
        self.responsible_party = \
            responsible_party
        self._implemented_component = None
        self.implemented_component = \
            implemented_component
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
        if implemented_component is None:
            self.implemented_component = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            uuid=obj.get(
                'uuid',
                None),
            prose=obj.get(
                'prose',
                None),
            description=obj.get(
                'description',
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
            implemented_component=obj.get(
                'implemented_component',
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
        newcls.implemented_component = \
            obj.get('implemented_components')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """A globally unique identifier that can be used to reference this
        inventory item entry elsewhere in an OSCAL document. A UUID should
        be consistently used for a given resource across revisions of the
        document.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, x):
        self._uuid = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def description(self):
        """A summary of the inventory item stating its purpose within the
        system.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

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

    @property
    def implemented_component(self):
        """The set of components that are implemented in a given system
        inventory item.
        """
        return self._implemented_component

    @implemented_component.setter
    def implemented_component(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._implemented_component):
            self._implemented_component = []
        if bool(x):
            if x != self._implemented_component:
                self._implemented_component += list(x)

    @property
    def implemented_components(self):
        return self._implemented_component

    @implemented_components.setter
    def implemented_components(self, x):
        self.implemented_component(x)
