class Result:
    """Assessment Result

    Used by the assessment results and POA&M. In the assessment results,
this identifies all of the assessment observations and findings,
initial and residual risks, deviations, and disposition. In the POA&M,
this identifies initial and residual risks, deviations, and
disposition.

    Attributes:
        uuid (uuid):Uniquely identifies this set of results. This
UUID may be referenced elsewhere in an OSCAL document when
referring to this information. Once assigned, a UUID should
be consistently used for a given set of results across
revisions.

        prose (str):Default value holder for raw data in texts

        title (markup-line):The title for this set of results.

        description (markup-multiline):A human-readable description
of this set of test results.

        start (dateTime-with-timezone):Date/time stamp identifying
the start of the evidence collection reflected in these
results.

        end (dateTime-with-timezone):Date/time stamp identifying the
end of the evidence collection reflected in these results.
In a continuous motoring scenario, this may contain the same
value as start if appropriate.

        oscal_property (ARRAY):

        link (ARRAY):

        local_definitions (str):Used to define data objects that are
used in the assessment plan, that do not appear in the
referenced SSP.

        reviewed_controls (str):

        attestation (ARRAY):A set of textual statements, typically
written by the assessor.

        assessment_log (str):A log of all assessment-related actions
taken.

        observation (ARRAY):

        risk (ARRAY):

        finding (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-ar",
        "oscal-metadata",
        "oscal-assessment-common",
    ]
    parameters = [
        "uuid",
    ]
    subcomponents = [
        "prose",
        "title",
        "description",
        "start",
        "end",
        "oscal_property",
        "link",
        "local_definitions",
        "reviewed_controls",
        "attestation",
        "assessment_log",
        "observation",
        "risk",
        "finding",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        title,
        description,
        start,
        reviewed_controls,
        use_name='result',
        prose=None,
        end=None,
        oscal_property=None,
        link=None,
        local_definitions=None,
        attestation=None,
        assessment_log=None,
        observation=None,
        risk=None,
        finding=None,
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
        self._start = None
        self.start = \
            start
        self._end = None
        self.end = \
            end
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._local_definitions = None
        self.local_definitions = \
            local_definitions
        self._reviewed_controls = None
        self.reviewed_controls = \
            reviewed_controls
        self._attestation = None
        self.attestation = \
            attestation
        self._assessment_log = None
        self.assessment_log = \
            assessment_log
        self._observation = None
        self.observation = \
            observation
        self._risk = None
        self.risk = \
            risk
        self._finding = None
        self.finding = \
            finding
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if attestation is None:
            self.attestation = []
        if observation is None:
            self.observation = []
        if risk is None:
            self.risk = []
        if finding is None:
            self.finding = []

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
            start=obj.get(
                'start',
                None),
            end=obj.get(
                'end',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            local_definitions=obj.get(
                'local_definitions',
                None),
            reviewed_controls=obj.get(
                'reviewed_controls',
                None),
            attestation=obj.get(
                'attestation',
                None),
            assessment_log=obj.get(
                'assessment_log',
                None),
            observation=obj.get(
                'observation',
                None),
            risk=obj.get(
                'risk',
                None),
            finding=obj.get(
                'finding',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('prop')
        newcls.link = \
            obj.get('links')
        newcls.attestation = \
            obj.get('attestations')
        newcls.observation = \
            obj.get('observations')
        newcls.risk = \
            obj.get('risks')
        newcls.finding = \
            obj.get('findings')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """Uniquely identifies this set of results. This UUID may be referenced
        elsewhere in an OSCAL document when referring to this information.
        Once assigned, a UUID should be consistently used for a given set of
        results across revisions.
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
        """The title for this set of results.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def description(self):
        """A human-readable description of this set of test results.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

    @property
    def start(self):
        """Date/time stamp identifying the start of the evidence collection
        reflected in these results.
        """
        return self._start

    @start.setter
    def start(self, x):
        self._start = x

    @property
    def end(self):
        """Date/time stamp identifying the end of the evidence collection
        reflected in these results. In a continuous motoring scenario, this
        may contain the same value as start if appropriate.
        """
        return self._end

    @end.setter
    def end(self, x):
        self._end = x

    @property
    def local_definitions(self):
        """Used to define data objects that are used in the assessment plan,
        that do not appear in the referenced SSP.
        """
        return self._local_definitions

    @local_definitions.setter
    def local_definitions(self, x):
        self._local_definitions = x

    @property
    def reviewed_controls(self):
        return self._reviewed_controls

    @reviewed_controls.setter
    def reviewed_controls(self, x):
        self._reviewed_controls = x

    @property
    def assessment_log(self):
        """A log of all assessment-related actions taken.
        """
        return self._assessment_log

    @assessment_log.setter
    def assessment_log(self, x):
        self._assessment_log = x

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
    def prop(self):
        return self._oscal_property

    @prop.setter
    def prop(self, x):
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
    def attestation(self):
        """A set of textual statements, typically written by the assessor.
        """
        return self._attestation

    @attestation.setter
    def attestation(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._attestation):
            self._attestation = []
        if bool(x):
            if x != self._attestation:
                self._attestation += list(x)

    @property
    def attestations(self):
        return self._attestation

    @attestations.setter
    def attestations(self, x):
        self.attestation(x)

    @property
    def observation(self):
        return self._observation

    @observation.setter
    def observation(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._observation):
            self._observation = []
        if bool(x):
            if x != self._observation:
                self._observation += list(x)

    @property
    def observations(self):
        return self._observation

    @observations.setter
    def observations(self, x):
        self.observation(x)

    @property
    def risk(self):
        return self._risk

    @risk.setter
    def risk(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._risk):
            self._risk = []
        if bool(x):
            if x != self._risk:
                self._risk += list(x)

    @property
    def risks(self):
        return self._risk

    @risks.setter
    def risks(self, x):
        self.risk(x)

    @property
    def finding(self):
        return self._finding

    @finding.setter
    def finding(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._finding):
            self._finding = []
        if bool(x):
            if x != self._finding:
                self._finding += list(x)

    @property
    def findings(self):
        return self._finding

    @findings.setter
    def findings(self, x):
        self.finding(x)


class Result(Result):
    def __init__(self, **kw):
        super(Result, self).__init__(**kw)
        self.use_name = 'result'
