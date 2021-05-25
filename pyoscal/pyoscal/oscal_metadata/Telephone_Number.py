class Telephone_Number:
    """Telephone Number

    Contact number by telephone.

    Attributes:
        type (str):Indicates the type of phone number.

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-metadata",
    ]
    parameters = [
        "type",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        use_name='telephone-number',
        type=None,
        prose=None,
    ):
        self._type = None
        self.type = \
            type
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            type=obj.get(
                'type',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def type(self):
        """Indicates the type of phone number.
        """
        return self._type

    @type.setter
    def type(self, x):
        self._type = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x
