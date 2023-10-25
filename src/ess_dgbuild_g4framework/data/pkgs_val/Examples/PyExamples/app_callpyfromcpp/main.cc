#include "Core/Python.hh"
#include <cstdio>

int main(int,char**) {

  //Task: Call the python function "some_function" which is defined in the
  //PyExamples.Example python module.

  //First we need to initialise python, since we are not inside a python module
  //here:

  pyextra::ensurePyInit();

  //Then import the desired module:
  py::object mod = pyextra::pyimport("PyExamples.Example");

  //And grab the desired function:
  py::object some_function = mod.attr("some_function");

  //And call it (converting the returned py::object to a C++ double):
  double res = py::extract<double>(some_function(2.2,-0.4));

  //Print the result:
  printf("Result of calling PyExamples.Example.some_function(2.2,-0.4): %g\n",res);

  return 0;
}
