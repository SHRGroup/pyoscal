class Control_Selection:
    """Assessed Controls

    Identifies the controls being assessed. In the assessment plan, these
are the planned controls. In the assessment results, these are the
actual controls, and reflects any changes from the plan.

    Attributes:
        prose (str):Default value holder for raw data in texts

        description (markup-multiline):A human-readable description
of in-scope controls specified for assessment.

        oscal_property (ARRAY):

        link (ARRAY):

        exclude_control (ARRAY):

        remarks (str):

        include_all (str):A key word to indicate all.

        include_control (ARRAY):

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
        "exclude_control",
        "remarks",
        "include_all",
        "include_control",
    ]

    def __init__(
        self,
        include_all,
        include_control,
        use_name='control-selection',
        prose=None,
        description=None,
        oscal_property=None,
        link=None,
        exclude_control=None,
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
        self._exclude_control = None
        self.exclude_control = \
            exclude_control
        self._remarks = None
        self.remarks = \
            remarks
        self._include_all = None
        self.include_all = \
            include_all
        self._include_control = None
        self.include_control = \
            include_control
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if exclude_control is None:
            self.exclude_control = []
        if include_control is None:
            self.include_control = []

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
            exclude_control=obj.get(
                'exclude_control',
                None),
            remarks=obj.get(
                'remarks',
                None),
            include_all=obj.get(
                'include_all',
                None),
            include_control=obj.get(
                'include_control',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.exclude_control = \
            obj.get('exclude_controls')
        newcls.include_control = \
            obj.get('include_controls')
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
        """A human-readable description of in-scope controls specified for
        assessment.
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
    def exclude_control(self):
        return self._exclude_control

    @exclude_control.setter
    def exclude_control(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._exclude_control):
            self._exclude_control = []
        if bool(x):
            if x != self._exclude_control:
                self._exclude_control += list(x)

    @property
    def exclude_controls(self):
        return self._exclude_control

    @exclude_controls.setter
    def exclude_controls(self, x):
        self.exclude_control(x)

    @property
    def include_control(self):
        return self._include_control

    @include_control.setter
    def include_control(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._include_control):
            self._include_control = []
        if bool(x):
            if x != self._include_control:
                self._include_control += list(x)

    @property
    def include_controls(self):
        return self._include_control

    @include_controls.setter
    def include_controls(self, x):
        self.include_control(x)
