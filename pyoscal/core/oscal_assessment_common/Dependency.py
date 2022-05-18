class Dependency:
    """Task Dependency

    Used to indicate that a task is dependent on another task.

    Attributes:
        task_uuid (uuid):References a unique task by UUID.

        prose (str):Default value holder for raw data in texts

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
        "remarks",
    ]

    def __init__(
        self,
        task_uuid,
        use_name='dependency',
        prose=None,
        remarks=None,
    ):
        self._task_uuid = None
        self.task_uuid = \
            task_uuid
        self._prose = None
        self.prose = \
            prose
        self._remarks = None
        self.remarks = \
            remarks
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
            remarks=obj.get(
                'remarks',
                None),
        )
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
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, x):
        self._remarks = x
