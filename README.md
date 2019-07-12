This project showcases how reusable C++ code can be shared between R, Python, and Julia, the three
main statistical/machine learning languages. It showcases how package management could be done
using conan, a C++ package manager, and the language-specific package managers.

Alternative to Conan: conda, for cpp, julia, and whatever, but is it something that is used
a lot by the R users? Also, CRAN, Conan and Conda compatibility layer?

TODO:

- Test and finalize C++
- Implement CI/CD
- Implement linkage for R
- Implement CI/CD for C++
- Evaluate how to do linkage with Python
- Implement linkage for Python
- Evaluate how to do linkage with Julia
- Implement linkage with Julia
- Implement notebooks
- Readme instructions
- OSS
- Maybe add support for scala and intercompatibility with scala, to show how
  JVM models can be implemented as well.
- Write an article to show how to build a continuum like that.

In general, it is about writing C++-first code.
