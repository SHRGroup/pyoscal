class Categorization:
    """Information Type Categorization

    A set of information type identifiers qualified by the given
identification

    Attributes:
        system (uri):Specifies the information type identification
system used.

        prose (str):Default value holder for raw data in texts

        information_type_id (ARRAY):An identifier qualified by the
given identification

    """

    contexts = [
        "oscal-ssp",
        "oscal-metadata",
        "oscal-implementation-common",
    ]
    parameters = [
        "system",
    ]
    subcomponents = [
        "prose",
        "information_type_id",
    ]

    def __init__(
        self,
        system,
        use_name='categorization',
        prose=None,
        information_type_id=None,
    ):
        self._system = None
        self.system = \
            system
        self._prose = None
        self.prose = \
            prose
        self._information_type_id = None
        self.information_type_id = \
            information_type_id
        self.use_name = use_name
        if information_type_id is None:
            self.information_type_id = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            system=obj.get(
                'system',
                None),
            prose=obj.get(
                'prose',
                None),
            information_type_id=obj.get(
                'information_type_id',
                None),
        )
        newcls.information_type_id = \
            obj.get('information_type_ids')
        return newcls

    @property
    def system(self):
        """Specifies the information type identification system used.
        """
        return self._system

    @system.setter
    def system(self, x):
        self._system = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def information_type_id(self):
        """An identifier qualified by the given identification
        """
        return self._information_type_id

    @information_type_id.setter
    def information_type_id(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._information_type_id):
            self._information_type_id = []
        if bool(x):
            if x != self._information_type_id:
                self._information_type_id += list(x)

    @property
    def information_type_ids(self):
        return self._information_type_id

    @information_type_ids.setter
    def information_type_ids(self, x):
        self.information_type_id(x)
