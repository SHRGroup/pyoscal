class Response:
    """Risk Response

    Describes either recommended or an actual plan for addressing the
risk.

    Attributes:
        uuid (uuid):Uniquely identifies this remediation. This UUID
may be referenced elsewhere in an OSCAL document when
referring to this information. Once assigned, a UUID should
be consistently used for a given remediation across
revisions.

        lifecycle (NCName):Identifies whether this is a
recommendation, such as from an assessor or tool, or an
actual plan accepted by the system owner.

        prose (str):Default value holder for raw data in texts

        title (markup-line):The title for this response activity.

        description (markup-multiline):A human-readable description
of this response plan.

        oscal_property (ARRAY):

        link (ARRAY):

        origin (ARRAY):

        required_asset (ARRAY):Identifies an asset required to
achieve remediation.

        task (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "uuid",
        "lifecycle",
    ]
    subcomponents = [
        "prose",
        "title",
        "description",
        "oscal_property",
        "link",
        "origin",
        "required_asset",
        "task",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        lifecycle,
        title,
        description,
        use_name='response',
        prose=None,
        oscal_property=None,
        link=None,
        origin=None,
        required_asset=None,
        task=None,
        remarks=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._lifecycle = None
        self.lifecycle = \
            lifecycle
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
        self._origin = None
        self.origin = \
            origin
        self._required_asset = None
        self.required_asset = \
            required_asset
        self._task = None
        self.task = \
            task
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if origin is None:
            self.origin = []
        if required_asset is None:
            self.required_asset = []
        if task is None:
            self.task = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            uuid=obj.get(
                'uuid',
                None),
            lifecycle=obj.get(
                'lifecycle',
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
            origin=obj.get(
                'origin',
                None),
            required_asset=obj.get(
                'required_asset',
                None),
            task=obj.get(
                'task',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.origin = \
            obj.get('origins')
        newcls.required_asset = \
            obj.get('required_assets')
        newcls.task = \
            obj.get('tasks')
        newcls.oscal_property = \
            obj.get('prop')
        newcls.task = \
            obj.get('assessment_task')
        newcls.task = \
            obj.get('assessment_task')
        return newcls

    @property
    def uuid(self):
        """Uniquely identifies this remediation. This UUID may be referenced
        elsewhere in an OSCAL document when referring to this information.
        Once assigned, a UUID should be consistently used for a given
        remediation across revisions.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, x):
        self._uuid = x

    @property
    def lifecycle(self):
        """Identifies whether this is a recommendation, such as from an
        assessor or tool, or an actual plan accepted by the system owner.
        """
        return self._lifecycle

    @lifecycle.setter
    def lifecycle(self, x):
        self._lifecycle = x

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
        """The title for this response activity.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def description(self):
        """A human-readable description of this response plan.
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
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._origin):
            self._origin = []
        if bool(x):
            if x != self._origin:
                self._origin += list(x)

    @property
    def origins(self):
        return self._origin

    @origins.setter
    def origins(self, x):
        self.origin(x)

    @property
    def required_asset(self):
        """Identifies an asset required to achieve remediation.
        """
        return self._required_asset

    @required_asset.setter
    def required_asset(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._required_asset):
            self._required_asset = []
        if bool(x):
            if x != self._required_asset:
                self._required_asset += list(x)

    @property
    def required_assets(self):
        return self._required_asset

    @required_assets.setter
    def required_assets(self, x):
        self.required_asset(x)

    @property
    def task(self):
        return self._task

    @task.setter
    def task(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._task):
            self._task = []
        if bool(x):
            if x != self._task:
                self._task += list(x)

    @property
    def tasks(self):
        return self._task

    @tasks.setter
    def tasks(self, x):
        self.task(x)

    @property
    def assessment_task(self):
        return self._task

    @assessment_task.setter
    def assessment_task(self, x):
        self.task(x)

    @property
    def assessment_task(self):
        return self._task

    @assessment_task.setter
    def assessment_task(self, x):
        self.task(x)
