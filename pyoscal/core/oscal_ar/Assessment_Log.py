class Assessment_Log:
    """Assessment Log

    A log of all assessment-related actions taken.

    Attributes:
        prose (str):Default value holder for raw data in texts

        entry (ARRAY):Identifies the result of an action and/or task
that occurred as part of executing an assessment plan or an
assessment event that occurred in producing the assessment
results.

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
        "entry",
    ]

    def __init__(
        self,
        entry,
        use_name='assessment-log',
        prose=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._entry = None
        self.entry = \
            entry
        self.use_name = use_name
        if entry is None:
            self.entry = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
            entry=obj.get(
                'entry',
                None),
        )
        newcls.entry = \
            obj.get('entries')
        return newcls

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def entry(self):
        """Identifies the result of an action and/or task that occurred as part
        of executing an assessment plan or an assessment event that occurred
        in producing the assessment results.
        """
        return self._entry

    @entry.setter
    def entry(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._entry):
            self._entry = []
        if bool(x):
            if x != self._entry:
                self._entry += list(x)

    @property
    def entries(self):
        return self._entry

    @entries.setter
    def entries(self, x):
        self.entry(x)
