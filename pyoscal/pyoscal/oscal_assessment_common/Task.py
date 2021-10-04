class Task:
    """Task

    Represents a scheduled event or milestone, which may be associated
with a series of assessment actions.

    Attributes:
        uuid (uuid):Uniquely identifies this assessment task.

        type (token):The type of task.

        prose (str):Default value holder for raw data in texts

        title (markup-line):The title for this task.

        description (markup-multiline):A human-readable description
of this task.

        oscal_property (ARRAY):

        link (ARRAY):

        timing (str):The timing under which the task is intended to
occur.

        dependency (ARRAY):Used to indicate that a task is dependent
on another task.

        task (ARRAY):

        associated_activity (ARRAY):Identifies an individual
activity to be performed as part of a task.

        subject (ARRAY):

        responsible_role (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "uuid",
        "type",
    ]
    subcomponents = [
        "prose",
        "title",
        "description",
        "oscal_property",
        "link",
        "timing",
        "dependency",
        "task",
        "associated_activity",
        "subject",
        "responsible_role",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        type,
        title,
        use_name='task',
        prose=None,
        description=None,
        oscal_property=None,
        link=None,
        timing=None,
        dependency=None,
        task=None,
        associated_activity=None,
        subject=None,
        responsible_role=None,
        remarks=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._type = None
        self.type = \
            type
        self._prose = None
        self.prose = \
            prose
        self._title = None
        self.title = \
            title
        self._description = None
        self.description = \
            description
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._timing = None
        self.timing = \
            timing
        self._dependency = None
        self.dependency = \
            dependency
        self._task = None
        self.task = \
            task
        self._associated_activity = None
        self.associated_activity = \
            associated_activity
        self._subject = None
        self.subject = \
            subject
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
        if dependency is None:
            self.dependency = []
        if task is None:
            self.task = []
        if associated_activity is None:
            self.associated_activity = []
        if subject is None:
            self.subject = []
        if responsible_role is None:
            self.responsible_role = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            uuid=obj.get(
                'uuid',
                None),
            type=obj.get(
                'type',
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
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            timing=obj.get(
                'timing',
                None),
            dependency=obj.get(
                'dependency',
                None),
            task=obj.get(
                'task',
                None),
            associated_activity=obj.get(
                'associated_activity',
                None),
            subject=obj.get(
                'subject',
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
        newcls.dependency = \
            obj.get('dependencies')
        newcls.task = \
            obj.get('tasks')
        newcls.associated_activity = \
            obj.get('associated_activities')
        newcls.subject = \
            obj.get('subjects')
        newcls.responsible_role = \
            obj.get('responsible_roles')
        newcls.oscal_property = \
            obj.get('prop')
        newcls.task = \
            obj.get('assessment_task')
        newcls.task = \
            obj.get('assessment_task')
        return newcls

    @property
    def uuid(self):
        """Uniquely identifies this assessment task.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, x):
        self._uuid = x

    @property
    def type(self):
        """The type of task.
        """
        return self._type

    @type.setter
    def type(self, x):
        self._type = x

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
        """The title for this task.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def description(self):
        """A human-readable description of this task.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

    @property
    def timing(self):
        """The timing under which the task is intended to occur.
        """
        return self._timing

    @timing.setter
    def timing(self, x):
        self._timing = x

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
    def dependency(self):
        """Used to indicate that a task is dependent on another task.
        """
        return self._dependency

    @dependency.setter
    def dependency(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._dependency):
            self._dependency = []
        if bool(x):
            if x != self._dependency:
                self._dependency += list(x)

    @property
    def dependencies(self):
        return self._dependency

    @dependencies.setter
    def dependencies(self, x):
        self.dependency(x)

    @property
    def task(self):
        return self._task

    @task.setter
    def task(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._task):
            self._task = []
        if bool(x):
            if x != self._task:
                self._task += list(x)

    @property
    def tasks(self):
        return self._task

    @tasks.setter
    def tasks(self, x):
        self.task(x)

    @property
    def assessment_task(self):
        return self._task

    @assessment_task.setter
    def assessment_task(self, x):
        self.task(x)

    @property
    def assessment_task(self):
        return self._task

    @assessment_task.setter
    def assessment_task(self, x):
        self.task(x)

    @property
    def associated_activity(self):
        """Identifies an individual activity to be performed as part of a task.
        """
        return self._associated_activity

    @associated_activity.setter
    def associated_activity(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._associated_activity):
            self._associated_activity = []
        if bool(x):
            if x != self._associated_activity:
                self._associated_activity += list(x)

    @property
    def associated_activities(self):
        return self._associated_activity

    @associated_activities.setter
    def associated_activities(self, x):
        self.associated_activity(x)

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


class Assessment_Task(Task):
    def __init__(self, **kw):
        super(Assessment_Task, self).__init__(**kw)
        self.use_name = 'assessment_task'
