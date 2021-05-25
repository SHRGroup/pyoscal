class By_Component:
    """Component Control Implementation

    Defines how the referenced component implements a set of controls.

    Attributes:
        component_uuid (uuid):A reference to the component that is
implementing a given control or control statement.

        uuid (uuid):A globally unique identifier that can be used to
reference this by-component entry elsewhere in an OSCAL
document. A UUID should be consistently used for a given
resource across revisions of the document.

        prose (str):Default value holder for raw data in texts

        description (markup-multiline):An implementation statement
that describes how a control or a control statement is
implemented within the referenced system component.

        oscal_property (ARRAY):

        link (ARRAY):

        set_parameter (BY_KEY):

        implementation_status (str):

        export (str):Identifies content intended for external
consumption, such as with leveraged organizations.

        inherited (ARRAY):Describes a control implementation
inherited by a leveraging system.

        satisfied (ARRAY):Describes how this system satisfies a
responsibility imposed by a leveraged system.

        responsible_role (BY_KEY):

        remarks (str):

    """

    contexts = [
        "oscal-ssp",
        "oscal-metadata",
        "oscal-implementation-common",
    ]
    parameters = [
        "component_uuid",
        "uuid",
    ]
    subcomponents = [
        "prose",
        "description",
        "oscal_property",
        "link",
        "set_parameter",
        "implementation_status",
        "export",
        "inherited",
        "satisfied",
        "responsible_role",
        "remarks",
    ]

    def __init__(
        self,
        component_uuid,
        uuid,
        description,
        use_name='by-component',
        prose=None,
        oscal_property=None,
        link=None,
        set_parameter=None,
        implementation_status=None,
        export=None,
        inherited=None,
        satisfied=None,
        responsible_role=None,
        remarks=None,
    ):
        self._component_uuid = None
        self.component_uuid = \
            component_uuid
        self._uuid = None
        self.uuid = \
            uuid
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
        self._implementation_status = None
        self.implementation_status = \
            implementation_status
        self._export = None
        self.export = \
            export
        self._inherited = None
        self.inherited = \
            inherited
        self._satisfied = None
        self.satisfied = \
            satisfied
        self._responsible_role = None
        self.responsible_role = \
            responsible_role
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
        if inherited is None:
            self.inherited = []
        if satisfied is None:
            self.satisfied = []
        if responsible_role is None:
            self.responsible_role = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            component_uuid=obj.get(
                'component_uuid',
                None),
            uuid=obj.get(
                'uuid',
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
            implementation_status=obj.get(
                'implementation_status',
                None),
            export=obj.get(
                'export',
                None),
            inherited=obj.get(
                'inherited',
                None),
            satisfied=obj.get(
                'satisfied',
                None),
            responsible_role=obj.get(
                'responsible_role',
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
            obj.get('parameter_settings')
        newcls.inherited = \
            obj.get('inherited')
        newcls.satisfied = \
            obj.get('satisfied')
        newcls.responsible_role = \
            obj.get('responsible_roles')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def component_uuid(self):
        """A reference to the component that is implementing a given control or
        control statement.
        """
        return self._component_uuid

    @component_uuid.setter
    def component_uuid(self, x):
        self._component_uuid = x

    @property
    def uuid(self):
        """A globally unique identifier that can be used to reference this by-
        component entry elsewhere in an OSCAL document. A UUID should be
        consistently used for a given resource across revisions of the
        document.
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
    def description(self):
        """An implementation statement that describes how a control or a
        control statement is implemented within the referenced system
        component.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

    @property
    def implementation_status(self):
        return self._implementation_status

    @implementation_status.setter
    def implementation_status(self, x):
        self._implementation_status = x

    @property
    def export(self):
        """Identifies content intended for external consumption, such as with
        leveraged organizations.
        """
        return self._export

    @export.setter
    def export(self, x):
        self._export = x

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
    def parameter_settings(self):
        return self._set_parameter

    @parameter_settings.setter
    def parameter_settings(self, x):
        self.set_parameter(x)

    @property
    def inherited(self):
        """Describes a control implementation inherited by a leveraging system.
        """
        return self._inherited

    @inherited.setter
    def inherited(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._inherited):
            self._inherited = []
        if bool(x):
            if x != self._inherited:
                self._inherited += list(x)

    @property
    def satisfied(self):
        """Describes how this system satisfies a responsibility imposed by a
        leveraged system.
        """
        return self._satisfied

    @satisfied.setter
    def satisfied(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._satisfied):
            self._satisfied = []
        if bool(x):
            if x != self._satisfied:
                self._satisfied += list(x)

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
