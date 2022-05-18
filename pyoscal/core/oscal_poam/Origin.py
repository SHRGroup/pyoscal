class Origin:
    """Origin

    Identifies the source of the finding, such as a tool or person.

    Attributes:
        prose (str):Default value holder for raw data in texts

        actor (ARRAY):

    """

    contexts = [
        "oscal-poam",
        "oscal-metadata",
        "oscal-implementation-common",
        "oscal-assessment-common",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "actor",
    ]

    def __init__(
        self,
        actor,
        use_name='origin',
        prose=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._actor = None
        self.actor = \
            actor
        self.use_name = use_name
        if actor is None:
            self.actor = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
            actor=obj.get(
                'actor',
                None),
        )
        newcls.actor = \
            obj.get('actors')
        return newcls

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def actor(self):
        return self._actor

    @actor.setter
    def actor(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._actor):
            self._actor = []
        if bool(x):
            if x != self._actor:
                self._actor += list(x)

    @property
    def actors(self):
        return self._actor

    @actors.setter
    def actors(self, x):
        self.actor(x)
