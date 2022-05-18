class Assessment_Results:
    """Security Assessment Results (SAR)

    Security assessment results, such as those provided by a FedRAMP
assessor in the FedRAMP Security Assessment Report.

    Attributes:
        uuid (uuid):Uniquely identifies this assessment results
file. This UUID must be changed each time the content of the
results changes.

        prose (str):Default value holder for raw data in texts

        metadata (str):

        import_ap (str):

        local_definitions (str):Used to define data objects that are
used in the assessment plan, that do not appear in the
referenced SSP.

        result (ARRAY):

        back_matter (str):

    """

    contexts = [
        "oscal-ar",
        "oscal-metadata",
        "oscal-assessment-common",
    ]
    parameters = [
        "uuid",
    ]
    subcomponents = [
        "prose",
        "metadata",
        "import_ap",
        "local_definitions",
        "result",
        "back_matter",
    ]

    def __init__(
        self,
        uuid,
        metadata,
        import_ap,
        result,
        use_name='assessment-results',
        prose=None,
        local_definitions=None,
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
        self._import_ap = None
        self.import_ap = \
            import_ap
        self._local_definitions = None
        self.local_definitions = \
            local_definitions
        self._result = None
        self.result = \
            result
        self._back_matter = None
        self.back_matter = \
            back_matter
        self.use_name = use_name
        if result is None:
            self.result = []

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
            import_ap=obj.get(
                'import_ap',
                None),
            local_definitions=obj.get(
                'local_definitions',
                None),
            result=obj.get(
                'result',
                None),
            back_matter=obj.get(
                'back_matter',
                None),
        )
        newcls.result = \
            obj.get('results')
        newcls.result = \
            obj.get('result')
        return newcls

    @property
    def uuid(self):
        """Uniquely identifies this assessment results file. This UUID must be
        changed each time the content of the results changes.
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
    def import_ap(self):
        return self._import_ap

    @import_ap.setter
    def import_ap(self, x):
        self._import_ap = x

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
    def back_matter(self):
        return self._back_matter

    @back_matter.setter
    def back_matter(self, x):
        self._back_matter = x

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._result):
            self._result = []
        if bool(x):
            if x != self._result:
                self._result += list(x)

    @property
    def results(self):
        return self._result

    @results.setter
    def results(self, x):
        self.result(x)
