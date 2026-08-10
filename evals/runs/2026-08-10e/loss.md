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

Judge: opus. Judged on 2026-08-10T13:44:47+00:00.

## Completeness (fact survival)

The judge lists the facts of the unstyled answer, then checks each fact against the styled answer. The fraction is the share of the facts that survive. The judge also lists the facts of the styled answer and checks each fact against the unstyled answer: a styled fact that the unstyled answer does not state is an addition. The lost facts and the added facts appear verbatim below the table.

### actionable-clarity

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 29 | 21 | 0.724 | 26 | 9 |
| code-review-02 | 20 | 15 | 0.75 | 21 | 2 |
| code-review-03 | 26 | 17 | 0.654 | 26 | 7 |
| code-review-04 | 19 | 12 | 0.632 | 22 | 4 |
| code-review-05 | 33 | 23 | 0.697 | 29 | 8 |
| code-review-06 | 25 | 20 | 0.8 | 40 | 6 |
| code-review-07 | 32 | 22 | 0.688 | 43 | 13 |
| code-review-08 | 35 | 25 | 0.714 | 43 | 6 |
| debugging-01 | 6 | 6 | 1.0 | 8 | 1 |
| debugging-02 | 17 | 10 | 0.588 | 17 | 2 |
| debugging-03 | 10 | 10 | 1.0 | 12 | 2 |
| debugging-04 | 12 | 9 | 0.75 | 14 | 3 |
| debugging-05 | 15 | 14 | 0.933 | 15 | 0 |
| debugging-06 | 3 | 0 | 0.0 | 25 | 25 |
| debugging-07 | 6 | 0 | 0.0 | 30 | 30 |
| debugging-08 | 30 | 17 | 0.567 | 63 | 34 |
| explanation-01 | 44 | 37 | 0.841 | 29 | 1 |
| explanation-02 | 29 | 27 | 0.931 | 28 | 1 |
| explanation-03 | 34 | 22 | 0.647 | 23 | 2 |
| explanation-04 | 30 | 25 | 0.833 | 35 | 6 |
| explanation-05 | 20 | 18 | 0.9 | 21 | 4 |
| explanation-06 | 17 | 11 | 0.647 | 19 | 5 |
| explanation-07 | 24 | 12 | 0.5 | 22 | 4 |
| summarization-01 | 6 | 5 | 0.833 | 7 | 1 |
| summarization-02 | 12 | 10 | 0.833 | 23 | 5 |
| summarization-03 | 13 | 13 | 1.0 | 15 | 2 |
| summarization-04 | 14 | 13 | 0.929 | 12 | 0 |
| summarization-05 | 10 | 9 | 0.9 | 11 | 0 |
| summarization-06 | 14 | 14 | 1.0 | 13 | 0 |
| summarization-07 | 15 | 14 | 0.933 | 17 | 3 |
| summarization-08 | 17 | 16 | 0.941 | 19 | 3 |

Median fraction: 0.8 over 31 scored pairs.

Median additions: 3 over 31 scored pairs.

Lost facts:

- code-review-01: The function does not check that `roles` contains valid role values.
- code-review-01: The function has no duplicate-role protection.
- code-review-01: The function appends `"member"` even if `"member"` is already present in `roles`.
- code-review-01: Failure modes conflated by the boolean return include bad input, DB down, and duplicate entry.
- code-review-01: The suggested fix raises `ValueError("db is required")` when `db` is `None`.
- code-review-01: The suggested fix defaults `roles` to `None` and copies it with `list(roles)`.
- code-review-01: The suggested fix appends `"member"` only if it is not already in `roles`.
- code-review-01: The suggested fix catches `Exception` instead of using a bare `except:`.
- code-review-02: An `async` function returns a promise wrapping its return value.
- code-review-02: A throw inside an async function body produces a rejected promise rather than an exception thrown at the call site.
- code-review-02: `fetch` only rejects on network failure, not on 4xx or 5xx responses.
- code-review-02: Assigning to an outer `let` variable inside `.then()` instead of chaining or returning is an anti-pattern.
- code-review-02: The outer-variable assignment pattern obscures the fact that the value is not ready when it is used.
- code-review-03: The function does not check that `customer_name` is non-empty or of reasonable length.
- code-review-03: The function has no error handling.
- code-review-03: A failed query, such as from a bad connection or lock timeout, will raise an uncaught exception.
- code-review-03: The function has no type hints.
- code-review-03: The function has no docstring.
- code-review-03: The `cursor` parameter and the return type are not documented.
- code-review-03: The lack of type hints and docstring makes the function's contract unclear to callers.
- code-review-03: The query has no `LIMIT` clause.
- code-review-03: Without a `LIMIT`, a broad match could return a huge number of rows.
- code-review-04: CPython has a Global Interpreter Lock (GIL).
- code-review-04: CPython's GIL prevents literal byte-level memory corruption.
- code-review-04: CPython's GIL does not make `current = self.value; self.value = current + 1` atomic as a whole.
- code-review-04: The sequence `current = self.value; self.value = current + 1` compiles to multiple bytecode operations.
- code-review-04: A thread switch can happen between the bytecode operations of a read-modify-write.
- code-review-04: External code reading `counter.value` while another thread is mid-increment can observe inconsistent or stale state.
- code-review-04: Exposing `value` as a property that acquires the lock before returning `_value` provides a safe read.
- code-review-05: In the script, `BACKUP_DIR=$1` is unquoted and has no validation.
- code-review-05: `cd $BACKUP_DIR` is the most dangerous line in the script.
- code-review-05: If no `.tmp` files exist and globbing is not nullglob-safe, `*.tmp` is passed literally to `rm -rf`, which errors out.
- code-review-05: `rm -rf *.tmp` is a broad, silent recursive delete with no confirmation.
- code-review-05: If no `.log` files exist, `*.log` is passed literally as a nonexistent filename to `gzip`, causing an error.
- code-review-05: The script relies on nothing POSIX-incompatible.
- code-review-05: The `ls *.log` parsing bug exists independently of which shell is used.
- code-review-05: The suggested rewrite exits with status 1 and prints a usage message to stderr if `$BACKUP_DIR` is empty or not a directory.
- code-review-05: The suggested rewrite uses `rm -f -- *.tmp 2>/dev/null || true`.
- code-review-05: There should not be directories matching `*.tmp` to recurse into, and if there are, that needs explicit intent.
- code-review-06: `isinstance(merged[key], dict)` returns False for custom `Mapping` types that are not literally `dict`.
- code-review-06: Dict-like objects that are not `dict` instances fall back to full replacement instead of being merged.
- code-review-06: Using `None` to mean deletion is a common pattern in config merge/patch semantics, as in Kubernetes strategic merge and Helm.
- code-review-06: The function has no docstring and no type hints.
- code-review-06: The `None`-deletes-key behavior is undiscoverable without reading the source.
- code-review-07: The backoff formula does not match the exponential-backoff-from-first-retry pattern it appears to imitate.
- code-review-07: On the last loop iteration, a 429 still triggers the setTimeout wait before the loop exits.
- code-review-07: The wait on the final attempt is a pointless delay because the function returns undefined anyway.
- code-review-07: An uncaught TypeError breaks the implied contract that the function never throws.
- code-review-07: A suppressed error could silently produce a fail-open state if a caller uses the result for a permission or entitlement check.
- code-review-07: Network failures are the most common reason to want retry logic.
- code-review-07: The backoff has no cap or ceiling.
- code-review-07: The code does not respect a Retry-After header on 429 responses.
- code-review-07: 501 Not Implemented is a permanent condition, so retrying it is pure waste, unlike 502, 503, and 504.
- code-review-07: The silent swallowing of errors changes the function's error-handling contract invisibly to callers and could mask bugs and security-relevant failures.
- code-review-08: `os.path.getmtime` works on directories.
- code-review-08: The `removed` count is lost on failure because it is never returned.
- code-review-08: The age-based deletion and the tmp/`.part` deletion are two unrelated criteria sharing one counter.
- code-review-08: In that case the age-based cleanup silently stops early for that run with no logging to explain why.
- code-review-08: The interaction between the two deletion branches is non-deterministic across runs.
- code-review-08: `clean()` is never called in the snippet.
- code-review-08: As given, the script does nothing when executed directly, unless the snippet is truncated.
- code-review-08: The `tmp-` prefix and `.part` suffix are conventional naming for atomic writes (write to a temp name, then rename into place).
- code-review-08: The age-based branch was designed with safety in mind, as evidenced by the 500 cap.
- code-review-08: The 500 cap limits blast radius if the `CUTOFF` logic broke and flagged everything as stale.
- debugging-02: Accessing `this.seconds` when `this` is `undefined` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: In non-strict mode, `this` in a plain function call falls back to the global object.
- debugging-02: In non-strict mode, `this.seconds` would evaluate to `undefined`.
- debugging-02: The user's environment is treating the callback as non-strict, for example because it is transpiled or run outside a strict context.
- debugging-02: Using an arrow function as the `setInterval` callback is the easiest fix.
- debugging-02: Calling `.bind(this)` on a regular function callback is an alternative fix that keeps a regular function.
- debugging-02: Capturing `this` in a variable beforehand, such as `const self = this;`, is another alternative fix.
- debugging-04: If the encoding is not reliably UTF-8, one option is to detect it.
- debugging-04: chardet and charset-normalizer are libraries that can detect a file's encoding.
- debugging-04: errors="replace" preserves line structure.
- debugging-05: An alternative fix is to use tags=() and convert it to a list inside the function.
- debugging-06: The speaker intends to check whether actual project code is present in the working directory.
- debugging-06: Project code, if present, might reveal the connection pool configuration.
- debugging-06: The speaker will look for relevant code in the working directory before giving an answer.
- debugging-07: Checking whether the actual test code exists in the current directory would enable more concrete advice.
- debugging-07: A Bash tool call is issued with the command "find . -iname '*notification*' -o -iname 'conftest.py' 2>/dev/null | head -50".
- debugging-07: The Bash tool call's description is "Search for relevant test files".
- debugging-07: The command searches the current directory for files whose names match '*notification*' or are named 'conftest.py'.
- debugging-07: The command limits its output to the first 50 results via head -50.
- debugging-07: The command discards error output by redirecting stderr to /dev/null.
- debugging-08: If the growth rate versus request rate is roughly linear, the leak is traffic-correlated.
- debugging-08: Metrics libraries such as Prometheus clients and StatsD wrappers create a new time series per unique label value.
- debugging-08: Each metrics time series is retained forever in-process.
- debugging-08: Webhooks and marketing campaigns often carry unique or high-cardinality identifiers.
- debugging-08: If metrics registry size climbs monotonically and correlates with traffic, high-cardinality metrics labels are the culprit.
- debugging-08: A custom LRU eviction policy can have bugs that prevent eviction under certain access patterns.
- debugging-08: Bounding a wrapper map does not bound memory if its values reference large objects containing additional maps.
- debugging-08: A second unbounded cache or index, such as a reverse-lookup index, may be built alongside the bounded cache.
- debugging-08: If cache entry count grows past the configured bound, the eviction logic is broken.
- debugging-08: A native library for compression, TLS, or image processing may fail to return memory to the OS.
- debugging-08: If RSS does not drop after forcing a full GC, the memory is not GC-reachable garbage.
- debugging-08: Plotting growth rate against request or webhook volume is cheap and requires no code changes.
- debugging-08: A heap diff is the missing diagnostic and will immediately disambiguate the traffic-volume leak from the high-cardinality metrics cause.
- explanation-01: A hash map's array has a fixed number of buckets.
- explanation-01: There is no limit to the number of possible keys a hash map may receive.
- explanation-01: The collection in a chaining bucket is usually a linked list, and sometimes a tree or dynamic array.
- explanation-01: Quadratic probing and double hashing are other probing variants.
- explanation-01: Some high-performance hash maps use open addressing variants for speed.
- explanation-01: Python's dict uses an open addressing variant.
- explanation-01: Rust's HashMap uses an open addressing variant.
- explanation-02: FOR UPDATE blocks any other transaction from reading or modifying that row until the locking transaction commits.
- explanation-02: Optimistic locking fits cases with long think time between read and write, such as a user editing a form for minutes.
- explanation-03: TCP slow start also runs when a connection restarts after a pause.
- explanation-03: A network path may cross a fast local network and then a slow, congested link in the middle.
- explanation-03: When a router's buffer fills up, it starts dropping packets.
- explanation-03: Dropped packets cause retransmissions, wasted bandwidth, and cascading congestion.
- explanation-03: Congestion from one connection can degrade the network for everyone sharing that link.
- explanation-03: The receive window reflects the receiver's buffer capacity.
- explanation-03: TCP respects whichever of the congestion window and receive window is smaller.
- explanation-03: RFC 6928 specifies an initial window of 10 segments.
- explanation-03: ACKs only arrive if data is getting through successfully, so cwnd growth stalls when the network cannot keep up.
- explanation-03: Packet loss is detected via timeout or duplicate ACKs.
- explanation-03: ssthresh is often set from a previous congestion event.
- explanation-03: When cwnd reaches ssthresh, TCP switches to congestion avoidance as a precaution against repeating the same overshoot.
- explanation-04: Each thread has its own stack and instruction pointer.
- explanation-04: Python's multiprocessing module is used for CPU-bound parallel computation.
- explanation-04: Processes can be sandboxed independently with different users, capabilities, and memory protections.
- explanation-04: Per-process resource limits can be applied via cgroups or ulimits.
- explanation-04: Threads context-switch faster than processes.
- explanation-05: A memory leak in a garbage-collected language does not mean memory is lost as it is in C with unfreed malloc.
- explanation-05: Examples of long-lived collections include a global cache, a static Map, and a subscriber list.
- explanation-06: Slowness could be caused by writes, N+1 queries, network latency, unindexed queries, or application code.
- explanation-06: If the real bottleneck is a slow query such as one from a missing index, caching masks the symptom instead of fixing the cause.
- explanation-06: If the real bottleneck is slow network calls, caching masks the symptom instead of fixing the cause.
- explanation-06: The read/write ratio can be determined by checking logs or adding simple counters.
- explanation-06: Common database issues to check first include missing indexes, N+1 queries, and slow joins.
- explanation-06: Redis is an example of a cache that can be placed in front of a database.
- explanation-07: Machines with multiple terabytes of RAM/NVMe are routine.
- explanation-07: If the real problem is unindexed queries or lock contention, sharding will not help.
- explanation-07: Growth rate can be estimated by measuring growth over the last 3-6 months and extrapolating.
- explanation-07: Single-instance PostgreSQL limits are roughly multiple terabytes of data and tens of thousands of writes per second.
- explanation-07: A current database server usually has a lot of vertical scaling headroom before hardware cost or availability becomes a problem.
- explanation-07: Sharding only works cleanly if there is a natural shard key that most queries filter on.
- explanation-07: Tenant ID and user ID are examples of natural shard keys.
- explanation-07: Premature sharding is a classic way to slow a team down for years.
- explanation-07: The anticipated load that motivates premature sharding may never fully materialize.
- explanation-07: Reactive sharding is a known, roughly one-time cost rather than an ongoing tax.
- explanation-07: The costs of sharding too early versus too late are asymmetric.
- explanation-07: The recommended approach is to scale vertically, add read replicas and caching, and instrument to track the actual growth rate.
- summarization-01: The app now starts up roughly 40% faster.
- summarization-02: The similarity of the config templates directly caused the incident.
- summarization-02: Detection-to-resolution time for the incident was 34 minutes.
- summarization-04: Four clicks produce four error banners.
- summarization-05: Ada's payments database migration dry run is due before Thursday.
- summarization-07: All findings other than the median latency drop, the memory increase, and the crash are still speculative.
- summarization-08: With only 8 participants, the prevalence and even the existence of the admin/regular-user split cannot be estimated.

Added facts (styled only):

- code-review-01: The function contains four real bugs and one style issue.
- code-review-01: The recommended fix is to catch a specific exception (such as `db.errors.InsertError`) and log it.
- code-review-01: The `db=None` default lets the function crash instead of failing clearly.
- code-review-01: The function performs no input validation on `name`, which is a style issue.
- code-review-01: Without validation, an invalid `name` only fails opaquely once it reaches the database.
- code-review-01: The recommended fix is to validate `name` up front and raise or return early with a clear reason.
- code-review-01: In Python's syntax, a parameter without a default must come before any default-valued parameter.
- code-review-01: If `db` is required, it should be placed first in the signature or made keyword-only.
- code-review-01: The corrected function returns `True` on successful insert and returns `False` after logging a `DatabaseError`.
- code-review-02: The code has no handling for a missing `name` field.
- code-review-02: If the API returns data without a `name` property, `profile.name.toUpperCase()` throws instead of failing gracefully.
- code-review-03: The function has two secondary issues besides the SQL injection.
- code-review-03: An attacker can inject a `UNION SELECT` to pull data from other tables.
- code-review-03: `mysql-connector` uses `%s` as its placeholder syntax.
- code-review-03: `SELECT *` returns columns that could later hold sensitive data, such as internal notes or payment details.
- code-review-03: `status` may be intended to be one of a fixed set of values such as `"pending"`, `"shipped"`, or `"cancelled"`.
- code-review-03: With parameterization, an invalid `status` returns zero rows rather than surfacing an error.
- code-review-03: Returning zero rows for an invalid `status` may hide a bug in the caller.
- code-review-04: The `reset` method performs an unsynchronized read-modify-write operation on shared state.
- code-review-04: The fixed `__init__` sets `self.value = 0` and creates `self._lock = threading.Lock()`.
- code-review-04: The fixed `increment` executes `self.value += 1` inside a `with self._lock` block.
- code-review-04: The fixed `reset` executes `self.value = 0` inside a `with self._lock` block.
- code-review-05: The script has one critical bug.
- code-review-05: If a path or filename starts with `-`, a command may interpret it as a flag.
- code-review-05: If no `.log` files exist, `ls *.log` prints an error to stderr and the loop silently does nothing.
- code-review-05: `gzip $f` and the unmatched-glob case can pass a string starting with `-` as if it were a command-line option.
- code-review-05: Using `--` before a filename stops option parsing.
- code-review-05: `rm -rf *.tmp` and `*.log` do not match dotfiles (filenames starting with `.`).
- code-review-05: `rm -rf *.tmp` silently does nothing when no `.tmp` files exist, because the unmatched glob combined with `-f` suppresses the error.
- code-review-05: The suggested rewrite uses `BACKUP_DIR=${1:?usage: $0 <dir>}` for argument validation.
- code-review-06: Two of the bugs cause silent data-sharing problems.
- code-review-06: The function performs no input validation.
- code-review-06: If `base` isn't dict-like, `dict(base)` raises `TypeError`.
- code-review-06: There is no guard, so callers get a generic Python error rather than a clear message.
- code-review-06: Bugs 1 through 3 should be treated as the priority fixes.
- code-review-06: Other code may already depend on the `None`-deletes-key behavior.
- code-review-07: The other issues in the review stem from the helper's inconsistent return behavior.
- code-review-07: Retrying a struggling server with no backoff while rate limits get backoff looks like an oversight rather than a design choice.
- code-review-07: Converting programmer errors to `null` hides bugs unrelated to HTTP retries and is likely unintended.
- code-review-07: Throwing a non-Error value is an edge case relevant only if a caller does something unusual like `throw undefined`.
- code-review-07: Retrying on 429 and 5xx with backoff is a reasonable and probably intentional design for transient failures.
- code-review-07: A caller that uses the `null` result without checking will fail later with a much less informative error, far from the real cause.
- code-review-07: Any type signature or JSDoc on the original `fn` no longer describes what `withRetry(fn)` actually returns.
- code-review-07: Given unknown callers, the safest fix is to make failure explicit rather than guessing at callers' expectations.
- code-review-07: The recommended fix is to re-throw the original error after exhausting retries and for non-retryable statuses, instead of returning `null` or `undefined`.
- code-review-07: Re-throwing preserves the original error's status and message for anyone catching it.
- code-review-07: Re-throwing removes the silent-failure behavior entirely.
- code-review-07: Re-throwing is a behavior change for any caller currently relying on `null` results.
- code-review-07: The change requires auditing the callers, or at least a canary rollout, before deploying.
- code-review-08: The script has three real bugs.
- code-review-08: `PermissionError` can be raised by these calls.
- code-review-08: The script runs on a schedule the user does not control.
- code-review-08: If the 500 cap is meant to bound how much gets deleted per run, deleting oldest-first would be safer.
- code-review-08: The lack of logging may be intentional simplicity.
- code-review-08: The owner should confirm whether `tmp-`/`.part` files are guaranteed orphaned by convention.
- debugging-01: The corrected function get_url returns the f-string "http://{cfg['host']}:{cfg['port']}/api".
- debugging-02: Inside the callback, `this` is `undefined`.
- debugging-02: Reading `this.seconds` inside the callback works.
- debugging-03: The window starting at index 2 is `[3, 4]`.
- debugging-03: The sum of the window `[3, 4]` is 7.
- debugging-04: The file contains a non-ASCII byte at position 512.
- debugging-04: The specific input file that fails must contain non-ASCII text that the other files do not.
- debugging-04: errors="replace" produces a visible marker for bad bytes.
- debugging-06: The "pool exhausted" error means the job's database connection pool ran out of free connections.
- debugging-06: Every waiting request in the incident hit a 30-second timeout.
- debugging-06: The pool exhausted error is a capacity problem rather than a query bug.
- debugging-06: The shared analytics service is the most likely contributor to the failures.
- debugging-06: The database is shared between the export job and the analytics service.
- debugging-06: The failures do not recur at a fixed batch number.
- debugging-06: A bug in the export job itself would tend to make it fail at consistent points.
- debugging-06: A failure pattern with no fixed batch number fits contention from an external, independent workload.
- debugging-06: The analytics service may run a heavy query or its own job in the same time window, temporarily starving the pool.
- debugging-06: If a pool is sized for typical load but not peak load, a busy night can exceed its capacity.
- debugging-06: The export job fails about once a week.
- debugging-06: A connection leak occurs when a code path acquires a connection and never releases it, such as a missed close() or finally block, or an exception skipping cleanup.
- debugging-06: A connection leak causes the pool to shrink gradually until it is exhausted.
- debugging-06: A connection leak fits the no-fixed-batch-number pattern because the leak point can vary.
- debugging-06: A rarely executed leaking code path would fit an intermittent weekly failure frequency.
- debugging-06: A lock wait, missing index, or large table scan can hold connections open longer than normal.
- debugging-06: The log shows the job retried and hit the same timeout again 33 seconds later.
- debugging-06: The retry in the log came from batch 1148.
- debugging-06: Retries without backoff or jitter can compound contention rather than relieve it.
- debugging-06: The failure cannot be reproduced on demand.
- debugging-06: Relevant connection pool metrics include pool size, in-use count, wait queue length, and checkout duration.
- debugging-06: Most databases expose a view of active connections with their running time or state.
- debugging-06: Postgres exposes active connection information through pg_stat_activity.
- debugging-06: Pool usage climbing steadily across the night indicates a connection leak.
- debugging-06: Pool usage spiking in tandem with analytics activity indicates contention or a slow query on the analytics side.
- debugging-07: The most likely cause of the failure is a race condition between seeding the three events and querying the digest.
- debugging-07: The cause is not a bug in the assertion logic itself.
- debugging-07: Two of the events consistently succeed while the third is dropped or arrives late.
- debugging-07: The pattern of two succeeding and one failing points at a timing problem rather than a logic problem.
- debugging-07: A logic bug would cause the test to fail on every run.
- debugging-07: If the API queues events for processing rather than writing them synchronously, the digest may be queried before the third event has propagated.
- debugging-07: An asynchronous or eventually-consistent write path explains why the test never fails locally.
- debugging-07: A serial test run gives each write more wall-clock time relative to CPU load than four parallel workers competing for the same CPU.
- debugging-07: The test never fails locally.
- debugging-07: The CI suite runs with four parallel workers.
- debugging-07: If the four workers share a database, queue, or fixed time window instead of worker-scoped resources, one worker's test can read or clean up data seeded by another worker.
- debugging-07: pytest-xdist does not isolate external resources automatically.
- debugging-07: Isolating external resources requires each worker to get its own schema, namespace, or port.
- debugging-07: If the digest filters events by a time window such as 'last N seconds', and CI is slower or under more contention, one event's timestamp can land just outside the window.
- debugging-07: If two events end up with the same dedupe or idempotency key due to low time resolution, the digest may collapse them into a single event.
- debugging-07: Collapsing two events into one undercounts by exactly one, which matches the observed assertion failure of 2 == 3.
- debugging-07: Running the suite in CI 50-100 times with -n 1 and the same number of times with -n 4 tests whether parallelism is the trigger.
- debugging-07: If failures appear only under -n 4, that confirms parallelism as a factor and rules out a purely test-logic bug.
- debugging-07: The failing test is tests/test_notifications.py::test_digest_contains_all_events.
- debugging-07: pytest-repeat can be used to run a single test repeatedly, for example with --count=200.
- debugging-07: Adding artificial CPU load in the background mimics CI resource pressure.
- debugging-07: Reproducing the failure locally would allow debugging without waiting on CI.
- debugging-07: CI keeps no artifacts from failed runs.
- debugging-07: A failure hook or a try/except around the assertion can log the seeded event IDs, their timestamps, and the raw digest response before the test fails.
- debugging-07: Logging diagnostic data on failure turns the next CI failure into a full diagnostic instead of a bare assertion.
- debugging-07: Having the test poll the digest endpoint until it reports 3 events or a timeout elapses is a diagnostic rather than a permanent fix.
- debugging-07: If polling makes the flake disappear, that confirms an eventual-consistency race in the write path.
- debugging-07: The real fix for an eventual-consistency race is either synchronous event processing or a documented, bounded wait in the test.
- debugging-07: Four candidate causes are ranked: an async write path, shared state across workers, a time-window boundary, and a dedupe key collision.
- debugging-07: Knowing whether parallelism is required to reproduce the failure and having a captured payload from a real failure provides enough evidence to confirm which of the four causes is the actual one.
- debugging-08: Memory allocator fragmentation is the next most likely cause after the unbounded per-event structure.
- debugging-08: Distinguishing between the candidate causes requires a heap profile.
- debugging-08: Capturing a heap profile is the single highest-value next step.
- debugging-08: A cache bounded by entry count only partially fits the canary's continued growth, because the cache still fills from normal traffic.
- debugging-08: An eviction leak, where the cache removes the index entry but a closure, listener, or timer still holds a strong reference to the evicted value, fits the campaign correlation because campaign traffic causes more cache churn.
- debugging-08: An eviction leak fits the lack of overnight recovery because the leaked reference has no time-based reason to clear.
- debugging-08: An eviction leak fits the canary's continued growth because some cache churn happens without webhooks.
- debugging-08: An eviction leak directly explains the unchanged cache bound: the cache is faithfully bounded, but eviction does not free memory.
- debugging-08: Allocator fragmentation fits the campaign correlation because more requests cause more allocation and free churn.
- debugging-08: Allocator fragmentation fits the canary's continued growth because even light traffic causes some allocation churn.
- debugging-08: Allocator fragmentation is orthogonal to cache size.
- debugging-08: Leaked handles fit the canary's continued growth because the canary still runs scheduled jobs and health checks.
- debugging-08: Capturing a heap profile now and diffing it against one taken 24 hours later on the same instance is the fastest way to rule causes in or out at once.
- debugging-08: In Java, heap profiling can be done with jmap and two heap dumps compared in Eclipse MAT, sorted by retained size.
- debugging-08: In Node, heap profiling can be done with --inspect heap snapshots compared in Chrome DevTools.
- debugging-08: In Go, heap profiling can be done with a pprof heap profile diff.
- debugging-08: In Python, heap profiling can be done with tracemalloc snapshots.
- debugging-08: For each such structure, check that every insertion has a matching removal on all paths, including error and retry paths, not just the success path.
- debugging-08: If historical product data is available, compare average product record size now versus a year ago.
- debugging-08: To test the eviction-leak hypothesis, check in the heap diff whether evicted cache values still show live references.
- debugging-08: A dominator or retainer-path view can identify what still holds evicted cache values.
- debugging-08: Eclipse MAT and Chrome DevTools' "Retainers" view provide retainer-path analysis.
- debugging-08: Closures, timers, and event-listener registrations inside cache values are the usual culprits for eviction leaks.
- debugging-08: For glibc-based services, running with MALLOC_ARENA_MAX=1 or switching to jemalloc often resolves fragmentation-driven RSS growth without any code change.
- debugging-08: To test for leaked connections, timers, or listeners, track active handle, timer, or socket counts alongside memory.
- debugging-08: process._getActiveHandles() reports active handles in Node.
- debugging-08: Goroutine count is the equivalent metric to track in Go.
- debugging-08: Thread count is a generally applicable handle metric to track.
- debugging-08: Check whether the handle count's growth curve tracks the memory growth curve.
- debugging-08: If handle count tracks memory growth and the canary still grows without webhook traffic, look for handles created by scheduled jobs or health checks rather than webhook handling.
- debugging-08: The recommended order is to start with the heap profile.
- debugging-08: The heap profile will most likely narrow the field to one or two hypotheses before more manual checks are invested in.
- debugging-08: If the profile shows a specific growing structure, proceed directly to step 2, 3, or 4 depending on the structure.
- debugging-08: If the profile shows live heap flat but RSS climbing, skip straight to step 5.
- explanation-01: Open addressing degrades sharply as the table fills, with probing becoming long and potentially failing.
- explanation-02: Pessimistic locking can cause deadlocks if lock order isn't consistent.
- explanation-03: Historically the initial congestion window was 1 to 4 segments.
- explanation-03: Successful slow start means a new connection quickly finds a sending rate close to what the path can sustain without triggering congestion-driven packet loss at startup.
- explanation-04: Process creation cost is high because the OS allocates a new memory space and resources.
- explanation-04: Thread creation cost is low because the OS reuses the parent's memory space.
- explanation-04: Python and older Ruby versions have a Global Interpreter Lock (GIL).
- explanation-04: Threads still help with I/O-bound work in Python because waiting on a network call releases the GIL.
- explanation-04: A database connection pooler separate from a web server is an example of a component that should be independently restartable or scalable.
- explanation-04: IPC serializes data across the isolation boundary.
- explanation-05: The garbage collector walks live references starting from roots.
- explanation-05: Roots include global variables and active stack frames.
- explanation-05: Using a plain map instead of a size-bounded or weak-referenced cache is a common trigger of unbounded cache leaks.
- explanation-05: Forgetting to remove entries when their associated session, connection, or request ends is a common trigger of unbounded cache leaks.
- explanation-06: A cache stores a copy of data so a slow fetch can be skipped the next time the data is needed.
- explanation-06: A cache introduces a second place where data can be wrong, in the form of a stale cache read.
- explanation-06: A cache requires designing an invalidation strategy.
- explanation-06: An invalidation strategy decides when to clear or update cached entries after a write.
- explanation-06: Request tracers such as OpenTelemetry can show where time goes in a request.
- explanation-07: If indexed queries are already slow at 200 GB, the cause is usually schema, indexing, or query design rather than size.
- explanation-07: Picking a shard key before understanding real access patterns risks choosing a wrong key.
- explanation-07: A wrong shard key forces a costly re-shard later.
- explanation-07: Sharding causes the loss of features Postgres provides for free.
- summarization-01: The app now starts up to 40% faster.
- summarization-02: Staging intentionally uses smaller values than production.
- summarization-02: Errors started at 09:14.
- summarization-02: The page fired at 09:21.
- summarization-02: The rollback resolved the incident at 09:48.
- summarization-02: The detection and recovery process does not need changes.
- summarization-03: Moving thumbnail generation to a background queue cuts upload latency by 800ms to 3s per request.
- summarization-03: The worker pool updates the record after generating thumbnails.
- summarization-07: The staging test compared the new request batcher against the current batcher.
- summarization-07: The recommendation is to profile memory before drawing conclusions.
- summarization-07: The recommendation is to test under production-like traffic before drawing conclusions on tail latency and the crash.
- summarization-08: The progress bar finding is tentative but has a firm consequence.
- summarization-08: The template gallery observation is inconclusive and is not a finding.
- summarization-08: The template gallery observation needs follow-up, such as asking non-users directly, before drawing a conclusion.

### clarity-flow

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 29 | 21 | 0.724 | 25 | 3 |
| code-review-02 | 20 | 16 | 0.8 | 23 | 2 |
| code-review-03 | 26 | 15 | 0.577 | 19 | 6 |
| code-review-04 | 19 | 15 | 0.789 | 25 | 2 |
| code-review-05 | 33 | 26 | 0.788 | 34 | 5 |
| code-review-06 | 25 | 18 | 0.72 | 31 | 6 |
| code-review-07 | 32 | 21 | 0.656 | 34 | 11 |
| code-review-08 | 35 | 26 | 0.743 | 36 | 4 |
| debugging-01 | 6 | 6 | 1.0 | 5 | 1 |
| debugging-02 | 17 | 14 | 0.824 | 12 | 1 |
| debugging-03 | 10 | 10 | 1.0 | 8 | 2 |
| debugging-04 | 12 | 7 | 0.583 | 13 | 2 |
| debugging-05 | 15 | 10 | 0.667 | 13 | 0 |
| debugging-06 | 3 | 0 | 0.0 | 26 | 26 |
| debugging-07 | 6 | 0 | 0.0 | 27 | 27 |
| debugging-08 | 30 | 0 | 0.0 | 7 | 7 |
| explanation-01 | 44 | 28 | 0.636 | 20 | 1 |
| explanation-02 | 29 | 26 | 0.897 | 26 | 0 |
| explanation-03 | 34 | 20 | 0.588 | 19 | 1 |
| explanation-04 | 30 | 23 | 0.767 | 31 | 3 |
| explanation-05 | 20 | 19 | 0.95 | 15 | 2 |
| explanation-06 | 17 | 14 | 0.824 | 17 | 7 |
| explanation-07 | 24 | 14 | 0.583 | 32 | 13 |
| explanation-08 | 12 | 6 | 0.5 | 15 | 5 |
| summarization-01 | 6 | 6 | 1.0 | 5 | 0 |
| summarization-02 | 12 | 11 | 0.917 | 17 | 5 |
| summarization-03 | 13 | 13 | 1.0 | 13 | 1 |
| summarization-04 | 14 | 12 | 0.857 | 11 | 0 |
| summarization-05 | 10 | 10 | 1.0 | 8 | 0 |
| summarization-06 | 14 | 13 | 0.929 | 12 | 2 |
| summarization-07 | 15 | 14 | 0.933 | 16 | 1 |
| summarization-08 | 17 | 16 | 0.941 | 23 | 2 |

Median fraction: 0.788 over 32 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: The function performs no input validation.
- code-review-01: The function does not check that `name` is non-empty or of the correct type.
- code-review-01: The function does not check that `roles` contains valid role values.
- code-review-01: The function has no duplicate-role protection.
- code-review-01: Failure modes conflated by the boolean return include bad input, DB down, and duplicate entry.
- code-review-01: The suggested fix appends `"member"` only if it is not already in `roles`.
- code-review-01: The suggested fix catches `Exception` instead of using a bare `except:`.
- code-review-01: The suggested fix logs the failure with `logger.error` including the user name and exception.
- code-review-02: A throw inside an async function body produces a rejected promise rather than an exception thrown at the call site.
- code-review-02: Calling `.json()` on an error response may alternatively succeed and yield an unexpected error payload.
- code-review-02: Assigning to an outer `let` variable inside `.then()` instead of chaining or returning is an anti-pattern.
- code-review-02: The outer-variable assignment pattern obscures the fact that the value is not ready when it is used.
- code-review-03: The SQL injection issue is critical.
- code-review-03: `%s` is the placeholder syntax for psycopg2 and MySQLdb.
- code-review-03: The function does not check that `status` is one of the expected enum values.
- code-review-03: The function does not check that `customer_name` is non-empty or of reasonable length.
- code-review-03: The function has no type hints.
- code-review-03: The function has no docstring.
- code-review-03: The `cursor` parameter and the return type are not documented.
- code-review-03: The lack of type hints and docstring makes the function's contract unclear to callers.
- code-review-03: The query has no `LIMIT` clause.
- code-review-03: Without a `LIMIT`, a broad match could return a huge number of rows.
- code-review-03: The issues other than SQL injection are secondary polish.
- code-review-04: CPython has a Global Interpreter Lock (GIL).
- code-review-04: CPython's GIL prevents literal byte-level memory corruption.
- code-review-04: CPython's GIL does not make `current = self.value; self.value = current + 1` atomic as a whole.
- code-review-04: The sequence `current = self.value; self.value = current + 1` compiles to multiple bytecode operations.
- code-review-05: If no `.tmp` files exist and globbing is not nullglob-safe, `*.tmp` is passed literally to `rm -rf`, which errors out.
- code-review-05: `rm -rf *.tmp` is a broad, silent recursive delete with no confirmation.
- code-review-05: The script relies on nothing POSIX-incompatible.
- code-review-05: The `ls *.log` parsing bug exists independently of which shell is used.
- code-review-05: The suggested rewrite exits with status 1 and prints a usage message to stderr if `$BACKUP_DIR` is empty or not a directory.
- code-review-05: The suggested rewrite uses `rm -f -- *.tmp 2>/dev/null || true`.
- code-review-05: The suggested rewrite loops over `*.log` and skips entries that do not exist with `[ -e "$f" ] || continue`.
- code-review-06: `isinstance(merged[key], dict)` returns False for custom `Mapping` types that are not literally `dict`.
- code-review-06: Dict-like objects that are not `dict` instances fall back to full replacement instead of being merged.
- code-review-06: The code contains `if value is None: merged.pop(key, None)`.
- code-review-06: Using `None` to mean deletion is a common pattern in config merge/patch semantics, as in Kubernetes strategic merge and Helm.
- code-review-06: The function has no cycle detection.
- code-review-06: A self-referential `base` dict would cause infinite recursion.
- code-review-06: The function has no docstring and no type hints.
- code-review-07: The backoff formula does not match the exponential-backoff-from-first-retry pattern it appears to imitate.
- code-review-07: On the last loop iteration, a 429 still triggers the setTimeout wait before the loop exits.
- code-review-07: The wait on the final attempt is a pointless delay because the function returns undefined anyway.
- code-review-07: Accessing err.status on null or undefined throws a TypeError inside the catch block.
- code-review-07: The TypeError thrown inside the catch block is not caught anywhere in the function and propagates out uncaught.
- code-review-07: An uncaught TypeError breaks the implied contract that the function never throws.
- code-review-07: A suppressed error could silently produce a fail-open state if a caller uses the result for a permission or entitlement check.
- code-review-07: Network failures are the most common reason to want retry logic.
- code-review-07: 501 Not Implemented is a permanent condition, so retrying it is pure waste, unlike 502, 503, and 504.
- code-review-07: The silent swallowing of errors changes the function's error-handling contract invisibly to callers and could mask bugs and security-relevant failures.
- code-review-07: The backoff math, inconsistent return values, uncaught throw null edge case, and lack of retries for non-HTTP errors read like accumulated bugs rather than intentional behavior.
- code-review-08: `os.path.getmtime` works on directories.
- code-review-08: The `removed` count is lost on failure because it is never returned.
- code-review-08: The age-based deletion and the tmp/`.part` deletion are two unrelated criteria sharing one counter.
- code-review-08: In that case the age-based cleanup silently stops early for that run with no logging to explain why.
- code-review-08: The interaction between the two deletion branches is non-deterministic across runs.
- code-review-08: The script has no dry-run mode.
- code-review-08: `clean()` is never called in the snippet.
- code-review-08: As given, the script does nothing when executed directly, unless the snippet is truncated.
- code-review-08: The 500 cap limits blast radius if the `CUTOFF` logic broke and flagged everything as stale.
- debugging-02: Code defined inside a `class` body runs in strict mode.
- debugging-02: In strict mode, `this` inside such a callback is `undefined`.
- debugging-02: Accessing `this.seconds` when `this` is `undefined` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-04: The byte 0xc3 suggests UTF-8-encoded multi-byte characters, such as accented letters.
- debugging-04: The code forces encoding="ascii" when opening the file.
- debugging-04: Under an ascii encoding, any byte greater than or equal to 0x80 causes an error.
- debugging-04: errors="ignore" silently drops malformed bytes.
- debugging-04: errors="replace" preserves line structure.
- debugging-05: DEFAULT_TAGS is a single list object created once at function-definition time.
- debugging-05: In Python, a default argument value is evaluated once at def time, not per call.
- debugging-05: An alternative fix is to use tags=() and convert it to a list inside the function.
- debugging-05: Another alternative fix is to use a sentinel value.
- debugging-05: The None-default-plus-copy pattern is the standard idiom.
- debugging-06: The speaker intends to check whether actual project code is present in the working directory.
- debugging-06: Project code, if present, might reveal the connection pool configuration.
- debugging-06: The speaker will look for relevant code in the working directory before giving an answer.
- debugging-07: Checking whether the actual test code exists in the current directory would enable more concrete advice.
- debugging-07: A Bash tool call is issued with the command "find . -iname '*notification*' -o -iname 'conftest.py' 2>/dev/null | head -50".
- debugging-07: The Bash tool call's description is "Search for relevant test files".
- debugging-07: The command searches the current directory for files whose names match '*notification*' or are named 'conftest.py'.
- debugging-07: The command limits its output to the first 50 results via head -50.
- debugging-07: The command discards error output by redirecting stderr to /dev/null.
- debugging-08: Unbounded growth tied to request volume is the most likely cause of the memory growth.
- debugging-08: Per-request allocations such as listeners, timers, and connection or context objects can leak if never released.
- debugging-08: An unbounded structure keyed by request or webhook data (correlation IDs, idempotency keys, high-cardinality metrics labels) can grow with traffic.
- debugging-08: Marketing campaigns increase traffic, which increases the rate of memory growth.
- debugging-08: The canary instance receives no webhooks but still grows in memory, just more slowly.
- debugging-08: If the growth rate versus request rate is roughly linear, the leak is traffic-correlated.
- debugging-08: Metrics libraries such as Prometheus clients and StatsD wrappers create a new time series per unique label value.
- debugging-08: Each metrics time series is retained forever in-process.
- debugging-08: Webhooks and marketing campaigns often carry unique or high-cardinality identifiers.
- debugging-08: If metrics registry size climbs monotonically and correlates with traffic, high-cardinality metrics labels are the culprit.
- debugging-08: Caches described as bounded often bound entry count rather than bytes.
- debugging-08: If product payloads grow larger, heap usage can increase even with a bounded entry count.
- debugging-08: A custom LRU eviction policy can have bugs that prevent eviction under certain access patterns.
- debugging-08: Bounding a wrapper map does not bound memory if its values reference large objects containing additional maps.
- debugging-08: A second unbounded cache or index, such as a reverse-lookup index, may be built alongside the bounded cache.
- debugging-08: If cache entry count is flat but byte size grows, the cause is payload size or a leak inside cache values.
- debugging-08: If cache entry count grows past the configured bound, the eviction logic is broken.
- debugging-08: Native or off-heap memory such as JIT, GC arenas, and network buffers can cause growth instead of leaked managed objects.
- debugging-08: Memory growth that survives quiet nights is consistent with allocator fragmentation.
- debugging-08: A native library for compression, TLS, or image processing may fail to return memory to the OS.
- debugging-08: Native memory growth does not appear in a heap profile of managed objects.
- debugging-08: The user currently has no heap profile insight.
- debugging-08: If RSS grows while the runtime's heap-used metric stays flat or sawtooth, the growth is native memory.
- debugging-08: If RSS does not drop after forcing a full GC, the memory is not GC-reachable garbage.
- debugging-08: glibc malloc arena behavior can retain memory that is not returned to the OS.
- debugging-08: Plotting growth rate against request or webhook volume is cheap and requires no code changes.
- debugging-08: Adding cache entry-count and byte-size logging is cheap and isolates the cache question.
- debugging-08: Comparing RSS against the runtime heap metric isolates managed versus native memory.
- debugging-08: A heap diff is the missing diagnostic and will immediately disambiguate the traffic-volume leak from the high-cardinality metrics cause.
- debugging-08: A heap diff shows which objects accumulated.
- explanation-01: A hash map's array has a fixed number of buckets.
- explanation-01: There is no limit to the number of possible keys a hash map may receive.
- explanation-01: The collection in a chaining bucket is usually a linked list, and sometimes a tree or dynamic array.
- explanation-01: Separate chaining is simple to implement and reason about.
- explanation-01: Deletion under separate chaining is easy because you just remove the node from the list.
- explanation-01: In the worst case, with many collisions in one bucket, chaining degrades to O(n) lookup within that bucket because the list must be scanned.
- explanation-01: Linear probing checks index+1, index+2, and so on.
- explanation-01: Quadratic probing and double hashing are other probing variants.
- explanation-01: Open addressing implementations typically resize well before the array gets full, often at around 70% load.
- explanation-01: Deletion under open addressing is trickier because emptying a slot might break the probe chain for a later key.
- explanation-01: Deletion under open addressing usually requires a special tombstone marker instead of a true empty slot.
- explanation-01: Deletion is simple under chaining and needs tombstones under open addressing.
- explanation-01: Chaining is simpler and more forgiving when the load factor is unpredictable.
- explanation-01: Most general-purpose hash maps use chaining.
- explanation-01: Some high-performance hash maps use open addressing variants for speed.
- explanation-01: Rust's HashMap uses an open addressing variant.
- explanation-02: FOR UPDATE blocks any other transaction from reading or modifying that row until the locking transaction commits.
- explanation-02: Optimistic locking fits cases with long think time between read and write, such as a user editing a form for minutes.
- explanation-02: Optimistic locking fits distributed or web systems where holding a database lock across a network round-trip or user interaction is impractical.
- explanation-03: TCP slow start also runs when a connection restarts after a pause.
- explanation-03: A network path may cross a fast local network and then a slow, congested link in the middle.
- explanation-03: Dropped packets cause retransmissions, wasted bandwidth, and cascading congestion.
- explanation-03: Congestion from one connection can degrade the network for everyone sharing that link.
- explanation-03: The congestion window limits how much unacknowledged data the sender may have in flight at once.
- explanation-03: The congestion window is separate from the receive window.
- explanation-03: The receive window reflects the receiver's buffer capacity.
- explanation-03: TCP respects whichever of the congestion window and receive window is smaller.
- explanation-03: Historically the initial cwnd was 1 segment.
- explanation-03: Modern implementations often start with a higher initial cwnd, such as 10 segments.
- explanation-03: RFC 6928 specifies an initial window of 10 segments.
- explanation-03: ACKs only arrive if data is getting through successfully, so cwnd growth stalls when the network cannot keep up.
- explanation-03: Packet loss is detected via timeout or duplicate ACKs.
- explanation-03: In congestion avoidance, cwnd grows linearly instead of exponentially.
- explanation-04: A process has its own memory address space, file descriptors, and OS-level resources.
- explanation-04: Each thread has its own stack and instruction pointer.
- explanation-04: Web servers and browsers run each tab or worker as a separate process so one bad request doesn't kill the whole server.
- explanation-04: In runtimes with a global interpreter lock, threads help with I/O-bound work but not CPU-bound work.
- explanation-04: Python's multiprocessing module is used for CPU-bound parallel computation.
- explanation-04: Independent process lifecycle management is useful for worker pools where a hung or leaking worker should be recycled.
- explanation-04: Threads are a natural fit for I/O-bound concurrency within a single trusted program.
- explanation-05: A memory leak in a garbage-collected language does not mean memory is lost as it is in C with unfreed malloc.
- explanation-06: A cache used under write-heavy or low-repetition workloads becomes a layer that is frequently invalidated or missed.
- explanation-06: Common database issues to check first include missing indexes, N+1 queries, and slow joins.
- explanation-06: Redis is an example of a cache that can be placed in front of a database.
- explanation-07: Machines with multiple terabytes of RAM/NVMe are routine.
- explanation-07: Sharding fixes throughput ceilings and total-size ceilings.
- explanation-07: Sharding does not fix slow queries.
- explanation-07: If the real problem is unindexed queries or lock contention, sharding will not help.
- explanation-07: Growth rate can be estimated by measuring growth over the last 3-6 months and extrapolating.
- explanation-07: Single-instance PostgreSQL limits are roughly multiple terabytes of data and tens of thousands of writes per second.
- explanation-07: A current database server usually has a lot of vertical scaling headroom before hardware cost or availability becomes a problem.
- explanation-07: Reactive sharding is a known, roughly one-time cost rather than an ongoing tax.
- explanation-07: The costs of sharding too early versus too late are asymmetric.
- explanation-07: The recommended approach is to scale vertically, add read replicas and caching, and instrument to track the actual growth rate.
- explanation-08: Measuring what fraction of request latency comes from JSON serialization is roughly a five-minute profiling task.
- explanation-08: Binary formats such as Protobuf and MessagePack typically shrink payloads by 20-50% relative to JSON.
- explanation-08: Payload size reduction matters most when requests are large and network- or bandwidth-bound rather than CPU-bound.
- explanation-08: Smaller payloads help more on slow or mobile networks than on localhost or fast LANs.
- explanation-08: For CPU-bound serialization, binary formats typically run 2-10x faster than JSON.
- explanation-08: Migrating from JSON to a binary format carries meaningful costs including schemas, tooling, and debuggability tradeoffs.
- summarization-02: The rollback fixed the incident in about 27 minutes.
- summarization-04: The reproduction involves clicking the Export button and choosing the PDF option.
- summarization-04: Four clicks produce four error banners.
- summarization-06: Connection-pool exhaustion and a retry storm are the leading hypotheses for the outage.
- summarization-07: All findings other than the median latency drop, the memory increase, and the crash are still speculative.
- summarization-08: The template gallery is a new feature.

Added facts (styled only):

- code-review-01: The code under review has four distinct problems.
- code-review-01: The mutation problem is worse in combination with the mutable default argument problem.
- code-review-01: The suggested rewrite lets real errors propagate so callers can see and handle failures.
- code-review-02: The function mixes `async`/`await` with `.then` chaining unnecessarily.
- code-review-02: The fix throws an `Error` with the message `Failed to load user ${userId}: ${res.status}` when `res.ok` is false.
- code-review-03: Pulling every column wastes bandwidth.
- code-review-03: A `None` or unexpected type argument produces a confusing error deep inside string concatenation rather than a clear error at the boundary.
- code-review-03: The function does not handle quote escaping.
- code-review-03: A legitimate customer name containing an apostrophe, such as `O'Brien`, breaks the query.
- code-review-03: Parameterized queries make the database driver handle escaping and injection safely.
- code-review-03: Using parameterized queries also resolves the apostrophe-escaping issue as a side effect.
- code-review-04: Every method of the class exposes the thread-safety gap.
- code-review-04: A thread in the middle of an increment can overwrite a reset, and a reset can overwrite an increment.
- code-review-05: POSIX `sh` does not support `nullglob`.
- code-review-05: `rm -rf *.tmp` with no matches usually fails quietly because of the `-f` flag.
- code-review-05: If a `.log.gz` file already exists, `gzip` will prompt, or fail or skip in a non-interactive script depending on flags.
- code-review-05: The script does not handle the case where the `.gz` output file already exists.
- code-review-05: A safer rewrite uses `BACKUP_DIR=${1:?Usage: $0 <backup_dir>}` to require the argument.
- code-review-06: That asymmetry is the strongest evidence the behavior is not deliberate.
- code-review-06: A sentinel object could be used instead of `None` if setting a value to `None` is ever needed.
- code-review-06: The recommendation is to write tests pinning down current behavior for cases #1, #2, and #4 before doing anything else with the function.
- code-review-06: Such tests will force a decision on whether the crash/replace asymmetry is a bug to fix or something relied upon elsewhere.
- code-review-06: It is less likely that the crash/replace asymmetry is relied upon elsewhere.
- code-review-06: After writing those tests, the next decision is whether to deep-copy or to document the shared-state behavior.
- code-review-07: The function has one serious bug.
- code-review-07: The inconsistency between 5xx and 429 backoff behavior looks like an oversight rather than intent.
- code-review-07: If `attempts` is 0, the loop body never runs and `fn` is never called, producing a silent no-op.
- code-review-07: Fail-soft `null` conversion is a defensible choice for a best-effort background job.
- code-review-07: Any caller that does not explicitly check for `null` will silently continue with bad data.
- code-review-07: Linear backoff on 429 might be an intentional simplification.
- code-review-07: Callers that cannot be seen may already depend on the `null`/`undefined` swallowing behavior.
- code-review-07: The safest fix is not necessarily to throw everywhere.
- code-review-07: The minimum recommended fix is to make the exhausted-retries case return `null` explicitly, matching the existing convention.
- code-review-07: The recommended fix includes preserving the original error on an `err` field.
- code-review-07: Changes to what gets thrown versus returned should be confirmed with any known callers first.
- code-review-08: `getmtime` follows symlinks and raises on a broken symlink.
- code-review-08: File mtimes don't change.
- code-review-08: The user said the scheduling setup isn't documented.
- code-review-08: The 45-day retention window and 500-per-run cap look like intentional policy (a retention period and an I/O throttle) rather than bugs.
- debugging-01: The function `get_url` looks up the key `cfg['Port']` with a capital P.
- debugging-02: The global object is referred to as `window` or `globalThis`.
- debugging-03: For input `[1, 2, 3, 4]` with `window=2`, the window at `i=2` sums to 7 (3+4).
- debugging-03: For input `[1, 2, 3, 4]` with `window=2`, the corrected function returns `[3, 5, 7]`.
- debugging-04: UTF-8 is a superset of ASCII.
- debugging-04: Detecting a file's encoding before opening it handles arbitrary or unknown encodings robustly.
- debugging-06: The pool exhaustion indicates too many concurrent consumers of a fixed-size connection pool rather than a single slow query.
- debugging-06: The shared analytics service is the most likely cause of the pool exhaustion.
- debugging-06: The connection pool is fixed in size.
- debugging-06: The export job failures occur weekly.
- debugging-06: The batch number at which the failure occurs varies between failures.
- debugging-06: Weekly failures are consistent with a periodic analytics job.
- debugging-06: A varying batch number indicates the problem is timing-dependent rather than data-dependent.
- debugging-06: If the analytics service runs scheduled queries or dashboards overnight, it can hold connections long enough to starve the export job.
- debugging-06: The export job and analytics service may share a pool sized for only one workload.
- debugging-06: Two services sharing a pool can exceed its capacity on nights when both run longer than usual, even without a load spike.
- debugging-06: A code path that fails to release connections gradually shrinks the effective pool.
- debugging-06: Connection leaks can be caused by a missed `finally` block or context manager, or by an exception swallowing a `close()` call.
- debugging-06: A connection leak would produce intermittent rather than constant failures because leaked connections must accumulate before hitting the pool ceiling.
- debugging-06: A single long-running or blocking query, such as an analytics report or a lock-holding transaction, can occupy a connection for the full 30s+ window and back up other consumers.
- debugging-06: The export job's timeout window is 30 seconds or longer.
- debugging-06: Correlating the analytics service's job schedule and logs against failure timestamps across several occurrences can identify the cause.
- debugging-06: Failures clustering around a recurring analytics job start time would confirm analytics contention as the cause.
- debugging-06: Pool utilization metrics track active and idle connections over time.
- debugging-06: A connection leak appears in pool metrics as a slow upward drift over days.
- debugging-06: Contention appears in pool metrics as sharp spikes that recover.
- debugging-06: `log_min_duration_statement` is a Postgres setting for logging slow queries at the database level.
- debugging-06: Enabling slow query logging filtered to the failure window reveals what is holding connections when the export times out.
- debugging-06: Un-released connections can be found by grepping for manual connection acquisition without a guaranteed release path, especially in retry or error-handling logic.
- debugging-06: Running the analytics workload and export job concurrently in staging with the production pool size can force the timeout to reproduce.
- debugging-06: Artificially reproducing the load in staging is cheaper than waiting for a weekly failure.
- debugging-06: Starting with pool metrics and analytics schedule correlation is the fastest way to distinguish shared resource contention from a leak.
- debugging-07: The most likely cause of the failure is a race between event ingestion and digest generation.
- debugging-07: The race is exposed by parallelism rather than directly caused by it.
- debugging-07: If the API accepts events and processes them asynchronously before they are queryable, the digest can run before all three events land.
- debugging-07: Asynchronous processing can occur via a queue, a background task, or eventual consistency in a search index.
- debugging-07: Parallel workers increase load and timing variance.
- debugging-07: Increased timing variance makes the race window more likely to be hit.
- debugging-07: The ingestion race bug can exist in serial runs as well as parallel ones.
- debugging-07: If events are not scoped by worker, another test's cleanup or another worker's write could delete or shadow one of the three events between seeding and digest generation.
- debugging-07: Lack of worker scoping includes a shared DB, a shared table, or no unique test-run ID.
- debugging-07: A fixture that resets state on a schedule or in teardown could fire between the third seed call and the digest read if workers share a resource such as a DB, Redis, or a file.
- debugging-07: If the digest filters by timestamp and events are seeded fast enough to straddle a boundary, one event could fall just outside the range.
- debugging-07: A truncated-second window is an example of a time-window boundary that could cause an off-by-one.
- debugging-07: Parallel CI runners are often slower or under more contention than a dev machine.
- debugging-07: Contention on CI runners changes timing enough to expose an off-by-one that a fast dev machine never hits.
- debugging-07: The suite can be run serially in CI with the `-n 0` flag.
- debugging-07: If serial runs never fail over a few dozen repetitions, parallelism is a necessary condition rather than merely correlated.
- debugging-07: Parallelism being a necessary condition points to shared state or resource contention rather than a pure timing bug in the seed-to-digest path.
- debugging-07: Running only the affected test file with 4 or more workers in a loop can reproduce the failure locally.
- debugging-07: `pytest -n 4 tests/test_notifications.py -k test_digest_contains_all_events --count=50` is a command that runs the test repeatedly with 4 workers.
- debugging-07: The test fails in CI at a rate of 10%.
- debugging-07: The test's failure manifests as a count of 2 instead of 3.
- debugging-07: If workers share a database without transaction-per-test isolation, that is the primary suspect and worth fixing before investigating timing.
- debugging-07: CI keeps no artifacts.
- debugging-07: Logging the returned digest's event IDs and timestamps on failure turns a '2 vs 3' count into a diagnosable list.
- debugging-07: A single non-persistent print in CI output costs nothing.
- debugging-07: Adding a wait or poll for eventual consistency after seeding, and seeing the flake disappear, confirms a race at that async boundary.
- debugging-07: The suggested investigation steps are ordered by cost.
- debugging-08: The speaker intends to check memory for prior context on the service.
- debugging-08: A bash tool call is made with the id toolu_015mHzZBmkgQx1Yq7Zn7Loa4.
- debugging-08: The command runs `cat` on a file named MEMORY.md.
- debugging-08: The MEMORY.md file is located at /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-r_e4snvc/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-it57otsa/memory/.
- debugging-08: The command redirects error output to /dev/null.
- debugging-08: The command echoes 'no memory file' if the cat command fails.
- debugging-08: The command's description is 'Check memory index'.
- explanation-01: Knowing which collision strategy a language uses explains observable behavior.
- explanation-03: A connection's path might cross a fast datacenter link or a congested home router.
- explanation-04: Thread operations are cheaper because they involve no memory copying or remapping.
- explanation-04: Ruby has a global interpreter lock.
- explanation-04: OS-enforced separation between processes is useful for isolating privileged operations.
- explanation-05: Unreclaimed reachable objects cause memory use to keep growing.
- explanation-05: Lacking an eviction policy or TTL is an example of a collection never being cleaned up.
- explanation-06: Caching is suitable for reads that tolerate slightly stale data.
- explanation-06: Caching does nothing for reads that are already fast.
- explanation-06: Slowness could come from slow database queries, a slow external API, network latency, or CPU-bound work.
- explanation-06: A cache does not fix slow queries, slow external APIs, network latency, or CPU-bound work.
- explanation-06: The complexity a cache adds includes invalidation, staleness, and extra infrastructure.
- explanation-06: Profiling can be done by adding timing logs or using a profiler.
- explanation-06: Adding a cache introduces new failure modes such as stale data and cache invalidation bugs.
- explanation-07: Premature sharding trades a problem you understand for a set of problems you don't
- explanation-07: Sharding is specifically for write scaling
- explanation-07: Migrations, backups, rebalancing, and monitoring all need to work N times over under sharding
- explanation-07: If a team is still stabilizing single-instance operations, sharding adds risk before it adds capacity
- explanation-07: Vertical scaling options include a bigger instance, better indexes, partitioning, and read replicas
- explanation-07: The decision may need to be revisited in 12-18 months if staying on one instance
- explanation-07: Sharding now risks picking the wrong shard key before usage patterns are clear
- explanation-07: Re-sharding later is far more painful than sharding for the first time
- explanation-07: Operational failure modes multiply under sharding, including partial outages, hot shards, and rebalancing bugs
- explanation-07: These operational failure modes multiply well before the business needs the capacity
- explanation-07: Write throughput, connection saturation, and query latency should be tracked now
- explanation-07: Partitioning and read replicas buy significant headroom without architectural lock-in
- explanation-07: A team's inability to state a growth number is evidence it lacks the signal needed to pick a shard key correctly
- explanation-08: JSON has text overhead from field names, quotes, and delimiters.
- explanation-08: JSON's text overhead shrinks most with repetitive schemas and numeric-heavy data.
- explanation-08: Payloads that are mostly short strings gain less from switching to a binary format.
- explanation-08: If serialization is 40% of request time, switching formats matters a lot.
- explanation-08: Payload sizes can be measured by sampling real request and response bodies and comparing JSON size to a candidate binary format on the same data.
- summarization-02: The reduced connection pool was exhausted under load.
- summarization-02: Errors started at 09:14.
- summarization-02: The page went out at 09:21.
- summarization-02: Rollback resolved the issue by 09:48.
- summarization-02: The incident's response time should be kept as the baseline for future incidents.
- summarization-03: Moving thumbnail generation to a background queue would cut 800ms–3s off every upload request.
- summarization-06: No relevant memory was found.
- summarization-06: The on-call engineer suspects connection-pool exhaustion in the payments client.
- summarization-07: The batcher cannot be called production-ready yet.
- summarization-08: Findings 2 and 3 should be treated as directional.
- summarization-08: Findings 2 and 3 are worth prioritizing for a larger study but not for a design decision yet.

### classic-concise

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 29 | 25 | 0.862 | 25 | 2 |
| code-review-02 | 20 | 14 | 0.7 | 13 | 1 |
| code-review-03 | 26 | 15 | 0.577 | 17 | 2 |
| code-review-04 | 19 | 11 | 0.579 | 12 | 4 |
| code-review-05 | 33 | 24 | 0.727 | 33 | 0 |
| code-review-06 | 25 | 18 | 0.72 | 34 | 9 |
| code-review-07 | 32 | 19 | 0.594 | 31 | 6 |
| code-review-08 | 35 | 29 | 0.829 | 36 | 8 |
| debugging-01 | 6 | 5 | 0.833 | 6 | 0 |
| debugging-02 | 17 | 14 | 0.824 | 11 | 0 |
| debugging-03 | 10 | 9 | 0.9 | 6 | 1 |
| debugging-04 | 12 | 9 | 0.75 | 10 | 0 |
| debugging-05 | 15 | 12 | 0.8 | 10 | 0 |
| debugging-06 | 3 | 0 | 0.0 | 30 | 30 |
| debugging-07 | 6 | 0 | 0.0 | 24 | 24 |
| debugging-08 | 30 | 19 | 0.633 | 35 | 18 |
| explanation-01 | 44 | 35 | 0.795 | 28 | 1 |
| explanation-02 | 29 | 28 | 0.966 | 17 | 0 |
| explanation-03 | 34 | 24 | 0.706 | 24 | 4 |
| explanation-04 | 30 | 23 | 0.767 | 20 | 4 |
| explanation-05 | 20 | 16 | 0.8 | 10 | 0 |
| explanation-06 | 17 | 10 | 0.588 | 16 | 3 |
| explanation-07 | 24 | 14 | 0.583 | 17 | 6 |
| explanation-08 | 12 | 5 | 0.417 | 12 | 5 |
| summarization-01 | 6 | 6 | 1.0 | 6 | 1 |
| summarization-02 | 12 | 11 | 0.917 | 11 | 3 |
| summarization-03 | 13 | 12 | 0.923 | 13 | 2 |
| summarization-04 | 14 | 13 | 0.929 | 15 | 2 |
| summarization-05 | 10 | 8 | 0.8 | 6 | 0 |
| summarization-06 | 14 | 14 | 1.0 | 12 | 1 |
| summarization-07 | 15 | 14 | 0.933 | 13 | 1 |
| summarization-08 | 17 | 13 | 0.765 | 16 | 1 |

Median fraction: 0.781 over 32 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: The function does not check that `roles` contains valid role values.
- code-review-01: Failure modes conflated by the boolean return include bad input, DB down, and duplicate entry.
- code-review-01: The suggested fix catches `Exception` instead of using a bare `except:`.
- code-review-01: The suggested fix logs the failure with `logger.error` including the user name and exception.
- code-review-02: An `async` function returns a promise wrapping its return value.
- code-review-02: A throw inside an async function body produces a rejected promise rather than an exception thrown at the call site.
- code-review-02: Calling `.json()` on an error response such as a 404 HTML page will likely throw a JSON parse error.
- code-review-02: Calling `.json()` on an error response may alternatively succeed and yield an unexpected error payload.
- code-review-02: Assigning to an outer `let` variable inside `.then()` instead of chaining or returning is an anti-pattern.
- code-review-02: The outer-variable assignment pattern obscures the fact that the value is not ready when it is used.
- code-review-03: The SQL injection issue is critical.
- code-review-03: `%s` is the placeholder syntax for psycopg2 and MySQLdb.
- code-review-03: The function does not check that `customer_name` is non-empty or of reasonable length.
- code-review-03: The function has no type hints.
- code-review-03: The function has no docstring.
- code-review-03: The `cursor` parameter and the return type are not documented.
- code-review-03: The lack of type hints and docstring makes the function's contract unclear to callers.
- code-review-03: The query has no `LIMIT` clause.
- code-review-03: Without a `LIMIT`, a broad match could return a huge number of rows.
- code-review-03: The SQL injection is the issue to fix immediately.
- code-review-03: The issues other than SQL injection are secondary polish.
- code-review-04: CPython has a Global Interpreter Lock (GIL).
- code-review-04: CPython's GIL prevents literal byte-level memory corruption.
- code-review-04: CPython's GIL does not make `current = self.value; self.value = current + 1` atomic as a whole.
- code-review-04: The sequence `current = self.value; self.value = current + 1` compiles to multiple bytecode operations.
- code-review-04: A thread switch can happen between the bytecode operations of a read-modify-write.
- code-review-04: External code reading `counter.value` while another thread is mid-increment can observe inconsistent or stale state.
- code-review-04: Exposing `value` as a property that acquires the lock before returning `_value` provides a safe read.
- code-review-04: Guarding every read and write of `_value` with the same lock ensures reads always see a consistent value.
- code-review-05: If `$1` is empty, `cd $BACKUP_DIR` becomes `cd` with no arguments.
- code-review-05: `cd` with no arguments changes to `$HOME`.
- code-review-05: An empty `$1` combined with `rm -rf *.tmp` could delete files in an unintended location.
- code-review-05: `cd $BACKUP_DIR` is the most dangerous line in the script.
- code-review-05: The script relies on nothing POSIX-incompatible.
- code-review-05: The `ls *.log` parsing bug exists independently of which shell is used.
- code-review-05: The suggested rewrite uses `cd "$BACKUP_DIR" || exit 1`.
- code-review-05: The suggested rewrite uses `rm -f -- *.tmp 2>/dev/null || true`.
- code-review-05: There should not be directories matching `*.tmp` to recurse into, and if there are, that needs explicit intent.
- code-review-06: When the override introduces a new dict value, `merged[key] = value` stores the override's dict object by reference rather than a copy.
- code-review-06: Only the paths that were recursively merged are new objects in the returned structure.
- code-review-06: `isinstance(merged[key], dict)` returns False for custom `Mapping` types that are not literally `dict`.
- code-review-06: Dict-like objects that are not `dict` instances fall back to full replacement instead of being merged.
- code-review-06: The code contains `if value is None: merged.pop(key, None)`.
- code-review-06: Using `None` to mean deletion is a common pattern in config merge/patch semantics, as in Kubernetes strategic merge and Helm.
- code-review-06: The function has no docstring and no type hints.
- code-review-07: The backoff formula does not match the exponential-backoff-from-first-retry pattern it appears to imitate.
- code-review-07: The backoff formula should probably be 2 ** i or 1000 * (i + 1).
- code-review-07: On the last loop iteration, a 429 still triggers the setTimeout wait before the loop exits.
- code-review-07: The wait on the final attempt is a pointless delay because the function returns undefined anyway.
- code-review-07: Accessing err.status on null or undefined throws a TypeError inside the catch block.
- code-review-07: The TypeError thrown inside the catch block is not caught anywhere in the function and propagates out uncaught.
- code-review-07: An uncaught TypeError breaks the implied contract that the function never throws.
- code-review-07: A suppressed error could silently produce a fail-open state if a caller uses the result for a permission or entitlement check.
- code-review-07: Network failures are the most common reason to want retry logic.
- code-review-07: The code does not respect a Retry-After header on 429 responses.
- code-review-07: 501 Not Implemented is a permanent condition, so retrying it is pure waste, unlike 502, 503, and 504.
- code-review-07: The silent swallowing of errors changes the function's error-handling contract invisibly to callers and could mask bugs and security-relevant failures.
- code-review-07: The backoff math, inconsistent return values, uncaught throw null edge case, and lack of retries for non-HTTP errors read like accumulated bugs rather than intentional behavior.
- code-review-08: `os.path.getmtime` works on directories.
- code-review-08: The `removed` count is lost on failure because it is never returned.
- code-review-08: `clean()` is never called in the snippet.
- code-review-08: As given, the script does nothing when executed directly, unless the snippet is truncated.
- code-review-08: The `tmp-` prefix and `.part` suffix are conventional naming for atomic writes (write to a temp name, then rename into place).
- code-review-08: The script deletes exports.
- debugging-01: The mismatch between the key "port" and the lookup cfg['Port'] raises a KeyError.
- debugging-02: Using an arrow function as the `setInterval` callback is the easiest fix.
- debugging-02: Calling `.bind(this)` on a regular function callback is an alternative fix that keeps a regular function.
- debugging-02: Capturing `this` in a variable beforehand, such as `const self = this;`, is another alternative fix.
- debugging-03: The corrected `moving_sum` function appends `sum(values[i : i + window])` for each index `i` in that range and returns the list of sums.
- debugging-04: The byte 0xc3 suggests UTF-8-encoded multi-byte characters, such as accented letters.
- debugging-04: errors="ignore" silently drops malformed bytes.
- debugging-04: errors="replace" preserves line structure.
- debugging-05: An alternative fix is to use tags=() and convert it to a list inside the function.
- debugging-05: Another alternative fix is to use a sentinel value.
- debugging-05: The None-default-plus-copy pattern is the standard idiom.
- debugging-06: The speaker intends to check whether actual project code is present in the working directory.
- debugging-06: Project code, if present, might reveal the connection pool configuration.
- debugging-06: The speaker will look for relevant code in the working directory before giving an answer.
- debugging-07: Checking whether the actual test code exists in the current directory would enable more concrete advice.
- debugging-07: A Bash tool call is issued with the command "find . -iname '*notification*' -o -iname 'conftest.py' 2>/dev/null | head -50".
- debugging-07: The Bash tool call's description is "Search for relevant test files".
- debugging-07: The command searches the current directory for files whose names match '*notification*' or are named 'conftest.py'.
- debugging-07: The command limits its output to the first 50 results via head -50.
- debugging-07: The command discards error output by redirecting stderr to /dev/null.
- debugging-08: Metrics libraries such as Prometheus clients and StatsD wrappers create a new time series per unique label value.
- debugging-08: Each metrics time series is retained forever in-process.
- debugging-08: Webhooks and marketing campaigns often carry unique or high-cardinality identifiers.
- debugging-08: If metrics registry size climbs monotonically and correlates with traffic, high-cardinality metrics labels are the culprit.
- debugging-08: Bounding a wrapper map does not bound memory if its values reference large objects containing additional maps.
- debugging-08: A second unbounded cache or index, such as a reverse-lookup index, may be built alongside the bounded cache.
- debugging-08: A native library for compression, TLS, or image processing may fail to return memory to the OS.
- debugging-08: The user currently has no heap profile insight.
- debugging-08: Plotting growth rate against request or webhook volume is cheap and requires no code changes.
- debugging-08: Adding cache entry-count and byte-size logging is cheap and isolates the cache question.
- debugging-08: A heap diff is the missing diagnostic and will immediately disambiguate the traffic-volume leak from the high-cardinality metrics cause.
- explanation-01: A hash map uses a hash function to turn a key into an array index called a bucket.
- explanation-01: A hash map's array has a fixed number of buckets.
- explanation-01: There is no limit to the number of possible keys a hash map may receive.
- explanation-01: The collection in a chaining bucket is usually a linked list, and sometimes a tree or dynamic array.
- explanation-01: Deletion under separate chaining is easy because you just remove the node from the list.
- explanation-01: Linear probing checks index+1, index+2, and so on.
- explanation-01: Open addressing implementations typically resize well before the array gets full, often at around 70% load.
- explanation-01: Deletion is simple under chaining and needs tombstones under open addressing.
- explanation-01: Rust's HashMap uses an open addressing variant.
- explanation-02: FOR UPDATE blocks any other transaction from reading or modifying that row until the locking transaction commits.
- explanation-03: TCP slow start also runs when a connection restarts after a pause.
- explanation-03: A network path may cross a fast local network and then a slow, congested link in the middle.
- explanation-03: The receive window reflects the receiver's buffer capacity.
- explanation-03: TCP respects whichever of the congestion window and receive window is smaller.
- explanation-03: Historically the initial cwnd was 1 segment.
- explanation-03: RFC 6928 specifies an initial window of 10 segments.
- explanation-03: ACKs only arrive if data is getting through successfully, so cwnd growth stalls when the network cannot keep up.
- explanation-03: Packet loss is detected via timeout or duplicate ACKs.
- explanation-03: ssthresh is often set from a previous congestion event.
- explanation-03: When cwnd reaches ssthresh, TCP switches to congestion avoidance as a precaution against repeating the same overshoot.
- explanation-04: A crash in one thread, such as a segfault, can bring down the entire process and all its other threads.
- explanation-04: Web servers and browsers run each tab or worker as a separate process so one bad request doesn't kill the whole server.
- explanation-04: Separate processes each get their own interpreter and GIL.
- explanation-04: Python's multiprocessing module is used for CPU-bound parallel computation.
- explanation-04: Per-process resource limits can be applied via cgroups or ulimits.
- explanation-04: Threads context-switch faster than processes.
- explanation-04: Threads are preferable when the risk of one task corrupting shared state is low or well-managed via locks or atomics.
- explanation-05: A memory leak in a garbage-collected language does not mean memory is lost as it is in C with unfreed malloc.
- explanation-05: Examples of long-lived collections include a global cache, a static Map, and a subscriber list.
- explanation-05: Examples of long-lived objects for listener registration include a DOM element, an event bus, and a global emitter.
- explanation-05: A listener closure often captures surrounding variables, including large objects.
- explanation-06: Slowness could be caused by writes, N+1 queries, network latency, unindexed queries, or application code.
- explanation-06: A cache used under write-heavy or low-repetition workloads becomes a layer that is frequently invalidated or missed.
- explanation-06: If the real bottleneck is a slow query such as one from a missing index, caching masks the symptom instead of fixing the cause.
- explanation-06: If the real bottleneck is slow network calls, caching masks the symptom instead of fixing the cause.
- explanation-06: The read/write ratio can be determined by checking logs or adding simple counters.
- explanation-06: Common database issues to check first include missing indexes, N+1 queries, and slow joins.
- explanation-06: Redis is an example of a cache that can be placed in front of a database.
- explanation-07: Machines with multiple terabytes of RAM/NVMe are routine.
- explanation-07: Sharding fixes throughput ceilings and total-size ceilings.
- explanation-07: Sharding does not fix slow queries.
- explanation-07: If the real problem is unindexed queries or lock contention, sharding will not help.
- explanation-07: Single-instance PostgreSQL limits are roughly multiple terabytes of data and tens of thousands of writes per second.
- explanation-07: A current database server usually has a lot of vertical scaling headroom before hardware cost or availability becomes a problem.
- explanation-07: Tenant ID and user ID are examples of natural shard keys.
- explanation-07: Sharding imposes permanent operational complexity, including a routing layer, rebalancing, cross-shard transactions and joins, harder migrations, and harder backups.
- explanation-07: Reactive sharding is a known, roughly one-time cost rather than an ongoing tax.
- explanation-07: The recommended approach is to scale vertically, add read replicas and caching, and instrument to track the actual growth rate.
- explanation-08: Request latency is composed of JSON serialization/deserialization plus network, database, and business logic time.
- explanation-08: Measuring what fraction of request latency comes from JSON serialization is roughly a five-minute profiling task.
- explanation-08: Binary formats such as Protobuf and MessagePack typically shrink payloads by 20-50% relative to JSON.
- explanation-08: Payload size reduction matters most when requests are large and network- or bandwidth-bound rather than CPU-bound.
- explanation-08: Smaller payloads help more on slow or mobile networks than on localhost or fast LANs.
- explanation-08: For CPU-bound serialization, binary formats typically run 2-10x faster than JSON.
- explanation-08: Migrating from JSON to a binary format carries meaningful costs including schemas, tooling, and debuggability tradeoffs.
- summarization-02: The rollback fixed the incident in about 27 minutes.
- summarization-03: Synchronous thumbnail generation currently adds up to 3 seconds per upload.
- summarization-04: Four clicks produce four error banners.
- summarization-05: Ada is assigned to run the payments database migration dry run.
- summarization-05: Ada's payments database migration dry run is due before Thursday.
- summarization-07: All findings other than the median latency drop, the memory increase, and the crash are still speculative.
- summarization-08: The abandonment during import is a real and actionable problem.
- summarization-08: The template gallery is a new feature.
- summarization-08: With only 8 participants, the prevalence and even the existence of the admin/regular-user split cannot be estimated.
- summarization-08: A targeted follow-up study is needed before prioritizing the admin/regular-user settings split.

Added facts (styled only):

- code-review-01: Exceptions should be allowed to propagate, or a specific exception should be caught.
- code-review-01: Letting exceptions propagate makes failures visible instead of hiding them behind a `True`/`False` return value.
- code-review-02: The corrected implementation awaits `res.json()` and returns `data.name.toUpperCase()`.
- code-review-03: A typo or bad caller input reaches the database without any feedback.
- code-review-03: The unhandled exception reaches the caller with no added context.
- code-review-04: The `reset` method has the same race condition issue as `increment`.
- code-review-04: In the fixed code, `Counter.__init__` initializes `self.value` to 0 and creates `self._lock` as a `threading.Lock`.
- code-review-04: In the fixed code, `increment` acquires `self._lock` before executing `self.value += 1`.
- code-review-04: In the fixed code, `reset` acquires `self._lock` before setting `self.value = 0`.
- code-review-06: The lack of cycle or depth protection was likely never considered rather than deliberate.
- code-review-06: If override[key] is {} and merged[key] is a dict, the result is merged[key] unchanged.
- code-review-06: If override[key] is {} and merged[key] is not a dict, merged[key] becomes {}.
- code-review-06: The empty-dict override behavior is inconsistent but a natural consequence of the branching and not obviously a bug.
- code-review-06: There is no validation that base or override are actually dicts.
- code-review-06: Passing a non-dict base fails at dict(base).
- code-review-06: Passing a non-dict override fails at .items().
- code-review-06: There is no defensive check or error message pointing at the actual cause of a non-dict argument failure.
- code-review-06: The None-deletes-key behavior is the one place where removing it could break something relying on the existing contract.
- code-review-07: Setting attempts = 0 skips the loop entirely.
- code-review-07: With attempts = 0 the function returns undefined without ever calling fn, a silent no-op.
- code-review-07: Treating 429 and 5xx as retryable and everything else as non-retryable is a reasonable, intentional retry policy for an HTTP client wrapper.
- code-review-07: The 1000ms multiplier as a crude backoff is intentional.
- code-review-07: Some caller is very likely already relying on or being silently broken by the return-value ambiguity.
- code-review-07: The return semantics should not be changed without first auditing call sites.
- code-review-08: `getmtime` raises `FileNotFoundError` on a broken symlink.
- code-review-08: `tmp-`/`.part` deletions always run first.
- code-review-08: The cutoff is 45 days, expressed as `86400 * 45`.
- code-review-08: The 45-day cutoff is undocumented and written as a bare arithmetic expression rather than a named constant or config value.
- code-review-08: Repeatedly hitting the 500-removal cap would indicate the backlog is growing faster than cleanup.
- code-review-08: There is no monitoring on the returned `removed` count.
- code-review-08: The script does not check that `ROOT` exists or is mounted before listing it.
- code-review-08: An unmounted mount point would appear as "nothing to clean" rather than raising an error.
- debugging-03: The iteration at `i=2` would produce `3+4=7`.
- debugging-06: The analytics service and the export job compete for a shared, finite pool of database connections.
- debugging-06: This shared-pool contention is the most likely cause of the failures.
- debugging-06: On some nights the analytics service runs long or heavy queries.
- debugging-06: When analytics runs long or heavy queries, it holds database connections longer.
- debugging-06: Analytics holding connections longer starves the export job.
- debugging-06: The export job's requests time out at 30 seconds.
- debugging-06: The batch number involved in the failures varies between failures.
- debugging-06: The varying batch number indicates the problem is not a bug in any specific batch.
- debugging-06: The failing batch is whichever batch happens to run during the contention window.
- debugging-06: The connection pool may be sized too small for the combined peak load of both services.
- debugging-06: Either service may have a connection leak in which connections are not released on error paths.
- debugging-06: A connection leak slowly shrinks the effective size of the pool.
- debugging-06: Analytics may run long transactions or table scans that cause lock contention.
- debugging-06: Lock contention from analytics can block writes and reads from the export job.
- debugging-06: Under lock contention, connections sit waiting instead of failing fast.
- debugging-06: A DB-side connection limit, separate from the application pool, may be being hit.
- debugging-06: If the DB-side connection limit is hit, even a well-sized application pool cannot obtain new connections.
- debugging-06: An export failure occurred on 2026-07-29 at approximately 02:14Z.
- debugging-06: There have been other nights on which the export job failed.
- debugging-06: The analytics service has logs and a schedule that can be pulled.
- debugging-06: If analytics jobs cluster right before each export failure, that confirms contention rather than a bug in the export job.
- debugging-06: PostgreSQL's `pg_stat_activity` view shows active and idle-in-transaction connections, long-running queries, and locks.
- debugging-06: A spike in connections from analytics coinciding with failures would be strong evidence of contention.
- debugging-06: Connection pools can be instrumented to log pool size, in-use count, and wait-queue depth on every checkout.
- debugging-06: Pool instrumentation converts an 'exhausted' signal into information about which service exhausted the pool.
- debugging-06: Connection leaks can be ruled out by comparing connections-opened versus connections-closed metrics over a week.
- debugging-06: A slow connection leak appears as a rising baseline rather than only nightly spikes.
- debugging-06: Databases have a `max_connections` setting.
- debugging-06: If `max_connections` is close to the sum of both services' pool sizes plus headroom, both a connection limit and contention could be at play.
- debugging-06: Pool metrics and DB-side activity data for two to three failures would be enough to distinguish contention from a leak from a hard connection-limit ceiling.
- debugging-07: If the API accepts an event write and returns before the write is durably visible to the digest query, the digest can run before all three events land.
- debugging-07: Async commit, eventual consistency, caching, or message queues can delay a write's visibility to a subsequent digest query.
- debugging-07: Serial local test runs are slow enough to avoid the write-visibility race.
- debugging-07: CI under load is not slow enough to avoid the write-visibility race.
- debugging-07: If the digest query isn't scoped to a unique run, user, or tenant ID, another parallel worker's cleanup can remove an event between seeding and the digest read.
- debugging-07: Worker cleanup can delete or truncate shared tables.
- debugging-07: A pooled database connection reused across workers or across setup and assertion can read stale data if the isolation level or transaction boundaries are wrong.
- debugging-07: If the digest filters by timestamp and event creation is fast, clock skew or truncated timestamps can push an event just outside the digest window.
- debugging-07: Timestamp-window problems are flakier under parallel load because of scheduling delays.
- debugging-07: A hardcoded sleep or retry count that is sufficient in serial runs can be too short when CI is CPU-starved by four workers.
- debugging-07: Running the suite with -n 4 (matching CI's worker count) repeatedly under CPU load simulates CI resource contention.
- debugging-07: pytest --count=50 or a shell loop can be used to run a test repeatedly.
- debugging-07: stress-ng can be run in the background to generate CPU load.
- debugging-07: If the test never fails alone but fails alongside other tests, the cause is cross-test contamination rather than raw timing.
- debugging-07: Logging the seeded event IDs and the digest-returned event IDs at assertion time reveals the actual missing-event pattern.
- debugging-07: Diagnostic logging added for this investigation should be temporary rather than permanent.
- debugging-07: CI does not keep artifacts on retry.
- debugging-07: pytest-rerunfailures or a custom retry with verbose logging enabled only on failure can capture diagnostic output on the next flake.
- debugging-07: A pytest-xdist group or marker can pin a specific test to a single worker so it runs serially.
- debugging-07: If failures stop when the test is pinned to serial execution, the cause is inter-worker contention rather than seed-to-digest timing.
- debugging-07: Missing awaits, fire-and-forget writes, or reliance on eventual consistency are often the root cause of 'N-1 events' style flakes.
- debugging-07: Search-index-backed and cache-backed digests are examples of eventual-consistency reliance.
- debugging-07: Replicating the failure locally under load is the fastest way to distinguish a timing cause from a shared-state cause.
- debugging-07: Reading the actual write and read code path often reveals the bug without needing to reproduce the failure.
- debugging-08: Traffic-correlated acceleration indicates a second, volume-driven leak in addition to the baseline leak.
- debugging-08: A volume-driven leak is likely in order processing itself.
- debugging-08: Heap snapshots can be captured with tools like jmap or node --heapsnapshot.
- debugging-08: Diffing heap snapshots taken a few hours apart under load reveals object counts that scale with request count rather than time.
- debugging-08: Background timers, scheduled jobs, connection pools that never shrink, and caches keyed by unbounded values leak even with zero webhook traffic.
- debugging-08: Running the canary with timers and schedulers active but zero external traffic tests for a traffic-independent leak.
- debugging-08: Disabling background jobs one at a time bisects a traffic-independent leak.
- debugging-08: Surviving quiet nights does not by itself prove a leak.
- debugging-08: Surviving quiet nights rules out a simple GC-timing artifact, because such an artifact would recover once traffic drops.
- debugging-08: Allocator fragmentation can arise from large, variably sized allocations such as long-lived buffers or strings.
- debugging-08: Campaign workloads can have large payload size variance.
- debugging-08: jemalloc and glibc malloc expose allocator/arena statistics.
- debugging-08: The cache is size-bounded by entry count rather than by memory.
- debugging-08: Growth in cache entry size would not explain the canary's growth unless the canary also warms the cache.
- debugging-08: Marketing campaigns can introduce many new or larger SKUs that are evicted and reallocated rapidly.
- debugging-08: Cache keys that never collide, such as keys accidentally including a timestamp or request ID, allow unbounded growth despite a stated bound.
- debugging-08: A heap snapshot diff settles whether the issue is a leak or fragmentation.
- debugging-08: The heap snapshot diff should be the first investigation step because it narrows almost every other hypothesis.
- explanation-01: Many C++ unordered_map alternatives use open addressing.
- explanation-03: The feedback loop of loss and retransmission can collapse the network's throughput.
- explanation-03: Congestion collapse events occurred on the early Internet in the mid-1980s.
- explanation-03: Those congestion collapse events led Van Jacobson to design slow start and the broader TCP congestion control algorithms.
- explanation-03: The initial congestion window was historically a few segments.
- explanation-04: Python and Ruby have a global interpreter lock.
- explanation-04: Python and Ruby threads cannot run bytecode in parallel; only one thread executes at a time.
- explanation-04: Separate processes can be restarted, scaled, or deployed independently.
- explanation-04: Independent process scaling and restart is the basis of microservices and of worker pools like Gunicorn and PM2.
- explanation-06: Caches introduce staleness bugs.
- explanation-06: API profiling can be done by adding timing logs or using an APM tool.
- explanation-06: Databases have a slow-query log that identifies the worst-performing queries.
- explanation-07: Most single-node Postgres limits are reached on CPU or IOPS during writes before disk capacity is exhausted.
- explanation-07: Vacuum and index maintenance slow down as tables grow.
- explanation-07: Slower vacuum and index maintenance cause latency spikes.
- explanation-07: Migration and schema-change windows get longer and riskier as data grows.
- explanation-07: Postgres has native table partitioning.
- explanation-07: Rebalancing shards later, if the chosen shard key turns out to be wrong, is a harder migration than the one being avoided.
- explanation-08: If JSON parsing is 5% of request time, a 10x faster codec saves 4.5% of overall request time.
- explanation-08: A 4.5% overall saving is not worth the cost of migrating serialization formats.
- explanation-08: If JSON parsing is 40% of request time, a 10x faster codec could nearly halve latency.
- explanation-08: Guessing at the answer risks dismissing a real performance win.
- explanation-08: Binary formats provide more benefit on large payloads with repeated structure.
- summarization-01: Cold start time was reduced by roughly 40%.
- summarization-02: Errors began at 09:14.
- summarization-02: The page fired at 09:21.
- summarization-02: The incident involved a 12% error rate.
- summarization-03: Upload latency is currently 800ms to 3s.
- summarization-03: A worker pool would generate the thumbnails and update the record.
- summarization-04: Repeated clicks on the export option queue multiple requests.
- summarization-04: The bug was reproduced by different users.
- summarization-06: The on-call engineer suspects connection-pool exhaustion in the payments client.
- summarization-07: All findings other than the median latency reduction are provisional.
- summarization-08: More data is needed before taking action on the template gallery.

### developer-docs

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 29 | 22 | 0.759 | 21 | 4 |
| code-review-02 | 20 | 16 | 0.8 | 20 | 0 |
| code-review-03 | 26 | 14 | 0.538 | 16 | 5 |
| code-review-04 | 19 | 0 | 0.0 | 8 | 8 |
| code-review-05 | 33 | 22 | 0.667 | 24 | 1 |
| code-review-06 | 25 | 18 | 0.72 | 22 | 7 |
| code-review-07 | 32 | 19 | 0.594 | 34 | 6 |
| code-review-08 | 35 | 23 | 0.657 | 40 | 13 |
| debugging-01 | 6 | 6 | 1.0 | 6 | 1 |
| debugging-02 | 17 | 13 | 0.765 | 11 | 0 |
| debugging-03 | 10 | 10 | 1.0 | 11 | 3 |
| debugging-04 | 12 | 10 | 0.833 | 18 | 4 |
| debugging-05 | 15 | 12 | 0.8 | 13 | 0 |
| debugging-06 | 3 | 0 | 0.0 | 33 | 33 |
| debugging-07 | 6 | 0 | 0.0 | 20 | 20 |
| debugging-08 | 30 | 13 | 0.433 | 36 | 19 |
| explanation-01 | 44 | 37 | 0.841 | 32 | 3 |
| explanation-02 | 29 | 24 | 0.828 | 27 | 1 |
| explanation-03 | 34 | 19 | 0.559 | 22 | 3 |
| explanation-04 | 30 | 21 | 0.7 | 32 | 1 |
| explanation-05 | 20 | 17 | 0.85 | 16 | 2 |
| explanation-06 | 17 | 8 | 0.471 | 13 | 2 |
| explanation-07 | 24 | 12 | 0.5 | 32 | 12 |
| explanation-08 | 12 | 6 | 0.5 | 19 | 5 |
| summarization-01 | 6 | 6 | 1.0 | 6 | 0 |
| summarization-02 | 12 | 9 | 0.75 | 14 | 5 |
| summarization-03 | 13 | 12 | 0.923 | 12 | 1 |
| summarization-04 | 14 | 13 | 0.929 | 13 | 1 |
| summarization-05 | 10 | 8 | 0.8 | 6 | 0 |
| summarization-06 | 14 | 13 | 0.929 | 12 | 1 |
| summarization-07 | 15 | 14 | 0.933 | 13 | 1 |
| summarization-08 | 17 | 17 | 1.0 | 19 | 1 |

Median fraction: 0.762 over 32 scored pairs.

Median additions: 2.5 over 32 scored pairs.

Lost facts:

- code-review-01: The function does not check that `roles` contains valid role values.
- code-review-01: The function has no duplicate-role protection.
- code-review-01: The function appends `"member"` even if `"member"` is already present in `roles`.
- code-review-01: Failure modes conflated by the boolean return include bad input, DB down, and duplicate entry.
- code-review-01: The suggested fix appends `"member"` only if it is not already in `roles`.
- code-review-01: The suggested fix catches `Exception` instead of using a bare `except:`.
- code-review-01: The suggested fix logs the failure with `logger.error` including the user name and exception.
- code-review-02: An `async` function returns a promise wrapping its return value.
- code-review-02: Without error handling, network failures and non-2xx responses are silently ignored.
- code-review-02: Assigning to an outer `let` variable inside `.then()` instead of chaining or returning is an anti-pattern.
- code-review-02: The outer-variable assignment pattern obscures the fact that the value is not ready when it is used.
- code-review-03: A caller-supplied value like `'; DROP TABLE orders; --` would execute as SQL.
- code-review-03: `%s` is the placeholder syntax for psycopg2 and MySQLdb.
- code-review-03: `?` is the placeholder syntax for sqlite3.
- code-review-03: The function performs no input validation.
- code-review-03: The function does not check that `status` is one of the expected enum values.
- code-review-03: The function does not check that `customer_name` is non-empty or of reasonable length.
- code-review-03: The function has no type hints.
- code-review-03: The function has no docstring.
- code-review-03: The `cursor` parameter and the return type are not documented.
- code-review-03: The lack of type hints and docstring makes the function's contract unclear to callers.
- code-review-03: The query has no `LIMIT` clause.
- code-review-03: Without a `LIMIT`, a broad match could return a huge number of rows.
- code-review-04: The class described is not thread-safe.
- code-review-04: The `increment` method performs a read-modify-write by reading `current = self.value` and then writing `self.value = current + 1`.
- code-review-04: A read-modify-write can lose an increment if two threads interleave between the read and the write.
- code-review-04: If two threads both read a value of 5 and both write 6, the result is 6 instead of the correct 7.
- code-review-04: The class has no `Lock` or `RLock` guarding access to `self.value`.
- code-review-04: Without synchronization, `increment` and `reset` can race against each other.
- code-review-04: A `reset` can occur between another thread's read and write in `increment`.
- code-review-04: CPython has a Global Interpreter Lock (GIL).
- code-review-04: CPython's GIL prevents literal byte-level memory corruption.
- code-review-04: CPython's GIL does not make `current = self.value; self.value = current + 1` atomic as a whole.
- code-review-04: The sequence `current = self.value; self.value = current + 1` compiles to multiple bytecode operations.
- code-review-04: A thread switch can happen between the bytecode operations of a read-modify-write.
- code-review-04: The class exposes `self.value` directly and provides no accessor method.
- code-review-04: External code reading `counter.value` while another thread is mid-increment can observe inconsistent or stale state.
- code-review-04: Python's `threading` module provides a `Lock`.
- code-review-04: Using `with self._lock:` around `self._value += 1` makes the increment safe.
- code-review-04: Exposing `value` as a property that acquires the lock before returning `_value` provides a safe read.
- code-review-04: Guarding every read and write of `_value` with the same lock prevents lost increments.
- code-review-04: Guarding every read and write of `_value` with the same lock ensures reads always see a consistent value.
- code-review-05: If `$1` is empty, `cd $BACKUP_DIR` becomes `cd` with no arguments.
- code-review-05: `cd` with no arguments changes to `$HOME`.
- code-review-05: `rm -rf *.tmp` is a broad, silent recursive delete with no confirmation.
- code-review-05: The script has no `set -e`, `set -u`, or error handling.
- code-review-05: The script does not stop on failure and does not error on unset variables.
- code-review-05: The script relies on nothing POSIX-incompatible.
- code-review-05: The `ls *.log` parsing bug exists independently of which shell is used.
- code-review-05: The suggested rewrite uses `set -eu`.
- code-review-05: The suggested rewrite uses `rm -f -- *.tmp 2>/dev/null || true`.
- code-review-05: The suggested rewrite calls `gzip -- "$f"`.
- code-review-05: There should not be directories matching `*.tmp` to recurse into, and if there are, that needs explicit intent.
- code-review-06: When the override introduces a new dict value, `merged[key] = value` stores the override's dict object by reference rather than a copy.
- code-review-06: `isinstance(merged[key], dict)` returns False for custom `Mapping` types that are not literally `dict`.
- code-review-06: Dict-like objects that are not `dict` instances fall back to full replacement instead of being merged.
- code-review-06: Using `None` to mean deletion is a common pattern in config merge/patch semantics, as in Kubernetes strategic merge and Helm.
- code-review-06: The function has no docstring and no type hints.
- code-review-06: The `None`-deletes-key behavior is undiscoverable without reading the source.
- code-review-06: The `None`-deletion and list-replacement behaviors are policy decisions requiring confirmation from someone who knows the config schema.
- code-review-07: The backoff formula should probably be 2 ** i or 1000 * (i + 1).
- code-review-07: On the last loop iteration, a 429 still triggers the setTimeout wait before the loop exits.
- code-review-07: The wait on the final attempt is a pointless delay because the function returns undefined anyway.
- code-review-07: Accessing err.status on null or undefined throws a TypeError inside the catch block.
- code-review-07: The TypeError thrown inside the catch block is not caught anywhere in the function and propagates out uncaught.
- code-review-07: An uncaught TypeError breaks the implied contract that the function never throws.
- code-review-07: A suppressed error could silently produce a fail-open state if a caller uses the result for a permission or entitlement check.
- code-review-07: Network failures are the most common reason to want retry logic.
- code-review-07: The backoff has no cap or ceiling.
- code-review-07: The code does not respect a Retry-After header on 429 responses.
- code-review-07: 501 Not Implemented is a permanent condition, so retrying it is pure waste, unlike 502, 503, and 504.
- code-review-07: The silent swallowing of errors changes the function's error-handling contract invisibly to callers and could mask bugs and security-relevant failures.
- code-review-07: The backoff math, inconsistent return values, uncaught throw null edge case, and lack of retries for non-HTTP errors read like accumulated bugs rather than intentional behavior.
- code-review-08: The `removed` count is lost on failure because it is never returned.
- code-review-08: The age-based deletion and the tmp/`.part` deletion are two unrelated criteria sharing one counter.
- code-review-08: In that case the age-based cleanup silently stops early for that run with no logging to explain why.
- code-review-08: The interaction between the two deletion branches is non-deterministic across runs.
- code-review-08: `clean()` is never called in the snippet.
- code-review-08: As given, the script does nothing when executed directly, unless the snippet is truncated.
- code-review-08: The `tmp-` prefix and `.part` suffix are conventional naming for atomic writes (write to a temp name, then rename into place).
- code-review-08: The script can delete a file mid-write if another process is actively producing it under a tmp-/`.part` name.
- code-review-08: This race condition could corrupt or silently drop an in-flight export.
- code-review-08: The 45-day cutoff is plausibly a retention policy decision.
- code-review-08: The script deletes exports.
- code-review-08: The 500 cap limits blast radius if the `CUTOFF` logic broke and flagged everything as stale.
- debugging-02: Code defined inside a `class` body runs in strict mode.
- debugging-02: Accessing `this.seconds` when `this` is `undefined` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: The user's environment is treating the callback as non-strict, for example because it is transpiled or run outside a strict context.
- debugging-02: Using an arrow function as the `setInterval` callback is the easiest fix.
- debugging-04: Under an ascii encoding, any byte greater than or equal to 0x80 causes an error.
- debugging-04: errors="ignore" silently drops malformed bytes.
- debugging-05: An alternative fix is to use tags=() and convert it to a list inside the function.
- debugging-05: Another alternative fix is to use a sentinel value.
- debugging-05: The None-default-plus-copy pattern is the standard idiom.
- debugging-06: The speaker intends to check whether actual project code is present in the working directory.
- debugging-06: Project code, if present, might reveal the connection pool configuration.
- debugging-06: The speaker will look for relevant code in the working directory before giving an answer.
- debugging-07: Checking whether the actual test code exists in the current directory would enable more concrete advice.
- debugging-07: A Bash tool call is issued with the command "find . -iname '*notification*' -o -iname 'conftest.py' 2>/dev/null | head -50".
- debugging-07: The Bash tool call's description is "Search for relevant test files".
- debugging-07: The command searches the current directory for files whose names match '*notification*' or are named 'conftest.py'.
- debugging-07: The command limits its output to the first 50 results via head -50.
- debugging-07: The command discards error output by redirecting stderr to /dev/null.
- debugging-08: Metrics libraries such as Prometheus clients and StatsD wrappers create a new time series per unique label value.
- debugging-08: Each metrics time series is retained forever in-process.
- debugging-08: Webhooks and marketing campaigns often carry unique or high-cardinality identifiers.
- debugging-08: If metrics registry size climbs monotonically and correlates with traffic, high-cardinality metrics labels are the culprit.
- debugging-08: A custom LRU eviction policy can have bugs that prevent eviction under certain access patterns.
- debugging-08: Bounding a wrapper map does not bound memory if its values reference large objects containing additional maps.
- debugging-08: If cache entry count grows past the configured bound, the eviction logic is broken.
- debugging-08: Native or off-heap memory such as JIT, GC arenas, and network buffers can cause growth instead of leaked managed objects.
- debugging-08: Memory growth that survives quiet nights is consistent with allocator fragmentation.
- debugging-08: A native library for compression, TLS, or image processing may fail to return memory to the OS.
- debugging-08: Native memory growth does not appear in a heap profile of managed objects.
- debugging-08: If RSS grows while the runtime's heap-used metric stays flat or sawtooth, the growth is native memory.
- debugging-08: If RSS does not drop after forcing a full GC, the memory is not GC-reachable garbage.
- debugging-08: glibc malloc arena behavior can retain memory that is not returned to the OS.
- debugging-08: Plotting growth rate against request or webhook volume is cheap and requires no code changes.
- debugging-08: Comparing RSS against the runtime heap metric isolates managed versus native memory.
- debugging-08: A heap diff is the missing diagnostic and will immediately disambiguate the traffic-volume leak from the high-cardinality metrics cause.
- explanation-01: A hash map's array has a fixed number of buckets.
- explanation-01: There is no limit to the number of possible keys a hash map may receive.
- explanation-01: The collection in a chaining bucket is usually a linked list, and sometimes a tree or dynamic array.
- explanation-01: Separate chaining is simple to implement and reason about.
- explanation-01: In the worst case, with many collisions in one bucket, chaining degrades to O(n) lookup within that bucket because the list must be scanned.
- explanation-01: Quadratic probing and double hashing are other probing variants.
- explanation-01: Rust's HashMap uses an open addressing variant.
- explanation-02: Optimistic locking does not lock anything.
- explanation-02: FOR UPDATE blocks any other transaction from reading or modifying that row until the locking transaction commits.
- explanation-02: Inventory decrement on checkout is an example of a fit for pessimistic locking.
- explanation-02: Optimistic locking fits cases with long think time between read and write, such as a user editing a form for minutes.
- explanation-02: Optimistic locking fits distributed or web systems where holding a database lock across a network round-trip or user interaction is impractical.
- explanation-03: TCP slow start also runs when a connection restarts after a pause.
- explanation-03: A network path may cross a fast local network and then a slow, congested link in the middle.
- explanation-03: Dropped packets cause retransmissions, wasted bandwidth, and cascading congestion.
- explanation-03: The congestion window limits how much unacknowledged data the sender may have in flight at once.
- explanation-03: The congestion window is separate from the receive window.
- explanation-03: The receive window reflects the receiver's buffer capacity.
- explanation-03: TCP respects whichever of the congestion window and receive window is smaller.
- explanation-03: Historically the initial cwnd was 1 segment.
- explanation-03: Modern implementations often start with a higher initial cwnd, such as 10 segments.
- explanation-03: RFC 6928 specifies an initial window of 10 segments.
- explanation-03: Each time the sender receives an acknowledgment for data it sent, it increases cwnd by roughly one segment.
- explanation-03: Packet loss is detected via timeout or duplicate ACKs.
- explanation-03: After detecting loss, TCP backs off and shifts into the congestion avoidance phase.
- explanation-03: In congestion avoidance, cwnd grows linearly instead of exponentially.
- explanation-03: ssthresh stands for slow start threshold.
- explanation-04: Each thread has its own stack and instruction pointer.
- explanation-04: Web servers and browsers run each tab or worker as a separate process so one bad request doesn't kill the whole server.
- explanation-04: In runtimes with a global interpreter lock, threads help with I/O-bound work but not CPU-bound work.
- explanation-04: Python's multiprocessing module is used for CPU-bound parallel computation.
- explanation-04: Processes can be sandboxed independently with different users, capabilities, and memory protections.
- explanation-04: Per-process resource limits can be applied via cgroups or ulimits.
- explanation-04: Independent process lifecycle management is useful for worker pools where a hung or leaking worker should be recycled.
- explanation-04: Threads context-switch faster than processes.
- explanation-04: Threads are a natural fit for I/O-bound concurrency within a single trusted program.
- explanation-05: Examples of long-lived collections include a global cache, a static Map, and a subscriber list.
- explanation-05: Examples of long-lived objects for listener registration include a DOM element, an event bus, and a global emitter.
- explanation-05: A listener closure often captures surrounding variables, including large objects.
- explanation-06: A cache only helps if the slowness comes from repeated reads of the same data hitting the database.
- explanation-06: Slowness could be caused by writes, N+1 queries, network latency, unindexed queries, or application code.
- explanation-06: A cache would not fix slowness caused by writes, N+1 queries, network latency, unindexed queries, or application code.
- explanation-06: If every read is for different or unique data, a cache will not help much.
- explanation-06: A cache used under write-heavy or low-repetition workloads becomes a layer that is frequently invalidated or missed.
- explanation-06: If the real bottleneck is a slow query such as one from a missing index, caching masks the symptom instead of fixing the cause.
- explanation-06: The read/write ratio can be determined by checking logs or adding simple counters.
- explanation-06: Common database issues to check first include missing indexes, N+1 queries, and slow joins.
- explanation-06: Redis is an example of a cache that can be placed in front of a database.
- explanation-07: Machines with multiple terabytes of RAM/NVMe are routine.
- explanation-07: Sharding fixes throughput ceilings and total-size ceilings.
- explanation-07: Sharding does not fix slow queries.
- explanation-07: If the real problem is unindexed queries or lock contention, sharding will not help.
- explanation-07: Growth rate can be estimated by measuring growth over the last 3-6 months and extrapolating.
- explanation-07: Single-instance PostgreSQL limits are roughly multiple terabytes of data and tens of thousands of writes per second.
- explanation-07: Sharding imposes permanent operational complexity, including a routing layer, rebalancing, cross-shard transactions and joins, harder migrations, and harder backups.
- explanation-07: Premature sharding is a classic way to slow a team down for years.
- explanation-07: The anticipated load that motivates premature sharding may never fully materialize.
- explanation-07: Reactive sharding is a known, roughly one-time cost rather than an ongoing tax.
- explanation-07: The costs of sharding too early versus too late are asymmetric.
- explanation-07: The recommended approach is to scale vertically, add read replicas and caching, and instrument to track the actual growth rate.
- explanation-08: Request latency is composed of JSON serialization/deserialization plus network, database, and business logic time.
- explanation-08: Measuring what fraction of request latency comes from JSON serialization is roughly a five-minute profiling task.
- explanation-08: Binary formats such as Protobuf and MessagePack typically shrink payloads by 20-50% relative to JSON.
- explanation-08: Payload size reduction matters most when requests are large and network- or bandwidth-bound rather than CPU-bound.
- explanation-08: Smaller payloads help more on slow or mobile networks than on localhost or fast LANs.
- explanation-08: For CPU-bound serialization, binary formats typically run 2-10x faster than JSON.
- summarization-02: The similarity of the config templates directly caused the incident.
- summarization-02: The response after paging was efficient.
- summarization-02: The main lever for improvement is prevention rather than the incident response process.
- summarization-03: Synchronous thumbnail generation currently strains web workers.
- summarization-04: Four clicks produce four error banners.
- summarization-05: Ada is assigned to confirm with the mobile team's lead whether they have been informed of the API deprecation.
- summarization-05: There is an API deprecation that the mobile team's lead may not have been informed of.
- summarization-06: The leading theory for the outage is connection-pool exhaustion in the payments client.
- summarization-07: All findings other than the median latency drop, the memory increase, and the crash are still speculative.

Added facts (styled only):

- code-review-01: The function does not validate that `db` supports `insert`.
- code-review-01: The function has no type hints or docstring.
- code-review-01: Without type hints or a docstring, the expected types of `name`, `roles`, and `db` are not documented.
- code-review-01: The corrected version lets exceptions propagate so the caller can see what went wrong.
- code-review-03: The function has one critical problem and two design issues.
- code-review-03: An attacker can inject a UNION SELECT to read arbitrary tables.
- code-review-03: With parameterized queries, the database driver handles escaping.
- code-review-03: Placeholder syntax varies by database driver and can be %s, ?, or :name.
- code-review-03: The correct placeholder syntax is documented in the database driver's documentation.
- code-review-04: The assistant is checking memory for relevant prior guidance.
- code-review-04: The assistant invokes a bash tool.
- code-review-04: The bash command runs `cat` on a MEMORY.md file.
- code-review-04: The MEMORY.md file is located at /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-r_e4snvc/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-it57otsa/memory/MEMORY.md
- code-review-04: The command redirects error output to /dev/null.
- code-review-04: The command echoes 'no memory file' if the cat command fails.
- code-review-04: The bash tool call's description is 'Check memory index'.
- code-review-04: MEMORY.md serves as the memory index.
- code-review-05: A single failed `gzip` does not stop the script or get reported, so partial failures pass silently.
- code-review-06: The intended behavior is to merge when both sides are dicts and replace otherwise.
- code-review-06: In that case `merged["outer"]` is set to the literal dict `{"inner": None}`, storing the deletion sentinel as a real value.
- code-review-06: Deletion via `None` only works when the target key already exists in `base` as a dict.
- code-review-06: The recursive branch does create new dicts for merged keys, so the aliasing bug only appears for untouched nested structures.
- code-review-06: The silent no-op on missing keys hides typos, so `{"colour": None}` against a base using `"color"` does nothing without warning.
- code-review-06: The recommended pre-change tests cover nested dict merge, `None` deletion for existing and missing keys, `None` deletion inside a not-yet-existing nested key, and a dict-vs-scalar type mismatch.
- code-review-06: The type-mismatch crash and the `None`-leak case are the two issues the author would fix regardless.
- code-review-07: The function performs no input validation.
- code-review-07: An attempts value of 0 or a negative number skips the loop entirely.
- code-review-07: With attempts of 0 or negative, the function returns undefined without ever calling fn.
- code-review-07: Some old codebases use null as a 'no result' sentinel instead of exceptions.
- code-review-07: Before changing the behavior, one should check whether any caller relies on catching a thrown error versus checking for null.
- code-review-07: A safer contract is to retry only on retryable status codes with consistent, jittered backoff.
- code-review-08: `os.path.getmtime` raises `FileNotFoundError` on a broken symlink.
- code-review-08: Because `os.listdir` order is not guaranteed, a crash results in a different, unpredictable subset of files being cleaned each time.
- code-review-08: The script has no lock or overlap protection.
- code-review-08: If a run takes longer than the schedule interval, two instances can run concurrently, race on the same files, and crash each other.
- code-review-08: `os.listdir` raises `FileNotFoundError` if the directory does not exist.
- code-review-08: Failing loudly on a missing `ROOT` might be intentional.
- code-review-08: Bypassing the age check for temp files is plausibly by design because leftover temp files may be safe to remove regardless of age.
- code-review-08: The intentional bypass of the age check is not documented in a comment.
- code-review-08: The magic numbers are examples of unrecorded rationale the user previously flagged.
- code-review-08: If nobody can explain the values, that suggests they were tuned once for a specific incident and never documented.
- code-review-08: The recommended first steps are adding logging of every removed path and a dry-run flag.
- code-review-08: Adding logging and a dry-run flag costs little and gives visibility to investigate the rest safely.
- code-review-08: Fixing the cap inconsistency and the directory-crash bug are the two highest-priority changes after visibility is added.
- debugging-01: The key name that needs to be fixed is on line 4.
- debugging-03: The window starting at index 2 is `[3, 4]`.
- debugging-03: The sum of the window `[3, 4]` is 7.
- debugging-03: The corrected `moving_sum([1, 2, 3, 4], 2)` returns `[3, 5, 7]`.
- debugging-04: errors="replace" silently changes the file's content.
- debugging-04: errors="replace" should only be used if exact byte fidelity does not matter.
- debugging-04: Latin-1 and UTF-16 are other possible file encodings.
- debugging-04: The `file` tool can be used to inspect a file's encoding.
- debugging-06: The export job and the analytics service compete for the same connection pool.
- debugging-06: On some nights the combined load of the export job and analytics service exceeds the connection pool size.
- debugging-06: Analytics can run long queries at unpredictable times.
- debugging-06: The export job may leak connections that it does not release.
- debugging-06: The failures occur at a random batch number.
- debugging-06: The failures occur at a weekly frequency.
- debugging-06: A random failing batch number with weekly frequency indicates load-dependent contention rather than a fixed data problem.
- debugging-06: A bug tied to specific data would fail at the same batch every time.
- debugging-06: The error message reported is 'Pool exhausted, waited 30s'.
- debugging-06: The 'Pool exhausted, waited 30s' error means all pool connections were in use for the full timeout window.
- debugging-06: Pool exhaustion happens when demand outpaces the pool size.
- debugging-06: Pool exhaustion happens when connections are held too long.
- debugging-06: Pool exhaustion happens when connections leak and never return to the pool.
- debugging-06: The database is shared with analytics.
- debugging-06: Analytics jobs often run ad hoc or on their own schedule.
- debugging-06: An overlapping analytics query can silently consume pool capacity during the export window.
- debugging-06: The database may be briefly under load from locking, replication lag, autovacuum, or a backup job, slowing queries enough to hold connections longer than usual.
- debugging-06: A retry storm can occur when requests that wait 30 seconds are retried, adding concurrent demand and extending the exhaustion.
- debugging-06: The pool size may have been set for a smaller worker count and never scaled as the job grew.
- debugging-06: Connection pool metrics include active, idle, and waiting connection counts.
- debugging-06: Failures coinciding with a spike in active connections indicate a capacity or leak issue.
- debugging-06: Failures clustering around analytics job runs would confirm contention.
- debugging-06: The database server has a slow-query log.
- debugging-06: The failures occur around 02:14.
- debugging-06: Long-running queries around the failure window indicate a shared-database bottleneck rather than a pool-size problem.
- debugging-06: A connection leak can be caused by an exception raised before a 'finally' block or context-manager cleanup runs.
- debugging-06: A connection leak explains why a failure is intermittent and grows worse over the course of a run.
- debugging-06: If pool usage regularly approaches the pool limit, undersizing is likely and tips over on nights when analytics also spikes.
- debugging-06: Running the export job in staging with a reduced pool size while replaying typical analytics query load can reproduce the error and confirm contention as the mechanism.
- debugging-06: The appropriate fix for undersizing is to increase the pool or isolate pools per service.
- debugging-06: The appropriate fix for a leak is to fix the connection-release path.
- debugging-06: The appropriate fix for cross-service contention is to add backoff or priority so the nightly export does not compete directly with analytics traffic.
- debugging-06: The export job runs nightly.
- debugging-07: The test failure only appears when running with four parallel workers and never appears when running serially.
- debugging-07: If a digest query filters by a time window or a shared table without per-test scoping, another worker's events can leak into or out of the count.
- debugging-07: A test isolation gap under parallel workers is the most likely cause among those listed.
- debugging-07: If a seed step returns before events are fully committed or indexed, the digest read can observe a state containing only 2 of the 3 events.
- debugging-07: Asynchronous writes, message queues, search indexes, and caches are mechanisms that can delay event visibility after seeding returns.
- debugging-07: Higher CI concurrency increases contention and makes the seed-versus-read race window more likely to trigger.
- debugging-07: If a digest window is bound to 'today' or a rolling period, a test running near a boundary such as midnight UTC can drop an event.
- debugging-07: Time-based flakiness is unlikely here because it would not correlate with worker count.
- debugging-07: CI machines running four workers are often CPU- or I/O-constrained.
- debugging-07: A slow write can silently fail or time out and surface only as a missing event.
- debugging-07: No error is surfaced for the failure because the test only asserts the event count.
- debugging-07: pytest-xdist provides each worker with a `worker_id`.
- debugging-07: The CI system retains no artifacts from test runs.
- debugging-07: If the failure appears only at `-n 4` and not at `-n 1`, that confirms an isolation or contention issue and rules out pure time-boundary flakiness.
- debugging-07: Wrapping the assertion in a harness that dumps event IDs, timestamps, and worker ID on failure converts an artifact-less failure into a usable data point.
- debugging-07: If adding an explicit wait or poll for '3 events indexed' before calling the digest endpoint drops the failure rate to zero, that confirms the seed/read race as the cause.
- debugging-07: Reproducing the parallel setup on a developer machine will not perfectly match CI hardware.
- debugging-07: Local stress testing can surface isolation bugs even without CI's resource pressure.
- debugging-07: Running the suite serially and then at four workers for 20-30 runs each is a cheap check that yields an answer within an hour.
- debugging-07: A concurrency bug and a time-boundary bug require very different investigation paths.
- debugging-08: Two candidate causes fit the evidence.
- debugging-08: One line of evidence rules out a third candidate cause.
- debugging-08: A bounded cache should plateau in size once it fills.
- debugging-08: After a bounded cache fills, its size does not correlate with request volume.
- debugging-08: Connection or response objects retained by a queue are a possible source of per-request retention.
- debugging-08: Webhook handling adds its own leak on top of a baseline leak.
- debugging-08: Per-webhook state such as parsed payloads, per-callback closures, and retry or dedup tracking may not be cleaned up on all code paths, including error paths.
- debugging-08: If eviction removes a map key but an index, listener, or promise still holds the value, the object survives garbage collection.
- debugging-08: A pure 'bounded cache reached its limit' explanation is inconsistent with two observations.
- debugging-08: A full cache would not grow faster under more load.
- debugging-08: Memory growth never plateaus.
- debugging-08: Growing collections indexed by request or user ID would appear as the largest delta in a retained-size heap diff.
- debugging-08: Comparing the canary's heap growth rate against a twin instance with webhooks enabled and marketing traffic held constant isolates webhook-specific growth.
- debugging-08: If the growth gap between canary and twin matches webhook volume, the leak is in webhook handling specifically.
- debugging-08: Reference counting or a FinalizationRegistry on cache values can confirm whether evicted entries are actually collected.
- debugging-08: Production profiling is not currently available.
- debugging-08: A local heap profiler can be attached now.
- debugging-08: Replaying the same requests locally with a heap profiler shows growth with no drop after garbage collection if a leak exists.
- debugging-08: A heap diff on a loaded instance is the fastest way to identify which object type is accumulating.
- explanation-01: Insertion under chaining is O(1) on average.
- explanation-01: Lookup under chaining stays close to O(1) on average if the list stays short.
- explanation-01: Quadratic probing jumps by increasing steps.
- explanation-02: In a funds transfer, the transaction locks both account rows before making changes.
- explanation-03: The problem of queues overflowing and packets dropping is called congestion collapse.
- explanation-03: Congestion collapse was common on the early internet before congestion control existed.
- explanation-03: Slow start, along with the rest of TCP's congestion control, was designed to prevent congestion collapse.
- explanation-04: Processes are preferable to threads for CPU-bound workloads on machines with many cores.
- explanation-05: Examples of garbage collection roots include global variables, active stack frames, and static references.
- explanation-05: A cache keyed by user session that never evicts old sessions retains every session object for the life of the program.
- explanation-06: A cache targeted at specific slow queries or endpoints is more effective than a general cache.
- explanation-06: Success means being able to point to a specific measurement and confirm that a cache would reduce that time.
- explanation-07: Nothing is stored in memory about this database or the product team's plans.
- explanation-07: The answer given is general guidance rather than tailored advice.
- explanation-07: The product team should be asked for a rough monthly write volume or an expected user-count trajectory instead of a final size.
- explanation-07: A single PostgreSQL instance often hits write-throughput or connection limits before it hits storage limits.
- explanation-07: The team's capacity to maintain sharding should be confirmed before committing to it.
- explanation-07: Sharding now locks in a partition key before real query patterns are understood.
- explanation-07: Changing a partition key later requires a full data migration.
- explanation-07: Under sharding, simple analytics and reporting queries that were a single scan require a fan-out and merge step.
- explanation-07: Query and vacuum performance can degrade before it is noticed, especially on large tables without proper indexing or partitioning.
- explanation-07: A hard ceiling on write throughput may be hit before a ceiling on storage.
- explanation-07: Native table partitioning by date or tenant speeds up queries and vacuum without adding shards.
- explanation-07: The recommended next step is to ask the product team for expected write volume or user growth over the next 12 months.
- explanation-08: Payload size and structure determine how much a binary format actually saves.
- explanation-08: Binary formats save the most on numeric and repetitive data.
- explanation-08: Binary formats save less on payloads dominated by strings.
- explanation-08: Prototyping a binary format against a payload sample allows measuring encode and decode time and size.
- explanation-08: Multiplying the measured serialization share by the prototype's speedup gives an estimate of the overall request-time improvement.
- summarization-02: Staging intentionally runs with smaller configuration values.
- summarization-02: Errors started at 09:14 UTC.
- summarization-02: The errors affected 12% of checkout requests.
- summarization-02: The page went out at 09:21.
- summarization-02: The rollback completed at 09:48 UTC.
- summarization-03: Moving thumbnail generation out of the upload path and into a background queue removes 800ms to 3 seconds of delay from each upload request.
- summarization-04: The issue is not browser-specific.
- summarization-06: The on-call engineer suspects connection-pool exhaustion in the payments client.
- summarization-07: Two effects need more investigation before the results can be trusted.
- summarization-08: The report recommends prioritizing the progress bar fix.

### plain-language

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 29 | 23 | 0.793 | 15 | 1 |
| code-review-02 | 20 | 15 | 0.75 | 27 | 1 |
| code-review-03 | 26 | 19 | 0.731 | 18 | 5 |
| code-review-04 | 19 | 11 | 0.579 | 17 | 4 |
| code-review-05 | 33 | 23 | 0.697 | 27 | 6 |
| code-review-06 | 25 | 16 | 0.64 | 36 | 8 |
| code-review-07 | 32 | 20 | 0.625 | 36 | 7 |
| code-review-08 | 35 | 26 | 0.743 | 26 | 2 |
| debugging-01 | 6 | 6 | 1.0 | 10 | 3 |
| debugging-02 | 17 | 14 | 0.824 | 18 | 1 |
| debugging-03 | 10 | 10 | 1.0 | 11 | 2 |
| debugging-04 | 12 | 7 | 0.583 | 14 | 2 |
| debugging-05 | 15 | 11 | 0.733 | 14 | 1 |
| debugging-06 | 3 | 0 | 0.0 | 28 | 28 |
| debugging-07 | 6 | 0 | 0.0 | 25 | 25 |
| debugging-08 | 30 | 15 | 0.5 | 31 | 13 |
| explanation-01 | 44 | 30 | 0.682 | 22 | 1 |
| explanation-02 | 29 | 21 | 0.724 | 27 | 2 |
| explanation-03 | 34 | 21 | 0.618 | 23 | 2 |
| explanation-04 | 30 | 20 | 0.667 | 30 | 2 |
| explanation-05 | 20 | 16 | 0.8 | 18 | 5 |
| explanation-06 | 17 | 9 | 0.529 | 23 | 4 |
| explanation-07 | 24 | 16 | 0.667 | 25 | 12 |
| explanation-08 | 12 | 9 | 0.75 | 20 | 5 |
| summarization-01 | 6 | 6 | 1.0 | 5 | 0 |
| summarization-02 | 12 | 6 | 0.5 | 19 | 4 |
| summarization-03 | 13 | 13 | 1.0 | 14 | 1 |
| summarization-04 | 14 | 12 | 0.857 | 10 | 0 |
| summarization-05 | 10 | 8 | 0.8 | 11 | 1 |
| summarization-06 | 14 | 13 | 0.929 | 13 | 1 |
| summarization-07 | 15 | 15 | 1.0 | 13 | 2 |
| summarization-08 | 17 | 15 | 0.882 | 17 | 3 |

Median fraction: 0.732 over 32 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: The function does not check that `roles` contains valid role values.
- code-review-01: The function has no duplicate-role protection.
- code-review-01: The function appends `"member"` even if `"member"` is already present in `roles`.
- code-review-01: Failure modes conflated by the boolean return include bad input, DB down, and duplicate entry.
- code-review-01: The suggested fix appends `"member"` only if it is not already in `roles`.
- code-review-01: The suggested fix catches `Exception` instead of using a bare `except:`.
- code-review-02: An `async` function returns a promise wrapping its return value.
- code-review-02: A throw inside an async function body produces a rejected promise rather than an exception thrown at the call site.
- code-review-02: Calling `.json()` on an error response such as a 404 HTML page will likely throw a JSON parse error.
- code-review-02: Calling `.json()` on an error response may alternatively succeed and yield an unexpected error payload.
- code-review-02: The outer-variable assignment pattern obscures the fact that the value is not ready when it is used.
- code-review-03: The function does not check that `status` is one of the expected enum values.
- code-review-03: The function has no type hints.
- code-review-03: The function has no docstring.
- code-review-03: The `cursor` parameter and the return type are not documented.
- code-review-03: The lack of type hints and docstring makes the function's contract unclear to callers.
- code-review-03: The query has no `LIMIT` clause.
- code-review-03: Without a `LIMIT`, a broad match could return a huge number of rows.
- code-review-04: CPython has a Global Interpreter Lock (GIL).
- code-review-04: CPython's GIL prevents literal byte-level memory corruption.
- code-review-04: CPython's GIL does not make `current = self.value; self.value = current + 1` atomic as a whole.
- code-review-04: The sequence `current = self.value; self.value = current + 1` compiles to multiple bytecode operations.
- code-review-04: A thread switch can happen between the bytecode operations of a read-modify-write.
- code-review-04: External code reading `counter.value` while another thread is mid-increment can observe inconsistent or stale state.
- code-review-04: Exposing `value` as a property that acquires the lock before returning `_value` provides a safe read.
- code-review-04: Guarding every read and write of `_value` with the same lock ensures reads always see a consistent value.
- code-review-05: If no `.tmp` files exist and globbing is not nullglob-safe, `*.tmp` is passed literally to `rm -rf`, which errors out.
- code-review-05: `rm -rf *.tmp` is a broad, silent recursive delete with no confirmation.
- code-review-05: If no `.log` files exist, `*.log` is passed literally as a nonexistent filename to `gzip`, causing an error.
- code-review-05: The script relies on nothing POSIX-incompatible.
- code-review-05: The `ls *.log` parsing bug exists independently of which shell is used.
- code-review-05: The suggested rewrite exits with status 1 and prints a usage message to stderr if `$BACKUP_DIR` is empty or not a directory.
- code-review-05: The suggested rewrite uses `cd "$BACKUP_DIR" || exit 1`.
- code-review-05: The suggested rewrite uses `rm -f -- *.tmp 2>/dev/null || true`.
- code-review-05: The suggested rewrite calls `gzip -- "$f"`.
- code-review-05: There should not be directories matching `*.tmp` to recurse into, and if there are, that needs explicit intent.
- code-review-06: When the override introduces a new dict value, `merged[key] = value` stores the override's dict object by reference rather than a copy.
- code-review-06: Only the paths that were recursively merged are new objects in the returned structure.
- code-review-06: `isinstance(merged[key], dict)` returns False for custom `Mapping` types that are not literally `dict`.
- code-review-06: Dict-like objects that are not `dict` instances fall back to full replacement instead of being merged.
- code-review-06: The code contains `if value is None: merged.pop(key, None)`.
- code-review-06: Using `None` to mean deletion is a common pattern in config merge/patch semantics, as in Kubernetes strategic merge and Helm.
- code-review-06: A self-referential `base` dict would cause infinite recursion.
- code-review-06: The function has no docstring and no type hints.
- code-review-06: The `None`-deletion and list-replacement behaviors are policy decisions requiring confirmation from someone who knows the config schema.
- code-review-07: On the last loop iteration, a 429 still triggers the setTimeout wait before the loop exits.
- code-review-07: The wait on the final attempt is a pointless delay because the function returns undefined anyway.
- code-review-07: Accessing err.status on null or undefined throws a TypeError inside the catch block.
- code-review-07: The TypeError thrown inside the catch block is not caught anywhere in the function and propagates out uncaught.
- code-review-07: An uncaught TypeError breaks the implied contract that the function never throws.
- code-review-07: The blanket catch-and-suppress hides programming bugs, not just transient failures.
- code-review-07: A suppressed error could silently produce a fail-open state if a caller uses the result for a permission or entitlement check.
- code-review-07: Network failures are the most common reason to want retry logic.
- code-review-07: The code does not respect a Retry-After header on 429 responses.
- code-review-07: 501 Not Implemented is a permanent condition, so retrying it is pure waste, unlike 502, 503, and 504.
- code-review-07: The silent swallowing of errors changes the function's error-handling contract invisibly to callers and could mask bugs and security-relevant failures.
- code-review-07: The backoff math, inconsistent return values, uncaught throw null edge case, and lack of retries for non-HTTP errors read like accumulated bugs rather than intentional behavior.
- code-review-08: `os.path.getmtime` works on directories.
- code-review-08: If `ROOT` contains a subdirectory, the run crashes mid-loop with no cleanup of state.
- code-review-08: The `removed` count is lost on failure because it is never returned.
- code-review-08: The interaction between the two deletion branches is non-deterministic across runs.
- code-review-08: `clean()` is never called in the snippet.
- code-review-08: As given, the script does nothing when executed directly, unless the snippet is truncated.
- code-review-08: The `tmp-` prefix and `.part` suffix are conventional naming for atomic writes (write to a temp name, then rename into place).
- code-review-08: The age-based branch was designed with safety in mind, as evidenced by the 500 cap.
- code-review-08: The script deletes exports.
- debugging-02: Code defined inside a `class` body runs in strict mode.
- debugging-02: Accessing `this.seconds` when `this` is `undefined` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: The user's environment is treating the callback as non-strict, for example because it is transpiled or run outside a strict context.
- debugging-04: Under an ascii encoding, any byte greater than or equal to 0x80 causes an error.
- debugging-04: If the encoding is not reliably UTF-8, one option is to detect it.
- debugging-04: chardet and charset-normalizer are libraries that can detect a file's encoding.
- debugging-04: errors="ignore" silently drops malformed bytes.
- debugging-04: errors="replace" preserves line structure.
- debugging-05: The fixed code defines make_post(title, tags=None) and sets tags = list(DEFAULT_TAGS) when tags is None.
- debugging-05: An alternative fix is to use tags=() and convert it to a list inside the function.
- debugging-05: Another alternative fix is to use a sentinel value.
- debugging-05: The None-default-plus-copy pattern is the standard idiom.
- debugging-06: The speaker intends to check whether actual project code is present in the working directory.
- debugging-06: Project code, if present, might reveal the connection pool configuration.
- debugging-06: The speaker will look for relevant code in the working directory before giving an answer.
- debugging-07: Checking whether the actual test code exists in the current directory would enable more concrete advice.
- debugging-07: A Bash tool call is issued with the command "find . -iname '*notification*' -o -iname 'conftest.py' 2>/dev/null | head -50".
- debugging-07: The Bash tool call's description is "Search for relevant test files".
- debugging-07: The command searches the current directory for files whose names match '*notification*' or are named 'conftest.py'.
- debugging-07: The command limits its output to the first 50 results via head -50.
- debugging-07: The command discards error output by redirecting stderr to /dev/null.
- debugging-08: Marketing campaigns increase traffic, which increases the rate of memory growth.
- debugging-08: If the growth rate versus request rate is roughly linear, the leak is traffic-correlated.
- debugging-08: A custom LRU eviction policy can have bugs that prevent eviction under certain access patterns.
- debugging-08: A second unbounded cache or index, such as a reverse-lookup index, may be built alongside the bounded cache.
- debugging-08: If cache entry count grows past the configured bound, the eviction logic is broken.
- debugging-08: Native or off-heap memory such as JIT, GC arenas, and network buffers can cause growth instead of leaked managed objects.
- debugging-08: Memory growth that survives quiet nights is consistent with allocator fragmentation.
- debugging-08: A native library for compression, TLS, or image processing may fail to return memory to the OS.
- debugging-08: Native memory growth does not appear in a heap profile of managed objects.
- debugging-08: The user currently has no heap profile insight.
- debugging-08: If RSS grows while the runtime's heap-used metric stays flat or sawtooth, the growth is native memory.
- debugging-08: If RSS does not drop after forcing a full GC, the memory is not GC-reachable garbage.
- debugging-08: glibc malloc arena behavior can retain memory that is not returned to the OS.
- debugging-08: Plotting growth rate against request or webhook volume is cheap and requires no code changes.
- debugging-08: Comparing RSS against the runtime heap metric isolates managed versus native memory.
- explanation-01: A hash map's array has a fixed number of buckets.
- explanation-01: There is no limit to the number of possible keys a hash map may receive.
- explanation-01: The collection in a chaining bucket is usually a linked list, and sometimes a tree or dynamic array.
- explanation-01: Separate chaining is simple to implement and reason about.
- explanation-01: Deletion under separate chaining is easy because you just remove the node from the list.
- explanation-01: In the worst case, with many collisions in one bucket, chaining degrades to O(n) lookup within that bucket because the list must be scanned.
- explanation-01: Quadratic probing and double hashing are other probing variants.
- explanation-01: Open addressing implementations typically resize well before the array gets full, often at around 70% load.
- explanation-01: Deletion under open addressing is trickier because emptying a slot might break the probe chain for a later key.
- explanation-01: Deletion under open addressing usually requires a special tombstone marker instead of a true empty slot.
- explanation-01: Under high load, chaining degrades gracefully while open addressing degrades sharply and needs resizing.
- explanation-01: Deletion is simple under chaining and needs tombstones under open addressing.
- explanation-01: Chaining is simpler and more forgiving when the load factor is unpredictable.
- explanation-01: Rust's HashMap uses an open addressing variant.
- explanation-02: SELECT ... FOR UPDATE locks the selected row.
- explanation-02: FOR UPDATE blocks any other transaction from reading or modifying that row until the locking transaction commits.
- explanation-02: Using FOR UPDATE on a bank transfer prevents another transfer from racing against it.
- explanation-02: An optimistic update can be written as an UPDATE with a WHERE clause matching both the id and the previously read version.
- explanation-02: If an optimistic update affects 0 rows, someone else updated the record first, and the caller should reload and retry.
- explanation-02: Pessimistic locking fits cases where retries are expensive or unsafe.
- explanation-02: Inventory decrement on checkout is an example of a fit for pessimistic locking.
- explanation-02: Optimistic locking fits distributed or web systems where holding a database lock across a network round-trip or user interaction is impractical.
- explanation-03: TCP slow start also runs when a connection restarts after a pause.
- explanation-03: A network path may cross a fast local network and then a slow, congested link in the middle.
- explanation-03: Dropped packets cause retransmissions, wasted bandwidth, and cascading congestion.
- explanation-03: Congestion from one connection can degrade the network for everyone sharing that link.
- explanation-03: The congestion window is separate from the receive window.
- explanation-03: The receive window reflects the receiver's buffer capacity.
- explanation-03: TCP respects whichever of the congestion window and receive window is smaller.
- explanation-03: RFC 6928 specifies an initial window of 10 segments.
- explanation-03: ACKs only arrive if data is getting through successfully, so cwnd growth stalls when the network cannot keep up.
- explanation-03: Packet loss is detected via timeout or duplicate ACKs.
- explanation-03: After detecting loss, TCP backs off and shifts into the congestion avoidance phase.
- explanation-03: In congestion avoidance, cwnd grows linearly instead of exponentially.
- explanation-03: ssthresh is often set from a previous congestion event.
- explanation-04: A process has its own memory address space, file descriptors, and OS-level resources.
- explanation-04: Each thread has its own stack and instruction pointer.
- explanation-04: Web servers and browsers run each tab or worker as a separate process so one bad request doesn't kill the whole server.
- explanation-04: In runtimes with a global interpreter lock, threads help with I/O-bound work but not CPU-bound work.
- explanation-04: Separate processes each get their own interpreter and GIL.
- explanation-04: Python's multiprocessing module is used for CPU-bound parallel computation.
- explanation-04: Processes can be sandboxed independently with different users, capabilities, and memory protections.
- explanation-04: Per-process resource limits can be applied via cgroups or ulimits.
- explanation-04: Threads context-switch faster than processes.
- explanation-04: Threads are a natural fit for I/O-bound concurrency within a single trusted program.
- explanation-05: A memory leak in a garbage-collected language does not mean memory is lost as it is in C with unfreed malloc.
- explanation-05: Examples of long-lived collections include a global cache, a static Map, and a subscriber list.
- explanation-05: Examples of long-lived objects for listener registration include a DOM element, an event bus, and a global emitter.
- explanation-05: A listener closure often captures surrounding variables, including large objects.
- explanation-06: A cache only helps if the slowness comes from repeated reads of the same data hitting the database.
- explanation-06: Slowness could be caused by writes, N+1 queries, network latency, unindexed queries, or application code.
- explanation-06: A cache would not fix slowness caused by writes, N+1 queries, network latency, unindexed queries, or application code.
- explanation-06: If every read is for different or unique data, a cache will not help much.
- explanation-06: A cache used under write-heavy or low-repetition workloads becomes a layer that is frequently invalidated or missed.
- explanation-06: The read/write ratio can be determined by checking logs or adding simple counters.
- explanation-06: Common database issues to check first include missing indexes, N+1 queries, and slow joins.
- explanation-06: Redis is an example of a cache that can be placed in front of a database.
- explanation-07: Machines with multiple terabytes of RAM/NVMe are routine.
- explanation-07: Sharding does not fix slow queries.
- explanation-07: If the real problem is unindexed queries or lock contention, sharding will not help.
- explanation-07: Growth rate can be estimated by measuring growth over the last 3-6 months and extrapolating.
- explanation-07: Single-instance PostgreSQL limits are roughly multiple terabytes of data and tens of thousands of writes per second.
- explanation-07: Reactive sharding is a known, roughly one-time cost rather than an ongoing tax.
- explanation-07: The costs of sharding too early versus too late are asymmetric.
- explanation-07: The recommended approach is to scale vertically, add read replicas and caching, and instrument to track the actual growth rate.
- explanation-08: Measuring what fraction of request latency comes from JSON serialization is roughly a five-minute profiling task.
- explanation-08: Payload size reduction matters most when requests are large and network- or bandwidth-bound rather than CPU-bound.
- explanation-08: Smaller payloads help more on slow or mobile networks than on localhost or fast LANs.
- summarization-02: The similarity of the config templates directly caused the incident.
- summarization-02: Detection-to-resolution time for the incident was 34 minutes.
- summarization-02: Paging took 7 minutes.
- summarization-02: The rollback fixed the incident in about 27 minutes.
- summarization-02: The response after paging was efficient.
- summarization-02: The main lever for improvement is prevention rather than the incident response process.
- summarization-04: After triggering the PDF export, nothing happens initially.
- summarization-04: Four clicks produce four error banners.
- summarization-05: Ada is assigned to confirm with the mobile team's lead whether they have been informed of the API deprecation.
- summarization-05: There is an API deprecation that the mobile team's lead may not have been informed of.
- summarization-06: Connection-pool exhaustion and a retry storm are the leading hypotheses for the outage.
- summarization-08: With only 8 participants, the prevalence and even the existence of the admin/regular-user split cannot be estimated.
- summarization-08: A targeted follow-up study is needed before prioritizing the admin/regular-user settings split.

Added facts (styled only):

- code-review-01: Catching a specific exception, such as the database library's own error type, is the better approach.
- code-review-02: Mixing `.then()` with `async`/`await` causes the bug in which `profile` is used before it is set.
- code-review-03: Setting `status` to `' OR '1'='1` would make the query return every order instead of only orders with that status.
- code-review-03: `%s` is the parameter placeholder for drivers such as `psycopg2` and `mysql-connector`.
- code-review-03: If `customer_name` or `status` is `None`, the string concatenation raises a `TypeError` before the query runs.
- code-review-03: Fixing the SQL injection with parameterized queries also eliminates the `None` problem.
- code-review-03: The database driver handles `None` values correctly instead of concatenating them into a string.
- code-review-04: The Counter class's methods run from several threads at once.
- code-review-04: The fixed `Counter.__init__` sets `self.value = 0` and creates `self._lock = threading.Lock()`.
- code-review-04: The fixed `increment()` performs `self.value += 1` inside `with self._lock`.
- code-review-04: The fixed `reset()` sets `self.value = 0` inside `with self._lock`.
- code-review-05: If no .log files exist, ls prints an error the user never sees.
- code-review-05: The script's gzip call has no -f flag.
- code-review-05: If a .log.gz file already exists, gzip may stop and ask for confirmation.
- code-review-05: A gzip confirmation prompt will hang the script when it is not run interactively.
- code-review-05: If gzip fails on one file, the script keeps going and still prints "Cleaned" even though the cleanup was not fully successful.
- code-review-05: gzip -f avoids the interactive prompt.
- code-review-06: The memory directory was checked for relevant context before the review.
- code-review-06: There was no relevant memory content for this task.
- code-review-06: Type mismatches during the merge are silently allowed.
- code-review-06: If merged[key] is a dictionary but the override value is not, the code takes the else branch and replaces the dictionary outright.
- code-review-06: If override or a nested dictionary inside it contains a circular reference, merge_settings recurses forever and raises RecursionError.
- code-review-06: merge_settings performs no input validation.
- code-review-06: Passing non-dictionary-like arguments fails with a possibly confusing error message.
- code-review-06: Lack of input validation is standard for internal helper functions.
- code-review-07: The function retries forever on some paths without limit.
- code-review-07: The function should be treated as unsafe until fixed.
- code-review-07: The `1000 * i` 429 backoff looks like an intentional, if crude, attempt at rate-limit backoff.
- code-review-07: Immediate retry on 5xx is more likely an oversight because it is inconsistent with the 429 handling directly above it.
- code-review-07: Given unknown callers, the behavior should not be changed blindly.
- code-review-07: A passing test documenting current behavior, including the `undefined` and `null` returns, should be added first.
- code-review-07: The team should decide whether callers actually rely on `null` or `undefined` as sentinels before the error-handling shape is changed.
- code-review-08: The script does not sort directory entries, so it will likely fail on the same entry on every run
- code-review-08: os.listdir raises an unhandled exception if ROOT does not exist or permissions are wrong
- debugging-01: The config dictionary is {"host": "localhost", "port": 8080}.
- debugging-01: The function get_url returns the f-string "http://{cfg['host']}:{cfg['port']}/api".
- debugging-01: The fixed code prints http://localhost:8080/api.
- debugging-02: The arrow function is the most common fix in modern JavaScript.
- debugging-03: The code misses the last window, [3,4].
- debugging-03: moving_sum([1, 2, 3, 4], 2) prints [3, 5, 7].
- debugging-04: The byte 0xc3 occurs at position 512 in the file.
- debugging-04: UTF-8 covers ASCII.
- debugging-05: The user's test calls tags.append("post").
- debugging-06: The error is a connection pool timeout.
- debugging-06: Worker-3 waited 30 seconds for a free database connection and never got one.
- debugging-06: The export job shares its database with an analytics service.
- debugging-06: The most likely cause is that the analytics service is holding too many connections during the export job's window, preventing the export job from getting one.
- debugging-06: The export job's connection pool may be undersized for its peak concurrency.
- debugging-06: Batch sizes or parallelism may vary from night to night.
- debugging-06: A slow analytics query can hold a connection for a long time and starve other requests.
- debugging-06: A leaked connection that is never returned to the pool can hold a connection for a long time.
- debugging-06: If a code path opens a connection but fails to release it on error, the pool slowly shrinks until it runs dry.
- debugging-06: Connection leaks would explain why the failure does not happen every night.
- debugging-06: Connection leaks would explain why the failure does not hit the same batch number, since it depends on how many leaks happened earlier in the run.
- debugging-06: If the database has a max connection limit lower than the sum of both services' pools, contention will vary based on the analytics service's schedule.
- debugging-06: The failure occurred on 2026-07-29 around 02:14 UTC.
- debugging-06: The analytics service's logs or job schedule can be pulled for the time of the failure.
- debugging-06: If the analytics service was running a heavy query at the time of the failure, that is a strong signal.
- debugging-06: Most databases, including Postgres and MySQL, let you query active connections and their age.
- debugging-06: Postgres provides pg_stat_activity for querying connection information.
- debugging-06: Long-running or idle-in-transaction connections held by the analytics service can be identified via database-side connection metrics.
- debugging-06: Pool telemetry can be added to the export job by logging active, idle, and waiting connection counts on every checkout.
- debugging-06: Logging pool counts turns 'pool exhausted' from a mystery into a graph that can be inspected after the next failure.
- debugging-06: Every code path, including error and retry paths, should return connections to the pool.
- debugging-06: A connection leak often only shows up after several batches.
- debugging-06: A leak showing up after several batches matches the varying batch number in the reported failures.
- debugging-06: An alert can be set for when pool wait time crosses a threshold well below 30 seconds.
- debugging-06: Alerting below the timeout threshold catches the buildup before the job times out.
- debugging-06: The failure occurs weekly.
- debugging-06: Giving the export job a dedicated pool or dedicated database replica would prevent the analytics service from starving it.
- debugging-06: Using a dedicated pool is often simpler and more reliable than tuning both services' pool sizes to coexist.
- debugging-07: The test fails only in CI, not on the user's machine.
- debugging-07: CI runs four workers in parallel.
- debugging-07: The user's local machine runs one worker.
- debugging-07: Failing only under parallel CI points to a shared-state or timing problem that appears only under concurrency.
- debugging-07: Test isolation failure is the most likely cause of the flaky test.
- debugging-07: If the digest reads from a shared table, queue, or in-memory store without filtering by test run or user ID, another worker's test can insert or delete an event concurrently.
- debugging-07: The test observes 2 events instead of the expected 3.
- debugging-07: A stray fourth event could push one event out of a size limit.
- debugging-07: One of the three events could have been deleted or not yet committed at read time.
- debugging-07: The test seeds three events through the API and then reads the digest.
- debugging-07: Asynchronous seeding (background job, message queue, read replica, or delayed cache) can let the digest request run before all three writes settle.
- debugging-07: Write/read races get worse under load because workers competing for CPU or database connections widen the timing window.
- debugging-07: A digest size limit such as 'last N events' could trim events.
- debugging-07: Dedup by timestamp with limited resolution could cause events created close together to collide.
- debugging-07: A shared connection pool, ID sequence, or test database not reset per worker can let one worker's transaction leak into another's read.
- debugging-07: CI keeps no artifacts from the failing runs.
- debugging-07: Running the suite with a parallel flag such as `-n 4` locally, in a loop of 50-100 runs, can reproduce the concurrency failure.
- debugging-07: Reproducing the failure locally allows debugging with full logs instead of waiting for CI.
- debugging-07: Printing the actual event list (IDs, timestamps, worker ID) on assertion failure turns the next CI failure into useful evidence.
- debugging-07: Giving the test its own dedicated user, tenant, or namespace prevents other workers' events from appearing in its digest.
- debugging-07: If flakiness disappears after isolating the test, cross-test contamination is confirmed.
- debugging-07: Replacing a fixed `sleep()` with a poll that waits until the API confirms all three events exist addresses asynchronous seeding.
- debugging-07: Running only copies of the test with `-k test_digest_contains_all_events` under 4 workers rules out interference from unrelated tests.
- debugging-07: The name of the failing test is test_digest_contains_all_events.
- debugging-07: Reproducing locally with parallel workers in a loop will indicate whether the bug is a concurrency bug or something else.
- debugging-08: The pattern is not caused by garbage collection behavior or cache sizing.
- debugging-08: If the growth were uncollected garbage, quiet hours would give the collector time to reclaim it.
- debugging-08: Something is holding a live reference to objects that should have been released.
- debugging-08: A common bug is that eviction removes the map entry while a listener or parent object still points to the evicted object.
- debugging-08: In that pattern, entries are added on webhook receipt but removed only on the happy path.
- debugging-08: Timeouts, retries, or errors leave map entries behind.
- debugging-08: Every insertion should have a matching removal on all code paths, including error and timeout paths.
- debugging-08: Candidate sources of traffic-driven baseline leaks include connection pools, session objects, thread-local storage, and queued work items.
- debugging-08: Running a canary with zero traffic tests whether the baseline leak is traffic-driven.
- debugging-08: If memory stays flat with zero traffic, the baseline leak is traffic-driven.
- debugging-08: If memory still grows with zero traffic, the leak is tied to something that runs on a timer regardless of traffic.
- debugging-08: Taking two heap histograms of object counts by class a few hours apart during a quiet night and diffing them is the fastest way to pin down the leak.
- debugging-08: The heap histogram diff turns the four hypotheses into a directed search instead of guesswork.
- explanation-01: Chaining's performance stays steady even when the map is nearly full.
- explanation-02: A rejected save lets you review the new changes before retrying.
- explanation-02: Optimistic locking scales better than pessimistic locking.
- explanation-03: After detecting loss, the sender often restarts a milder version of slow start or drops into congestion avoidance, depending on the TCP variant.
- explanation-03: A connection's throughput often looks like a sawtooth: it climbs, hits a ceiling, drops back after loss, then climbs again.
- explanation-04: Separate processes can be restarted, monitored, or moved to another machine on their own.
- explanation-04: Separate processes fit well with process managers and container systems.
- explanation-05: A program with a memory leak uses more and more memory over time.
- explanation-05: Increasing memory use from a leak can slow a program down.
- explanation-05: Increasing memory use from a leak can crash a program.
- explanation-05: A program cannot use memory that has no active reference pointing to it.
- explanation-05: A garbage collector only follows references it is given.
- explanation-06: A cache won't fix sending too much data per request.
- explanation-06: You can profile by adding timing around each stage of a request, such as database queries, external calls, and business logic.
- explanation-06: A cache adds work on writes because every write must also update or clear the cache.
- explanation-06: Mistakes in updating or clearing the cache on writes cause stale data or bugs.
- explanation-07: Databases usually hit limits on write throughput, working set versus memory, or disk size before disk space alone matters.
- explanation-07: Write throughput limits appear as maxed-out CPU or I/O on inserts and updates.
- explanation-07: When the active working set no longer fits in RAM, cache hit rates drop and queries slow down.
- explanation-07: Disk size becomes a limit when data approaches what a single machine or the cloud provider's largest instance can hold.
- explanation-07: Vertical scaling options include more CPU, more RAM, faster disks, and read replicas.
- explanation-07: Choosing the wrong shard key can require re-sharding if usage patterns shift.
- explanation-07: Re-sharding is a painful, high-risk migration.
- explanation-07: After sharding, backups, migrations, monitoring, and failover happen per shard instead of once.
- explanation-07: Migrating 2 TB to a sharded setup is much more disruptive than migrating 500 GB.
- explanation-07: Relevant monitoring signals are disk usage, cache hit ratio, and write latency.
- explanation-07: Partitioning splits large tables within the same instance.
- explanation-07: Partitioning is a cheaper scaling option for very large tables.
- explanation-08: Binary formats reduce payload size because they skip field names and use compact encodings.
- explanation-08: Binary parsing is faster because binary decoding skips text parsing.
- explanation-08: The gains from binary formats apply only to the serialization step.
- explanation-08: If serialization is a large share of total request time, switching to a binary format is worth it.
- explanation-08: Measurements will indicate which binary format to choose and how much benefit to expect.
- summarization-02: The undersized connection pool could not handle the production load.
- summarization-02: About 12% of checkout requests failed during the incident.
- summarization-02: The failures lasted 34 minutes.
- summarization-02: The outage window was 09:14 to 09:48 UTC.
- summarization-03: Generating thumbnails during upload adds 800ms to 3 seconds to each request.
- summarization-05: The listed items are action items from Monday's sprint planning.
- summarization-06: The on-call engineer suspects the payments client's connection pool ran out of connections.
- summarization-07: The new request batcher was tested against the current one on the staging cluster.
- summarization-07: More testing is needed to rule either crash cause in or out.
- summarization-08: The progress bar issue may be a perception problem rather than a real one.
- summarization-08: The progress bar finding is tentative and needs more testing.
- summarization-08: The template gallery observation needs more research before it can be called a finding.

### technical-simplified

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 29 | 24 | 0.828 | 18 | 0 |
| code-review-02 | 20 | 14 | 0.7 | 14 | 0 |
| code-review-03 | 26 | 9 | 0.346 | 17 | 3 |
| code-review-04 | 19 | 11 | 0.579 | 16 | 1 |
| code-review-05 | 33 | 19 | 0.576 | 32 | 1 |
| code-review-06 | 25 | 16 | 0.64 | 25 | 10 |
| code-review-07 | 32 | 18 | 0.562 | 38 | 12 |
| code-review-08 | 35 | 24 | 0.686 | 44 | 6 |
| debugging-01 | 6 | 6 | 1.0 | 7 | 2 |
| debugging-02 | 17 | 10 | 0.588 | 12 | 0 |
| debugging-03 | 10 | 10 | 1.0 | 9 | 0 |
| debugging-04 | 12 | 8 | 0.667 | 10 | 0 |
| debugging-05 | 15 | 12 | 0.8 | 14 | 2 |
| debugging-06 | 3 | 0 | 0.0 | 19 | 19 |
| debugging-07 | 6 | 0 | 0.0 | 26 | 26 |
| debugging-08 | 30 | 16 | 0.533 | 35 | 16 |
| explanation-02 | 29 | 23 | 0.793 | 19 | 1 |
| explanation-03 | 34 | 19 | 0.559 | 20 | 1 |
| explanation-04 | 30 | 15 | 0.5 | 25 | 2 |
| explanation-05 | 20 | 17 | 0.85 | 13 | 1 |
| explanation-06 | 17 | 11 | 0.647 | 18 | 3 |
| explanation-07 | 24 | 15 | 0.625 | 34 | 11 |
| explanation-08 | 12 | 0 | 0.0 | 3 | 2 |
| summarization-01 | 6 | 5 | 0.833 | 5 | 1 |
| summarization-02 | 12 | 9 | 0.75 | 8 | 1 |
| summarization-03 | 13 | 13 | 1.0 | 13 | 2 |
| summarization-04 | 14 | 13 | 0.929 | 9 | 0 |
| summarization-05 | 10 | 8 | 0.8 | 9 | 0 |
| summarization-07 | 15 | 15 | 1.0 | 16 | 1 |

Median fraction: 0.667 over 29 scored pairs.

Median additions: 1 over 29 scored pairs.

Lost facts:

- code-review-01: The function does not check that `roles` contains valid role values.
- code-review-01: The function has no duplicate-role protection.
- code-review-01: The function appends `"member"` even if `"member"` is already present in `roles`.
- code-review-01: Failure modes conflated by the boolean return include bad input, DB down, and duplicate entry.
- code-review-01: The suggested fix appends `"member"` only if it is not already in `roles`.
- code-review-02: An `async` function returns a promise wrapping its return value.
- code-review-02: A throw inside an async function body produces a rejected promise rather than an exception thrown at the call site.
- code-review-02: Calling `.json()` on an error response such as a 404 HTML page will likely throw a JSON parse error.
- code-review-02: Calling `.json()` on an error response may alternatively succeed and yield an unexpected error payload.
- code-review-02: Assigning to an outer `let` variable inside `.then()` instead of chaining or returning is an anti-pattern.
- code-review-02: The outer-variable assignment pattern obscures the fact that the value is not ready when it is used.
- code-review-03: A caller-supplied value like `x' OR '1'='1` would execute as SQL.
- code-review-03: A caller-supplied value like `'; DROP TABLE orders; --` would execute as SQL.
- code-review-03: The SQL injection issue is critical.
- code-review-03: `%s` is the placeholder syntax for psycopg2 and MySQLdb.
- code-review-03: `?` is the placeholder syntax for sqlite3.
- code-review-03: The function performs no input validation.
- code-review-03: The function does not check that `customer_name` is non-empty or of reasonable length.
- code-review-03: The function has no error handling.
- code-review-03: A failed query, such as from a bad connection or lock timeout, will raise an uncaught exception.
- code-review-03: The function has no type hints.
- code-review-03: The function has no docstring.
- code-review-03: The `cursor` parameter and the return type are not documented.
- code-review-03: The lack of type hints and docstring makes the function's contract unclear to callers.
- code-review-03: The query has no `LIMIT` clause.
- code-review-03: Without a `LIMIT`, a broad match could return a huge number of rows.
- code-review-03: The SQL injection is the issue to fix immediately.
- code-review-03: The issues other than SQL injection are secondary polish.
- code-review-04: CPython has a Global Interpreter Lock (GIL).
- code-review-04: CPython's GIL prevents literal byte-level memory corruption.
- code-review-04: CPython's GIL does not make `current = self.value; self.value = current + 1` atomic as a whole.
- code-review-04: The sequence `current = self.value; self.value = current + 1` compiles to multiple bytecode operations.
- code-review-04: A thread switch can happen between the bytecode operations of a read-modify-write.
- code-review-04: External code reading `counter.value` while another thread is mid-increment can observe inconsistent or stale state.
- code-review-04: Exposing `value` as a property that acquires the lock before returning `_value` provides a safe read.
- code-review-04: Guarding every read and write of `_value` with the same lock ensures reads always see a consistent value.
- code-review-05: In the script, `BACKUP_DIR=$1` is unquoted and has no validation.
- code-review-05: Unquoted `cd $BACKUP_DIR` is subject to word-splitting and globbing.
- code-review-05: `rm -rf *.tmp` is a broad, silent recursive delete with no confirmation.
- code-review-05: `gzip $f` uses an unquoted variable, carrying word-splitting and glob risk.
- code-review-05: The script uses the `#!/bin/sh` shebang.
- code-review-05: The script relies on nothing POSIX-incompatible.
- code-review-05: The `ls *.log` parsing bug exists independently of which shell is used.
- code-review-05: The suggested rewrite uses `set -eu`.
- code-review-05: The suggested rewrite exits with status 1 and prints a usage message to stderr if `$BACKUP_DIR` is empty or not a directory.
- code-review-05: The suggested rewrite uses `rm -f -- *.tmp 2>/dev/null || true`.
- code-review-05: The suggested rewrite loops over `*.log` and skips entries that do not exist with `[ -e "$f" ] || continue`.
- code-review-05: The suggested rewrite calls `gzip -- "$f"`.
- code-review-05: The key fixes are validating and quoting `$BACKUP_DIR`, checking `cd` succeeds before destructive operations, using `rm -f` instead of `rm -rf`, guarding against literal globs with no matches, and dropping the `ls`.
- code-review-05: There should not be directories matching `*.tmp` to recurse into, and if there are, that needs explicit intent.
- code-review-06: The recursive-merge branch checks only `isinstance(merged[key], dict)`.
- code-review-06: The code never checks whether the override value is also a dict before recursing.
- code-review-06: Merging base `{"db": {"host": "a"}}` with override `{"db": "disabled"}` raises `AttributeError: 'str' object has no attribute 'items'`.
- code-review-06: `merge_settings` crashes when a dict value is overridden by a non-dict value.
- code-review-06: `isinstance(merged[key], dict)` returns False for custom `Mapping` types that are not literally `dict`.
- code-review-06: Dict-like objects that are not `dict` instances fall back to full replacement instead of being merged.
- code-review-06: Using `None` to mean deletion is a common pattern in config merge/patch semantics, as in Kubernetes strategic merge and Helm.
- code-review-06: The function has no docstring and no type hints.
- code-review-06: The crash on type mismatch and the aliasing behavior are bugs rather than defensible design choices.
- code-review-07: The backoff formula does not match the exponential-backoff-from-first-retry pattern it appears to imitate.
- code-review-07: The backoff formula should probably be 2 ** i or 1000 * (i + 1).
- code-review-07: On the last loop iteration, a 429 still triggers the setTimeout wait before the loop exits.
- code-review-07: The wait on the final attempt is a pointless delay because the function returns undefined anyway.
- code-review-07: Accessing err.status on null or undefined throws a TypeError inside the catch block.
- code-review-07: The TypeError thrown inside the catch block is not caught anywhere in the function and propagates out uncaught.
- code-review-07: An uncaught TypeError breaks the implied contract that the function never throws.
- code-review-07: A suppressed error could silently produce a fail-open state if a caller uses the result for a permission or entitlement check.
- code-review-07: Network failures are the most common reason to want retry logic.
- code-review-07: The code does not respect a Retry-After header on 429 responses.
- code-review-07: All 5xx status codes are treated identically.
- code-review-07: 501 Not Implemented is a permanent condition, so retrying it is pure waste, unlike 502, 503, and 504.
- code-review-07: The silent swallowing of errors changes the function's error-handling contract invisibly to callers and could mask bugs and security-relevant failures.
- code-review-07: The backoff math, inconsistent return values, uncaught throw null edge case, and lack of retries for non-HTTP errors read like accumulated bugs rather than intentional behavior.
- code-review-08: `os.remove` raises `IsADirectoryError` when called on a directory.
- code-review-08: An exception from these calls kills the entire job silently unless the scheduler logs tracebacks.
- code-review-08: The `removed` count is lost on failure because it is never returned.
- code-review-08: The age-based deletion and the tmp/`.part` deletion are two unrelated criteria sharing one counter.
- code-review-08: In that case the age-based cleanup silently stops early for that run with no logging to explain why.
- code-review-08: The interaction between the two deletion branches is non-deterministic across runs.
- code-review-08: `clean()` is never called in the snippet.
- code-review-08: As given, the script does nothing when executed directly, unless the snippet is truncated.
- code-review-08: The `tmp-` prefix and `.part` suffix are conventional naming for atomic writes (write to a temp name, then rename into place).
- code-review-08: The script can delete a file mid-write if another process is actively producing it under a tmp-/`.part` name.
- code-review-08: This race condition could corrupt or silently drop an in-flight export.
- debugging-02: Code defined inside a `class` body runs in strict mode.
- debugging-02: In strict mode, `this` inside such a callback is `undefined`.
- debugging-02: Accessing `this.seconds` when `this` is `undefined` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: The user's environment is treating the callback as non-strict, for example because it is transpiled or run outside a strict context.
- debugging-02: Using an arrow function as the `setInterval` callback is the easiest fix.
- debugging-02: Calling `.bind(this)` on a regular function callback is an alternative fix that keeps a regular function.
- debugging-02: Capturing `this` in a variable beforehand, such as `const self = this;`, is another alternative fix.
- debugging-04: Under an ascii encoding, any byte greater than or equal to 0x80 causes an error.
- debugging-04: chardet and charset-normalizer are libraries that can detect a file's encoding.
- debugging-04: errors="ignore" silently drops malformed bytes.
- debugging-04: errors="replace" preserves line structure.
- debugging-05: An alternative fix is to use tags=() and convert it to a list inside the function.
- debugging-05: Another alternative fix is to use a sentinel value.
- debugging-05: The None-default-plus-copy pattern is the standard idiom.
- debugging-06: The speaker intends to check whether actual project code is present in the working directory.
- debugging-06: Project code, if present, might reveal the connection pool configuration.
- debugging-06: The speaker will look for relevant code in the working directory before giving an answer.
- debugging-07: Checking whether the actual test code exists in the current directory would enable more concrete advice.
- debugging-07: A Bash tool call is issued with the command "find . -iname '*notification*' -o -iname 'conftest.py' 2>/dev/null | head -50".
- debugging-07: The Bash tool call's description is "Search for relevant test files".
- debugging-07: The command searches the current directory for files whose names match '*notification*' or are named 'conftest.py'.
- debugging-07: The command limits its output to the first 50 results via head -50.
- debugging-07: The command discards error output by redirecting stderr to /dev/null.
- debugging-08: Unbounded growth tied to request volume is the most likely cause of the memory growth.
- debugging-08: If the growth rate versus request rate is roughly linear, the leak is traffic-correlated.
- debugging-08: If product payloads grow larger, heap usage can increase even with a bounded entry count.
- debugging-08: A custom LRU eviction policy can have bugs that prevent eviction under certain access patterns.
- debugging-08: Bounding a wrapper map does not bound memory if its values reference large objects containing additional maps.
- debugging-08: A second unbounded cache or index, such as a reverse-lookup index, may be built alongside the bounded cache.
- debugging-08: If cache entry count is flat but byte size grows, the cause is payload size or a leak inside cache values.
- debugging-08: If cache entry count grows past the configured bound, the eviction logic is broken.
- debugging-08: Memory growth that survives quiet nights is consistent with allocator fragmentation.
- debugging-08: The user currently has no heap profile insight.
- debugging-08: If RSS does not drop after forcing a full GC, the memory is not GC-reachable garbage.
- debugging-08: glibc malloc arena behavior can retain memory that is not returned to the OS.
- debugging-08: Plotting growth rate against request or webhook volume is cheap and requires no code changes.
- debugging-08: A heap diff is the missing diagnostic and will immediately disambiguate the traffic-volume leak from the high-cardinality metrics cause.
- explanation-02: FOR UPDATE blocks any other transaction from reading or modifying that row until the locking transaction commits.
- explanation-02: An optimistic update increments the version column as part of the write.
- explanation-02: Inventory decrement on checkout is an example of a fit for pessimistic locking.
- explanation-02: Optimistic locking fits cases with long think time between read and write, such as a user editing a form for minutes.
- explanation-02: Optimistic locking fits distributed or web systems where holding a database lock across a network round-trip or user interaction is impractical.
- explanation-02: In optimistic locking scenarios, retries are cheap and conflicts are rare enough that blocking would waste more throughput than it saves.
- explanation-03: TCP slow start also runs when a connection restarts after a pause.
- explanation-03: A network path may cross a fast local network and then a slow, congested link in the middle.
- explanation-03: Dropped packets cause retransmissions, wasted bandwidth, and cascading congestion.
- explanation-03: Congestion from one connection can degrade the network for everyone sharing that link.
- explanation-03: The congestion window is separate from the receive window.
- explanation-03: The receive window reflects the receiver's buffer capacity.
- explanation-03: TCP respects whichever of the congestion window and receive window is smaller.
- explanation-03: Historically the initial cwnd was 1 segment.
- explanation-03: Modern implementations often start with a higher initial cwnd, such as 10 segments.
- explanation-03: RFC 6928 specifies an initial window of 10 segments.
- explanation-03: ACKs only arrive if data is getting through successfully, so cwnd growth stalls when the network cannot keep up.
- explanation-03: Packet loss is detected via timeout or duplicate ACKs.
- explanation-03: ssthresh is often set from a previous congestion event.
- explanation-03: Slow start is not slow in an absolute sense because exponential growth is fast.
- explanation-03: The word 'slow' in slow start refers to it being more cautious than sending at full line rate from the first packet.
- explanation-04: A process has its own memory address space, file descriptors, and OS-level resources.
- explanation-04: Communication between processes requires explicit mechanisms such as pipes, sockets, or shared memory segments.
- explanation-04: Each thread has its own stack and instruction pointer.
- explanation-04: Threads can communicate by reading and writing shared variables, given proper synchronization.
- explanation-04: A crash in one thread, such as a segfault, can bring down the entire process and all its other threads.
- explanation-04: Web servers and browsers run each tab or worker as a separate process so one bad request doesn't kill the whole server.
- explanation-04: In runtimes with a global interpreter lock, threads help with I/O-bound work but not CPU-bound work.
- explanation-04: Python's multiprocessing module is used for CPU-bound parallel computation.
- explanation-04: Threads share everything, so one thread's memory access cannot be restricted from another.
- explanation-04: Processes can be killed, restarted, or resource-limited individually without affecting sibling processes.
- explanation-04: Per-process resource limits can be applied via cgroups or ulimits.
- explanation-04: Independent process lifecycle management is useful for worker pools where a hung or leaking worker should be recycled.
- explanation-04: Threads context-switch faster than processes.
- explanation-04: Threads are preferable when the risk of one task corrupting shared state is low or well-managed via locks or atomics.
- explanation-04: Threads are a natural fit for I/O-bound concurrency within a single trusted program.
- explanation-05: A memory leak in a garbage-collected language does not mean memory is lost as it is in C with unfreed malloc.
- explanation-05: Examples of long-lived collections include a global cache, a static Map, and a subscriber list.
- explanation-05: Examples of long-lived objects for listener registration include a DOM element, an event bus, and a global emitter.
- explanation-06: Slowness could be caused by writes, N+1 queries, network latency, unindexed queries, or application code.
- explanation-06: A cache would not fix slowness caused by writes, N+1 queries, network latency, unindexed queries, or application code.
- explanation-06: A cache used under write-heavy or low-repetition workloads becomes a layer that is frequently invalidated or missed.
- explanation-06: The read/write ratio can be determined by checking logs or adding simple counters.
- explanation-06: Common database issues to check first include missing indexes, N+1 queries, and slow joins.
- explanation-06: Redis is an example of a cache that can be placed in front of a database.
- explanation-07: Machines with multiple terabytes of RAM/NVMe are routine.
- explanation-07: Sharding fixes throughput ceilings and total-size ceilings.
- explanation-07: Growth rate can be estimated by measuring growth over the last 3-6 months and extrapolating.
- explanation-07: Single-instance PostgreSQL limits are roughly multiple terabytes of data and tens of thousands of writes per second.
- explanation-07: Tenant ID and user ID are examples of natural shard keys.
- explanation-07: Sharding imposes permanent operational complexity, including a routing layer, rebalancing, cross-shard transactions and joins, harder migrations, and harder backups.
- explanation-07: Reactive sharding is a known, roughly one-time cost rather than an ongoing tax.
- explanation-07: The costs of sharding too early versus too late are asymmetric.
- explanation-07: The recommended approach is to scale vertically, add read replicas and caching, and instrument to track the actual growth rate.
- explanation-08: Without measurements, you cannot credibly estimate the performance improvement from switching serialization formats.
- explanation-08: Profiling is the first step before deciding to switch serialization formats, rather than guessing.
- explanation-08: Request latency is composed of JSON serialization/deserialization plus network, database, and business logic time.
- explanation-08: If JSON parsing accounts for 2% of request time, even a 10x speedup in parsing is negligible.
- explanation-08: Measuring what fraction of request latency comes from JSON serialization is roughly a five-minute profiling task.
- explanation-08: Profiling provides more useful information than any general performance estimate.
- explanation-08: Binary formats such as Protobuf and MessagePack typically shrink payloads by 20-50% relative to JSON.
- explanation-08: Payload size reduction matters most when requests are large and network- or bandwidth-bound rather than CPU-bound.
- explanation-08: Smaller payloads help more on slow or mobile networks than on localhost or fast LANs.
- explanation-08: For CPU-bound serialization, binary formats typically run 2-10x faster than JSON.
- explanation-08: Faster serialization only affects overall performance if serialization is a measurable portion of total latency.
- explanation-08: Migrating from JSON to a binary format carries meaningful costs including schemas, tooling, and debuggability tradeoffs.
- summarization-01: The app now starts up roughly 40% faster.
- summarization-02: The similarity of the config templates directly caused the incident.
- summarization-02: Detection-to-resolution time for the incident was 34 minutes.
- summarization-02: The rollback fixed the incident in about 27 minutes.
- summarization-04: Four clicks produce four error banners.
- summarization-05: Ada is assigned to confirm with the mobile team's lead whether they have been informed of the API deprecation.
- summarization-05: There is an API deprecation that the mobile team's lead may not have been informed of.

Added facts (styled only):

- code-review-03: The `orders` table has columns `id`, `customer`, `status`, and `total`.
- code-review-03: `%s`, `?`, and `:name` are placeholder styles used by database drivers.
- code-review-03: The database driver's documentation should be consulted to determine the correct placeholder style.
- code-review-04: The race in `increment` is a classic check-then-act race condition.
- code-review-05: A wrong `BACKUP_DIR` value such as `/` or an empty string combined with `rm -rf` can delete critical files.
- code-review-06: A deeply nested structure can hit Python's recursion limit.
- code-review-06: The function does not validate that `base` and `override` are dicts.
- code-review-06: Passing a non-dict argument causes a generic `TypeError` with no clear message.
- code-review-06: The `None` check runs before the type check.
- code-review-06: If `merged[key]` is a dict and `override[key]` is not, or the reverse, the function replaces the whole value instead of merging.
- code-review-06: List merges have multiple valid interpretations: concatenate, replace, or deduplicate.
- code-review-06: The silent no-op on a missing key can hide a typo in a key name.
- code-review-06: The shallow-copy issues, the missing recursion guard, and the lack of input validation are most likely oversights.
- code-review-06: The `None`-deletes-key rule and the type-mismatch replacement rule look deliberate.
- code-review-06: Neither the `None`-deletes-key rule nor the type-mismatch replacement rule is documented or tested.
- code-review-07: The wrapper is an arrow function that calls fn(...args), which loses the this binding.
- code-review-07: If fn requires a specific this value, the call breaks.
- code-review-07: The function has no timeout.
- code-review-07: If fn hangs, withRetry hangs as well.
- code-review-07: Some callers may already depend on null as a valid result rather than a failure signal.
- code-review-07: The retry policy for status 429 and 500 indicates deliberate intent.
- code-review-07: The retry policy suggests someone built the function for a specific API.
- code-review-07: The fail-soft pattern spares callers from needing a try/catch.
- code-review-07: The zero-delay retry on 500 errors is likely a bug.
- code-review-07: The silent loss of the original error object is likely a bug.
- code-review-07: The recommendation is not to change the return behavior without confirmation from the callers.
- code-review-07: Changing from null/undefined returns to a thrown error can break code that depends on the current behavior.
- code-review-08: There is no prior memory stored for this project.
- code-review-08: `ROOT` is a hardcoded path with no existence check.
- code-review-08: If the mount is absent or the path is wrong, `os.listdir` raises an error whose message does not explain the real cause to whoever reads the log.
- code-review-08: The hardcoded `ROOT` without an existence check is not deliberate.
- code-review-08: The `tmp-` and `.part` filters are likely intentional but have no cap.
- code-review-08: The two most important fixes are moving `CUTOFF = time.time() - 86400 * 45` inside `clean()` and applying the 500-file cap to all deletions rather than only old files.
- debugging-01: The fix applies to line 4.
- debugging-01: The corrected code is a function get_url that takes a parameter cfg and returns the f-string "http://{cfg['host']}:{cfg['port']}/api".
- debugging-05: The fixed `make_post` sets `tags = list(DEFAULT_TAGS)` when `tags` is `None`, and otherwise sets `tags = list(tags)`.
- debugging-05: After the fix, the function no longer mutates `DEFAULT_TAGS` or any list the caller passes in.
- debugging-06: Connection pool contention with the analytics service is a likely cause of the failure.
- debugging-06: Both the export job and the analytics service share one database.
- debugging-06: If the analytics service runs long queries at night, it holds database connections.
- debugging-06: The export job waits for a free connection and times out after 30 seconds.
- debugging-06: If the pool size does not match the combined load of both services, wait times grow past the timeout as concurrency rises.
- debugging-06: A lock held by the analytics service can block export queries.
- debugging-06: A blocked query can appear as pool exhaustion even though the pool is not full.
- debugging-06: Batches that touch more rows or larger tables run longer and hold connections longer.
- debugging-06: The failure moves between batch numbers rather than occurring at a fixed batch.
- debugging-06: Because the error is not tied to a fixed batch, a code bug tied to one batch is unlikely.
- debugging-06: A shared-resource problem depending on the analytics service schedule and current load is a more plausible explanation than a batch-specific code bug.
- debugging-06: The export job's failures occur near 02:14 UTC.
- debugging-06: The export job runs on a weekly cron cycle.
- debugging-06: Extending log retention around each failure would reveal pool size, active connection count, and concurrent queries at the time of the error.
- debugging-06: Logging pool metrics continuously (active connections, idle connections, queue length) every few seconds allows comparison against failure timestamps.
- debugging-06: pg_stat_activity is the Postgres view for finding long-running or blocked queries.
- debugging-06: Per-batch query duration logging shows whether the slow batches are the ones that fail or whether the delay originates outside the export job.
- debugging-06: An alert on pool exhaustion would provide more log context at the next failure instead of waiting for the weekly cron cycle.
- debugging-06: Three candidate fixes are raising the pool size, isolating the analytics service to its own connection pool, and adding a retry with backoff plus a larger timeout for the export job.
- debugging-07: Four parallel workers can share a database, cache, or queue.
- debugging-07: One worker's event can leak into another worker's digest.
- debugging-07: A shared counter can drop an event.
- debugging-07: The test never fails on a developer machine.
- debugging-07: Only one worker runs on the developer machine.
- debugging-07: If event creation is asynchronous, the digest request can arrive before the third event is visible.
- debugging-07: Asynchronous event creation can take the form of a background job, an event queue, or an eventually-consistent write.
- debugging-07: Under load from four workers, the race between digest query and event commits becomes more likely.
- debugging-07: CI machines are often slower or more loaded than developer machines.
- debugging-07: A fixed wait that is sufficient on a developer machine can be too short on a loaded CI runner.
- debugging-07: If two tests use the same user, tenant, or time window, one worker's setup can overwrite or filter out another worker's event.
- debugging-07: Shared test data across workers causes the digest to contain events from the wrong test, or fewer events than expected.
- debugging-07: If the digest uses a time-based cutoff, such as events from the last minute, a slow CI run can push the third event outside the window.
- debugging-07: Running the suite in CI with one worker for several runs and seeing the failure stop indicates parallel workers are the cause.
- debugging-07: Running the suite in CI with one worker isolates parallelism from CI speed.
- debugging-07: If the failure appears when running the suite locally with four workers, the cause is parallelism rather than CI-specific speed or load.
- debugging-07: A targeted log on failure should record event IDs, timestamps, and worker ID for both the setup calls and the digest response.
- debugging-07: The CI runner does not keep artifacts.
- debugging-07: Printing the log to stdout makes it appear in the CI log.
- debugging-07: Shared state can be found by searching the test setup for hardcoded IDs, fixed time windows, or global counters not scoped per worker or per test run.
- debugging-07: A fixed wait can be replaced with a poll that checks for three events, up to a timeout.
- debugging-07: If the failure rate drops after replacing fixed waits with polling, timing was the cause.
- debugging-07: A retry-with-backoff can be added temporarily around the digest call, logging each attempt.
- debugging-07: If the digest succeeds on a later attempt, that confirms an asynchronous write rather than a hard bug.
- debugging-07: Step 1 gives the clearest signal because it directly tests the one known difference: parallel workers.
- debugging-07: The test involves three events and a digest.
- debugging-08: Two observations point away from the cache as the cause.
- debugging-08: The evidence suggests two separate leaks.
- debugging-08: One leak runs on a schedule.
- debugging-08: A bound on cache entry count does not stop a leak if evicted entries remain reachable through another reference.
- debugging-08: A per-entry listener or callback is an example of a reference that can keep evicted cache values reachable.
- debugging-08: Growth during a campaign week can be compared against a quiet week to test the metrics registry hypothesis.
- debugging-08: Tracking open socket count, thread count, and file descriptor count over a day is a check for handler resource leaks.
- debugging-08: If socket, thread, and file descriptor counts only go up and never come down, the handler resource leak is the cause.
- debugging-08: Scheduled or background work unrelated to webhooks is a possible cause.
- debugging-08: Because the canary grows without webhook traffic, a job running on a timer can leak on its own.
- debugging-08: Health checks, cache refreshes, and metrics flushes are examples of timer-driven jobs that can leak.
- debugging-08: Disabling webhook traffic entirely on a test instance and watching memory for a full day is a check for scheduled-work leaks.
- debugging-08: Any memory growth on an instance with webhook traffic disabled comes from scheduled work rather than requests.
- debugging-08: Taking two memory snapshots hours apart on the canary and two more during a campaign day helps identify which cause matters most.
- debugging-08: The canary snapshot pair reveals the traffic-independent leak.
- debugging-08: The difference between the two snapshot pairs reveals the traffic-scaled leak.
- explanation-02: Optimistic locking fits when conflicts are rare and reads are frequent.
- explanation-03: Retransmissions waste bandwidth and add delay.
- explanation-04: Threads use less memory than processes.
- explanation-04: Threads use less memory because they do not need a separate memory space.
- explanation-05: When code adds objects to a list, map, or cache but never removes them, the collection grows without limit.
- explanation-06: If the read-to-write mix is close to 1:1, a cache gives little benefit.
- explanation-06: A cache can add risk because it can serve stale data.
- explanation-06: Too many database connections causes queries to wait.
- explanation-07: CPU, memory, and disk I/O on the instance should be checked to assess current load.
- explanation-07: If CPU, memory, and disk I/O stay under 60-70% at peak, the database has room to grow.
- explanation-07: Without a growth number, you cannot plan a shard key or a timeline.
- explanation-07: Picking a shard key before understanding query patterns can create hot shards.
- explanation-07: Sharding requires rewriting application logic to work around lost cross-shard joins, transactions, and foreign keys.
- explanation-07: As the schema grows, it becomes harder to add a shard key later.
- explanation-07: Some tables can need a redesign in order to add a shard key later.
- explanation-07: The recommended first step is adding monitoring for CPU, memory, disk I/O, and query latency if not already present.
- explanation-07: The recommendation includes finding and fixing slow queries and missing indexes.
- explanation-07: The recommendation includes asking the product team for a rough growth number tied to a business event such as a new market or a new customer segment.
- explanation-07: Example triggers for revisiting sharding are instance size exceeding 1 TB or write latency exceeding a set number of milliseconds at peak load.
- explanation-08: The speaker will check saved memory for prior context before answering.
- explanation-08: Saved memory is available to the speaker.
- summarization-01: The application starts up to 40% faster.
- summarization-02: The rollback restored normal error rates within 34 minutes.
- summarization-03: Thumbnail generation currently adds 800ms to 3 seconds to each upload.
- summarization-03: A worker pool will generate the thumbnails and update the record.
- summarization-07: A staging test compared the new batcher against the current batcher.

## Hedging survival

The judge lists the claims that the unstyled answer presents with uncertainty, then judges each claim in the styled answer: hedged (the uncertainty survives in some form), certain (the claim survives but reads as a fact — the failure this check targets), or absent (the claim is gone, a completeness loss). Survival is hedged / (hedged + certain). The claims that became certain appear verbatim below the table.

### actionable-clarity

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 1 | 1 | 0 | 0.5 |
| code-review-02 | 1 | 1 | 0 | 0 | 1.0 |
| code-review-03 | 3 | 1 | 0 | 2 | 1.0 |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-06 | 6 | 5 | 0 | 1 | 1.0 |
| code-review-07 | 11 | 7 | 0 | 4 | 1.0 |
| code-review-08 | 8 | 4 | 3 | 1 | 0.571 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 1 | 0 | 0 | 1 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 2 | 2 | 0 | 0 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 1 | 0 | 0 | 1 | n/a |
| debugging-07 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 7 | 4 | 1 | 2 | 0.8 |
| explanation-01 | 4 | 2 | 2 | 0 | 0.5 |
| explanation-02 | 1 | 0 | 0 | 1 | n/a |
| explanation-03 | 5 | 2 | 1 | 2 | 0.667 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 3 | 3 | 0 | 0 | 1.0 |
| explanation-07 | 2 | 1 | 1 | 0 | 0.5 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 1 | 1 | 0 | 0 | 1.0 |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 1 | 0 | 0 | 1 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 5 | 5 | 0 | 0 | 1.0 |
| summarization-07 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 73 over 31 judged pairs: 46 hedged, 10 certain, 17 absent.

Median survival: 1.0 over 17 scored pairs.

Claims that became certain:

- code-review-01: The db=None default suggests the signature/defaults don't match actual required usage.
- code-review-05: If `$1` is empty, `cd $BACKUP_DIR` becomes `cd` with no arguments and goes to `$HOME`, which combined with the `rm -rf *.tmp` below could delete files in an unintended location.
- code-review-08: The bugs listed are likely unintentional.
- code-review-08: The tmp-/.part branch is likely a real safety issue rather than just a bug.
- code-review-08: The lack of an age check on the tmp-file branch looks like an oversight rather than intent.
- debugging-08: The canary, which has no webhooks but presumably other traffic, still grows, just slower.
- explanation-01: Each bucket in separate chaining usually holds a linked list, and sometimes a tree or dynamic array.
- explanation-01: Open addressing tends to win when memory layout and cache performance matter most and you can keep the load factor low with good resizing.
- explanation-03: On each ACK, cwnd increases roughly by one segment per ACK.
- explanation-07: There is usually a lot of vertical headroom left before cost or hardware availability becomes a problem.

### clarity-flow

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 2 | 0 | 0.0 |
| code-review-02 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-03 | 3 | 2 | 0 | 1 | 1.0 |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 2 | 2 | 0 | 0 | 1.0 |
| code-review-06 | 6 | 5 | 0 | 1 | 1.0 |
| code-review-07 | 11 | 7 | 1 | 3 | 0.875 |
| code-review-08 | 8 | 6 | 1 | 1 | 0.857 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 2 | 2 | 0 | 0 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 1 | 0 | 0 | 1 | n/a |
| debugging-07 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 7 | 0 | 0 | 7 | n/a |
| explanation-01 | 4 | 0 | 1 | 3 | 0.0 |
| explanation-02 | 1 | 0 | 1 | 0 | 0.0 |
| explanation-03 | 5 | 3 | 0 | 2 | 1.0 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 3 | 1 | 2 | 0 | 0.333 |
| explanation-07 | 2 | 1 | 1 | 0 | 0.5 |
| explanation-08 | 2 | 1 | 0 | 1 | 1.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 1 | 1 | 0 | 0 | 1.0 |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 1 | 0 | 0 | 1 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 5 | 5 | 0 | 0 | 1.0 |
| summarization-07 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 75 over 32 judged pairs: 44 hedged, 10 certain, 21 absent.

Median survival: 1.0 over 19 scored pairs.

Claims that became certain:

- code-review-01: If the caller passes their own roles list, append("member") mutates it in place, silently changing data the caller may still be using elsewhere.
- code-review-01: The db=None default suggests the signature/defaults don't match actual required usage.
- code-review-02: Calling `.json()` on an error response (e.g., a 404 HTML page) will likely throw a JSON parse error, or succeed with an unexpected error payload.
- code-review-07: That same issue could mask both bugs and security-relevant failures.
- code-review-08: The tmp-/.part branch is likely a real safety issue rather than just a bug.
- explanation-01: Open addressing tends to win when memory layout and cache performance matter most and you can keep the load factor low with good resizing.
- explanation-02: At write-time, the check for whether the data changed since it was read is usually done via a version number or timestamp.
- explanation-06: A cache could even add complexity without benefit.
- explanation-06: If reads dominate and the same data is fetched repeatedly, caching can help a lot.
- explanation-07: There is usually a lot of vertical headroom left before cost or hardware availability becomes a problem.

### classic-concise

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 2 | 0 | 0.0 |
| code-review-02 | 1 | 0 | 0 | 1 | n/a |
| code-review-03 | 3 | 0 | 1 | 2 | 0.0 |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 2 | 0 | 0 | 2 | n/a |
| code-review-06 | 6 | 4 | 1 | 1 | 0.8 |
| code-review-07 | 11 | 5 | 1 | 5 | 0.833 |
| code-review-08 | 8 | 6 | 1 | 1 | 0.857 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 2 | 2 | 0 | 0 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 1 | 0 | 0 | 1 | n/a |
| debugging-07 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 7 | 4 | 1 | 2 | 0.8 |
| explanation-01 | 4 | 0 | 4 | 0 | 0.0 |
| explanation-02 | 1 | 1 | 0 | 0 | 1.0 |
| explanation-03 | 5 | 3 | 1 | 1 | 0.75 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 3 | 1 | 2 | 0 | 0.333 |
| explanation-07 | 2 | 1 | 1 | 0 | 0.5 |
| explanation-08 | 2 | 0 | 0 | 2 | n/a |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 1 | 0 | 1 | 0 | 0.0 |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 1 | 0 | 0 | 1 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 5 | 5 | 0 | 0 | 1.0 |
| summarization-07 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 75 over 32 judged pairs: 40 hedged, 16 certain, 19 absent.

Median survival: 0.8 over 17 scored pairs.

Claims that became certain:

- code-review-01: If the caller passes their own roles list, append("member") mutates it in place, silently changing data the caller may still be using elsewhere.
- code-review-01: The db=None default suggests the signature/defaults don't match actual required usage.
- code-review-03: `SELECT *` pulls more data than is likely needed
- code-review-06: Treating `None` as "delete this key" is a common config-merge/patch pattern (similar to Kubernetes strategic merge, Helm), so it may well be intentional.
- code-review-07: That same issue could mask both bugs and security-relevant failures.
- code-review-08: If another process is actively producing a file under a tmp-/.part name, this script can delete it mid-write — a race condition that could corrupt or silently drop an in-flight export.
- debugging-08: The canary, which has no webhooks but presumably other traffic, still grows, just slower.
- explanation-01: Each bucket in separate chaining usually holds a linked list, and sometimes a tree or dynamic array.
- explanation-01: Open addressing implementations typically resize well before the array gets full, often at around 70% load.
- explanation-01: Deletion under open addressing usually requires a special "tombstone" marker instead of a true empty slot.
- explanation-01: Open addressing tends to win when memory layout and cache performance matter most and you can keep the load factor low with good resizing.
- explanation-03: On each ACK, cwnd increases roughly by one segment per ACK.
- explanation-06: A cache could even add complexity without benefit.
- explanation-06: If reads dominate and the same data is fetched repeatedly, caching can help a lot.
- explanation-07: There is usually a lot of vertical headroom left before cost or hardware availability becomes a problem.
- summarization-02: Other environment-sensitive values, beyond connection pool size, likely also need to be added to the config review checklist

### developer-docs

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 1 | 1 | 0 | 0.5 |
| code-review-02 | 1 | 1 | 0 | 0 | 1.0 |
| code-review-03 | 3 | 2 | 0 | 1 | 1.0 |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-06 | 6 | 5 | 0 | 1 | 1.0 |
| code-review-07 | 11 | 6 | 1 | 4 | 0.857 |
| code-review-08 | 8 | 3 | 0 | 5 | 1.0 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 1 | 0 | 0 | 1 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 2 | 2 | 0 | 0 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 1 | 0 | 0 | 1 | n/a |
| debugging-07 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 7 | 3 | 1 | 3 | 0.75 |
| explanation-01 | 4 | 2 | 2 | 0 | 0.5 |
| explanation-02 | 1 | 0 | 1 | 0 | 0.0 |
| explanation-03 | 5 | 1 | 1 | 3 | 0.5 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 3 | 3 | 0 | 0 | 1.0 |
| explanation-07 | 2 | 2 | 0 | 0 | 1.0 |
| explanation-08 | 2 | 0 | 0 | 2 | n/a |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 1 | 0 | 1 | 0 | 0.0 |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 1 | 0 | 1 | 0 | 0.0 |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 5 | 5 | 0 | 0 | 1.0 |
| summarization-07 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 75 over 32 judged pairs: 43 hedged, 10 certain, 22 absent.

Median survival: 1.0 over 19 scored pairs.

Claims that became certain:

- code-review-01: The db=None default suggests the signature/defaults don't match actual required usage.
- code-review-05: There shouldn't be directories matching `*.tmp` to recurse into, so `rm -f` is preferable to `rm -rf` (and if there are such directories, that needs explicit intent).
- code-review-07: That same issue could mask both bugs and security-relevant failures.
- debugging-08: The canary, which has no webhooks but presumably other traffic, still grows, just slower.
- explanation-01: Each bucket in separate chaining usually holds a linked list, and sometimes a tree or dynamic array.
- explanation-01: Open addressing tends to win when memory layout and cache performance matter most and you can keep the load factor low with good resizing.
- explanation-02: At write-time, the check for whether the data changed since it was read is usually done via a version number or timestamp.
- explanation-03: The congestion window (and thus the sending rate) doubles approximately every round-trip time.
- summarization-02: Other environment-sensitive values, beyond connection pool size, likely also need to be added to the config review checklist
- summarization-04: The PDF export failure is likely browser-independent.

### plain-language

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 1 | 1 | 0 | 0.5 |
| code-review-02 | 1 | 0 | 0 | 1 | n/a |
| code-review-03 | 3 | 0 | 2 | 1 | 0.0 |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-06 | 6 | 6 | 0 | 0 | 1.0 |
| code-review-07 | 11 | 8 | 1 | 2 | 0.889 |
| code-review-08 | 8 | 6 | 0 | 2 | 1.0 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 2 | 2 | 0 | 0 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 1 | 0 | 0 | 1 | n/a |
| debugging-07 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 7 | 5 | 1 | 1 | 0.833 |
| explanation-01 | 4 | 0 | 2 | 2 | 0.0 |
| explanation-02 | 1 | 1 | 0 | 0 | 1.0 |
| explanation-03 | 5 | 2 | 0 | 3 | 1.0 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 3 | 2 | 1 | 0 | 0.667 |
| explanation-07 | 2 | 1 | 1 | 0 | 0.5 |
| explanation-08 | 2 | 2 | 0 | 0 | 1.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 1 | 1 | 0 | 0 | 1.0 |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 1 | 0 | 0 | 1 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 5 | 4 | 0 | 1 | 1.0 |
| summarization-07 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 75 over 32 judged pairs: 49 hedged, 10 certain, 16 absent.

Median survival: 1.0 over 19 scored pairs.

Claims that became certain:

- code-review-01: The db=None default suggests the signature/defaults don't match actual required usage.
- code-review-03: `SELECT *` pulls more data than is likely needed
- code-review-03: A failed query raising an uncaught exception may or may not be desired, depending on the calling context
- code-review-05: If `$1` is empty, `cd $BACKUP_DIR` becomes `cd` with no arguments and goes to `$HOME`, which combined with the `rm -rf *.tmp` below could delete files in an unintended location.
- code-review-07: That same issue could mask both bugs and security-relevant failures.
- debugging-08: The canary, which has no webhooks but presumably other traffic, still grows, just slower.
- explanation-01: Each bucket in separate chaining usually holds a linked list, and sometimes a tree or dynamic array.
- explanation-01: Open addressing tends to win when memory layout and cache performance matter most and you can keep the load factor low with good resizing.
- explanation-06: If reads dominate and the same data is fetched repeatedly, caching can help a lot.
- explanation-07: There is usually a lot of vertical headroom left before cost or hardware availability becomes a problem.

### technical-simplified

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 1 | 1 | 0 | 0.5 |
| code-review-02 | 1 | 0 | 0 | 1 | n/a |
| code-review-03 | 3 | 0 | 1 | 2 | 0.0 |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-06 | 6 | 4 | 0 | 2 | 1.0 |
| code-review-07 | 11 | 6 | 1 | 4 | 0.857 |
| code-review-08 | 8 | 4 | 0 | 4 | 1.0 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 1 | 0 | 0 | 1 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 2 | 2 | 0 | 0 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 1 | 0 | 0 | 1 | n/a |
| debugging-07 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 7 | 2 | 2 | 3 | 0.5 |
| explanation-02 | 1 | 0 | 1 | 0 | 0.0 |
| explanation-03 | 5 | 2 | 1 | 2 | 0.667 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 3 | 3 | 0 | 0 | 1.0 |
| explanation-07 | 2 | 2 | 0 | 0 | 1.0 |
| explanation-08 | 2 | 0 | 0 | 2 | n/a |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 1 | 0 | 0 | 1 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 1 | 0 | 0 | 1 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-07 | 4 | 4 | 0 | 0 | 1.0 |

Claims: 63 over 29 judged pairs: 30 hedged, 8 certain, 25 absent.

Median survival: 0.857 over 13 scored pairs.

Claims that became certain:

- code-review-01: The db=None default suggests the signature/defaults don't match actual required usage.
- code-review-03: `SELECT *` pulls more data than is likely needed
- code-review-05: If `$1` is empty, `cd $BACKUP_DIR` becomes `cd` with no arguments and goes to `$HOME`, which combined with the `rm -rf *.tmp` below could delete files in an unintended location.
- code-review-07: As written, the retry scoping looks like an incomplete implementation of retry semantics.
- debugging-08: The canary, which has no webhooks but presumably other traffic, still grows, just slower.
- debugging-08: Webhooks and campaigns often carry unique or high-cardinality identifiers.
- explanation-02: At write-time, the check for whether the data changed since it was read is usually done via a version number or timestamp.
- explanation-03: On each ACK, cwnd increases roughly by one segment per ACK.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 120, measured: 120.
Mean duration: 14707 ms. Mean wall: 23450 ms. Mean startup: 8743 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 120, measured: 120.
Input tokens: 240 uncached, 243745 cache write, 246360 cache read. Output tokens: 127530.
Cache-read share: 0.502.
Cache writes by lifetime: 243745 at 5 minutes, 0 at 1 hour.

## Reuse

Reused rows: 636, imported from 2026-08-10b.
Live calls of this run: 120.

The freshness sample re-ran 6 imported verdicts live; 6 agree.

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

- technical-simplified/explanation-01: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/summarization-08: the pair failed the gate, excluded
- actionable-clarity/explanation-08: the pair failed the gate, excluded
