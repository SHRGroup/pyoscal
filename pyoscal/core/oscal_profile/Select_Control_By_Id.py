class Select_Control_By_Id:
    """Call

    Call a control by its ID

    Attributes:
        with_child_controls (str):

        prose (str):Default value holder for raw data in texts

        with_id (ARRAY):None

        matching (ARRAY):Select controls by (regular expression)
match on ID

    """

    contexts = [
        "oscal-profile",
        "oscal-metadata",
        "oscal-catalog-common",
    ]
    parameters = [
        "with_child_controls",
    ]
    subcomponents = [
        "prose",
        "with_id",
        "matching",
    ]

    def __init__(
        self,
        use_name='select-control-by-id',
        with_child_controls=None,
        prose=None,
        with_id=None,
        matching=None,
    ):
        self._with_child_controls = None
        self.with_child_controls = \
            with_child_controls
        self._prose = None
        self.prose = \
            prose
        self._with_id = None
        self.with_id = \
            with_id
        self._matching = None
        self.matching = \
            matching
        self.use_name = use_name
        if with_id is None:
            self.with_id = []
        if matching is None:
            self.matching = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            with_child_controls=obj.get(
                'with_child_controls',
                None),
            prose=obj.get(
                'prose',
                None),
            with_id=obj.get(
                'with_id',
                None),
            matching=obj.get(
                'matching',
                None),
        )
        newcls.with_id = \
            obj.get('with_ids')
        newcls.matching = \
            obj.get('matching')
        return newcls

    @property
    def with_child_controls(self):
        return self._with_child_controls

    @with_child_controls.setter
    def with_child_controls(self, x):
        self._with_child_controls = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def with_id(self):
        return self._with_id

    @with_id.setter
    def with_id(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._with_id):
            self._with_id = []
        if bool(x):
            if x != self._with_id:
                self._with_id += list(x)

    @property
    def with_ids(self):
        return self._with_id

    @with_ids.setter
    def with_ids(self, x):
        self.with_id(x)

    @property
    def matching(self):
        """Select controls by (regular expression) match on ID
        """
        return self._matching

    @matching.setter
    def matching(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._matching):
            self._matching = []
        if bool(x):
            if x != self._matching:
                self._matching += list(x)


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
