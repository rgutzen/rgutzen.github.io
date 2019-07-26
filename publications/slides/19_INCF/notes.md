* 20min Talk
* reveal.js slides
* link to NetworkUnit tutorial
* publish slides on blog


# Evaluating neural network models within a formal validation framework

## 1) (4min)
### What can we learn from models?
* A model is an abstract formal description of a system, able to generate predictions
* What can we learn from models about the system it aims to describe?
* With models we can only learn by inductive inference (Hume: Induction problem)
* Thus, with modeling we can't and don't seek truth, but usefulness
### How can we learn from models?
* The quality of a model is only determined of the accuracy of its predictions
* Validation quantifies the prediction accuracy, and thus presents a measure of the quality i.e. the usefulness of a model

::: notes
* In neuroscience we have many many different models. For example neuron models. When we specify which neuron types and activity states we are interested in, validation enables us to evaluate how much trust we can put in each model.
* The other aspect of models besides its prediction accuracy, is its explanatory power (simplicity, correspondancy to physical measures), and models of course also differ in that regard, but this is not directly of interest for validation.

* Their main attribute is not only to adequately describe past observations but also to make testable predictions.
The accuracy of these predictions determines the trust we have in the model.
Think about two very common models:
There is the much trusted standard model in particle physics which is able to make immensely precise predictions which have been confirmed over and over again (e.g. Higgs-Boson, gravitational waves) and is probably the best model there is. This is why an violation of one of its predictions is likely related to groundbreaking new physics.
On the other hand there are for example meteorologic models which are also able to make very useful predictions, but as you know, every once in a while, the weatherforecast proves to be wrong. This does not mean that the underlying model is not useful but it reduces the confidence in the model predictions.
The reason we need to operate with terms as 'trust' or 'confidence' and can't just prove a model to be right is that the logic of modeling relies on inductive inference. Meaning that the model itself can only be falsefied but not verfied.
And since models can't be verified, we apply validation
:::

## 2) How can we learn from models? (3min)
* (Definition): Validation quantifies the prediction accuracy, and thus presents a measure of the quality i.e. the usefulness of a model

* Validation enables the evaluation and comparison of models, and is thus indispensable for rigorous and reproducible (simulation) science

::: notes
* introduce terminology
* give small example
* reproducible in a sense that changes in a model and additional influences (e.g. simulator engine) can be detected and measured
:::

## 3) Introduce validation (/substantiation) with reference model (2min)
* Explain interpretability
* acceptable agreement depends on the intended use
* Bottom-up vs. Top-down
* Explain applicability of M2M
	* compare version of same model
	* compare simulators
	* compare datasets
	* compare to already validated model
* Show example within workflow

## 4) Demonstrate the Network/SciUnit validation workflow (with exp. data) (3min)
* Explain role of elements (model, test, capability, score, data)
* Explain design principles and relations between elements
* Using a example of graph measures?

## 5) Application: Simulator comparison (3min)
* Substantiating neuromorphic hardware to C
* Take aways:
    * Validation testing enhances model(implementation) development
    * There is no hierarchy of failure
    * There is not single comprehensive test, so use many
* Result: qualitative reproduction, no equivalence, quantified level of agreement

## 5.5) Application: Comparison via wave dynamics
* Comparing DPSNN to NEST
* Comparing Wavescales to Ca+ Imaging data ?

## 6) Outlook: Validation Framework (2min)
* Searchable database of models, tests, and scores

## End (1min)
* refer to poster
* Link to NetworkUnit (tutorial)
* Link to Elephant
* Link to SciUnit
* Twitter handle

## to include somewhere
* difference between calibration and validation
* difference between bottom-up and top-down (cell-level, network-level) validation
* bottom-up espically prevalent in engineering context
