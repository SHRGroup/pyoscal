class Incorporates_Component:
    """Incorporates Component

    TBD

    Attributes:
        component_uuid (uuid):A reference to a component by its
identifier

        prose (str):Default value holder for raw data in texts

        description (markup-multiline):A description of the
component, including information about its function.

    """

    contexts = [
        "oscal-component-definition",
        "oscal-implementation-common",
    ]
    parameters = [
        "component_uuid",
    ]
    subcomponents = [
        "prose",
        "description",
    ]

    def __init__(
        self,
        component_uuid,
        description,
        use_name='incorporates-component',
        prose=None,
    ):
        self._component_uuid = None
        self.component_uuid = \
            component_uuid
        self._prose = None
        self.prose = \
            prose
        self._description = None
        self.description = \
            description
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            component_uuid=obj.get(
                'component_uuid',
                None),
            prose=obj.get(
                'prose',
                None),
            description=obj.get(
                'description',
                None),
        )
        return newcls

    @property
    def component_uuid(self):
        """A reference to a component by its identifier
        """
        return self._component_uuid

    @component_uuid.setter
    def component_uuid(self, x):
        self._component_uuid = x

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
        """A description of the component, including information about its
        function.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x
