# fmi-ls-struct
[![Build Specification](https://github.com/modelica/fmi-ls-struct/actions/workflows/build-ls-struct.yml/badge.svg)](https://github.com/modelica/fmi-ls-struct/actions/workflows/build-ls-struct.yml)

This repository contains a current prototype draft for the FMI Layered Standard for strtucturing of variables (fmi-ls-struct) based on the [Functional Mock-up Interface][FMI].

The goal of this layered standard is to  define semantic groups of variables to ease their access and presentation for the user. The idea of grouping is similar to the Terminals and Icons approach of FMI 3.0 (https://fmi-standard.org/docs/3.0/#fmiTerminalsAndIcons).

Use cases are:
* grouping of parameters and other variables which represent a look-up-table or a map inside the FMU. This grouping enables for example:
  * the importer to display the table in an user-friendly way,
  * to link it with A2L entities for XCP-based calibration (see https://github.com/modelica/fmi-ls-xcp),
  * to link the map parameters to various data sources
* grouping of parameters of certain devices in record-like structures to ease the parametrization of large models for the user alternatively to the usage of the structured naming convention.

The [FMI 3.0 Layered Standard for structuring of variables][spec] is currently maintained on [GitHub][githubspec] and is published [here][spec]. It is
based on the [FMI][] standard.

[FMI]: https://fmi-standard.org/
[githubspec]: docs/index.adoc
[spec]: https://modelica.github.io/fmi-ls-struct/main/
