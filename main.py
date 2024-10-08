"""Main Module to Run Manual tests and Others"""

from oop.patterns.patterns_runner import PattersRunner

if __name__ == "__main__":
    runner: PattersRunner = PattersRunner()
    runner.run_singleton()
    runner.run_factory()
    runner.run_abstract_factory()
    runner.run_prototype()
