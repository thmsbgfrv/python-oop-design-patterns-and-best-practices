"""Runner Module to Test Manually Patterns"""
from oop.patterns.creational.abstract_factory.logistics import (
    AbstractFactory,
    RoadLogisticsFactory,
    SeaLogisticsFactory,
)
from oop.patterns.creational.factory.logistic.logistics import Logistics
from oop.patterns.creational.factory.logistic.road_logistics import RoadLogistics
from oop.patterns.creational.factory.logistic.ship_logistics import ShipLogistics
from oop.patterns.creational.prototype.prototype import SelfReferencingEntity, SomeComponent
from oop.patterns.creational.singleton.singleton_naive import SingletonNaive
from oop.patterns.creational.singleton.singleton_naive_thread_safe import SingletonNaiveThreadSafe
from oop.utils.decorators.fancy_print import fancy_print


class PattersRunner:
    """PatternsRunner to run each pattern manually"""

    @fancy_print
    def run_singleton(self) -> None:
        """Run and Check Singleton"""
        # Testing Singleton
        print("Testing Singleton:")
        singleton1 = SingletonNaive("First Singleton")
        singleton2 = SingletonNaive("Second Singleton")

        print(f"singleton1: {singleton1.name}")
        print(f"singleton2: {singleton2.name}")
        print(f"Are singleton1 and singleton2 the same instance? {'Yes' if singleton1 is singleton2 else 'No'}")

        print("\nTesting SingletonNaiveThreadSafe:")
        # Testing Thread-safe Singleton
        singleton_threadsafe1 = SingletonNaiveThreadSafe("First Thread-Safe Singleton")
        singleton_threadsafe2 = SingletonNaiveThreadSafe("Second Thread-Safe Singleton")

        print(f"singleton_threadsafe1: {singleton_threadsafe1.name}")
        print(f"singleton_threadsafe2: {singleton_threadsafe2.name}")
        answer: str = 'Yes' if singleton_threadsafe1 is singleton_threadsafe2 else 'No'
        print(f"Are singleton_threadsafe1 and singleton_threadsafe2 the same instance? -{answer}")

    @fancy_print
    def run_factory(self) -> None:
        """Run and Check Factory"""

        def client_code(logistics: Logistics) -> None:
            """The client code works with an instance of a concrete logistics, albeit through its base interface."""
            print(logistics.plan_delivery())

        print("App: Launched with Road Logistics.")
        client_code(RoadLogistics())
        print("\n")
        print("App: Launched with Sea Logistics.")
        client_code(ShipLogistics())

    @fancy_print
    def run_abstract_factory(self) -> None:
        """Run and Check Abstract Factory"""

        def client_code(factory: AbstractFactory) -> None:
            """
            The client code works with factories and products only through abstract
            types: AbstractFactory and AbstractProduct. This lets you pass any factory
            or product subclass to the client code without breaking it.
            """
            transport = factory.create_transport()
            packaging = factory.create_packaging()

            print(transport.deliver())
            print(packaging.package(), end="")

        print("Client: Testing client code with the Road Logistics factory:")
        client_code(RoadLogisticsFactory())
        print("\n")
        print("Client: Testing the same client code with the Sea Logistics factory:")
        client_code(SeaLogisticsFactory())

    @fancy_print
    def run_prototype(self) -> None:
        """Run and Check prototype"""
        circular_ref = SelfReferencingEntity()
        some_list_of_objects: list[int | set[int] | list[int]] = [1, {1, 2, 3}, [1, 2, 3]]
        component: SomeComponent = SomeComponent(23, some_list_of_objects, circular_ref)
        circular_ref.set_parent(component)

        shallow_copied_component: SomeComponent = component.shallow_clone()

        # Let's change the list in shallow_copied_component and see if it changes in
        # component.
        shallow_copied_component.some_list_of_objects.append(10)
        if component.some_list_of_objects[-1] == 10:
            print(
                "Adding elements to `shallow_copied_component`'s "
                "some_list_of_objects adds it to `component`'s "
                "some_list_of_objects."
            )
        else:
            print(
                "Adding elements to `shallow_copied_component`'s "
                "some_list_of_objects doesn't add it to `component`'s "
                "some_list_of_objects."
            )

        # Let's change the set in the list of objects.
        component.some_list_of_objects[1].add(4)  # type: ignore
        if 4 in shallow_copied_component.some_list_of_objects[1]:  # type: ignore
            print(
                "Changing objects in the `component`'s some_list_of_objects "
                "changes that object in `shallow_copied_component`'s "
                "some_list_of_objects."
            )
        else:
            print(
                "Changing objects in the `component`'s some_list_of_objects "
                "doesn't change that object in `shallow_copied_component`'s "
                "some_list_of_objects."
            )

        deep_copied_component = component.clone()

        # Let's change the list in deep_copied_component and see if it changes in
        # component.
        deep_copied_component.some_list_of_objects.append(12)
        if component.some_list_of_objects[-1] == 12:
            print(
                "Adding elements to `deep_copied_component`'s "
                "some_list_of_objects adds it to `component`'s "
                "some_list_of_objects."
            )
        else:
            print(
                "Adding elements to `deep_copied_component`'s "
                "some_list_of_objects doesn't add it to `component`'s "
                "some_list_of_objects."
            )

        # Let's change the set in the list of objects.
        component.some_list_of_objects[1].add(10)  # type: ignore
        if 10 in deep_copied_component.some_list_of_objects[1]:  # type: ignore
            print(
                "Changing objects in the `component`'s some_list_of_objects "
                "changes that object in `deep_copied_component`'s "
                "some_list_of_objects."
            )
        else:
            print(
                "Changing objects in the `component`'s some_list_of_objects "
                "doesn't change that object in `deep_copied_component`'s "
                "some_list_of_objects."
            )

        print(
            f"id(deep_copied_component.some_circular_ref.parent): "
            f"{id(deep_copied_component.some_circular_ref.parent)}"
        )
        print(
            f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): "
            f"{id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}"  # type: ignore
        )
        print(
            "^^ This shows that deepcopied objects contain same reference, they "
            "are not cloned repeatedly."
        )
