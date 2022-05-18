class Associated_Risk:
    """Associated Risk

    Relates the finding to a set of referenced risks that were used to
determine the finding.

    Attributes:
        risk_uuid (uuid):References an risk defined in the list of
risks.

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-ar",
        "oscal-metadata",
        "oscal-assessment-common",
    ]
    parameters = [
        "risk_uuid",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        risk_uuid,
        use_name='associated-risk',
        prose=None,
    ):
        self._risk_uuid = None
        self.risk_uuid = \
            risk_uuid
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            risk_uuid=obj.get(
                'risk_uuid',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def risk_uuid(self):
        """References an risk defined in the list of risks.
        """
        return self._risk_uuid

    @risk_uuid.setter
    def risk_uuid(self, x):
        self._risk_uuid = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x
