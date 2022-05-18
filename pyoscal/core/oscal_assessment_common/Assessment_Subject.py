class Assessment_Subject:
    """Subject of Assessment

    Identifies system elements being assessed, such as components,
inventory items, and locations. In the assessment plan, this
identifies a planned assessment subject. In the assessment results
this is an actual assessment subject, and reflects any changes from
the plan. exactly what will be the focus of this assessment. Any
subjects not identified in this way are out-of-scope.

    Attributes:
        type (token):Indicates the type of assessment subject, such
as a component, inventory, item, location, or party
represented by this selection statement.

        prose (str):Default value holder for raw data in texts

        description (markup-multiline):A human-readable description
of the collection of subjects being included in this
assessment.

        oscal_property (ARRAY):

        link (ARRAY):

        exclude_subject (ARRAY):

        remarks (str):

        include_all (str):A key word to indicate all.

        include_subject (ARRAY):

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "type",
    ]
    subcomponents = [
        "prose",
        "description",
        "oscal_property",
        "link",
        "exclude_subject",
        "remarks",
        "include_all",
        "include_subject",
    ]

    def __init__(
        self,
        type,
        include_all,
        include_subject,
        use_name='assessment-subject',
        prose=None,
        description=None,
        oscal_property=None,
        link=None,
        exclude_subject=None,
        remarks=None,
    ):
        self._type = None
        self.type = \
            type
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
        self._exclude_subject = None
        self.exclude_subject = \
            exclude_subject
        self._remarks = None
        self.remarks = \
            remarks
        self._include_all = None
        self.include_all = \
            include_all
        self._include_subject = None
        self.include_subject = \
            include_subject
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if exclude_subject is None:
            self.exclude_subject = []
        if include_subject is None:
            self.include_subject = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            type=obj.get(
                'type',
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
            exclude_subject=obj.get(
                'exclude_subject',
                None),
            remarks=obj.get(
                'remarks',
                None),
            include_all=obj.get(
                'include_all',
                None),
            include_subject=obj.get(
                'include_subject',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.exclude_subject = \
            obj.get('exclude_subjects')
        newcls.include_subject = \
            obj.get('include_subjects')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def type(self):
        """Indicates the type of assessment subject, such as a component,
        inventory, item, location, or party represented by this selection
        statement.
        """
        return self._type

    @type.setter
    def type(self, x):
        self._type = x

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
        """A human-readable description of the collection of subjects being
        included in this assessment.
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
    def include_all(self):
        """A key word to indicate all.
        """
        return self._include_all

    @include_all.setter
    def include_all(self, x):
        self._include_all = x

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
    def exclude_subject(self):
        return self._exclude_subject

    @exclude_subject.setter
    def exclude_subject(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._exclude_subject):
            self._exclude_subject = []
        if bool(x):
            if x != self._exclude_subject:
                self._exclude_subject += list(x)

    @property
    def exclude_subjects(self):
        return self._exclude_subject

    @exclude_subjects.setter
    def exclude_subjects(self, x):
        self.exclude_subject(x)

    @property
    def include_subject(self):
        return self._include_subject

    @include_subject.setter
    def include_subject(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._include_subject):
            self._include_subject = []
        if bool(x):
            if x != self._include_subject:
                self._include_subject += list(x)

    @property
    def include_subjects(self):
        return self._include_subject

    @include_subjects.setter
    def include_subjects(self, x):
        self.include_subject(x)


class Subject(Assessment_Subject):
    def __init__(self, **kw):
        super(Subject, self).__init__(**kw)
        self.use_name = 'subject'
