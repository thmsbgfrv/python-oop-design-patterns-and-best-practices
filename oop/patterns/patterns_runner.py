"""Runner Module to Test Manually Patterns"""
from oop.patterns.behavioral.chain import HighLevelHandler, LowLevelHandler, MidLevelHandler
from oop.patterns.creational.abstract_factory.logistics import (
    AbstractFactory,
    RoadLogisticsFactory,
    SeaLogisticsFactory,
)
from oop.patterns.creational.builder.builder import Car, CarBuilder
from oop.patterns.creational.factory.logistic.logistics import Logistics
from oop.patterns.creational.factory.logistic.road_logistics import RoadLogistics
from oop.patterns.creational.factory.logistic.ship_logistics import ShipLogistics
from oop.patterns.creational.prototype.prototype import SelfReferencingEntity, SomeComponent
from oop.patterns.creational.singleton.singleton_naive import SingletonNaive
from oop.patterns.creational.singleton.singleton_naive_thread_safe import SingletonNaiveThreadSafe
from oop.patterns.structural.adapter import PayPalAdapter, PayPalPayment, StripeAdapter, StripePayment
from oop.patterns.structural.bridge import CreditCardPayment, CryptoPayment, CryptoProcessor
from oop.patterns.structural.bridge import PayPalPayment as PayPalPaymentBridge
from oop.patterns.structural.bridge import PayPalProcessor, StripeProcessor
from oop.patterns.structural.composite import Directory, File
from oop.patterns.structural.decorator import EmailNotification, Notification, SMSNotification
from oop.patterns.structural.facade import VideoStreamingFacade
from oop.patterns.structural.flyweight import CharacterFactory
from oop.patterns.structural.proxy import BankAccountProxy, RealBankAccount
from oop.utils.decorators.fancy_print import fancy_print


class PattersRunner:
    """PatternsRunner to run each pattern manually"""

    @fancy_print
    def run_all(self) -> None:
        """Run all Patterns Example Manual"""
        # creature
        self.__run_singleton()
        self.__run_factory()
        self.__run_abstract_factory()
        self.__run_prototype()
        self.__run_builder()

        # structure
        self.__run_adapter()
        self.__run_bridge()
        self.__run_proxy()
        self.__run_facade()
        self.__run_decorator()
        self.__run_composite()
        self.__run_flyweight()

        # behavioral
        self.__run_chain()
        self.__run_observer()
        self.__run_strategy()
        self.__run_command()
        self.__run_iterator()
        self.__run_state()
        self.__run_memento()
        self.__run_template()
        self.__run_visitor()
        self.__run_mediator()

    @fancy_print
    def __run_chain(self) -> None:
        """Run and Check chain"""
        # Creating the handlers
        low: LowLevelHandler = LowLevelHandler()
        mid: MidLevelHandler = MidLevelHandler()
        high: HighLevelHandler = HighLevelHandler()

        # Setting up the chain: low -> mid -> high
        low.set_next(mid).set_next(high)

        # Test requests
        requests: list[str] = ["low", "mid", "high", "unknown"]

        for req in requests:
            result: str | None = low.handle(req)
            if result:
                print(result)
            else:
                print(f"No handler found for {req}")

    @fancy_print
    def __run_observer(self) -> None:
        """Run and Check observer"""

    @fancy_print
    def __run_strategy(self) -> None:
        """Run and Check strategy"""

    @fancy_print
    def __run_command(self) -> None:
        """Run and Check command"""

    @fancy_print
    def __run_iterator(self) -> None:
        """Run and Check iterator"""

    @fancy_print
    def __run_state(self) -> None:
        """Run and Check state"""

    @fancy_print
    def __run_memento(self) -> None:
        """Run and Check memento"""

    @fancy_print
    def __run_template(self) -> None:
        """Run and Check template"""

    @fancy_print
    def __run_visitor(self) -> None:
        """Run and Check visitor"""

    @fancy_print
    def __run_mediator(self) -> None:
        """Run and Check mediator"""

    @fancy_print
    def __run_flyweight(self) -> None:
        """Run and Check FlyWeight"""
        factory = CharacterFactory()

        # Create shared characters with different attributes
        char_a_red = factory.get_character('A', 'Arial', 'Red')
        char_a_blue = factory.get_character('A', 'Arial', 'Blue')
        char_b_red = factory.get_character('B', 'Arial', 'Red')

        # Display characters
        char_a_red.display()
        char_a_blue.display()
        char_b_red.display()

        # Show that shared instances are reused
        char_a_red_again = factory.get_character('A', 'Arial', 'Red')
        print("Is char_a_red the same as char_a_red_again?", char_a_red is char_a_red_again)  # Should be True

    @fancy_print
    def __run_composite(self) -> None:
        """Run and Check Composite"""
        # Create files
        file1 = File("file1.txt")
        file2 = File("file2.txt")

        # Create directories
        dir1 = Directory("dir1")
        dir2 = Directory("dir2")

        # Add files to directories
        dir1.add(file1)
        dir1.add(file2)

        # Add a directory inside another directory
        dir2.add(dir1)

        # Display the file system structure
        dir2.display()

    @fancy_print
    def __run_decorator(self) -> None:
        """Run and Check Decorator"""
        # Create a basic notification
        notification = Notification()
        notification.send()

        print("\n--- With Email Notification ---\n")
        # Add email notification capability
        email_notification = EmailNotification(notification)
        email_notification.send()

        print("\n--- With SMS Notification ---\n")
        # Add SMS notification capability
        sms_notification = SMSNotification(email_notification)
        sms_notification.send()

        print("\n--- With Combined Notification ---\n")
        combined = SMSNotification(EmailNotification(notification))
        combined.send()

    @fancy_print
    def __run_facade(self) -> None:
        """Run and Check Facade"""
        facade = VideoStreamingFacade()
        facade.watch_video("user", "password", "1234")  # Should work
        facade.watch_video("invalid_user", "wrong_password", "5678")  # Should fail

    @fancy_print
    def __run_proxy(self) -> None:
        """Run and Check Proxy"""
        # Create a real bank account with an initial balance of $100
        real_account = RealBankAccount(initial_balance=100.0)

        # Create a proxy for the bank account with an unauthenticated user
        proxy_unauthenticated = BankAccountProxy(real_account, user_authenticated=False)
        proxy_unauthenticated.deposit(50.0)  # Output: Access denied. User is not authenticated.
        proxy_unauthenticated.withdraw(20.0)  # Output: Access denied. User is not authenticated.

        # Create a proxy for the bank account with an authenticated user
        proxy_authenticated = BankAccountProxy(real_account, user_authenticated=True)
        proxy_authenticated.deposit(50.0)  # Output: Deposited $50.0. New balance is $150.0.
        proxy_authenticated.withdraw(20.0)  # Output: Withdrew $20.0. New balance is $130.0.

    @fancy_print
    def __run_bridge(self) -> None:
        """Run and Check Bridge"""
        # Create a credit card payment with Stripe processor
        stripe_processor = StripeProcessor()
        credit_card_payment = CreditCardPayment(card_number="1234-5678-9876-5432", processor=stripe_processor)
        print(credit_card_payment.pay(100.0))
        # Output: Using Credit Card 1234-5678-9876-5432: Processing payment of $100.0 via Stripe.

        # Create a PayPal payment with PayPal processor
        paypal_processor = PayPalProcessor()
        paypal_payment = PayPalPaymentBridge(paypal_account="user@example.com", processor=paypal_processor)
        print(paypal_payment.pay(50.0))
        # Output: Using PayPal Account user@example.com: Processing payment of $50.0 via PayPal.

        # Create a crypto payment with CryptoAPI processor
        crypto_processor = CryptoProcessor()
        crypto_payment = CryptoPayment(wallet_address="abc123wallet", processor=crypto_processor)
        print(crypto_payment.pay(200.0))
        # Output: Using Wallet abc123wallet: Processing payment of $200.0 via CryptoAPI.

    @fancy_print
    def __run_adapter(self) -> None:
        """Run and Check Adapter"""

        # Using PayPal
        paypal_adapter = PayPalAdapter(PayPalPayment())
        print(paypal_adapter.process_payment(50.0))  # Output: PayPal: Processed payment of $50.00

        # Using Stripe
        stripe_adapter = StripeAdapter(StripePayment())
        print(stripe_adapter.process_payment(75.0))  # Output: Stripe: Charged $75.00

    @fancy_print
    def __run_singleton(self) -> None:
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
    def __run_factory(self) -> None:
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
    def __run_abstract_factory(self) -> None:
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
    def __run_prototype(self) -> None:
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

    @fancy_print
    def __run_builder(self) -> None:
        """Run builder design pattern"""
        car_builder: CarBuilder = CarBuilder()
        car: Car = (car_builder
                    .set_model("Tesla")
                    .set_year(2023)
                    .build())
        print(car)
