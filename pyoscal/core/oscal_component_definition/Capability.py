class Capability:
    """Capability

    A grouping of other components and/or capabilities.

    Attributes:
        uuid (uuid):A unique identifier for a capability.

        name (string):The capability's human-readable name.

        prose (str):Default value holder for raw data in texts

        description (markup-multiline):A summary of the capability.

        oscal_property (ARRAY):

        link (ARRAY):

        incorporates_component (ARRAY):

        control_implementation (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-component-definition",
        "oscal-implementation-common",
    ]
    parameters = [
        "uuid",
        "name",
    ]
    subcomponents = [
        "prose",
        "description",
        "oscal_property",
        "link",
        "incorporates_component",
        "control_implementation",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        name,
        description,
        use_name='capability',
        prose=None,
        oscal_property=None,
        link=None,
        incorporates_component=None,
        control_implementation=None,
        remarks=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._name = None
        self.name = \
            name
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
        self._incorporates_component = None
        self.incorporates_component = \
            incorporates_component
        self._control_implementation = None
        self.control_implementation = \
            control_implementation
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if incorporates_component is None:
            self.incorporates_component = []
        if control_implementation is None:
            self.control_implementation = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            uuid=obj.get(
                'uuid',
                None),
            name=obj.get(
                'name',
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
            incorporates_component=obj.get(
                'incorporates_component',
                None),
            control_implementation=obj.get(
                'control_implementation',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.incorporates_component = \
            obj.get('incorporates_components')
        newcls.control_implementation = \
            obj.get('control_implementations')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """A unique identifier for a capability.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, x):
        self._uuid = x

    @property
    def name(self):
        """The capability's human-readable name.
        """
        return self._name

    @name.setter
    def name(self, x):
        self._name = x

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
        """A summary of the capability.
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
    def incorporates_component(self):
        return self._incorporates_component

    @incorporates_component.setter
    def incorporates_component(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._incorporates_component):
            self._incorporates_component = []
        if bool(x):
            if x != self._incorporates_component:
                self._incorporates_component += list(x)

    @property
    def incorporates_components(self):
        return self._incorporates_component

    @incorporates_components.setter
    def incorporates_components(self, x):
        self.incorporates_component(x)

    @property
    def control_implementation(self):
        return self._control_implementation

    @control_implementation.setter
    def control_implementation(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._control_implementation):
            self._control_implementation = []
        if bool(x):
            if x != self._control_implementation:
                self._control_implementation += list(x)

    @property
    def control_implementations(self):
        return self._control_implementation

    @control_implementations.setter
    def control_implementations(self, x):
        self.control_implementation(x)
