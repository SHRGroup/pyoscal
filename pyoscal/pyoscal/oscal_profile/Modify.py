class Modify:
    """Modify controls

    Set parameters or amend controls in resolution

    Attributes:
        prose (str):Default value holder for raw data in texts

        set_parameter (BY_KEY):

        alter (ARRAY):

    """

    contexts = [
        "oscal-profile",
        "oscal-metadata",
        "oscal-catalog-common",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "set_parameter",
        "alter",
    ]

    def __init__(
        self,
        use_name='modify',
        prose=None,
        set_parameter=None,
        alter=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._set_parameter = None
        self.set_parameter = \
            set_parameter
        self._alter = None
        self.alter = \
            alter
        self.use_name = use_name
        if set_parameter is None:
            self.set_parameter = []
        if alter is None:
            self.alter = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
            set_parameter=obj.get(
                'set_parameter',
                None),
            alter=obj.get(
                'alter',
                None),
        )
        newcls.set_parameter = \
            obj.get('set_parameters')
        newcls.alter = \
            obj.get('alters')
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
    def set_parameter(self):
        return self._set_parameter

    @set_parameter.setter
    def set_parameter(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._set_parameter):
            self._set_parameter = []
        if bool(x):
            if x != self._set_parameter:
                self._set_parameter += list(x)

    @property
    def set_parameters(self):
        return self._set_parameter

    @set_parameters.setter
    def set_parameters(self, x):
        self.set_parameter(x)

    @property
    def alter(self):
        return self._alter

    @alter.setter
    def alter(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._alter):
            self._alter = []
        if bool(x):
            if x != self._alter:
                self._alter += list(x)

    @property
    def alters(self):
        return self._alter

    @alters.setter
    def alters(self, x):
        self.alter(x)
