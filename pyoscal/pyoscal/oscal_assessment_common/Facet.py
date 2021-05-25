class Facet:
    """Facet

    An individual characteristic that is part of a larger set produced by
the same actor.

    Attributes:
        name (NCName):The name of the risk metric within the
specified system.

        system (uri):Specifies the naming system under which this
risk metric is organized, which allows for the same names to
be used in different systems controlled by different
parties. This avoids the potential of a name clash.

        value (string):Indicates the value of the facet.

        prose (str):Default value holder for raw data in texts

        oscal_property (ARRAY):

        link (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "name",
        "system",
        "value",
    ]
    subcomponents = [
        "prose",
        "oscal_property",
        "link",
        "remarks",
    ]

    def __init__(
        self,
        name,
        system,
        value,
        use_name='facet',
        prose=None,
        oscal_property=None,
        link=None,
        remarks=None,
    ):
        self._name = None
        self.name = \
            name
        self._system = None
        self.system = \
            system
        self._value = None
        self.value = \
            value
        self._prose = None
        self.prose = \
            prose
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            name=obj.get(
                'name',
                None),
            system=obj.get(
                'system',
                None),
            value=obj.get(
                'value',
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
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def name(self):
        """The name of the risk metric within the specified system.
        """
        return self._name

    @name.setter
    def name(self, x):
        self._name = x

    @property
    def system(self):
        """Specifies the naming system under which this risk metric is
        organized, which allows for the same names to be used in different
        systems controlled by different parties. This avoids the potential
        of a name clash.
        """
        return self._system

    @system.setter
    def system(self, x):
        self._system = x

    @property
    def value(self):
        """Indicates the value of the facet.
        """
        return self._value

    @value.setter
    def value(self, x):
        self._value = x

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
