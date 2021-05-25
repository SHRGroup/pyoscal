class Parameter_Selection:
    """Selection

    Presenting a choice among alternatives

    Attributes:
        how_many (string):Describes the number of selections that
must occur.

        prose (str):Default value holder for raw data in texts

        choice (ARRAY):A value selection among several such options

    """

    contexts = [
        "oscal-catalog-common",
        "oscal-metadata",
    ]
    parameters = [
        "how_many",
    ]
    subcomponents = [
        "prose",
        "choice",
    ]

    def __init__(
        self,
        use_name='parameter-selection',
        how_many=None,
        prose=None,
        choice=None,
    ):
        self._how_many = None
        self.how_many = \
            how_many
        self._prose = None
        self.prose = \
            prose
        self._choice = None
        self.choice = \
            choice
        self.use_name = use_name
        if choice is None:
            self.choice = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            how_many=obj.get(
                'how_many',
                None),
            prose=obj.get(
                'prose',
                None),
            choice=obj.get(
                'choice',
                None),
        )
        newcls.choice = \
            obj.get('choice')
        return newcls

    @property
    def how_many(self):
        """Describes the number of selections that must occur.
        """
        return self._how_many

    @how_many.setter
    def how_many(self, x):
        self._how_many = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def choice(self):
        """A value selection among several such options
        """
        return self._choice

    @choice.setter
    def choice(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._choice):
            self._choice = []
        if bool(x):
            if x != self._choice:
                self._choice += list(x)


class Select(Parameter_Selection):
    def __init__(self, **kw):
        super(Select, self).__init__(**kw)
        self.use_name = 'select'
