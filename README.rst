The database for 11-tetrahedra census of orientable cusped hyperbolic 3-manifolds
============================

This repository stores the manifold database of a complete census of
all orientable cusped hyperbolic 3-manifolds triangulizable by no more than 10 tetrahedra, 
and includes the source code for the Python module
:code:`snappy_11_tets` which packages them up for use in SnapPy and
Spherogram.

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

The raw source for the tables are in::
  
  manifold_src/original_manifold_sources

stored as plain text CSV files for the potential convenience of other
users. The triangulations themselves are stored in the "isosig" format
of Burton, as described in the appendix to `this paper
<http://arxiv.org/abs/1110.6080>`_ with an added "decoration" suffix
that describes the peripheral framing.
