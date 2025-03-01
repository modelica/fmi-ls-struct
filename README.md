# FMI Layered Standard for Structured Data
[![Build Specification](https://github.com/modelica/fmi-ls-struct/actions/workflows/build-ls-struct.yml/badge.svg)](https://github.com/modelica/fmi-ls-struct/actions/workflows/build-ls-struct.yml)

This repository contains a current prototype draft for the FMI Layered Standard for Structured Data (fmi-ls-struct) based on the [Functional Mock-up Interface][FMI].

Based on FMI 3.0, this layered standard defines how variables (especially parameters) of an FMU can be structured and grouped in a more flexible way than with the "structured naming convention" of the FMI Standard. The first version of this layered standard is focused on the definition of sampled maps.

The [FMI 3.0 Layered Standard for structuring of variables][spec] is currently maintained on [GitHub][githubspec] and is published [here][spec]. It is
based on the [FMI][] standard.

## News

Dive into our latest video ["FMI, Layered Standards and ASAM Standards - Enabling Seamless SiL Simulation of Virtual ECUs"](https://www.youtube.com/watch?v=KzzKRa3jORs).
Discover how the cutting-edge FMI 3.0 standard and the layered standards based on it are revolutionizing the world of Software-in-the-Loop (SiL) simulations.

During the presentation the three new layered standards for simulating virtual ECUs with FMI 3.0 are introduced:

- FMI-LS-XCP for measurement & calibration with XCP
- FMI-LS-BUS for simulation of network communication with CAN, CAN FD CAN XL, FlexRay, Ethernet, LIN
- FMI-LS-STRUCT for structured entities like lookup tables

After this a demo from different SiL tool vendors (Akkodis, Altair, AVL, Bosch, dSPACE, PMSF, SYNOPSYS) illustrates the interoperability of these layered standards.

## Repository Structure

- `docs` -- Sources of the specification document
- `schema` -- XSD schema for this FMI Layered

## Copyright and License

Code and documentation copyright (C) 2024 The Modelica Association Project FMI.
Code released under the [2-Clause BSD License].
Docs released under [Attribution-ShareAlike 4.0 International].

[FMI]: https://fmi-standard.org/
[githubspec]: docs/index.adoc
[spec]: https://modelica.github.io/fmi-ls-struct/main/
[2-Clause BSD License]: https://opensource.org/licenses/BSD-2-Clause
[Attribution-ShareAlike 4.0 International]: https://creativecommons.org/licenses/by-sa/4.0/
