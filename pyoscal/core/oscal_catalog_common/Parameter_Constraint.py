class Parameter_Constraint:
    """Constraint

    A formal or informal expression of a constraint or test

    Attributes:
        prose (str):Default value holder for raw data in texts

        description (markup-multiline):A textual summary of the
constraint to be applied.

        test (ARRAY):A test expression which is expected to be
evaluated by a tool.

    """

    contexts = [
        "oscal-catalog-common",
        "oscal-metadata",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "description",
        "test",
    ]

    def __init__(
        self,
        use_name='parameter-constraint',
        prose=None,
        description=None,
        test=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._description = None
        self.description = \
            description
        self._test = None
        self.test = \
            test
        self.use_name = use_name
        if test is None:
            self.test = []

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
            test=obj.get(
                'test',
                None),
        )
        newcls.test = \
            obj.get('tests')
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
        """A textual summary of the constraint to be applied.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

    @property
    def test(self):
        """A test expression which is expected to be evaluated by a tool.
        """
        return self._test

    @test.setter
    def test(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._test):
            self._test = []
        if bool(x):
            if x != self._test:
                self._test += list(x)

    @property
    def tests(self):
        return self._test

    @tests.setter
    def tests(self, x):
        self.test(x)


class Constraint(Parameter_Constraint):
    def __init__(self, **kw):
        super(Constraint, self).__init__(**kw)
        self.use_name = 'constraint'
