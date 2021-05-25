class Control_Implementation:
    """Control Implementation Set

    Defines how the component or capability supports a set of controls.

    Attributes:
        uuid (uuid):A unique identifier for the set of implemented
controls.

        source (str):

        prose (str):Default value holder for raw data in texts

        description (markup-multiline):A description of how the
specified set of controls are implemented for the containing
component or capability.

        oscal_property (ARRAY):

        link (ARRAY):

        set_parameter (BY_KEY):

        implemented_requirement (ARRAY):

    """

    contexts = [
        "oscal-component-definition",
        "oscal-implementation-common",
    ]
    parameters = [
        "uuid",
        "source",
    ]
    subcomponents = [
        "prose",
        "description",
        "oscal_property",
        "link",
        "set_parameter",
        "implemented_requirement",
    ]

    def __init__(
        self,
        uuid,
        source,
        description,
        implemented_requirement,
        use_name='control-implementation',
        prose=None,
        oscal_property=None,
        link=None,
        set_parameter=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._source = None
        self.source = \
            source
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
        self._set_parameter = None
        self.set_parameter = \
            set_parameter
        self._implemented_requirement = None
        self.implemented_requirement = \
            implemented_requirement
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if set_parameter is None:
            self.set_parameter = []
        if implemented_requirement is None:
            self.implemented_requirement = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            uuid=obj.get(
                'uuid',
                None),
            source=obj.get(
                'source',
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
            set_parameter=obj.get(
                'set_parameter',
                None),
            implemented_requirement=obj.get(
                'implemented_requirement',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.set_parameter = \
            obj.get('set_parameters')
        newcls.implemented_requirement = \
            obj.get('implemented_requirements')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """A unique identifier for the set of implemented controls.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, x):
        self._uuid = x

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, x):
        self._source = x

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
        """A description of how the specified set of controls are implemented
        for the containing component or capability.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

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
