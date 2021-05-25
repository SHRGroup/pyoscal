class Reviewed_Controls:
    """Reviewed Controls and Control Objectives

    Identifies the controls being assessed and their control objectives.

    Attributes:
        prose (str):Default value holder for raw data in texts

        description (markup-multiline):A human-readable description
of control objectives.

        oscal_property (ARRAY):

        link (ARRAY):

        control_selection (ARRAY):Identifies the controls being
assessed. In the assessment plan, these are the planned
controls. In the assessment results, these are the actual
controls, and reflects any changes from the plan.

        control_objective_selection (ARRAY):Identifies the control
objectives of the assessment. In the assessment plan, these
are the planned objectives. In the assessment results, these
are the assessed objectives, and reflects any changes from
the plan.

        remarks (str):

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
        "control_selection",
        "control_objective_selection",
        "remarks",
    ]

    def __init__(
        self,
        control_selection,
        use_name='reviewed-controls',
        prose=None,
        description=None,
        oscal_property=None,
        link=None,
        control_objective_selection=None,
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
        self._control_selection = None
        self.control_selection = \
            control_selection
        self._control_objective_selection = None
        self.control_objective_selection = \
            control_objective_selection
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if control_selection is None:
            self.control_selection = []
        if control_objective_selection is None:
            self.control_objective_selection = []

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
            control_selection=obj.get(
                'control_selection',
                None),
            control_objective_selection=obj.get(
                'control_objective_selection',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.control_selection = \
            obj.get('control_selections')
        newcls.control_objective_selection = \
            obj.get('control_objective_selections')
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
        """A human-readable description of control objectives.
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
    def control_selection(self):
        """Identifies the controls being assessed. In the assessment plan,
        these are the planned controls. In the assessment results, these are
        the actual controls, and reflects any changes from the plan.
        """
        return self._control_selection

    @control_selection.setter
    def control_selection(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._control_selection):
            self._control_selection = []
        if bool(x):
            if x != self._control_selection:
                self._control_selection += list(x)

    @property
    def control_selections(self):
        return self._control_selection

    @control_selections.setter
    def control_selections(self, x):
        self.control_selection(x)

    @property
    def control_objective_selection(self):
        """Identifies the control objectives of the assessment. In the
        assessment plan, these are the planned objectives. In the assessment
        results, these are the assessed objectives, and reflects any changes
        from the plan.
        """
        return self._control_objective_selection

    @control_objective_selection.setter
    def control_objective_selection(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._control_objective_selection):
            self._control_objective_selection = []
        if bool(x):
            if x != self._control_objective_selection:
                self._control_objective_selection += list(x)

    @property
    def control_objective_selections(self):
        return self._control_objective_selection

    @control_objective_selections.setter
    def control_objective_selections(self, x):
        self.control_objective_selection(x)


class Related_Controls(Reviewed_Controls):
    def __init__(self, **kw):
        super(Related_Controls, self).__init__(**kw)
        self.use_name = 'related_controls'
