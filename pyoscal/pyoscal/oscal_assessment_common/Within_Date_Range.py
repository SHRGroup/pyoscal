class Within_Date_Range:
    """On Date Range Condition

    The task is intended to occur within the specified date range.

    Attributes:
        start (dateTime-with-timezone):The task must occur on or
after the specified date.

        end (dateTime-with-timezone):The task must occur on or
before the specified date.

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "start",
        "end",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        start,
        end,
        use_name='within-date-range',
        prose=None,
    ):
        self._start = None
        self.start = \
            start
        self._end = None
        self.end = \
            end
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            start=obj.get(
                'start',
                None),
            end=obj.get(
                'end',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def start(self):
        """The task must occur on or after the specified date.
        """
        return self._start

    @start.setter
    def start(self, x):
        self._start = x

    @property
    def end(self):
        """The task must occur on or before the specified date.
        """
        return self._end

    @end.setter
    def end(self, x):
        self._end = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x
