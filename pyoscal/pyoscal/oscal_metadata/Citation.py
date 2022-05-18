class Citation:
    """Citation

    A citation consisting of end note text and optional structured
bibliographic data.

    Attributes:
        prose (str):Default value holder for raw data in texts

        text (markup-line):A line of citation text.

        oscal_property (ARRAY):

        link (ARRAY):

    """

    contexts = [
        "oscal-metadata",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "text",
        "oscal_property",
        "link",
    ]

    def __init__(
        self,
        text,
        use_name='citation',
        prose=None,
        oscal_property=None,
        link=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._text = None
        self.text = \
            text
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
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
            prose=obj.get(
                'prose',
                None),
            text=obj.get(
                'text',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
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
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def text(self):
        """A line of citation text.
        """
        return self._text

    @text.setter
    def text(self, x):
        self._text = x

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
