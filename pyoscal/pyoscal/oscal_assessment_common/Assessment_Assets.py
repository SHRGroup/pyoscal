class Assessment_Assets:
    """Assessment Assets

    Identifies the assets used to perform this assessment, such as the
assessment team, scanning tools, and assumptions.

    Attributes:
        prose (str):Default value holder for raw data in texts

        component (BY_KEY):

        assessment_platform (ARRAY):Used to represent the toolset
used to perform aspects of the assessment.

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
        "component",
        "assessment_platform",
    ]

    def __init__(
        self,
        assessment_platform,
        use_name='assessment-assets',
        prose=None,
        component=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._component = None
        self.component = \
            component
        self._assessment_platform = None
        self.assessment_platform = \
            assessment_platform
        self.use_name = use_name
        if component is None:
            self.component = []
        if assessment_platform is None:
            self.assessment_platform = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
            component=obj.get(
                'component',
                None),
            assessment_platform=obj.get(
                'assessment_platform',
                None),
        )
        newcls.component = \
            obj.get('components')
        newcls.assessment_platform = \
            obj.get('assessment_platforms')
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
    def component(self):
        return self._component

    @component.setter
    def component(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._component):
            self._component = []
        if bool(x):
            if x != self._component:
                self._component += list(x)

    @property
    def components(self):
        return self._component

    @components.setter
    def components(self, x):
        self.component(x)

    @property
    def assessment_platform(self):
        """Used to represent the toolset used to perform aspects of the
        assessment.
        """
        return self._assessment_platform

    @assessment_platform.setter
    def assessment_platform(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._assessment_platform):
            self._assessment_platform = []
        if bool(x):
            if x != self._assessment_platform:
                self._assessment_platform += list(x)

    @property
    def assessment_platforms(self):
        return self._assessment_platform

    @assessment_platforms.setter
    def assessment_platforms(self, x):
        self.assessment_platform(x)
