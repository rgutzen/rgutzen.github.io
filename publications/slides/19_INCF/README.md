
# Content Curator Materials

## About

   This repository contains materials for preparing content curators for their
   job in the institute. Since Curators are expected to rotate on a yearly
   basis, these materials should be updated and prepared by the current
   curators to best explain their job to the next generation.


## How to build

   To see the materials in formats other than their source markdown you mainly
   need to have Snakemake and pandoc installed. Some output formats require
   additional software such as pdflatex to be available. If you have a \*conda
   flavour installed you can use the `environment.yaml` to have all tools
   installed in a dedicated environment. Just run

    conda env create -n curation -f environment.yaml
    conda activate curation

   Then the whole process of building the different output formats is
   acomplished by the Snakemake workflow. Run

    snakemake

   To change the produced output formats modify the input section of the `done`
   rule in `Snakefile`. Be aware that some formats may need addional files that
   might not be in the repository yet. Not all output formats are useful or
   were tested.

