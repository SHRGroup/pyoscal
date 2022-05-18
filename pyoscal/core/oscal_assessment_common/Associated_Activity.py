class Associated_Activity:
    """Associated Activity

    Identifies an individual activity to be performed as part of a task.

    Attributes:
        activity_uuid (uuid):References an activity defined in the
list of activities.

        prose (str):Default value holder for raw data in texts

        oscal_property (ARRAY):

        link (ARRAY):

        responsible_role (ARRAY):

        subject (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "activity_uuid",
    ]
    subcomponents = [
        "prose",
        "oscal_property",
        "link",
        "responsible_role",
        "subject",
        "remarks",
    ]

    def __init__(
        self,
        activity_uuid,
        subject,
        use_name='associated-activity',
        prose=None,
        oscal_property=None,
        link=None,
        responsible_role=None,
        remarks=None,
    ):
        self._activity_uuid = None
        self.activity_uuid = \
            activity_uuid
        self._prose = None
        self.prose = \
            prose
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._responsible_role = None
        self.responsible_role = \
            responsible_role
        self._subject = None
        self.subject = \
            subject
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
        if subject is None:
            self.subject = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            activity_uuid=obj.get(
                'activity_uuid',
                None),
            prose=obj.get(
                'prose',
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
            subject=obj.get(
                'subject',
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
        newcls.subject = \
            obj.get('subjects')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def activity_uuid(self):
        """References an activity defined in the list of activities.
        """
        return self._activity_uuid

    @activity_uuid.setter
    def activity_uuid(self, x):
        self._activity_uuid = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

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
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._subject):
            self._subject = []
        if bool(x):
            if x != self._subject:
                self._subject += list(x)

    @property
    def subjects(self):
        return self._subject

    @subjects.setter
    def subjects(self, x):
        self.subject(x)
