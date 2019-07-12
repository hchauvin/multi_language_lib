/*
 * Copyright (c) Hadrien Chauvin
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

#include <Rcpp.h>

#include "example/example.hpp"

// [[Rcpp::export]]
std::vector<std::string> str_split(std::string s) { return example::split(s); }
