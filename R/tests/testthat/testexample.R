context("example")

test_that("'split' splits a string", {
  expect_equal(example_split("foo\tbar qux"), c("foo", "bar", "qux"))
})

test_that("'split' checks that a string is passed as a parameter", {
  expect_error(example_split(list(a = 1)))
})
