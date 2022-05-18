from pyoscal.core.oscal_ssp.Import_Profile import Import_Profile
from .core.oscal_metadata import (
    Metadata, Last_Modified, Version, Oscal_Version,
    Title as metaTitle, Uuid, Role_Id, Type, Name, Telephone_Number,
    Short_Name, Email_Address, Addr_Line, Address, City, Country,
    Postal_Code, State as addrState, Party, Responsible_Party
)

from .core.oscal_implementation_common import (
    System_User, System_Id, Description, System_Component, Title,
    Control_Id, Component_Type, Identifier_Type
)

from .core.oscal_ssp import (
    System_Security_Plan, System_Name, Security_Sensitivity_Level,
    Information_Type, Base, Confidentiality_Impact, System_Information,
    Authorization_Boundary, System_Characteristics,
    System_Implementation, Integrity_Impact, Availability_Impact,
    Security_Objective_Integrity, Security_Objective_Availability,
    Security_Objective_Confidentiality, Status, State, Href,
    Control_Implementation, Implemented_Requirement, Security_Impact_Level,
    By_Component, Component_Uuid, Party_Uuid
)

from .OSCAL import Oscal
from .common import getToday, createUUID, get_prop


class SSP(Oscal):

    def __init__(
        self,
        title="",
        version=getToday(fmt='day'),
        oscal_version=getToday(),
        last_modified=getToday(),
        uuid=createUUID(),
        obj=None
    ):

        if obj:
            self.oscal = obj
            return

        metadata = Metadata.Metadata(
            title=metaTitle.Title(prose=title),
            last_modified=Last_Modified.Last_Modified(prose=last_modified),
            version=Version.Version(prose=version),
            oscal_version=Oscal_Version.Oscal_Version(prose=oscal_version),
        )

        system_characteristics = System_Characteristics.System_Characteristics(
            system_id=None,
            system_name=None,
            description=None,
            security_sensitivity_level=  # noqa: E251
            Security_Sensitivity_Level.Security_Sensitivity_Level(),
            system_information=  # noqa: E251
            System_Information.System_Information(
                information_type=Information_Type.Information_Type(
                    title=Title.Title(prose=""),
                    description=Description.Description(prose=""),
                    confidentiality_impact=Confidentiality_Impact.
                    Confidentiality_Impact(
                        base=Base.Base()
                    ),
                    integrity_impact=Integrity_Impact.
                    Integrity_Impact(
                        base=Base.Base()
                    ),
                    availability_impact=  # noqa: E251
                    Availability_Impact.Availability_Impact(
                        base=Base.Base()
                    )
                )
            ),
            security_impact_level=Security_Impact_Level.
            Security_Impact_Level(
                security_objective_confidentiality=  # noqa: E251
                Security_Objective_Confidentiality.
                Security_Objective_Confidentiality(),
                security_objective_integrity=  # noqa: E251
                Security_Objective_Integrity.
                Security_Objective_Integrity(),
                security_objective_availability=  # noqa: E251
                Security_Objective_Availability.
                Security_Objective_Availability(),
            ),
            status=Status.Status(
                state=State.State(prose="")
            ),
            authorization_boundary=  # noqa: E251
            Authorization_Boundary.
            Authorization_Boundary(
                Description.Description(prose="")
            )
        )

        system_implementation = System_Implementation.System_Implementation(
            user=None,
            component=None
        )
        control_implementation = Control_Implementation.Control_Implementation(
            description=Description.Description(prose=""),
            implemented_requirement=None
        )

        self.oscal = System_Security_Plan.System_Security_Plan(
            uuid=Uuid.Uuid(prose=uuid),
            metadata=metadata,
            import_profile=Import_Profile(
                href=Href.Href(prose="")
            ),
            system_characteristics=system_characteristics,
            system_implementation=system_implementation,
            control_implementation=control_implementation
        )

    def set_cia(self, c, i, a):
        info = self.oscal.system_characteristics.\
               system_information.information_type[0]
        info.confidentiality_impact.base.prose = c
        info.integrity_impact.base.prose = i
        info.availability_impact.base.prose = a

        imp = self.oscal.system_characteristics.\
            security_impact_level
        imp.security_objective_confidentiality.prose = c
        imp.security_objective_integrity.prose = i
        imp.security_objective_availability.prose = a

    def add_party(
        self,
        role,
        name,
        personOrOrg='person',
        title='N/A',
        org='N/A',
        address='N/A',
        phone='N/A',
        email='N/A'
    ):
        uuid = createUUID()
        party = Party.Party(
            uuid=Uuid.Uuid(prose=uuid),
            type=Type.Type(prose=personOrOrg),
            name=Name.Name(prose=name),
            short_name=Short_Name.Short_Name(prose=title),
            telephone_number=Telephone_Number.Telephone_Number(prose=phone),
            email_address=Email_Address.Email_Address(prose=email),
            address=self.parse_address(address)
        )
        self.oscal.metadata.party = party
        responsible = Responsible_Party.Responsible_Party(
            role_id=Role_Id.Role_Id(prose=role),
            party_uuid=Party_Uuid.Party_Uuid(prose=uuid)
        )
        self.oscal.system_characteristics.responsible_party = responsible

    @property
    def information_types(self):
        return_value = []
        infos = self.oscal.system_characteristics.\
            system_information.information_type
        for info in infos:
            return_value += [
                {
                    'type':        info.title.prose,
                    'description': info.description.prose,
                    'id':          info.uuid.prose,
                    'cia':         (
                                       info.confidentiality_impact.base.prose,
                                       info.integrity_impact.base.prose,
                                       info.availability_impact.base.prose
                                   )
                }
            ]
        return return_value

    @property
    def impact_level(self):
        levels = self.oscal.system_characteristics.\
            security_impact_level
        return (
            levels.security_objective_confidentiality.prose,
            levels.security_objective_integrity.prose,
            levels.security_objective_availability.prose
        )

    def find_party_from_role(self, parent, roleid):
        for role in (parent.responsible_role or []):
            if role.role_id.prose == roleid:
                return role.party_uuid.prose
        return None

    def find_party(self, party_uuid):
        for p in self.oscal.metadata.party:
            if p.uuid.prose == party_uuid:
                return p
        return None

    def parse_address(self, addr_string):
        temp = ['', '', '', '', '']
        parts = addr_string.split(',')
        for i in range(len(parts)):
            temp[i] = parts[i].strip()
        return Address.Address(
            addr_line=Addr_Line.Addr_Line(prose=temp[0]),
            city=City.City(prose=temp[1]),
            state=addrState.State(prose=temp[2]),
            postal_code=Postal_Code.Postal_Code(prose=temp[3]),
            country=Country.Country(prose=temp[4])
        )

    def address2string(self, address):
        if address is None:
            return ""
        output = ""
        if isinstance(address, list):
            for a in address:
                output += self.address2string(a)+"\n"
        else:
            tmp = []
            if address.addr_line:
                tmp += ['\n'.join([line.prose for line in address.addr_line])]
            if address.city and address.city.prose:
                tmp += [address.city.prose]
            if address.state and address.state.prose:
                tmp += [address.state.prose]
            if address.postal_code and address.postal_code.prose:
                tmp += [address.postal_code.prose]
            if address.country and address.country.prose:
                tmp += [address.country.prose]
            return '\n'.join(tmp)
        return output

    def parse_party(self, party):
        if party is None:
            return {
                'name': "",
                'title': "",
                'organization': "",
                'address': "",
                'phone': "",
                'email': ""
            }
        name = party.name.prose or ""
        title = party.short_name.prose or ""
        if party.member_of_organization:
            organization = [
                p
                for p in self.oscal.metadata.party
                if p.uuid.prose == party.member_of_organization[0].prose
            ][0]
        else:
            organization = ""
        address = self.address2string(party.address)
        phone = ', '.join([p.prose for p in party.telephone_number])
        email = ', '.join([e.prose for e in party.email_address])
        return {
            'name': name,
            'title': title,
            'organization': organization,
            'address': address,
            'phone': phone,
            'email': email
        }

    def get_named_role(self, role_id):
        responsible = self.oscal.system_characteristics.responsible_party
        party_uuid = None
        for r in responsible:
            if r.role_id.prose == role_id:
                party_uuid = r.party_uuid[0].prose
        if party_uuid:
            party = self.find_party(party_uuid)
            return self.parse_party(party)
        return None

    @property
    def owner(self):
        return self.get_named_role('owner')

    @property
    def AO(self):
        return self.get_named_role('authorizing-official')

    @property
    def ISSO(self):
        return self.get_named_role('isso')

    @property
    def parties(self):
        parties = []
        responsible = self.oscal.system_characteristics.responsible_party
        for r in responsible:
            p = self.find_party(r.party_uuid[0].prose)
            if p:
                parties += [self.parse_party(p)]
        return parties

    @property
    def name(self):
        return self.oscal.system_characteristics.system_name.prose

    @property
    def description(self):
        return self.oscal.system_characteristics.description.prose

    @property
    def authorization_boundary(self):
        return self.oscal.system_characteristics.authorization_boundary.prose

    @property
    def system_id(self):
        return self.oscal.system_characteristics.system_id.prose

    @property
    def sensitivity(self):
        return self.oscal.system_characteristics.\
            security_sensitivity_level.prose

    @property
    def components(self):
        return_value = []
        for c in self.oscal.system_implementation.component:
            try:
                c_details = {
                    'title': c.title.prose,
                    'description': c.description.prose or "",
                    'type': c.type.prose or "",
                    'status': c.status.state.prose or "Unknown"
                }
            except Exception as e:
                print(e)
                pass
            return_value += [c_details]
        return return_value

    @property
    def status(self):
        return_value = {}
        for c in self.components:
            c_status = c.get('status')
            if c_status not in return_value:
                return_value[c_status] = []
            return_value[c_status] += c
        return return_value

    @property
    def users(self):
        return [
            {
                'role': u.role_id.prose or "",
                'privileged': get_prop('privileged', "NP"),
                'sensitivity': get_prop('sensitivity', 'Low'),
                'privileges': [(
                    ap.title.prose,
                    ap.description.prose,
                    ap.function_performed.prose)
                    for ap in u.authorized_privilege] or [],
                'functions': get_prop('functions', 'N/A')
            }
            for u in self.oscal.system_implementation.user
        ]

    @property
    def network_architecture(self):
        try:
            net = self.oscal.system_characteristics.network_architecture
            dia = net.diagram
            return dict(
                description=net.description.prose or "",
                caption=dia.caption.prose or "",
                diagram=get_prop(dia, 'plantuml', default=None, prose=True)
            )
        except Exception:
            return None

    @property
    def data_flow(self):
        try:
            net = self.oscal.system_characteristics.data_flow
            dia = net.diagram
            return dict(
                description=net.description.prose or "",
                caption=dia.caption.prose or "",
                diagram=get_prop(dia, 'plantuml', default=None, prose=True)
            )
        except Exception:
            return None

    @property
    def pps(self):
        pps = []
        components = self.oscal.system_implementation.component
        for c in components:
            if c.type.prose == 'service':
                for p in c.protocol:
                    for range in p.port_range:
                        pps += dict(
                            ports="{}/{}-{}".format(
                                range.transport,
                                range.start.prose,
                                range.end.prose
                            ),
                            protocols=p.name.prose,
                            services=p.title.prose,
                            purpose=p.prose or "",
                            component=c.title.prose
                        )
        return pps

    @property
    def interconnections(self):
        connections = []
        components = self.oscal.system_implementation.component
        for c in components:
            if c.type.prose == 'interconnection':
                poc = self.parse_party(
                    self.find_party(
                        self.find_party_from_role('isa-poc-remote')
                    )
                )
                connections += dict(
                    local_address=get_prop(
                        c, 'ipv4-address', prop_class='local'),
                    org=get_prop(c, 'service-processor', 'None'),
                    poc=poc,
                    security=get_prop(c, 'connection-security', 'None'),
                    direction=', '.join(get_prop(c, 'direction')),
                    information=get_prop(c, 'information'),
                    portnum="{}/{}".format(
                        get_prop(c, 'circuit', default=""),
                        get_prop(c, 'port', default="")
                    )
                )
        return connections

    def set_info(self, name, description):
        char = self.oscal.system_characteristics
        char.system_id = System_Id.System_Id(
            identifier_type=Identifier_Type.Identifier_Type(
                prose='https://ietf.org/rfc/rfc4122'),
            prose=createUUID()
        )
        char.system_name = System_Name.System_Name(prose=name)
        char.description = Description.Description(prose=description)
        info = self.oscal.system_characteristics.\
            system_information.information_type[0]
        info.uuid = Uuid.Uuid(prose=createUUID())
        info.title = Title.Title(prose=name)
        info.description = Description.Description(prose=description)

    def add_user(self, title, role_id=None, props=[]):
        u = System_User.User(
            uuid=Uuid.Uuid(prose=createUUID()),
            title=Title.Title(prose=title),
            role_id=Role_Id.Role_Id(prose=role_id)
        )
        self.oscal.system_implementation.user = u

    def add_component(
        self, title, description, type='component', status='operational'
    ):
        c = System_Component.Component(
                uuid=Uuid.Uuid(prose=createUUID()),
                type=Component_Type.Type(prose=type),
                title=Title.Title(prose=title),
                description=Description.Description(prose=description),
                status=Status.Status(state=State.State(prose=status)),
                prose=""
            )
        self.oscal.system_implementation.component = c

    @property
    def controls(self):
        controls = {}
        for imp in self.oscal.control_implementation.implemented_requirement:
            cid = imp.control_id.prose
            controls[cid] = []
            for comp in imp.by_component:
                controls[cid] += [{
                    'uuid': comp.uuid.prose,
                    'narrative': comp.description.prose
                }]
        return controls

    def add_control(
        self,
        component_id,
        control_id,
        narrative
    ):
        b = By_Component.By_Component(
            uuid=Uuid.Uuid(prose=createUUID()),
            component_uuid=Component_Uuid.Component_Uuid(prose=component_id),
            description=Description.Description(prose=narrative)
        )

        i = Implemented_Requirement.Implemented_Requirement(
            uuid=Uuid.Uuid(prose=createUUID()),
            control_id=Control_Id.Control_Id(prose=control_id),
            by_component=b
        )
        self.oscal.control_implementation.implemented_requirement = i
