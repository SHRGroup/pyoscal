class Assessment_Platform:
    """Assessment Platform

    Used to represent the toolset used to perform aspects of the
assessment.

    Attributes:
        uuid (uuid):Uniquely identifies this assessment Platform.

        prose (str):Default value holder for raw data in texts

        title (markup-line):The title or name for the assessment
platform.

        oscal_property (ARRAY):

        link (ARRAY):

        uses_component (ARRAY):The set of components that are used
by the assessment platform.

        remarks (str):

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "uuid",
    ]
    subcomponents = [
        "prose",
        "title",
        "oscal_property",
        "link",
        "uses_component",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        use_name='assessment-platform',
        prose=None,
        title=None,
        oscal_property=None,
        link=None,
        uses_component=None,
        remarks=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._prose = None
        self.prose = \
            prose
        self._title = None
        self.title = \
            title
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._uses_component = None
        self.uses_component = \
            uses_component
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if uses_component is None:
            self.uses_component = []

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
            title=obj.get(
                'title',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            uses_component=obj.get(
                'uses_component',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.uses_component = \
            obj.get('uses_components')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """Uniquely identifies this assessment Platform.
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
    def title(self):
        """The title or name for the assessment platform.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

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
    def uses_component(self):
        """The set of components that are used by the assessment platform.
        """
        return self._uses_component

    @uses_component.setter
    def uses_component(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._uses_component):
            self._uses_component = []
        if bool(x):
            if x != self._uses_component:
                self._uses_component += list(x)

    @property
    def uses_components(self):
        return self._uses_component

    @uses_components.setter
    def uses_components(self, x):
        self.uses_component(x)
