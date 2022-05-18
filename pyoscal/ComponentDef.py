from .core.oscal_component_definition import (
    Component_Definition, Defined_Component, Control_Implementation,
    Implemented_Requirement, Uuid, Incorporates_Component
)
from .core.oscal_component_definition import Capability as oscal_capability

from .core.oscal_implementation_common import (
    Component_Type, Description, Control_Id, Title,
    Source, Name, Component_Uuid, Protocol, Start, End,
    Port_Range, Transport
)
from .core.oscal_metadata import (
    Metadata, Last_Modified, Version, Oscal_Version, Oscal_Property, Value
)
from .core.oscal_metadata import Title as metaTitle
from .OSCAL import Oscal
from .core.OSCAL import OSCAL as core
from .common import getToday, createUUID


class ComponentDefinition(Oscal):

    def __init__(
        self,
        title="",
        description="",
        version=getToday(fmt='day'),
        oscal_version=getToday(),
        last_modified=getToday(),
        uuid=createUUID(),
        data=None,
        obj=None
    ):

        if obj:
            self.oscal = obj
            return

        if data is None:
            data = []
        props = [
            Oscal_Property.Prop(
                name=Name.Name(prose=k),
                value=Value.Value(prose=v)
            ) for k, v in data
        ]

        self.title = title
        self.uuid = uuid

        metadata = Metadata.Metadata(
            title=metaTitle.Title(prose=title),
            last_modified=Last_Modified.Last_Modified(prose=last_modified),
            version=Version.Version(prose=version),
            oscal_version=Oscal_Version.Oscal_Version(prose=oscal_version),
            oscal_property=props
        )

        self.oscal = Component_Definition.Component_Definition(
                uuid=Uuid.Uuid(prose=uuid),
                metadata=metadata
            )

    @classmethod
    def from_file(cls, filepath):
        new = cls()
        oscal = core()
        new.oscal = oscal.parse_file(filepath)
        new.title = new.oscal.metadata.title.prose
        new.uuid = new.oscal.uuid.prose
        return new

    @classmethod
    def from_string(cls, content):
        pass

    @property
    def description(self):
        capabilities = self.oscal.capability
        if isinstance(capabilities, list):
            cap = capabilities[0]
        else:
            cap = capabilities
        try:
            return cap.description.prose
        except Exception:
            return ""

    @property
    def component_type(self):
        for prop in self.oscal.metadata.oscal_property:
            if prop.name.prose == 'type':
                return prop.value.prose
        return "unknown"

    def get_controls(self):
        controls = []
        for capability in self.oscal.capability+self.oscal.component:
            for cimp in capability.control_implementation:
                for impreq in cimp.implemented_requirement:
                    controls += [{
                        'control_id': impreq.control_id.prose,
                        'narrative': impreq.description.prose,
                        'props': [(p.name.prose, p.value.prose, p.prose)
                                  for p in impreq.oscal_property]
                    }]
        return controls

    def add_pps(self, services):
        for service in services:
            protocols = services[service]
            component = Component(
                type='service',
                title=service
            )
            for proto_key in protocols:
                protocol_obj = Protocol.Protocol(
                    name=Name.Name(prose=proto_key)
                )
                for range in protocols[proto_key]:
                    if '-' in str(range['ports']):
                        start, end = range['ports']
                    else:
                        start = end = str(range['ports'])
                    p_range = Port_Range.Port_Range(
                        start=Start.Start(prose=start),
                        end=End.End(prose=end),
                        transport=Transport.Transport(prose=range['transport'])
                    )
                    protocol_obj.port_range = p_range
                component.oscal.protocol = protocol_obj
            self.oscal.component = component.oscal

    def add_component(
        self, component
    ):
        self.oscal.component = component.oscal

    def add_capability(
        self, capability
    ):
        self.oscal.capability = capability.oscal


class Capability:

    def __init__(
        self,
        name,
        uuid=createUUID(),
        description=""
    ):

        self.oscal = oscal_capability.Capability(
            uuid=Uuid.Uuid(prose=uuid),
            name=Name.Name(prose=name),
            description=Description.Description(prose=description)
        )

    def add_component(self, component_uuid, description=""):
        self.oscal.incorporates_component = \
            Incorporates_Component.Incorporates_Component(
                component_uuid=Component_Uuid.Component_Uuid(
                    prose=component_uuid
                ),
                description=Description.Description(
                    prose=description
                )
            )

    def add_control(
        self,
        controlid,
        narrative="",
        props=[]
    ):
        control = Control()
        control.oscal.implemented_requirement = [
            Requirement(
                controlid,
                description=narrative,
                props=props
            ).oscal
        ]
        self.oscal.control_implementation = control.oscal


class Component:

    def __init__(
        self,
        title,
        uuid=None,
        type='generic',
        description="",
        controls=[]
    ):

        if uuid is None:
            uuid = createUUID()
        self.uuid = uuid

        self.oscal = Defined_Component.Component(
            title=Title.Title(prose=title),
            uuid=Uuid.Uuid(prose=uuid),
            type=Component_Type.Component_Type(prose=type),
            description=Description.Description(prose=description)
        )

    def add_control(
        self,
        controlid,
        narrative=""
    ):
        control = Control()
        control.oscal.implemented_requirement = [
            Requirement(
                controlid,
                description=narrative
            ).oscal
        ]
        self.oscal.control_implementation = control.oscal

    def add_property(
        self, name, value
    ):
        property = Oscal_Property.Prop(
            name=Name.Name(prose=name),
            value=Value.Value(prose=value)
        )
        self.oscal.oscal_property = property


class Control:

    def __init__(
        self,
        uuid=createUUID(),
        description="",
        requirements=[],
        source='NIST_SP-800-53_rev4_catalog.xml'
    ):

        self.requirements = [r.oscal for r in requirements]
        self.oscal = Control_Implementation.Control_Implementation(
            uuid=Uuid.Uuid(prose=uuid),
            source=Source.Source(prose=source),
            description=Description.Description(prose=description),
            implemented_requirement=[r.oscal for r in requirements]
        )


class Requirement:

    def __init__(
        self,
        controlid,
        uuid=createUUID(),
        description="",
        props=[]
    ):

        self.oscal = Implemented_Requirement.Implemented_Requirement(
            uuid=Uuid.Uuid(prose=uuid),
            description=Description.Description(prose=description),
            control_id=Control_Id.Control_Id(prose=controlid)
        )
        for prop in props:
            name, value, content = prop
            p = Oscal_Property.Prop(
                name=Name.Name(prose=name),
                value=Value.Value(prose=value),
                prose=content
            )
            self.oscal.oscal_property = p
