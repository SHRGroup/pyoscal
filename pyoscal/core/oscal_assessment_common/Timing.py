class Timing:
    """Event Timing

    The timing under which the task is intended to occur.

    Attributes:
        prose (str):Default value holder for raw data in texts

        on_date (str):The task is intended to occur on the specified
date.

        within_date_range (str):The task is intended to occur within
the specified date range.

        at_frequency (str):The task is intended to occur at the
specified frequency.

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "on_date",
        "within_date_range",
        "at_frequency",
    ]

    def __init__(
        self,
        on_date,
        within_date_range,
        at_frequency,
        use_name='timing',
        prose=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._on_date = None
        self.on_date = \
            on_date
        self._within_date_range = None
        self.within_date_range = \
            within_date_range
        self._at_frequency = None
        self.at_frequency = \
            at_frequency
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
            on_date=obj.get(
                'on_date',
                None),
            within_date_range=obj.get(
                'within_date_range',
                None),
            at_frequency=obj.get(
                'at_frequency',
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

    @property
    def on_date(self):
        """The task is intended to occur on the specified date.
        """
        return self._on_date

    @on_date.setter
    def on_date(self, x):
        self._on_date = x

    @property
    def within_date_range(self):
        """The task is intended to occur within the specified date range.
        """
        return self._within_date_range

    @within_date_range.setter
    def within_date_range(self, x):
        self._within_date_range = x

    @property
    def at_frequency(self):
        """The task is intended to occur at the specified frequency.
        """
        return self._at_frequency

    @at_frequency.setter
    def at_frequency(self, x):
        self._at_frequency = x
