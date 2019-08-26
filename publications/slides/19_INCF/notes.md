* 15min Talk
* 5min Discussion
* 20min Panel Discussion
* reveal.js slides

### Example
* Math. Model: Newton mechanics
* System oI: Appletree
* Simulation: pygame
* Verification: Checking code, using UnitTests
* Data: falling time for apples of different height
* Test: Throwing height test
* BaseTest: Throwing test (angle X)
* Capability: ProducesMovement
* Score: Effect Size

# Evaluating neural network models within a formal validation framework
* Work done by me and my colleges at the INM-6, Computational and Systems Neuroscience, at the research center Jülich
* I will talk about the concept and terminology of validation, how to employ this in the form of a software tool, and show its application to a quantitative simulator comparison

## 1) (2min)
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
* The other aspect of models besides its prediction accuracy, is its explanatory power (simplicity, correspondence to physical measures), and models of course also differ in that regard, but this is not directly of interest for validation.
:::

## 2) How can we learn from models? (1min)
* (Definition): Validation quantifies the prediction accuracy, and thus presents a measure of the quality i.e. the usefulness of a model

* Validation enables the evaluation and comparison of models, and is thus indispensable for rigorous and reproducible (simulation) science

::: notes
* introduce terminology
* give small example
* reproducible in a sense that changes in a model and additional influences (e.g. simulator engine) can be detected and measured
:::

## 3) Why is this not a trivial problem? (2min)
### Bottom-up vs. Top-down
* Validation of small scale elements does not entail agreement on larger scales!
* Validation on large scales does not entail agreement on small scales!
* -> Single-cell and network-level validation are complementary.
### Did the test, got a score, what now?
* A validation score is a quantitative measure of agreement
* Any single score can never reflect the entire range of features, environments, and statistics
* The interpretation depends on the model's intended use
### 'Validation' beyond validation
	* compare version of same model (for development, or quantifying influence of small changes)
	* compare to already validated model
    * compare simulators

::: notes
* Ok, in this conceptual framework, the workflow seems rather straight-forward: conceive and describe a (mathematical) model from observations and theory, implement it as an executable code, and compare the simulation outcomes to new observations.
* However, along the line of this basic workflow there are exceptions and additional aspects to consider which might become more relevant, the more complex the modeling and validation scenario becomes.
* The structure of the any corresponding software tool therefore should also reflect these aspects and be versatile enough to be able to adapt to the challenges of specific workflows.
* I will briefly mention 3 points which illustrate that validation is not a trivial problem.
* *1)* Approaches: Bottom-up vs. Top-down
    * In many engineering scenarios, the typical approach is to validate the elementary structures and iteratively build up to the validation of larger system. However, this is generally not possible in neuroscience. This has several reasons.
    * On the model side, the relations between scales of ion-channels, neurons, networks, and behavior are very complex and often unknown.
    * On the experimental side, corresponding multi-scale data is typically not available.
    * And additionally, the parameter regime of validation tests of e.g. single-cell does not necessarily reflect the relevant parameter space within the network dynamic.
    * Inferring single-cell validation from network-level validation also does not work, as has been shown for example by Potjans & Diesmann that large scale network dynamics can be accurately modeled by networks of simple LIF neurons, which are clearly not an accurate model.
    in software: ??
* *2)* Did the test, got a score, what now?
    * Outcome of a validation test is a score. This score quantifies how to update the credibility we ascribe to the model.
    * However, a single test can never evaluate all aspects of the model over the entire domain of interest. This has to be kept in mind when interpreting the result.
    * Generally, one should apply many different tests, evaluating different features, and using different statistical measures.
    * As you noted, a validation score is generally not a pass-or-fail assessment. This interpretation step highly depends on the intended use of the model (and also uncertainties of data and model). In an ideal case the modeler should formulate a priori an 'acceptable agreement' in which the score should lie to consider the test being passed.
    * in software: easy combination of test and score classes to build a range of tests
* *3)* 'Validation' beyond validation
    * Often you would like to validate a model, but lack an appropriate dataset to validate against, or have to little data to come to a strong conclusion. In these cases it is very helpful to instead validated against the simulation outcome of a more trusted model.
    * Such comparisons, although being practically identical, are not actual validation tests as they don't evaluate the predictiveness of the system of interest. But however, they can gather evidence that a model is reasonable, and identify and quantify limitations and deviation form other models.
    * What can also be helpful, is to compare a model not to another model but to another version of the same model. This can be used to evaluate incremental changes in model development or quantify the network-level influence of small tweaks in the model, like changing the ODE solver, or the underlying neuron model.
    * One of such changes could also be the choice of the simulator engine which used to run the model. As long as the simulators and the implementation is correct, the results should be identical, right? So, this comparison could practically 'validate' simulators.
    I will come back to this scenario and show a study of such a simulator comparison.
    * in software: M2M Test class

* So how should a software tool look like which is able to facilitate such various validation workflows, and ensure their replicability?
:::

## 4) Developing a network-level validation tool (5min)
* Explain role of elements (model, test, capability, score, data)
* Explain design principles and relations between elements
* Using a example of graph measures?

::: notes
* The first step when building a software tool is to check whether there exists already something like it. And indeed there is. The python package SciUnit provides a general framework for validating scientific models. So the tool we build for network-level validation, NetworkUnit, directly builds on that  
* we developed the Python package NetworkUnit which is based on the general scientific validation tool SciUnit.

* To be clear, this structure is largely provided by the underlying SciUnit package.
* The basic ingredients are the implementation model, and the experimental data.
* The model represented in a class object, which is able to run a simulation. If Newton would have been into coding, this would have written to test his formulas.
* In the most general case, the data may come in any form, as long as the associated test knows how to deal with it.
* For example the validation test here could test the velocity of a falling apple after a given distance.
* The test is as well a class object, which can compute the corresponding velocity values from the model simulation, and compare the two to generate the validation score object.
* Beside the quantitative validation outcome, the score object also has all the metadata from the model, the test, and the data. This enables not only the interpretation of the result but also its reproducibility.
* Besides aiding reproducibility, another design principle here is modularity. So the type of score is not hardcoded into the test, but attached via a ScoreType object (here we use an effect size, but could easily switch this to a student's t test or something else).
* Just as well as any parameter settings of the test.
* Consequently, there is an abstract test class implementation which is agnostic about the score type and the parameter settings, and therefore reusable for other test variation without the need to rewrite any code pieces.
* In the example of the apple this would be the falling velocity test. However, some scientist might also test the apple's velocity when thrown horizontally. Such a test has obviously some similarities and uses some of the same calculations as the falling test. Therefore, in order to code no calculation twice, there is then a another parent test class which implements the more general case of apple movement with arbitrary initial conditions.
* To give another example from network neuroscience. One typical base test would calculate correlations from neural activity, a derived child test could either directly compare the distribution of those, or could generate a corresponding weighted graph. This graph test would then be parent to various tests of graph centrality measures.
* Finally, this framework also ensures that a test against a particular model actually makes sense, via a capability object.
* Here, the capability the test makes use of is the movement of the apple, thus Newton's model simulation should have the capability to produce a movement to be evaluated.
* This modular structure is indeed versatile enough to easily incorporate the validation practice of comparing two models. This only requires only an additional inheritance of a dedicated test class.
This way, validation tests with experimental data and substantiation tests with models can be formally equivalent.
* In the apple example, Newton's model can be directly compared to a relativistic model of motion, and evaluate the domain in which Newton's model has a sufficient accuracy, without needing to measure very fast objects.
:::

## 5) Minimal code example


## 6.1) Application: Simulator comparison (4min)
* Substantiating neuromorphic hardware to C
* explain context of Izhikevich model and 3 papers

## 6.2) Application: Simulator comparison
* Employing the model on SpiNNaker with incremental improvements
* Quantify improvements via validation tests -> Validation testing enhances model(implementation) development

## 6.3) Application: Simulator comparison
* We found: Although there is a hierarchy of the statistical order of a tested measure, there is no hierarchy of failure. That means, a test of higher order (e.g. correlation coefficients) showing good agreement, does not imply agreement of tests of lower order (e.g. LV regularity)

## 6.4) Application: Simulator comparison
* There is not single comprehensive test, so use many
* Finally, good qualitative agreement, quantified via effect sizes
* However, no exact reproduction, especially when looks at spatio-temporal patterns
* Result: qualitative reproduction, no equivalence, quantified level of agreement

## 6) Outlook(1min)
* HBP Valiadtion Framework
    * Searchable database of models, tests, and scores
* Tests for wavedynamics
* other specialized validation test packages (NeuronUnit, HippUnit, etc.)

## End (1min)
* refer to poster
* Link to NetworkUnit (tutorial)
* Link to Elephant
* Link to SciUnit
* Twitter handle

## Discussion notes
* Besides the prediction accuracy, there is another aspect to the overall quality of a model, it's explanatory power. ...
see also [Why model? by Joshua Epstein 2008](http://jasss.soc.surrey.ac.uk/11/4/12.html)
* Prediction does not imply explanation and explanation does not imply prediction

* Quality = Predictiveness + Explantory power + (Contextuality)
* Validation evaluates predictiveness
* Qualification/Confirmation evaluates explantory power ??
* M2M evaluates contextuality ??

* Calibration vs. Validation
* A main part of the scientific work is the formulation of the expected agreement. To determine which aspects of the network dynamics are the relevant features the model should produces.

* Why use Izhikevich model, when we know that it is false (groups are artifacts)
