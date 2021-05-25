class Finding_Target:
    """Objective Status

    Captures an assessor's conclusions regarding the degree to which an
objective is satisfied.

    Attributes:
        type (string):Identifies the type of the target.

        id_ref (NCName):Identifies the specific target qualified by
the

        prose (str):Default value holder for raw data in texts

        title (markup-line):The title for this objective status.

        description (markup-multiline):A human-readable description
of the assessor's conclusions regarding the degree to which
an objective is satisfied.

        oscal_property (ARRAY):

        link (ARRAY):

        status (NCName):A brief indication as to whether the
objective is satisfied or not within a given system.

        implementation_status (str):

        remarks (str):

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "type",
        "id_ref",
    ]
    subcomponents = [
        "prose",
        "title",
        "description",
        "oscal_property",
        "link",
        "status",
        "implementation_status",
        "remarks",
    ]

    def __init__(
        self,
        type,
        id_ref,
        status,
        use_name='finding-target',
        prose=None,
        title=None,
        description=None,
        oscal_property=None,
        link=None,
        implementation_status=None,
        remarks=None,
    ):
        self._type = None
        self.type = \
            type
        self._id_ref = None
        self.id_ref = \
            id_ref
        self._prose = None
        self.prose = \
            prose
        self._title = None
        self.title = \
            title
        self._description = None
        self.description = \
            description
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._status = None
        self.status = \
            status
        self._implementation_status = None
        self.implementation_status = \
            implementation_status
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
            type=obj.get(
                'type',
                None),
            id_ref=obj.get(
                'id_ref',
                None),
            prose=obj.get(
                'prose',
                None),
            title=obj.get(
                'title',
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
            status=obj.get(
                'status',
                None),
            implementation_status=obj.get(
                'implementation_status',
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
    def type(self):
        """Identifies the type of the target.
        """
        return self._type

    @type.setter
    def type(self, x):
        self._type = x

    @property
    def id_ref(self):
        """Identifies the specific target qualified by the
        """
        return self._id_ref

    @id_ref.setter
    def id_ref(self, x):
        self._id_ref = x

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
        """The title for this objective status.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def description(self):
        """A human-readable description of the assessor's conclusions regarding
        the degree to which an objective is satisfied.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

    @property
    def status(self):
        """A brief indication as to whether the objective is satisfied or not
        within a given system.
        """
        return self._status

    @status.setter
    def status(self, x):
        self._status = x

    @property
    def implementation_status(self):
        return self._implementation_status

    @implementation_status.setter
    def implementation_status(self, x):
        self._implementation_status = x

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


class Target(Finding_Target):
    def __init__(self, **kw):
        super(Target, self).__init__(**kw)
        self.use_name = 'target'
