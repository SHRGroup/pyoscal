class Related_Response:
    """Risk Response Reference

    Identifies an individual risk response that this log entry is for.

    Attributes:
        response_uuid (uuid):References a unique risk response by
UUID.

        prose (str):Default value holder for raw data in texts

        oscal_property (ARRAY):

        link (ARRAY):

        related_task (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "response_uuid",
    ]
    subcomponents = [
        "prose",
        "oscal_property",
        "link",
        "related_task",
        "remarks",
    ]

    def __init__(
        self,
        response_uuid,
        use_name='related-response',
        prose=None,
        oscal_property=None,
        link=None,
        related_task=None,
        remarks=None,
    ):
        self._response_uuid = None
        self.response_uuid = \
            response_uuid
        self._prose = None
        self.prose = \
            prose
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._related_task = None
        self.related_task = \
            related_task
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if related_task is None:
            self.related_task = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            response_uuid=obj.get(
                'response_uuid',
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
            related_task=obj.get(
                'related_task',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.related_task = \
            obj.get('related_tasks')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def response_uuid(self):
        """References a unique risk response by UUID.
        """
        return self._response_uuid

    @response_uuid.setter
    def response_uuid(self, x):
        self._response_uuid = x

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
    def related_task(self):
        return self._related_task

    @related_task.setter
    def related_task(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._related_task):
            self._related_task = []
        if bool(x):
            if x != self._related_task:
                self._related_task += list(x)

    @property
    def related_tasks(self):
        return self._related_task

    @related_tasks.setter
    def related_tasks(self, x):
        self.related_task(x)
