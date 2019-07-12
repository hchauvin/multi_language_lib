This project showcases how reusable C++ code can be shared between R, Python, and Julia, the three
main statistical/machine learning languages. It showcases how package management could be done
using conan, a C++ package manager, and the language-specific package managers.

Alternative to Conan: conda, for cpp, julia, and whatever, but is it something that is used
a lot by the R users? Also, CRAN, Conan and Conda compatibility layer?

TODO:

- / Test and finalize C++
- Implement CI/CD
- / Implement linkage for R
- Try this on Windows
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
- Write an article to show how to build a continuum like that. Say that it comes
  from the realization that there are a lot of cool packages in R, such as stuff around
  LME, but that when you want to put things into production, you have to resort
  using R, which comes with lots of issues, or re-writing your stuff again. C++ being
  the lingua franca of numerical computing, it makes sense to have a C++-first
  development mentality.
- This can be even expanded by providing access to R, in the code, that can work if
  called outside of R, e.g. in python. Similar for Python. This way, C++ can be
  used to smooth transition in a numerical computing system that is multi-language.
  But it is a shame that a library such as nltk is available in python first. What
  if I want to write stuff in R without going multi-language? This sort of things?
  You end up having to write microservices, etc. instead of going native in the beginning.
  Notice that you can actually run C++ anywhere: on iPhones, on Androids, in embedded systems, ...
  So that's probably the most portable language. You cannot say so with Java.

In general, it is about writing C++-first code.

Commands:

```bash
cd cpp

# TODO: Add third party not published to conan central.

conan install . --build=outdated
cmake . -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Debug
cmake --build . --target test
bin/test

cd ../R

R -e "Rcpp::compileAttributes()"

# R -e "devtools::load_all()"

# R CMD build .
# R CMD check .
# R CMD INSTALL .

R -e "devtools::check()"

R -e "devtools::test()"
```
