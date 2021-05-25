class Origin:
    """Origin

    Identifies the source of the finding, such as a tool, interviewed
person, or activity.

    Attributes:
        prose (str):Default value holder for raw data in texts

        actor (ARRAY):

        related_task (ARRAY):

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "actor",
        "related_task",
    ]

    def __init__(
        self,
        actor,
        use_name='origin',
        prose=None,
        related_task=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._actor = None
        self.actor = \
            actor
        self._related_task = None
        self.related_task = \
            related_task
        self.use_name = use_name
        if actor is None:
            self.actor = []
        if related_task is None:
            self.related_task = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
            actor=obj.get(
                'actor',
                None),
            related_task=obj.get(
                'related_task',
                None),
        )
        newcls.actor = \
            obj.get('actors')
        newcls.related_task = \
            obj.get('related_tasks')
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
    def actor(self):
        return self._actor

    @actor.setter
    def actor(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._actor):
            self._actor = []
        if bool(x):
            if x != self._actor:
                self._actor += list(x)

    @property
    def actors(self):
        return self._actor

    @actors.setter
    def actors(self, x):
        self.actor(x)

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
