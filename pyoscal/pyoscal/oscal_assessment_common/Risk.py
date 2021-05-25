class Risk:
    """Identified Risk

    An identified risk.

    Attributes:
        uuid (uuid):Uniquely identifies this risk. This UUID may be
referenced elsewhere in an OSCAL document when referring to
this information. Once assigned, a UUID should be
consistently used for a given risk across revisions.

        prose (str):Default value holder for raw data in texts

        title (markup-line):The title for this risk.

        description (markup-multiline):A human-readable summary of
what was identified regarding the risk.

        statement (markup-multiline):An summary of impact for how
the risk affects the system.

        oscal_property (ARRAY):

        link (ARRAY):

        status (NCName):Describes the status of the associated risk.

        origin (ARRAY):

        threat_id (ARRAY):

        characterization (ARRAY):

        mitigating_factor (ARRAY):Describes an existing mitigating
factor that may affect the overall determination of the
risk, with an optional link to an implementation statement
in the SSP.

        deadline (dateTime-with-timezone):The date/time by which the
risk must be resolved.

        response (ARRAY):

        risk_log (str):A log of all risk-related tasks taken.

        related_observation (ARRAY):Relates the finding to a set of
referenced observations that were used to determine the
finding.

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
        "statement",
        "oscal_property",
        "link",
        "status",
        "origin",
        "threat_id",
        "characterization",
        "mitigating_factor",
        "deadline",
        "response",
        "risk_log",
        "related_observation",
    ]

    def __init__(
        self,
        uuid,
        title,
        description,
        statement,
        status,
        use_name='risk',
        prose=None,
        oscal_property=None,
        link=None,
        origin=None,
        threat_id=None,
        characterization=None,
        mitigating_factor=None,
        deadline=None,
        response=None,
        risk_log=None,
        related_observation=None,
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
        self._statement = None
        self.statement = \
            statement
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._status = None
        self.status = \
            status
        self._origin = None
        self.origin = \
            origin
        self._threat_id = None
        self.threat_id = \
            threat_id
        self._characterization = None
        self.characterization = \
            characterization
        self._mitigating_factor = None
        self.mitigating_factor = \
            mitigating_factor
        self._deadline = None
        self.deadline = \
            deadline
        self._response = None
        self.response = \
            response
        self._risk_log = None
        self.risk_log = \
            risk_log
        self._related_observation = None
        self.related_observation = \
            related_observation
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if origin is None:
            self.origin = []
        if threat_id is None:
            self.threat_id = []
        if characterization is None:
            self.characterization = []
        if mitigating_factor is None:
            self.mitigating_factor = []
        if response is None:
            self.response = []
        if related_observation is None:
            self.related_observation = []

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
            statement=obj.get(
                'statement',
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
            origin=obj.get(
                'origin',
                None),
            threat_id=obj.get(
                'threat_id',
                None),
            characterization=obj.get(
                'characterization',
                None),
            mitigating_factor=obj.get(
                'mitigating_factor',
                None),
            deadline=obj.get(
                'deadline',
                None),
            response=obj.get(
                'response',
                None),
            risk_log=obj.get(
                'risk_log',
                None),
            related_observation=obj.get(
                'related_observation',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.origin = \
            obj.get('origins')
        newcls.threat_id = \
            obj.get('threat_ids')
        newcls.characterization = \
            obj.get('characterizations')
        newcls.mitigating_factor = \
            obj.get('mitigating_factors')
        newcls.response = \
            obj.get('remediations')
        newcls.related_observation = \
            obj.get('related_observations')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """Uniquely identifies this risk. This UUID may be referenced elsewhere
        in an OSCAL document when referring to this information. Once
        assigned, a UUID should be consistently used for a given risk across
        revisions.
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
        """The title for this risk.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def description(self):
        """A human-readable summary of what was identified regarding the risk.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

    @property
    def statement(self):
        """An summary of impact for how the risk affects the system.
        """
        return self._statement

    @statement.setter
    def statement(self, x):
        self._statement = x

    @property
    def status(self):
        """Describes the status of the associated risk.
        """
        return self._status

    @status.setter
    def status(self, x):
        self._status = x

    @property
    def deadline(self):
        """The date/time by which the risk must be resolved.
        """
        return self._deadline

    @deadline.setter
    def deadline(self, x):
        self._deadline = x

    @property
    def risk_log(self):
        """A log of all risk-related tasks taken.
        """
        return self._risk_log

    @risk_log.setter
    def risk_log(self, x):
        self._risk_log = x

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
    def threat_id(self):
        return self._threat_id

    @threat_id.setter
    def threat_id(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._threat_id):
            self._threat_id = []
        if bool(x):
            if x != self._threat_id:
                self._threat_id += list(x)

    @property
    def threat_ids(self):
        return self._threat_id

    @threat_ids.setter
    def threat_ids(self, x):
        self.threat_id(x)

    @property
    def characterization(self):
        return self._characterization

    @characterization.setter
    def characterization(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._characterization):
            self._characterization = []
        if bool(x):
            if x != self._characterization:
                self._characterization += list(x)

    @property
    def characterizations(self):
        return self._characterization

    @characterizations.setter
    def characterizations(self, x):
        self.characterization(x)

    @property
    def mitigating_factor(self):
        """Describes an existing mitigating factor that may affect the overall
        determination of the risk, with an optional link to an
        implementation statement in the SSP.
        """
        return self._mitigating_factor

    @mitigating_factor.setter
    def mitigating_factor(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._mitigating_factor):
            self._mitigating_factor = []
        if bool(x):
            if x != self._mitigating_factor:
                self._mitigating_factor += list(x)

    @property
    def mitigating_factors(self):
        return self._mitigating_factor

    @mitigating_factors.setter
    def mitigating_factors(self, x):
        self.mitigating_factor(x)

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._response):
            self._response = []
        if bool(x):
            if x != self._response:
                self._response += list(x)

    @property
    def remediations(self):
        return self._response

    @remediations.setter
    def remediations(self, x):
        self.response(x)

    @property
    def related_observation(self):
        """Relates the finding to a set of referenced observations that were
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
