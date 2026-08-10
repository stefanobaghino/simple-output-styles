# Content-loss report

The checks measure what a rewrite loses relative to the unstyled
answer of the same prompt, per gated pair. The judge extracts the
facts and the uncertain claims from the unstyled answer, then
checks each item against the styled answer. No judge call sees
both answers of a pair: the extracted items travel between the
calls, never the source text. No prompt names a style or an arm,
and the judge model differs from the writer of the answers.

The unstyled answer is the reference, not a gold standard. A fact
that the unstyled answer omits is invisible to these checks, and
survival measures loss against that baseline, not correctness.

Judge: opus. Judged on 2026-08-10T13:33:41+00:00.

## Completeness (fact survival)

The judge lists the facts of the unstyled answer, then checks each fact against the styled answer. The fraction is the share of the facts that survive. The judge also lists the facts of the styled answer and checks each fact against the unstyled answer: a styled fact that the unstyled answer does not state is an addition. The lost facts and the added facts appear verbatim below the table.

### actionable-clarity

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 27 | 20 | 0.741 | 28 | 3 |
| code-review-02 | 17 | 16 | 0.941 | 22 | 4 |
| code-review-03 | 27 | 19 | 0.704 | 35 | 10 |
| code-review-04 | 26 | 20 | 0.769 | 20 | 4 |
| code-review-05 | 33 | 23 | 0.697 | 31 | 6 |
| code-review-06 | 29 | 22 | 0.759 | 54 | 16 |
| code-review-07 | 40 | 32 | 0.8 | 32 | 3 |
| code-review-08 | 29 | 24 | 0.828 | 40 | 7 |
| debugging-01 | 7 | 7 | 1.0 | 7 | 1 |
| debugging-02 | 18 | 17 | 0.944 | 15 | 1 |
| debugging-03 | 13 | 13 | 1.0 | 12 | 0 |
| debugging-04 | 15 | 12 | 0.8 | 13 | 6 |
| debugging-05 | 19 | 18 | 0.947 | 15 | 0 |
| debugging-06 | 35 | 15 | 0.429 | 27 | 4 |
| debugging-07 | 2 | 1 | 0.5 | 43 | 43 |
| debugging-08 | 1 | 0 | 0.0 | 40 | 40 |
| explanation-01 | 37 | 30 | 0.811 | 34 | 5 |
| explanation-02 | 32 | 25 | 0.781 | 27 | 3 |
| explanation-03 | 28 | 18 | 0.643 | 23 | 2 |
| explanation-04 | 35 | 27 | 0.771 | 40 | 3 |
| explanation-05 | 16 | 10 | 0.625 | 18 | 3 |
| explanation-06 | 16 | 15 | 0.938 | 25 | 7 |
| explanation-07 | 21 | 18 | 0.857 | 29 | 3 |
| explanation-08 | 15 | 10 | 0.667 | 16 | 10 |
| summarization-01 | 6 | 5 | 0.833 | 5 | 1 |
| summarization-02 | 11 | 11 | 1.0 | 17 | 1 |
| summarization-03 | 15 | 15 | 1.0 | 13 | 0 |
| summarization-04 | 14 | 12 | 0.857 | 11 | 0 |
| summarization-05 | 9 | 6 | 0.667 | 10 | 1 |
| summarization-06 | 15 | 14 | 0.933 | 13 | 1 |
| summarization-07 | 14 | 14 | 1.0 | 14 | 2 |
| summarization-08 | 21 | 20 | 0.952 | 15 | 1 |

Median fraction: 0.806 over 32 scored pairs.

Median additions: 3.0 over 32 scored pairs.

Lost facts:

- code-review-01: If `"member"` is already in `roles`, it is appended again, producing `["member", "member"]`.
- code-review-01: The function performs no validation on `name`, such as checking for an empty string or wrong type.
- code-review-01: The function performs no validation that `roles` is actually a list.
- code-review-01: A `True`/`False` return value tells the caller nothing about why the call failed or what was inserted, such as a created user ID.
- code-review-01: The suggested fix copies the caller's list with `list(roles)` to avoid mutating it.
- code-review-01: The suggested fix appends `"member"` only if it is not already in `roles`.
- code-review-01: Specific exceptions can be caught at the call site if needed.
- code-review-02: The fixed version checks `res.ok` and throws an `Error` including `res.status` when the response is not OK.
- code-review-03: Stacked queries can enable worse attacks, depending on the database driver.
- code-review-03: If `customer_name` or `status` is not a string (e.g. `None`), the `+` concatenation raises a `TypeError`.
- code-review-03: A `TypeError` from concatenation is raised instead of a meaningful error.
- code-review-03: The code does not handle `fetchall()` on large result sets.
- code-review-03: If a customer has many orders, `fetchall()` loads everything into memory at once.
- code-review-03: Pagination or `fetchmany()` is worth considering for large datasets.
- code-review-03: Exact string matching makes the query case-sensitive.
- code-review-03: Case-insensitive matching or normalization such as trimming whitespace may be wanted, depending on requirements.
- code-review-04: This read-modify-write pattern is a TOCTOU (time-of-check-to-time-of-use) bug.
- code-review-04: Every method of the class is unsafe to call concurrently with any other method, including itself.
- code-review-04: The proposed fix uses a threading.Lock acquired via 'with' in increment(), reset(), and a value property.
- code-review-04: The proposed fix serializes all reads and writes through a single lock.
- code-review-04: itertools.count() is thread-safe in CPython.
- code-review-04: itertools.count() and multiprocessing.Value are lock-free alternatives worth considering for higher throughput under heavy contention.
- code-review-05: The script performs no sanity check on the supplied path.
- code-review-05: A caller could pass `/` or `/home` and the script would `cd` there and delete `*.tmp` files.
- code-review-05: If no `.log` files exist, `ls *.log` prints a "No such file or directory" error to stderr.
- code-review-05: When `ls *.log` matches nothing, the loop harmlessly does not execute.
- code-review-05: Using a bare glob avoids the stderr error message.
- code-review-05: In plain `sh`/dash an unmatched glob does not match, so the literal-glob issue does not arise there.
- code-review-05: `gzip` can fail on a read-only file or an already-gzipped file.
- code-review-05: The script should print something like `Usage: $0 <backup_dir>` and exit when `$1` is missing.
- code-review-05: The `-f` flag in `rm -rf *.tmp` suppresses errors.
- code-review-05: Suppressing errors with `-f` is fine for the no-match case but also silently masks permission errors.
- code-review-06: The list-replacement behavior is inconsistent with the function's dict-merging behavior.
- code-review-06: The resulting traceback appears far from the actual bad input, making it confusing.
- code-review-06: The function can never produce a None settings value.
- code-review-06: pop(key, None) does not crash when the key being deleted is absent from merged.
- code-review-06: The asymmetry between list and dict handling is more likely an incomplete implementation than a deliberate choice.
- code-review-06: There are currently no tests for the code.
- code-review-06: Writing tests that pin down current behavior before changing anything is the recommended approach.
- code-review-07: The zero-delay first backoff is not documented and is inconsistent with the rest of the backoff logic.
- code-review-07: On the final loop iteration, a 429 still triggers the setTimeout wait before the loop exits.
- code-review-07: The delay on the final attempt is wasted because there is no subsequent attempt.
- code-review-07: Swallowing errors as null is the riskiest issue because it hides programming errors rather than only HTTP failures.
- code-review-07: There is no upper bound check on err.status >= 500.
- code-review-07: Any status of 500 or greater, including nonstandard or custom codes, is treated as retryable.
- code-review-07: There is no err.status < 600 guard, so the condition means '>= 500' rather than '5xx'.
- code-review-07: Retry-on-429, retry-on-5xx, and giving up on other errors form a recognizable rate-limit and transient-error retry pattern.
- code-review-08: `os.listdir()` returns entries in filesystem order, not sorted by mtime.
- code-review-08: The script does not select files oldest-first for the 500 cap.
- code-review-08: Immediate deletion of tmp-/.part files could be deliberate if writer processes rename atomically on completion.
- code-review-08: The script does not own the system that produces the tmp-/.part files.
- code-review-08: No one owns the script's schedule.
- debugging-02: The global object is referred to as `window` or `globalThis`.
- debugging-04: A file can be opened in binary mode with the "rb" mode string.
- debugging-04: Counting occurrences of b"\n" in binary mode yields a line count.
- debugging-04: Opening the file in binary mode avoids decoding entirely.
- debugging-05: `tags = list(DEFAULT_TAGS)` can be replaced with `["draft"]`.
- debugging-06: The working directory is empty.
- debugging-06: There is no code to inspect, so the task is pure log analysis.
- debugging-06: A nightly bulk read/write job can collide with analytics traffic that spikes unpredictably.
- debugging-06: Dashboard refreshes and scheduled analytics queries are examples of unpredictable analytics traffic spikes.
- debugging-06: A slow analytics query can be caused by a missing index or a table scan.
- debugging-06: Slow analytics queries starving a co-tenant is the classic 'noisy neighbor' pattern for shared databases.
- debugging-06: The failures occur on a weekly frequency.
- debugging-06: Weekly failure frequency could line up with a periodic batch job, a deploy, or a data-volume spike.
- debugging-06: A mismatch between pool size and instance/replica count is a plausible cause.
- debugging-06: If a service scaled up its workers or replicas without raising the database max-connections or pool size, exhaustion becomes a matter of timing rather than a deterministic bug.
- debugging-06: One check is whether analytics query volume, replica count, or a specific slow query spikes around 02:14 UTC on failure nights.
- debugging-06: The failures occur around 02:14 UTC.
- debugging-06: Pool-level metrics such as active, idle, and waiting connections over time should be gathered from both services.
- debugging-06: Some database drivers or ORMs expose pool metrics such as checked-out connections and wait queue length.
- debugging-06: Retention for metrics is often longer than log retention and cheaper to keep.
- debugging-06: Checking database-side logs can reveal what was holding connections at 02:14:07-02:14:41.
- debugging-06: The failure window on the observed night spanned 02:14:07 to 02:14:41.
- debugging-06: Increasing log retention or adding sampling for pool stats would avoid being left with only rotated log fragments next time.
- debugging-06: The available logs are rotated fragments.
- debugging-06: A single WARN or ERROR line without pool size, active count, or caller identity is hard to act on.
- debugging-07: There is memory that may be relevant to the task.
- debugging-08: The session ID is 4988878c-7c4a-4c17-92eb-92beb2d5be32.
- explanation-01: A hash map's underlying array has only one slot per index.
- explanation-01: Chaining is also known as separate chaining.
- explanation-01: The collection in a chaining slot is usually a linked list, and sometimes a tree or array.
- explanation-01: Quadratic probing jumps by increasing squares.
- explanation-01: Open addressing can degrade sharply as the array fills up, due to clustering and more probes.
- explanation-01: Open addressing implementations often resize at around a 70% load factor.
- explanation-01: Go's map uses a bucket-based chaining variant.
- explanation-02: When an optimistic write is rejected, the caller retries.
- explanation-02: An optimistic stock update can be written as `UPDATE products SET stock = stock - 1, version = version + 1 WHERE id = 42 AND version = 7;`.
- explanation-02: Optimistic locking fits when transactions are short and fast.
- explanation-02: Examples of good fits for optimistic locking include a web app editing user profiles, e-commerce catalog updates, and most CRUD APIs.
- explanation-02: A pessimistic transfer example uses BEGIN, two `SELECT balance FROM accounts WHERE id = ... FOR UPDATE` statements, balance updates, and COMMIT.
- explanation-02: Financial transfers, inventory reservation for a flash sale, and seat booking systems are examples where pessimistic locking fits.
- explanation-02: Pessimistic locking risks contention and deadlocks.
- explanation-03: A network path may consist of a single fast link or may cross several routers of varying speed and load.
- explanation-03: Persistent overloading of the network causes congestive collapse.
- explanation-03: In congestive collapse, throughput drops sharply even though all senders are trying to send at full speed.
- explanation-03: Slow start is TCP's mechanism for finding a safe sending rate on an unknown path without causing congestive collapse.
- explanation-03: The sender maintains a congestion window (cwnd) in addition to the receiver's advertised window.
- explanation-03: The amount of data in flight is limited by the smaller of the congestion window and the receiver's advertised window.
- explanation-03: Historically, the initial cwnd was 1 segment.
- explanation-03: RFC 6928 specifies the initial window of around 10 segments.
- explanation-03: Slow start continues until a packet loss or ECN mark is detected, or until cwnd reaches the ssthresh threshold.
- explanation-03: A detected packet loss or ECN mark is interpreted as a signal that the network is congested.
- explanation-04: Each thread has its own stack and register state.
- explanation-04: Communication between threads is done by accessing shared memory, with appropriate synchronization.
- explanation-04: Threads sharing memory directly is fast but requires locks or synchronization to avoid race conditions.
- explanation-04: Python's multiprocessing module exists specifically to enable real parallelism for CPU-bound work.
- explanation-04: Using processes for largely independent work avoids race conditions, deadlocks, and lock contention.
- explanation-04: A process-based architecture with workers communicating via queues or sockets generalizes naturally to multiple machines.
- explanation-04: Thread-based designs assume a single shared address space and do not extend across machines.
- explanation-04: Spinning up a full process per connection would be wasteful.
- explanation-05: A collection can be kept reachable by being held by a long-lived singleton.
- explanation-05: A listener's closure often captures its whole surrounding scope, including large objects and DOM nodes.
- explanation-05: A captured closure scope keeps all of the captured objects alive indefinitely.
- explanation-05: Static or global variables accumulating data is another frequent cause of memory leaks.
- explanation-05: Mutual references between long-lived and short-lived objects are another frequent cause of memory leaks.
- explanation-05: Mutual references can keep a short-lived object artificially alive.
- explanation-06: Profiling is cheap.
- explanation-07: Reaching 2-5TB within a year would justify planning for sharding ahead of time.
- explanation-07: Sharding eliminates free ACID guarantees across the whole dataset.
- explanation-07: Partitions map naturally to shards, so partitioning provides leverage if sharding becomes necessary.
- explanation-08: Huge payloads or a hot loop are cases where serialization can account for 40% of request time.
- explanation-08: The second key number is how binary formats compare for the user's actual payload shape.
- explanation-08: Payload characteristics that affect binary format gains include deep nesting, string-heaviness, numeric-heaviness, and repetitiveness.
- explanation-08: A generic claim that binary is faster can be off by an order of magnitude in either direction for a specific schema.
- explanation-08: The profiling and benchmarking work would take a few hours.
- summarization-01: Cold start time has been reduced by roughly 40%.
- summarization-04: PDF export on the Reports page fails silently.
- summarization-04: Clicking the PDF export option initially produces no visible response.
- summarization-05: Ada is assigned to run the payments database migration dry run.
- summarization-05: The payments database migration dry run is due before Thursday.
- summarization-05: Ada is assigned to check with the mobile team's lead about whether the mobile team has been informed of the API deprecation.
- summarization-06: The on-call engineer suspects connection-pool exhaustion in the payments client.
- summarization-08: The template gallery finding is tentative.

Added facts (styled only):

- code-review-01: The code contains four real bugs.
- code-review-01: The four bugs are ordered by severity.
- code-review-01: An alternative fix for the bare `except:` is to catch `Exception` and log it.
- code-review-02: The `async` keyword adds no value in the current version of the function.
- code-review-02: The code has no handling for a missing `name` field.
- code-review-02: If the API returns an object without a `name` property, `profile.name.toUpperCase()` throws.
- code-review-02: Handling a missing `name` field may require a check or a default value, depending on the API contract.
- code-review-03: `%s` is the placeholder syntax for psycopg2.
- code-review-03: `%s` is the placeholder syntax for MySQLdb.
- code-review-03: A customer name like `O'Brien` breaks the query syntax and raises an error.
- code-review-03: Breakage on single quotes happens even without malicious intent.
- code-review-03: Parameterized queries also fix the single-quote problem.
- code-review-03: Database drivers handle escaping in parameterized queries.
- code-review-03: The function doesn't check that `status` is one of the expected values.
- code-review-03: Expected `status` values include "pending", "shipped", and "cancelled".
- code-review-03: Validating `status` against an allow-list prevents typos from reaching the database.
- code-review-03: Validating `status` against an allow-list prevents unexpected queries from reaching the database.
- code-review-04: Under enough concurrent calls, the counter can drift arbitrarily far from the correct total.
- code-review-04: In that interleaving the counter ends at 6 instead of the expected 1.
- code-review-04: Any thread can set counter.value = 100 directly, bypassing increment() and reset().
- code-review-04: Direct attribute assignment would still race even after adding a lock inside the methods, because it does not go through the lock.
- code-review-05: The most dangerous bug is that a failed `cd` does not stop execution.
- code-review-05: `echo Cleaned $BACKUP_DIR` should be quoted for consistency and to preserve exact output, though this is a minor issue.
- code-review-05: Using the glob directly is safer when there are no matching files, since with nullglob-style behavior in most shells the loop will not misfire on a literal `*.log` string.
- code-review-05: `rm -rf *.tmp` gives no feedback and no confirmation before a destructive, irreversible delete.
- code-review-05: The script's shebang is `#!/bin/sh`.
- code-review-05: The script sticks to POSIX-compatible syntax, so there are no bashisms to flag.
- code-review-06: The result shares mutable state with both `base` and `override`.
- code-review-06: Most settings mergers replace lists and non-dict containers rather than merging them.
- code-review-06: The function has no validation, no docstring, and no type hints.
- code-review-06: The absence of validation, docstring, and type hints is not a bug but reduces confidence.
- code-review-06: Replacing a settings section with a flag is a common override pattern.
- code-review-06: In the `else: merged[key] = value` branch, a new key's dict value is assigned by reference rather than copied.
- code-review-06: Mutating the merge result can also mutate the caller's `override`.
- code-review-06: Full replacement for lists and scalars is a reasonable default.
- code-review-06: Dict subclasses or `Mapping` values such as `OrderedDict` or custom config objects fail the `isinstance(merged[key], dict)` check.
- code-review-06: Values that fail the `isinstance` check are treated as opaque values rather than merged.
- code-review-06: The dict-subclass issue only matters if the codebase uses such types for settings.
- code-review-06: The function has no cycle protection.
- code-review-06: A self-referential `base` or `override` would cause infinite recursion.
- code-review-06: Cycle protection is low priority unless settings are ever built dynamically.
- code-review-06: The recommendation is to fix the crash and the aliasing issue before touching call sites.
- code-review-06: Fixing the aliasing requires deep-copying or copying nested structures on paths not touched by the recursion.
- code-review-07: Converting exceptions into `null` is a "fail soft" pattern used deliberately by some older libraries.
- code-review-07: An `attempts` value of 0 or less could occur if `attempts` comes from configuration.
- code-review-07: Changing the function's return behavior would require grepping for `withRetry` usages, or making the change and verifying with the type checker and tests.
- code-review-08: The script has one likely bug.
- code-review-08: The script has two behaviors that look deliberate but need intent confirmation before being trusted.
- code-review-08: APScheduler is an example of an in-process scheduler.
- code-review-08: `os.listdir(ROOT)` raises an exception if the directory does not exist or the process lacks permission.
- code-review-08: Without logging, a bad run leaves no audit trail and deletions would have to be reconstructed from backups.
- code-review-08: The script has no concurrency guard.
- code-review-08: If a run overlaps with the next scheduled trigger, two `clean()` calls can race on the same files and hit the `FileNotFoundError` case.
- debugging-01: The dictionary contains only the key "port" in lowercase.
- debugging-02: Class bodies run in strict mode.
- debugging-04: The file contains a non-ASCII byte at position 512.
- debugging-04: UTF-8 is the most common encoding case for such files.
- debugging-04: The errors="ignore" option drops bad bytes.
- debugging-04: Using errors="replace" or errors="ignore" lets the function handle mixed or unknown encodings without crashing.
- debugging-04: Decoding a UTF-8 file as latin-1 does not raise an error.
- debugging-04: Guessing an encoding incorrectly can silently produce wrong characters.
- debugging-06: Transient network or database-server slowness can delay connection setup and teardown.
- debugging-06: Delayed connection setup and teardown inflates checkout wait time without any leak or contention.
- debugging-06: pg_locks is the Postgres view for checking lock waits.
- debugging-06: Retry logic is a particularly likely place for connection-release bugs in error-handling paths.
- debugging-07: The most likely cause of the failure is a race condition between event creation and digest generation.
- debugging-07: The race condition is made visible only under CI's parallel load.
- debugging-07: Eventual consistency between seed and read is the most likely cause.
- debugging-07: If the API's event-seeding call returns before the event is fully committed or indexed, the test can query the digest before all three writes land.
- debugging-07: Asynchronous queues, outbox patterns, and search-index syncing are examples of mechanisms that can cause a seeding call to return before the event is committed or indexed.
- debugging-07: The eventual-consistency issue would not show up on a dev machine, where the box is otherwise idle and writes finish fast.
- debugging-07: The CI setup uses 4 parallel workers.
- debugging-07: Under 4 parallel CI workers, CPU and I/O contention slow the write path enough to expose the race.
- debugging-07: The test fails about 10% of the time.
- debugging-07: Shared state across parallel workers is the second most plausible cause.
- debugging-07: If workers share a database, cache, or fixed time window instead of each having an isolated schema or tenant, one worker's test can read or evict another worker's data.
- debugging-07: A common trigger is a digest query that filters by a time window, where worker contention delays a seed call past the window boundary and drops it from the digest.
- debugging-07: Silent write failure under load is the third most plausible cause.
- debugging-07: Connection-pool exhaustion or a request timeout at 4x concurrency could cause one of the three seed calls to fail or retry silently.
- debugging-07: A silent seed failure would leave only 2 events actually persisted.
- debugging-07: A silent seed failure goes unnoticed if the test does not check the seed response status.
- debugging-07: Non-unique identifiers colliding across workers is the fourth most plausible cause.
- debugging-07: If events are keyed by coarse-grained values such as a timestamp truncated to the second or a shared sequence counter, two parallel tests could generate colliding keys and one write could overwrite another.
- debugging-07: The test can be reproduced locally under parallel load by running it repeatedly with `pytest -n 4` or higher in a loop.
- debugging-07: An example local reproduction command is `pytest -n 4 tests/test_notifications.py::test_digest_contains_all_events --count=200` using pytest-repeat.
- debugging-07: The `--count` option is provided by the pytest-repeat plugin.
- debugging-07: If the test starts flaking locally under parallel load, that confirms parallelism rather than CI-specific infrastructure is the trigger.
- debugging-07: If the test does not flake locally, CI-specific factors such as a shared DB instance or resource limits should be examined.
- debugging-07: Reading the seed endpoint implementation reveals whether it writes to the primary store directly or enqueues work for a background processor.
- debugging-07: If the seed endpoint is asynchronous, that indicates cause #1.
- debugging-07: The fix for an asynchronous seed endpoint is to have the test poll or wait for a confirmation signal before requesting the digest, rather than adding a sleep.
- debugging-07: The digest builder should be searched for 'last N minutes/events' time-window logic.
- debugging-07: The presence of time-window filtering in the digest query supports cause #2.
- debugging-07: The fix for time-window filtering is to seed events with an explicit, wide-enough time range or to have the test control the clock.
- debugging-07: Each seed call's response status should be verified inside the test, not just its side effect.
- debugging-07: If the test currently ignores the response body or status of the three seed calls, an assertion should be added on each one.
- debugging-07: Asserting on seed responses turns a silent seed failure into an explicit assertion failure at the write site instead of the read site, pinpointing cause #3.
- debugging-07: The CI config should be checked for how pytest-xdist or an equivalent provisions test databases: one shared DB, one DB per worker, or one schema per worker.
- debugging-07: A single shared DB without per-test data scoping via unique tenant or user IDs indicates cause #2 or #4.
- debugging-07: The fix for a lack of worker isolation is either per-worker DB isolation or scoping all test data by a unique run ID.
- debugging-07: CI does not currently keep artifacts from failures.
- debugging-07: Adding pytest-rerunfailures with `--reruns 1 --reruns-delay 1` causes a flake to rerun and logs both attempts.
- debugging-07: Temporarily logging the three event IDs and the digest's returned event IDs on assertion failure, printed to stdout, lands the information in the CI log even without artifact storage.
- debugging-07: A log line showing the digest's returned event IDs and the seeded IDs reveals whether the missing event was ever written.
- debugging-07: That single log line distinguishes between causes 1 and 3 versus causes 2 and 4 in one failing run.
- debugging-07: The test seeds three events.
- debugging-07: Steps 1 through 3 should be done first because they will likely confirm or rule out the race-condition theory within an hour.
- debugging-07: The isolation and identifier-collision theories are harder to verify.
- debugging-08: The evidence points to two leaks stacking on top of each other rather than a single cause.
- debugging-08: One leak is a baseline leak present on every instance regardless of traffic.
- debugging-08: The other leak is a traffic-scaled leak tied to webhook volume.
- debugging-08: Both leaks are true leaks, meaning retained references that outlive garbage collection.
- debugging-08: The growth is not merely a cache that has not yet hit its bound, because usage never drops back to the morning baseline overnight.
- debugging-08: The size-bounded cache is probably not the main driver of the leak.
- debugging-08: A correctly bounded cache cannot grow without limit.
- debugging-08: The cache's bound has not changed in a year.
- debugging-08: If the bounded cache were the whole story, growth would plateau.
- debugging-08: A bound on entry count does not stop growth if entry size increases or if eviction has a bug.
- debugging-08: One candidate cause is unbounded cardinality in metrics or logging, where labels are built from webhook fields such as customer ID or product ID.
- debugging-08: Unbounded metric label cardinality would explain growth with all traffic, faster growth with webhooks specifically, scaling with marketing-week volume, and never shrinking overnight.
- debugging-08: Unbounded label cardinality can be checked by inspecting the metrics client's internal label-set size over time, for example the Prometheus client registry.
- debugging-08: Unbounded label cardinality can be checked by comparing unique label combinations before and after a marketing spike.
- debugging-08: Another candidate cause is broken eviction in the bounded cache, such as an off-by-one in the count check, a key equality or hashing bug preventing dedup, or eviction running on a schedule that lags inserts.
- debugging-08: Broken cache eviction would explain slow baseline growth because product lookups happen even without webhooks.
- debugging-08: Broken cache eviction does not fully explain the webhook-specific acceleration.
- debugging-08: Broken cache eviction can be checked by logging the cache's actual entry count and estimated byte size continuously.
- debugging-08: If the cache entry count exceeds the configured bound, eviction is broken.
- debugging-08: If cache entry count stays flat while heap still grows, the cache is not the cause.
- debugging-08: Another candidate cause is per-webhook object accumulation, such as a dedup/idempotency set of webhook IDs, a retry queue, or an audit log that is unbounded or never expires.
- debugging-08: Per-webhook object accumulation would explain the canary growing slower without webhook traffic while still growing, with webhook traffic adding extra growth.
- debugging-08: Per-webhook object accumulation can be checked by searching webhook handler code for any global list, set, or map appended per event and never removed or expired.
- debugging-08: Per-webhook object accumulation can be checked by heap-dump diffing an instance under load against the canary and comparing counts of webhook-related object types.
- debugging-08: Another candidate cause is leaked threads, connections, or event listeners registered per webhook and not torn down.
- debugging-08: Leaked threads or connections would explain webhook-driven acceleration.
- debugging-08: Each leaked thread or connection retains its own stack and buffers, which would explain steady growth that never reverts.
- debugging-08: Leaked threads or connections can be checked by tracking live thread count and open connection or file-descriptor count over the week, not just heap size.
- debugging-08: If thread and connection counts climb in lockstep with memory, leaked threads or connections are likely the cause.
- debugging-08: The first recommended check is tracking thread count, open connections, and cache entry count over a full week alongside heap size.
- debugging-08: Tracking threads, connections, and cache entry count is cheap and immediately reveals whether the leak is object-based (heap only) or resource-based (threads/connections track memory too).
- debugging-08: The second recommended check is taking two heap dumps on the canary a day apart and diffing object counts by class.
- debugging-08: Diffing two canary heap dumps isolates the baseline leak because the canary removes webhook traffic as a variable.
- debugging-08: The third recommended check is taking a heap dump on a normal instance during a marketing spike and diffing it against the canary dump.
- debugging-08: The difference between the spike heap dump and the canary dump should point directly at the webhook-driven component.
- debugging-08: The fourth recommended check is examining the metrics/logging client's internal state size.
- debugging-08: The metrics/logging client's internal state is the most common root cause for this pattern of bounded cache untouched, growth scaling with traffic, and memory never reclaimed.
- debugging-08: Metrics client state size is easy to rule in or out by reading the label cardinality.
- debugging-08: The candidate list will narrow quickly once a heap dump is available.
- debugging-08: The candidate list is currently ranked by fit to the four observations, not by certainty.
- explanation-01: Load factor is the ratio of entries to slots.
- explanation-01: Many general-purpose hash maps use chaining.
- explanation-01: Java's HashMap uses chaining.
- explanation-01: Performance-critical implementations tend to use open addressing.
- explanation-01: Rust's HashMap uses open addressing.
- explanation-02: Web applications where a user loads a form, edits it, and submits minutes later are a case where conflicts are infrequent.
- explanation-02: Optimistic locking scales better under high read concurrency.
- explanation-02: Short, fast transactions where wait time is negligible are an example where pessimistic locking fits.
- explanation-03: After a packet loss, the sender cuts ssthresh, commonly to half the current cwnd.
- explanation-03: After a packet loss, the sender either restarts slow start from a small window or drops into congestion avoidance, depending on the TCP variant.
- explanation-04: A process boundary contains the damage when a unit of work crashes or hangs.
- explanation-04: The OS can give processes separate memory and CPU limits.
- explanation-04: A GUI keeping its interface responsive while a background thread loads a file is an example of work suited to threads.
- explanation-05: UI components and event buses are examples of long-lived objects that listeners get registered on.
- explanation-05: Using bounded caches with eviction, such as an LRU, is a fix for memory leaks from unbounded collections.
- explanation-05: Weak references can be used to avoid memory leaks in languages that support them.
- explanation-06: A cache in front of the database does not help when slowness comes from a downstream API call.
- explanation-06: Using a cache requires paying the cost of checking the cache.
- explanation-06: APM tools can be used to profile a service.
- explanation-06: Datadog is an APM tool.
- explanation-06: New Relic is an APM tool.
- explanation-06: Timing logs can be added around each layer to profile a service, including request handling, database queries, and external calls.
- explanation-06: Database logs or metrics can show the ratio of SELECT queries to INSERT/UPDATE/DELETE queries.
- explanation-07: Cloud-managed Postgres instances often support tens of terabytes before storage becomes a hard limit.
- explanation-07: Global uniqueness is an example of a constraint that is harder to enforce across shards.
- explanation-07: A single primary that cannot keep up with write load causes latency spikes or replication lag.
- explanation-08: If JSON encode/decode is 2% of request time, a 10x faster format saves about 1.8% of total request time overall.
- explanation-08: A 1.8% overall improvement is not worth the cost of migrating serialization formats.
- explanation-08: Binary formats only address the parsing and transfer portions of request time.
- explanation-08: Binary formats mainly help when payloads are large or bandwidth-constrained.
- explanation-08: For small payloads, the fixed overhead of parsing often dominates and the gain from a binary format shrinks.
- explanation-08: Binary formats typically reduce serialized size by 20-60% compared to JSON.
- explanation-08: Binary formats typically reduce parsing time by 2-10x compared to JSON.
- explanation-08: Deeply nested objects benefit more from binary formats than flat key-value data does.
- explanation-08: If serialization is under roughly 5-10% of request time, switching to a binary format likely isn't worth the added complexity.
- explanation-08: Binary formats add complexity in the form of schema management, tooling, and debugging opacity.
- summarization-01: Each button's tooltip shows that button's keyboard shortcut.
- summarization-02: The incident affected roughly 12% of checkout requests.
- summarization-05: Ada is assigned to confirm that a dry run for the payments database migration happens.
- summarization-06: The likely cause of the incident is connection-pool exhaustion in the payments client.
- summarization-07: The memory growth should be profiled before rollout.
- summarization-07: The crash should be investigated before rollout.
- summarization-08: The field-mapping result is the strongest result in the study.

### clarity-flow

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 27 | 24 | 0.889 | 26 | 3 |
| code-review-02 | 17 | 15 | 0.882 | 20 | 3 |
| code-review-03 | 27 | 16 | 0.593 | 18 | 5 |
| code-review-04 | 26 | 14 | 0.538 | 17 | 1 |
| code-review-05 | 33 | 22 | 0.667 | 20 | 1 |
| code-review-06 | 29 | 22 | 0.759 | 33 | 7 |
| code-review-07 | 40 | 27 | 0.675 | 23 | 4 |
| code-review-08 | 29 | 17 | 0.586 | 37 | 9 |
| debugging-01 | 7 | 6 | 0.857 | 7 | 0 |
| debugging-02 | 18 | 15 | 0.833 | 12 | 1 |
| debugging-03 | 13 | 12 | 0.923 | 8 | 0 |
| debugging-04 | 15 | 10 | 0.667 | 13 | 2 |
| debugging-05 | 19 | 18 | 0.947 | 11 | 2 |
| debugging-06 | 35 | 17 | 0.486 | 24 | 3 |
| debugging-07 | 2 | 1 | 0.5 | 23 | 23 |
| debugging-08 | 1 | 0 | 0.0 | 30 | 30 |
| explanation-01 | 37 | 29 | 0.784 | 20 | 2 |
| explanation-02 | 32 | 22 | 0.688 | 24 | 3 |
| explanation-03 | 28 | 12 | 0.429 | 19 | 2 |
| explanation-04 | 35 | 24 | 0.686 | 24 | 0 |
| explanation-05 | 16 | 12 | 0.75 | 12 | 0 |
| explanation-06 | 16 | 14 | 0.875 | 16 | 3 |
| explanation-07 | 21 | 13 | 0.619 | 27 | 9 |
| explanation-08 | 15 | 7 | 0.467 | 14 | 3 |
| summarization-01 | 6 | 6 | 1.0 | 6 | 1 |
| summarization-02 | 11 | 7 | 0.636 | 16 | 5 |
| summarization-03 | 15 | 15 | 1.0 | 13 | 0 |
| summarization-04 | 14 | 13 | 0.929 | 12 | 0 |
| summarization-05 | 9 | 9 | 1.0 | 11 | 0 |
| summarization-06 | 15 | 15 | 1.0 | 13 | 0 |
| summarization-07 | 14 | 14 | 1.0 | 17 | 0 |
| summarization-08 | 21 | 18 | 0.857 | 24 | 2 |

Median fraction: 0.754 over 32 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: The function performs no validation on `name`, such as checking for an empty string or wrong type.
- code-review-01: The function performs no validation that `roles` is actually a list.
- code-review-01: A `True`/`False` return value tells the caller nothing about why the call failed or what was inserted, such as a created user ID.
- code-review-02: Declaring a function `async` without using `await` is a strong signal the promise chain was meant to be awaited but isn't.
- code-review-02: `fetch` only rejects on network failure.
- code-review-03: Stacked queries can enable worse attacks, depending on the database driver.
- code-review-03: If `customer_name` or `status` is not a string (e.g. `None`), the `+` concatenation raises a `TypeError`.
- code-review-03: A `TypeError` from concatenation is raised instead of a meaningful error.
- code-review-03: The code does not handle `fetchall()` on large result sets.
- code-review-03: If a customer has many orders, `fetchall()` loads everything into memory at once.
- code-review-03: Pagination or `fetchmany()` is worth considering for large datasets.
- code-review-03: The code has no error handling around `cursor.execute`.
- code-review-03: A database error such as a bad connection or a locked table will propagate as a raw exception with no context about what operation failed.
- code-review-03: Exact string matching makes the query case-sensitive.
- code-review-03: Case-insensitive matching or normalization such as trimming whitespace may be wanted, depending on requirements.
- code-review-03: The SQL injection must be fixed before the code goes to production.
- code-review-04: This read-modify-write pattern is a TOCTOU (time-of-check-to-time-of-use) bug.
- code-review-04: CPython has a GIL (Global Interpreter Lock).
- code-review-04: The GIL only guarantees that individual bytecode operations are atomic.
- code-review-04: The GIL can switch threads between the read and the write of a read-modify-write sequence.
- code-review-04: With enough concurrent increments, updates will reliably be lost.
- code-review-04: 100,000 increments from 10 threads will often produce a final value less than 100,000.
- code-review-04: Every method of the class is unsafe to call concurrently with any other method, including itself.
- code-review-04: A single attribute read or write is atomic in CPython.
- code-review-04: Reading counter.value will not return garbage.
- code-review-04: Nothing in the class signals to callers that reading .value as part of a larger operation is dangerous.
- code-review-04: itertools.count() is thread-safe in CPython.
- code-review-04: itertools.count() and multiprocessing.Value are lock-free alternatives worth considering for higher throughput under heavy contention.
- code-review-05: With an empty `BACKUP_DIR`, `cd $BACKUP_DIR` becomes a bare `cd`.
- code-review-05: A bare `cd` changes to `$HOME`.
- code-review-05: A caller could pass `/` or `/home` and the script would `cd` there and delete `*.tmp` files.
- code-review-05: `for f in $(ls *.log)` mishandles filenames starting with `-` or containing glob-special characters.
- code-review-05: When `ls *.log` matches nothing, the loop harmlessly does not execute.
- code-review-05: In plain `sh`/dash an unmatched glob does not match, so the literal-glob issue does not arise there.
- code-review-05: `gzip` can fail on a read-only file or an already-gzipped file.
- code-review-05: The script should print something like `Usage: $0 <backup_dir>` and exit when `$1` is missing.
- code-review-05: The `-f` flag in `rm -rf *.tmp` suppresses errors.
- code-review-05: Suppressing errors with `-f` is fine for the no-match case but also silently masks permission errors.
- code-review-05: The suggested rewrite adds an argument check, quotes all variables, avoids parsing `ls`, guards against the no-match glob case, and uses `set -eu` so failures stop the script.
- code-review-06: The list-replacement behavior is inconsistent with the function's dict-merging behavior.
- code-review-06: The function has four distinct branch behaviors: adding new keys, deleting keys on None, recursively merging dict-vs-dict, and overwriting everything else.
- code-review-06: pop(key, None) does not crash when the key being deleted is absent from merged.
- code-review-06: The function has no naming or documentation distinguishing its four behaviors.
- code-review-06: The shallow copy of unmerged nested structures is very unlikely to be intentional.
- code-review-06: There are currently no tests for the code.
- code-review-06: Writing tests that pin down current behavior before changing anything is the recommended approach.
- code-review-07: The zero first delay appears to be an off-by-one error where i + 1 was likely intended.
- code-review-07: The zero-delay first backoff is not documented and is inconsistent with the rest of the backoff logic.
- code-review-07: On the final loop iteration, a 429 still triggers the setTimeout wait before the loop exits.
- code-review-07: The delay on the final attempt is wasted because there is no subsequent attempt.
- code-review-07: Errors without an err.status property have err.status equal to undefined.
- code-review-07: For undefined status, both undefined === 429 and undefined >= 500 evaluate to false.
- code-review-07: Swallowing errors as null is the riskiest issue because it hides programming errors rather than only HTTP failures.
- code-review-07: There is no upper bound check on err.status >= 500.
- code-review-07: Any status of 500 or greater, including nonstandard or custom codes, is treated as retryable.
- code-review-07: There is no err.status < 600 guard, so the condition means '>= 500' rather than '5xx'.
- code-review-07: When attempts <= 0, the function returns undefined without ever calling fn.
- code-review-07: There is no validation or error raised for an attempts value of 0 or less.
- code-review-07: Combined with the null swallow, an outage would be indistinguishable from everything returning null.
- code-review-08: The `removed < 500` condition gates only the `elif` branch.
- code-review-08: The `if` branch handling tmp/.part files has no removal cap.
- code-review-08: The 500-removal cap does not bound I/O per run for the tmp/.part branch.
- code-review-08: Calling `os.path.getmtime` on a broken symlink raises `FileNotFoundError`.
- code-review-08: The script has no logging, dry-run mode, or audit trail.
- code-review-08: The script returns only an integer count.
- code-review-08: In the snippet, the returned count is not printed or logged anywhere.
- code-review-08: `os.listdir()` returns entries in filesystem order, not sorted by mtime.
- code-review-08: The script does not select files oldest-first for the 500 cap.
- code-review-08: Immediate deletion of tmp-/.part files could be deliberate if writer processes rename atomically on completion.
- code-review-08: The script does not own the system that produces the tmp-/.part files.
- code-review-08: No one owns the script's schedule.
- debugging-01: Accessing cfg['Port'] when the key is 'port' raises a KeyError.
- debugging-02: The global object is referred to as `window` or `globalThis`.
- debugging-02: Accessing `this.seconds` throws if `this` is `undefined` in strict mode.
- debugging-02: The `NaN` value is logged and reassigned on each tick of the interval.
- debugging-03: The fixed `moving_sum` function appends `sum(values[i : i + window])` to a list for each index `i` and returns that list.
- debugging-04: The byte 0xc3 suggests UTF-8-encoded characters such as accented letters like é.
- debugging-04: Under strict ascii decoding, any byte greater than or equal to 0x80 causes an error.
- debugging-04: A file can be opened in binary mode with the "rb" mode string.
- debugging-04: Counting occurrences of b"\n" in binary mode yields a line count.
- debugging-04: Opening the file in binary mode avoids decoding entirely.
- debugging-05: The fixed code is `def make_post(title, tags=None)` with `if tags is None: tags = list(DEFAULT_TAGS)`, then `tags.append("post")`, then `return {"title": title, "tags": tags}`.
- debugging-06: The working directory is empty.
- debugging-06: There is no code to inspect, so the task is pure log analysis.
- debugging-06: Dashboard refreshes and scheduled analytics queries are examples of unpredictable analytics traffic spikes.
- debugging-06: A slow analytics query can be caused by a missing index or a table scan.
- debugging-06: If a code path fails to release a connection on error, the pool slowly shrinks overnight until it is exhausted.
- debugging-06: Weekly failure frequency could line up with a periodic batch job, a deploy, or a data-volume spike.
- debugging-06: A mismatch between pool size and instance/replica count is a plausible cause.
- debugging-06: If a service scaled up its workers or replicas without raising the database max-connections or pool size, exhaustion becomes a matter of timing rather than a deterministic bug.
- debugging-06: Pool-level metrics such as active, idle, and waiting connections over time should be gathered from both services.
- debugging-06: Some database drivers or ORMs expose pool metrics such as checked-out connections and wait queue length.
- debugging-06: Retention for metrics is often longer than log retention and cheaper to keep.
- debugging-06: Checking database-side logs can reveal what was holding connections at 02:14:07-02:14:41.
- debugging-06: The failure window on the observed night spanned 02:14:07 to 02:14:41.
- debugging-06: Increasing log retention or adding sampling for pool stats would avoid being left with only rotated log fragments next time.
- debugging-06: The available logs are rotated fragments.
- debugging-06: Comparing pool configuration against total client count is a way to narrow down the cause.
- debugging-06: The comparison involves the sum of max pool size across all export workers and analytics service instances versus the database's max_connections.
- debugging-06: If total configured pool size is close to the database's max_connections, a small ephemeral spike such as a deploy restart or an extra worker is enough to exhaust it.
- debugging-07: There is memory that may be relevant to the task.
- debugging-08: The session ID is 4988878c-7c4a-4c17-92eb-92beb2d5be32.
- explanation-01: A hash map's underlying array has only one slot per index.
- explanation-01: Chaining is also known as separate chaining.
- explanation-01: Quadratic probing jumps by increasing squares.
- explanation-01: Hitting an empty slot during an open addressing lookup means the key does not exist.
- explanation-01: Deletion in open addressing is trickier and must use tombstones or rehashing.
- explanation-01: Java's HashMap is a general-purpose language implementation that picks a collision strategy based on these trade-offs.
- explanation-01: Python's dict uses open addressing internally.
- explanation-01: Go's map uses a bucket-based chaining variant.
- explanation-02: An optimistic locking example uses a `products` table with a `version` integer column.
- explanation-02: An optimistic stock update can be written as `UPDATE products SET stock = stock - 1, version = version + 1 WHERE id = 42 AND version = 7;`.
- explanation-02: Optimistic locking fits when transactions are short and fast.
- explanation-02: Examples of good fits for optimistic locking include a web app editing user profiles, e-commerce catalog updates, and most CRUD APIs.
- explanation-02: A pessimistic transfer example uses BEGIN, two `SELECT balance FROM accounts WHERE id = ... FOR UPDATE` statements, balance updates, and COMMIT.
- explanation-02: In some databases, `FOR UPDATE` prevents other transactions from even reading the locked rows.
- explanation-02: Financial transfers, inventory reservation for a flash sale, and seat booking systems are examples where pessimistic locking fits.
- explanation-02: Optimistic locking requires more code to handle retries.
- explanation-02: Pessimistic locking gives simpler conflict handling.
- explanation-02: Pessimistic locking risks contention and deadlocks.
- explanation-03: A network path may consist of a single fast link or may cross several routers of varying speed and load.
- explanation-03: If a sender transmitted at whatever rate the receiver's window allowed, it could send more data than routers along the path can forward.
- explanation-03: When packets are dropped, senders retransmit them.
- explanation-03: Persistent overloading of the network causes congestive collapse.
- explanation-03: In congestive collapse, throughput drops sharply even though all senders are trying to send at full speed.
- explanation-03: Slow start is TCP's mechanism for finding a safe sending rate on an unknown path without causing congestive collapse.
- explanation-03: The sender maintains a congestion window (cwnd) in addition to the receiver's advertised window.
- explanation-03: The amount of data in flight is limited by the smaller of the congestion window and the receiver's advertised window.
- explanation-03: Historically, the initial cwnd was 1 segment.
- explanation-03: Modern TCP implementations typically start with an initial cwnd of around 10 segments.
- explanation-03: RFC 6928 specifies the initial window of around 10 segments.
- explanation-03: A full window of data generates a full window of ACKs.
- explanation-03: Slow start continues until a packet loss or ECN mark is detected, or until cwnd reaches the ssthresh threshold.
- explanation-03: A detected packet loss or ECN mark is interpreted as a signal that the network is congested.
- explanation-03: ssthresh is the name of the slow start threshold.
- explanation-03: In congestion avoidance, cwnd growth is linear, roughly +1 segment per RTT.
- explanation-04: A process is an independent execution unit with its own memory address space, file descriptors, and OS resources.
- explanation-04: All threads in a process share the same memory address space, heap, and file descriptors.
- explanation-04: Each thread has its own stack and register state.
- explanation-04: A crash in one thread, such as a segfault, usually kills the whole process.
- explanation-04: The higher cost of processes comes from separate memory spaces and OS bookkeeping.
- explanation-04: Python and older Ruby are languages with a GIL.
- explanation-04: Python's multiprocessing module exists specifically to enable real parallelism for CPU-bound work.
- explanation-04: A crashed worker process can be restarted without affecting other processes.
- explanation-04: Using processes for largely independent work avoids race conditions, deadlocks, and lock contention.
- explanation-04: A process-based architecture with workers communicating via queues or sockets generalizes naturally to multiple machines.
- explanation-04: Thread-based designs assume a single shared address space and do not extend across machines.
- explanation-05: The event source holds a reference to the registered listener.
- explanation-05: A listener's closure often captures its whole surrounding scope, including large objects and DOM nodes.
- explanation-05: Mutual references between long-lived and short-lived objects are another frequent cause of memory leaks.
- explanation-05: Mutual references can keep a short-lived object artificially alive.
- explanation-06: Profiling is cheap.
- explanation-06: Timing middleware and slow query logs are examples of basic profiling.
- explanation-07: Reaching 2-5TB within a year would justify planning for sharding ahead of time.
- explanation-07: Sharding multiplies operational complexity, including migrations, cross-shard joins and transactions, and rebalancing.
- explanation-07: Under sharding, cross-shard transactions and joins become application-level problems.
- explanation-07: Sharding eliminates free ACID guarantees across the whole dataset.
- explanation-07: PostgreSQL has native table partitioning that can partition by tenant or date.
- explanation-07: Logical partitioning is far cheaper to implement than sharding.
- explanation-07: Partitions map naturally to shards, so partitioning provides leverage if sharding becomes necessary.
- explanation-07: Logical partitioning buys time to observe growth rate before committing to a shard key.
- explanation-08: If JSON parsing is 2% of request time, a binary format that parses 3x faster saves about 1.3% end-to-end.
- explanation-08: Huge payloads or a hot loop are cases where serialization can account for 40% of request time.
- explanation-08: The second key number is how binary formats compare for the user's actual payload shape.
- explanation-08: Gains from Protobuf, msgpack, and FlatBuffers vary a lot depending on the payload shape.
- explanation-08: Payload characteristics that affect binary format gains include deep nesting, string-heaviness, numeric-heaviness, and repetitiveness.
- explanation-08: A generic claim that binary is faster can be off by an order of magnitude in either direction for a specific schema.
- explanation-08: Profiling a representative request path would show time spent in serialize/deserialize versus network, DB, and business logic.
- explanation-08: The profiling and benchmarking work would take a few hours.
- summarization-02: Staging's connection pool size is intentionally small at 5.
- summarization-02: Detection lag was approximately 7 minutes.
- summarization-02: Total impact was approximately 34 minutes.
- summarization-02: Error onset occurred at 09:14.
- summarization-04: PDF export on the Reports page fails silently.
- summarization-08: The abandonment finding is firm, but the cause of the abandonment is tentative.
- summarization-08: The small sample size cannot confirm the mechanism behind the progress bar abandonment.
- summarization-08: The template gallery finding is tentative.

Added facts (styled only):

- code-review-01: The function has five distinct problems.
- code-review-01: The recommended fix for the bare `except` is to catch a specific exception, such as whatever `db.insert` raises, and log it.
- code-review-01: The cleaner version raises `ValueError("db is required")` when `db` is `None`.
- code-review-02: The `async` keyword is pointless in this function.
- code-review-02: There is no guard on `data.name`.
- code-review-02: If the API response does not include `name`, `.toUpperCase()` throws even after a successful fetch.
- code-review-03: An attacker can exfiltrate data via a `UNION SELECT` injection.
- code-review-03: With parameterized queries, the database driver handles escaping.
- code-review-03: Validating `status` early is cheap to check.
- code-review-03: The function does not handle the case where the query returns no rows.
- code-review-03: Callers should be confirmed to expect an empty list rather than `None` or an exception when no rows are returned.
- code-review-04: The property stops callers from touching `_value` directly and bypassing the lock.
- code-review-05: If no .tmp files exist, `*.tmp` expands to the literal string `*.tmp` and rm errors out.
- code-review-06: The function has one real bug.
- code-review-06: The partial copy may have been an intentional performance tradeoff to avoid copying untouched branches.
- code-review-06: Nothing in the code signals that relying on the partial copy is safe.
- code-review-06: There is no recursion depth guard.
- code-review-06: Deeply nested configs could hit Python's recursion limit.
- code-review-06: Replacing rather than merging lists is reasonable for settings but undocumented.
- code-review-06: The type-mismatch crash and the shallow-copy aliasing are the two issues that should be fixed or tested before trusting the function in production.
- code-review-07: Callers that previously caught specific errors from `fn` will now silently receive null instead.
- code-review-07: The code has no maximum backoff cap, so the wait time grows unbounded as the `attempts` value increases.
- code-review-07: The default value of `attempts` is 3.
- code-review-07: The absence of a backoff cap is fragile if someone raises the `attempts` value.
- code-review-08: The script has one serious bug and several risky gaps.
- code-review-08: The unconditional deletion branch should almost certainly use the same age check as the second branch.
- code-review-08: Nothing else in the script suggests the author wanted to race against active writers.
- code-review-08: The script has no locking to prevent overlapping runs.
- code-review-08: If two invocations overlap, both list the same directory.
- code-review-08: Overlapping invocations each count toward their own 500-item cap independently.
- code-review-08: Independent per-run caps mean the 500-item cap stops bounding anything.
- code-review-08: Typical cron scheduling runs a fresh process each invocation.
- code-review-08: The user said the schedule was not set up by their team.
- debugging-02: The arrow function is the cleanest of these options here.
- debugging-04: UTF-8 is a superset of ASCII.
- debugging-04: errors="replace" should only be used when exact byte fidelity is not required.
- debugging-05: The assertion only holds when this test runs first and alone.
- debugging-05: The fixed version creates a fresh `["draft"]` list on every call.
- debugging-06: Metrics spiking near the pool's max size right before 02:14 would confirm contention rather than a leak.
- debugging-06: The export job's pool size or connection lifetime configuration may have changed recently.
- debugging-06: The incident currently has no reproduction.
- debugging-07: A test that fails under 4-way parallelism but never fails serially indicates a race or shared-state bug rather than inherently random behavior.
- debugging-07: Race and shared-state bugs only expose themselves under contention.
- debugging-07: There are three most likely causes of this failure pattern.
- debugging-07: One likely cause is the digest being read before all events are committed or visible.
- debugging-07: If event creation triggers async work such as a queue, background indexer, or eventual-consistency store, the digest query can race that pipeline.
- debugging-07: Contention from other workers can be enough to slow the write past the read.
- debugging-07: Digest reads racing an async pipeline is the most common source of this symptom.
- debugging-07: A second likely cause is cross-test state leakage under parallel workers.
- debugging-07: If workers share a database, event store, or global fixture instead of each having an isolated schema or tenant, a concurrently running test can overwrite or evict one of the three events.
- debugging-07: A third likely cause is a time-window filter in the digest query.
- debugging-07: If the digest is defined as events in the last N seconds or minutes, a slow CI worker under load can push the first seeded event's timestamp outside the window before the digest runs.
- debugging-07: The test can be run locally under contention with `pytest -n 4 --count=50`.
- debugging-07: The `-n` flag is provided by the `pytest-xdist` plugin.
- debugging-07: The `--count` flag is provided by the `pytest-repeat` plugin.
- debugging-07: A local failure under parallelism confirms the problem is contention-driven and enables faster iteration than waiting on CI.
- debugging-07: Reading the digest fetch path can reveal async or windowed behavior.
- debugging-07: Checking whether event creation and digest retrieval hit the same synchronous DB transaction, or whether either goes through a queue, cache, or time filter, will usually point directly at the async-race cause or the time-window cause.
- debugging-07: Fixture and worker isolation can be checked by grepping for module- or session-scoped fixtures, shared connection strings, or hardcoded IDs such as tenant, user, or event namespace.
- debugging-07: Hardcoded IDs can collide across `pytest-xdist` workers.
- debugging-07: The CI system keeps no artifacts.
- debugging-07: Temporary diagnostic logging can print the seeded event IDs and the digest's returned event IDs on assertion failure.
- debugging-07: Such diagnostic logging converts a '1 event missing' failure into knowing which event was missing and whether it was written or just not read.
- debugging-07: The four narrowing-down steps are ordered by increasing effort.
- debugging-08: The observed pattern indicates two separate memory leaks rather than one.
- debugging-08: One leak is a baseline leak that occurs even without webhook traffic.
- debugging-08: The second leak scales with request volume.
- debugging-08: The cache is a plausible carrier for the baseline leak.
- debugging-08: Per-request/webhook state is the likely carrier for the traffic-scaling leak.
- debugging-08: The canary instance receives no webhooks.
- debugging-08: The canary's memory still grows despite receiving no webhooks.
- debugging-08: Growth without traffic implies something runs regardless of traffic, such as scheduled jobs, background cache refreshes, connection keep-alives, or thread-local accumulation.
- debugging-08: There is a size-bounded cache in the system that went unnoticed.
- debugging-08: A bound on cache entry count does not cap memory growth if the average entry size increases.
- debugging-08: Product payloads may have grown larger over the past year through added images or variants.
- debugging-08: Eviction can remove the primary map entry while leaving the object reachable through a secondary index, listener, or LRU list node.
- debugging-08: A flat cache entry count combined with rising memory indicates entries are growing in size rather than multiplying in number.
- debugging-08: Logging cache.size() alongside RSS over several days can distinguish entry growth from entry multiplication.
- debugging-08: Comparing average serialized entry size now versus a year ago can reveal entry size growth.
- debugging-08: A thread dump and jmap histogram taken from the canary at two points a day apart can be diffed by retained counts per class.
- debugging-08: Memory growth accelerates during marketing campaigns.
- debugging-08: Memory growth is worse on webhook-receiving instances than on the canary.
- debugging-08: The campaign correlation points to per-request accumulation, such as an idempotency/dedupe map keyed by order or correlation ID, a retry queue, or an event listener registered per webhook and never removed.
- debugging-08: Global mutable collections such as static maps or lists touched in the webhook handler path can be found by grepping.
- debugging-08: A tight correlation between daily growth percentage and request volume confirms a per-request leak.
- debugging-08: The canary's residual growth represents the floor of the baseline leak.
- debugging-08: Eclipse MAT can be used to diff object counts between two heap dumps taken a day apart.
- debugging-08: Memory usage never drops overnight in this system.
- debugging-08: The command `jcmd <pid> GC.run` forces a full garbage collection.
- debugging-08: If RSS does not fall after a forced full GC during a quiet period, the objects are genuinely reachable and the leak is real rather than a garbage collector timing artifact.
- debugging-08: No heap profile has been taken yet.
- debugging-08: The fastest next step is taking a jmap histogram or MAT dump from both the canary and a live instance, a day apart.
- debugging-08: Such heap dumps will reveal which classes are actually accumulating.
- debugging-08: The heap dumps will settle which of the two leak candidates, or both, is real.
- explanation-01: The trade-off between chaining and open addressing comes down to memory and worst-case behavior.
- explanation-01: Chaining is recommended when the load factor is expected to vary or when entries are large.
- explanation-02: A document-editing table can have a version column for optimistic locking.
- explanation-02: An optimistic save can run UPDATE docs SET content = ?, version = version + 1 WHERE id = ? AND version = ?.
- explanation-02: Optimistic locking fits low-contention, read-heavy workloads.
- explanation-03: Historically, the initial congestion window was a few packets.
- explanation-03: The slow start threshold is based on past experience with the path.
- explanation-06: If data changes so often that cache entries go stale before reuse, a cache adds complexity without much payoff.
- explanation-06: A slow API can be caused by the database, a slow downstream API, unindexed queries, network latency, or slow serialization code.
- explanation-06: Profiling data indicates which endpoints or queries to target with a cache.
- explanation-07: Revenue projections, user signups, and upcoming feature launches can serve as proxies for estimating database growth.
- explanation-07: Read-heavy workloads can be scaled with read replicas, connection pooling, and caching without sharding.
- explanation-07: A bad shard key choice causes hot shards and frequent cross-shard joins.
- explanation-07: Sharding early diverts engineering time from product work to infrastructure.
- explanation-07: Sharding early can leave the real bottleneck, such as missing indexes, unaddressed.
- explanation-07: Vertical scaling and read replicas run out of headroom faster than expected when growth is front-loaded.
- explanation-07: Write throughput, connection saturation, and table growth rate should be tracked monthly.
- explanation-07: The sharding trigger should be a concrete operational metric, such as primary CPU/IOPS sustained above 70% or degrading write latency under peak load, rather than a size threshold.
- explanation-07: Sharding should be revisited when the defined trigger is hit or when the product team can commit to a stable, mostly-single-shard access pattern.
- explanation-08: If payloads are small, network and connection overhead likely dominate.
- explanation-08: If payloads are small, a binary format will not improve performance much.
- explanation-08: If payloads are large, both serialization time and transfer time matter more.
- summarization-01: Keyboard shortcuts have been added for the user's ten most-used actions.
- summarization-02: The incident was detected at 09:14.
- summarization-02: The on-call engineer was paged at 09:21.
- summarization-02: The time from page to rollback was 34 minutes.
- summarization-02: The team's response time on this incident was good.
- summarization-02: The team has not yet fixed the root cause.
- summarization-08: The large-file upload finding is tentative but worth prioritizing.
- summarization-08: The observation that nobody used the template gallery is not yet a finding.

### classic-concise

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 27 | 23 | 0.852 | 22 | 3 |
| code-review-02 | 17 | 14 | 0.824 | 17 | 1 |
| code-review-03 | 27 | 17 | 0.63 | 14 | 0 |
| code-review-04 | 26 | 18 | 0.692 | 22 | 0 |
| code-review-05 | 33 | 22 | 0.667 | 21 | 5 |
| code-review-06 | 29 | 15 | 0.517 | 29 | 12 |
| code-review-07 | 40 | 27 | 0.675 | 30 | 7 |
| code-review-08 | 29 | 23 | 0.793 | 29 | 2 |
| debugging-01 | 7 | 6 | 0.857 | 6 | 0 |
| debugging-02 | 18 | 10 | 0.556 | 8 | 0 |
| debugging-03 | 13 | 9 | 0.692 | 7 | 0 |
| debugging-04 | 15 | 10 | 0.667 | 10 | 0 |
| debugging-05 | 19 | 18 | 0.947 | 12 | 2 |
| debugging-06 | 35 | 18 | 0.514 | 34 | 11 |
| debugging-07 | 2 | 1 | 0.5 | 25 | 25 |
| debugging-08 | 1 | 0 | 0.0 | 36 | 36 |
| explanation-01 | 37 | 29 | 0.784 | 22 | 5 |
| explanation-02 | 32 | 27 | 0.844 | 20 | 5 |
| explanation-03 | 28 | 20 | 0.714 | 25 | 1 |
| explanation-04 | 35 | 24 | 0.686 | 24 | 2 |
| explanation-05 | 16 | 10 | 0.625 | 11 | 1 |
| explanation-06 | 16 | 9 | 0.562 | 14 | 2 |
| explanation-07 | 21 | 15 | 0.714 | 34 | 6 |
| explanation-08 | 15 | 7 | 0.467 | 15 | 9 |
| summarization-01 | 6 | 5 | 0.833 | 9 | 4 |
| summarization-02 | 11 | 6 | 0.545 | 12 | 2 |
| summarization-03 | 15 | 14 | 0.933 | 12 | 0 |
| summarization-04 | 14 | 11 | 0.786 | 11 | 0 |
| summarization-05 | 9 | 8 | 0.889 | 10 | 0 |
| summarization-06 | 15 | 15 | 1.0 | 14 | 0 |
| summarization-07 | 14 | 14 | 1.0 | 18 | 3 |
| summarization-08 | 21 | 20 | 0.952 | 22 | 0 |

Median fraction: 0.703 over 32 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: If `"member"` is already in `roles`, it is appended again, producing `["member", "member"]`.
- code-review-01: The suggested fix copies the caller's list with `list(roles)` to avoid mutating it.
- code-review-01: The suggested fix appends `"member"` only if it is not already in `roles`.
- code-review-01: The suggested fix makes `db` a required parameter.
- code-review-02: Declaring a function `async` without using `await` is a strong signal the promise chain was meant to be awaited but isn't.
- code-review-02: `fetch` only rejects on network failure.
- code-review-02: The fixed version awaits `res.json()` and returns `data.name.toUpperCase()`.
- code-review-03: Passing `status` as `' OR '1'='1` returns every order.
- code-review-03: The code has no input validation or type checking.
- code-review-03: If `customer_name` or `status` is not a string (e.g. `None`), the `+` concatenation raises a `TypeError`.
- code-review-03: A `TypeError` from concatenation is raised instead of a meaningful error.
- code-review-03: Pagination or `fetchmany()` is worth considering for large datasets.
- code-review-03: The code has no error handling around `cursor.execute`.
- code-review-03: A database error such as a bad connection or a locked table will propagate as a raw exception with no context about what operation failed.
- code-review-03: Exact string matching makes the query case-sensitive.
- code-review-03: Case-insensitive matching or normalization such as trimming whitespace may be wanted, depending on requirements.
- code-review-03: The SQL injection must be fixed before the code goes to production.
- code-review-04: This read-modify-write pattern is a TOCTOU (time-of-check-to-time-of-use) bug.
- code-review-04: With enough concurrent increments, updates will reliably be lost.
- code-review-04: 100,000 increments from 10 threads will often produce a final value less than 100,000.
- code-review-04: Every method of the class is unsafe to call concurrently with any other method, including itself.
- code-review-04: A single attribute read or write is atomic in CPython.
- code-review-04: Reading counter.value will not return garbage.
- code-review-04: itertools.count() is thread-safe in CPython.
- code-review-04: itertools.count() and multiprocessing.Value are lock-free alternatives worth considering for higher throughput under heavy contention.
- code-review-05: `cd` can fail due to a nonexistent directory, permissions, or a typo.
- code-review-05: `cd "$BACKUP_DIR" || exit 1` is the recommended form.
- code-review-05: The script performs no sanity check on the supplied path.
- code-review-05: A caller could pass `/` or `/home` and the script would `cd` there and delete `*.tmp` files.
- code-review-05: If no `.log` files exist, `ls *.log` prints a "No such file or directory" error to stderr.
- code-review-05: When `ls *.log` matches nothing, the loop harmlessly does not execute.
- code-review-05: Using a bare glob avoids the stderr error message.
- code-review-05: In plain `sh`/dash an unmatched glob does not match, so the literal-glob issue does not arise there.
- code-review-05: `gzip` can fail on a read-only file or an already-gzipped file.
- code-review-05: The `-f` flag in `rm -rf *.tmp` suppresses errors.
- code-review-05: Suppressing errors with `-f` is fine for the no-match case but also silently masks permission errors.
- code-review-06: The list-replacement behavior is inconsistent with the function's dict-merging behavior.
- code-review-06: The recursive branch checks that merged[key] is a dict but does not check that value is a dict.
- code-review-06: If merged[key] is a dict and override[key] is a string, the code calls merge_settings(some_dict, "a_string").
- code-review-06: Strings do not have an .items() method.
- code-review-06: Passing a string as the override argument raises AttributeError: 'str' object has no attribute 'items' inside the recursion.
- code-review-06: The resulting traceback appears far from the actual bad input, making it confusing.
- code-review-06: The code should check isinstance(value, dict) before recursing.
- code-review-06: The function can never produce a None settings value.
- code-review-06: The function has four distinct branch behaviors: adding new keys, deleting keys on None, recursively merging dict-vs-dict, and overwriting everything else.
- code-review-06: pop(key, None) does not crash when the key being deleted is absent from merged.
- code-review-06: The function has no naming or documentation distinguishing its four behaviors.
- code-review-06: The missing isinstance(value, dict) check is likely an oversight rather than intentional.
- code-review-06: The asymmetry between list and dict handling is more likely an incomplete implementation than a deliberate choice.
- code-review-06: There are currently no tests for the code.
- code-review-07: The zero-delay first backoff is not documented and is inconsistent with the rest of the backoff logic.
- code-review-07: On the final loop iteration, a 429 still triggers the setTimeout wait before the loop exits.
- code-review-07: The delay on the final attempt is wasted because there is no subsequent attempt.
- code-review-07: Unseen callers may already depend on the 'errors become null' behavior.
- code-review-07: Swallowing errors as null is the riskiest issue because it hides programming errors rather than only HTTP failures.
- code-review-07: There is no upper bound check on err.status >= 500.
- code-review-07: Any status of 500 or greater, including nonstandard or custom codes, is treated as retryable.
- code-review-07: There is no err.status < 600 guard, so the condition means '>= 500' rather than '5xx'.
- code-review-07: When attempts <= 0, the function returns undefined without ever calling fn.
- code-review-07: There is no validation or error raised for an attempts value of 0 or less.
- code-review-07: The function contains no logging anywhere.
- code-review-07: Retry-on-429, retry-on-5xx, and giving up on other errors form a recognizable rate-limit and transient-error retry pattern.
- code-review-07: Swallowing all non-status errors as null without logging or rethrow is ambiguous in intent but risky regardless.
- code-review-08: Calling `os.path.getmtime` on a broken symlink raises `FileNotFoundError`.
- code-review-08: `os.listdir()` returns entries in filesystem order, not sorted by mtime.
- code-review-08: The script does not select files oldest-first for the 500 cap.
- code-review-08: Immediate deletion of tmp-/.part files could be deliberate if writer processes rename atomically on completion.
- code-review-08: The script does not own the system that produces the tmp-/.part files.
- code-review-08: No one owns the script's schedule.
- debugging-01: The fix is to define get_url(cfg) to return the f-string "http://{cfg['host']}:{cfg['port']}/api".
- debugging-02: A regular function's `this` is determined by how the function is called, not by where it is defined.
- debugging-02: `setInterval` invokes its callback as a plain function call.
- debugging-02: The global object is referred to as `window` or `globalThis`.
- debugging-02: Accessing `this.seconds` throws if `this` is `undefined` in strict mode.
- debugging-02: The `NaN` value is logged and reassigned on each tick of the interval.
- debugging-02: `.bind(this)` on a regular function callback is an alternative fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-02: The `Timer` constructor initializes `this.seconds` to 0.
- debugging-03: The fixed `moving_sum` function appends `sum(values[i : i + window])` to a list for each index `i` and returns that list.
- debugging-03: For values of length 4 and window 2, the fixed code yields sums `[1+2, 2+3, 3+4]`.
- debugging-03: `[1+2, 2+3, 3+4]` equals `[3, 5, 7]`.
- debugging-03: `[3, 5, 7]` is the expected result.
- debugging-04: UTF-8 is the safe default encoding to use.
- debugging-04: chardet and charset-normalizer are libraries for detecting encoding.
- debugging-04: A file can be opened in binary mode with the "rb" mode string.
- debugging-04: Counting occurrences of b"\n" in binary mode yields a line count.
- debugging-04: Opening the file in binary mode avoids decoding entirely.
- debugging-05: The fixed code is `def make_post(title, tags=None)` with `if tags is None: tags = list(DEFAULT_TAGS)`, then `tags.append("post")`, then `return {"title": title, "tags": tags}`.
- debugging-06: The working directory is empty.
- debugging-06: There is no code to inspect, so the task is pure log analysis.
- debugging-06: Dashboard refreshes and scheduled analytics queries are examples of unpredictable analytics traffic spikes.
- debugging-06: A slow analytics query can be caused by a missing index or a table scan.
- debugging-06: Slow analytics queries starving a co-tenant is the classic 'noisy neighbor' pattern for shared databases.
- debugging-06: The failures occur on a weekly frequency.
- debugging-06: Weekly failure frequency could line up with a periodic batch job, a deploy, or a data-volume spike.
- debugging-06: One check is whether analytics query volume, replica count, or a specific slow query spikes around 02:14 UTC on failure nights.
- debugging-06: The failures occur around 02:14 UTC.
- debugging-06: Some database drivers or ORMs expose pool metrics such as checked-out connections and wait queue length.
- debugging-06: Retention for metrics is often longer than log retention and cheaper to keep.
- debugging-06: Checking database-side logs can reveal what was holding connections at 02:14:07-02:14:41.
- debugging-06: The failure window on the observed night spanned 02:14:07 to 02:14:41.
- debugging-06: Comparing pool configuration against total client count is a way to narrow down the cause.
- debugging-06: The comparison involves the sum of max pool size across all export workers and analytics service instances versus the database's max_connections.
- debugging-06: If total configured pool size is close to the database's max_connections, a small ephemeral spike such as a deploy restart or an extra worker is enough to exhaust it.
- debugging-06: Correlating with analytics logs and checking database-side logs are the fastest steps to confirm or rule out the shared-database theory.
- debugging-07: There is memory that may be relevant to the task.
- debugging-08: The session ID is 4988878c-7c4a-4c17-92eb-92beb2d5be32.
- explanation-01: A hash map's underlying array has only one slot per index.
- explanation-01: Chaining is also known as separate chaining.
- explanation-01: The collection in a chaining slot is usually a linked list, and sometimes a tree or array.
- explanation-01: Quadratic probing jumps by increasing squares.
- explanation-01: Deletion in open addressing is trickier and must use tombstones or rehashing.
- explanation-01: Open addressing implementations often resize at around a 70% load factor.
- explanation-01: Python's dict uses open addressing internally.
- explanation-01: Go's map uses a bucket-based chaining variant.
- explanation-02: An optimistic locking example uses a `products` table with a `version` integer column.
- explanation-02: An optimistic stock update can be written as `UPDATE products SET stock = stock - 1, version = version + 1 WHERE id = 42 AND version = 7;`.
- explanation-02: If the row's version is no longer 7 because someone else updated it first, the UPDATE affects 0 rows.
- explanation-02: Optimistic locking fits when transactions are short and fast.
- explanation-02: A pessimistic transfer example uses BEGIN, two `SELECT balance FROM accounts WHERE id = ... FOR UPDATE` statements, balance updates, and COMMIT.
- explanation-03: A network path may consist of a single fast link or may cross several routers of varying speed and load.
- explanation-03: If a sender transmitted at whatever rate the receiver's window allowed, it could send more data than routers along the path can forward.
- explanation-03: In congestive collapse, throughput drops sharply even though all senders are trying to send at full speed.
- explanation-03: The sender maintains a congestion window (cwnd) in addition to the receiver's advertised window.
- explanation-03: The amount of data in flight is limited by the smaller of the congestion window and the receiver's advertised window.
- explanation-03: Slow start continues until a packet loss or ECN mark is detected, or until cwnd reaches the ssthresh threshold.
- explanation-03: A detected packet loss or ECN mark is interpreted as a signal that the network is congested.
- explanation-03: In congestion avoidance, cwnd growth is linear, roughly +1 segment per RTT.
- explanation-04: Each thread has its own stack and register state.
- explanation-04: Creating and switching processes is more expensive than creating and switching threads.
- explanation-04: The higher cost of processes comes from separate memory spaces and OS bookkeeping.
- explanation-04: Processes bypass the GIL because each process has its own interpreter.
- explanation-04: Multiple processes each get their own interpreter and GIL and can run on separate cores.
- explanation-04: Python's multiprocessing module exists specifically to enable real parallelism for CPU-bound work.
- explanation-04: A process-based architecture with workers communicating via queues or sockets generalizes naturally to multiple machines.
- explanation-04: Thread-based designs assume a single shared address space and do not extend across machines.
- explanation-04: Threads are preferable for I/O-bound concurrency where many threads wait on network or disk.
- explanation-04: Threads have low memory overhead and allow fast, frequent communication between concurrent units.
- explanation-04: Spinning up a full process per connection would be wasteful.
- explanation-05: A collection can be kept reachable by being held by a long-lived singleton.
- explanation-05: A listener's closure often captures its whole surrounding scope, including large objects and DOM nodes.
- explanation-05: A captured closure scope keeps all of the captured objects alive indefinitely.
- explanation-05: Static or global variables accumulating data is another frequent cause of memory leaks.
- explanation-05: Mutual references between long-lived and short-lived objects are another frequent cause of memory leaks.
- explanation-05: Mutual references can keep a short-lived object artificially alive.
- explanation-06: A cache only helps if the slowness is caused by repeated reads of the same data hitting the database.
- explanation-06: Caching provides little benefit for a read-heavy workload in which every read is for different data, because the cache hit rate is low.
- explanation-06: The complexity added by a cache includes cache invalidation, staleness, and another system to operate.
- explanation-06: If reads are mostly unique lookups, caching will not improve performance much.
- explanation-06: Database reads on a small set of hot data, such as the same user profile or config fetched thousands of times, is the textbook case where a cache pays off.
- explanation-06: Profiling is cheap.
- explanation-06: Timing middleware and slow query logs are examples of basic profiling.
- explanation-07: Reaching 2-5TB within a year would justify planning for sharding ahead of time.
- explanation-07: Sharding addresses write and connection bottlenecks more than it addresses raw disk size.
- explanation-07: Sharding makes migrations, backups, monitoring, and debugging harder for every feature.
- explanation-07: Vertical scaling has a ceiling set by the largest available instance size and IOPS limits.
- explanation-07: Exceeding vertical scaling limits before sharding infrastructure exists results in downtime or degraded performance.
- explanation-07: Partitions map naturally to shards, so partitioning provides leverage if sharding becomes necessary.
- explanation-08: If JSON parsing is 2% of request time, a binary format that parses 3x faster saves about 1.3% end-to-end.
- explanation-08: Huge payloads or a hot loop are cases where serialization can account for 40% of request time.
- explanation-08: The second key number is how binary formats compare for the user's actual payload shape.
- explanation-08: Gains from Protobuf, msgpack, and FlatBuffers vary a lot depending on the payload shape.
- explanation-08: Payload characteristics that affect binary format gains include deep nesting, string-heaviness, numeric-heaviness, and repetitiveness.
- explanation-08: A generic claim that binary is faster can be off by an order of magnitude in either direction for a specific schema.
- explanation-08: Benchmarking one or two candidate formats against real sample payloads is a recommended step.
- explanation-08: The profiling and benchmarking work would take a few hours.
- summarization-01: Cold start time has been reduced by roughly 40%.
- summarization-02: Staging's connection pool size is intentionally small at 5.
- summarization-02: Detection lag was approximately 7 minutes.
- summarization-02: Total impact was approximately 34 minutes.
- summarization-02: Error onset occurred at 09:14.
- summarization-02: Rollback occurred at 09:48.
- summarization-03: Under the proposal, uploads will return a placeholder URL.
- summarization-04: PDF export on the Reports page fails silently.
- summarization-04: Clicking the PDF export option initially produces no visible response.
- summarization-04: The 'export failed' error banners contain no additional error details.
- summarization-05: Chen is assigned to continue search indexing work.
- summarization-08: The small sample size cannot confirm the mechanism behind the progress bar abandonment.

Added facts (styled only):

- code-review-01: The default `db=None` is not itself a bug.
- code-review-01: A bad `db` object only fails at call time.
- code-review-01: The fixed version uses `roles = roles + ["member"]`, which creates a new list instead of mutating the caller's list.
- code-review-02: An `async` function is meant to resolve to a value.
- code-review-05: If no .tmp files exist, most shells leave the literal string `*.tmp`, causing `rm` to error.
- code-review-05: That `rm` error on an unmatched glob is harmless in this script but fragile.
- code-review-05: If no .log files match, the literal string `*.log` is passed to gzip, causing a "no such file" error.
- code-review-05: `echo Cleaned $BACKUP_DIR` is unquoted, which is a cosmetic issue for paths containing spaces.
- code-review-05: The suggested fix uses `set -eu`, validates the argument, quotes variables, uses `cd -- "$BACKUP_DIR"`, and iterates globs directly with `[ -e "$f" ]` existence guards.
- code-review-06: The reviewer has no prior context on the code being reviewed.
- code-review-06: If `merged[key]` is a dict and `value` is not a dict, the entire subtree is replaced by the scalar.
- code-review-06: The subtree replacement on type mismatch produces no error and no warning.
- code-review-06: Override-wins-on-type-conflict could be intentional 'last write wins' semantics.
- code-review-06: Assigning a dict `value` directly is inconsistent with the stated 'merge dicts recursively' intent.
- code-review-06: Assigning a dict `value` directly is arguably correct because there is nothing to merge into.
- code-review-06: The function has no cycle detection or recursion-depth protection.
- code-review-06: Deeply nested or self-referential structures will overflow the stack.
- code-review-06: Cycles are unlikely in real config data.
- code-review-06: The function performs no type checking on `base` or `override`.
- code-review-06: Passing a non-dict such as `None` as `base` causes `dict(base)` or `.items()` to raise an unhandled `TypeError`.
- code-review-06: The delete sentinel is the behavior most likely to break callers if it were 'corrected'.
- code-review-07: Delay growth is unbounded and has no cap.
- code-review-07: Unbounded delay growth is not a problem at attempts = 3.
- code-review-07: attempts = 3 means 3 total tries, consisting of 1 initial attempt plus 2 retries.
- code-review-07: attempts = 3 does not mean 3 retries.
- code-review-07: The semantics of attempts are easy for a caller to misread.
- code-review-07: The inconsistency between the 5xx path and the 429 path suggests oversight rather than deliberate design.
- code-review-07: The off-by-one delay, the undefined/null mismatch, and the swallowing of non-HTTP errors read as bugs rather than intent.
- code-review-08: `os.path.getmtime` and `os.remove` will raise if permissions are wrong.
- code-review-08: The `removed < 500` check does not achieve any real cap.
- debugging-05: In the fixed version, `tags` becomes `list(tags)` when the caller passes a non-None value, and `["draft"]` otherwise.
- debugging-05: The fix also stops `make_post` from mutating a caller-supplied list.
- debugging-06: The failures are not caused by a data bug or a code bug.
- debugging-06: A fixed 30-second wait matches a connection pool checkout timeout.
- debugging-06: A fixed 30-second wait does not match a query timeout.
- debugging-06: A connection leak slowly starves the pool until the service recovers or restarts.
- debugging-06: The export job's writes and analytics reads/writes can lock the same rows or tables.
- debugging-06: Under lock contention, connections sit idle waiting on locks rather than doing work.
- debugging-06: Logging pool state at the time of error often distinguishes a leak from an undersized pool from contention.
- debugging-06: Increasing the pool size or timeout can be used as a diagnostic rather than a fix.
- debugging-06: If failures stop or move later in the run after increasing pool size or timeout, that confirms undersizing rather than a leak.
- debugging-06: Instrumenting pool state at timeout time is the recommended first step.
- debugging-06: Instrumenting pool state at timeout will likely identify which of the five listed causes is responsible.
- debugging-07: The failing test seeds three events and then reads a digest endpoint.
- debugging-07: The test fails roughly 1 in 10 times in CI.
- debugging-07: The test passes reliably when run serially.
- debugging-07: The test does not reproduce on developer machines.
- debugging-07: The CI runs the test suite with 4-way parallelism.
- debugging-07: The CI shared runner retains no artifacts.
- debugging-07: On failure, only the event count is currently visible, not which event is missing.
- debugging-07: The test is test_digest_contains_all_events in tests/test_notifications.py.
- debugging-07: A missing await, an async write queue, an eventually-consistent index, or a delayed background job could cause the digest to be read before all three writes commit.
- debugging-07: Four workers running against a single shared DB or queue can cause events to leak across tests.
- debugging-07: A digest endpoint that isn't scoped to the test's user or session can be affected by a concurrent test's cleanup.
- debugging-07: A shared fixture such as an in-memory queue, cache, or singleton that isn't worker-isolated can cause one worker's setup to collide with another's.
- debugging-07: If digest logic dedupes by timestamp, two events landing in the same millisecond can cause one to be dropped.
- debugging-07: If digest logic filters by a time window, events straddling a boundary can be dropped.
- debugging-07: CI's added latency and jitter under parallel load make timing-related failures more likely there than on a quiet dev machine.
- debugging-07: A fixture that resets state per-test but not per-worker can see stale state depending on interleaving.
- debugging-07: Race conditions and cross-worker state bleed are the two most likely causes of this failure.
- debugging-07: Race conditions and cross-worker state bleed both explain flakiness under 4-way parallelism with serial success and no dev-machine repro.
- debugging-07: pytest-xdist gives each worker its own process.
- debugging-07: pytest-xdist does not automatically give each worker its own database or queue.
- debugging-07: Running pytest -n 4 locally in a loop can confirm whether parallelism is the trigger.
- debugging-07: Adding an explicit wait or poll for three committed events before calling the digest endpoint would isolate timing as the cause.
- debugging-07: The pytest options --reruns 1 and -v can be used to capture more failure detail.
- debugging-07: If the failure rate scales with worker count, cross-test or cross-worker contention is implicated over network jitter.
- debugging-07: Reproducing the failure locally under -n4 turns a CI-only bug into one that can be iterated on directly.
- debugging-08: The evidence points to a real object leak tied to request handling rather than only cache warm-up.
- debugging-08: The most likely cause is per-request objects that are never released.
- debugging-08: Event listeners, timers, or promise/callback chains can be registered per webhook and never cleared.
- debugging-08: Per-request object leaks fit every clue in the evidence.
- debugging-08: Memory growth scales with traffic from marketing campaigns.
- debugging-08: The memory growth does not plateau.
- debugging-08: Growth does not plateau because each request adds more objects and nothing evicts them.
- debugging-08: The bug does not require webhooks specifically.
- debugging-08: Any request path with the same bug would explain the canary's slower growth.
- debugging-08: The canary instance shows slower memory growth.
- debugging-08: Webhook and canary code paths can be grepped for '.on(', 'addEventListener', 'setInterval', and 'setTimeout' calls lacking matching 'removeListener', 'clearInterval', or 'clearTimeout'.
- debugging-08: Two heap snapshots taken hours apart on one instance can be diffed by retained object counts by type.
- debugging-08: A per-request object leak shows up as a steadily growing count of listener or timer objects rather than strings or buffers.
- debugging-08: The second most plausible cause is a connection or socket leak from webhook processing.
- debugging-08: Outbound calls to downstream services or databases can open connections without closing them.
- debugging-08: A connection pool can grow unbounded under load.
- debugging-08: 'lsof -p <pid>' or 'netstat' can be used over time to compare the busy instance against the canary.
- debugging-08: Open file descriptors or sockets climbing in step with memory indicates a connection or socket leak.
- debugging-08: The third possibility is an unbounded structure sitting next to the bounded cache.
- debugging-08: The cache itself may be bounded.
- debugging-08: Structures adjacent to a bounded cache are often unbounded.
- debugging-08: Examples of unbounded adjacent structures include in-flight request de-duplication maps, negative or miss caches, and per-key metadata such as timestamps and access counts.
- debugging-08: Per-key metadata may not be cleared on eviction.
- debugging-08: The cache's actual entry count and byte size can be logged over a day.
- debugging-08: If entry count stays flat at the bound while memory keeps climbing, the leak is in metadata or in entries growing larger over time rather than in the cache's core bound.
- debugging-08: Product payloads getting bigger is an example of entries growing larger over time.
- debugging-08: The fourth possibility is allocator fragmentation, which is secondary and not a leak per se.
- debugging-08: Allocator fragmentation explains memory never returning to baseline even when the live heap is fine.
- debugging-08: Some allocators do not return freed memory to the operating system.
- debugging-08: Allocators are especially prone to not returning freed memory under bursty allocation patterns such as those from campaign traffic.
- debugging-08: RSS can be compared to the runtime's own live-heap metric, such as GC stats.
- debugging-08: If live heap is flat while RSS climbs, the cause is fragmentation rather than a leak.
- debugging-08: Fragmentation requires a different fix, such as tuning the allocator or triggering periodic compaction or restart.
- debugging-08: The most useful single next step is capturing a heap snapshot at the start of day and another after several hours of growth, then diffing by retained type and count.
- debugging-08: The heap snapshot diff will reveal in one step whether the cause is listeners, connections, cache metadata, or fragmentation.
- debugging-08: Diffing heap snapshots is cheaper than checking all four hypotheses blind.
- explanation-01: Most general-purpose hash maps use chaining or a hybrid.
- explanation-01: Java's HashMap is a general-purpose hash map that uses chaining or a hybrid.
- explanation-01: Python's dict is a general-purpose hash map that uses chaining or a hybrid.
- explanation-01: Performance-critical hash maps favor open addressing for cache efficiency.
- explanation-01: Hash maps in Rust and Go are examples of performance-critical implementations that favor open addressing.
- explanation-02: In the e-commerce example, two admins edit the same product listing at the same time and each read fetches `version = 5`.
- explanation-02: In the e-commerce example, the first save succeeds and bumps the version to 6.
- explanation-02: In the e-commerce example, the second save's `WHERE version = 5` matches zero rows, and the app tells that admin to reload and retry.
- explanation-02: Web apps and APIs favor optimistic locking because it avoids holding a lock across a network round trip or user think-time.
- explanation-02: Pessimistic locking guarantees no conflicts.
- explanation-03: The name 'slow start' is somewhat misleading because growth starts slow but accelerates quickly.
- explanation-04: nginx and Postgres use worker processes.
- explanation-04: A game engine's render and physics threads share a scene graph.
- explanation-05: A subscriber added to an event emitter or observable holds a reference back to the object that registered it.
- explanation-06: Without profiling, "slow" could mean a slow downstream service.
- explanation-06: If reads dominate and the database is the hot spot, a cache will pay off.
- explanation-07: If writes dominate on a single table, partitioning rather than full sharding may suffice.
- explanation-07: Sharding without the supporting infrastructure creates outages rather than scale.
- explanation-07: Migrating a live database to a sharded architecture is harder than starting out sharded.
- explanation-07: A shard key should be picked in advance so it is ready if sharding becomes necessary.
- explanation-07: Sharding should be revisited only upon hitting a concrete wall.
- explanation-07: The size limit for vertical scaling and partitioning is typically tens of terabytes.
- explanation-08: Binary formats such as protobuf and msgpack usually beat JSON on encode/decode speed.
- explanation-08: Binary formats are often 2-10x faster than JSON at encoding and decoding.
- explanation-08: Binary formats usually beat JSON on payload size.
- explanation-08: Binary formats often produce payloads 20-50% smaller than JSON.
- explanation-08: It is common for JSON parsing to be a small share of request time because network, database, or business logic dominate.
- explanation-08: Payload sizes for representative requests should be measured before committing to the rewrite.
- explanation-08: A profiler or a simple timing wrapper is sufficient to measure serialization time.
- explanation-08: Profiling reveals whether the change is worth the migration cost.
- explanation-08: Migration costs include new schemas, client changes, and debugging harder-to-inspect payloads.
- summarization-01: A build tooling bump was omitted from the release notes.
- summarization-01: A session module refactor was omitted from the release notes.
- summarization-01: A telemetry interval change was omitted from the release notes.
- summarization-01: The build tooling bump, session module refactor, and telemetry interval change are internal and not user-facing.
- summarization-02: The copy occurred via a shared template used by both environments.
- summarization-02: Mix-ups between the templates are likely to recur.
- summarization-07: Memory was checked for relevant context before answering.
- summarization-07: No relevant context was found in memory.
- summarization-07: All findings other than the median latency result are guesses.

### developer-docs

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 27 | 23 | 0.852 | 26 | 4 |
| code-review-02 | 17 | 14 | 0.824 | 22 | 5 |
| code-review-03 | 27 | 15 | 0.556 | 20 | 4 |
| code-review-04 | 26 | 16 | 0.615 | 20 | 1 |
| code-review-05 | 33 | 24 | 0.727 | 34 | 7 |
| code-review-06 | 29 | 21 | 0.724 | 27 | 6 |
| code-review-07 | 40 | 32 | 0.8 | 34 | 6 |
| code-review-08 | 29 | 23 | 0.793 | 28 | 2 |
| debugging-01 | 7 | 7 | 1.0 | 8 | 0 |
| debugging-02 | 18 | 15 | 0.833 | 12 | 1 |
| debugging-03 | 13 | 13 | 1.0 | 11 | 0 |
| debugging-04 | 15 | 10 | 0.667 | 8 | 0 |
| debugging-05 | 19 | 13 | 0.684 | 12 | 0 |
| debugging-06 | 35 | 19 | 0.543 | 32 | 9 |
| debugging-07 | 2 | 1 | 0.5 | 26 | 26 |
| debugging-08 | 1 | 0 | 0.0 | 40 | 40 |
| explanation-01 | 37 | 28 | 0.757 | 27 | 1 |
| explanation-02 | 32 | 26 | 0.812 | 27 | 3 |
| explanation-03 | 28 | 15 | 0.536 | 22 | 2 |
| explanation-04 | 35 | 26 | 0.743 | 40 | 3 |
| explanation-05 | 16 | 11 | 0.688 | 9 | 0 |
| explanation-06 | 16 | 14 | 0.875 | 22 | 4 |
| explanation-07 | 21 | 15 | 0.714 | 22 | 5 |
| explanation-08 | 15 | 9 | 0.6 | 21 | 14 |
| summarization-01 | 6 | 5 | 0.833 | 8 | 4 |
| summarization-02 | 11 | 7 | 0.636 | 15 | 2 |
| summarization-03 | 15 | 15 | 1.0 | 12 | 0 |
| summarization-04 | 14 | 11 | 0.786 | 10 | 0 |
| summarization-05 | 9 | 8 | 0.889 | 10 | 0 |
| summarization-06 | 15 | 15 | 1.0 | 12 | 0 |
| summarization-07 | 14 | 14 | 1.0 | 18 | 0 |
| summarization-08 | 21 | 19 | 0.905 | 23 | 2 |

Median fraction: 0.772 over 32 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: The function performs no validation that `roles` is actually a list.
- code-review-01: A `True`/`False` return value tells the caller nothing about why the call failed or what was inserted, such as a created user ID.
- code-review-01: The suggested fix lets real exceptions propagate instead of hiding them.
- code-review-01: Specific exceptions can be caught at the call site if needed.
- code-review-02: Declaring a function `async` without using `await` is a strong signal the promise chain was meant to be awaited but isn't.
- code-review-02: `fetch` only rejects on network failure.
- code-review-02: The fixed version awaits `res.json()` and returns `data.name.toUpperCase()`.
- code-review-03: Stacked queries can enable worse attacks, depending on the database driver.
- code-review-03: SQL injection is the single biggest issue in the code.
- code-review-03: If `customer_name` or `status` is not a string (e.g. `None`), the `+` concatenation raises a `TypeError`.
- code-review-03: A `TypeError` from concatenation is raised instead of a meaningful error.
- code-review-03: The code does not handle `fetchall()` on large result sets.
- code-review-03: If a customer has many orders, `fetchall()` loads everything into memory at once.
- code-review-03: Pagination or `fetchmany()` is worth considering for large datasets.
- code-review-03: The query does exact string matching on the `customer` and `status` columns.
- code-review-03: Exact string matching makes the query case-sensitive.
- code-review-03: Case-insensitive matching or normalization such as trimming whitespace may be wanted, depending on requirements.
- code-review-03: The SQL injection must be fixed before the code goes to production.
- code-review-03: The issues other than SQL injection are secondary robustness and design concerns.
- code-review-04: This read-modify-write pattern is a TOCTOU (time-of-check-to-time-of-use) bug.
- code-review-04: CPython has a GIL (Global Interpreter Lock).
- code-review-04: The GIL only guarantees that individual bytecode operations are atomic.
- code-review-04: The GIL can switch threads between the read and the write of a read-modify-write sequence.
- code-review-04: With enough concurrent increments, updates will reliably be lost.
- code-review-04: 100,000 increments from 10 threads will often produce a final value less than 100,000.
- code-review-04: Every method of the class is unsafe to call concurrently with any other method, including itself.
- code-review-04: A single attribute read or write is atomic in CPython.
- code-review-04: Reading counter.value will not return garbage.
- code-review-04: itertools.count() and multiprocessing.Value are lock-free alternatives worth considering for higher throughput under heavy contention.
- code-review-05: `cd` can fail due to a nonexistent directory, permissions, or a typo.
- code-review-05: `cd "$BACKUP_DIR" || exit 1` is the recommended form.
- code-review-05: If no `.log` files exist, `ls *.log` prints a "No such file or directory" error to stderr.
- code-review-05: When `ls *.log` matches nothing, the loop harmlessly does not execute.
- code-review-05: Using a bare glob avoids the stderr error message.
- code-review-05: In plain `sh`/dash an unmatched glob does not match, so the literal-glob issue does not arise there.
- code-review-05: `gzip` can fail on a read-only file or an already-gzipped file.
- code-review-05: The `-f` flag in `rm -rf *.tmp` suppresses errors.
- code-review-05: Suppressing errors with `-f` is fine for the no-match case but also silently masks permission errors.
- code-review-06: The list-replacement behavior is inconsistent with the function's dict-merging behavior.
- code-review-06: The resulting traceback appears far from the actual bad input, making it confusing.
- code-review-06: The function can never produce a None settings value.
- code-review-06: The function has four distinct branch behaviors: adding new keys, deleting keys on None, recursively merging dict-vs-dict, and overwriting everything else.
- code-review-06: The function has no naming or documentation distinguishing its four behaviors.
- code-review-06: Recursive dict merging is a deliberate design choice and the main purpose of the function.
- code-review-06: The shallow copy of unmerged nested structures is very unlikely to be intentional.
- code-review-06: The asymmetry between list and dict handling is more likely an incomplete implementation than a deliberate choice.
- code-review-07: The zero-delay first backoff is not documented and is inconsistent with the rest of the backoff logic.
- code-review-07: On the final loop iteration, a 429 still triggers the setTimeout wait before the loop exits.
- code-review-07: The delay on the final attempt is wasted because there is no subsequent attempt.
- code-review-07: Swallowing errors as null is the riskiest issue because it hides programming errors rather than only HTTP failures.
- code-review-07: There is no upper bound check on err.status >= 500.
- code-review-07: Any status of 500 or greater, including nonstandard or custom codes, is treated as retryable.
- code-review-07: There is no err.status < 600 guard, so the condition means '>= 500' rather than '5xx'.
- code-review-07: Swallowing all non-status errors as null without logging or rethrow is ambiguous in intent but risky regardless.
- code-review-08: Calling `os.path.getmtime` on a broken symlink raises `FileNotFoundError`.
- code-review-08: The script has no logging, dry-run mode, or audit trail.
- code-review-08: In the snippet, the returned count is not printed or logged anywhere.
- code-review-08: Immediate deletion of tmp-/.part files could be deliberate if writer processes rename atomically on completion.
- code-review-08: The script does not own the system that produces the tmp-/.part files.
- code-review-08: No one owns the script's schedule.
- debugging-02: The global object is referred to as `window` or `globalThis`.
- debugging-02: Accessing `this.seconds` throws if `this` is `undefined` in strict mode.
- debugging-02: The `NaN` value is logged and reassigned on each tick of the interval.
- debugging-04: UTF-8 is the safe default encoding to use.
- debugging-04: chardet and charset-normalizer are libraries for detecting encoding.
- debugging-04: A file can be opened in binary mode with the "rb" mode string.
- debugging-04: Counting occurrences of b"\n" in binary mode yields a line count.
- debugging-04: Opening the file in binary mode avoids decoding entirely.
- debugging-05: `DEFAULT_TAGS = ["draft"]` is created once at function definition time.
- debugging-05: When the test runs in isolation, `DEFAULT_TAGS` starts as `["draft"]`.
- debugging-05: When the test runs in isolation, `"post"` is appended, producing `["draft", "post"]`, and the test passes.
- debugging-05: By the time the test runs, `DEFAULT_TAGS` may already be `["draft", "post"]` or `["draft", "post", "post"]`.
- debugging-05: The assertion `== ["draft", "post"]` fails because extra `"post"` entries accumulate.
- debugging-05: `tags = list(DEFAULT_TAGS)` can be replaced with `["draft"]`.
- debugging-06: The working directory is empty.
- debugging-06: There is no code to inspect, so the task is pure log analysis.
- debugging-06: Dashboard refreshes and scheduled analytics queries are examples of unpredictable analytics traffic spikes.
- debugging-06: A slow analytics query can be caused by a missing index or a table scan.
- debugging-06: Slow analytics queries starving a co-tenant is the classic 'noisy neighbor' pattern for shared databases.
- debugging-06: Weekly failure frequency could line up with a periodic batch job, a deploy, or a data-volume spike.
- debugging-06: A mismatch between pool size and instance/replica count is a plausible cause.
- debugging-06: If a service scaled up its workers or replicas without raising the database max-connections or pool size, exhaustion becomes a matter of timing rather than a deterministic bug.
- debugging-06: One check is whether analytics query volume, replica count, or a specific slow query spikes around 02:14 UTC on failure nights.
- debugging-06: Some database drivers or ORMs expose pool metrics such as checked-out connections and wait queue length.
- debugging-06: Retention for metrics is often longer than log retention and cheaper to keep.
- debugging-06: The failure window on the observed night spanned 02:14:07 to 02:14:41.
- debugging-06: Comparing pool configuration against total client count is a way to narrow down the cause.
- debugging-06: The comparison involves the sum of max pool size across all export workers and analytics service instances versus the database's max_connections.
- debugging-06: If total configured pool size is close to the database's max_connections, a small ephemeral spike such as a deploy restart or an extra worker is enough to exhaust it.
- debugging-06: Correlating with analytics logs and checking database-side logs are the fastest steps to confirm or rule out the shared-database theory.
- debugging-07: There is memory that may be relevant to the task.
- debugging-08: The session ID is 4988878c-7c4a-4c17-92eb-92beb2d5be32.
- explanation-01: A hash map's underlying array has only one slot per index.
- explanation-01: Chaining is also known as separate chaining.
- explanation-01: The collection in a chaining slot is usually a linked list, and sometimes a tree or array.
- explanation-01: Quadratic probing jumps by increasing squares.
- explanation-01: Open addressing can degrade sharply as the array fills up, due to clustering and more probes.
- explanation-01: Open addressing implementations often resize at around a 70% load factor.
- explanation-01: Java's HashMap is a general-purpose language implementation that picks a collision strategy based on these trade-offs.
- explanation-01: Python's dict uses open addressing internally.
- explanation-01: Go's map uses a bucket-based chaining variant.
- explanation-02: An optimistic stock update can be written as `UPDATE products SET stock = stock - 1, version = version + 1 WHERE id = 42 AND version = 7;`.
- explanation-02: Examples of good fits for optimistic locking include a web app editing user profiles, e-commerce catalog updates, and most CRUD APIs.
- explanation-02: A pessimistic transfer example uses BEGIN, two `SELECT balance FROM accounts WHERE id = ... FOR UPDATE` statements, balance updates, and COMMIT.
- explanation-02: In some databases, `FOR UPDATE` prevents other transactions from even reading the locked rows.
- explanation-02: Financial transfers, inventory reservation for a flash sale, and seat booking systems are examples where pessimistic locking fits.
- explanation-02: Pessimistic locking risks contention and deadlocks.
- explanation-03: A network path may consist of a single fast link or may cross several routers of varying speed and load.
- explanation-03: Routers buffer excess packets.
- explanation-03: Router buffers are finite.
- explanation-03: When router buffers fill up, packets are dropped.
- explanation-03: Persistent overloading of the network causes congestive collapse.
- explanation-03: In congestive collapse, throughput drops sharply even though all senders are trying to send at full speed.
- explanation-03: Slow start is TCP's mechanism for finding a safe sending rate on an unknown path without causing congestive collapse.
- explanation-03: The sender maintains a congestion window (cwnd) in addition to the receiver's advertised window.
- explanation-03: The amount of data in flight is limited by the smaller of the congestion window and the receiver's advertised window.
- explanation-03: RFC 6928 specifies the initial window of around 10 segments.
- explanation-03: Slow start continues until a packet loss or ECN mark is detected, or until cwnd reaches the ssthresh threshold.
- explanation-03: A detected packet loss or ECN mark is interpreted as a signal that the network is congested.
- explanation-03: In congestion avoidance, cwnd growth is linear, roughly +1 segment per RTT.
- explanation-04: Each thread has its own stack and register state.
- explanation-04: The higher cost of processes comes from separate memory spaces and OS bookkeeping.
- explanation-04: Python and older Ruby are languages with a GIL.
- explanation-04: Python's multiprocessing module exists specifically to enable real parallelism for CPU-bound work.
- explanation-04: A crashed worker process can be restarted without affecting other processes.
- explanation-04: A process-based architecture with workers communicating via queues or sockets generalizes naturally to multiple machines.
- explanation-04: Thread-based designs assume a single shared address space and do not extend across machines.
- explanation-04: Threads are preferable for I/O-bound concurrency where many threads wait on network or disk.
- explanation-04: Spinning up a full process per connection would be wasteful.
- explanation-05: A collection can be kept reachable by being held by a long-lived singleton.
- explanation-05: A listener's closure often captures its whole surrounding scope, including large objects and DOM nodes.
- explanation-05: Static or global variables accumulating data is another frequent cause of memory leaks.
- explanation-05: Mutual references between long-lived and short-lived objects are another frequent cause of memory leaks.
- explanation-05: Mutual references can keep a short-lived object artificially alive.
- explanation-06: The complexity added by a cache includes cache invalidation, staleness, and another system to operate.
- explanation-06: Profiling is cheap.
- explanation-07: Reaching 2-5TB within a year would justify planning for sharding ahead of time.
- explanation-07: Sharding addresses write and connection bottlenecks more than it addresses raw disk size.
- explanation-07: PostgreSQL has native table partitioning that can partition by tenant or date.
- explanation-07: Logical partitioning is far cheaper to implement than sharding.
- explanation-07: Partitions map naturally to shards, so partitioning provides leverage if sharding becomes necessary.
- explanation-07: Logical partitioning buys time to observe growth rate before committing to a shard key.
- explanation-08: If JSON parsing is 2% of request time, a binary format that parses 3x faster saves about 1.3% end-to-end.
- explanation-08: Huge payloads or a hot loop are cases where serialization can account for 40% of request time.
- explanation-08: Gains from Protobuf, msgpack, and FlatBuffers vary a lot depending on the payload shape.
- explanation-08: Payload characteristics that affect binary format gains include deep nesting, string-heaviness, numeric-heaviness, and repetitiveness.
- explanation-08: A generic claim that binary is faster can be off by an order of magnitude in either direction for a specific schema.
- explanation-08: The profiling and benchmarking work would take a few hours.
- summarization-01: Cold start time has been reduced by roughly 40%.
- summarization-02: Staging's connection pool size is intentionally small at 5.
- summarization-02: Detection lag was approximately 7 minutes.
- summarization-02: Total impact was approximately 34 minutes.
- summarization-02: Error onset occurred at 09:14.
- summarization-04: PDF export on the Reports page fails silently.
- summarization-04: Clicking the PDF export option initially produces no visible response.
- summarization-04: The issue was reproduced on the latest version of Firefox.
- summarization-05: Chen is assigned to continue search indexing work.
- summarization-08: The small sample size cannot confirm the mechanism behind the progress bar abandonment.
- summarization-08: The template gallery finding is tentative.

Added facts (styled only):

- code-review-01: Specific exceptions should be caught instead, for example `except (AttributeError, KeyError) as e`.
- code-review-01: The cleaner version raises `ValueError("name is required")` when `name` is falsy.
- code-review-01: The cleaner version raises `ValueError("db is required")` when `db` is `None`.
- code-review-01: The cleaner version catches `Exception as e`, logs the error with `logging.error`, and returns `False`.
- code-review-02: The `async` keyword only means the function returns a promise.
- code-review-02: The `async` keyword does not pause execution of the function.
- code-review-02: The function cannot return the full profile.
- code-review-02: The function cannot handle a missing `name` field.
- code-review-02: The corrected version throws an `Error` including the user ID and `res.status` when `res.ok` is false.
- code-review-03: The function has no docstring.
- code-review-03: The function has no type hints.
- code-review-03: The function's parameters and return type aren't documented.
- code-review-03: Callers must read the implementation to know what to pass to the function and what they get back.
- code-review-04: The author checked memory and found no prior context relevant to this review.
- code-review-05: The script uses an unquoted $1 assigned to BACKUP_DIR.
- code-review-05: The `rm -rf *.tmp` line is the most dangerous line in the script.
- code-review-05: `sh` does not support `nullglob`.
- code-review-05: When `*.log` expands literally, `gzip` fails on a nonexistent file named `*.log`.
- code-review-05: The unquoted `$BACKUP_DIR` in the final `echo` is a minor issue because it is only used for display.
- code-review-05: Every command's failure in the script is silently ignored.
- code-review-05: The suggested rewrite exits with status 1 and prints a usage message to stderr if BACKUP_DIR is empty or is not a directory.
- code-review-06: The function has one likely bug, two aliasing hazards, and several undocumented design choices.
- code-review-06: Assigning the override's dict directly stores the object rather than a copy.
- code-review-06: Later mutation of the override's nested dict leaks into the merged result.
- code-review-06: The function has no depth or cycle protection.
- code-review-06: A self-referential or extremely deep override recurses until Python's recursion limit is hit.
- code-review-06: Characterization tests prevent 'fixing' behavior that a caller already depends on.
- code-review-07: There is no cap on the backoff delay, so with a large `attempts` value the delay grows unbounded.
- code-review-07: The helper does not respect a `Retry-After` header on 429 responses.
- code-review-07: Many APIs send a `Retry-After` header with an exact wait time.
- code-review-07: The likely intent of returning `null` is to let callers check for a falsy result instead of wrapping calls in try/catch.
- code-review-07: The missing backoff on 5xx retries is probably a bug.
- code-review-07: Silently treating errors without `status` as terminal failures, rather than logging or rethrowing them, is probably a bug.
- code-review-08: The script surfaces no error to whatever schedules it.
- code-review-08: The cutoff is 45 days, expressed as `86400 * 45`.
- debugging-02: The `.bind(this)` and `const self = this` approaches are useful for environments that lack arrow functions.
- debugging-06: If both services write to the same tables, lock waits can make queries hold connections longer than usual.
- debugging-06: A retry storm amplifying the problem is a plausible cause.
- debugging-06: A retry occurred at 02:14:08.
- debugging-06: The retry adds a new pool request while the pool is already exhausted.
- debugging-06: Adding requests to an exhausted pool can make recovery harder.
- debugging-06: 5 seconds is a slow-query logging threshold below the 30-second pool timeout.
- debugging-06: Connections should be returned in a `finally` block or equivalent.
- debugging-06: Increasing the pool size or giving the export job a dedicated pool does not fix the root cause.
- debugging-06: Increasing the pool size or using a dedicated pool reduces contention.
- debugging-07: The most likely cause of the failure is a race condition in the seed-then-read path.
- debugging-07: The race condition only shows up under load.
- debugging-07: Something in the write path (event creation, an async worker, a queue, or a cache) has not finished by the time the digest read happens.
- debugging-07: The test suite runs with four parallel workers.
- debugging-07: The four parallel workers add CPU and DB contention on CI.
- debugging-07: That contention exposes a timing gap that a serial dev run never hits.
- debugging-07: Event creation can return before the event is fully persisted or indexed.
- debugging-07: Delayed persistence can be caused by a background job, message queue, search index, or cache invalidation.
- debugging-07: The digest can read too early and miss the last write.
- debugging-07: If the digest logic filters by a timestamp window, a delayed write under load can land just outside the window.
- debugging-07: Clock resolution may be too coarse to order concurrent writes correctly.
- debugging-07: The test makes three seed API calls.
- debugging-07: One of the seed API calls could fail silently due to a rate limit, connection pool exhaustion, or a transient 5xx.
- debugging-07: The test does not check the seed call responses.
- debugging-07: If a seed call fails silently, only two events would ever exist.
- debugging-07: If tests share a database, tenant, or user account instead of isolating per test, another worker's activity could interfere with the count or query scope.
- debugging-07: Under four workers, connection pool exhaustion or a stale read replica could return results from before the third write commits.
- debugging-07: Asserting on every seed call's response (status code, returned ID) before requesting the digest rules out the silent seed failure cause.
- debugging-07: Adding a poll that retries the digest fetch until the count reaches 3 or times out, and logging retry counts, would confirm a timing race if it fixes the failure.
- debugging-07: Running the suite with -n 1, -n 2, and -n 4 in a loop shows whether the failure rate scales with worker count.
- debugging-07: That worker-count experiment confirms whether parallelism is the actual trigger.
- debugging-07: CI keeps no artifacts.
- debugging-07: Adding temporary logging inside the test makes the pytest failure output carry seeded event IDs and the digest response body even without external artifacts.
- debugging-07: The observed failure symptom is an assertion of `2 == 3`, off by exactly one.
- debugging-07: The failure is triggered only when running in parallel.
- debugging-07: Time-window or async-processing logic in the digest implementation is the most likely root cause.
- debugging-08: Faster memory growth during campaigns indicates something that scales with request/webhook volume.
- debugging-08: Memory never returning to baseline overnight rules out short-lived garbage and cache churn that self-heals.
- debugging-08: Memory never returning to baseline overnight points to a genuine leak or unreclaimed native memory rather than normal GC behavior.
- debugging-08: A canary with no webhooks that still grows rules out a leak confined solely to the webhook code path.
- debugging-08: Continued growth on a webhook-free canary indicates a baseline leak plus an additional contribution from webhook traffic.
- debugging-08: A cache bound unchanged for a year eliminates an obviously misconfigured bound as the cause.
- debugging-08: A cache being 'bounded' does not mean its size in bytes is constant.
- debugging-08: A likely cause is that the cache is bounded by entry count rather than by bytes, with entries having grown larger over time.
- debugging-08: Product data schemas tend to grow over a year, gaining more fields, longer descriptions, more image URLs, and variant data.
- debugging-08: If a cache bound caps the number of entries, total memory use is not actually capped.
- debugging-08: Campaign traffic drives more distinct products through the cache.
- debugging-08: Baseline traffic on the canary keeps the cache active even without webhooks.
- debugging-08: Exposing a gauge for the estimated byte size of the cache, not just entry count, can test the entry-count-bound hypothesis.
- debugging-08: Entry count staying flat at the bound while byte size climbs would confirm the entry-count-bound hypothesis.
- debugging-08: A cache eviction bug can cause the true entry count to exceed the configured bound.
- debugging-08: Some cache libraries mishandle eviction under concurrent access or with certain expiry policies.
- debugging-08: A load test inserting well past the bound under concurrency, asserting entry count settles back down, can detect an eviction bug.
- debugging-08: A cache library's changelog and issue tracker can be checked for known eviction bugs matching the version in use.
- debugging-08: A leak in request/webhook handling can come from retained references, listeners, or callbacks that are never cleaned up.
- debugging-08: More webhook calls producing more leaked objects fits the campaign correlation.
- debugging-08: Leaked objects are not garbage, so GC cannot reclaim them, which explains why the leak survives quiet nights.
- debugging-08: Taking two heap dumps hours apart and diffing object counts can reveal classes tied to the webhook handler growing without bound.
- debugging-08: Queues, listener lists, and futures/promises are object types to look for in a heap dump diff of the webhook path.
- debugging-08: If heap dumps are not feasible, gauges can be added for the size of internal queues, listener registries, and maps in the webhook path.
- debugging-08: A baseline leak unrelated to webhooks could come from background jobs, scheduled tasks, or connection pools.
- debugging-08: The canary proves something leaks even with zero webhook traffic.
- debugging-08: A periodic job, health check handler, or connection/session state accumulating regardless of external calls is a likely baseline leak source.
- debugging-08: Running a second canary with all traffic removed, including health checks, can confirm whether growth still occurs.
- debugging-08: Background jobs can be audited and instrumented for internal state that grows, such as retry queues, metrics buffers, and schedulers holding references to completed tasks.
- debugging-08: The growth could be off-heap or native memory rather than a managed-heap leak.
- debugging-08: Thread leaks, direct buffers, and native library allocations do not show up in a heap profile.
- debugging-08: Off-heap growth matches the absence of a heap profile signal and the failure of quiet periods to reclaim memory.
- debugging-08: Graphing process RSS against the runtime's reported heap/managed memory size over the same period tests for native memory growth.
- debugging-08: If RSS outpaces heap, thread count should be tracked over time.
- debugging-08: A thread-per-webhook pattern that does not clean up threads would explain both the campaign correlation and the canary's slower baseline growth from periodic tasks.
- debugging-08: JVM Native Memory Tracking, Go's pprof allocs, and valgrind --tool=massif are native memory tooling options.
- debugging-08: Cache entry count, estimated cache byte size, thread count, and RSS versus managed heap size are cheap gauges to add first.
- debugging-08: These gauges test the entry-count-bound, eviction-bug, and native-memory causes without any profiling infrastructure.
- debugging-08: Running a canary with zero traffic at all isolates background-job leaks from traffic-triggered ones.
- debugging-08: If gauges do not explain the growth, heap dumps should be captured at intervals and diffed to find growing object types in the webhook path.
- explanation-01: In chaining insertion, the map checks the list at that index for a matching key.
- explanation-02: Under pessimistic locking, conflicts never happen, so there is no conflict cost.
- explanation-02: The example optimistic update is `UPDATE products SET price = 19.99, version = version + 1 WHERE id = 42 AND version = 3;`.
- explanation-02: The pessimistic locking example uses `BEGIN; SELECT * FROM accounts WHERE id = 42 FOR UPDATE; UPDATE accounts SET balance = balance - 100 WHERE id = 42; COMMIT;`.
- explanation-03: ssthresh stands for slow start threshold.
- explanation-03: On packet loss, the sender lowers ssthresh and cwnd and adjusts its sending rate downward.
- explanation-04: The operating system gives each process its own security context.
- explanation-04: Processes can be used to bypass a single-process resource limit.
- explanation-04: Processes have separate memory and permissions.
- explanation-06: Writes often require also updating or invalidating the cache.
- explanation-06: Sources of slowness other than the database include network latency, an inefficient algorithm, and slow external API calls.
- explanation-06: Timing can be measured with a profiler or by adding timing logs around each major step.
- explanation-06: The read-to-write ratio can be found in database logs or metrics.
- explanation-07: No relevant memory was found for this question.
- explanation-07: Without a growth rate, a trigger date for sharding cannot be set.
- explanation-07: If reads dominate the workload, read replicas solve the problem more cheaply than sharding.
- explanation-07: Cloud providers offer instances with multiple terabytes of RAM and tens of terabytes of storage.
- explanation-07: Retrofitting a shard key onto an existing schema and data set is harder than designing it upfront.
- explanation-08: A reliable estimate of the benefit depends on the size of a typical payload.
- explanation-08: Binary formats typically reduce payload size by 20-50% compared to JSON.
- explanation-08: Binary formats achieve size savings mostly by dropping field names and using compact number encoding.
- explanation-08: For payloads of a few hundred bytes, a 20-50% size saving amounts to a few dozen bytes.
- explanation-08: Size savings from a binary format can disappear entirely once HTTP overhead or compression is taken into account.
- explanation-08: JSON already benefits from compression.
- explanation-08: Binary encoders and decoders are often 2-10x faster per byte than JSON parsers.
- explanation-08: The real bottleneck could be format size, CPU time, or something unrelated to serialization.
- explanation-08: Each possible bottleneck points to a different fix.
- explanation-08: Sampling representative payloads and comparing JSON size against a binary encoding is a recommended measurement step.
- explanation-08: A quick script using Protocol Buffers or a similar library can produce real payload size numbers in under an hour.
- explanation-08: If serialization is under 5% of request time, a binary format is unlikely to deliver noticeable results.
- explanation-08: If payload size is not a network or storage bottleneck, a binary format is unlikely to deliver noticeable results.
- explanation-08: Switching to a binary format costs debuggability and tooling.
- summarization-01: A tool call failed.
- summarization-01: There is no relevant memory.
- summarization-01: The release notes presented have internal-only items filtered out.
- summarization-01: Each button's tooltip shows its keyboard shortcut.
- summarization-02: The exhausted pool caused errors for about 12% of checkout requests.
- summarization-02: The total response time was about 27 minutes.
- summarization-08: The finding about the progress bar is rated tentative.
- summarization-08: The template gallery observation is not a ranked finding.

### plain-language

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 27 | 0 | 0.0 | 5 | 5 |
| code-review-02 | 17 | 14 | 0.824 | 14 | 2 |
| code-review-03 | 27 | 13 | 0.481 | 15 | 3 |
| code-review-04 | 26 | 15 | 0.577 | 22 | 4 |
| code-review-05 | 33 | 23 | 0.697 | 29 | 4 |
| code-review-06 | 29 | 0 | 0.0 | 3 | 1 |
| code-review-07 | 40 | 0 | 0.0 | 2 | 2 |
| code-review-08 | 29 | 26 | 0.897 | 33 | 5 |
| debugging-01 | 7 | 7 | 1.0 | 9 | 2 |
| debugging-02 | 18 | 13 | 0.722 | 16 | 1 |
| debugging-03 | 13 | 13 | 1.0 | 9 | 0 |
| debugging-04 | 15 | 11 | 0.733 | 16 | 4 |
| debugging-05 | 19 | 18 | 0.947 | 13 | 0 |
| debugging-06 | 35 | 23 | 0.657 | 32 | 11 |
| debugging-07 | 2 | 1 | 0.5 | 27 | 27 |
| debugging-08 | 1 | 0 | 0.0 | 5 | 5 |
| explanation-01 | 37 | 28 | 0.757 | 22 | 0 |
| explanation-02 | 32 | 20 | 0.625 | 26 | 4 |
| explanation-03 | 28 | 9 | 0.321 | 20 | 1 |
| explanation-04 | 35 | 0 | 0.0 | 0 | 0 |
| explanation-05 | 16 | 11 | 0.688 | 15 | 2 |
| explanation-06 | 16 | 13 | 0.812 | 18 | 4 |
| explanation-07 | 21 | 11 | 0.524 | 32 | 13 |
| explanation-08 | 15 | 0 | 0.0 | 0 | 0 |
| summarization-01 | 6 | 6 | 1.0 | 10 | 4 |
| summarization-02 | 11 | 10 | 0.909 | 12 | 0 |
| summarization-03 | 15 | 15 | 1.0 | 15 | 0 |
| summarization-04 | 14 | 13 | 0.929 | 11 | 1 |
| summarization-05 | 9 | 8 | 0.889 | 11 | 1 |
| summarization-06 | 15 | 15 | 1.0 | 13 | 0 |
| summarization-07 | 14 | 14 | 1.0 | 14 | 1 |
| summarization-08 | 21 | 20 | 0.952 | 21 | 4 |

Median fraction: 0.728 over 32 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: A mutable default argument like `roles=[]` is created once at function definition time.
- code-review-01: A mutable default list is shared across all calls that do not pass `roles` explicitly.
- code-review-01: The function mutates `roles` by calling `.append` on it.
- code-review-01: Repeated calls that omit `roles` keep appending to the same shared list.
- code-review-01: The second call that omits `roles` already sees `"member"` from the first call before appending another `"member"`.
- code-review-01: A bare `except:` catches `KeyboardInterrupt`, `SystemExit`, and `MemoryError`, not just expected failures.
- code-review-01: A bare `except:` silently discards the actual error.
- code-review-01: The bare `except:` makes a bad `db`, a network error, a validation error, and a programmer typo indistinguishable from one another.
- code-review-01: Returning `False` gives the caller no information about the failure.
- code-review-01: The `db` parameter has a default value of `None`.
- code-review-01: If `db` is `None`, calling `db.insert(...)` raises `AttributeError`.
- code-review-01: That `AttributeError` is swallowed by the bare except and reported as a normal "failed" return instead of a visible crash.
- code-review-01: If the caller forgets to pass `db`, the function returns `False` via the except clause rather than failing loudly.
- code-review-01: The function has no explicit check or error for a missing required dependency.
- code-review-01: When a caller passes their own `roles` list, `roles.append("member")` mutates that list in place as a side effect.
- code-review-01: A caller may not expect their list to be changed by calling `add_user`.
- code-review-01: If `"member"` is already in `roles`, it is appended again, producing `["member", "member"]`.
- code-review-01: The function performs no validation on `name`, such as checking for an empty string or wrong type.
- code-review-01: The function performs no validation that `roles` is actually a list.
- code-review-01: A `True`/`False` return value tells the caller nothing about why the call failed or what was inserted, such as a created user ID.
- code-review-01: The uninformative return value combined with the bare except makes debugging failures very hard.
- code-review-01: The suggested fix uses `roles=None` as the default and assigns a new empty list when it is `None`.
- code-review-01: The suggested fix copies the caller's list with `list(roles)` to avoid mutating it.
- code-review-01: The suggested fix appends `"member"` only if it is not already in `roles`.
- code-review-01: The suggested fix makes `db` a required parameter.
- code-review-01: The suggested fix lets real exceptions propagate instead of hiding them.
- code-review-01: Specific exceptions can be caught at the call site if needed.
- code-review-02: The function is declared `async` but never uses `await`.
- code-review-02: Declaring a function `async` without using `await` is a strong signal the promise chain was meant to be awaited but isn't.
- code-review-02: Parsing an error response as JSON can produce bad data or a parse error.
- code-review-03: Passing `status` as `' OR '1'='1` returns every order.
- code-review-03: Stacked queries can enable worse attacks, depending on the database driver.
- code-review-03: `SELECT *` can silently break if column order changes.
- code-review-03: The code has no input validation or type checking.
- code-review-03: If `customer_name` or `status` is not a string (e.g. `None`), the `+` concatenation raises a `TypeError`.
- code-review-03: A `TypeError` from concatenation is raised instead of a meaningful error.
- code-review-03: The code does not handle `fetchall()` on large result sets.
- code-review-03: If a customer has many orders, `fetchall()` loads everything into memory at once.
- code-review-03: Pagination or `fetchmany()` is worth considering for large datasets.
- code-review-03: The code has no error handling around `cursor.execute`.
- code-review-03: A database error such as a bad connection or a locked table will propagate as a raw exception with no context about what operation failed.
- code-review-03: Exact string matching makes the query case-sensitive.
- code-review-03: Case-insensitive matching or normalization such as trimming whitespace may be wanted, depending on requirements.
- code-review-03: The SQL injection must be fixed before the code goes to production.
- code-review-04: This read-modify-write pattern is a TOCTOU (time-of-check-to-time-of-use) bug.
- code-review-04: CPython has a GIL (Global Interpreter Lock).
- code-review-04: The GIL only guarantees that individual bytecode operations are atomic.
- code-review-04: The GIL can switch threads between the read and the write of a read-modify-write sequence.
- code-review-04: Every method of the class is unsafe to call concurrently with any other method, including itself.
- code-review-04: A single attribute read or write is atomic in CPython.
- code-review-04: Reading counter.value will not return garbage.
- code-review-04: Nothing in the class signals to callers that reading .value as part of a larger operation is dangerous.
- code-review-04: The proposed fix uses a threading.Lock acquired via 'with' in increment(), reset(), and a value property.
- code-review-04: itertools.count() is thread-safe in CPython.
- code-review-04: itertools.count() and multiprocessing.Value are lock-free alternatives worth considering for higher throughput under heavy contention.
- code-review-05: `cd` can fail due to a nonexistent directory, permissions, or a typo.
- code-review-05: `cd "$BACKUP_DIR" || exit 1` is the recommended form.
- code-review-05: A caller could pass `/` or `/home` and the script would `cd` there and delete `*.tmp` files.
- code-review-05: If no `.log` files exist, `ls *.log` prints a "No such file or directory" error to stderr.
- code-review-05: When `ls *.log` matches nothing, the loop harmlessly does not execute.
- code-review-05: Using a bare glob avoids the stderr error message.
- code-review-05: In plain `sh`/dash an unmatched glob does not match, so the literal-glob issue does not arise there.
- code-review-05: `gzip` can fail on a read-only file or an already-gzipped file.
- code-review-05: The `-f` flag in `rm -rf *.tmp` suppresses errors.
- code-review-05: Suppressing errors with `-f` is fine for the no-match case but also silently masks permission errors.
- code-review-06: The function merge_settings only merges dicts, not lists, sets, or other container types.
- code-review-06: When both merged[key] and value are lists, the override list replaces the base list entirely instead of being merged or extended.
- code-review-06: The list-replacement behavior is inconsistent with the function's dict-merging behavior.
- code-review-06: The recursive branch checks that merged[key] is a dict but does not check that value is a dict.
- code-review-06: If merged[key] is a dict and override[key] is a string, the code calls merge_settings(some_dict, "a_string").
- code-review-06: Strings do not have an .items() method.
- code-review-06: Passing a string as the override argument raises AttributeError: 'str' object has no attribute 'items' inside the recursion.
- code-review-06: The resulting traceback appears far from the actual bad input, making it confusing.
- code-review-06: The code should check isinstance(value, dict) before recursing.
- code-review-06: The function uses dict(base), which is a shallow copy of only the top-level dict.
- code-review-06: Nested dicts and lists inside base are shared by reference with the original after dict(base).
- code-review-06: Nested dict values that are overridden produce new merged dicts because of the recursive branch.
- code-review-06: Nested dicts not touched by override remain shared with base's originals.
- code-review-06: In-place mutation of nested structures in the returned result can silently corrupt base.
- code-review-06: A None value in the override always deletes the key.
- code-review-06: The function provides no way to explicitly set a key's value to None.
- code-review-06: The function cannot distinguish removing a key from setting a key's value to None.
- code-review-06: The function can never produce a None settings value.
- code-review-06: The function has four distinct branch behaviors: adding new keys, deleting keys on None, recursively merging dict-vs-dict, and overwriting everything else.
- code-review-06: pop(key, None) does not crash when the key being deleted is absent from merged.
- code-review-06: The function has no naming or documentation distinguishing its four behaviors.
- code-review-06: Using None to delete a key is a common intentional convention in config-merging code.
- code-review-06: Recursive dict merging is a deliberate design choice and the main purpose of the function.
- code-review-06: Non-dict override values winning outright is the expected default merge semantics.
- code-review-06: The missing isinstance(value, dict) check is likely an oversight rather than intentional.
- code-review-06: The shallow copy of unmerged nested structures is very unlikely to be intentional.
- code-review-06: The asymmetry between list and dict handling is more likely an incomplete implementation than a deliberate choice.
- code-review-06: There are currently no tests for the code.
- code-review-06: Writing tests that pin down current behavior before changing anything is the recommended approach.
- code-review-07: When retries are exhausted on 429 or 5xx responses, the for loop ends and the function returns undefined.
- code-review-07: There is no return statement after the retry loop.
- code-review-07: An error that is not a 429 or 5xx causes the function to explicitly return null.
- code-review-07: The function uses two different sentinel values, null and undefined, to signal failure.
- code-review-07: If fn can legitimately return null or undefined, callers cannot distinguish success from failure.
- code-review-07: The backoff delay is computed as 1000 * i.
- code-review-07: On the first failure, i equals 0, so the wait is 0ms.
- code-review-07: Backoff effectively only begins on the second retry.
- code-review-07: The zero first delay appears to be an off-by-one error where i + 1 was likely intended.
- code-review-07: The zero-delay first backoff is not documented and is inconsistent with the rest of the backoff logic.
- code-review-07: On the final loop iteration, a 429 still triggers the setTimeout wait before the loop exits.
- code-review-07: The delay on the final attempt is wasted because there is no subsequent attempt.
- code-review-07: All non-retryable errors are swallowed and converted to a return of null, with no rethrow and no logging.
- code-review-07: Swallowed errors include genuine programming bugs such as TypeError from a null dereference inside fn, ReferenceError, and JSON parse failures.
- code-review-07: Errors without an err.status property have err.status equal to undefined.
- code-review-07: For undefined status, both undefined === 429 and undefined >= 500 evaluate to false.
- code-review-07: Errors without a status fall through to return null in the same way a 404 does.
- code-review-07: Converting all errors to null conflates API rejections with broken code.
- code-review-07: Returning null destroys the error's stack trace and message.
- code-review-07: Unseen callers may already depend on the 'errors become null' behavior.
- code-review-07: Swallowing errors as null is the riskiest issue because it hides programming errors rather than only HTTP failures.
- code-review-07: Errors with err.status >= 500 are retried immediately with no delay.
- code-review-07: 429 errors receive a linear backoff.
- code-review-07: Immediate retries against an unhealthy downstream service hammer that service.
- code-review-07: The backoff has no jitter.
- code-review-07: A fixed 1000 * i backoff causes concurrent callers hitting a 429 to retry in lockstep.
- code-review-07: Retrying in lockstep is the thundering-herd problem that jittered backoff is designed to prevent.
- code-review-07: There is no upper bound check on err.status >= 500.
- code-review-07: Any status of 500 or greater, including nonstandard or custom codes, is treated as retryable.
- code-review-07: There is no err.status < 600 guard, so the condition means '>= 500' rather than '5xx'.
- code-review-07: When attempts <= 0, the function returns undefined without ever calling fn.
- code-review-07: There is no validation or error raised for an attempts value of 0 or less.
- code-review-07: The function contains no logging anywhere.
- code-review-07: Without logging, the function fails silently in production.
- code-review-07: Combined with the null swallow, an outage would be indistinguishable from everything returning null.
- code-review-07: Retry-on-429, retry-on-5xx, and giving up on other errors form a recognizable rate-limit and transient-error retry pattern.
- code-review-07: The retry-on-429 and retry-on-5xx behavior appears intentional.
- code-review-07: The 1000 * i zero-first-delay and the null-versus-undefined failure inconsistency are almost certainly bugs.
- code-review-07: Swallowing all non-status errors as null without logging or rethrow is ambiguous in intent but risky regardless.
- code-review-07: Even as a deliberate 'always resolve, never reject' contract, swallowing errors is indistinguishable from silently eating bugs.
- code-review-08: Calling `os.path.getmtime` on a broken symlink raises `FileNotFoundError`.
- code-review-08: Immediate deletion of tmp-/.part files could be deliberate if writer processes rename atomically on completion.
- code-review-08: No one owns the script's schedule.
- debugging-02: The global object is referred to as `window` or `globalThis`.
- debugging-02: Accessing `this.seconds` throws if `this` is `undefined` in strict mode.
- debugging-02: The `NaN` value is logged and reassigned on each tick of the interval.
- debugging-02: `.bind(this)` on a regular function callback is an alternative fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-04: chardet and charset-normalizer are libraries for detecting encoding.
- debugging-04: A file can be opened in binary mode with the "rb" mode string.
- debugging-04: Counting occurrences of b"\n" in binary mode yields a line count.
- debugging-04: Opening the file in binary mode avoids decoding entirely.
- debugging-05: `tags = list(DEFAULT_TAGS)` can be replaced with `["draft"]`.
- debugging-06: The working directory is empty.
- debugging-06: There is no code to inspect, so the task is pure log analysis.
- debugging-06: Dashboard refreshes and scheduled analytics queries are examples of unpredictable analytics traffic spikes.
- debugging-06: A slow analytics query can be caused by a missing index or a table scan.
- debugging-06: A mismatch between pool size and instance/replica count is a plausible cause.
- debugging-06: If a service scaled up its workers or replicas without raising the database max-connections or pool size, exhaustion becomes a matter of timing rather than a deterministic bug.
- debugging-06: Retention for metrics is often longer than log retention and cheaper to keep.
- debugging-06: The failure window on the observed night spanned 02:14:07 to 02:14:41.
- debugging-06: A single WARN or ERROR line without pool size, active count, or caller identity is hard to act on.
- debugging-06: Comparing pool configuration against total client count is a way to narrow down the cause.
- debugging-06: The comparison involves the sum of max pool size across all export workers and analytics service instances versus the database's max_connections.
- debugging-06: If total configured pool size is close to the database's max_connections, a small ephemeral spike such as a deploy restart or an extra worker is enough to exhaust it.
- debugging-07: There is memory that may be relevant to the task.
- debugging-08: The session ID is 4988878c-7c4a-4c17-92eb-92beb2d5be32.
- explanation-01: Chaining is also known as separate chaining.
- explanation-01: The collection in a chaining slot is usually a linked list, and sometimes a tree or array.
- explanation-01: Quadratic probing jumps by increasing squares.
- explanation-01: Double hashing uses a second hash function to compute the step.
- explanation-01: Chaining has worse cache performance because linked list nodes are scattered in memory.
- explanation-01: Open addressing has better cache performance because probing stays within the array.
- explanation-01: Open addressing implementations often resize at around a 70% load factor.
- explanation-01: Open addressing requires careful tuning of load factor thresholds and probing scheme, and more complex deletion logic.
- explanation-01: Go's map uses a bucket-based chaining variant.
- explanation-02: An optimistic locking example uses a `products` table with a `version` integer column.
- explanation-02: An optimistic stock update can be written as `UPDATE products SET stock = stock - 1, version = version + 1 WHERE id = 42 AND version = 7;`.
- explanation-02: If the row's version is no longer 7 because someone else updated it first, the UPDATE affects 0 rows.
- explanation-02: When 0 rows are affected, the application detects the conflict and retries or surfaces an error.
- explanation-02: Optimistic locking fits when transactions are short and fast.
- explanation-02: Examples of good fits for optimistic locking include a web app editing user profiles, e-commerce catalog updates, and most CRUD APIs.
- explanation-02: A pessimistic transfer example uses BEGIN, two `SELECT balance FROM accounts WHERE id = ... FOR UPDATE` statements, balance updates, and COMMIT.
- explanation-02: `FOR UPDATE` locks the selected rows.
- explanation-02: Rows locked with `FOR UPDATE` cannot be modified by other transactions until the locking transaction commits or rolls back.
- explanation-02: In some databases, `FOR UPDATE` prevents other transactions from even reading the locked rows.
- explanation-02: Financial transfers, inventory reservation for a flash sale, and seat booking systems are examples where pessimistic locking fits.
- explanation-02: Pessimistic locking risks contention and deadlocks.
- explanation-03: A network path may consist of a single fast link or may cross several routers of varying speed and load.
- explanation-03: If a sender transmitted at whatever rate the receiver's window allowed, it could send more data than routers along the path can forward.
- explanation-03: Routers buffer excess packets.
- explanation-03: Router buffers are finite.
- explanation-03: When router buffers fill up, packets are dropped.
- explanation-03: Persistent overloading of the network causes congestive collapse.
- explanation-03: In congestive collapse, throughput drops sharply even though all senders are trying to send at full speed.
- explanation-03: Slow start is TCP's mechanism for finding a safe sending rate on an unknown path without causing congestive collapse.
- explanation-03: The sender maintains a congestion window (cwnd) in addition to the receiver's advertised window.
- explanation-03: The amount of data in flight is limited by the smaller of the congestion window and the receiver's advertised window.
- explanation-03: Historically, the initial cwnd was 1 segment.
- explanation-03: Modern TCP implementations typically start with an initial cwnd of around 10 segments.
- explanation-03: RFC 6928 specifies the initial window of around 10 segments.
- explanation-03: During slow start, cwnd increases by one segment for every ACK received.
- explanation-03: A full window of data generates a full window of ACKs.
- explanation-03: Slow start continues until a packet loss or ECN mark is detected, or until cwnd reaches the ssthresh threshold.
- explanation-03: A detected packet loss or ECN mark is interpreted as a signal that the network is congested.
- explanation-03: ssthresh is the name of the slow start threshold.
- explanation-03: In congestion avoidance, cwnd growth is linear, roughly +1 segment per RTT.
- explanation-04: A process is an independent execution unit with its own memory address space, file descriptors, and OS resources.
- explanation-04: Processes do not share memory by default.
- explanation-04: Communicating between processes requires IPC such as pipes, sockets, or shared memory segments.
- explanation-04: A thread is an execution unit within a process.
- explanation-04: All threads in a process share the same memory address space, heap, and file descriptors.
- explanation-04: Each thread has its own stack and register state.
- explanation-04: Communication between threads is done by accessing shared memory, with appropriate synchronization.
- explanation-04: A crash in one process does not take down another process.
- explanation-04: A crash in one thread, such as a segfault, usually kills the whole process.
- explanation-04: Creating and switching processes is more expensive than creating and switching threads.
- explanation-04: The higher cost of processes comes from separate memory spaces and OS bookkeeping.
- explanation-04: Threads sharing memory directly is fast but requires locks or synchronization to avoid race conditions.
- explanation-04: Inter-process communication is slower than shared-memory communication but is naturally isolated.
- explanation-04: CPython has a global interpreter lock (GIL).
- explanation-04: Under a global interpreter lock, threads cannot run Python bytecode in true parallel on multiple cores.
- explanation-04: Under a GIL, only one thread executes bytecode at a time.
- explanation-04: Processes bypass the GIL because each process has its own interpreter.
- explanation-04: Python and older Ruby are languages with a GIL.
- explanation-04: The GIL serializes bytecode execution, so threads do not give real parallelism for CPU-heavy tasks.
- explanation-04: Multiple processes each get their own interpreter and GIL and can run on separate cores.
- explanation-04: Python's multiprocessing module exists specifically to enable real parallelism for CPU-bound work.
- explanation-04: Separate processes contain the blast radius when one unit of work crashes.
- explanation-04: A crashed worker process can be restarted without affecting other processes.
- explanation-04: Processes have separate memory spaces enforced by the OS/MMU.
- explanation-04: One process cannot read another process's memory, barring shared segments.
- explanation-04: Process isolation matters for sandboxing untrusted code, such as browser tabs and containers.
- explanation-04: Threads offer no security isolation boundary.
- explanation-04: Using processes for largely independent work avoids race conditions, deadlocks, and lock contention.
- explanation-04: Using processes requires explicit IPC when communication is needed.
- explanation-04: A process-based architecture with workers communicating via queues or sockets generalizes naturally to multiple machines.
- explanation-04: Thread-based designs assume a single shared address space and do not extend across machines.
- explanation-04: Threads are preferable for I/O-bound concurrency where many threads wait on network or disk.
- explanation-04: Threads have low memory overhead and allow fast, frequent communication between concurrent units.
- explanation-04: Spinning up a full process per connection would be wasteful.
- explanation-04: Shared-memory access is more efficient than IPC for tightly coupled work.
- explanation-05: A collection can be kept reachable by being held by a long-lived singleton.
- explanation-05: A listener's closure often captures its whole surrounding scope, including large objects and DOM nodes.
- explanation-05: Static or global variables accumulating data is another frequent cause of memory leaks.
- explanation-05: Mutual references between long-lived and short-lived objects are another frequent cause of memory leaks.
- explanation-05: Mutual references can keep a short-lived object artificially alive.
- explanation-06: The complexity added by a cache includes cache invalidation, staleness, and another system to operate.
- explanation-06: Profiling is cheap.
- explanation-06: Timing middleware and slow query logs are examples of basic profiling.
- explanation-07: Reaching 2-5TB within a year would justify planning for sharding ahead of time.
- explanation-07: Sharding addresses write and connection bottlenecks more than it addresses raw disk size.
- explanation-07: Under sharding, cross-shard transactions and joins become application-level problems.
- explanation-07: Sharding eliminates free ACID guarantees across the whole dataset.
- explanation-07: Sharding makes migrations, backups, monitoring, and debugging harder for every feature.
- explanation-07: Exceeding vertical scaling limits before sharding infrastructure exists results in downtime or degraded performance.
- explanation-07: PostgreSQL has native table partitioning that can partition by tenant or date.
- explanation-07: Logical partitioning is far cheaper to implement than sharding.
- explanation-07: Partitions map naturally to shards, so partitioning provides leverage if sharding becomes necessary.
- explanation-07: Logical partitioning buys time to observe growth rate before committing to a shard key.
- explanation-08: Without measurements, one cannot say whether the proposed change is worthwhile.
- explanation-08: The user is missing the prerequisite data needed to scope the proposal properly.
- explanation-08: Two numbers matter for this decision, and the user has neither of them.
- explanation-08: One key number is what fraction of request latency is spent on serialization/deserialization.
- explanation-08: If JSON parsing is 2% of request time, a binary format that parses 3x faster saves about 1.3% end-to-end.
- explanation-08: If serialization/deserialization is 40% of request time, a 3x parsing speedup is meaningful.
- explanation-08: Huge payloads or a hot loop are cases where serialization can account for 40% of request time.
- explanation-08: The second key number is how binary formats compare for the user's actual payload shape.
- explanation-08: Gains from Protobuf, msgpack, and FlatBuffers vary a lot depending on the payload shape.
- explanation-08: Payload characteristics that affect binary format gains include deep nesting, string-heaviness, numeric-heaviness, and repetitiveness.
- explanation-08: A generic claim that binary is faster can be off by an order of magnitude in either direction for a specific schema.
- explanation-08: Profiling a representative request path would show time spent in serialize/deserialize versus network, DB, and business logic.
- explanation-08: Benchmarking one or two candidate formats against real sample payloads is a recommended step.
- explanation-08: The profiling and benchmarking work would take a few hours.
- explanation-08: Doing the profiling and benchmarking turns the decision from a guess into one backed by numbers.
- summarization-02: Staging's connection pool size is intentionally small at 5.
- summarization-04: PDF export on the Reports page fails silently.
- summarization-05: Ada is assigned to check with the mobile team's lead about whether the mobile team has been informed of the API deprecation.
- summarization-08: The abandonment finding is firm, but the cause of the abandonment is tentative.

Added facts (styled only):

- code-review-01: A read operation is invoked on the file at /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-wb6o1l2o/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-0lx55all/memory/MEMORY.md
- code-review-01: The file being read is named MEMORY.md
- code-review-01: MEMORY.md is located in a directory named memory
- code-review-01: The memory directory is under a project directory named -private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-0lx55all
- code-review-01: That project directory is inside a projects directory under /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-wb6o1l2o
- code-review-02: Without error handling, callers get an unhandled rejection instead of a clear error.
- code-review-02: If the API returns a user without a `name` field, calling `.toUpperCase()` will throw.
- code-review-03: The function has no type hints.
- code-review-03: The function has no docstring.
- code-review-03: Adding `customer_name: str`, `status: str`, and a return-type hint would make the function easier to use correctly.
- code-review-04: In the fixed version, `__init__` sets `self.value = 0` and `self._lock = threading.Lock()`.
- code-review-04: In the fixed version, `increment()` executes `self.value += 1` while holding `self._lock`.
- code-review-04: In the fixed version, `reset()` sets `self.value = 0` while holding `self._lock`.
- code-review-04: In the fixed version, `get()` returns `self.value` while holding `self._lock`.
- code-review-05: If `BACKUP_DIR` is empty, missing, or invalid, `cd $BACKUP_DIR` fails.
- code-review-05: The unchecked `cd` followed by `rm -rf *.tmp` is the most dangerous bug in the script.
- code-review-05: If no `*.log` files exist, the loop runs once with the literal string `*.log` as the filename.
- code-review-05: When the loop runs with the literal string `*.log`, `gzip` fails with an error.
- code-review-06: A read tool was used.
- code-review-07: The speaker will check memory for relevant guidance.
- code-review-07: The memory check will happen before reviewing.
- code-review-08: The script does not check that ROOT exists.
- code-review-08: If the mount point is missing, `os.listdir(ROOT)` throws and the script dies with no cleanup and no record of why.
- code-review-08: The script has no lock file.
- code-review-08: If schedule runs overlap, two copies could run at once and race on the same files.
- code-review-08: The recommended fixes in order of risk are: add an age check before deleting `tmp-*`/`.part` files, apply the 500 cap to all deletions, add a directory/isfile guard, wrap each deletion in try/except, and add logging.
- debugging-01: The faulty lookup is on line 4 of `app.py`.
- debugging-01: The fix is to change `Port` to `port` in `app.py` line 4.
- debugging-02: The global object is `global` in Node.
- debugging-04: The error identifies byte 0xc3 at position 512.
- debugging-04: The byte 0xc3 starts a two-byte UTF-8 character.
- debugging-04: UTF-8 can decode plain ASCII text.
- debugging-04: Because UTF-8 handles ASCII text, switching to UTF-8 is safe for every file, not only the failing one.
- debugging-06: The export job and the analytics service share the same database.
- debugging-06: Analytics hogging connections is the most likely cause, given the shared database.
- debugging-06: High CPU or disk I/O on the database can slow every query down.
- debugging-06: When queries are slowed by database overload, connections stay checked out longer and the pool fills up faster.
- debugging-06: Most connection pool libraries expose active connections, idle connections, and queue length metrics.
- debugging-06: Active connections trending upward over hours or days while idle points to a leak rather than contention.
- debugging-06: Giving the export job its own connection pool separate from the analytics service is a pragmatic interim fix.
- debugging-06: PgBouncer is a proxy that can be used to separate the export job's connections from the analytics service's.
- debugging-06: Isolating the two workloads prevents the analytics service from starving the export job.
- debugging-06: Isolating the workloads does not reveal the root cause.
- debugging-06: Whether the failures stop after isolating the workloads will confirm or rule out contention as the cause.
- debugging-07: The most likely cause of the intermittent failure is a race between writing events and reading the digest.
- debugging-07: The failure pattern indicates a timing (race) condition rather than random bad luck.
- debugging-07: A test that seeds data through an API and immediately reads it back will fail intermittently if the write path is not guaranteed to finish before the read.
- debugging-07: Event creation that triggers a background job, queue, or async worker instead of writing synchronously is an example of a write path that isn't guaranteed to finish before a read.
- debugging-07: Parallel workers make the race condition more likely to show up.
- debugging-07: Four workers compete for CPU and I/O.
- debugging-07: Resource contention makes background jobs and database writes take longer.
- debugging-07: Under contention, writes are more likely to still be in flight when the digest is requested.
- debugging-07: If test events or the digest are keyed by something not unique per test run, two tests running concurrently on different workers can interfere with each other's data.
- debugging-07: Examples of non-unique keys are a shared date window, a shared user, or a timestamp with too little precision.
- debugging-07: If the digest logic dedupes events by timestamp and two events land in the same millisecond, one event could be dropped.
- debugging-07: If the test doesn't check that all three seed calls succeeded, a failed or timed-out seed call would go unnoticed until the assertion.
- debugging-07: The test makes three seed calls.
- debugging-07: If the digest reads from a cache or a read replica that lags the write, the fourth worker's extra load could make the lag large enough to matter.
- debugging-07: Running the full suite locally in a loop with the same worker count CI uses reproduces the parallelism, not just the test.
- debugging-07: `pytest -n 4` runs the test suite with four workers.
- debugging-07: If the failure reproduces locally under load, parallelism rather than something CI-specific is the trigger.
- debugging-07: The CI setup keeps no artifacts.
- debugging-07: Diagnostics should be added temporarily and logged only on failure.
- debugging-07: Useful diagnostics include the worker ID, timestamps for each seed call and its response, and the digest response.
- debugging-07: Attaching diagnostics as a CI artifact removes the need to guess on the next failure.
- debugging-07: Test data should be checked for anything shared across workers, such as a fixed user ID, date, or time window.
- debugging-07: Shared test identifiers should be replaced with unique, per-test identifiers.
- debugging-07: The event creation API handler should be checked for whether it writes directly or hands off to a queue or background job.
- debugging-07: If event creation is asynchronous, the test must wait for confirmation via polling or a completion signal before requesting the digest.
- debugging-07: If events are deduped by timestamp, the timestamp resolution should be fine enough that two events created in quick succession cannot collide.
- debugging-07: Step 1 is the fastest way to confirm parallelism is the trigger before investing time in the deeper checks.
- debugging-08: The assistant will check memory for earlier context on the service.
- debugging-08: A memory directory is located at /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-wb6o1l2o/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-0lx55all/memory/.
- debugging-08: The command is run in PowerShell.
- debugging-08: The command uses `ls` to list the contents of the memory directory.
- debugging-08: The command redirects error output to $null to suppress errors.
- explanation-02: Under pessimistic locking, no one else can read or edit the locked record until the lock is released.
- explanation-02: Pessimistic locking works well when transactions are short, because wait time stays small.
- explanation-02: A document-editing app may store a `version` column on each document.
- explanation-02: If a user loads version 5 of a document and someone else saves version 6 first, the user's save fails and they must reload the latest version before retrying.
- explanation-03: Slow start is called 'slow' only in comparison to sending everything at once.
- explanation-05: In a garbage-collected language, the garbage collector is a background process that frees memory used by objects the code can no longer reach.
- explanation-05: UI components and event buses are examples of long-lived objects.
- explanation-06: If data changes often, a cache adds complexity without much benefit.
- explanation-06: Keeping cached data in sync with the database is a new source of bugs.
- explanation-06: Most profiling tools can show where time is spent.
- explanation-06: Slow database queries include queries that scan large tables.
- explanation-07: The assistant checked its memory for relevant project context and prior guidance.
- explanation-07: The memory contained nothing about database sharding or PostgreSQL architecture.
- explanation-07: The answer is based on general practice rather than stored project context.
- explanation-07: Before sharding, one should check whether the current instance is actually hitting a limit.
- explanation-07: Relevant metrics to check are CPU, memory, disk I/O, and query latency.
- explanation-07: If no metric is close to a limit, there is no problem to solve yet.
- explanation-07: Scaling up or adding read replicas often solves growth problems for years.
- explanation-07: Sharding hurts more than it helps when queries need global uniqueness or ordering.
- explanation-07: Spending engineering time on premature sharding delays other work.
- explanation-07: Single-machine limits, write throughput, and lock contention are limits of scaling up a single instance.
- explanation-07: The recommendation is to add monitoring for CPU, memory, disk I/O, and query latency now.
- explanation-07: Monitoring these metrics now gives early warning signs.
- explanation-07: An example of a concrete justifying number is projecting to hit the disk I/O limit in 6 months at the current growth rate.
- summarization-01: The assistant checked its stored memory for relevant preferences before writing the release notes.
- summarization-01: The memory contained nothing relevant to this task.
- summarization-01: The release notes omit a build tooling bump, a session module refactor, and a telemetry batching change.
- summarization-01: The build tooling bump, session module refactor, and telemetry batching change are internal and do not affect how the user uses the app.
- summarization-04: Four identical "export failed" error banners appear after the repeated PDF export clicks.
- summarization-05: The listed items are action items from a meeting.
- summarization-07: The summary is one paragraph and intended for the team lead.
- summarization-08: The progress bar finding is tentative.
- summarization-08: The sample is too small to know how widespread the progress bar problem is.
- summarization-08: It is not yet known whether the progress bar fix is visual (better progress feedback) or behavioral (user expectations).
- summarization-08: The template gallery observation is not one of the three main findings.

### technical-simplified

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 27 | 22 | 0.815 | 23 | 4 |
| code-review-02 | 17 | 14 | 0.824 | 18 | 2 |
| code-review-03 | 27 | 14 | 0.519 | 15 | 3 |
| code-review-04 | 26 | 14 | 0.538 | 16 | 1 |
| code-review-05 | 33 | 20 | 0.606 | 39 | 9 |
| code-review-07 | 40 | 0 | 0.0 | 7 | 7 |
| code-review-08 | 29 | 23 | 0.793 | 38 | 9 |
| debugging-01 | 7 | 7 | 1.0 | 9 | 2 |
| debugging-02 | 18 | 12 | 0.667 | 13 | 0 |
| debugging-03 | 13 | 13 | 1.0 | 11 | 0 |
| debugging-04 | 15 | 9 | 0.6 | 9 | 0 |
| debugging-05 | 19 | 18 | 0.947 | 17 | 2 |
| debugging-06 | 35 | 18 | 0.514 | 19 | 4 |
| explanation-01 | 37 | 15 | 0.405 | 20 | 3 |
| explanation-02 | 32 | 19 | 0.594 | 23 | 1 |
| explanation-03 | 28 | 11 | 0.393 | 15 | 1 |
| explanation-04 | 35 | 18 | 0.514 | 19 | 2 |
| explanation-05 | 16 | 10 | 0.625 | 14 | 2 |
| explanation-06 | 16 | 13 | 0.812 | 25 | 0 |
| explanation-07 | 21 | 13 | 0.619 | 30 | 14 |
| explanation-08 | 15 | 9 | 0.6 | 11 | 5 |
| summarization-01 | 6 | 5 | 0.833 | 5 | 0 |
| summarization-02 | 11 | 6 | 0.545 | 10 | 4 |
| summarization-03 | 15 | 15 | 1.0 | 14 | 0 |
| summarization-04 | 14 | 10 | 0.714 | 11 | 2 |
| summarization-05 | 9 | 8 | 0.889 | 8 | 0 |
| summarization-07 | 14 | 14 | 1.0 | 15 | 2 |

Median fraction: 0.625 over 27 scored pairs.

Median additions: 2 over 27 scored pairs.

Lost facts:

- code-review-01: When a caller passes their own `roles` list, `roles.append("member")` mutates that list in place as a side effect.
- code-review-01: A caller may not expect their list to be changed by calling `add_user`.
- code-review-01: The function performs no validation that `roles` is actually a list.
- code-review-01: A `True`/`False` return value tells the caller nothing about why the call failed or what was inserted, such as a created user ID.
- code-review-01: The suggested fix makes `db` a required parameter.
- code-review-02: Declaring a function `async` without using `await` is a strong signal the promise chain was meant to be awaited but isn't.
- code-review-02: `fetch` only rejects on network failure.
- code-review-02: Parsing an error response as JSON can produce bad data or a parse error.
- code-review-03: User-controlled input containing a single quote breaks out of the string literal in the query.
- code-review-03: Stacked queries can enable worse attacks, depending on the database driver.
- code-review-03: `SELECT *` gives callers columns they did not ask for.
- code-review-03: `SELECT *` can silently break if column order changes.
- code-review-03: If `customer_name` or `status` is not a string (e.g. `None`), the `+` concatenation raises a `TypeError`.
- code-review-03: A `TypeError` from concatenation is raised instead of a meaningful error.
- code-review-03: The code does not handle `fetchall()` on large result sets.
- code-review-03: If a customer has many orders, `fetchall()` loads everything into memory at once.
- code-review-03: Pagination or `fetchmany()` is worth considering for large datasets.
- code-review-03: Exact string matching makes the query case-sensitive.
- code-review-03: Case-insensitive matching or normalization such as trimming whitespace may be wanted, depending on requirements.
- code-review-03: The SQL injection must be fixed before the code goes to production.
- code-review-03: The issues other than SQL injection are secondary robustness and design concerns.
- code-review-04: This read-modify-write pattern is a TOCTOU (time-of-check-to-time-of-use) bug.
- code-review-04: CPython has a GIL (Global Interpreter Lock).
- code-review-04: The GIL only guarantees that individual bytecode operations are atomic.
- code-review-04: The GIL can switch threads between the read and the write of a read-modify-write sequence.
- code-review-04: 100,000 increments from 10 threads will often produce a final value less than 100,000.
- code-review-04: Every method of the class is unsafe to call concurrently with any other method, including itself.
- code-review-04: A single attribute read or write is atomic in CPython.
- code-review-04: Reading counter.value will not return garbage.
- code-review-04: Nothing in the class signals to callers that reading .value as part of a larger operation is dangerous.
- code-review-04: The proposed fix uses a threading.Lock acquired via 'with' in increment(), reset(), and a value property.
- code-review-04: itertools.count() is thread-safe in CPython.
- code-review-04: itertools.count() and multiprocessing.Value are lock-free alternatives worth considering for higher throughput under heavy contention.
- code-review-05: `cd` can fail due to a nonexistent directory, permissions, or a typo.
- code-review-05: The script performs no sanity check on the supplied path.
- code-review-05: A caller could pass `/` or `/home` and the script would `cd` there and delete `*.tmp` files.
- code-review-05: `for f in $(ls *.log)` mishandles filenames starting with `-` or containing glob-special characters.
- code-review-05: If no `.log` files exist, `ls *.log` prints a "No such file or directory" error to stderr.
- code-review-05: When `ls *.log` matches nothing, the loop harmlessly does not execute.
- code-review-05: Using a bare glob avoids the stderr error message.
- code-review-05: In plain `sh`/dash an unmatched glob does not match, so the literal-glob issue does not arise there.
- code-review-05: `gzip` can fail on a read-only file or an already-gzipped file.
- code-review-05: The script should print something like `Usage: $0 <backup_dir>` and exit when `$1` is missing.
- code-review-05: The `-f` flag in `rm -rf *.tmp` suppresses errors.
- code-review-05: Suppressing errors with `-f` is fine for the no-match case but also silently masks permission errors.
- code-review-05: The suggested rewrite adds an argument check, quotes all variables, avoids parsing `ls`, guards against the no-match glob case, and uses `set -eu` so failures stop the script.
- code-review-07: When retries are exhausted on 429 or 5xx responses, the for loop ends and the function returns undefined.
- code-review-07: There is no return statement after the retry loop.
- code-review-07: An error that is not a 429 or 5xx causes the function to explicitly return null.
- code-review-07: The function uses two different sentinel values, null and undefined, to signal failure.
- code-review-07: If fn can legitimately return null or undefined, callers cannot distinguish success from failure.
- code-review-07: The backoff delay is computed as 1000 * i.
- code-review-07: On the first failure, i equals 0, so the wait is 0ms.
- code-review-07: Backoff effectively only begins on the second retry.
- code-review-07: The zero first delay appears to be an off-by-one error where i + 1 was likely intended.
- code-review-07: The zero-delay first backoff is not documented and is inconsistent with the rest of the backoff logic.
- code-review-07: On the final loop iteration, a 429 still triggers the setTimeout wait before the loop exits.
- code-review-07: The delay on the final attempt is wasted because there is no subsequent attempt.
- code-review-07: All non-retryable errors are swallowed and converted to a return of null, with no rethrow and no logging.
- code-review-07: Swallowed errors include genuine programming bugs such as TypeError from a null dereference inside fn, ReferenceError, and JSON parse failures.
- code-review-07: Errors without an err.status property have err.status equal to undefined.
- code-review-07: For undefined status, both undefined === 429 and undefined >= 500 evaluate to false.
- code-review-07: Errors without a status fall through to return null in the same way a 404 does.
- code-review-07: Converting all errors to null conflates API rejections with broken code.
- code-review-07: Returning null destroys the error's stack trace and message.
- code-review-07: Unseen callers may already depend on the 'errors become null' behavior.
- code-review-07: Swallowing errors as null is the riskiest issue because it hides programming errors rather than only HTTP failures.
- code-review-07: Errors with err.status >= 500 are retried immediately with no delay.
- code-review-07: 429 errors receive a linear backoff.
- code-review-07: Immediate retries against an unhealthy downstream service hammer that service.
- code-review-07: The backoff has no jitter.
- code-review-07: A fixed 1000 * i backoff causes concurrent callers hitting a 429 to retry in lockstep.
- code-review-07: Retrying in lockstep is the thundering-herd problem that jittered backoff is designed to prevent.
- code-review-07: There is no upper bound check on err.status >= 500.
- code-review-07: Any status of 500 or greater, including nonstandard or custom codes, is treated as retryable.
- code-review-07: There is no err.status < 600 guard, so the condition means '>= 500' rather than '5xx'.
- code-review-07: When attempts <= 0, the function returns undefined without ever calling fn.
- code-review-07: There is no validation or error raised for an attempts value of 0 or less.
- code-review-07: The function contains no logging anywhere.
- code-review-07: Without logging, the function fails silently in production.
- code-review-07: Combined with the null swallow, an outage would be indistinguishable from everything returning null.
- code-review-07: Retry-on-429, retry-on-5xx, and giving up on other errors form a recognizable rate-limit and transient-error retry pattern.
- code-review-07: The retry-on-429 and retry-on-5xx behavior appears intentional.
- code-review-07: The 1000 * i zero-first-delay and the null-versus-undefined failure inconsistency are almost certainly bugs.
- code-review-07: Swallowing all non-status errors as null without logging or rethrow is ambiguous in intent but risky regardless.
- code-review-07: Even as a deliberate 'always resolve, never reject' contract, swallowing errors is indistinguishable from silently eating bugs.
- code-review-08: The script has no logging, dry-run mode, or audit trail.
- code-review-08: `os.listdir()` returns entries in filesystem order, not sorted by mtime.
- code-review-08: The script does not select files oldest-first for the 500 cap.
- code-review-08: Immediate deletion of tmp-/.part files could be deliberate if writer processes rename atomically on completion.
- code-review-08: The script does not own the system that produces the tmp-/.part files.
- code-review-08: No one owns the script's schedule.
- debugging-02: The global object is referred to as `window` or `globalThis`.
- debugging-02: In strict mode or modules, `this` inside a plain function call is `undefined`.
- debugging-02: Accessing `this.seconds` throws if `this` is `undefined` in strict mode.
- debugging-02: The `NaN` value is logged and reassigned on each tick of the interval.
- debugging-02: `.bind(this)` on a regular function callback is an alternative fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-04: Under strict ascii decoding, any byte greater than or equal to 0x80 causes an error.
- debugging-04: UTF-8 is the safe default encoding to use.
- debugging-04: chardet and charset-normalizer are libraries for detecting encoding.
- debugging-04: A file can be opened in binary mode with the "rb" mode string.
- debugging-04: Counting occurrences of b"\n" in binary mode yields a line count.
- debugging-04: Opening the file in binary mode avoids decoding entirely.
- debugging-05: The fixed code is `def make_post(title, tags=None)` with `if tags is None: tags = list(DEFAULT_TAGS)`, then `tags.append("post")`, then `return {"title": title, "tags": tags}`.
- debugging-06: The working directory is empty.
- debugging-06: There is no code to inspect, so the task is pure log analysis.
- debugging-06: A nightly bulk read/write job can collide with analytics traffic that spikes unpredictably.
- debugging-06: Dashboard refreshes and scheduled analytics queries are examples of unpredictable analytics traffic spikes.
- debugging-06: A slow analytics query can be caused by a missing index or a table scan.
- debugging-06: Slow analytics queries starving a co-tenant is the classic 'noisy neighbor' pattern for shared databases.
- debugging-06: Weekly failure frequency could line up with a periodic batch job, a deploy, or a data-volume spike.
- debugging-06: A mismatch between pool size and instance/replica count is a plausible cause.
- debugging-06: If a service scaled up its workers or replicas without raising the database max-connections or pool size, exhaustion becomes a matter of timing rather than a deterministic bug.
- debugging-06: One check is whether analytics query volume, replica count, or a specific slow query spikes around 02:14 UTC on failure nights.
- debugging-06: Some database drivers or ORMs expose pool metrics such as checked-out connections and wait queue length.
- debugging-06: Retention for metrics is often longer than log retention and cheaper to keep.
- debugging-06: Checking database-side logs can reveal what was holding connections at 02:14:07-02:14:41.
- debugging-06: The failure window on the observed night spanned 02:14:07 to 02:14:41.
- debugging-06: A single WARN or ERROR line without pool size, active count, or caller identity is hard to act on.
- debugging-06: If total configured pool size is close to the database's max_connections, a small ephemeral spike such as a deploy restart or an extra worker is enough to exhaust it.
- debugging-06: Correlating with analytics logs and checking database-side logs are the fastest steps to confirm or rule out the shared-database theory.
- explanation-01: Chaining is also known as separate chaining.
- explanation-01: The collection in a chaining slot is usually a linked list, and sometimes a tree or array.
- explanation-01: Linear probing checks index+1, index+2, and so on.
- explanation-01: Quadratic probing jumps by increasing squares.
- explanation-01: Double hashing uses a second hash function to compute the step.
- explanation-01: Chaining has extra memory overhead per entry from list nodes and pointers.
- explanation-01: Chaining has worse cache performance because linked list nodes are scattered in memory.
- explanation-01: Open addressing has better cache performance because probing stays within the array.
- explanation-01: Open addressing can degrade sharply as the array fills up, due to clustering and more probes.
- explanation-01: Deletion in chaining is simple, requiring only removal from the list.
- explanation-01: Deletion in open addressing is trickier and must use tombstones or rehashing.
- explanation-01: In open addressing, removing a slot can break probe chains.
- explanation-01: Resizing pressure is less urgent for chaining.
- explanation-01: Open addressing must keep the load factor well below 1.0.
- explanation-01: Open addressing implementations often resize at around a 70% load factor.
- explanation-01: Chaining is simpler and more forgiving as the map fills up.
- explanation-01: Open addressing is faster and more memory-efficient when the load factor is kept low.
- explanation-01: Open addressing requires careful tuning of load factor thresholds and probing scheme, and more complex deletion logic.
- explanation-01: Java's HashMap is a general-purpose language implementation that picks a collision strategy based on these trade-offs.
- explanation-01: Python's dict uses open addressing internally.
- explanation-01: Go's map uses a bucket-based chaining variant.
- explanation-01: The choice between collision strategies reflects different priorities around memory, speed, and implementation complexity.
- explanation-02: An optimistic locking example uses a `products` table with a `version` integer column.
- explanation-02: An optimistic stock update can be written as `UPDATE products SET stock = stock - 1, version = version + 1 WHERE id = 42 AND version = 7;`.
- explanation-02: Optimistic locking fits when transactions are short and fast.
- explanation-02: Optimistic locking fits when you want high throughput.
- explanation-02: Examples of good fits for optimistic locking include a web app editing user profiles, e-commerce catalog updates, and most CRUD APIs.
- explanation-02: A banking transfer between two accounts is an example of pessimistic locking.
- explanation-02: A pessimistic transfer example uses BEGIN, two `SELECT balance FROM accounts WHERE id = ... FOR UPDATE` statements, balance updates, and COMMIT.
- explanation-02: In some databases, `FOR UPDATE` prevents other transactions from even reading the locked rows.
- explanation-02: Pessimistic locking fits when conflicts are expensive or hard to retry.
- explanation-02: Financial transfers, inventory reservation for a flash sale, and seat booking systems are examples where pessimistic locking fits.
- explanation-02: Pessimistic locking fits when correctness under concurrent write pressure matters more than throughput.
- explanation-02: Pessimistic locking risks contention and deadlocks.
- explanation-02: Pessimistic locking reduces throughput.
- explanation-03: A network path may consist of a single fast link or may cross several routers of varying speed and load.
- explanation-03: If a sender transmitted at whatever rate the receiver's window allowed, it could send more data than routers along the path can forward.
- explanation-03: When packets are dropped, senders retransmit them.
- explanation-03: Persistent overloading of the network causes congestive collapse.
- explanation-03: In congestive collapse, throughput drops sharply even though all senders are trying to send at full speed.
- explanation-03: Slow start is TCP's mechanism for finding a safe sending rate on an unknown path without causing congestive collapse.
- explanation-03: The sender maintains a congestion window (cwnd) in addition to the receiver's advertised window.
- explanation-03: The amount of data in flight is limited by the smaller of the congestion window and the receiver's advertised window.
- explanation-03: Historically, the initial cwnd was 1 segment.
- explanation-03: Modern TCP implementations typically start with an initial cwnd of around 10 segments.
- explanation-03: RFC 6928 specifies the initial window of around 10 segments.
- explanation-03: A full window of data generates a full window of ACKs.
- explanation-03: Slow start continues until a packet loss or ECN mark is detected, or until cwnd reaches the ssthresh threshold.
- explanation-03: A detected packet loss or ECN mark is interpreted as a signal that the network is congested.
- explanation-03: ssthresh is the name of the slow start threshold.
- explanation-03: In congestion avoidance, cwnd growth is linear, roughly +1 segment per RTT.
- explanation-03: The name 'slow start' is a misnomer because it refers to starting from a small window, not to the rate of growth.
- explanation-04: A process is an independent execution unit with its own memory address space, file descriptors, and OS resources.
- explanation-04: Communicating between processes requires IPC such as pipes, sockets, or shared memory segments.
- explanation-04: All threads in a process share the same memory address space, heap, and file descriptors.
- explanation-04: Each thread has its own stack and register state.
- explanation-04: Creating and switching processes is more expensive than creating and switching threads.
- explanation-04: The higher cost of processes comes from separate memory spaces and OS bookkeeping.
- explanation-04: Threads sharing memory directly is fast but requires locks or synchronization to avoid race conditions.
- explanation-04: Processes bypass the GIL because each process has its own interpreter.
- explanation-04: Python and older Ruby are languages with a GIL.
- explanation-04: Multiple processes each get their own interpreter and GIL and can run on separate cores.
- explanation-04: Python's multiprocessing module exists specifically to enable real parallelism for CPU-bound work.
- explanation-04: Using processes for largely independent work avoids race conditions, deadlocks, and lock contention.
- explanation-04: A process-based architecture with workers communicating via queues or sockets generalizes naturally to multiple machines.
- explanation-04: Thread-based designs assume a single shared address space and do not extend across machines.
- explanation-04: Threads are preferable for I/O-bound concurrency where many threads wait on network or disk.
- explanation-04: Threads have low memory overhead and allow fast, frequent communication between concurrent units.
- explanation-04: Spinning up a full process per connection would be wasteful.
- explanation-05: A collection can be kept reachable by being held by a long-lived singleton.
- explanation-05: A listener's closure often captures its whole surrounding scope, including large objects and DOM nodes.
- explanation-05: A captured closure scope keeps all of the captured objects alive indefinitely.
- explanation-05: Static or global variables accumulating data is another frequent cause of memory leaks.
- explanation-05: Mutual references between long-lived and short-lived objects are another frequent cause of memory leaks.
- explanation-05: Mutual references can keep a short-lived object artificially alive.
- explanation-06: The complexity added by a cache includes cache invalidation, staleness, and another system to operate.
- explanation-06: Profiling is cheap.
- explanation-06: Timing middleware and slow query logs are examples of basic profiling.
- explanation-07: A 200GB workload is better addressed with read replicas, better indexing, connection pooling, or vertical scaling than with distributed sharding.
- explanation-07: Sharding addresses write and connection bottlenecks more than it addresses raw disk size.
- explanation-07: A single PostgreSQL instance with fast NVMe storage can comfortably hold multiple terabytes.
- explanation-07: Sharding makes migrations, backups, monitoring, and debugging harder for every feature.
- explanation-07: Vertical scaling has a ceiling set by the largest available instance size and IOPS limits.
- explanation-07: Exceeding vertical scaling limits before sharding infrastructure exists results in downtime or degraded performance.
- explanation-07: PostgreSQL has native table partitioning that can partition by tenant or date.
- explanation-07: Partitions map naturally to shards, so partitioning provides leverage if sharding becomes necessary.
- explanation-08: If JSON parsing is 2% of request time, a binary format that parses 3x faster saves about 1.3% end-to-end.
- explanation-08: Huge payloads or a hot loop are cases where serialization can account for 40% of request time.
- explanation-08: Gains from Protobuf, msgpack, and FlatBuffers vary a lot depending on the payload shape.
- explanation-08: Payload characteristics that affect binary format gains include deep nesting, string-heaviness, numeric-heaviness, and repetitiveness.
- explanation-08: A generic claim that binary is faster can be off by an order of magnitude in either direction for a specific schema.
- explanation-08: The profiling and benchmarking work would take a few hours.
- summarization-01: Cold start time has been reduced by roughly 40%.
- summarization-02: The similarity of the templates makes it easy to copy staging's pool size into production.
- summarization-02: Staging's connection pool size is intentionally small at 5.
- summarization-02: A 10x reduction in connection pool size shipped unnoticed.
- summarization-02: Total impact was approximately 34 minutes.
- summarization-02: Rollback occurred at 09:48.
- summarization-04: PDF export on the Reports page fails silently.
- summarization-04: Clicking the PDF export option initially produces no visible response.
- summarization-04: Clicking the PDF export button several more times produces multiple duplicate 'export failed' error banners.
- summarization-04: The issue was reproduced on the latest version of Firefox.
- summarization-05: Ada is assigned to check with the mobile team's lead about whether the mobile team has been informed of the API deprecation.

Added facts (styled only):

- code-review-01: The function has five problems.
- code-review-01: In the corrected version, an empty `name` raises `ValueError("name must not be empty")`.
- code-review-01: In the corrected version, a `db` of `None` raises `ValueError("db must not be None")`.
- code-review-01: In the corrected version, `roles` is copied with `list(roles)` when truthy and otherwise set to a new empty list.
- code-review-02: Declaring a function `async` without using `await` defeats the purpose of `async`.
- code-review-02: The function does not check that `data.name` exists before `toUpperCase()` is called on it.
- code-review-03: Selecting all columns wastes bandwidth.
- code-review-03: The database driver escapes values passed as query parameters.
- code-review-03: psycopg2 and MySQLdb use `%s` as the parameter placeholder.
- code-review-04: In the fixed version, increment, reset, and get_value each acquire the lock.
- code-review-05: In sh, an unmatched glob stays as the literal string, so *.tmp is passed literally.
- code-review-05: With an unmatched glob, rm tries to remove a file named literally *.tmp and prints an error.
- code-review-05: Using ls adds an extra process.
- code-review-05: If the *.log glob does not match, the loop body runs once with the literal string *.log as $f.
- code-review-05: If the loop runs with the literal string *.log, gzip fails.
- code-review-05: The unquoted echo is a minor issue.
- code-review-05: Without set -u, the script does not warn about unset variables.
- code-review-05: The suggested fixed script uses #!/bin/sh with set -eu, cd "$BACKUP_DIR" || exit 1, rm -f -- *.tmp, a for f in *.log loop with [ -f "$f" ] || continue and gzip "$f", and echo "Cleaned $BACKUP_DIR".
- code-review-05: Memory was checked and contained no relevant notes for this task.
- code-review-07: The speaker will check their memory for relevant context before answering.
- code-review-07: The speaker invokes a bash tool.
- code-review-07: The bash command runs `cat` on the file at /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-wb6o1l2o/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-0lx55all/memory/MEMORY.md
- code-review-07: The bash command redirects stderr to /dev/null.
- code-review-07: The bash command echoes 'NO MEMORY FILE' if the cat command fails.
- code-review-07: The bash command is given the description 'Check memory index'.
- code-review-07: The memory index file is named MEMORY.md.
- code-review-08: `CUTOFF` should be computed inside `clean()`.
- code-review-08: `os.remove`, `os.path.getmtime`, and `os.listdir` can all raise errors.
- code-review-08: `CUTOFF` is set to `86400 * 45`.
- code-review-08: `ROOT` is set to the hardcoded path `/var/data/exports`.
- code-review-08: A hardcoded path is common for a single-purpose production script.
- code-review-08: It is worth confirming that `ROOT` is not meant to come from an environment variable or config file across different deployments.
- code-review-08: The recommendation is to add an age check to the `tmp-`/`.part` branch.
- code-review-08: The recommendation is to wrap each `os.remove` in a `try`/`except` and log successes and failures.
- code-review-08: The recommendation is to move `time.time()` inside `clean()`.
- debugging-01: The config dictionary is {"host": "localhost", "port": 8080}.
- debugging-01: The corrected code calls print(get_url(config)).
- debugging-05: The test calls tags.append("post").
- debugging-05: With the fix, no call can change state that other calls depend on.
- debugging-06: The error is not caused by a code bug.
- debugging-06: Worker-3 waited 30 seconds for a free database connection.
- debugging-06: Worker-3 failed twice and then gave up.
- debugging-06: The export job and the analytics service share a fixed pool of database connections.
- explanation-01: Separate chaining is recommended when many collisions are expected.
- explanation-01: Separate chaining is recommended when the number of entries is unknown.
- explanation-01: Open addressing is recommended when predictable performance is needed.
- explanation-02: Most web applications have many reads and few writes to the same row.
- explanation-03: When a packet drop happens, TCP lowers the congestion window.
- explanation-04: A process can contain one thread or many threads.
- explanation-04: Parts of a system with different resource needs should be run as separate processes.
- explanation-05: A memory leak can eventually cause the program to run out of memory.
- explanation-05: A memory leak can eventually cause the program to become slow.
- explanation-07: The sharding decision depends on write throughput, table growth rate, query latency, read scaling, and data model.
- explanation-07: Current CPU and I/O use during peak load should be checked.
- explanation-07: A table that grows past 1-2 TB becomes hard to manage on one instance.
- explanation-07: A table that grows past a few hundred million rows becomes hard to manage on one instance.
- explanation-07: Index scans, vacuum, or backups already taking too long is an early warning sign.
- explanation-07: If growth continues without sharding, write latency increases as tables grow and indexes get large.
- explanation-07: Vacuum and backup jobs take longer as data grows and can start to affect the production instance.
- explanation-07: A single instance remains a single point of failure, and if it fails the whole product goes down.
- explanation-07: Without sharding, at some point migration must happen under time pressure rather than on your own schedule.
- explanation-07: Sharding does not fix a bad schema or bad queries.
- explanation-07: Sharding can hide schema and query problems and make them harder to correct.
- explanation-07: Monitoring should be set up for write throughput, table size, and query latency.
- explanation-07: A clear trigger point should be defined, such as a table exceeding a set size or write latency exceeding a set threshold.
- explanation-07: A rough growth estimate range helps set the trigger point.
- explanation-08: Two key facts are currently unknown: the payload sizes and serialization's share of request time.
- explanation-08: A binary format helps most when payloads are large.
- explanation-08: For small payloads, the gain from a binary format is small.
- explanation-08: Network time, database time, and business logic often dominate request time.
- explanation-08: Switching to a binary format carries costs including schema management, client updates, and the loss of human-readable payloads for debugging.
- summarization-02: The staging and production templates should be stored in separate directories with distinct names.
- summarization-02: The outage started at 09:14 UTC.
- summarization-02: The page went out at 09:21 UTC.
- summarization-02: The gap between the outage start and the page was 7 minutes.
- summarization-04: Four identical "export failed" error banners appear.
- summarization-04: A colleague can reproduce the bug on a different machine.
- summarization-07: The median latency and memory results are confirmed.
- summarization-07: The measured numbers are probably too optimistic.

## Hedging survival

The judge lists the claims that the unstyled answer presents with uncertainty, then judges each claim in the styled answer: hedged (the uncertainty survives in some form), certain (the claim survives but reads as a fact — the failure this check targets), or absent (the claim is gone, a completeness loss). Survival is hedged / (hedged + certain). The claims that became certain appear verbatim below the table.

### actionable-clarity

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 1 | 0 | 0 | 1.0 |
| code-review-02 | 2 | 1 | 1 | 0 | 0.5 |
| code-review-03 | 3 | 0 | 2 | 1 | 0.0 |
| code-review-04 | 3 | 0 | 3 | 0 | 0.0 |
| code-review-05 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-06 | 7 | 6 | 1 | 0 | 0.857 |
| code-review-07 | 9 | 7 | 0 | 2 | 1.0 |
| code-review-08 | 7 | 6 | 0 | 1 | 1.0 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-05 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-06 | 12 | 4 | 0 | 8 | 1.0 |
| debugging-07 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 0 | 0 | 0 | 0 | n/a |
| explanation-01 | 3 | 0 | 3 | 0 | 0.0 |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 6 | 3 | 2 | 1 | 0.6 |
| explanation-04 | 2 | 2 | 0 | 0 | 1.0 |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 4 | 2 | 2 | 0 | 0.5 |
| explanation-07 | 0 | 0 | 0 | 0 | n/a |
| explanation-08 | 1 | 0 | 0 | 1 | n/a |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 1 | 0 | 1 | 0 | 0.0 |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 5 | 5 | 0 | 0 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 75 over 32 judged pairs: 45 hedged, 16 certain, 14 absent.

Median survival: 1.0 over 19 scored pairs.

Claims that became certain:

- code-review-02: A 404/500 response would still resolve and get parsed as JSON, potentially producing bad data or a parse error.
- code-review-03: Stacked queries may make the SQL injection even worse, depending on the driver.
- code-review-03: Using `SELECT *` can silently break the code if column order changes.
- code-review-04: Thread B could also read 0 before thread A writes, in the read-modify-write sequence in increment()
- code-review-04: 100,000 increments from 10 threads will often produce something less than 100,000
- code-review-04: A thread calling reset() and another mid-way through increment() can interleave so that the increment's write clobbers the reset, leaving value at 1 instead of 0, or vice versa depending on timing
- code-review-05: In plain sh/dash, a bare `*.log` glob with no matches just doesn't match, so guarding against the literal `*.log` isn't an issue there — but the actual shell's behavior is worth checking.
- code-review-06: The recursive branch should almost certainly check isinstance(value, dict) as well, not just isinstance(merged[key], dict).
- explanation-01: Each array slot in chaining usually holds a linked list, and sometimes a tree/array, instead of a single value.
- explanation-01: Open addressing can degrade sharply as the array fills up, due to clustering and more probes.
- explanation-01: Open addressing must keep the load factor well below 1.0, often resizing at around 70%.
- explanation-03: In congestion avoidance, growth becomes linear at roughly +1 segment per RTT.
- explanation-03: The name "slow start" is a bit of a misnomer, since it's "slow" only in that it starts from a small window, not in how fast it grows.
- explanation-06: I'd recommend profiling the API before building anything, to find out where time is actually going.
- explanation-06: I'd suggest we hold off on committing to 'add a cache' and spend a short cycle profiling first.
- summarization-02: Connection pool sizes are likely not the only capacity-related settings missing from the config review checklist — other capacity-related settings are probably also uncovered.

### clarity-flow

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 1 | 0 | 0 | 1.0 |
| code-review-02 | 2 | 1 | 0 | 1 | 1.0 |
| code-review-03 | 3 | 0 | 1 | 2 | 0.0 |
| code-review-04 | 3 | 0 | 2 | 1 | 0.0 |
| code-review-05 | 1 | 0 | 0 | 1 | n/a |
| code-review-06 | 7 | 4 | 3 | 0 | 0.571 |
| code-review-07 | 9 | 6 | 1 | 2 | 0.857 |
| code-review-08 | 7 | 5 | 1 | 1 | 0.833 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-05 | 1 | 0 | 1 | 0 | 0.0 |
| debugging-06 | 12 | 6 | 0 | 6 | 1.0 |
| debugging-07 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 0 | 0 | 0 | 0 | n/a |
| explanation-01 | 3 | 1 | 2 | 0 | 0.333 |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 6 | 2 | 1 | 3 | 0.667 |
| explanation-04 | 2 | 0 | 0 | 2 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 4 | 2 | 2 | 0 | 0.5 |
| explanation-07 | 0 | 0 | 0 | 0 | n/a |
| explanation-08 | 1 | 0 | 0 | 1 | n/a |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 1 | 0 | 0 | 1 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 5 | 4 | 0 | 1 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 75 over 32 judged pairs: 39 hedged, 14 certain, 22 absent.

Median survival: 0.845 over 16 scored pairs.

Claims that became certain:

- code-review-03: Using `SELECT *` can silently break the code if column order changes.
- code-review-04: Thread B could also read 0 before thread A writes, in the read-modify-write sequence in increment()
- code-review-04: A thread calling reset() and another mid-way through increment() can interleave so that the increment's write clobbers the reset, leaving value at 1 instead of 0, or vice versa depending on timing
- code-review-06: The issues identified in merge_settings are likely bugs.
- code-review-06: The recursive branch should almost certainly check isinstance(value, dict) as well, not just isinstance(merged[key], dict).
- code-review-06: The missing isinstance(value, dict) check before recursing looks like an oversight; there's no plausible reason to want a crash there instead of overwriting or raising a clear error.
- code-review-07: Retrying 5xx immediately with no delay is arguably worse than doing nothing when a downstream service is unhealthy.
- code-review-08: The tmp/.part immediate-delete behavior is a plausible data-loss path.
- debugging-05: By the time this test runs, DEFAULT_TAGS may already be ["draft", "post"] or ["draft", "post", "post"], so the assertion == ["draft", "post"] fails
- explanation-01: Each array slot in chaining usually holds a linked list, and sometimes a tree/array, instead of a single value.
- explanation-01: Open addressing can degrade sharply as the array fills up, due to clustering and more probes.
- explanation-03: The name "slow start" is a bit of a misnomer, since it's "slow" only in that it starts from a small window, not in how fast it grows.
- explanation-06: I'd recommend profiling the API before building anything, to find out where time is actually going.
- explanation-06: I'd suggest we hold off on committing to 'add a cache' and spend a short cycle profiling first.

### classic-concise

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-02 | 2 | 1 | 1 | 0 | 0.5 |
| code-review-03 | 3 | 1 | 1 | 1 | 0.5 |
| code-review-04 | 3 | 0 | 2 | 1 | 0.0 |
| code-review-05 | 1 | 0 | 0 | 1 | n/a |
| code-review-06 | 7 | 5 | 0 | 2 | 1.0 |
| code-review-07 | 9 | 6 | 0 | 3 | 1.0 |
| code-review-08 | 7 | 6 | 0 | 1 | 1.0 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-05 | 1 | 0 | 1 | 0 | 0.0 |
| debugging-06 | 12 | 7 | 0 | 5 | 1.0 |
| debugging-07 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 0 | 0 | 0 | 0 | n/a |
| explanation-01 | 3 | 0 | 2 | 1 | 0.0 |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 6 | 3 | 1 | 2 | 0.75 |
| explanation-04 | 2 | 2 | 0 | 0 | 1.0 |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 4 | 2 | 2 | 0 | 0.5 |
| explanation-07 | 0 | 0 | 0 | 0 | n/a |
| explanation-08 | 1 | 0 | 0 | 1 | n/a |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 1 | 0 | 0 | 1 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 5 | 4 | 0 | 1 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 75 over 32 judged pairs: 44 hedged, 11 certain, 20 absent.

Median survival: 1.0 over 17 scored pairs.

Claims that became certain:

- code-review-01: The caller may not expect their list to change just from calling `add_user`.
- code-review-02: The function being declared `async` but never using `await` is a strong signal that the promise chain was meant to be awaited but isn't.
- code-review-03: Using `SELECT *` can silently break the code if column order changes.
- code-review-04: Thread B could also read 0 before thread A writes, in the read-modify-write sequence in increment()
- code-review-04: A thread calling reset() and another mid-way through increment() can interleave so that the increment's write clobbers the reset, leaving value at 1 instead of 0, or vice versa depending on timing
- debugging-05: By the time this test runs, DEFAULT_TAGS may already be ["draft", "post"] or ["draft", "post", "post"], so the assertion == ["draft", "post"] fails
- explanation-01: Each array slot in chaining usually holds a linked list, and sometimes a tree/array, instead of a single value.
- explanation-01: Open addressing can degrade sharply as the array fills up, due to clustering and more probes.
- explanation-03: Since a full window of data generates a full window of ACKs, cwnd roughly doubles every round-trip time.
- explanation-06: I'd recommend profiling the API before building anything, to find out where time is actually going.
- explanation-06: I'd suggest we hold off on committing to 'add a cache' and spend a short cycle profiling first.

### developer-docs

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 1 | 0 | 0 | 1.0 |
| code-review-02 | 2 | 0 | 2 | 0 | 0.0 |
| code-review-03 | 3 | 0 | 2 | 1 | 0.0 |
| code-review-04 | 3 | 2 | 0 | 1 | 1.0 |
| code-review-05 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-06 | 7 | 6 | 1 | 0 | 0.857 |
| code-review-07 | 9 | 7 | 0 | 2 | 1.0 |
| code-review-08 | 7 | 5 | 2 | 0 | 0.714 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-05 | 1 | 0 | 1 | 0 | 0.0 |
| debugging-06 | 12 | 6 | 1 | 5 | 0.857 |
| debugging-07 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 0 | 0 | 0 | 0 | n/a |
| explanation-01 | 3 | 0 | 3 | 0 | 0.0 |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 6 | 4 | 1 | 1 | 0.8 |
| explanation-04 | 2 | 2 | 0 | 0 | 1.0 |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 4 | 2 | 2 | 0 | 0.5 |
| explanation-07 | 0 | 0 | 0 | 0 | n/a |
| explanation-08 | 1 | 0 | 0 | 1 | n/a |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 1 | 0 | 0 | 1 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 5 | 4 | 0 | 1 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 75 over 32 judged pairs: 46 hedged, 16 certain, 13 absent.

Median survival: 0.857 over 18 scored pairs.

Claims that became certain:

- code-review-02: The function being declared `async` but never using `await` is a strong signal that the promise chain was meant to be awaited but isn't.
- code-review-02: A 404/500 response would still resolve and get parsed as JSON, potentially producing bad data or a parse error.
- code-review-03: Stacked queries may make the SQL injection even worse, depending on the driver.
- code-review-03: Using `SELECT *` can silently break the code if column order changes.
- code-review-05: In plain sh/dash, a bare `*.log` glob with no matches just doesn't match, so guarding against the literal `*.log` isn't an issue there — but the actual shell's behavior is worth checking.
- code-review-06: The recursive branch should almost certainly check isinstance(value, dict) as well, not just isinstance(merged[key], dict).
- code-review-08: The bugs listed are likely unintentional.
- code-review-08: A TOCTOU race between listdir() and the file operation is plausible here, since this same script may be deleting concurrently-written files.
- debugging-05: By the time this test runs, DEFAULT_TAGS may already be ["draft", "post"] or ["draft", "post", "post"], so the assertion == ["draft", "post"] fails
- debugging-06: The export job and the analytics service possibly share one pool config (they are assumed to share one DB).
- explanation-01: Each array slot in chaining usually holds a linked list, and sometimes a tree/array, instead of a single value.
- explanation-01: Open addressing can degrade sharply as the array fills up, due to clustering and more probes.
- explanation-01: Open addressing must keep the load factor well below 1.0, often resizing at around 70%.
- explanation-03: The name "slow start" is a bit of a misnomer, since it's "slow" only in that it starts from a small window, not in how fast it grows.
- explanation-06: I'd recommend profiling the API before building anything, to find out where time is actually going.
- explanation-06: I'd suggest we hold off on committing to 'add a cache' and spend a short cycle profiling first.

### plain-language

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 0 | 0 | 1 | n/a |
| code-review-02 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-03 | 3 | 0 | 1 | 2 | 0.0 |
| code-review-04 | 3 | 0 | 3 | 0 | 0.0 |
| code-review-05 | 1 | 0 | 0 | 1 | n/a |
| code-review-06 | 7 | 0 | 0 | 7 | n/a |
| code-review-07 | 9 | 0 | 0 | 9 | n/a |
| code-review-08 | 7 | 6 | 1 | 0 | 0.857 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-05 | 1 | 0 | 1 | 0 | 0.0 |
| debugging-06 | 12 | 7 | 1 | 4 | 0.875 |
| debugging-07 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 0 | 0 | 0 | 0 | n/a |
| explanation-01 | 3 | 0 | 2 | 1 | 0.0 |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 6 | 3 | 0 | 3 | 1.0 |
| explanation-04 | 2 | 0 | 0 | 2 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 4 | 2 | 2 | 0 | 0.5 |
| explanation-07 | 0 | 0 | 0 | 0 | n/a |
| explanation-08 | 1 | 0 | 0 | 1 | n/a |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 1 | 0 | 0 | 1 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 5 | 4 | 0 | 1 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 75 over 32 judged pairs: 29 hedged, 12 certain, 34 absent.

Median survival: 0.857 over 13 scored pairs.

Claims that became certain:

- code-review-02: A 404/500 response would still resolve and get parsed as JSON, potentially producing bad data or a parse error.
- code-review-03: Using `SELECT *` can silently break the code if column order changes.
- code-review-04: Thread B could also read 0 before thread A writes, in the read-modify-write sequence in increment()
- code-review-04: 100,000 increments from 10 threads will often produce something less than 100,000
- code-review-04: A thread calling reset() and another mid-way through increment() can interleave so that the increment's write clobbers the reset, leaving value at 1 instead of 0, or vice versa depending on timing
- code-review-08: Deleting an arbitrary 500 files rather than the oldest ones is not what the variable name CUTOFF might imply.
- debugging-05: By the time this test runs, DEFAULT_TAGS may already be ["draft", "post"] or ["draft", "post", "post"], so the assertion == ["draft", "post"] fails
- debugging-06: The export job and the analytics service possibly share one pool config (they are assumed to share one DB).
- explanation-01: Each array slot in chaining usually holds a linked list, and sometimes a tree/array, instead of a single value.
- explanation-01: Open addressing can degrade sharply as the array fills up, due to clustering and more probes.
- explanation-06: I'd recommend profiling the API before building anything, to find out where time is actually going.
- explanation-06: I'd suggest we hold off on committing to 'add a cache' and spend a short cycle profiling first.

### technical-simplified

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 0 | 0 | 1 | n/a |
| code-review-02 | 2 | 0 | 2 | 0 | 0.0 |
| code-review-03 | 3 | 0 | 1 | 2 | 0.0 |
| code-review-04 | 3 | 2 | 0 | 1 | 1.0 |
| code-review-05 | 1 | 0 | 0 | 1 | n/a |
| code-review-07 | 9 | 0 | 0 | 9 | n/a |
| code-review-08 | 7 | 3 | 2 | 2 | 0.6 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-05 | 1 | 0 | 1 | 0 | 0.0 |
| debugging-06 | 12 | 6 | 2 | 4 | 0.75 |
| explanation-01 | 3 | 0 | 2 | 1 | 0.0 |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 6 | 0 | 2 | 4 | 0.0 |
| explanation-04 | 2 | 2 | 0 | 0 | 1.0 |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 4 | 2 | 2 | 0 | 0.5 |
| explanation-07 | 0 | 0 | 0 | 0 | n/a |
| explanation-08 | 1 | 0 | 0 | 1 | n/a |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 1 | 0 | 0 | 1 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 60 over 27 judged pairs: 19 hedged, 14 certain, 27 absent.

Median survival: 0.55 over 12 scored pairs.

Claims that became certain:

- code-review-02: The function being declared `async` but never using `await` is a strong signal that the promise chain was meant to be awaited but isn't.
- code-review-02: A 404/500 response would still resolve and get parsed as JSON, potentially producing bad data or a parse error.
- code-review-03: Using `SELECT *` can silently break the code if column order changes.
- code-review-08: A TOCTOU race between listdir() and the file operation is plausible here, since this same script may be deleting concurrently-written files.
- code-review-08: The tmp/.part immediate-delete behavior is a plausible data-loss path.
- debugging-05: By the time this test runs, DEFAULT_TAGS may already be ["draft", "post"] or ["draft", "post", "post"], so the assertion == ["draft", "post"] fails
- debugging-06: Pool-level metrics may be obtainable from both services, if the DB driver/ORM exposes them.
- debugging-06: Steps #1 and #3 will probably confirm or rule out the shared-DB theory fastest, so they are the suggested starting point.
- explanation-01: Each array slot in chaining usually holds a linked list, and sometimes a tree/array, instead of a single value.
- explanation-01: Open addressing can degrade sharply as the array fills up, due to clustering and more probes.
- explanation-03: If the sender just started blasting data at whatever rate the receiver's window allowed, it could easily dump far more data onto the network than any router along the way can forward.
- explanation-03: Since a full window of data generates a full window of ACKs, cwnd roughly doubles every round-trip time.
- explanation-06: I'd recommend profiling the API before building anything, to find out where time is actually going.
- explanation-06: I'd suggest we hold off on committing to 'add a cache' and spend a short cycle profiling first.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 122, measured: 122.
Mean duration: 17774 ms. Mean wall: 29272 ms. Mean startup: 11497 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 122, measured: 122.
Input tokens: 244 uncached, 255507 cache write, 246603 cache read. Output tokens: 143924.
Cache-read share: 0.491.
Cache writes by lifetime: 255507 at 5 minutes, 0 at 1 hour.

## Reuse

Reused rows: 618, imported from 2026-08-10.
Live calls of this run: 122.

The freshness sample re-ran 6 imported verdicts live; 3 agree.
- completeness:check:0185e8fea7f573a40f1e3a30f5f493877f24d73a7a2cd06604870b51832d3fc4: the verdicts differ.
- completeness:reverse:00d4cb26b33d5d4cb5be69c75e58a5ba6f453cc2ff9fc637a375c3e388d8542a: the verdicts differ.
- completeness:reverse:0185e8fea7f573a40f1e3a30f5f493877f24d73a7a2cd06604870b51832d3fc4: the verdicts differ.

A verdict axis compares on exact equality, and one differing
verdict is a warning. The clarity picks carry an aggregate
tolerance instead: the sample warns only when its disagreement
count clears a one-sided binomial tail of 0.05 at the
0.4 cross-judge disagreement rate of the
runs/2026-08-08 second-judge sample. Two judges disagree
with each other at least as often as one judge disagrees with
itself later, so the cross-judge rate bounds the reuse noise
from above.

## Warnings

- technical-simplified/code-review-06: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/summarization-08: the pair failed the gate, excluded
- technical-simplified/debugging-07: the pair failed the gate, excluded
- technical-simplified/debugging-08: the pair failed the gate, excluded
- reuse freshness: completeness:check:0185e8fea7f573a40f1e3a30f5f493877f24d73a7a2cd06604870b51832d3fc4: the live verdict differs from the reused one
- reuse freshness: completeness:reverse:00d4cb26b33d5d4cb5be69c75e58a5ba6f453cc2ff9fc637a375c3e388d8542a: the live verdict differs from the reused one
- reuse freshness: completeness:reverse:0185e8fea7f573a40f1e3a30f5f493877f24d73a7a2cd06604870b51832d3fc4: the live verdict differs from the reused one
