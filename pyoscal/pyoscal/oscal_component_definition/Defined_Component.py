class Defined_Component:
    """Component

    A defined component that can be part of an implemented system.

    Attributes:
        uuid (uuid):The unique identifier for the component.

        type (str):

        prose (str):Default value holder for raw data in texts

        title (markup-line):A human readable name for the component.

        description (markup-multiline):A description of the
component, including information about its function.

        purpose (markup-line):A summary of the technological or
business purpose of the component.

        oscal_property (ARRAY):

        link (ARRAY):

        responsible_role (ARRAY):

        protocol (ARRAY):

        control_implementation (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-component-definition",
        "oscal-implementation-common",
    ]
    parameters = [
        "uuid",
        "type",
    ]
    subcomponents = [
        "prose",
        "title",
        "description",
        "purpose",
        "oscal_property",
        "link",
        "responsible_role",
        "protocol",
        "control_implementation",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        type,
        title,
        description,
        use_name='defined-component',
        prose=None,
        purpose=None,
        oscal_property=None,
        link=None,
        responsible_role=None,
        protocol=None,
        control_implementation=None,
        remarks=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._type = None
        self.type = \
            type
        self._prose = None
        self.prose = \
            prose
        self._title = None
        self.title = \
            title
        self._description = None
        self.description = \
            description
        self._purpose = None
        self.purpose = \
            purpose
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._responsible_role = None
        self.responsible_role = \
            responsible_role
        self._protocol = None
        self.protocol = \
            protocol
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
        if responsible_role is None:
            self.responsible_role = []
        if protocol is None:
            self.protocol = []
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
            type=obj.get(
                'type',
                None),
            prose=obj.get(
                'prose',
                None),
            title=obj.get(
                'title',
                None),
            description=obj.get(
                'description',
                None),
            purpose=obj.get(
                'purpose',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            responsible_role=obj.get(
                'responsible_role',
                None),
            protocol=obj.get(
                'protocol',
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
        newcls.responsible_role = \
            obj.get('responsible_roles')
        newcls.protocol = \
            obj.get('protocols')
        newcls.control_implementation = \
            obj.get('control_implementations')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """The unique identifier for the component.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, x):
        self._uuid = x

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, x):
        self._type = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def title(self):
        """A human readable name for the component.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def description(self):
        """A description of the component, including information about its
        function.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

    @property
    def purpose(self):
        """A summary of the technological or business purpose of the component.
        """
        return self._purpose

    @purpose.setter
    def purpose(self, x):
        self._purpose = x

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
    def responsible_role(self):
        return self._responsible_role

    @responsible_role.setter
    def responsible_role(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._responsible_role):
            self._responsible_role = []
        if bool(x):
            if x != self._responsible_role:
                self._responsible_role += list(x)

    @property
    def responsible_roles(self):
        return self._responsible_role

    @responsible_roles.setter
    def responsible_roles(self, x):
        self.responsible_role(x)

    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._protocol):
            self._protocol = []
        if bool(x):
            if x != self._protocol:
                self._protocol += list(x)

    @property
    def protocols(self):
        return self._protocol

    @protocols.setter
    def protocols(self, x):
        self.protocol(x)

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


class Component(Defined_Component):
    def __init__(self, **kw):
        super(Component, self).__init__(**kw)
        self.use_name = 'component'
