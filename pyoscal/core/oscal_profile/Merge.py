class Merge:
    """Merge controls

    A Merge element merges controls in resolution.

    Attributes:
        prose (str):Default value holder for raw data in texts

        combine (str):

        as_is (str):

        custom (str):

    """

    contexts = [
        "oscal-profile",
        "oscal-metadata",
        "oscal-catalog-common",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "combine",
        "as_is",
        "custom",
    ]

    def __init__(
        self,
        use_name='merge',
        prose=None,
        combine=None,
        as_is=None,
        custom=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._combine = None
        self.combine = \
            combine
        self._as_is = None
        self.as_is = \
            as_is
        self._custom = None
        self.custom = \
            custom
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
            combine=obj.get(
                'combine',
                None),
            as_is=obj.get(
                'as_is',
                None),
            custom=obj.get(
                'custom',
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
    def combine(self):
        return self._combine

    @combine.setter
    def combine(self, x):
        self._combine = x

    @property
    def as_is(self):
        return self._as_is

    @as_is.setter
    def as_is(self, x):
        self._as_is = x

    @property
    def custom(self):
        return self._custom

    @custom.setter
    def custom(self, x):
        self._custom = x
