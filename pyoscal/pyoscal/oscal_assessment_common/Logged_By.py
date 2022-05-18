class Logged_By:
    """Logged By

    Used to indicate who created a log entry in what role.

    Attributes:
        party_uuid (uuid):A pointer to the party who is making the
log entry.

        role_id (token):A point to the role-id of the role in which
the party is making the log entry.

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "party_uuid",
        "role_id",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        party_uuid,
        use_name='logged-by',
        role_id=None,
        prose=None,
    ):
        self._party_uuid = None
        self.party_uuid = \
            party_uuid
        self._role_id = None
        self.role_id = \
            role_id
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            party_uuid=obj.get(
                'party_uuid',
                None),
            role_id=obj.get(
                'role_id',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def party_uuid(self):
        """A pointer to the party who is making the log entry.
        """
        return self._party_uuid

    @party_uuid.setter
    def party_uuid(self, x):
        self._party_uuid = x

    @property
    def role_id(self):
        """A point to the role-id of the role in which the party is making the
        log entry.
        """
        return self._role_id

    @role_id.setter
    def role_id(self, x):
        self._role_id = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x
