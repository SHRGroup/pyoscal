class Select_Objective_By_Id:
    """Select Objective

    Used to select a control objective for inclusion/exclusion based on
the control objective's identifier.

    Attributes:
        objective_id (str):

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "objective_id",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        objective_id,
        use_name='select-objective-by-id',
        prose=None,
    ):
        self._objective_id = None
        self.objective_id = \
            objective_id
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            objective_id=obj.get(
                'objective_id',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def objective_id(self):
        return self._objective_id

    @objective_id.setter
    def objective_id(self, x):
        self._objective_id = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x


class Exclude_Objective(Select_Objective_By_Id):
    def __init__(self, **kw):
        super(Exclude_Objective, self).__init__(**kw)
        self.use_name = 'exclude_objective'


class Include_Objective(Select_Objective_By_Id):
    def __init__(self, **kw):
        super(Include_Objective, self).__init__(**kw)
        self.use_name = 'include_objective'
