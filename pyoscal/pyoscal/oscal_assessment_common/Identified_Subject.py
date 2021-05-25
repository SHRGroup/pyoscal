class Identified_Subject:
    """Identified Subject

    Used to detail assessment subjects that were identfied by this task.

    Attributes:
        subject_placeholder_uuid (uuid):References a unique
assessment subject placeholder defined by this task.

        prose (str):Default value holder for raw data in texts

        subject (ARRAY):

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "subject_placeholder_uuid",
    ]
    subcomponents = [
        "prose",
        "subject",
    ]

    def __init__(
        self,
        subject_placeholder_uuid,
        subject,
        use_name='identified-subject',
        prose=None,
    ):
        self._subject_placeholder_uuid = None
        self.subject_placeholder_uuid = \
            subject_placeholder_uuid
        self._prose = None
        self.prose = \
            prose
        self._subject = None
        self.subject = \
            subject
        self.use_name = use_name
        if subject is None:
            self.subject = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            subject_placeholder_uuid=obj.get(
                'subject_placeholder_uuid',
                None),
            prose=obj.get(
                'prose',
                None),
            subject=obj.get(
                'subject',
                None),
        )
        newcls.subject = \
            obj.get('subjects')
        return newcls

    @property
    def subject_placeholder_uuid(self):
        """References a unique assessment subject placeholder defined by this
        task.
        """
        return self._subject_placeholder_uuid

    @subject_placeholder_uuid.setter
    def subject_placeholder_uuid(self, x):
        self._subject_placeholder_uuid = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

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
