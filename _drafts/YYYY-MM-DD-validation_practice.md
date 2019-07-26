---
layout: post
title: Practice of validation
subtitle: 3 things to consider when validating
tags: [validation, essay]
<!-- bigimg: -->
imgage:
share_img:
comments: false
social-share: true
<!-- css: -->
<!-- ext-css: -->
<!-- js: -->
<!-- js-ext: -->
googlefonts: ["Roboto", "Lobster"]
<!-- gh-reop: -->
<!-- gh-badge: -->
---
<!-- ToDos:
simulator - simulator engine
proofread, blogyfy
ref -> links -->

## Validating while Model-Building?
Validation provides precise statements about differences of simulation results and
observation and therefore builds the connection between the theory-driven, mathematical world of model building and the very practical evaluation of reality in form
of experiments. This makes validation a powerful tool for both experimentalists and
theoreticians. The experimentalists may be given suggestions and incentives where
to look and what to measure. For the theoreticians, validation makes it possible to
improve their ability to make accurate predictions by providing feedback about how
well the predictions match reality.
Testing model predictions by validation is one use of experimental data in model
development. Another use, which has to be strictly distinguished, is calibration.
Model development always takes inspiration and insights from experimental findings, but calibration refers more specifically to the use of a particular data set in
order to tune parameters of the model. Although this is a legitimate technique, it
has to be distinctly separated from validation. Validation shall never result in the
adaption of the model the way it is done for calibration, otherwise the model would
compromise its predictiveness. Consequently, models which were calibrated by use
of a particular data set require a second different data set to perform a validation
test (Thacker et al., 2004). For the model development this means that the detailed
knowledge of the validation results should not dictate the further development direction of the model, for example by tuning parameters to improve the validation
results. To illustrate this, we could a imagine a network model which is validated
against an experimental measurement, and fails the validation test. A test shows that
the firing rates are a lot smaller in the model simulation than in the measurement.
Knowing this result and thereupon increasing firing rates in the model to improve
the test result would be considered a calibration. In contrast to that, a proper revision
of the model in reaction to the failed test would then involve only changes a modeler would make who does not know how and why the validation test failed. These
changes could also include increasing the firing rates but due to other motivations.
Effectively, this then forms a continuous and iterative process in which the model
is continuously improved. The ongoing successful validation of a model can then
not only increase the confidence in the hypothesis on which the model was build,
but may also allow the model to draft more and more specific predictions which
may lead to the formulation of new hypotheses.

## Bottom-Up or Top-Down Validation?
When speaking of validation in the context of neuroscience, most of the time what is
meant or understood is the validation of the simulation of single neuron responses
or synapse behavior, e.g. to current injection (e.g. as done for the model presented
in Markram et al. (2015)). This is the typical bottom-up validation approach which
is based on the reasoning that when the basic building blocks of a system work appropriately the resulting system (or subsystem) combining many of the validated
building blocks should consequently also work appropriately. The validation of
the entire system would be applied only if all previous validation tests of the subelements were passed. This validation approach is also predominantly practiced in
engineering. While this approach certainly has its place in neuroscience, in contrast
to engineering, the link from the function of the smallest elements to the function
of larger composite systems is not well understood (to a large degree due to a lack of data and system complexity). Therefore, it is not as trivially possible as in many
engineering scenarios to build up the validation of models from its basic elements to
the larger scale system. This is especially true when considering that the modeling
of these elements (neurons and synapses) is usually very much simplified compared
to their biological example.
The enormous complexity of biological neural networks can not yet be adequately described and modeled (O’Reilly et al., 2012). This combined with the fact
that it is also not yet entirely clear which exact features of neurons and synapses
are essential for the functionality of the network makes the bottom-up validation
approach unfeasible in many neuroscience contexts.
A different, and more flexible approach would be the top-down validation, meaning to validate the network behavior first against the reality of interest before one
may look onto the smaller scales. This network level validation enables a much
quicker check of the desired network properties by disregarding how they may form
from underlying mechanisms. Thus, network models with very different premises
may be compared and validated equivalently. For example, the same validation test
may be applied to a very abstract rate-neuron based simulation model as well as to
a model based on a more biological reasonable model of spiking neurons. This can
directly contribute to the question which of the numerous features of a neuron are
actually relevant for the tested network behavior.
Another important application scenario for top-down validation are models which
are themselves designed in a fashion which could be described as ’top-down’. There
exist many models of large networks which use very simplistic neuron and synapse
models (e.g. Potjans & Diesmann, 2014). Because the focus of such models mostly
lies on the macroscopic parameters such as the ratio of inhibitory and excitatory
neurons, in-/out-degree distributions, or connectivity probabilities, they could not
be solely validated bottom-up.

## Validating Models with Models?
So far we employed the understanding that a model validation relies on the comparison to the reality of interest which is typically represented by a measurement in
an experimental setup. However, there are special validation scenarios in which it
makes sense to instead compare the model at hand to another model, another implementation of the model, or a different simulation run of the model.
First, there is the scenario which may be called simulator validation. The implementation of a model is usually fit to a specific simulator. Thus, the question arises
to what degree the choice of a simulator has an influence on the simulation outcome. Fortunately, there are efforts to overcome the simulator specificity, for example in form of the simulator independent modeling language PyNN (Davison et al.,
2008). Neural network models described in PyNN can be simulated using a variety
of simulators because PyNN provides a reliable translation from an abstract model
description to the simulator specific model configurations. While this does not solve
the issue of unknown, unwanted influences of the simulator, it provides a possibility to easily investigate it. In the framework of validation a particular simulator
specific model can often be seen as the abstraction of a more exact or more detailed
simulator implementation of the same model (i.e by using approximations of numerical solutions, different solver of differential equations, ...), just as the model itself is
an abstraction of reality. The comparison of such a simulator specific model to another which is known to be (more) accurate (and at best has itself been validated against experimental data) is therefore also a validation. This, however, should not
be confused with the validation of the model used for the simulator validation. The
validation of the model itself still requires experimental data.
Another application of a model-to-model validation is the checking of the consistency of the model. The simulation of a network model is usually stochastic in
one way or another. Typical source of stochasticity are usually a driving input, and
the initial connectivity, weights, and delays which are usually drawn from some
probability distribution. Therefore, two simulations of the same model do not have
the exact same outcome. A validation test comparing two simulations of the same
model can thus validate that a feature, that the test tests for, is actually emerging
from the model and not from an artifact. Furthermore, the simulation should react
appropriately to a reasonable change in a model parameter. Model parameters motivated from experimental observation are not arbitrarily precise and therefore have a
range in which they may be varied without causing a drastic change in the network
behavior. Testing the model against a slightly different version of the model thus
validates that the model is generally consistent (e.g. showing non-chaotic responses
to variation of parameters). Within the framework of validation the consistency and
appropriate dependency on small parameter changes can be seen as abstract properties of the reality. Testing such properties of the model can therefore be seen as a
validation although the model is tested against a version of itself instead of a measurement.
Lastly, a model-to-model validation may also be useful for accompanying the
model development. Testing a model against experimental data is more difficult
than testing against simulation data because experimental data is much more limited
both in quantity and specificity. Thus, when improving an existing model it is of
course necessary to rerun all the previous validation tests but this can be greatly
extended by model-to-model validation. A test comparing the improved model to
the previous version of the model can validate that the change in the model does
in fact only cause the desired changes in the network behavior and therefore can
enhance the overall confidence in the model.
These three scenarios should motivate the use of validation beyond its usual application on experimental findings. However, this is only reasonable to do in special
cases and always has to be carefully phrased and interpreted to not be confused
with the regular validation. In Chapter 6 the idea of model-to-model validation is
picked up for the validation of a neuromorphic system as a simulator against an
exact reference implementation of the model
