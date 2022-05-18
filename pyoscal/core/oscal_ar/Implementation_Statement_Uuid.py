class Implementation_Statement_Uuid:
    """Implementation Statement UUID

    Identifies the implementation statement in the SSP to which this
finding is related.

    Attributes:
        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-ar",
        "oscal-metadata",
        "oscal-assessment-common",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        use_name='implementation-statement-uuid',
        prose=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x
