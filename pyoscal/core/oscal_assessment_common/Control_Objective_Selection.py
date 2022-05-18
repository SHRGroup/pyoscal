class Control_Objective_Selection:
    """Referenced Control Objectives

    Identifies the control objectives of the assessment. In the assessment
plan, these are the planned objectives. In the assessment results,
these are the assessed objectives, and reflects any changes from the
plan.

    Attributes:
        prose (str):Default value holder for raw data in texts

        description (markup-multiline):A human-readable description
of this collection of control objectives.

        oscal_property (ARRAY):

        link (ARRAY):

        exclude_objective (ARRAY):

        remarks (str):

        include_all (str):A key word to indicate all.

        include_objective (ARRAY):

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "description",
        "oscal_property",
        "link",
        "exclude_objective",
        "remarks",
        "include_all",
        "include_objective",
    ]

    def __init__(
        self,
        include_all,
        include_objective,
        use_name='control-objective-selection',
        prose=None,
        description=None,
        oscal_property=None,
        link=None,
        exclude_objective=None,
        remarks=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._description = None
        self.description = \
            description
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._exclude_objective = None
        self.exclude_objective = \
            exclude_objective
        self._remarks = None
        self.remarks = \
            remarks
        self._include_all = None
        self.include_all = \
            include_all
        self._include_objective = None
        self.include_objective = \
            include_objective
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if exclude_objective is None:
            self.exclude_objective = []
        if include_objective is None:
            self.include_objective = []

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
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            exclude_objective=obj.get(
                'exclude_objective',
                None),
            remarks=obj.get(
                'remarks',
                None),
            include_all=obj.get(
                'include_all',
                None),
            include_objective=obj.get(
                'include_objective',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.exclude_objective = \
            obj.get('exclude_objectives')
        newcls.include_objective = \
            obj.get('include_objectives')
        newcls.oscal_property = \
            obj.get('prop')
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
        """A human-readable description of this collection of control
        objectives.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, x):
        self._remarks = x

    @property
    def include_all(self):
        """A key word to indicate all.
        """
        return self._include_all

    @include_all.setter
    def include_all(self, x):
        self._include_all = x

    @property
    def oscal_property(self):
        return self._oscal_property

    @oscal_property.setter
    def oscal_property(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._oscal_property):
            self._oscal_property = []
        if bool(x):
            if x != self._oscal_property:
                self._oscal_property += list(x)

    @property
    def props(self):
        return self._oscal_property

    @props.setter
    def props(self, x):
        self.oscal_property(x)

    @property
    def prop(self):
        return self._oscal_property

    @prop.setter
    def prop(self, x):
        self.oscal_property(x)

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._link):
            self._link = []
        if bool(x):
            if x != self._link:
                self._link += list(x)

    @property
    def links(self):
        return self._link

    @links.setter
    def links(self, x):
        self.link(x)

    @property
    def exclude_objective(self):
        return self._exclude_objective

    @exclude_objective.setter
    def exclude_objective(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._exclude_objective):
            self._exclude_objective = []
        if bool(x):
            if x != self._exclude_objective:
                self._exclude_objective += list(x)

    @property
    def exclude_objectives(self):
        return self._exclude_objective

    @exclude_objectives.setter
    def exclude_objectives(self, x):
        self.exclude_objective(x)

    @property
    def include_objective(self):
        return self._include_objective

    @include_objective.setter
    def include_objective(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._include_objective):
            self._include_objective = []
        if bool(x):
            if x != self._include_objective:
                self._include_objective += list(x)

    @property
    def include_objectives(self):
        return self._include_objective

    @include_objectives.setter
    def include_objectives(self, x):
        self.include_objective(x)
