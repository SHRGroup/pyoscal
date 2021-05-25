class Citation:
    """Citation

    A citation consisting of end note text and optional structured
bibliographic data.

    Attributes:
        prose (str):Default value holder for raw data in texts

        text (markup-line):A line of citation text.

        oscal_property (ARRAY):

        biblio (str):A container for structured bibliographic
information. The model of this information is undefined by
OSCAL.

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
        "biblio",
    ]

    def __init__(
        self,
        text,
        use_name='citation',
        prose=None,
        oscal_property=None,
        biblio=None,
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
        self._biblio = None
        self.biblio = \
            biblio
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []

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
            biblio=obj.get(
                'biblio',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
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
    def biblio(self):
        """A container for structured bibliographic information. The model of
        this information is undefined by OSCAL.
        """
        return self._biblio

    @biblio.setter
    def biblio(self, x):
        self._biblio = x

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
