"""Main Module to Run Manual tests and Others"""

from oop.patterns.patterns_runner import PattersRunner

if __name__ == "__main__":
    patterns_runner: PattersRunner = PattersRunner()
    patterns_runner.run_all()
