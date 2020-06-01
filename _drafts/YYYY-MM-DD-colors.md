---
layout: post
title: Lifting the Purple Haze
subtitle: Part I - Understanding Color Spaces and Perception (for Data Visualization)
tags: [essay]
<!-- bigimg: -->
image:
share-img:
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

<!-- subtitle: Part II: Understanding Color Palettes and Perception (for Data Visualization) -->

<!--
ToDo:
* Subtitle
* bigimg
* image & share-img
* check pronouns I, we, ...
* check how reader is addressed (you, indirect, ...)
-->

Colors matter. Colors are a considerable part of aesthetics, and aesthetics facilitate engagement. Colors can convey meaning and guide the reader's focus. Colors help the intuitive understanding of your visualization.

In the following, I will explain how color spaces work. I will dip into some physiological and psychology background, illustrate what distinguishes a good and a bad color palette, and link some helpful tools to select colors and build palettes.
There might be some digressions along the way, but there will be a summary of the relevant take-aways at the end.

- [What do we mean by Color?](#what-do-we-mean-by-color)
- [Color Spaces]()
    - [Primary Color Spaces: RGB and CMYK](#primary-color-spaces-rgb-and-cmyk)
    - [The Color Wheel: Hue](#the-color-wheel-hue)
    - [Cylindrical Color Spaces: HSL, HSV, HSB, HSI](#cylindrical-color-spaces-hsl-hsv-hsb-hsi)
    - [Color Perception: Part I](#color-perception-part-i)
    - [CIE Chromaticity Diagramm](#cie-chromaticity-diagramm)
- [Color Palettes]()
    - [Pitfalls of Palettes: JET](#pitfalls-of-palettes-jet)
    - [Choosing the right Palette](#choosing-the-right-palette)
    - [Color Perception: Part II](#color-perception-part-ii)
    - [Choosing the right Colors](#choosing-the-right-colors)
- [Resources]()
    - [Helpful Tools](#helpful-tools)
    - [Examples](#examples)
    - [References and Further Reading/Listening](#resources-and-further-readinglistening)

## What do we mean by Color?
<!-- #### Color is multi-phenomenological -->
There are two very common approaches to color. One is to look at the color spectrum in which the light colors are arranged by their wavelength, like a rainbow. The other is to start with some primary colors (red, green, blue, for example) and construct other colors via additive color mixing.
These approaches like other alternatives have distinct differences and influence how we think about color and how we represent it. The best system of representing and thinking about color depends highly on the application, on the editing mediums (paint palettes, lamps, digital software, ...), the display medium (screens, paper, ...), the intended observer (humans with or without color deficiencies, honeybees, octopuses, ...), and purpose (artistic, informative, signaling, ...).
<br>
The reason that there is such an ambiguity about color is that it is not purely a physical property, i.e., a wavelength, but also a property of physiological perception, psychological interpretation, and eventually subjective experience (in philosophy termed _'Qualia'_). Here, we will try to shine some light on at least the first three aspects.

<!-- #### Colors are mixable -->
We begin with a very basic but fundamental observation. Every color we see, we perceive as a singular individual color. Even a 'greenish blue' is its own color which we merely describe by referencing other colors. We see a color the same way independent of whether it was mixed or presented as a single monochromatic source. We don't see that this <span style="color:orange">yellow</span> is created by red and green pixels.
In fact, the number of wavelengths and light sources mixed together has no influence on the color we perceive. Our eyes and brain combine the incoming wavelengths to a single color impression. This is evolution's answer to increasing the number of perceivable colors (estimated 2 Mio [ref]) without requiring the same amount of color-specific photosensitive cells.
<br>
Conveniently, that is also the reason why color spaces like RGB work in the first place. With only three colors, all hues of the spectrum can be recreated by mixing (why hues and not colors will be addressed later). How to mix the primary colors to get the full spectrum is described by the so-called color matching functions. Why exactly 3? Humans have trichromatic vision, meaning they have three kinds of color sensitive cells (S, M, and L cones), thus, it requires three dimensions to represent the visible color spectrum.
<br>
The question of interest is which dimensions to choose to represent the spectrum best. As mentioned above, this depends largely on the application. Similar to coordinate transformations in physical space, choosing the adequate dimensions can make descriptions much easier to handle.
Although we will go through various descriptions here, we are ultimately interested in designing color palettes for data visualization to be consumed by humans on screens or paper.

> __Note:__
Although not directly visible for the naked eye it is still relevant to build white light sources which cover the whole spectrum of colors, because objects can of course only appear in their own color when that color is present in the light they are illuminated in. Additionally, some wavelengths also play other roles than just in color perception. Plants mostly need the red and blue wavelength for photosynthesis; the production of the sleepiness hormone Melatonin is most efficiently suppressed by particular blue wavelengths in a process independent form the retinal cones [](doi.org/0.1523/JNEUROSCI.21-16-06405.2001); Vitamin D production requires very short wavelengths in the UV B regime, which is however not in the visible range [](doi.org/10.4161%2Fderm.24494).

## Primary Color Spaces: RGB and CMYK
As established, we can mix three primary colors according to their matching functions to represent the color spectrum. The choice of primary colors to do that is in principle arbitrary. You can see an example of the color matching functions below. For each color in the spectrum on the horizontal axis the curves indicate the mixing proportions of the primary colors. Interestingly, the red curve is partly negative, indicating that in order to mix the colors between 440 nm and 550 nm (cyan, turquoise) you would need to add blue and green and then remove some red. This is of course not possible and in consequence means that this combination of primaries can not create a pure cyan but only a somewhat reddish cyan. Actually, there is no combination of three primary colors which can mix all spectral colors perfectly, there is always some negative part in the matching functions. However, how much of the spectral color space is accurately represented in the constructed three dimensional space does depend on the choice of primary colors, and is called the Gamut of the color space.
<br>
But wait, then how does the eye do it with only three kinds of color receptors? The answer is somewhere in between "it doesn't" and "it's tricky", but we'll come to that.

<figure>
<a href="" style="display:block;text-align:center;">
<img src="/assets/color_post/CIE1931_RGBCMF.png" alt="CIE 1931 RGB Matching Functions">
</a>
<figcaption style="text-align:center;font-style:italic">
<a href="https://commons.wikimedia.org/wiki/File:CIE1931_RGBCMF.png">CIE 1931 RGB Color Matching Functions</a>
</figcaption>
</figure>


So, the popularity of RGB is not totally arbitrary but a consequence of 'taking a color from either end of spectrum (red and blue) and some color from the middle (green)' yields a relatively good gamut. Nevertheless, RGB itself is not uniquely defined and there are different optimized standards for different applications using different hues for their red, green, and blue definition. Some examples are sRGB for most Internet applications, Adobe RGB for better CMYK transformability, DCI-P3 for movie production, or Rec. 709 and 2020 for televisions.
To be emphasized here, RGB is not the "natural" choice for a color space because of the red, green, blue cones on the retina, because that is not how color perception works, but more on that later.
<br>
Another popular combination of primary colors is cyan, magenta, and yellow, often accompanied by black as CMYK as a color-printing standard. Having a different color representations printing than for screen display is useful because in printing the color mixing is subtractive. Overlaying color dots add up to darker colors, thus to get a wide range of colors, lighter primary colors like CMY are better suited than the darker RGB. In screens the pixel colors are mixed additive, i.e., combinations generally become lighter and thus here the darker RGB base can represent more colors. Black (K) is usually added to CMY to improve the printing of darker colors. Mixing C M and Y would in principle also yield black but in practice it is easier and more economic to just add black separately.
<br>
These color representations are evidently very useful and wide spread. However, their appeal is mostly that they are nice to work with numerically and thus are practical to for machines, they are not particularly tailored towards the human perception.

<figure>
<a href="" style="display:block;text-align:center;">
<img src="/assets/color_post/RGB_cube.png" alt="RGB Cube">
</a>
<figcaption style="text-align:center;font-style:italic">
<a href="https://de.m.wikipedia.org/wiki/Datei:RGB_color_solid_cube.png">RGB Cube </a>
<a href="https://commons.wikimedia.org/wiki/User:SharkD">(by SharkD, </a>
<a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA)</a>
</figcaption>
</figure>

Their neat arrangement into a three dimensional cube makes it particularly easy to define a color by a triple of color coordinates, (r,g,b) for example. The precision of the coordinate values consequently defines the color resolution. Typically, the color values range either from 0 to 1, or to avoid floating point numbers from 0 to 255. This means that there are 256 color increments along each axis, and therefore 256<sup>3</sup>=16777216 different colors within the RGB cube. Another frequently used notation is the HEX code. A HEX code is just a different way of writing the RGB coordinates. In the decimal system, with digits from 0 to 9, we need three digits to count up to 255. Within the hexadecimal system each digit can go up to 15, thus, being able to represent 16 different values. Because of the lack of symbols the digits are counted from 0 to 9 and then from A to F. Within the 6 digit HEX code each RGB axis is represented by a pair of hexadecimal digits ranging from 00 to FF, and because each pair can represent 16<sup>2</sup>=256 color increments the HEX notation #RRGGBB is exactly equivalent to the (r,g,b) coordinates.

> __Fun Fact:__
The gamut describes the collection of colors which can be displayed within a color space. The term gamut, however, was first used to describe the starting point of a musical scale. _Gamut_ is the shorthand for _Gamma ut_, where _ut_ denotes the first tone in the sequence of syllables representing the basic tones: _ut_, _re_, _mi_, _fa_, _sol_, _la_. These names for the tones come from a short melody written by Paulus Diaconus in the first century to praise John the Baptist. In his six verse piece these phonemes are the first syllables of every verse. So, when a display advertises itself that it can display many colors, thus being 'wide Gamut', it derives the name partly from the poetry of an Italian monk 2000 years ago.

## The Color Wheel: Hue
So far we handled color, or more precisely its _hue_, as linear like in the spectrum or as some shape in a three dimensional color space.
Besides tints, tones, and shades of color, the hue describes the kind of color and is what we refer to by the color names red, green, blue, or yellow.
<br>
Astonishingly enough, hue is perceptually not linear but circular. This feature of perception was first discovered by Isaac Newton and described in his [1704 book _Opticks_](https://archive.org/details/opticksoratreat00newtgoog). He arranged the colors on a wheel, indicating seven principal colors in analogy of the spacings between the notes in the Dorian musical scale. This color theory was further developed and challenged over the following centuries, for example by Johann Wolfgang von Goethe in his [1810 book _Zur Farbenlehre_](https://www.theoryofcolor.org/Theory+of+Colors).

<figure>
<a href="" style="display:block;text-align:center;">
<img src="/assets/color_post/Newton_Goethe_color_circles.jpg" alt="Newton's and Goethe's color circles">
</a>
<figcaption style="text-align:center;font-style:italic">
<a href="https://upload.wikimedia.org/wikipedia/commons/0/0a/Newton%27s_colour_circle.png">Newton's (left)</a>
and
<a href="https://en.wikipedia.org/wiki/Color_theory#/media/File:GoetheFarbkreis.jpg">Goethe's (right)</a>
color wheels
</figcaption>
</figure>

The color wheel is used to illustrate the mixing of color. Colors opposite from each other on the wheel are complementary pairs which mix to white. Similarly, any straight line within the wheel represents the mixing of two colors in various proportions. This linear relationship was later formalized as [Grassmann's law in 1853](https://doi.org/10.1002/andp.18531650505).
<br>
Taking into account these insights, the question now is of course: how to reconcile the circular nature of hue with the 3D cube structure of the RGB space?

<!-- (disconinuity of wavelength mapping -> how are singularities represented in topological mapping? like pinwheels?) -->

## Cylindrical Color Spaces: HSL, HSV, HSB, HSI
The RGB space (or any primary color space) does not only contain the mixes of hues for which the mixing proportions equal the coordinates in the 3D space (r,g,b).
It does also contain a degree of color _lightness_ ranging from black in one corner (0,0,0) to white in the opposite corner (1,1,1).
Additionally, there is a degree of colorfulness or _saturation_ ranging from shades of grey along the central diagonal of equal rgb proportions to the pure colors at the corners: red (1,0,0), green (0,1,0), blue (0,0,1), yellow (1,1,0), magenta (1,0,1), and cyan (0,1,1).
<br>
Using these arguably more intuitive dimensions it is possible to construct an alternative color space which also respects the circular arrangement of hues. Thus, arranging the circular hue as circumference, the linear saturation as radius, and the linear lightness as the height axis creates the cylindrical color space HSL.

<figure>
<a href="" style="display:block;text-align:center;">
<img src="/assets/color_post/HSL_HSV.png" alt="HSL, HSV cylinder">
</a>
<figcaption style="text-align:center;font-style:italic">
<a href="https://en.wikipedia.org/wiki/HSL_and_HSV#/media/File:HSL_color_solid_cylinder_saturation_gray.png">HSL </a>
and
<a href="https://en.wikipedia.org/wiki/HSL_and_HSV#/media/File:HSV_color_solid_cylinder_saturation_gray.png"> HSV </a>
cylinders
<a href="https://commons.wikimedia.org/wiki/User:SharkD"> (by SharkD</a>
,
<a href="https://creativecommons.org/licenses/by-sa/4.0/"> CC BY-SA)</a>
</figcaption>
</figure>

<!-- ToDo: Jazz this Section up! -->
As illustrated above, there are multiple alternative cylindrical color spaces using slightly different parameterization of the colors.
Instead of the lightness describing the mixing with black (shades) and white (tints), the _value_ only describes the shading of the color. This alternative representation still covers the same gamut (amount of colors) of colors as the tinting can also be achieved by varying the saturation of the pure color (on the HSV cylinder moving inward from the top edge with V=1).
Other alternatives to lightness or value include also _brightness_, _intensity_, and _luma_. Brightness and value are typically used equivalently,
and luma is similar to intensity, just with an additional correction for the fact that we can make finer distinctions between darker colors than brighter colors.
Likewise, the saturation is sometimes replaced by the _chroma_, as shown in the figure below. This might be considered more intuitive since it resolves the ambiguity that there identical blacks and whites (only in HSL) for every level of saturation. In the alternative conic of bi-conic geometry only the pure colors have a maximum chroma value.

<figure>
<a href="" style="display:block;text-align:center;">
<img src="/assets/color_post/HCL_HCV.png" alt="HCL, HCV cones">
</a>
<figcaption style="text-align:center;font-style:italic">
<a href="https://upload.wikimedia.org/wikipedia/commons/b/b3/HSL_color_solid_dblcone_chroma_gray.png">HCL </a>
and
<a href="https://upload.wikimedia.org/wikipedia/commons/0/00/HSV_color_solid_cone_chroma_gray.png"> HCV </a>
cones
<a href="https://commons.wikimedia.org/wiki/User:SharkD"> (by SharkD</a>
,
<a href="https://creativecommons.org/licenses/by-sa/4.0/"> CC BY-SA)</a>
</figcaption>
</figure>

As you see, there are many variations and slight differences for cylindrical color spaces. This easily leads to confusion as different softwares use these different variations and transitioning from one to another may introduce unwanted color shifts. Besides using different color spaces, there is also wide array of visual representations of these spaces for color picking and each software seems to invent their own combination of scales, maps, and arrangements, obfuscating the slight differences in the color spaces even more.
It also doesn't help that the terms lightness, brightness, intensity, chroma, etc. are not always properly defined and handled very consistently.
<br>
So, what are the actual advantages of these color spaces? Their main selling point is that they are computational effective (compared to more complex models). The circular representation of the hue makes sense perceptually, but the resulting discontinuity may lead to some numerical difficulties. For example a hue at 1<sup>&deg;</sup> is as far away from 3<sup>&deg;</sup> as it is from 359<sup>&deg;</sup>. Importantly, it need to be noted that the cylindrical color spaces are not absolute spaces. They are defined only in reference to a RGB space, which is also not uniquely defined as we know. Hence, this means that they suffer from the same problem as RGB spaces, and  as well cannot cover the full range of possible colors.
<br>
The attempt of HSV, HSL, and friends to relate to better relate to the dimensions of perception actually leads to more confusion than it it is helpful. Besides the tricky terminology, the dimensions of the color cylinder are also confounded. As already indicated above by the ambiguity of between cylinders and cones, the saturation scale also contains varying degrees of lightness. Naturally, we perceive the hues of different pure colors with different amounts of lightness.
<br>
In conclusion, cylindrical color spaces offer no real advantage over RGB, especially since they need to be converted back to RGB (for the screen) or to CMYK (for print) anyway. Thus, they are still mostly practical for machines but not very useful for humans.

<!-- -> generally to avoid (Brewer from colorbrewer), I always thought it was relating to brewing colors somehow bot no! -->

> __Fun Fact__:
Just as most sensual perception, light intensity is perceived approximately on a logarithmic scale which enables us to manage a wide range of stimuli from dim night to bright sunshine (see [Weber-Fenchel law]() or [Steven's power law]()).

## Color Perception: Part I
To understand what makes a color space more suitable and intuitive for humans, we need to understand more about color perception.
<br>
Humans are trichromatic, meaning that they have three types of color sensitive cones. This feat is shared only with some other primates, most other animals who are mono- (e.g. marine mammals), di- (e.g. land mammals), or tetrachromatic (e.g. fish, reptiles, and birds).
The three cone types are sensitive to short-, middle, and long wavelengths of the light spectrum, respectively, and are thus called S, M, and L cones. Sometimes, they are also referred to as blue, green, and red cones. This is, however, more misleading as the sensitivity of each cone stretches over multiple colors, and even if described by their peak-sensitivity the L cone rather corresponds to yellow than red. You can see the the three absorption curves below.

<figure>
<a href="" style="display:block;text-align:center;">
<img src="/assets/color_post/Cone_Rod_response.png" alt="Cone and rod absorption">
</a>
<figcaption style="text-align:center;font-style:italic">
<a href="https://commons.wikimedia.org/wiki/File:Cone-response-en.svg">Spectral absorption of cones (colored) and rods (black dashed)</a>
(by
<a href="https://en.wikipedia.org/wiki/User:DrBob"> DrBob</a>
&
<a href="https://en.wikipedia.org/wiki/User:Zeimusu"> Zeimusu</a>
,
<a href="https://creativecommons.org/licenses/by-sa/4.0/"> CC BY-SA)</a>
</figcaption>
</figure>

<!-- Before coming back to the cones, let's have a small detour and talk about rods.
* most sensitive for green-yellowish color during daytime vision (photopic)
* during dark conditions, night, only rod is active (scotpic)
* rod which is also wavelength sensitivity
* during dim lighting, there is a mix (mesopic), where both rods and cones are active
* because of different sensitivity peaks, in mesopic most sensitive wavelength regime is shifted towards blue (Purkinje shift)

* depends on angle (definition relative to 2deg around fovea) -> standard observer -->

Back to the cones. An eye-catching property of the absorption curves is that they are covering the visible spectrum in a very non-uniform manner. The absorption of the M and L cones overlap a lot and mainly cover the green-yellow wavelengths while there is gap to the absorption curve of the S cones for the blue wavelengths. This feature already hints at the fact the perceived lightness of a color can differ depending on the hue. For example, a pure yellow, close to the peak sensitivity of both M an L cones, appears brighter than a pure blue, which is mainly detected by the S cone.
<br>
How can knowing about the absorption functions of the cones help us constructing better color spaces? You might have noticed, that the absorption curves are somewhat similar to the color matching functions introduced earlier. In both scenarios the functions indicate how to mix three different sources for a defined color impression. In case of the color matching the sources are the three primary colors and in case of the retina the input is the neural activity of the different cones.
As illustrated earlier, a major drawback of the primary color spaces is that they can't represent all visible colors because for any set primary colors some part of the matching functions will be negative and thus represent a color that is impossible to mix. Since we are associating the color matching functions with the absorption curves, what would be the corresponding primary colors of the S, M, and L cones which somehow allows to mix all colors?
<br>
The answer is: impossible colors. The primary color corresponding to the M cone, for example, would be probably considered greenish since that's where the M cones have maximum sensitivity. However, this primary-M-cone-green can never be seen or realized because every color always activates a combination of S, M, and L cones and there is no color which can exclusively activate M cones. Even though impossible colors do not actually exist, they can be described mathematically and ultimately used to define color spaces.

> __Fun Fact__:
 M and L curves are very close, why? This increases our red/green distinction which is useful to evaluate ripeness of fruit

## CIE Chromaticity Diagram
From the absorption curves of the retinal cones we now know that the trick to constructing a full color space is to start from impossible colors. Or rather, that means that the choice of the primary colors is not of interest. We can instead directly define the color matching functions in a way that the color space has favorable properties.
This is exactly what the people from the CIE did, the _Commission internationale de l'éclairage_. In 1931, this international commission set out to establish a new standard to represent color in a perceptually reasonable way and finally bring some order to the chaos of confounded colorimetry. The result was the formidable CIE 1931 chromaticity diagram. Although, there were slight revision in 1960 and 1976 and the derivation CIELAB and CIELUV, the original 1931 version still remains the most widely used.
<br>
THE CIE color space is based on the three color dimensions simply named X, Y, and Z. These are essentially the (impossible) primary colors. The color matching function for Y is chosen to resemble the perceived _luminance_ (measured in candela/m<sup>2</sup>) of human vision. The X and Z matching functions are then defined to cover the red and blue regimes of the spectrum without containing negative values.

<figure>
<a href="" style="display:block;text-align:center;">
<img src="/assets/color_post/CIE1931_XYZCMF.png" alt="CIE 1931 XYZ Color Matching Functions">
</a>
<figcaption style="text-align:center;font-style:italic">
<a href="https://commons.wikimedia.org/wiki/File:CIE_1931_XYZ_Color_Matching_Functions.svg">CIE 1932 XYZ Color Matching Functions</a> (by Acdx,
<a href="https://creativecommons.org/licenses/by-sa/4.0/"> CC BY-SA)</a>
</figcaption>
</figure>

What is a good choice for the exact shape of the functions is less obvious, but in the end, what makes the color space so elegant. The three matching functions represent all the spectral colors in the XYZ space and form a shape that is not yet very practical. Therefore, the colors are further projected. First, onto the unit plane where $X+Y+Z=1$, and then onto the $xy$ _chromaticity_ plane, where

$x=\frac{X}{X+Y+Z}$, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
$y=\frac{Y}{X+Y+Z}$, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
$z=\frac{Z}{X+Y+Z} = 1-x-y$.

This has the advantage that all hues can be represented in 2D with only the $x$ and $y$ coordinates. Since $z$ is a function of $x$ and $y$, it doesn't contain any additional information and can be left out. However, the construction that $X+Y+Z = x+y+z =1$ essentially normalizes out any notion of color intensity so that with only $x$ and $y$ there are no shades or tints. Thus, the luminance Y is added again as the third coordinate. The resulting color space is called the CIE xyY chromaticity diagram.

<figure>
<a href="" style="display:block;text-align:center;">
<img src="/assets/color_post/CIE1931xy.png" alt="CIE 1931 xy Chromaticity Diagram">
</a>
<figcaption style="text-align:center;font-style:italic">
<a href="https://commons.wikimedia.org/wiki/File:CIE1931xy_blank.svg">CIE 1931 xy Chromaticity Diagram</a>
</figcaption>
</figure>

In contrast to the primary and cylindrical color spaces, this color representation now exhibits a whole array of fascinating and useful features. Let's go through them.
The contour line of the horseshoe shaped color area is called the _spectral locus_ and contains all the pure colors, meaning colors that can be attributed to a single wavelength given the luminance level. This arrangement might remind you of a deformed version of the color wheel. A crucial difference to the color wheel is that the spectral locus is not a closed circle, which is inevitable because mapping the linear dimension of wavelengths onto a circle creates a discontinuity. However, our brain resolves this jump between the shortest blue wavelengths and the longest red wavelengths rather elegantly by inventing the non-spectral purple colors. There is no pink or magenta in the rainbow! These hues are just the unique impression we get from the mixture of red and blue colors.
<br>
The area encompassed by the spectral locus contains all the visible colors. However, the outside of the area is of interest as well because that's where all the impossible colors lie, which are not visible themselves but can help software tools to access a wider array of colors.
<br>
A main objective of color spaces, which already Newton attempted with his color wheel, is _perceptual uniformity_. In a perceptual uniform space the euclidean distance between two points is proportional to the perceived difference between the corresponding colors. This also entails that mixing two colors can simply be expressed by taking the arithmetic average of their coordinates. To be noted, in the chromaticity diagram these features still do not work absolutely perfectly. For example, the uniformity prevails better for nearby colors as for very distant colors.
<br>
The diagram also neatly contains the color of natural light sources. Glowing heat sources emit very characteristic light, and for idealized heat sources the color of the emitted light depends only its temperature. This is the so-called black-body radiation. In the chromaticity diagram these colors lie on the _Planckian locus_ aranged by their color temperature. The Planckian locus ranges from a reddish oh-god-please-don't-touch hot for about $1000$ Kelvin to a blueish will-literally-vaporize-you-when-you-come-close freakin' hot for $10 0000$ Kelvin and above. The lines crossing the Planckian locus in the image below are _isothermal lines_ which help to identify the color temperature of the surrounding near-white colors.
Since we usually don't interact with glowing objects that are thousands of Kelvins (or Celsius) hot, it is not too surprising that the color temperatures do not correspond to our intuitive impression of color warmth. In common terminology we speak of red as a warm color and blue as a cold color even though blue has a the higher color temperature.

<figure>
<a href="" style="display:block;text-align:center;">
<img src="/assets/color_post/CIE1931xy_planck.png" alt="CIE 1931 xy Chromaticity Diagram">
</a>
<figcaption style="text-align:center;font-style:italic">
<a href="https://commons.wikimedia.org/wiki/File:PlanckianLocus.png">CIE 1931 xy Chromaticity Diagram with Planckian Locus</a>
(by BenRG & cmglee,
<a href="https://creativecommons.org/licenses/by-sa/4.0/"> CC BY-SA)</a>
</figcaption>
</figure>


* white point
* dominant wavelengths, excitation purity
* Gamut of RGB spaces

<figure>
<a href="" style="display:block;text-align:center;">
<img src="/assets/color_post/CIE1931xy_gamut_comparison.png" alt="CIE 1931 xy Chromaticity Diagram">
</a>
<figcaption style="text-align:center;font-style:italic">
<a href="https://commons.wikimedia.org/wiki/File:CIE1931xy_gamut_comparison.svg">Gamuts of different primary color spaces</a>
</figcaption>
</figure>


* y is relative luminance


* Setting a white point
* Calculating if a color can be represented on a screen

> __Fun Fact__:
chimerical colors? fictional colors
(not to be confused with fictional colors https://en.wikipedia.org/wiki/List_of_fictional_colors)

 <!-- Split Post here? -->

## Pitfalls of Palettes: JET
* uniform/linear lightness/saturation/...
* https://eagereyes.org/basics/rainbow-color-map
* https://ai.googleblog.com/2019/08/turbo-improved-rainbow-colormap-for.html
* https://hub.packtpub.com/turbo-googles-new-color-palette-for-data-visualization-addresses-shortcomings-of-the-common-rainbow-palette-jet/
* https://twitter.com/jscarto/status/1164190471222116352
* Colorblindness
* brain interprets/ categorizes -> rainbow [ref]
* show different jet improvements

## Choosing the right Palette
* sequential
* categorical (don't use primary/secondary colors? evidence?)
* diverging
* cyclical
-> color choice

## Color Perception: Part II
"Perceived color depends on the spectral distribution of
the color stimulus; on the size, shape, structure, and
surround of the stimulus area; on the state of adaptation
of the observer’s visual system; and on the observer’s
experience of the prevailing and similar situations of
observations."
* Color constancy
* Konotations
* warm/cool, much/few
* Pair constrast
* Harmony
* Trends
* background and interpretation of amount
* considering the retinal processing is only parth of the truth.
* color perception as contrast from surounding,(mexican hat), from overlapping receptive fields.
* opponent color cells with Red/Green, Blue/Yellow, White/Black (see Ewald Hering), processing in the retina -> chimerical colors (there is no blueish yellow)
* But further processing in the cortex
*

## Choosing the right Colors
Less is more
intuitive usage
<!-- ## from psychology -->
* connotations
* intuitive meanings / feelings
* use existing color (from logos etc.)
<!-- ## from data viz research -->
* color-value perception depends on background
<!-- ## train your intuition -->
* think about what you connect with a certain color
* can highly depend on cultural background
* it is also a matter of taste
* copy from resources you like
*
<!-- ## color deficiencies -->
* different types color blindness and how to correct for that
* + using hashing, structure

-> keep in mind that whatever colors you select, they need to be well displayable by a screen or printable by common printers!

## Helpful Tools
<!-- ## in Python -->
* matplotlib is not the enemy, but its defaults
* alternatives Seaborn, Altair, bookeh, ...
* -> other talk: choosing the right plot
<!-- ## others (some examples) -->
* ...

## Examples
* From Nicolas Rougeux
*

## References, Resources, and Further Reading/Listening
#### Books
* "Field guide to colorimetry and fundamental color modeling", (2018) Jennifer D. T. Kruschwitz, [doi:10.1117/3.2500912](http://dx.doi.org/10.1117/3.2500912)
* Williamson, S J and Cummins, H Z, Light and Color in Nature and Art, Wiley 1983
* "Digital Video and HD Algorithms and Interfaces", (2012) Morgan Kaufmann, [doi:10.1016/C2010-0-68987-5](https://doi.org/10.1016/C2010-0-68987-5)

* Podcasts
   * datastories (point to episode)
   * storytelling with data (point to episode)
   * after the flood
* viziwiki.com
* flowingdata.com
