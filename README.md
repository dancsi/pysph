#pysph - python3

![pysph screenshot](https://github.com/benma/pysph/raw/master/screenshots/concat.png)

pysph is a demo of:

* sph (smooth particle hydrodynamics) fluid simulation
* screen space fluid rendering, based on Simon Green's paper [Screen Space Fluid Rendering with Curvature Flow](http://www.cs.rug.nl/~roe/publications/fluidcurvature.pdf).
* how to use Python for these kind of things using the excellent pyopengl and pyopencl libraries.
* how to make and use bindings to the Cg runtime libraries in Python.

Also contained are ports of radix sort and bitonic sort to pyopencl. Based on [enjalot's work](https://github.com/enjalot/adventures_in_opencl/tree/master/experiments). 

Big thanks to Ian Johnson (enjalot) for the radix/bitonic sort and his excellent tutorial: "[Adventures in PyOpenCL](http://enja.org/2011/02/22/adventures-in-pyopencl-part-1-getting-started-with-python/)".

## Running:

Run with `python main.py [number of particles]`. Start with `python main.py 8000` and slowly scale the number of particles up.

You can disable the advanced rendering by using `python main.py --disable-advanced-rendering [number of particles]`.
For more options, run `python main.py --help`.

## Dependencies

**On Debian Testing (sid):**
`sudo apt-get install python-opengl python-pyside nvidia-cg-toolkit python-numpy python-mako python-pyopencl`

And either package providing pyopencl-icd: nvidia-opencl-icd for nvidia users, amd-opencl-icd for ati users.

**On Ubuntu:**
`sudo apt-get install python-opengl python-pyside nvidia-cg-toolkit python-numpy  python-mako`

Unfortunately on Ubuntu (up to 12.04), the package python-pyopencl is outdated and is missing the --cl-enable-gl flag.
Using pip also won't work, because it does not configure the package using the --cl-enable-gl flag. 
You will need to follow the official build instructions here: http://wiki.tiker.net/PyOpenCL/Installation/Linux/Ubuntu.

If you want to isolate the installation of pyopencl, you can still install it in a virtualenv by using:

```
$ virtualenv --system-site-packages pysph_env

$ wget http://pypi.python.org/packages/source/p/pyopencl/pyopencl-2011.2.tar.gz
$ tar xfz pyopencl-2011.2.tar.gz
$ cd pyopencl-2011.2/
$ python ./configure.py --cl-enable-gl
$ python setup.py build
$ python setup.py install --prefix=/path/to/pysph_env/ --optimize=1 

$ source bin/activate
$ python /path/to/pysph/main.py
```

**On Windows:**
decorator, distribute, mako, numpy, pyOpenGL, pyOpenCL, pysideuic, pyside, pytools.
Yuo can get all of them at http://www.lfd.uci.edu/~gohlke/pythonlibs/ 

## Limitations

Screen space rendering rendering is not complete. It is not optimized for speed. 
Also, the rendering at the boundaries is not properly dealt with yet, you can see the artefacts in the screenshots.