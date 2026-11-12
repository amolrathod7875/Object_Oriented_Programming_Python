# PYTHON OOP — 42-DAY INTERVIEW CODING CHALLENGE

**One self-contained challenge per day. No solutions supplied.**

**Audience:** Python-focused Software / AI / ML / RAG engineering interviews.
**Prerequisite:** Completed the original six practical challenges (Bank Account, Employee Management, Shape ABC, Library, ML Model Comparison, Mini RAG).

## Rules for every day

- [ ] Sketch the class diagram (5 minutes) before writing code.
- [ ] Write the solution yourself; prefer small, cohesive classes.
- [ ] Add at least 3 positive, negative and edge-case tests.
- [ ] Explain where inheritance, composition, encapsulation, polymorphism, or abstraction is used — and why.
- [ ] Explain time and space complexity where relevant.
- [ ] Commit your code and a short README to GitHub.
- [ ] Only mark **Done** if all pass checks succeed.

**Suggested progression:** Weeks 1–2 ~35–75 min/day; Weeks 3–4 ~50–90 min/day; Weeks 5–6 ~50–110 min/day. These are study targets, not deadlines.

## Progress Overview

| Day | Challenge                             | Level        | Progress       |
| --: | ------------------------------------- | ------------ | -------------- |
|   1 | E-commerce Cart Pricing               | Intermediate | ☐ Not started |
|   2 | University Course Enrollment          | Intermediate | ☐ Not started |
|   3 | Digital Wallet Transfers              | Intermediate | ☐ Not started |
|   4 | Vehicle Rental Pricing Engine         | Intermediate | ☐ Not started |
|   5 | Notification Channels                 | Intermediate | ☐ Not started |
|   6 | Cinema Seat Booking                   | Intermediate | ☐ Not started |
|   7 | Expense Splitting for Friends         | Intermediate | ☐ Not started |
|   8 | Validated Product Properties          | Intermediate | ☐ Not started |
|   9 | Temperature Measurement Object        | Intermediate | ☐ Not started |
|  10 | Immutable Money Value Object          | Intermediate | ☐ Not started |
|  11 | Vector2D Operator Overloading         | Intermediate | ☐ Not started |
|  12 | Fraction Class with Normalization     | Intermediate | ☐ Not started |
|  13 | Inventory Import and Export           | Intermediate | ☐ Not started |
|  14 | Account ID Generation                 | Intermediate | ☐ Not started |
|  15 | Safe Audit Log Context Manager        | Intermediate | ☐ Not started |
|  16 | CSV Contact Repository                | Intermediate | ☐ Not started |
|  17 | Discount Strategy Engine              | Intermediate | ☐ Not started |
|  18 | Document Parser Factory               | Intermediate | ☐ Not started |
|  19 | Payment Processing Simulator          | Intermediate | ☐ Not started |
|  20 | Price Alert Observer                  | Intermediate | ☐ Not started |
|  21 | Undoable To-Do Manager                | Intermediate | ☐ Not started |
|  22 | Fluent Report Builder                 | Intermediate | ☐ Not started |
|  23 | Weather Data Adapter (Offline)        | Intermediate | ☐ Not started |
|  24 | Swappable Task Repositories           | Intermediate | ☐ Not started |
|  25 | LRU Cache                             | Advanced     | ☐ Not started |
|  26 | Per-User Rate Limiter                 | Advanced     | ☐ Not started |
|  27 | Priority Task Scheduler               | Advanced     | ☐ Not started |
|  28 | Nested Folder Size Calculator         | Advanced     | ☐ Not started |
|  29 | Positive Number Descriptor            | Advanced     | ☐ Not started |
|  30 | Typed Storage via Protocol            | Advanced     | ☐ Not started |
|  31 | Cooperative Multiple Inheritance      | Advanced     | ☐ Not started |
|  32 | Domain Exception Hierarchy            | Advanced     | ☐ Not started |
|  33 | Automatic Plugin Registration         | Advanced     | ☐ Not started |
|  34 | Lazy Property with Cache Invalidation | Advanced     | ☐ Not started |
|  35 | Thread-Safe Visit Counter             | Advanced     | ☐ Not started |
|  36 | Dataset Split Manager                 | Advanced     | ☐ Not started |
|  37 | ML Feature Pipeline Objects           | Advanced     | ☐ Not started |
|  38 | Binary Classification Metrics         | Advanced     | ☐ Not started |
|  39 | Model Inference Service               | Advanced     | ☐ Not started |
|  40 | RAG Document Chunker Strategies       | Advanced     | ☐ Not started |
|  41 | Retrieval and Reranking Pipeline      | Advanced     | ☐ Not started |
|  42 | Safe Agent Tool Orchestrator          | Advanced     | ☐ Not started |

## Week 1 — Practical Class Design

Build robust business objects and enforce invariants.

### DAY 01 — E-commerce Cart Pricing

**Level:** Intermediate  |  **Target:** 45–60 min  |  **Concepts:** Composition, validation, aggregation

**Tasks**

- [ ] Create Product(sku, name, unit_price) and CartItem(product, quantity).
- [ ] Implement ShoppingCart.add_item(), remove_item(), subtotal() and total() with a percentage discount.
- [ ] Reject negative prices, nonpositive quantities, and discounts outside 0–100%.

**Pass checks**

- [ ] Two units of ₹500 and one unit of ₹200 give subtotal ₹1,200.
- [ ] A 10% discount gives total ₹1,080.
- [ ] Adding an existing SKU updates its quantity instead of duplicating it.

**Interview reflection:** Why is a cart better modeled with composition than inheritance?

---

### DAY 02 — University Course Enrollment

**Level:** Intermediate  |  **Target:** 45–60 min  |  **Concepts:** Many-to-many object relationships, invariants

**Tasks**

- [ ] Create Student, Course(capacity) and University classes.
- [ ] Implement enroll(student_id, course_id), drop(...), and list_enrollments(...).
- [ ] Reject duplicate enrollments, unknown IDs and full courses.

**Pass checks**

- [ ] A course with capacity 2 accepts two students and rejects a third.
- [ ] Dropping a student makes one place available.
- [ ] The same student cannot enroll twice.

**Interview reflection:** Where should enrollment rules live: Student, Course or University?

---

### DAY 03 — Digital Wallet Transfers

**Level:** Intermediate  |  **Target:** 45–60 min  |  **Concepts:** Encapsulation, invariant preservation, atomic operations

**Tasks**

- [ ] Create Wallet(owner_id, starting_balance) with nonpublic balance.
- [ ] Implement deposit(), withdraw() and transfer_to(other_wallet, amount).
- [ ] Keep immutable-style transaction records; reject invalid and insufficient-funds transfers.

**Pass checks**

- [ ] Wallet A ₹1,000 transfers ₹300 to B ₹200: balances become ₹700 and ₹500.
- [ ] An attempted transfer of ₹5,000 leaves both wallets unchanged.
- [ ] External changes to retrieved history do not mutate internal history.

**Interview reflection:** What does atomicity mean in this in-memory model?

---

### DAY 04 — Vehicle Rental Pricing Engine

**Level:** Intermediate  |  **Target:** 45–60 min  |  **Concepts:** Inheritance, overriding, polymorphism

**Tasks**

- [ ] Create a Vehicle base class with id and daily_rate; derive Car, Bike and Truck.
- [ ] Each subclass implements rental_cost(days) with a type-specific fee rule you document.
- [ ] Build a RentalService that accepts a mixed Vehicle list and prints quotations.

**Pass checks**

- [ ] Every vehicle computes cost through the same rental_cost(days) call.
- [ ] days=0 and a negative rate are rejected.
- [ ] At least two subclasses produce different prices for the same rate and duration.

**Interview reflection:** How does method overriding differ from overloading in Python?

---

### DAY 05 — Notification Channels

**Level:** Intermediate  |  **Target:** 40–55 min  |  **Concepts:** ABC, polymorphism, dependency injection

**Tasks**

- [ ] Define abstract Notifier.send(recipient, message).
- [ ] Implement EmailNotifier, SMSNotifier and ConsoleNotifier with simulated deliveries (no real messages).
- [ ] Build AlertService that takes any Notifier and sends an alert.

**Pass checks**

- [ ] Calling Notifier() directly fails.
- [ ] AlertService works unchanged with all three implementations.
- [ ] Reject empty recipient/message; save delivery logs for inspection.

**Interview reflection:** What is the benefit of programming against an interface?

---

### DAY 06 — Cinema Seat Booking

**Level:** Intermediate  |  **Target:** 60–75 min  |  **Concepts:** State modeling, composition, unique constraints

**Tasks**

- [ ] Create Show, Seat and BookingManager; each seat is available or reserved.
- [ ] Implement reserve(show_id, seat_id, customer_id) and cancel(booking_id).
- [ ] Prevent double booking; validate show/seat IDs.

**Pass checks**

- [ ] Reserving A1 succeeds once; a second reservation is rejected.
- [ ] Cancelling makes A1 available again.
- [ ] Cancellation of an unknown booking does not change state.

**Interview reflection:** How would concurrency change the design?

---

### DAY 07 — Expense Splitting for Friends

**Level:** Intermediate  |  **Target:** 60–75 min  |  **Concepts:** Domain modeling, rounding, validation

**Tasks**

- [ ] Create Person, Expense(payer, amount, participants) and Group.
- [ ] Support equal splitting and compute each person’s net balance.
- [ ] Produce a minimal-ish settlement plan; use Decimal or integer paise.

**Pass checks**

- [ ] A pays ₹900 shared equally by A/B/C: B and C owe A ₹300 each.
- [ ] Reject empty participants, unknown people and nonpositive expenses.
- [ ] Total net balances sum to exactly zero.

**Interview reflection:** Why is floating-point arithmetic risky for money?

---

## Week 2 — Python Object Model

Properties, dataclasses, operator overloading, serialization.

### DAY 08 — Validated Product Properties

**Level:** Intermediate  |  **Target:** 40–55 min  |  **Concepts:** @property, setters, encapsulation

**Tasks**

- [ ] Create Product with validated name, price and stock.
- [ ] Expose price and stock via properties; forbid negative updates.
- [ ] Add inventory_value as a read-only computed property.

**Pass checks**

- [ ] price=₹250 and stock=4 give inventory_value=₹1,000.
- [ ] Setting stock=-1 raises ValueError.
- [ ] Attempting to assign inventory_value fails.

**Interview reflection:** When should a computed attribute be a property instead of a method?

---

### DAY 09 — Temperature Measurement Object

**Level:** Intermediate  |  **Target:** 35–50 min  |  **Concepts:** Properties, canonical representation

**Tasks**

- [ ] Store a temperature in Celsius in one internal attribute.
- [ ] Provide celsius and fahrenheit properties with working setters.
- [ ] Validate values against absolute zero.

**Pass checks**

- [ ] Setting Celsius to 0 makes Fahrenheit 32.
- [ ] Setting Fahrenheit to 212 makes Celsius 100.
- [ ] A temperature below −273.15 °C is rejected.

**Interview reflection:** Why store just one canonical unit internally?

---

### DAY 10 — Immutable Money Value Object

**Level:** Intermediate  |  **Target:** 50–65 min  |  **Concepts:** Frozen dataclasses, equality, immutability

**Tasks**

- [ ] Create a frozen Money(amount, currency) value object using Decimal.
- [ ] Implement addition/subtraction for matching currencies and clear formatting.
- [ ] Reject operations across currencies and negative amounts only where your chosen model requires.

**Pass checks**

- [ ] Money(100, INR)+Money(50, INR) produces INR 150.
- [ ] INR + USD raises a useful exception.
- [ ] Changing amount on a frozen object is rejected.

**Interview reflection:** What is the difference between a value object and an entity?

---

### DAY 11 — Vector2D Operator Overloading

**Level:** Intermediate  |  **Target:** 45–60 min  |  **Concepts:** Dunder methods, representation

**Tasks**

- [ ] Build Vector2D(x,y) with __add__, __sub__, __eq__, __repr__.
- [ ] Implement scalar multiplication and magnitude().
- [ ] Return NotImplemented for unsupported operand types.

**Pass checks**

- [ ] Vector2D(2,3)+Vector2D(4,-1) equals Vector2D(6,2).
- [ ] magnitude of (3,4) is 5.
- [ ] Adding a vector to a string fails predictably.

**Interview reflection:** What is NotImplemented, and how is it different from NotImplementedError?

---

### DAY 12 — Fraction Class with Normalization

**Level:** Intermediate  |  **Target:** 60–75 min  |  **Concepts:** Value objects, dunders, invariants

**Tasks**

- [ ] Create Fraction(numerator, denominator) and reduce using gcd.
- [ ] Implement +, -, *, /, equality and a readable __str__.
- [ ] Normalize signs and reject a zero denominator.

**Pass checks**

- [ ] 2/4 equals 1/2.
- [ ] 1/2 + 1/3 equals 5/6.
- [ ] Dividing by a zero-valued fraction raises an error.

**Interview reflection:** What invariants should remain true after every operation?

---

### DAY 13 — Inventory Import and Export

**Level:** Intermediate  |  **Target:** 45–60 min  |  **Concepts:** @classmethod, @staticmethod, serialization

**Tasks**

- [ ] Create InventoryItem with sku, title, price and stock.
- [ ] Implement from_dict() and to_dict() so objects round-trip.
- [ ] Add a static helper to validate SKU format.

**Pass checks**

- [ ] from_dict(to_dict(item)) reconstructs equivalent values.
- [ ] Malformed SKU and missing required fields are rejected.
- [ ] Serialization does not expose internal-only fields.

**Interview reflection:** When is @classmethod preferable to @staticmethod?

---

### DAY 14 — Account ID Generation

**Level:** Intermediate  |  **Target:** 45–60 min  |  **Concepts:** Class attributes, classmethods, instance identity

**Tasks**

- [ ] Create Customer accounts with automatically generated unique IDs.
- [ ] Keep the next-ID counter at the class level; expose a classmethod for controlled test resets.
- [ ] Store names and status per instance, never shared accidentally.

**Pass checks**

- [ ] Three new accounts receive distinct sequential IDs.
- [ ] Changing one customer’s status leaves others unchanged.
- [ ] You can explain why an instance-level counter would fail.

**Interview reflection:** What is the difference between a class attribute and an instance attribute?

---

## Week 3 — Reusable Design Patterns I

Context managers, persistence, Strategy, Factory, Observer, Command.

### DAY 15 — Safe Audit Log Context Manager

**Level:** Intermediate  |  **Target:** 50–65 min  |  **Concepts:** Context managers, resource ownership

**Tasks**

- [ ] Create AuditSession(path) implementing __enter__ and __exit__.
- [ ] Write timestamped messages to a text file and always close it on exit.
- [ ] Do not suppress exceptions; record that a session ended.

**Pass checks**

- [ ] A with-block writes two messages and closes the file.
- [ ] A forced exception still closes the file and propagates outward.
- [ ] The log can be reopened and read.

**Interview reflection:** When should __exit__ return True versus False?

---

### DAY 16 — CSV Contact Repository

**Level:** Intermediate  |  **Target:** 60–75 min  |  **Concepts:** File I/O, composition, data validation

**Tasks**

- [ ] Create Contact and ContactRepository classes.
- [ ] Implement save(), load(), find_by_email() using a CSV file.
- [ ] Reject duplicate emails and malformed rows; support a temporary file in tests.

**Pass checks**

- [ ] Two contacts survive a save-and-reload round trip.
- [ ] Duplicate email insertion fails.
- [ ] Empty or malformed CSV is handled without silent corruption.

**Interview reflection:** How would you separate persistence concerns from business rules?

---

### DAY 17 — Discount Strategy Engine

**Level:** Intermediate  |  **Target:** 50–65 min  |  **Concepts:** Strategy pattern, open/closed principle

**Tasks**

- [ ] Define a DiscountStrategy interface with apply(amount).
- [ ] Implement NoDiscount, PercentageDiscount and FixedDiscount.
- [ ] Create PricingService that accepts any strategy and never returns negative totals.

**Pass checks**

- [ ] ₹1,000 with 15% discount becomes ₹850.
- [ ] ₹1,000 with fixed ₹200 discount becomes ₹800.
- [ ] Adding a new discount needs no changes to PricingService logic.

**Interview reflection:** How is Strategy different from a large if/elif block?

---

### DAY 18 — Document Parser Factory

**Level:** Intermediate  |  **Target:** 60–75 min  |  **Concepts:** Factory pattern, abstract classes

**Tasks**

- [ ] Define Parser.parse(text) and implement JSONParser and CSVParser.
- [ ] Build ParserFactory.create(format_name) with clear errors for unsupported types.
- [ ] Return a normalized list of dictionaries and validate malformed inputs.

**Pass checks**

- [ ] JSON and CSV representing the same records produce equivalent output.
- [ ] An unknown format raises ValueError.
- [ ] Malformed JSON is reported instead of silently ignored.

**Interview reflection:** What problem does a Factory solve?

---

### DAY 19 — Payment Processing Simulator

**Level:** Intermediate  |  **Target:** 50–65 min  |  **Concepts:** Interfaces, dependency injection, error handling

**Tasks**

- [ ] Define PaymentProvider.charge(amount, reference) for simulated transactions.
- [ ] Implement CardSimulator and WalletSimulator; no real network or money movement.
- [ ] PaymentService records approved/declined attempts by reference.

**Pass checks**

- [ ] A valid simulated charge returns an approval record.
- [ ] A declined charge has a reason and does not appear approved.
- [ ] The service can swap provider implementations without code changes.

**Interview reflection:** Why would you inject a fake payment provider in tests?

---

### DAY 20 — Price Alert Observer

**Level:** Intermediate  |  **Target:** 55–70 min  |  **Concepts:** Observer pattern, event notification

**Tasks**

- [ ] Create PriceFeed and Subscriber/AlertListener interfaces.
- [ ] Allow listeners to subscribe/unsubscribe to a product price.
- [ ] Notify only when the price changes, and avoid duplicate subscriptions.

**Pass checks**

- [ ] Two subscribers both receive one change event.
- [ ] Unsubscribed listeners receive none.
- [ ] Setting the same price twice causes no duplicate notification.

**Interview reflection:** How would you prevent one failed listener from blocking the others?

---

### DAY 21 — Undoable To-Do Manager

**Level:** Intermediate  |  **Target:** 60–75 min  |  **Concepts:** Command pattern, undo/redo, state

**Tasks**

- [ ] Implement AddTaskCommand, CompleteTaskCommand and DeleteTaskCommand.
- [ ] Create TaskManager.execute(command), undo(), redo().
- [ ] Maintain consistent task IDs and reject invalid undo/redo states.

**Pass checks**

- [ ] Add → undo removes task → redo restores task.
- [ ] Complete → undo restores incomplete state.
- [ ] Undo on empty history fails safely.

**Interview reflection:** Why encapsulate actions as command objects?

---

## Week 4 — Reusable Design Patterns II

Builder, Adapter, Repository, caching, schedulers, Composite.

### DAY 22 — Fluent Report Builder

**Level:** Intermediate  |  **Target:** 50–65 min  |  **Concepts:** Builder pattern, fluent API

**Tasks**

- [ ] Create a ReportBuilder for title, sections, metadata and output format.
- [ ] Provide chainable methods returning self; build() returns an immutable Report.
- [ ] Prevent building a report without a title.

**Pass checks**

- [ ] builder.set_title("X").add_section("A").build() works.
- [ ] Mutating the builder later does not change an already-built report.
- [ ] Missing title raises a useful error.

**Interview reflection:** Why separate a mutable builder from an immutable result?

---

### DAY 23 — Weather Data Adapter (Offline)

**Level:** Intermediate  |  **Target:** 50–65 min  |  **Concepts:** Adapter pattern, unit conversion

**Tasks**

- [ ] Invent two mock weather providers with different field names/temperature units.
- [ ] Adapt both to a common WeatherReading(city, temp_c, humidity) interface.
- [ ] Create WeatherService that depends only on the common interface.

**Pass checks**

- [ ] A mock 86°F input becomes 30°C.
- [ ] Both providers produce the same normalized schema.
- [ ] Missing humidity produces a clear validation error.

**Interview reflection:** When should an Adapter be used instead of inheritance?

---

### DAY 24 — Swappable Task Repositories

**Level:** Intermediate  |  **Target:** 60–75 min  |  **Concepts:** Repository pattern, dependency injection

**Tasks**

- [ ] Define TaskRepository with add(), get(), list() and delete().
- [ ] Implement InMemoryTaskRepository and JSONFileTaskRepository.
- [ ] Build TaskService that works with either repository unmodified.

**Pass checks**

- [ ] TaskService passes the same tests against both implementations.
- [ ] JSON storage persists across repository instances.
- [ ] Unknown task IDs return a defined error.

**Interview reflection:** What is the difference between business logic and a repository?

---

### DAY 25 — LRU Cache

**Level:** Advanced  |  **Target:** 60–90 min  |  **Concepts:** Collections, object design, O(1) operations

**Tasks**

- [ ] Create LRUCache(capacity) with get(key) and put(key,value).
- [ ] Evict the least recently used key when capacity is exceeded.
- [ ] Target O(1) average get/put using OrderedDict or a dict + linked list.

**Pass checks**

- [ ] Capacity 2: put(A), put(B), get(A), put(C) evicts B.
- [ ] Updating a key makes it most recently used.
- [ ] capacity=0 is rejected.

**Interview reflection:** Explain the data structure choices and time complexity.

---

### DAY 26 — Per-User Rate Limiter

**Level:** Advanced  |  **Target:** 60–90 min  |  **Concepts:** Dependency injection, time-based state

**Tasks**

- [ ] Create RateLimiter(max_requests, window_seconds, clock).
- [ ] Allow/deny requests per user within a sliding or fixed window; document your choice.
- [ ] Inject a fake clock for deterministic tests.

**Pass checks**

- [ ] Limit 2 per 60 s: third immediate request for the same user is rejected.
- [ ] A second user has an independent allowance.
- [ ] After the window expires, a request is allowed again.

**Interview reflection:** What trade-off exists between fixed and sliding windows?

---

### DAY 27 — Priority Task Scheduler

**Level:** Advanced  |  **Target:** 60–80 min  |  **Concepts:** heapq, dataclasses, ordering

**Tasks**

- [ ] Create Task(id, priority, created_order, action) and TaskScheduler.
- [ ] Pop tasks by highest priority and FIFO for equal priority.
- [ ] Allow cancellations without corrupting future scheduling.

**Pass checks**

- [ ] High priority runs before low priority.
- [ ] Equal-priority tasks preserve insertion order.
- [ ] Cancelled tasks never run.

**Interview reflection:** How would you support task retries safely?

---

### DAY 28 — Nested Folder Size Calculator

**Level:** Advanced  |  **Target:** 50–75 min  |  **Concepts:** Composite pattern, tree recursion

**Tasks**

- [ ] Create File(name, size) and Folder(name) nodes with a common get_size() interface.
- [ ] Folders may contain files and nested folders.
- [ ] Prevent accidental cycles in folder relationships.

**Pass checks**

- [ ] Folder with 10-byte file and subfolder containing 20-byte file has size 30.
- [ ] Removing a child updates calculated size.
- [ ] Adding a folder as its own descendant is rejected.

**Interview reflection:** What makes this the Composite design pattern?

---

## Week 5 — Advanced Python OOP

Descriptors, Protocols, MRO, exception hierarchies, plugins, threading.

### DAY 29 — Positive Number Descriptor

**Level:** Advanced  |  **Target:** 60–80 min  |  **Concepts:** Descriptor protocol, attribute validation

**Tasks**

- [ ] Implement a PositiveNumber descriptor with __set_name__, __get__, __set__.
- [ ] Use it for width, height and price in different classes.
- [ ] Keep values isolated per instance and reject zero/negative inputs.

**Pass checks**

- [ ] Two Rectangle objects have independent widths.
- [ ] Setting width=-2 raises ValueError.
- [ ] Descriptor works for at least two owning classes.

**Interview reflection:** How are descriptors related to @property?

---

### DAY 30 — Typed Storage via Protocol

**Level:** Advanced  |  **Target:** 50–75 min  |  **Concepts:** typing.Protocol, structural typing, DI

**Tasks**

- [ ] Define a Storage Protocol with save(key, payload) and load(key).
- [ ] Build MemoryStorage and FakeCloudStorage implementations without explicit inheritance.
- [ ] Use a DocumentService typed against Storage.

**Pass checks**

- [ ] Both storage implementations run the same service tests.
- [ ] A missing key has a consistent error behavior.
- [ ] mypy/pyright can validate the interface if available.

**Interview reflection:** What is structural typing versus nominal typing?

---

### DAY 31 — Cooperative Multiple Inheritance

**Level:** Advanced  |  **Target:** 60–90 min  |  **Concepts:** MRO, mixins, cooperative super()

**Tasks**

- [ ] Create TimestampMixin and ValidationMixin with cooperative __init__(**kwargs).
- [ ] Combine them with BaseRecord in a final Record class.
- [ ] Inspect Record.mro() and ensure initialization happens once per class.

**Pass checks**

- [ ] Record has both timestamp and validation behavior.
- [ ] No required constructor argument is lost.
- [ ] Explain the order reported by Record.mro().

**Interview reflection:** Why can hard-coded parent calls break multiple inheritance?

---

### DAY 32 — Domain Exception Hierarchy

**Level:** Advanced  |  **Target:** 45–65 min  |  **Concepts:** Custom exceptions, error propagation

**Tasks**

- [ ] Define ApplicationError and meaningful subclasses such as DuplicateItemError and NotFoundError.
- [ ] Use them in a small InventoryService rather than generic Exception everywhere.
- [ ] Catch errors at the CLI boundary and print useful messages.

**Pass checks**

- [ ] Duplicate SKU raises DuplicateItemError.
- [ ] Unknown SKU raises NotFoundError.
- [ ] Unexpected programming errors are not swallowed.

**Interview reflection:** When is a new exception class worth creating?

---

### DAY 33 — Automatic Plugin Registration

**Level:** Advanced  |  **Target:** 60–85 min  |  **Concepts:** __init_subclass__, class registry

**Tasks**

- [ ] Build a Processor base class that registers subclasses by a declared key.
- [ ] Implement UppercaseProcessor and WordCountProcessor.
- [ ] Create ProcessorRegistry.get(key); reject duplicate registrations.

**Pass checks**

- [ ] Registry resolves both processors by name.
- [ ] Unknown key raises a clear error.
- [ ] Two subclasses cannot silently register the same key.

**Interview reflection:** What risks arise from dynamic plugin loading?

---

### DAY 34 — Lazy Property with Cache Invalidation

**Level:** Advanced  |  **Target:** 50–70 min  |  **Concepts:** @cached_property, memoization, invalidation

**Tasks**

- [ ] Create Dataset(records) with an expensive summary property (counts/mean).
- [ ] Compute summary lazily and cache it until records change.
- [ ] Provide append/remove that invalidate cached derived values.

**Pass checks**

- [ ] First summary access computes once.
- [ ] Repeated access without mutations uses the cached value.
- [ ] Appending data causes the next access to recompute.

**Interview reflection:** What are the dangers of caching mutable state?

---

### DAY 35 — Thread-Safe Visit Counter

**Level:** Advanced  |  **Target:** 60–85 min  |  **Concepts:** threading.Lock, shared state, testing

**Tasks**

- [ ] Create VisitCounter with increment() and get_count().
- [ ] Use threading.Lock to protect state updates.
- [ ] Run multiple threads performing many increments; compare to a single-threaded baseline.

**Pass checks**

- [ ] 10 threads × 1,000 increments yields exactly 10,000.
- [ ] The implementation does not rely on the GIL for correctness.
- [ ] Invalid decrement/negative adjustments are handled explicitly.

**Interview reflection:** Why is a read-modify-write sequence not necessarily atomic?

---

## Week 6 — AI/ML Systems in OOP

Production-inspired Python design for datasets, ML, RAG and agents.

### DAY 36 — Dataset Split Manager

**Level:** Advanced  |  **Target:** 60–90 min  |  **Concepts:** Data classes, reproducibility, leakage prevention

**Tasks**

- [ ] Create Dataset and SplitManager using Python lists (NumPy optional).
- [ ] Produce deterministic train/validation/test splits using an injected seed.
- [ ] Keep related group IDs in the same split to avoid leakage.

**Pass checks**

- [ ] Same seed + data yields identical splits.
- [ ] No sample ID appears in two splits.
- [ ] All samples are assigned exactly once.

**Interview reflection:** Why can random row-level splitting cause leakage?

---

### DAY 37 — ML Feature Pipeline Objects

**Level:** Advanced  |  **Target:** 70–90 min  |  **Concepts:** fit/transform interfaces, composition, state

**Tasks**

- [ ] Create a Transformer interface with fit(data), transform(data).
- [ ] Implement MeanImputer and StandardScaler; chain them in FeaturePipeline.
- [ ] Reject transform() before fit() and handle zero-variance features safely.

**Pass checks**

- [ ] Training mean [2,4,6] imputes missing value to 4.
- [ ] Pipeline uses training parameters on test data.
- [ ] Calling transform before fit raises a useful exception.

**Interview reflection:** Why must preprocessing be fit on training data only?

---

### DAY 38 — Binary Classification Metrics

**Level:** Advanced  |  **Target:** 55–80 min  |  **Concepts:** Single-responsibility, class design, numerical edge cases

**Tasks**

- [ ] Create ConfusionMatrix(y_true,y_pred) with TP, TN, FP, FN properties.
- [ ] Add precision(), recall(), f1() and accuracy().
- [ ] Choose and document safe zero-division behavior.

**Pass checks**

- [ ] For TP=2, FP=1, FN=1, TN=2: precision, recall and F1 each equal 2/3.
- [ ] Mismatched input lengths raise ValueError.
- [ ] All-negative predictions are handled without crashes.

**Interview reflection:** Why might accuracy be misleading on imbalanced data?

---

### DAY 39 — Model Inference Service

**Level:** Advanced  |  **Target:** 60–85 min  |  **Concepts:** ABC/Protocol, DI, adapter, error handling

**Tasks**

- [ ] Define PredictiveModel.predict(features) interface.
- [ ] Provide RuleBasedModel and FakeMLModel implementations.
- [ ] InferenceService validates requests, captures latency and normalizes response format.

**Pass checks**

- [ ] Both models work through the same InferenceService.
- [ ] Empty/malformed feature input is rejected.
- [ ] Predictions include model name and a numeric result without hard-coding a model type.

**Interview reflection:** How does this architecture help test ML inference without loading a real model?

---

### DAY 40 — RAG Document Chunker Strategies

**Level:** Advanced  |  **Target:** 70–90 min  |  **Concepts:** Strategy pattern, composition, metadata

**Tasks**

- [ ] Create Document(id,text) and Chunk(document_id,index,text).
- [ ] Implement WordCountChunker and SentenceChunker, using an interchangeable interface.
- [ ] Support configurable overlap for the word-count strategy; preserve provenance metadata.

**Pass checks**

- [ ] A 10-word document with chunk_size=4 and overlap=1 produces the expected overlapping segments.
- [ ] chunk_size ≤ overlap is rejected.
- [ ] Every chunk links back to the source document.

**Interview reflection:** What chunking trade-offs affect retrieval quality?

---

### DAY 41 — Retrieval and Reranking Pipeline

**Level:** Advanced  |  **Target:** 70–100 min  |  **Concepts:** Dependency injection, ranking, stable interfaces

**Tasks**

- [ ] Create Retriever.retrieve(query) and Reranker.rerank(query, docs) interfaces.
- [ ] Use deterministic mock implementations (keyword scores are sufficient).
- [ ] Orchestrate retrieve → deduplicate → rerank → threshold → final top_k.

**Pass checks**

- [ ] Repeated document IDs appear only once in final results.
- [ ] Returned items are sorted by descending score.
- [ ] A high threshold can correctly produce an empty result.

**Interview reflection:** Why separate candidate retrieval from reranking?

---

### DAY 42 — Safe Agent Tool Orchestrator

**Level:** Advanced  |  **Target:** 75–110 min  |  **Concepts:** Tool interfaces, permissions, state machine, bounded loops

**Tasks**

- [ ] Define Tool(name, validate_input, execute) and a ToolRegistry.
- [ ] Create an AgentRunner that processes a predefined sequence of tool calls with allowed-tool permissions and max_steps.
- [ ] Implement mock CalculatorTool, SearchDocsTool and RestrictedDeleteTool; do not access real services.

**Pass checks**

- [ ] An approved tool call runs and produces an auditable result.
- [ ] An unauthorized delete action is blocked.
- [ ] A plan exceeding max_steps stops safely; exceptions are recorded.

**Interview reflection:** What is the difference between a fixed workflow and an autonomous agent?

---

## Daily README template

```text
Day:
Challenge:
Classes / relationships:
Why these design choices:
Happy-path tests:
Invalid/edge tests:
Complexity where relevant:
What I learned:
```

## Review milestones

- End of Week 1: Refactor one day using smaller methods and clearer exception messages.
- End of Week 2: Explain `@property`, `@classmethod`, `@staticmethod`, dataclasses and 4 dunder methods without notes.
- End of Week 3: Draw Strategy, Factory and Observer relationships from memory.
- End of Week 4: Redesign a previous solution using dependency injection and repository interfaces.
- End of Week 5: Explain MRO, Protocols, descriptors and why concurrent state needs locks.
- End of Week 6: Mock interview — present one AI/ML service architecture and defend design trade-offs.

**Important:** Challenges are educational and use offline mocks for messaging, payments and agents. They are not production-ready financial, security, or clinical systems.
