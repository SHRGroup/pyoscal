class Test:
    """Constraint Test

    A test expression which is expected to be evaluated by a tool.

    Attributes:
        prose (str):Default value holder for raw data in texts

        expression (string):A formal (executable) expression of a
constraint

        remarks (str):

    """

    contexts = [
        "oscal-catalog-common",
        "oscal-metadata",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "expression",
        "remarks",
    ]

    def __init__(
        self,
        expression,
        use_name='test',
        prose=None,
        remarks=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._expression = None
        self.expression = \
            expression
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
            expression=obj.get(
                'expression',
                None),
            remarks=obj.get(
                'remarks',
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

    @property
    def expression(self):
        """A formal (executable) expression of a constraint
        """
        return self._expression

    @expression.setter
    def expression(self, x):
        self._expression = x

    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, x):
        self._remarks = x
