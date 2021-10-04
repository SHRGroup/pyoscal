class Component_Definition:
    """Component Definition

    A collection of component descriptions, which may optionally be
grouped by capability.

    Attributes:
        uuid (uuid):A globally unique identifier for this component
definition instance. This UUID should be changed when this
document is revised.

        prose (str):Default value holder for raw data in texts

        metadata (str):

        import_component_definition (ARRAY):

        component (ARRAY):

        capability (ARRAY):

        back_matter (str):

    """

    contexts = [
        "oscal-component-definition",
        "oscal-implementation-common",
    ]
    parameters = [
        "uuid",
    ]
    subcomponents = [
        "prose",
        "metadata",
        "import_component_definition",
        "component",
        "capability",
        "back_matter",
    ]

    def __init__(
        self,
        uuid,
        metadata,
        use_name='component-definition',
        prose=None,
        import_component_definition=None,
        component=None,
        capability=None,
        back_matter=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._prose = None
        self.prose = \
            prose
        self._metadata = None
        self.metadata = \
            metadata
        self._import_component_definition = None
        self.import_component_definition = \
            import_component_definition
        self._component = None
        self.component = \
            component
        self._capability = None
        self.capability = \
            capability
        self._back_matter = None
        self.back_matter = \
            back_matter
        self.use_name = use_name
        if import_component_definition is None:
            self.import_component_definition = []
        if component is None:
            self.component = []
        if capability is None:
            self.capability = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            uuid=obj.get(
                'uuid',
                None),
            prose=obj.get(
                'prose',
                None),
            metadata=obj.get(
                'metadata',
                None),
            import_component_definition=obj.get(
                'import_component_definition',
                None),
            component=obj.get(
                'component',
                None),
            capability=obj.get(
                'capability',
                None),
            back_matter=obj.get(
                'back_matter',
                None),
        )
        newcls.import_component_definition = \
            obj.get('import_component_definitions')
        newcls.component = \
            obj.get('components')
        newcls.capability = \
            obj.get('capabilities')
        return newcls

    @property
    def uuid(self):
        """A globally unique identifier for this component definition instance.
        This UUID should be changed when this document is revised.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, x):
        self._uuid = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, x):
        self._metadata = x

    @property
    def back_matter(self):
        return self._back_matter

    @back_matter.setter
    def back_matter(self, x):
        self._back_matter = x

    @property
    def import_component_definition(self):
        return self._import_component_definition

    @import_component_definition.setter
    def import_component_definition(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._import_component_definition):
            self._import_component_definition = []
        if bool(x):
            if x != self._import_component_definition:
                self._import_component_definition += list(x)

    @property
    def import_component_definitions(self):
        return self._import_component_definition

    @import_component_definitions.setter
    def import_component_definitions(self, x):
        self.import_component_definition(x)

    @property
    def component(self):
        return self._component

    @component.setter
    def component(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._component):
            self._component = []
        if bool(x):
            if x != self._component:
                self._component += list(x)

    @property
    def components(self):
        return self._component

    @components.setter
    def components(self, x):
        self.component(x)

    @property
    def capability(self):
        return self._capability

    @capability.setter
    def capability(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._capability):
            self._capability = []
        if bool(x):
            if x != self._capability:
                self._capability += list(x)

    @property
    def capabilities(self):
        return self._capability

    @capabilities.setter
    def capabilities(self, x):
        self.capability(x)
