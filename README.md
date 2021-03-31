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

rectangle "pyOSCAL-Builder" as builder {
    card "1.0" as build_10
    card "1.1.0" as build_11
    card "1.1.1" as build_112
    card "2.0" as build_20
    build_10 --> build_11
    build_11 --> build_112
    build_112 --> build_20 
}

rectangle "pyOSCAL" as pyOSCAL {
    card "1" as pyoscal_1
    card "1.1" as pyoscal_2
    card "1.2" as pyoscal_3
    card "2" as pyoscal_4
    card "2.0.1" as pyoscal_5
    card "2.0.2" as pyoscal_6
    card "3" as pyoscal_7
    pyoscal_1 --> pyoscal_2
    pyoscal_2 --> pyoscal_3
    pyoscal_3 --> pyoscal_4
    pyoscal_4 --> pyoscal_5
    pyoscal_5 --> pyoscal_6
    pyoscal_6 --> pyoscal_7
}

nist_10 -[#green;bold]> build_10 
nist_10 -[#blue;bold]> build_11 
nist_11 -[#red;bold]> build_11 
nist_20 -[#purple;bold]> build_11
nist_20 -[#teal;bold]> build_112
nist_20 -[#orange;bold]> build_20

build_10 -[#green;bold]> pyoscal_1
build_11 -[#blue;bold]> pyoscal_2
build_11 -[#red;bold]> pyoscal_3
build_11 -[#purple;bold]> pyoscal_4
build_112 -[#teal;bold]> pyoscal_5
build_20 -[#orange;bold]> pyoscal_7

note left of pyOSCAL 
    - Major Version Changes when Major Version 
      of *Either* Nist or Builder increment 
    - Minor Version Changes when Minor Version 
      of *Either* Nist or Builder increment 
    - Build Number Increments when either Builder 
      has a build number change, or the pyOSCAL package changes
    - Meta Data in pyOSCAL will include all source module versions
endnote

@enduml
```