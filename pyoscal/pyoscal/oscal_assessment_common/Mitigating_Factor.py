class Mitigating_Factor:
    """Mitigating Factor

    Describes an existing mitigating factor that may affect the overall
determination of the risk, with an optional link to an implementation
statement in the SSP.

    Attributes:
        uuid (uuid):Uniquely identifies this mitigating factor. This
UUID may be referenced elsewhere in an OSCAL document when
referring to this information. Once assigned, a UUID should
be consistently used for a given mitigating factor across
revisions.

        implementation_uuid (uuid):Points to an implementation
statement in the SSP.

        prose (str):Default value holder for raw data in texts

        description (markup-multiline):A human-readable description
of this mitigating factor.

        oscal_property (ARRAY):

        link (ARRAY):

        subject (ARRAY):

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "uuid",
        "implementation_uuid",
    ]
    subcomponents = [
        "prose",
        "description",
        "oscal_property",
        "link",
        "subject",
    ]

    def __init__(
        self,
        uuid,
        description,
        use_name='mitigating-factor',
        implementation_uuid=None,
        prose=None,
        oscal_property=None,
        link=None,
        subject=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._implementation_uuid = None
        self.implementation_uuid = \
            implementation_uuid
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
        self._subject = None
        self.subject = \
            subject
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if subject is None:
            self.subject = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            uuid=obj.get(
                'uuid',
                None),
            implementation_uuid=obj.get(
                'implementation_uuid',
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
            subject=obj.get(
                'subject',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.subject = \
            obj.get('subjects')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """Uniquely identifies this mitigating factor. This UUID may be
        referenced elsewhere in an OSCAL document when referring to this
        information. Once assigned, a UUID should be consistently used for a
        given mitigating factor across revisions.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, x):
        self._uuid = x

    @property
    def implementation_uuid(self):
        """Points to an implementation statement in the SSP.
        """
        return self._implementation_uuid

    @implementation_uuid.setter
    def implementation_uuid(self, x):
        self._implementation_uuid = x

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
        """A human-readable description of this mitigating factor.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

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
