class Combine:
    """Combination rule

    A Combine element defines whether and how to combine multiple
(competing) versions of the same control

    Attributes:
        method (str):

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-profile",
        "oscal-metadata",
        "oscal-catalog-common",
    ]
    parameters = [
        "method",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        use_name='combine',
        method=None,
        prose=None,
    ):
        self._method = None
        self.method = \
            method
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            method=obj.get(
                'method',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, x):
        self._method = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x
