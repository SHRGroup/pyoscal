class Add:
    """Addition

    Specifies contents to be added into controls, in resolution

    Attributes:
        position (token):Where to add the new content with respect
to the targeted element (beside it or inside it)

        by_id (token):Target location of the addition.

        prose (str):Default value holder for raw data in texts

        title (markup-line):A name given to the control, which may
be used by a tool for display and navigation.

        parameter (ARRAY):

        oscal_property (ARRAY):

        link (ARRAY):

        part (ARRAY):

    """

    contexts = [
        "oscal-profile",
        "oscal-metadata",
        "oscal-catalog-common",
    ]
    parameters = [
        "position",
        "by_id",
    ]
    subcomponents = [
        "prose",
        "title",
        "parameter",
        "oscal_property",
        "link",
        "part",
    ]

    def __init__(
        self,
        use_name='add',
        position=None,
        by_id=None,
        prose=None,
        title=None,
        parameter=None,
        oscal_property=None,
        link=None,
        part=None,
    ):
        self._position = None
        self.position = \
            position
        self._by_id = None
        self.by_id = \
            by_id
        self._prose = None
        self.prose = \
            prose
        self._title = None
        self.title = \
            title
        self._parameter = None
        self.parameter = \
            parameter
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._part = None
        self.part = \
            part
        self.use_name = use_name
        if parameter is None:
            self.parameter = []
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if part is None:
            self.part = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            position=obj.get(
                'position',
                None),
            by_id=obj.get(
                'by_id',
                None),
            prose=obj.get(
                'prose',
                None),
            title=obj.get(
                'title',
                None),
            parameter=obj.get(
                'parameter',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            part=obj.get(
                'part',
                None),
        )
        newcls.parameter = \
            obj.get('params')
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.part = \
            obj.get('parts')
        newcls.parameter = \
            obj.get('param')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def position(self):
        """Where to add the new content with respect to the targeted element
        (beside it or inside it)
        """
        return self._position

    @position.setter
    def position(self, x):
        self._position = x

    @property
    def by_id(self):
        """Target location of the addition.
        """
        return self._by_id

    @by_id.setter
    def by_id(self, x):
        self._by_id = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def title(self):
        """A name given to the control, which may be used by a tool for display
        and navigation.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def parameter(self):
        return self._parameter

    @parameter.setter
    def parameter(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._parameter):
            self._parameter = []
        if bool(x):
            if x != self._parameter:
                self._parameter += list(x)

    @property
    def params(self):
        return self._parameter

    @params.setter
    def params(self, x):
        self.parameter(x)

    @property
    def param(self):
        return self._parameter

    @param.setter
    def param(self, x):
        self.parameter(x)

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
    def part(self):
        return self._part

    @part.setter
    def part(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._part):
            self._part = []
        if bool(x):
            if x != self._part:
                self._part += list(x)

    @property
    def parts(self):
        return self._part

    @parts.setter
    def parts(self, x):
        self.part(x)
