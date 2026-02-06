The database for 11-tetrahedra census of orientable cusped hyperbolic 3-manifolds
=================================================================================

This repository stores the manifold database of a complete census of
all 505352 orientable cusped hyperbolic 3-manifolds whose minimal ideal triangulations consist of 11 tetrahedra, 
and includes the source code for the Python module :code:`snappy_11_tets` which packages them up for use in SnapPy.

The orientable cusped census of 10 tetrahedra has been merged into :code:`snappy_manifolds` in its recent release of version 1.4, and now comes with SnapPy version 3.3 automatically, see `SnapPy's News page <https://snappy.computop.org/news.html>`_ for details.

To install this package, do::

  python -m pip install --upgrade --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ snappy_11_tets

or, if you are using SageMath::

  sage -pip install --upgrade --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ snappy_11_tets

The above command should be able to automatically install the 1.4 version of :code:`snappy_manifolds`, if it is not readily installed.

To use this module with SnapPy, one can do::

  >>> import snappy, snappy_11_tets

The extended census can then be accessed via SnapPy's :code:`Manifold` class. 
For example::

  >>> m = snappy.Manifold('o11_123456')
  >>> m.triangulation_isosig()
  'lLALPzAMccbbegfhihjkkhhrwahhxrxhw_BbBa'

  >>> m = snappy.Manifold('o11_123456(2,3)')
  >>> m.triangulation_isosig()
  'lLALPzAMccbbegfhihjkkhhrwahhxrxhw_BbBa(2,3)'

The iterator for all manifolds in this module, along with those in :code:`snappy_manifolds`, is :code:`snappy.ElevenTetCuspedCensus`. 
For example::

  >>>
   len(snappy.ElevenTetCuspedCensus)
  717993

  >>> for M in snappy.ElevenTetCuspedCensus[-9:-6]: print(M, M.volume()) 
  o11_505343(0,0) 11.0017490870299
  o11_505344(0,0) 11.0075240445813
  o11_505345(0,0) 11.0075240445813

  >>> for M in snappy.ElevenTetCuspedCensus(num_cusps=2)[-3:]: print(M, M.volume(), M.num_cusps())
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
