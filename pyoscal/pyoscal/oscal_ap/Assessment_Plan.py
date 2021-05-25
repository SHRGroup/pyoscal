class Assessment_Plan:
    """Security Assessment Plan (SAP)

    An assessment plan, such as those provided by a FedRAMP assessor.

    Attributes:
        uuid (uuid):Uniquely identifies this assessment plan. This
UUID must be changed each time the content of the plan
changes.

        prose (str):Default value holder for raw data in texts

        metadata (str):

        import_ssp (str):

        local_definitions (str):Used to define data objects that are
used in the assessment plan, that do not appear in the
referenced SSP.

        terms_and_conditions (str):Used to define various terms and
conditions under which an assessment, described by the plan,
can be performed. Each child part defines a different type
of term or condition.

        reviewed_controls (str):

        assessment_subject (ARRAY):

        assessment_assets (str):

        task (ARRAY):

        back_matter (str):

    """

    contexts = [
        "oscal-ap",
        "oscal-metadata",
        "oscal-assessment-common",
    ]
    parameters = [
        "uuid",
    ]
    subcomponents = [
        "prose",
        "metadata",
        "import_ssp",
        "local_definitions",
        "terms_and_conditions",
        "reviewed_controls",
        "assessment_subject",
        "assessment_assets",
        "task",
        "back_matter",
    ]

    def __init__(
        self,
        uuid,
        metadata,
        import_ssp,
        reviewed_controls,
        use_name='assessment-plan',
        prose=None,
        local_definitions=None,
        terms_and_conditions=None,
        assessment_subject=None,
        assessment_assets=None,
        task=None,
        back_matter=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._prose = None
        self.prose = \
            prose
        self._metadata = None
        self.metadata = \
            metadata
        self._import_ssp = None
        self.import_ssp = \
            import_ssp
        self._local_definitions = None
        self.local_definitions = \
            local_definitions
        self._terms_and_conditions = None
        self.terms_and_conditions = \
            terms_and_conditions
        self._reviewed_controls = None
        self.reviewed_controls = \
            reviewed_controls
        self._assessment_subject = None
        self.assessment_subject = \
            assessment_subject
        self._assessment_assets = None
        self.assessment_assets = \
            assessment_assets
        self._task = None
        self.task = \
            task
        self._back_matter = None
        self.back_matter = \
            back_matter
        self.use_name = use_name
        if assessment_subject is None:
            self.assessment_subject = []
        if task is None:
            self.task = []

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
            metadata=obj.get(
                'metadata',
                None),
            import_ssp=obj.get(
                'import_ssp',
                None),
            local_definitions=obj.get(
                'local_definitions',
                None),
            terms_and_conditions=obj.get(
                'terms_and_conditions',
                None),
            reviewed_controls=obj.get(
                'reviewed_controls',
                None),
            assessment_subject=obj.get(
                'assessment_subject',
                None),
            assessment_assets=obj.get(
                'assessment_assets',
                None),
            task=obj.get(
                'task',
                None),
            back_matter=obj.get(
                'back_matter',
                None),
        )
        newcls.assessment_subject = \
            obj.get('assessment_subjects')
        newcls.task = \
            obj.get('tasks')
        newcls.task = \
            obj.get('assessment_task')
        newcls.task = \
            obj.get('assessment_task')
        return newcls

    @property
    def uuid(self):
        """Uniquely identifies this assessment plan. This UUID must be changed
        each time the content of the plan changes.
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
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, x):
        self._metadata = x

    @property
    def import_ssp(self):
        return self._import_ssp

    @import_ssp.setter
    def import_ssp(self, x):
        self._import_ssp = x

    @property
    def local_definitions(self):
        """Used to define data objects that are used in the assessment plan,
        that do not appear in the referenced SSP.
        """
        return self._local_definitions

    @local_definitions.setter
    def local_definitions(self, x):
        self._local_definitions = x

    @property
    def terms_and_conditions(self):
        """Used to define various terms and conditions under which an
        assessment, described by the plan, can be performed. Each child part
        defines a different type of term or condition.
        """
        return self._terms_and_conditions

    @terms_and_conditions.setter
    def terms_and_conditions(self, x):
        self._terms_and_conditions = x

    @property
    def reviewed_controls(self):
        return self._reviewed_controls

    @reviewed_controls.setter
    def reviewed_controls(self, x):
        self._reviewed_controls = x

    @property
    def assessment_assets(self):
        return self._assessment_assets

    @assessment_assets.setter
    def assessment_assets(self, x):
        self._assessment_assets = x

    @property
    def back_matter(self):
        return self._back_matter

    @back_matter.setter
    def back_matter(self, x):
        self._back_matter = x

    @property
    def assessment_subject(self):
        return self._assessment_subject

    @assessment_subject.setter
    def assessment_subject(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._assessment_subject):
            self._assessment_subject = []
        if bool(x):
            if x != self._assessment_subject:
                self._assessment_subject += list(x)

    @property
    def assessment_subjects(self):
        return self._assessment_subject

    @assessment_subjects.setter
    def assessment_subjects(self, x):
        self.assessment_subject(x)

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
