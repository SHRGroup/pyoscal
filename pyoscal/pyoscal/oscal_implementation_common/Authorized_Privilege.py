class Authorized_Privilege:
    """Privilege

    Identifies a specific system privilege held by the user, along with an
associated description and/or rationale for the privilege.

    Attributes:
        prose (str):Default value holder for raw data in texts

        title (markup-line):A human readable name for the privilege.

        description (markup-multiline):A summary of the privilege's
purpose within the system.

        function_performed (ARRAY):

    """

    contexts = [
        "oscal-implementation-common",
        "oscal-metadata",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "title",
        "description",
        "function_performed",
    ]

    def __init__(
        self,
        title,
        function_performed,
        use_name='authorized-privilege',
        prose=None,
        description=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._title = None
        self.title = \
            title
        self._description = None
        self.description = \
            description
        self._function_performed = None
        self.function_performed = \
            function_performed
        self.use_name = use_name
        if function_performed is None:
            self.function_performed = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
            title=obj.get(
                'title',
                None),
            description=obj.get(
                'description',
                None),
            function_performed=obj.get(
                'function_performed',
                None),
        )
        newcls.function_performed = \
            obj.get('functions_performed')
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
    def title(self):
        """A human readable name for the privilege.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def description(self):
        """A summary of the privilege's purpose within the system.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

    @property
    def function_performed(self):
        return self._function_performed

    @function_performed.setter
    def function_performed(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._function_performed):
            self._function_performed = []
        if bool(x):
            if x != self._function_performed:
                self._function_performed += list(x)

    @property
    def functions_performed(self):
        return self._function_performed

    @functions_performed.setter
    def functions_performed(self, x):
        self.function_performed(x)
