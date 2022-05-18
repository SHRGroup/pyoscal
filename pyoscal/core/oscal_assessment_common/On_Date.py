class On_Date:
    """On Date Condition

    The task is intended to occur on the specified date.

    Attributes:
        date (dateTime-with-timezone):The task must occur on the
specified date.

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "date",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        date,
        use_name='on-date',
        prose=None,
    ):
        self._date = None
        self.date = \
            date
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            date=obj.get(
                'date',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def date(self):
        """The task must occur on the specified date.
        """
        return self._date

    @date.setter
    def date(self, x):
        self._date = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x
