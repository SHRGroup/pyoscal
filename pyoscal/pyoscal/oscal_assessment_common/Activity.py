class Activity:
    """Activity

    Identifies an assessment or related process that can be performed. In
the assessment plan, this is an intended activity which may be
associated with an assessment task. In the assessment results, this an
activity that was actually performed as part of an assessment.

    Attributes:
        uuid (uuid):Uniquely identifies this assessment activity.
This UUID may be referenced elsewhere in an OSCAL document
when referring to this information. A UUID should be
consistently used for a given included activity across
revisions of the document.

        prose (str):Default value holder for raw data in texts

        title (markup-line):The title for this included activity.

        description (markup-multiline):A human-readable description
of this included activity.

        oscal_property (ARRAY):

        link (ARRAY):

        step (ARRAY):Identifies an individual step in a series of
steps related to an activity, such as an assessment test or
examination procedure.

        related_controls (str):

        responsible_role (ARRAY):

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
        "description",
        "oscal_property",
        "link",
        "step",
        "related_controls",
        "responsible_role",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        description,
        use_name='activity',
        prose=None,
        title=None,
        oscal_property=None,
        link=None,
        step=None,
        related_controls=None,
        responsible_role=None,
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
        self._description = None
        self.description = \
            description
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._step = None
        self.step = \
            step
        self._related_controls = None
        self.related_controls = \
            related_controls
        self._responsible_role = None
        self.responsible_role = \
            responsible_role
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if step is None:
            self.step = []
        if responsible_role is None:
            self.responsible_role = []

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
            description=obj.get(
                'description',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            step=obj.get(
                'step',
                None),
            related_controls=obj.get(
                'related_controls',
                None),
            responsible_role=obj.get(
                'responsible_role',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.step = \
            obj.get('steps')
        newcls.responsible_role = \
            obj.get('responsible_roles')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """Uniquely identifies this assessment activity. This UUID may be
        referenced elsewhere in an OSCAL document when referring to this
        information. A UUID should be consistently used for a given included
        activity across revisions of the document.
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
        """The title for this included activity.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def description(self):
        """A human-readable description of this included activity.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

    @property
    def related_controls(self):
        return self._related_controls

    @related_controls.setter
    def related_controls(self, x):
        self._related_controls = x

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
    def step(self):
        """Identifies an individual step in a series of steps related to an
        activity, such as an assessment test or examination procedure.
        """
        return self._step

    @step.setter
    def step(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._step):
            self._step = []
        if bool(x):
            if x != self._step:
                self._step += list(x)

    @property
    def steps(self):
        return self._step

    @steps.setter
    def steps(self, x):
        self.step(x)

    @property
    def responsible_role(self):
        return self._responsible_role

    @responsible_role.setter
    def responsible_role(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._responsible_role):
            self._responsible_role = []
        if bool(x):
            if x != self._responsible_role:
                self._responsible_role += list(x)

    @property
    def responsible_roles(self):
        return self._responsible_role

    @responsible_roles.setter
    def responsible_roles(self, x):
        self.responsible_role(x)


class Activity(Activity):
    def __init__(self, **kw):
        super(Activity, self).__init__(**kw)
        self.use_name = 'activity'
