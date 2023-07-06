# VCFParser

## Status

This project is in the early stages of development. The problem has been defined, and work is underway to devise an effective and efficient solution.

Please refer back to this README for updates as the project evolves.

## Overview

This project focuses on processing Variant Call Format (VCF) files, commonly used in bioinformatics to store gene sequence variations. The tool takes a VCF file, analyzes it according to provided parameters, and produces multiple output files each corresponding to a sample from the initial VCF file.

## Problem

The VCF file, which can contain a list of dozens to millions of genetic variants (mutations) from various samples, needs to be processed and split into separate VCF files per sample.

Each output file should contain:

- The VCF header as is.
- The VCF column line with the relevant sample's column.
- Variant lines present in that sample, filtered based on user-defined parameters for start and end positions and minimum depth (DP).
- An added subfield in the INFO column for each variant line, specifying the gene of that variant.

The processing should stop when reaching the end of the original VCF file, or after outputting the number of lines specified by the user in the limit parameter for each sample.

## Inputs and Outputs

The tool should accept the following inputs:

1. An optional start position.
2. An optional end position.
3. An optional DP.
4. A mandatory limit specifying the maximum number of output lines per sample.

The primary output of this tool will be a set of new VCF files named `<SAMPLE>_filtered.vcf`.

## Features

The main features of this project include parsing VCF files, processing and filtering genetic variants based on user-specified parameters, and producing formatted output files.

## Planning
![image](https://github.com/avivsarig/VCFParser/assets/97254290/c8870de5-c916-400f-8d43-4e33af5424fa)

