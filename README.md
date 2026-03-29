# RIBOTIM
supplement materials for the paper *Risk-Model-based Optimization Approach for Fault-Revealing Test Input Identification in Metamorphic Testing*

__Code:__
* __ribotim.py__: Python implementation of RIBOTIM, usage: p, q = ribotim(file_name,iterations=10000,c1=1.0,c2=1.5,eta=0.2)
  * file_name: data file name
  * accuracy rate = p / q
* __failtim.py__: Python implementation of FAILTIM (baseline), usage: p, q = failtim(file_name)
  * file_name: data file name
  * accuracy rate with the *i*th risk formula = p[*i*] / q

__Data (DM, KNN, SMM, Tcas, TSQ):__
* __mg_gen.py, res_gen.py, res_gen_w.py__: Python scripts to generate the data
* __results_mutant*i*.txt__: data file of the *i*th mutant
* __w_results_mutant*i*.txt__: data file of the *i*th mutant without false-satisfying metamorphic groups
