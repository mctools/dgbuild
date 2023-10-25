#include "Core/Python.hh"
#include "G4Examples/ExampleHooks.hh"

PYTHON_MODULE
{
  PYDEF("prepreInitHook",&ExampleHooks::prepreInitHook);
  PYDEF("preInitHook",&ExampleHooks::preInitHook);
  PYDEF("postInitHook",&ExampleHooks::postInitHook);
}
