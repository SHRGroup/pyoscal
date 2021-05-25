class Parameter_Value:
    """Parameter Value

    A parameter value or set of values.

    Attributes:
        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-implementation-common",
        "oscal-metadata",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        use_name='parameter-value',
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


class Value(Parameter_Value):
    def __init__(self, **kw):
        super(Value, self).__init__(**kw)
        self.use_name = 'value'
