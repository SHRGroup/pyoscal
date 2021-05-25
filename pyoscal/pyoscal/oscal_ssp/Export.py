class Export:
    """Export

    Identifies content intended for external consumption, such as with
leveraged organizations.

    Attributes:
        prose (str):Default value holder for raw data in texts

        description (markup-multiline):An implementation statement
that describes the aspects of the control or control
statement implementation that can be available to another
system leveraging this system.

        oscal_property (ARRAY):

        link (ARRAY):

        provided (ARRAY):Describes a capability which may be
inherited by a leveraging system.

        responsibility (ARRAY):Describes a control implementation
responsibility imposed on a leveraging system.

        remarks (str):

    """

    contexts = [
        "oscal-ssp",
        "oscal-metadata",
        "oscal-implementation-common",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "description",
        "oscal_property",
        "link",
        "provided",
        "responsibility",
        "remarks",
    ]

    def __init__(
        self,
        use_name='export',
        prose=None,
        description=None,
        oscal_property=None,
        link=None,
        provided=None,
        responsibility=None,
        remarks=None,
    ):
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
        self._provided = None
        self.provided = \
            provided
        self._responsibility = None
        self.responsibility = \
            responsibility
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if provided is None:
            self.provided = []
        if responsibility is None:
            self.responsibility = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
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
            provided=obj.get(
                'provided',
                None),
            responsibility=obj.get(
                'responsibility',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.provided = \
            obj.get('provided')
        newcls.responsibility = \
            obj.get('responsibilities')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

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
        """An implementation statement that describes the aspects of the
        control or control statement implementation that can be available to
        another system leveraging this system.
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
    def provided(self):
        """Describes a capability which may be inherited by a leveraging
        system.
        """
        return self._provided

    @provided.setter
    def provided(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._provided):
            self._provided = []
        if bool(x):
            if x != self._provided:
                self._provided += list(x)

    @property
    def responsibility(self):
        """Describes a control implementation responsibility imposed on a
        leveraging system.
        """
        return self._responsibility

    @responsibility.setter
    def responsibility(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._responsibility):
            self._responsibility = []
        if bool(x):
            if x != self._responsibility:
                self._responsibility += list(x)

    @property
    def responsibilities(self):
        return self._responsibility

    @responsibilities.setter
    def responsibilities(self, x):
        self.responsibility(x)
