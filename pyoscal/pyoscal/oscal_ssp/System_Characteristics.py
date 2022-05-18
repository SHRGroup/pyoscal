class System_Characteristics:
    """System Characteristics

    Contains the characteristics of the system, such as its name, purpose,
and security impact level.

    Attributes:
        prose (str):Default value holder for raw data in texts

        system_id (ARRAY):

        system_name (string):The full name of the system.

        system_name_short (string):A short name for the system, such
as an acronym, that is suitable for display in a data table
or summary list.

        description (markup-multiline):A summary of the system.

        oscal_property (ARRAY):

        link (ARRAY):

        date_authorized (str):

        security_sensitivity_level (str):The overall information
system sensitivity categorization, such as defined by

        system_information (str):

        security_impact_level (str):

        status (str):

        authorization_boundary (str):

        network_architecture (str):

        data_flow (str):

        responsible_party (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-ssp",
        "oscal-metadata",
        "oscal-implementation-common",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "system_id",
        "system_name",
        "system_name_short",
        "description",
        "oscal_property",
        "link",
        "date_authorized",
        "security_sensitivity_level",
        "system_information",
        "security_impact_level",
        "status",
        "authorization_boundary",
        "network_architecture",
        "data_flow",
        "responsible_party",
        "remarks",
    ]

    def __init__(
        self,
        system_id,
        system_name,
        description,
        security_sensitivity_level,
        system_information,
        security_impact_level,
        status,
        authorization_boundary,
        use_name='system-characteristics',
        prose=None,
        system_name_short=None,
        oscal_property=None,
        link=None,
        date_authorized=None,
        network_architecture=None,
        data_flow=None,
        responsible_party=None,
        remarks=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._system_id = None
        self.system_id = \
            system_id
        self._system_name = None
        self.system_name = \
            system_name
        self._system_name_short = None
        self.system_name_short = \
            system_name_short
        self._description = None
        self.description = \
            description
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._date_authorized = None
        self.date_authorized = \
            date_authorized
        self._security_sensitivity_level = None
        self.security_sensitivity_level = \
            security_sensitivity_level
        self._system_information = None
        self.system_information = \
            system_information
        self._security_impact_level = None
        self.security_impact_level = \
            security_impact_level
        self._status = None
        self.status = \
            status
        self._authorization_boundary = None
        self.authorization_boundary = \
            authorization_boundary
        self._network_architecture = None
        self.network_architecture = \
            network_architecture
        self._data_flow = None
        self.data_flow = \
            data_flow
        self._responsible_party = None
        self.responsible_party = \
            responsible_party
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if system_id is None:
            self.system_id = []
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if responsible_party is None:
            self.responsible_party = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
            system_id=obj.get(
                'system_id',
                None),
            system_name=obj.get(
                'system_name',
                None),
            system_name_short=obj.get(
                'system_name_short',
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
            date_authorized=obj.get(
                'date_authorized',
                None),
            security_sensitivity_level=obj.get(
                'security_sensitivity_level',
                None),
            system_information=obj.get(
                'system_information',
                None),
            security_impact_level=obj.get(
                'security_impact_level',
                None),
            status=obj.get(
                'status',
                None),
            authorization_boundary=obj.get(
                'authorization_boundary',
                None),
            network_architecture=obj.get(
                'network_architecture',
                None),
            data_flow=obj.get(
                'data_flow',
                None),
            responsible_party=obj.get(
                'responsible_party',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.system_id = \
            obj.get('system_ids')
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.responsible_party = \
            obj.get('responsible_parties')
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
    def system_name(self):
        """The full name of the system.
        """
        return self._system_name

    @system_name.setter
    def system_name(self, x):
        self._system_name = x

    @property
    def system_name_short(self):
        """A short name for the system, such as an acronym, that is suitable
        for display in a data table or summary list.
        """
        return self._system_name_short

    @system_name_short.setter
    def system_name_short(self, x):
        self._system_name_short = x

    @property
    def description(self):
        """A summary of the system.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

    @property
    def date_authorized(self):
        return self._date_authorized

    @date_authorized.setter
    def date_authorized(self, x):
        self._date_authorized = x

    @property
    def security_sensitivity_level(self):
        """The overall information system sensitivity categorization, such as
        defined by
        """
        return self._security_sensitivity_level

    @security_sensitivity_level.setter
    def security_sensitivity_level(self, x):
        self._security_sensitivity_level = x

    @property
    def system_information(self):
        return self._system_information

    @system_information.setter
    def system_information(self, x):
        self._system_information = x

    @property
    def security_impact_level(self):
        return self._security_impact_level

    @security_impact_level.setter
    def security_impact_level(self, x):
        self._security_impact_level = x

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, x):
        self._status = x

    @property
    def authorization_boundary(self):
        return self._authorization_boundary

    @authorization_boundary.setter
    def authorization_boundary(self, x):
        self._authorization_boundary = x

    @property
    def network_architecture(self):
        return self._network_architecture

    @network_architecture.setter
    def network_architecture(self, x):
        self._network_architecture = x

    @property
    def data_flow(self):
        return self._data_flow

    @data_flow.setter
    def data_flow(self, x):
        self._data_flow = x

    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, x):
        self._remarks = x

    @property
    def system_id(self):
        return self._system_id

    @system_id.setter
    def system_id(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._system_id):
            self._system_id = []
        if bool(x):
            if x != self._system_id:
                self._system_id += list(x)

    @property
    def system_ids(self):
        return self._system_id

    @system_ids.setter
    def system_ids(self, x):
        self.system_id(x)

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
    def responsible_party(self):
        return self._responsible_party

    @responsible_party.setter
    def responsible_party(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._responsible_party):
            self._responsible_party = []
        if bool(x):
            if x != self._responsible_party:
                self._responsible_party += list(x)

    @property
    def responsible_parties(self):
        return self._responsible_party

    @responsible_parties.setter
    def responsible_parties(self, x):
        self.responsible_party(x)
