class Assessment_Subject_Placeholder:
    """Assessment Subject Placeholder

    Used when the assessment subjects will be determined as part of one or
more other assessment activities. These assessment subjects will be
recorded in the assessment results in the assessment log.

    Attributes:
        uuid (uuid):Uniquely identifies a set of assessment subjects
that will be identified by a task or an activity that is
part of a task.

        prose (str):Default value holder for raw data in texts

        description (markup-multiline):A human-readable description
of intent of this assessment subject placeholder.

        source (ARRAY):Assessment subjects will be identified while
conducting the referenced activity-instance.

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
        "uuid",
    ]
    subcomponents = [
        "prose",
        "description",
        "source",
        "oscal_property",
        "link",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        source,
        use_name='assessment-subject-placeholder',
        prose=None,
        description=None,
        oscal_property=None,
        link=None,
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
        self._source = None
        self.source = \
            source
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
        if source is None:
            self.source = []
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
            source=obj.get(
                'source',
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
        newcls.source = \
            obj.get('sources')
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """Uniquely identifies a set of assessment subjects that will be
        identified by a task or an activity that is part of a task.
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
        """A human-readable description of intent of this assessment subject
        placeholder.
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
    def source(self):
        """Assessment subjects will be identified while conducting the
        referenced activity-instance.
        """
        return self._source

    @source.setter
    def source(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._source):
            self._source = []
        if bool(x):
            if x != self._source:
                self._source += list(x)

    @property
    def sources(self):
        return self._source

    @sources.setter
    def sources(self, x):
        self.source(x)

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


class Subject_Placeholder(Assessment_Subject_Placeholder):
    def __init__(self, **kw):
        super(Subject_Placeholder, self).__init__(**kw)
        self.use_name = 'subject_placeholder'
