class System_Id:
    """System Identification

    A unique identifier for the system described by this system security
plan.

    Attributes:
        identifier_type (uri):Identifies the identification system
from which the provided identifier was assigned.

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-implementation-common",
        "oscal-metadata",
    ]
    parameters = [
        "identifier_type",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        use_name='system-id',
        identifier_type=None,
        prose=None,
    ):
        self._identifier_type = None
        self.identifier_type = \
            identifier_type
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            identifier_type=obj.get(
                'identifier_type',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def identifier_type(self):
        """Identifies the identification system from which the provided
        identifier was assigned.
        """
        return self._identifier_type

    @identifier_type.setter
    def identifier_type(self, x):
        self._identifier_type = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x
