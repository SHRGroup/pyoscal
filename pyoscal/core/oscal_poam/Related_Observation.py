class Related_Observation:
    """Related Observation

    Relates the poam-item to a set of referenced observations that were
used to determine the finding.

    Attributes:
        observation_uuid (uuid):References an observation defined in
the list of observations.

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-poam",
        "oscal-metadata",
        "oscal-implementation-common",
        "oscal-assessment-common",
    ]
    parameters = [
        "observation_uuid",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        observation_uuid,
        use_name='related-observation',
        prose=None,
    ):
        self._observation_uuid = None
        self.observation_uuid = \
            observation_uuid
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            observation_uuid=obj.get(
                'observation_uuid',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def observation_uuid(self):
        """References an observation defined in the list of observations.
        """
        return self._observation_uuid

    @observation_uuid.setter
    def observation_uuid(self, x):
        self._observation_uuid = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x
