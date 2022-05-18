class Status:
    """Status

    Describes the operational status of the system.

    Attributes:
        state (string):The current operating status.

        prose (str):Default value holder for raw data in texts

        remarks (str):

    """

    contexts = [
        "oscal-ssp",
        "oscal-metadata",
        "oscal-implementation-common",
    ]
    parameters = [
        "state",
    ]
    subcomponents = [
        "prose",
        "remarks",
    ]

    def __init__(
        self,
        state,
        use_name='status',
        prose=None,
        remarks=None,
    ):
        self._state = None
        self.state = \
            state
        self._prose = None
        self.prose = \
            prose
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            state=obj.get(
                'state',
                None),
            prose=obj.get(
                'prose',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        return newcls

    @property
    def state(self):
        """The current operating status.
        """
        return self._state

    @state.setter
    def state(self, x):
        self._state = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, x):
        self._remarks = x
