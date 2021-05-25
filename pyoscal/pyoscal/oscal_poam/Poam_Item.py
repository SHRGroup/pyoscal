class Poam_Item:
    """POA&M Item

    Describes an individual POA&M item.

    Attributes:
        uuid (uuid):Uniquely identifies the POA&M entry. This UUID
may be referenced elsewhere in an OSCAL document when
referring to this information. A UUID should be consistently
used for a given POA&M item across revisions of the
document.

        prose (str):Default value holder for raw data in texts

        title (markup-line):The title or name for this POA&M item .

        description (markup-multiline):A human-readable description
of POA&M item.

        oscal_property (ARRAY):

        link (ARRAY):

        origin (ARRAY):Identifies the source of the finding, such as
a tool or person.

        related_observation (ARRAY):Relates the poam-item to a set
of referenced observations that were used to determine the
finding.

        associated_risk (ARRAY):Relates the finding to a set of
referenced risks that were used to determine the finding.

        remarks (str):

    """

    contexts = [
        "oscal-poam",
        "oscal-metadata",
        "oscal-implementation-common",
        "oscal-assessment-common",
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
        "origin",
        "related_observation",
        "associated_risk",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        title,
        description,
        use_name='poam-item',
        prose=None,
        oscal_property=None,
        link=None,
        origin=None,
        related_observation=None,
        associated_risk=None,
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
        self._origin = None
        self.origin = \
            origin
        self._related_observation = None
        self.related_observation = \
            related_observation
        self._associated_risk = None
        self.associated_risk = \
            associated_risk
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
        if related_observation is None:
            self.related_observation = []
        if associated_risk is None:
            self.associated_risk = []

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
            origin=obj.get(
                'origin',
                None),
            related_observation=obj.get(
                'related_observation',
                None),
            associated_risk=obj.get(
                'associated_risk',
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
        newcls.related_observation = \
            obj.get('related_observations')
        newcls.associated_risk = \
            obj.get('related_risks')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """Uniquely identifies the POA&M entry. This UUID may be referenced
        elsewhere in an OSCAL document when referring to this information. A
        UUID should be consistently used for a given POA&M item across
        revisions of the document.
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
        """The title or name for this POA&M item .
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def description(self):
        """A human-readable description of POA&M item.
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
        """Identifies the source of the finding, such as a tool or person.
        """
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
    def related_observation(self):
        """Relates the poam-item to a set of referenced observations that were
        used to determine the finding.
        """
        return self._related_observation

    @related_observation.setter
    def related_observation(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._related_observation):
            self._related_observation = []
        if bool(x):
            if x != self._related_observation:
                self._related_observation += list(x)

    @property
    def related_observations(self):
        return self._related_observation

    @related_observations.setter
    def related_observations(self, x):
        self.related_observation(x)

    @property
    def associated_risk(self):
        """Relates the finding to a set of referenced risks that were used to
        determine the finding.
        """
        return self._associated_risk

    @associated_risk.setter
    def associated_risk(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._associated_risk):
            self._associated_risk = []
        if bool(x):
            if x != self._associated_risk:
                self._associated_risk += list(x)

    @property
    def related_risks(self):
        return self._associated_risk

    @related_risks.setter
    def related_risks(self, x):
        self.associated_risk(x)
