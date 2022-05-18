class Uuid:
    """Assessment Plan Universally Unique Identifier

    Uniquely identifies this assessment plan. This UUID must be changed
each time the content of the plan changes.

    Attributes:
        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-ap",
        "oscal-metadata",
        "oscal-assessment-common",
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
