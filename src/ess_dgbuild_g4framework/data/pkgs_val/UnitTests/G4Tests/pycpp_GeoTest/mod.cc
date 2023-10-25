#include "G4Interfaces/GeoConstructPyExport.hh"
#include "G4Tests/GeoTest.hh"

PYTHON_MODULE
{
  GeoConstructPyExport::exportGeo<G4Tests::GeoTest>(PYMOD "GeoTest");
}
