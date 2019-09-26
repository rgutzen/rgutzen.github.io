* 15min

# Building a workflow for the analysis of slow wave activity across heterogeneous measurement
* This is a collaborative project by the people from the APE lab in Rome which you might recognize from the last talk and the INM-6 in Jülich.

# 1) Slow waves
* This project is also about slow waves. But since you just heard about slow waves, I here just mention again the key attributions
* Slow waves are slow, they are mostly within the theta range
* They are prominently present during anesthesia and sleep, which suggests a link to memory consolidation
* Most interesting for us, however, is that this is a phenomenon which can be consistently observed with different recording modalities and with different species.
* Here, you see figures taken from the last talk showing aspects of slow waves in calcium imaging, a model, and ECoG recordings.

* Having these very different angles to the analysis of slow waves, invites the question how to combine and integrate them into one coherent analysis and ultimately a coherent understanding of the phenomenon.

# 2) Collaboration of Use Case 3 (1min)
* This is the task we chose to tackle in the Use Case 2, or to use the more catchy name, the WaveScalEphant project.
* The project is the collaboration of Pier Paolucci's group in SP3, and Michael Denker and me from the HLST in SP5.
* From both sides we bring in our respective resources
## INFN: Data, Model, Pipeline
    * That is on one side the data. Which is Calcium Imaging and ECoG data from anesthetized mice. Although, originally the experiments were performed in Pavone's lab in Florence and Sanchez-Vives Lab in Barcelona.
    * And a model of slow waves, called WaveScalES, which is implemented both with the DPSNN simulator and the Nest simulator
    * The analysis pipelines
## FZJ: Methods, Implementation, Workflow design
    * On the other side, there is the further development and comparison of methods
    * And validation methodology
    * As well as the corresponding implementations for data handling and analysis.
    * And third, the workflow design to integrate together the various analysis, calibration, and validation elements.

# 3) Motivation (4min)
* There is a question which obviously imposes itself here: Why do we want to re-implement the analysis when there is already a working pipeline?
* The existing analysis is sufficient for the conducted research. It processes and analyses the data at hand and produces the results in the corresponding papers.
* So why would we want to revisit this analysis workflow, instead of focusing on the next new project?
* The thing with most analysis code is that it takes a long time to develop, and after the results are published it is typically not used again. Rarely within the same lab, and not at all outside it.
* One reason for this is, that the code is often very specific to the type of analysis, and the data format, and can not be easily reused for any other purpose than doing one specific analysis on one specific dataset.
* Another reason is also that while it is hard to write analysis code, it is even harder to read analysis code. So writing a new analysis often seems easier than to dig through the published code of someone else.
* I believe there is a lot of lost potential by the missing availability of analysis code in publications and missing reusability.
* This is especially true within the HBP, as it is one of our outspoken goals to develop and provide the infrastructure to enable the investigation of the big questions neuroscience.
* So I will lay out how these aspects are represented on the small scale of our project, and how we address them in practice.
* The aspects considered in our workflow design include:
    * Standard representations of data and results
    * Metadata enrichment
    * Standard algorithms and implementations
    * Modular and adaptable analysis steps
    * Provenance & explicit parameter settings
    * Generalization of analysis steps
* By taking care of these aspects we add value, which is manifested for example as:
    * Findability on the respective platforms (e.g. Knowledge Graph)
    * Accessibility of data and results, which includes sufficient documentation and metadata to make sense of it on its own
    * Interoperable link of data, metadata, and results
    * Reusable workflow elements
    * So these aspects basically describe the better reproducibility and reusability. But this reimplementation effort also allows us do something new, which is the bridging of scales within the same workflow, combining measurements from the neuron model with measurements from a population level!
* And by pure coincidence this spells out FAIR, well actually FAIRER

# 4) Tools (2min)
* So much about the Why. Let's now focus on the How, by briefly introducing the involved open-source tools.
* Neo
    * a structure to represent eletrophysiology data
    * generic enough to be used for various kinds of data and experiments
    * the data structure also directly includes and links the metadata
    * This is just a structure, and not a specific file format. It can be read and written with many different formats.
* Elephant
    * a tool which offer standard implementation for generic methods to analyze spike data as well as time series data such as LFP.
* Snakemake
    * snakemake is a workflow management tool which connects and organizes different workflow elements to make analysis more clearly arranged, reproducibility, and easily scalable, from a laptop to a cluster or a supercomputer.
* NetworkUnit
    * NetworkUnit is a framework and test suite to run model validations by evaluating and comparing the network activity

# 5) Reminder: Simulator Comparison (30s)
* Talking about NetworkUnit and validation, I insert here a short call back. I already showed this at the SP4 meeting in February, where some of you were.
* This illustrates the apparent differences of the WaveScalES model depending on whether this is run with the DPSNN or the Nest simulator.
* This should be a reminder to also include the simulator in the validation efforts.
* Ok, now back to our workflow

# 6) Workflow (7min)
* 1 Data types
* 2 Neo
* 3 Preprocess, ECoG Preprocess
* 4 elephant
* 5 Wave Detection, ECoG Wave Detection
* 6 Wave Processing
* 7 Caimg preprocess,
* 8 Caimg wave detection
* 9 caimg waveprocessing convergence
* 10 Simulation preprocess
* 11 simulation processing + convergence
* 12 Characterization
* 13-16 Comparisons arrows 4x (DPSNN/NEST)
* 17 Comparison
* 18 NetworkUnit
* 19 Snakemake
* 20 Caimg alt wave detection
* 21 LFP, EEG, Spikes
* 22 LFP processing
* 23 LFP wave processing
* 24 literature methods

* This is obviously not straight forward, but luckily we have the tools to make this more manageable. For the workflow, in particular snakemake. To dive deeper into this, I'll focus on the branch of the optical analysis.

# 7) Snakemake DAG
* Here, you see the dependency graph of the snakemake workflow which processes the optical raw data and calculates the velocity of occuring wavefronts.
* Each block is a script with an input and an output which is used as input for the next block.
* Additionally, there are explicitly all the parameter settings required for the analysis.
* As already show in the previous slide, there are the main steps of putting the data into the neo data structure, do the preprocessing, detecting the the transitions from down to up states indicating the wave fronts, and calculating the propagation velocity from that.

# 8) Results, Outlook, Scientific Questions (2min)
* To finally show some actual data, here is how the data and results look within these workflow steps
* In the raw images you might already see some activity, but it is hard to recognize
* So after the preprocessing, the wave behaviour becomes much more apparent
* By looking at the phase of the Hilbert transform, we can detect the transitions from down to UP states.
* This again represented in space enables the definition of wavefronts
* From which we can finally calculate characteristic measure such as the velocity, on which we can then base the validation and comparisons.

# 9) Outlook (next 6 month)
## Functionality
* Implementation of the wave characteristics
* parallel evaluation of the datasets
* multimodal validation of the model
## Scientific Questions
* As a disclaimer: We are not only doing all this purely out of good will for others to reuse these analysis elements. We also aim to employ this workflow to address some scientific questions of our own.
* Range of waves between cortical areas, characteristics!
* Relation to brain state
