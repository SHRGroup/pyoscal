class Oscal_Class:
    """Control Class

    A textual label that provides a sub-type or characterization of the
control.

    Attributes:
        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-catalog",
        "oscal-catalog-common",
        "oscal-metadata",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        use_name='class',
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
