class Import_Ap:
    """Import Assessment Plan

    Used by assessment-results to import information about the original
plan for assessing the system.

    Attributes:
        href (uri-reference):>A resolvable URL reference to the
assessment plan governing the assessment activities.

        prose (str):Default value holder for raw data in texts

        remarks (str):

    """

    contexts = [
        "oscal-ar",
        "oscal-metadata",
        "oscal-assessment-common",
    ]
    parameters = [
        "href",
    ]
    subcomponents = [
        "prose",
        "remarks",
    ]

    def __init__(
        self,
        href,
        use_name='import-ap',
        prose=None,
        remarks=None,
    ):
        self._href = None
        self.href = \
            href
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
            href=obj.get(
                'href',
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
    def href(self):
        """>A resolvable URL reference to the assessment plan governing the
        assessment activities.
        """
        return self._href

    @href.setter
    def href(self, x):
        self._href = x

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
