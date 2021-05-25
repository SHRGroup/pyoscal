# pyOSCAL-Builder

Python Script/Tool to create the pyOSCAL library from the NIST released MetaSchema

## Architecture

```plantuml
left to right direction

folder "OSCAL/src/metaschema" as metaschema
file "parse_meta.py" as parser
folder "pyoscal" as pyoscal
folder "oscal-content" as examples
file "unit_test.py" as unittest
component "objects" as pyobjects
file "Output XML" as output_xml
file "Class Diagram UML" as output_uml

metaschema --> parser
parser --> pyoscal : multiple classes
pyoscal -> unittest : import
examples --> unittest : parse examples
unittest <-> pyobjects
unittest --> output_xml
unittest --> output_uml
```

## Versioning 

Currently only using Master Branch until proper project cadence and Minimal Viable Product is achieved.

Below is the planned versioning methodology that will be used once tagged releases are established.

```plantuml 
scale .666
@startuml
left to right direction
rectangle "Nist-OSCAL" as Nist {
    card "1.0" as nist_10
    card "1.1" as nist_11
    card "2.0" as nist_20
    nist_10 --> nist_11
    nist_11 --> nist_20
}

rectangle "pyOSCAL" as pyOSCAL {
    card "1" as pyoscal_10
    card "1.1" as pyoscal_11
    card "2" as pyoscal_20
    card "2.0.1" as pyoscal_201
    card "2.0.2" as pyoscal_202
    pyoscal_10 --> pyoscal_11
    pyoscal_11 --> pyoscal_20
    pyoscal_20 --> pyoscal_201
    pyoscal_201 --> pyoscal_202
}


nist_10 -[#green;bold]> pyoscal_10
nist_11 -[#blue;bold]> pyoscal_11
nist_20 -[#red;bold]> pyoscal_20
nist_20 -[#red;bold]> pyoscal_201
nist_20 -[#red;bold]> pyoscal_202



note left of pyOSCAL 
    - Major Version Changes when Major Version 
      of *Either* Nist or PyOSCAL increment 
    - Minor Version Changes when Minor Version 
      of *Either* Nist or PyOSCAL increment 
    - Build Number Increments when the pyOSCAL package changes
    - Meta Data in pyOSCAL will include all source module versions
endnote

@enduml
```