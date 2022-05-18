class Address:
    """Address

    A postal address for the location.

    Attributes:
        type (str):

        prose (str):Default value holder for raw data in texts

        addr_line (ARRAY):

        city (str):City, town or geographical region for the mailing
address.

        state (str):State, province or analogous geographical region
for mailing address

        postal_code (str):Postal or ZIP code for mailing address

        country (str):The ISO 3166-1 alpha-2 country code for the
mailing address.

    """

    contexts = [
        "oscal-metadata",
    ]
    parameters = [
        "type",
    ]
    subcomponents = [
        "prose",
        "addr_line",
        "city",
        "state",
        "postal_code",
        "country",
    ]

    def __init__(
        self,
        use_name='address',
        type=None,
        prose=None,
        addr_line=None,
        city=None,
        state=None,
        postal_code=None,
        country=None,
    ):
        self._type = None
        self.type = \
            type
        self._prose = None
        self.prose = \
            prose
        self._addr_line = None
        self.addr_line = \
            addr_line
        self._city = None
        self.city = \
            city
        self._state = None
        self.state = \
            state
        self._postal_code = None
        self.postal_code = \
            postal_code
        self._country = None
        self.country = \
            country
        self.use_name = use_name
        if addr_line is None:
            self.addr_line = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            type=obj.get(
                'type',
                None),
            prose=obj.get(
                'prose',
                None),
            addr_line=obj.get(
                'addr_line',
                None),
            city=obj.get(
                'city',
                None),
            state=obj.get(
                'state',
                None),
            postal_code=obj.get(
                'postal_code',
                None),
            country=obj.get(
                'country',
                None),
        )
        newcls.addr_line = \
            obj.get('addr_lines')
        return newcls

    @property
    def type(self):
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
    def city(self):
        """City, town or geographical region for the mailing address.
        """
        return self._city

    @city.setter
    def city(self, x):
        self._city = x

    @property
    def state(self):
        """State, province or analogous geographical region for mailing address
        """
        return self._state

    @state.setter
    def state(self, x):
        self._state = x

    @property
    def postal_code(self):
        """Postal or ZIP code for mailing address
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, x):
        self._postal_code = x

    @property
    def country(self):
        """The ISO 3166-1 alpha-2 country code for the mailing address.
        """
        return self._country

    @country.setter
    def country(self, x):
        self._country = x

    @property
    def addr_line(self):
        return self._addr_line

    @addr_line.setter
    def addr_line(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._addr_line):
            self._addr_line = []
        if bool(x):
            if x != self._addr_line:
                self._addr_line += list(x)

    @property
    def addr_lines(self):
        return self._addr_line

    @addr_lines.setter
    def addr_lines(self, x):
        self.addr_line(x)
