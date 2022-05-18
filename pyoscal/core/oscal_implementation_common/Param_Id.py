class Param_Id:
    """Parameter ID

    A reference to a parameter within a control, who's catalog has been
imported into the current implementation context.

    Attributes:
        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-implementation-common",
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
        use_name='param-id',
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
