class Assessment_Method:
    """Assessment Method

    A local definition of a control objective. Uses catalog syntax for
control objective and assessment activities.

    Attributes:
        uuid (uuid):Uniquely identifies this defined assessment
method. This UUID may be referenced elsewhere in an OSCAL
document when referring to this information. A UUID should
be consistently used for a given assessment method across
revisions of the document.

        prose (str):Default value holder for raw data in texts

        description (markup-multiline):A human-readable description
of this assessment method.

        oscal_property (ARRAY):

        link (ARRAY):

        assessment_part (str):

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
        "oscal_property",
        "link",
        "assessment_part",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        assessment_part,
        use_name='assessment-method',
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
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._assessment_part = None
        self.assessment_part = \
            assessment_part
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
            assessment_part=obj.get(
                'assessment_part',
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
        """Uniquely identifies this defined assessment method. This UUID may be
        referenced elsewhere in an OSCAL document when referring to this
        information. A UUID should be consistently used for a given
        assessment method across revisions of the document.
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
        """A human-readable description of this assessment method.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

    @property
    def assessment_part(self):
        return self._assessment_part

    @assessment_part.setter
    def assessment_part(self, x):
        self._assessment_part = x

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
