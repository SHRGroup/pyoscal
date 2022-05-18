class Terms_And_Conditions:
    """Assessment Plan Terms and Conditions

    Used to define various terms and conditions under which an assessment,
described by the plan, can be performed. Each child part defines a
different type of term or condition.

    Attributes:
        prose (str):Default value holder for raw data in texts

        assessment_part (ARRAY):

    """

    contexts = [
        "oscal-ap",
        "oscal-metadata",
        "oscal-assessment-common",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "assessment_part",
    ]

    def __init__(
        self,
        use_name='terms-and-conditions',
        prose=None,
        assessment_part=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._assessment_part = None
        self.assessment_part = \
            assessment_part
        self.use_name = use_name
        if assessment_part is None:
            self.assessment_part = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
            assessment_part=obj.get(
                'assessment_part',
                None),
        )
        newcls.assessment_part = \
            obj.get('parts')
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
    def assessment_part(self):
        return self._assessment_part

    @assessment_part.setter
    def assessment_part(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._assessment_part):
            self._assessment_part = []
        if bool(x):
            if x != self._assessment_part:
                self._assessment_part += list(x)

    @property
    def parts(self):
        return self._assessment_part

    @parts.setter
    def parts(self, x):
        self.assessment_part(x)
