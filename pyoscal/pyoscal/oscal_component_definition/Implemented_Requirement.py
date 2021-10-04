class Implemented_Requirement:
    """Control Implementation

    Describes how the containing component or capability implements an
individual control.

    Attributes:
        uuid (uuid):A unique identifier for a specific control
implementation.

        control_id (str):

        prose (str):Default value holder for raw data in texts

        description (markup-multiline):A description of how the
specified control is implemented for the containing
component or capability.

        oscal_property (ARRAY):

        link (ARRAY):

        set_parameter (ARRAY):

        responsible_role (ARRAY):

        statement (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-component-definition",
        "oscal-implementation-common",
    ]
    parameters = [
        "uuid",
        "control_id",
    ]
    subcomponents = [
        "prose",
        "description",
        "oscal_property",
        "link",
        "set_parameter",
        "responsible_role",
        "statement",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        control_id,
        description,
        use_name='implemented-requirement',
        prose=None,
        oscal_property=None,
        link=None,
        set_parameter=None,
        responsible_role=None,
        statement=None,
        remarks=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
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
        self._set_parameter = None
        self.set_parameter = \
            set_parameter
        self._responsible_role = None
        self.responsible_role = \
            responsible_role
        self._statement = None
        self.statement = \
            statement
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if set_parameter is None:
            self.set_parameter = []
        if responsible_role is None:
            self.responsible_role = []
        if statement is None:
            self.statement = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            uuid=obj.get(
                'uuid',
                None),
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
            set_parameter=obj.get(
                'set_parameter',
                None),
            responsible_role=obj.get(
                'responsible_role',
                None),
            statement=obj.get(
                'statement',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.set_parameter = \
            obj.get('set_parameters')
        newcls.responsible_role = \
            obj.get('responsible_roles')
        newcls.statement = \
            obj.get('statements')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """A unique identifier for a specific control implementation.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, x):
        self._uuid = x

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
        """A description of how the specified control is implemented for the
        containing component or capability.
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
    def statement(self):
        return self._statement

    @statement.setter
    def statement(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._statement):
            self._statement = []
        if bool(x):
            if x != self._statement:
                self._statement += list(x)

    @property
    def statements(self):
        return self._statement

    @statements.setter
    def statements(self, x):
        self.statement(x)
