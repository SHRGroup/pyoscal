class Diagram:
    """Diagram

    A graphic that provides a visual representation the system, or some
aspect of it.

    Attributes:
        uuid (uuid):The identifier for this diagram.

        prose (str):Default value holder for raw data in texts

        description (markup-multiline):A summary of the diagram.

        oscal_property (ARRAY):

        link (ARRAY):

        caption (markup-line):A brief caption to annotate the
diagram.

        remarks (markup-multiline):Commentary about the diagram that
enhances it.

    """

    contexts = [
        "oscal-ssp",
        "oscal-metadata",
        "oscal-implementation-common",
    ]
    parameters = [
        "uuid",
    ]
    subcomponents = [
        "prose",
        "description",
        "oscal_property",
        "link",
        "caption",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        use_name='diagram',
        prose=None,
        description=None,
        oscal_property=None,
        link=None,
        caption=None,
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
        self._caption = None
        self.caption = \
            caption
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
            caption=obj.get(
                'caption',
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
    def uuid(self):
        """The identifier for this diagram.
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
        """A summary of the diagram.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

    @property
    def caption(self):
        """A brief caption to annotate the diagram.
        """
        return self._caption

    @caption.setter
    def caption(self, x):
        self._caption = x

    @property
    def remarks(self):
        """Commentary about the diagram that enhances it.
        """
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
