class At_Frequency:
    """Frequency Condition

    The task is intended to occur at the specified frequency.

    Attributes:
        period (positiveInteger):The task must occur after the
specified period has elapsed.

        unit (string):The unit of time for the period.

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "period",
        "unit",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        period,
        unit,
        use_name='at-frequency',
        prose=None,
    ):
        self._period = None
        self.period = \
            period
        self._unit = None
        self.unit = \
            unit
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            period=obj.get(
                'period',
                None),
            unit=obj.get(
                'unit',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def period(self):
        """The task must occur after the specified period has elapsed.
        """
        return self._period

    @period.setter
    def period(self, x):
        self._period = x

    @property
    def unit(self):
        """The unit of time for the period.
        """
        return self._unit

    @unit.setter
    def unit(self, x):
        self._unit = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x
