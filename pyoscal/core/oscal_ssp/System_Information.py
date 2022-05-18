class System_Information:
    """System Information

    Contains details about all information types that are stored,
processed, or transmitted by the system, such as privacy information,
and those defined in

    Attributes:
        prose (str):Default value holder for raw data in texts

        oscal_property (ARRAY):

        link (ARRAY):

        information_type (ARRAY):Contains details about one
information type that is stored, processed, or transmitted
by the system, such as privacy information, and those
defined in

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
        "oscal_property",
        "link",
        "information_type",
    ]

    def __init__(
        self,
        information_type,
        use_name='system-information',
        prose=None,
        oscal_property=None,
        link=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._information_type = None
        self.information_type = \
            information_type
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if information_type is None:
            self.information_type = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            information_type=obj.get(
                'information_type',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.information_type = \
            obj.get('information_types')
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
    def information_type(self):
        """Contains details about one information type that is stored,
        processed, or transmitted by the system, such as privacy
        information, and those defined in
        """
        return self._information_type

    @information_type.setter
    def information_type(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._information_type):
            self._information_type = []
        if bool(x):
            if x != self._information_type:
                self._information_type += list(x)

    @property
    def information_types(self):
        return self._information_type

    @information_types.setter
    def information_types(self, x):
        self.information_type(x)
