## PyTennessee 2018
Slides, notes and code for my talk on Property Based Testing with Hypothesis

The slides are written in markdown and presented through [reveal-md](https://github.com/webpro/reveal-md)

You can get hypothesis [here](https://hypothesis.readthedocs.io/en/latest/quickstart.html#installing)

The tests are in the same files as the code. You can run them using `pytest file_name` and pytest will auto discover them.

* addition.py has four tests for the properties of addition
* fibonacci.py has a Fibonacci algorithm and a test for its properties
* real_world.py has a simple aggregator and its property tests
