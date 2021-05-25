class Data_Flow:
    """Data Flow

    A description of the logical flow of information within the system and
across its boundaries, optionally supplemented by diagrams that
illustrate these flows.

    Attributes:
        prose (str):Default value holder for raw data in texts

        description (markup-multiline):A summary of the system's
data flow.

        oscal_property (ARRAY):

        link (ARRAY):

        diagram (BY_KEY):

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
        "diagram",
        "remarks",
    ]

    def __init__(
        self,
        description,
        use_name='data-flow',
        prose=None,
        oscal_property=None,
        link=None,
        diagram=None,
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
        self._diagram = None
        self.diagram = \
            diagram
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if diagram is None:
            self.diagram = []

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
            diagram=obj.get(
                'diagram',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.diagram = \
            obj.get('diagrams')
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
        """A summary of the system's data flow.
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
    def diagram(self):
        return self._diagram

    @diagram.setter
    def diagram(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._diagram):
            self._diagram = []
        if bool(x):
            if x != self._diagram:
                self._diagram += list(x)

    @property
    def diagrams(self):
        return self._diagram

    @diagrams.setter
    def diagrams(self, x):
        self.diagram(x)
