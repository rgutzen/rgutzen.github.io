* 15min

# Building a workflow for the analysis of slow wave activity across heterogeneous measurement

# 1) Slow waves
* short intro to phenomenon
* 0.5 - 4 Hz

# 2) Collaboration of Use Case 3 (1min)
## INFN: Data, Model, Pipeline
    * Ca+Imaging data of anesthetized mice (ketamin)
    * ECoG data of anesthetized mice
    * Spiking Model WaveScalES (DPSNN, NEST)
    * Slow Wave Analysis Pipeline SWAP
## FZJ: Methods, Implementation, Workflow design
    * Methods
    * Implementation
    * Workflows

# 3) Tools (2min)
    * Neo
    * Elephant
    * NetworkUnit
    * Snakemake

# 4) Motivation (4min)
* Why re-implement the analysis when there is already a pipeline?
* The existing analysis is sufficient for the conducted research. It processes and analyses the data at hand and produces results which are of interest for the scientific questions around slow waves. Corresponding papers are published (or are about to be). So why would we want to revisit this analysis workflow, instead of focusing on the next new project?
* The thing with most analysis code is that it takes a long time to develop, and after the results are published it is typically not used again. Rarely within the same lab, not at all outside it.
* One reason for this is, that the code is often very specific to the type of analysis, a narrow scientific question, and the data format, and can not be easily reused for any other purpose than doing one specific analysis on one specific dataset.
* Another reason is also that while it is hard to write analysis code, it is even harder to read analysis code. So writing a new analysis often seems easier than to dig through the published code of someone else.
* I believe there is a lot of lost potential of focusing only on on making the final results of a study available.
* There is now an evolving trend of also publishing datasets. A similar effort needs to be made with respect for the methods and the workflows used in the processing and analysis of data.
* This is especially true within the HBP, as it is one of our outspoken goals to develop the infrastructure and the tools to enable the investigation of the big questions neuroscience.
* Bridging of scales!
* I will lay out how these as aspects are represented on the small scale of this collaboration, and how we address them in practice.
* Workflow aspects
    * Standard representations of data and results
    * Standard algorithms and implementations
    * Modular and adaptable analysis steps
    * Provenance and explicit parameter settings
    * Quantitative methods for characterization/ calibration/ validation
* Added value
    * Findable on Neuroinformatics platforms (Knowledge Graph)
    * Accessibility of data and results
    * Interoperable
    * Reusable analysis elements
    * Interpretable results (metadata)
    * Generalization of the analysis
    * Quantitative evaluation of models/ data/ simulators

# 4) Workflow (7min)
## Ca-Img processing

## (ECoG processing)

## Simulation
* Ref. to Simulator comparison shown in SP4 meeting in February

## Wave measures + Validation

# 5) Results, Outlook, Scientific Questions (2min)
## Preliminary results

## Outlook (next 6 month)

## Scientific Questions
* As a disclaimer: We are not only doing all this purely out of good will for others to reuse these analysis elements. We also aim to employ this workflow to address some scientific questions of our own.
* Range of waves between cortical areas, characteristics!
* (Relation of slow waves to spiking patterns)
* Relation to brain state
* Occurrence in different frequency domains
