"""
Accurately assemble sequence using DNA reads generated by Oxford Nanopore flow cells as input.
"""

from latch.types import LatchDir, LatchFile
from latch import workflow, large_gpu_task
from .config import Configuration
from pathlib import Path
import subprocess
import os


@large_gpu_task
def batch_assembly_task(
    input_dir: LatchDir,
    input_file: LatchFile,
    config: Configuration,
) -> (LatchFile, LatchFile):
    """
    Run shasta on the input directory.
    """

    log_file = Path(f"/root/logfile.txt")
    output_dir = Path(f"/root/ShastaRun/")
    assembly_file =  Path(f"{output_dir}/Assembly.fasta")

    _assembly_cmd = [
        "./shasta", 
        "--input", 
        str(Path(input_file).resolve()), 
        "--config", 
        str(config.value),
        "--assemblyDirectory",
        str(output_dir),
    ]

    # _test_cmd = [
    #     "head",
    #     "-n",
    #     "1",
    #     str(Path(input_file).resolve()),
    # ]

    with open(log_file, "w") as f:
        subprocess.run(_assembly_cmd, stdout=f, stderr=f)

    return (
        LatchFile(str(log_file), f"latch://{log_file}"),
        LatchFile(str(assembly_file), f"latch://{assembly_file}"),
    )


@workflow
def shasta(
    input_dir: LatchDir,
    input_file: LatchFile,
    config: Configuration = Configuration.nano_may_22,
) -> (LatchFile, LatchFile):
    
    """Description...

    # Shasta long read assembler
    ___

    **The complete user documentation is available [here](https://chanzuckerberg.github.io/shasta/).**

    **For quick start information see [here](https://chanzuckerberg.github.io/shasta/QuickStart.html).**

    See [Shafin et al., Nature Biotechnology 2020](https://www.nature.com/articles/s41587-020-0503-6)
    for error analysis of the Shasta assembler and more.
    Reads from this paper are available 
    [here](https://s3-us-west-2.amazonaws.com/human-pangenomics/index.html).
    The assembly results are
    [here](https://s3-us-west-2.amazonaws.com/human-pangenomics/index.html?prefix=publications/SHASTA2019/assemblies/).

    [Here](https://github.com/human-pangenomics/assembly-analysis) is a QUAST analysis of a Shasta assembly of CHM13 
    and a comparison with other assemblers.

    **Requests for help:** please file GitHub issues to report problems, request help, or ask questions. **Please keep each issue on a single topic when possible.** 
    ___

    The goal of the Shasta long read assembler is to rapidly 
    produce accurate assembled sequence using DNA reads
    generated by [Oxford Nanopore](https://nanoporetech.com) flow cells as input.

    Computational methods used by the Shasta assembler include:

    * Using a
    [run-length](https://en.wikipedia.org/wiki/Run-length_encoding)
    representation of the read sequence.
    This makes the assembly process more resilient to errors in
    homopolymer repeat counts, which are the most common type
    of errors in Oxford Nanopore reads. 

    * Using in some phases of the computation a representation
    of the read sequence based on *markers*, a fixed
    subset of short k-mers (k ≈ 10).

    As currently implemented, Shasta can run an assembly 
    of a human genome at coverage around 60x
    in about 3 hours using a single, large machine (AWS instance type
    `x1.32xlarge`, with 128 virtual processors and 1952 GB of memory).
    The compute cost of such an assembly is around $20 at AWS spot market or reserved prices.

    Shasta assembly quality is comparable or better 
    than assembly quality achieved by other long read assemblers -
    see [Shafin et al., Nature Biotechnology 2020](https://www.nature.com/articles/s41587-020-0503-6)
    for an extensive analysis.
    However,
    **adjustments of assembly parameters are generally necessary** to 
    achieve optimal assembly results. 
    A set of sample configuration files is provided (in the `conf` directory)
    to assist with this process.



    #### Acknowledgments

    The Shasta software uses various external software packages.
    See [here](https://chanzuckerberg.github.io/shasta/Acknowledgments.html) for more information.

    #### Reporting Security Issues
    Please note: If you believe you have found a security issue, please responsibly disclose it by contacting security@chanzuckerberg.com.
    ___

    **The complete user documentation is available [here](https://chanzuckerberg.github.io/shasta/).**

    **For quick start information see [here](https://chanzuckerberg.github.io/shasta/QuickStart.html).**
    ___



    __metadata__:
        display_name: De novo assembly from Oxford Nanopore reads 
        author:
            name: Chan Zuckerberg Initiative
            email: security@chanzuckerberg.com
            github: https://github.com/chanzuckerberg/shasta
        repository:
        license:
            id: MIT

    Args:

        input_dir:
          Input FASTA/FASTQ file directory

          __metadata__:
            display_name: Input Directory

        input_file:
          Input FASTA/FASTQ file

          __metadata__:
            display_name: Input File

        config:
          Configuration Preset

          __metadata__:
            display_name: Configuration
    """
    
    # demo for now
    return batch_assembly_task(
        input_dir=input_dir,
        input_file=input_file, 
        config=config,
    )
