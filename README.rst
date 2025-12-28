The database for 11-tetrahedra census of orientable cusped hyperbolic 3-manifolds
============================

This repository stores the manifold database of a complete census of
all 505352 orientable cusped hyperbolic 3-manifolds triangulizable by no more than 11 tetrahedra, 
along with those in `snappy_10_tets <https://github.com/Shakugannotorch/snappy_10_tets/>`_,
and includes the source code for the Python module
:code:`snappy_11_tets` which packages them up for use in SnapPy.

To install the module in SageMath::

  sage -pip install git+https://github.com/Shakugannotorch/snappy_11_tets/

To use this module with SnapPy, one can do::

  sage: from snappy_11_tets import snappy

The extended census can then be accessed via SnapPy's :code:`Manifold` class. 
For example::

  sage: m = snappy.Manifold('o11_123456')
  sage: m.triangulation_isosig()
  'lLALPzAMccbbegfhihjkkhhrwahhxrxhw_BbBa'

  sage: m = snappy.Manifold('o11_123456(2,3)')
  sage: m.triangulation_isosig()
  'lLALPzAMccbbegfhihjkkhhrwahhxrxhw_BbBa(2,3)'

The iterator for the census is :code:`snappy.ElevenTetCuspedCensus`. For example::

  sage: for M in snappy.ElevenTetCuspedCensus[-9:-6]: print(M, M.volume()) 
  o11_505343(0,0) 11.0017490870299
  o11_505344(0,0) 11.0075240445813
  o11_505345(0,0) 11.0075240445813

  sage: for M in snappy.ElevenTetCuspedCensus(num_cusps=2)[-3:]: print(M, M.volume(), M.num_cusps())
  o11_505349(0,0)(0,0) 11.0179027639862 2
  o11_505350(0,0)(0,0) 11.0232112584876 2
  o11_505351(0,0)(0,0) 11.0232112584876 2

The raw source for the tables are in::
  
  manifold_src/original_manifold_sources

stored as plain text CSV files for the potential convenience of other
users. The triangulations themselves are stored in the "isosig" format
of Burton, as described in the appendix to `this paper
<http://arxiv.org/abs/1110.6080>`_ with an added "decoration" suffix
that describes the peripheral framing.
