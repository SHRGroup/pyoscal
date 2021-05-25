class Control_Implementation:
    """Control Implementation

    Describes how the system satisfies a set of controls.

    Attributes:
        prose (str):Default value holder for raw data in texts

        description (markup-multiline):A statement describing
important things to know about how this set of control
satisfaction documentation is approached.

        set_parameter (BY_KEY):

        implemented_requirement (ARRAY):

    """

    contexts = [
        "oscal-ssp",
        "oscal-metadata",
        "oscal-implementation-common",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "description",
        "set_parameter",
        "implemented_requirement",
    ]

    def __init__(
        self,
        description,
        implemented_requirement,
        use_name='control-implementation',
        prose=None,
        set_parameter=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._description = None
        self.description = \
            description
        self._set_parameter = None
        self.set_parameter = \
            set_parameter
        self._implemented_requirement = None
        self.implemented_requirement = \
            implemented_requirement
        self.use_name = use_name
        if set_parameter is None:
            self.set_parameter = []
        if implemented_requirement is None:
            self.implemented_requirement = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
            description=obj.get(
                'description',
                None),
            set_parameter=obj.get(
                'set_parameter',
                None),
            implemented_requirement=obj.get(
                'implemented_requirement',
                None),
        )
        newcls.set_parameter = \
            obj.get('set_parameters')
        newcls.implemented_requirement = \
            obj.get('implemented_requirements')
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
    def description(self):
        """A statement describing important things to know about how this set
        of control satisfaction documentation is approached.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

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
    def implemented_requirement(self):
        return self._implemented_requirement

    @implemented_requirement.setter
    def implemented_requirement(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._implemented_requirement):
            self._implemented_requirement = []
        if bool(x):
            if x != self._implemented_requirement:
                self._implemented_requirement += list(x)

    @property
    def implemented_requirements(self):
        return self._implemented_requirement

    @implemented_requirements.setter
    def implemented_requirements(self, x):
        self.implemented_requirement(x)
