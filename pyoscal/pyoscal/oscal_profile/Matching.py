class Matching:
    """Match Controls by Pattern

    Select controls by (regular expression) match on ID

    Attributes:
        pattern (str):

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-profile",
        "oscal-metadata",
        "oscal-catalog-common",
    ]
    parameters = [
        "pattern",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        use_name='matching',
        pattern=None,
        prose=None,
    ):
        self._pattern = None
        self.pattern = \
            pattern
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            pattern=obj.get(
                'pattern',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def pattern(self):
        return self._pattern

    @pattern.setter
    def pattern(self, x):
        self._pattern = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x
