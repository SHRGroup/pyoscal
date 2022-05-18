class Profile:
    """Profile

    Each OSCAL profile is defined by a Profile element

    Attributes:
        uuid (uuid):A globally unique identifier for this profile
instance. This UUID should be changed when this document is
revised.

        prose (str):Default value holder for raw data in texts

        metadata (str):

        oscal_import (ARRAY):

        merge (str):

        modify (str):

        back_matter (str):

    """

    contexts = [
        "oscal-profile",
        "oscal-metadata",
        "oscal-catalog-common",
    ]
    parameters = [
        "uuid",
    ]
    subcomponents = [
        "prose",
        "metadata",
        "oscal_import",
        "merge",
        "modify",
        "back_matter",
    ]

    def __init__(
        self,
        uuid,
        metadata,
        oscal_import,
        use_name='profile',
        prose=None,
        merge=None,
        modify=None,
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
        self._oscal_import = None
        self.oscal_import = \
            oscal_import
        self._merge = None
        self.merge = \
            merge
        self._modify = None
        self.modify = \
            modify
        self._back_matter = None
        self.back_matter = \
            back_matter
        self.use_name = use_name
        if oscal_import is None:
            self.oscal_import = []

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
            oscal_import=obj.get(
                'oscal_import',
                None),
            merge=obj.get(
                'merge',
                None),
            modify=obj.get(
                'modify',
                None),
            back_matter=obj.get(
                'back_matter',
                None),
        )
        newcls.oscal_import = \
            obj.get('imports')
        return newcls

    @property
    def uuid(self):
        """A globally unique identifier for this profile instance. This UUID
        should be changed when this document is revised.
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
    def merge(self):
        return self._merge

    @merge.setter
    def merge(self, x):
        self._merge = x

    @property
    def modify(self):
        return self._modify

    @modify.setter
    def modify(self, x):
        self._modify = x

    @property
    def back_matter(self):
        return self._back_matter

    @back_matter.setter
    def back_matter(self, x):
        self._back_matter = x

    @property
    def oscal_import(self):
        return self._oscal_import

    @oscal_import.setter
    def oscal_import(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._oscal_import):
            self._oscal_import = []
        if bool(x):
            if x != self._oscal_import:
                self._oscal_import += list(x)

    @property
    def imports(self):
        return self._oscal_import

    @imports.setter
    def imports(self, x):
        self.oscal_import(x)
