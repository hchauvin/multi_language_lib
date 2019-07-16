/*
 * Copyright (c) Hadrien Chauvin
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

#include "example/example.hpp"

int main() {
  example::split("foo\tbar qux");
  return 0;
}

}  // namespace example::tests
