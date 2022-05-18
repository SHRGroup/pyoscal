class Local_Objective:
    """Assessment-Specific Control Objective

    A local definition of a control objective for this assessment. Uses
catalog syntax for control objective and assessment actions.

    Attributes:
        control_id (str):

        prose (str):Default value holder for raw data in texts

        description (markup-multiline):A human-readable description
of this control objective.

        oscal_property (ARRAY):

        link (ARRAY):

        part (ARRAY):

        remarks (str):

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
        "description",
        "oscal_property",
        "link",
        "part",
        "remarks",
    ]

    def __init__(
        self,
        control_id,
        part,
        use_name='local-objective',
        prose=None,
        description=None,
        oscal_property=None,
        link=None,
        remarks=None,
    ):
        self._control_id = None
        self.control_id = \
            control_id
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
        self._part = None
        self.part = \
            part
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if part is None:
            self.part = []

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
            description=obj.get(
                'description',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            part=obj.get(
                'part',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.part = \
            obj.get('parts')
        newcls.oscal_property = \
            obj.get('prop')
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
    def description(self):
        """A human-readable description of this control objective.
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
    def part(self):
        return self._part

    @part.setter
    def part(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._part):
            self._part = []
        if bool(x):
            if x != self._part:
                self._part += list(x)

    @property
    def parts(self):
        return self._part

    @parts.setter
    def parts(self, x):
        self.part(x)


class Objectives_And_Methods(Local_Objective):
    def __init__(self, **kw):
        super(Objectives_And_Methods, self).__init__(**kw)
        self.use_name = 'objectives_and_methods'
