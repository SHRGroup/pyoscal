class Parameter_Guideline:
    """Guideline

    A prose statement that provides a recommendation for the use of a
parameter.

    Attributes:
        prose (markup-multiline):Prose permits multiple paragraphs,
lists, tables etc.

    """

    contexts = [
        "oscal-catalog-common",
        "oscal-metadata",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        prose,
        use_name='parameter-guideline',
    ):
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def prose(self):
        """Prose permits multiple paragraphs, lists, tables etc.
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x


class Guideline(Parameter_Guideline):
    def __init__(self, **kw):
        super(Guideline, self).__init__(**kw)
        self.use_name = 'guideline'
