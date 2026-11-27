# EP001 · Validating an internal request title

## Rule
The learner explained that a whitespace-only title contains no usable information. Trim the outer whitespace, reject an empty result, and preserve spaces inside a valid title.

## Implementation and debugging
The learner wrote and saved the function. The assistant ran the tests and guided fixes to Python syntax and capitalization, including using `==` for comparison and spelling `ValueError` correctly.

## Additional test
With guidance on `strip()` and the location of the test, the learner added a title containing a tab and a newline. The test expects `ValueError` because the resulting title is empty.

## Observed result
`python3 -m unittest -v` ran four tests. All passed. The learner reviewed how test discovery imports and calls the implementation.
