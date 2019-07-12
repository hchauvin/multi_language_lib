/*
 * Copyright (c) Hadrien Chauvin
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

#include "catch2/catch.hpp"

#include "example/example.hpp"

namespace example::tests {

TEST_CASE("example::split splits a string") {
  REQUIRE(split("foo\tbar qux")  == {"foo", "bar", "qux"});
}

}  // namespace example::tests
