# fmi-ls-struct
Layered standard for FMI for structuring of variables

The goal of this layered standard is to  define semantic groups of variables to ease their access and presentation for the user. The idea of grouping is similar to the Terminals and Icons approach of FMI 3.0 (https://fmi-standard.org/docs/3.0/#fmiTerminalsAndIcons).

Use cases are:
* grouping of parameters and other variables which represent a look-up-table or a map inside the FMU. This grouping enables for example:
  * the importer to display the table in an user-friendly way,
  * to link it with A2L entities for XCP-based calibration (see https://github.com/modelica/fmi-ls-xcp),
  * to link the map parameters to various data sources
* grouping of parameters of certain devices in record-like structures to ease the parametrization of large models for the user alternatively to the usage of the structured naming convention.
