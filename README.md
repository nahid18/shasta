# Shasta workflow

## Workflow on [LatchBio](https://latch.bio)
Access here: https://console.latch.bio/explore/60363/info

![Interace](./interface.png)

## About Shasta
The goal of Shasta is to rapidly produce accurate assembled sequence using as input DNA reads generated by [Oxford Nanopore](https://nanoporetech.com) flow cells.

Computational methods used by the Shasta assembler include:

- Using a [run-length](https://en.wikipedia.org/wiki/Run-length_encoding) representation of the read sequence. This makes the assembly process more resilient to errors in homopolymer repeat counts, which are the most common type of errors in Oxford Nanopore reads.
- Using in some phases of the computation a representation of the read sequence based on markers, a fixed subset of short k-mers (k ≈ 10).


## Links
- Configuration Presets: https://github.com/chanzuckerberg/shasta/tree/master/conf
- Source Code: https://github.com/chanzuckerberg/shasta
- Documentation: https://chanzuckerberg.github.io/shasta

## How to cite
- Paper: https://www.nature.com/articles/s41587-020-0503-6
- Acknowledgements to external packages: https://chanzuckerberg.github.io/shasta/Acknowledgments.html
