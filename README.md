This project showcases how reusable C++ code can be shared between R, Python, and Julia, the three
main statistical/machine learning languages. It showcases how package management could be done
using conan, a C++ package manager, and the language-specific package managers.

Alternative to Conan: conda, for cpp, julia, and whatever, but is it something that is used
a lot by the R users? Also, CRAN, Conan and Conda compatibility layer?

TODO:

- / Test and finalize C++
- / Implement CI/CD
- / Evaluate how to do linkage with Python
- / Implement linkage for Python
- / Implement notebooks
- / Implement linkage for R
- / Have dependent conanfile.txt to avoid loading boost::python in cpp
- (Isolate "cpp" and make it main, with a "bindings" folder where the R and python code live.)
- / Check python with a test package. How to use pip test packages, this sort of things, with python???
  I'm familiar with R's package management, not with Python's.
- / If conan not available, install conan
- (Try this on Windows)
- / Implement CI/CD for C++
- Package the C++ library with conan.
- Readme instructions
- Write an article to show how to build a continuum like that. Say that it comes
  from the realization that there are a lot of cool packages in R, such as stuff around
  LME, but that when you want to put things into production, you have to resort
  using R, which comes with lots of issues, or re-writing your stuff again. C++ being
  the lingua franca of numerical computing, it makes sense to have a C++-first
  development mentality.
- (Call the C++ unittests within the R and python packages.)
- (This can be even expanded by providing access to R, in the code, that can work if
  called outside of R, e.g. in python. Similar for Python. This way, C++ can be
  used to smooth transition in a numerical computing system that is multi-language.
  But it is a shame that a library such as nltk is available in python first. What
  if I want to write stuff in R without going multi-language? This sort of things?
  You end up having to write microservices, etc. instead of going native in the beginning.
  Notice that you can actually run C++ anywhere: on iPhones, on Androids, in embedded systems, ...
  So that's probably the most portable language. You cannot say so with Java.)
- (Package with conda as well.)
- (Maybe add support for scala and intercompatibility with scala, to show how
  JVM models can be implemented as well.)
- OSS
- Documentation, mock publication workflow.

In general, it is about writing C++-first code.

Commands:

```bash
cd cpp

mkdir -p build
cd build

conan install .. --build=outdated
cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Debug
cmake --build .. --target test
bin/test

cd ../../R

R -e "Rcpp::compileAttributes()"

R -e "devtools::load_all(); example::str_split('hello world')"

# R CMD build .
# R CMD check .
# R CMD INSTALL .

R -e "devtools::check()"

R -e "devtools::test()"

conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan
```
