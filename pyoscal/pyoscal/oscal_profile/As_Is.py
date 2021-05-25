class As_Is:
    """As is

    An As-is element indicates that the controls should be structured in
resolution as they are structured in their source catalogs. It does
not contain any elements or attributes.

    Attributes:
        prose (str):Default value holder for raw data in texts

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
    ]

    def __init__(
        self,
        use_name='as-is',
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
