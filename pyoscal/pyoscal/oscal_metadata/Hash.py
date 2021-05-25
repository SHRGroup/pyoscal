class Hash:
    """Hash

    A representation of a cryptographic digest generated over a resource
using a specified hash algorithm.

    Attributes:
        algorithm (string):Method by which a hash is derived

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-metadata",
    ]
    parameters = [
        "algorithm",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        algorithm,
        use_name='hash',
        prose=None,
    ):
        self._algorithm = None
        self.algorithm = \
            algorithm
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            algorithm=obj.get(
                'algorithm',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def algorithm(self):
        """Method by which a hash is derived
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, x):
        self._algorithm = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x
