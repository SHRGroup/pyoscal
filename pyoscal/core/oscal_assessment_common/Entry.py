class Entry:
    """Risk Log Entry

    Identifies an individual risk response that occurred as part of
managing an identified risk.

    Attributes:
        uuid (uuid):Uniquely identifies a risk log entry. This UUID
may be referenced elsewhere in an OSCAL document when
referring to this information. A UUID should be consistently
used for this schedule across revisions of the document.

        prose (str):Default value holder for raw data in texts

        title (markup-line):The title for this risk log entry.

        description (markup-multiline):A human-readable description
of what was done regarding the risk.

        start (dateTime-with-timezone):Identifies the start date and
time of the event.

        end (dateTime-with-timezone):Identifies the end date and
time of the event. If the event is a point in time, the
start and end will be the same date and time.

        oscal_property (ARRAY):

        link (ARRAY):

        logged_by (ARRAY):

        status_change (str):

        related_response (ARRAY):Identifies an individual risk
response that this log entry is for.

        remarks (str):

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "uuid",
    ]
    subcomponents = [
        "prose",
        "title",
        "description",
        "start",
        "end",
        "oscal_property",
        "link",
        "logged_by",
        "status_change",
        "related_response",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        start,
        use_name='entry',
        prose=None,
        title=None,
        description=None,
        end=None,
        oscal_property=None,
        link=None,
        logged_by=None,
        status_change=None,
        related_response=None,
        remarks=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._prose = None
        self.prose = \
            prose
        self._title = None
        self.title = \
            title
        self._description = None
        self.description = \
            description
        self._start = None
        self.start = \
            start
        self._end = None
        self.end = \
            end
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._logged_by = None
        self.logged_by = \
            logged_by
        self._status_change = None
        self.status_change = \
            status_change
        self._related_response = None
        self.related_response = \
            related_response
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if logged_by is None:
            self.logged_by = []
        if related_response is None:
            self.related_response = []

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
            title=obj.get(
                'title',
                None),
            description=obj.get(
                'description',
                None),
            start=obj.get(
                'start',
                None),
            end=obj.get(
                'end',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            logged_by=obj.get(
                'logged_by',
                None),
            status_change=obj.get(
                'status_change',
                None),
            related_response=obj.get(
                'related_response',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.logged_by = \
            obj.get('logged_by')
        newcls.related_response = \
            obj.get('related_responses')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """Uniquely identifies a risk log entry. This UUID may be referenced
        elsewhere in an OSCAL document when referring to this information. A
        UUID should be consistently used for this schedule across revisions
        of the document.
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
    def title(self):
        """The title for this risk log entry.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def description(self):
        """A human-readable description of what was done regarding the risk.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

    @property
    def start(self):
        """Identifies the start date and time of the event.
        """
        return self._start

    @start.setter
    def start(self, x):
        self._start = x

    @property
    def end(self):
        """Identifies the end date and time of the event. If the event is a
        point in time, the start and end will be the same date and time.
        """
        return self._end

    @end.setter
    def end(self, x):
        self._end = x

    @property
    def status_change(self):
        return self._status_change

    @status_change.setter
    def status_change(self, x):
        self._status_change = x

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
    def logged_by(self):
        return self._logged_by

    @logged_by.setter
    def logged_by(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._logged_by):
            self._logged_by = []
        if bool(x):
            if x != self._logged_by:
                self._logged_by += list(x)

    @property
    def related_response(self):
        """Identifies an individual risk response that this log entry is for.
        """
        return self._related_response

    @related_response.setter
    def related_response(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._related_response):
            self._related_response = []
        if bool(x):
            if x != self._related_response:
                self._related_response += list(x)

    @property
    def related_responses(self):
        return self._related_response

    @related_responses.setter
    def related_responses(self, x):
        self.related_response(x)
