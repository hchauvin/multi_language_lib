context("example")

test_that("'str_split' splits a string", {
  expect_equal(str_split("foo\tbar qux"), c("foo", "bar", "qux"))
})

test_that("'str_split' checks that a string is passed as a parameter", {
  expect_error(str_split(list(a = 1)))
})
