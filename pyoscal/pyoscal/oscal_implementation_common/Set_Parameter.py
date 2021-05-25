class Set_Parameter:
    """Set Parameter Value

    Identifies the parameter that will be set by the enclosed value.

    Attributes:
        param_id (str):

        prose (str):Default value holder for raw data in texts

        value (ARRAY):A parameter value or set of values.

        remarks (str):

    """

    contexts = [
        "oscal-implementation-common",
        "oscal-metadata",
    ]
    parameters = [
        "param_id",
    ]
    subcomponents = [
        "prose",
        "value",
        "remarks",
    ]

    def __init__(
        self,
        param_id,
        value,
        use_name='set-parameter',
        prose=None,
        remarks=None,
    ):
        self._param_id = None
        self.param_id = \
            param_id
        self._prose = None
        self.prose = \
            prose
        self._value = None
        self.value = \
            value
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if value is None:
            self.value = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            param_id=obj.get(
                'param_id',
                None),
            prose=obj.get(
                'prose',
                None),
            value=obj.get(
                'value',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.value = \
            obj.get('values')
        return newcls

    @property
    def param_id(self):
        return self._param_id

    @param_id.setter
    def param_id(self, x):
        self._param_id = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, x):
        self._remarks = x

    @property
    def value(self):
        """A parameter value or set of values.
        """
        return self._value

    @value.setter
    def value(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._value):
            self._value = []
        if bool(x):
            if x != self._value:
                self._value += list(x)

    @property
    def values(self):
        return self._value

    @values.setter
    def values(self, x):
        self.value(x)
