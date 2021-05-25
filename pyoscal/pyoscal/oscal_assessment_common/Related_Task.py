class Related_Task:
    """Task Reference

    Identifies an individual task for which the containing object is a
consequence of.

    Attributes:
        task_uuid (uuid):References a unique task by UUID.

        prose (str):Default value holder for raw data in texts

        oscal_property (ARRAY):

        link (ARRAY):

        responsible_party (BY_KEY):

        subject (ARRAY):

        identified_subject (str):Used to detail assessment subjects
that were identfied by this task.

        remarks (str):

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "task_uuid",
    ]
    subcomponents = [
        "prose",
        "oscal_property",
        "link",
        "responsible_party",
        "subject",
        "identified_subject",
        "remarks",
    ]

    def __init__(
        self,
        task_uuid,
        use_name='related-task',
        prose=None,
        oscal_property=None,
        link=None,
        responsible_party=None,
        subject=None,
        identified_subject=None,
        remarks=None,
    ):
        self._task_uuid = None
        self.task_uuid = \
            task_uuid
        self._prose = None
        self.prose = \
            prose
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._responsible_party = None
        self.responsible_party = \
            responsible_party
        self._subject = None
        self.subject = \
            subject
        self._identified_subject = None
        self.identified_subject = \
            identified_subject
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if responsible_party is None:
            self.responsible_party = []
        if subject is None:
            self.subject = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            task_uuid=obj.get(
                'task_uuid',
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
            responsible_party=obj.get(
                'responsible_party',
                None),
            subject=obj.get(
                'subject',
                None),
            identified_subject=obj.get(
                'identified_subject',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.responsible_party = \
            obj.get('responsible_parties')
        newcls.subject = \
            obj.get('subjects')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def task_uuid(self):
        """References a unique task by UUID.
        """
        return self._task_uuid

    @task_uuid.setter
    def task_uuid(self, x):
        self._task_uuid = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def identified_subject(self):
        """Used to detail assessment subjects that were identfied by this task.
        """
        return self._identified_subject

    @identified_subject.setter
    def identified_subject(self, x):
        self._identified_subject = x

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
