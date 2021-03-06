BEAST
=====

The Bayesian Extinction and Stellar Tool (BEAST) fits the ultraviolet to
near-infrared photometric SEDs of stars to extract stellar and
dust extinction parameters.  
The stellar parameters are age (t), mass (M), and metallicity (M).
The dust extinction parameters are dust column (Av), average grain size (Rv),
and mixing between type A and B extinction curves (fA).  

The full details of the BEAST are provide by 
Gordon et al. (2016, ApJ, 826, 104).
<http://adsabs.harvard.edu/abs/2016ApJ...826..104G>

BEAST Repository
================

Github: <https://github.com/karllark/beast>

Installing the BEAST
====================

.. toctree::
   :maxdepth: 2

   install.rst

Setup the BEAST
===============

Need documention on setting up the datamodel.py file for BEAST runs

Format of BEAST Files
=====================

.. toctree::
   :maxdepth: 2

   beast_grid_format.rst

Generating AST Inputs
=====================

.. toctree::
   :maxdepth: 2

   Description <generating_asts.rst>

Contribute to Development
=========================

.. toctree::
   :maxdepth: 2

   Description <beast_development.rst>

Reference API
=============
.. toctree::
   :maxdepth: 1

   physicsmodel_api.rst
   observationmodel_api.rst
   fitting_api.rst
	      
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
