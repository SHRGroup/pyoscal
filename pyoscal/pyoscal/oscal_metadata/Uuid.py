class Uuid:
    """Property Universally Unique Identifier

    A unique identifier that can be used to reference this property
elsewhere in an OSCAL document. A UUID should be consistently used for
a given location across revisions of the document.

    Attributes:
        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-metadata",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        use_name='uuid',
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
