class Document_Id:
    """Document Identifier

    A document identifier qualified by an identifier

    Attributes:
        scheme (uri):Qualifies the kind of document identifier using
a URI. If the scheme is not provided the value of the
element will be interpreted as a string of characters.

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
        use_name='document-id',
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
        """Qualifies the kind of document identifier using a URI. If the scheme
        is not provided the value of the element will be interpreted as a
        string of characters.
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
