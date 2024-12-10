# JLCSC-Import-KiCad

## Description
Import components' symbol, footprint and model data to KiCad's project.

## Table of Content

## Progam Flow
1. go to project directory that store lots of kicad project
2. ask user to select kicad project
   - display all kicad projects and let user to choose one
3. ask user to input serial number
   - input serial number one by one
   - input txt / csv / json file to input all serial numbers
4. generate all necessary files
5.  generate csv / json file that contain info of all components that are included in different projects, such as name, serial number, path of its footprint...

## To-Do List
- [ ] Finish most basic functionalities (can import components to KiCad)
- [ ] Finish above functionalities
- [ ] Build GUI for above functionalities
- [ ] Build KiCad Plug-in

## Reference
 - [JLC2KiCad_lib](https://github.com/TousstNicolas/JLC2KiCad_lib)
 - [KiCad Footprint Generator](https://gitlab.com/kicad/libraries/kicad-footprint-generator)