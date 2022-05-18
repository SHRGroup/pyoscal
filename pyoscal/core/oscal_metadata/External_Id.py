class External_Id:
    """Party External Identifier

    An identifier for a person or organization using a designated scheme.
e.g. an Open Researcher and Contributor ID (ORCID)

    Attributes:
        scheme (uri):Indicates the type of external identifier.

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-metadata",
    ]
    parameters = [
        "scheme",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        scheme,
        use_name='external-id',
        prose=None,
    ):
        self._scheme = None
        self.scheme = \
            scheme
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            scheme=obj.get(
                'scheme',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def scheme(self):
        """Indicates the type of external identifier.
        """
        return self._scheme

    @scheme.setter
    def scheme(self, x):
        self._scheme = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x
