class Source:
    """Assessment Subject Source

    Assessment subjects will be identified while conducting the referenced
activity-instance.

    Attributes:
        task_uuid (uuid):Uniquely identifies an assessment activity
to be performed as part of the event. This UUID may be
referenced elsewhere in an OSCAL document when referring to
this information. A UUID should be consistently used for
this schedule across revisions of the document.

        prose (str):Default value holder for raw data in texts

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
    ]

    def __init__(
        self,
        task_uuid,
        use_name='source',
        prose=None,
    ):
        self._task_uuid = None
        self.task_uuid = \
            task_uuid
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

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
        )
        return newcls

    @property
    def task_uuid(self):
        """Uniquely identifies an assessment activity to be performed as part
        of the event. This UUID may be referenced elsewhere in an OSCAL
        document when referring to this information. A UUID should be
        consistently used for this schedule across revisions of the
        document.
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
