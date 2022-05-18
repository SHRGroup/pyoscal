class Observation:
    """Observation

    Describes an individual observation.

    Attributes:
        uuid (uuid):Uniquely identifies this observation. This UUID
may be referenced elsewhere in an OSCAL document when
referring to this information. Once assigned, a UUID should
be consistently used for a given observation across
revisions.

        prose (str):Default value holder for raw data in texts

        title (markup-line):The title for this observation.

        description (markup-multiline):A human-readable description
of this assessment observation.

        oscal_property (ARRAY):

        link (ARRAY):

        method (ARRAY):Identifies how the observation was made.

        type (ARRAY):Identifies the nature of the observation. More
than one may be used to further qualify and enable
filtering.

        origin (ARRAY):

        subject (ARRAY):

        relevant_evidence (ARRAY):Links this observation to relevant
evidence.

        collected (dateTime-with-timezone):Date/time stamp
identifying when the finding information was collected.

        expires (dateTime-with-timezone):Date/time identifying when
the finding information is out-of-date and no longer valid.
Typically used with continuous assessment scenarios.

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
        "method",
        "type",
        "origin",
        "subject",
        "relevant_evidence",
        "collected",
        "expires",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        description,
        method,
        collected,
        use_name='observation',
        prose=None,
        title=None,
        oscal_property=None,
        link=None,
        type=None,
        origin=None,
        subject=None,
        relevant_evidence=None,
        expires=None,
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
        self._method = None
        self.method = \
            method
        self._type = None
        self.type = \
            type
        self._origin = None
        self.origin = \
            origin
        self._subject = None
        self.subject = \
            subject
        self._relevant_evidence = None
        self.relevant_evidence = \
            relevant_evidence
        self._collected = None
        self.collected = \
            collected
        self._expires = None
        self.expires = \
            expires
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if method is None:
            self.method = []
        if type is None:
            self.type = []
        if origin is None:
            self.origin = []
        if subject is None:
            self.subject = []
        if relevant_evidence is None:
            self.relevant_evidence = []

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
            method=obj.get(
                'method',
                None),
            type=obj.get(
                'type',
                None),
            origin=obj.get(
                'origin',
                None),
            subject=obj.get(
                'subject',
                None),
            relevant_evidence=obj.get(
                'relevant_evidence',
                None),
            collected=obj.get(
                'collected',
                None),
            expires=obj.get(
                'expires',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.method = \
            obj.get('methods')
        newcls.type = \
            obj.get('types')
        newcls.origin = \
            obj.get('origins')
        newcls.subject = \
            obj.get('subjects')
        newcls.relevant_evidence = \
            obj.get('relevant_evidence')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """Uniquely identifies this observation. This UUID may be referenced
        elsewhere in an OSCAL document when referring to this information.
        Once assigned, a UUID should be consistently used for a given
        observation across revisions.
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
        """The title for this observation.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def description(self):
        """A human-readable description of this assessment observation.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

    @property
    def collected(self):
        """Date/time stamp identifying when the finding information was
        collected.
        """
        return self._collected

    @collected.setter
    def collected(self, x):
        self._collected = x

    @property
    def expires(self):
        """Date/time identifying when the finding information is out-of-date
        and no longer valid. Typically used with continuous assessment
        scenarios.
        """
        return self._expires

    @expires.setter
    def expires(self, x):
        self._expires = x

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
    def method(self):
        """Identifies how the observation was made.
        """
        return self._method

    @method.setter
    def method(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._method):
            self._method = []
        if bool(x):
            if x != self._method:
                self._method += list(x)

    @property
    def methods(self):
        return self._method

    @methods.setter
    def methods(self, x):
        self.method(x)

    @property
    def type(self):
        """Identifies the nature of the observation. More than one may be used
        to further qualify and enable filtering.
        """
        return self._type

    @type.setter
    def type(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._type):
            self._type = []
        if bool(x):
            if x != self._type:
                self._type += list(x)

    @property
    def types(self):
        return self._type

    @types.setter
    def types(self, x):
        self.type(x)

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
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._subject):
            self._subject = []
        if bool(x):
            if x != self._subject:
                self._subject += list(x)

    @property
    def subjects(self):
        return self._subject

    @subjects.setter
    def subjects(self, x):
        self.subject(x)

    @property
    def relevant_evidence(self):
        """Links this observation to relevant evidence.
        """
        return self._relevant_evidence

    @relevant_evidence.setter
    def relevant_evidence(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._relevant_evidence):
            self._relevant_evidence = []
        if bool(x):
            if x != self._relevant_evidence:
                self._relevant_evidence += list(x)
