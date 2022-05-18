class Select_Control_By_Id:
    """Select Control

    Used to select a control for inclusion/exclusion based on one or more
control identifiers. A set of statement identifiers can be used to
target the inclusion/exclusion to only specific control statements
providing more granularity over the specific statements that are
within the asessment scope.

    Attributes:
        control_id (str):

        prose (str):Default value holder for raw data in texts

        statement_id (ARRAY):Used to constrain the selection to only
specificity identified statements.

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "control_id",
    ]
    subcomponents = [
        "prose",
        "statement_id",
    ]

    def __init__(
        self,
        control_id,
        use_name='select-control-by-id',
        prose=None,
        statement_id=None,
    ):
        self._control_id = None
        self.control_id = \
            control_id
        self._prose = None
        self.prose = \
            prose
        self._statement_id = None
        self.statement_id = \
            statement_id
        self.use_name = use_name
        if statement_id is None:
            self.statement_id = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            control_id=obj.get(
                'control_id',
                None),
            prose=obj.get(
                'prose',
                None),
            statement_id=obj.get(
                'statement_id',
                None),
        )
        newcls.statement_id = \
            obj.get('statement_ids')
        return newcls

    @property
    def control_id(self):
        return self._control_id

    @control_id.setter
    def control_id(self, x):
        self._control_id = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def statement_id(self):
        """Used to constrain the selection to only specificity identified
        statements.
        """
        return self._statement_id

    @statement_id.setter
    def statement_id(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._statement_id):
            self._statement_id = []
        if bool(x):
            if x != self._statement_id:
                self._statement_id += list(x)

    @property
    def statement_ids(self):
        return self._statement_id

    @statement_ids.setter
    def statement_ids(self, x):
        self.statement_id(x)


class Exclude_Control(Select_Control_By_Id):
    def __init__(self, **kw):
        super(Exclude_Control, self).__init__(**kw)
        self.use_name = 'exclude_control'


class Include_Control(Select_Control_By_Id):
    def __init__(self, **kw):
        super(Include_Control, self).__init__(**kw)
        self.use_name = 'include_control'


class Include_Controls(Select_Control_By_Id):
    def __init__(self, **kw):
        super(Include_Controls, self).__init__(**kw)
        self.use_name = 'include_controls'


class Exclude_Controls(Select_Control_By_Id):
    def __init__(self, **kw):
        super(Exclude_Controls, self).__init__(**kw)
        self.use_name = 'exclude_controls'
