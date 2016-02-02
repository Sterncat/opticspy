
#opticspy  

Opticspy is a python module for optics application. I want to this for a long time. One reason is I know both optics and python, so why no develop some optics tools? The second reason is that there is not much opensource, easy-to-use optics program module(matlab has great fuctions but do not specify to optics application). I want this could be developed in to a core for a future web application for optics.

###There are some examples opticspy module:   
  
####1. [Zernike Polynomial Methods](http://sterncat.github.io/files/Zernike_Polynomial_Method.html)

####2. [Zernike Polynomial Fitting Methods](http://sterncat.github.io/files/Zernike_Polynomial_Fitting_Method.html)  

####3. [Interferometer Methods](http://sterncat.github.io/files/Interferometer_Method.html) 

####4. [Phase shift interferometer and surface rebuild](http://sterncat.github.io/files/PSI.html)

####5. [Wave Propagation and Aberration Methods](http://sterncat.github.io/files/Diffraction_Method.html)

####6. [Lens aberration, Jones matrix and gauss beam methods ](http://sterncat.github.io/files/Other_functions.html)

####7. [Orthonormal Rectangular Polynomials](http://sterncat.github.io/files/Orthonormal_Rectangular_Polynomials.html) 

####8. [Hartmann Test Patterns](http://sterncat.github.io/files/Hartmann_Test.html)   

###There are some interesting derivative from opticspy:

####1. [A Zernike Polynomial GUI app based on opticspy and PyQt5](https://github.com/Sterncat/zernikeapp) 
####It is very easy to reuse or "wrap" opticspy module with a GUI(e.g. PyQt)

<p><img src="http://sterncat.github.io/images/panelpic.png" height="300" width="480" /></p>

####2. [Zernike Surface gif show](http://sterncat.github.io/images/zernikegif.gif)
  
####This is the [Opticspy project page](http://opticspy.org)

####This project is hosted on github in [https://github.com/Sterncat/opticspy](https://github.com/Sterncat/opticspy)

##Installing
####Use pip install (recommend)
```
$ pip install opticspy
```
####[Or download here](http://sterncat.github.io/files/opticspy-0.1.tar.gz)

```
$ python2.7 setup.py install
```
####Some trouble shooting please read [troubleshooting.md](https://github.com/Sterncat/opticspy/blob/master/troubleshooting.md)
##How to use
```
>>> import opticspy
```

And just have fun with it!

## What I want
<ul>	
  <li>1. After import the module and you will get some functions that can do some calculation and education in optics</li>
  <li>2. Parameters should be very flexible, and the results should be shown in visualized, intuitionistic figures.</li>
  <li>3. After development of core, I want it be dynamic web application(with Javascript)</li>
  <li>4. I even hope one day it will become a part of online optics design application, who knows?</li>
</ul>

##TODO:
* ✓ Rectangular, circle, double circle, frame, etc aperture
* ✓ Third order ray aberration plot
* ✓ Twyman_Green interferogram with aberration
* ✓ Lateral Shear interferogram with aberration
* ✓ Zernike Coefficient calculation
* ✓ Zernike Polynomials surface(3D), map(2D), cutoff of 3D(1D), PSF
* ✓ Zernike Polynomials Fitting Method
* ✓ Diffraction: generate diffraction pattern
* ✓ Convert Zernike to Seidel coefficient
* ✓ Seidel aberrations surface and interferogram
* ✓ Fresnel and Fraunhofer diffraction
* ✓ Hartmann Pattern Simulation
* ✓ Geometric matrix calculation
* ✓ PSF, OTF and MTF calculation
* Rochi Test
* Asphere fitting
* Some freeform theory
* More testing technology
* Real Ray tracing and basic lens design
* Third and high order aberration calculation
* Make it rock!



##Authors and Contributors
I am Xing Fan. An optics master student now studying in the [Institute of Optics](http://www.optics.rochester.edu/), [University of Rochester](http://www.rochester.edu/). 

And this is my personal blog [Marvin's Neverland!](http://sterncat.github.io)

##Support or Contact
If you have questions and advice, or want to participate in this project, contact me at marvin.fanxing@gmail.com. I would be very happy to find some one have the same interest!

###MIT License
-----------

Copyright (c) 2014-2016 Xing fan (https://github.com/Sterncat/opticspy)
Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

		
