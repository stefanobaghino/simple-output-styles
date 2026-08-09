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

Judge: opus. Judged on 2026-08-08T08:26:14+00:00.

## Completeness (fact survival)

The judge lists the facts of the unstyled answer, then checks each fact against the styled answer. The fraction is the share of the facts that survive. The judge also lists the facts of the styled answer and checks each fact against the unstyled answer: a styled fact that the unstyled answer does not state is an addition. The lost facts and the added facts appear verbatim below the table.

### clarity-flow

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 25 | 20 | 0.8 | 27 | 2 |
| code-review-02 | 23 | 16 | 0.696 | 17 | 3 |
| code-review-03 | 26 | 14 | 0.538 | 12 | 3 |
| code-review-04 | 26 | 22 | 0.846 | 24 | 4 |
| code-review-05 | 27 | 21 | 0.778 | 23 | 3 |
| code-review-06 | 39 | 24 | 0.615 | 24 | 4 |
| code-review-07 | 43 | 31 | 0.721 | 45 | 14 |
| code-review-08 | 36 | 27 | 0.75 | 40 | 8 |
| debugging-01 | 8 | 6 | 0.75 | 6 | 1 |
| debugging-02 | 20 | 14 | 0.7 | 14 | 2 |
| debugging-03 | 11 | 11 | 1.0 | 9 | 0 |
| debugging-04 | 12 | 8 | 0.667 | 15 | 1 |
| debugging-05 | 20 | 20 | 1.0 | 12 | 1 |
| debugging-06 | 26 | 14 | 0.538 | 27 | 8 |
| debugging-07 | 30 | 17 | 0.567 | 27 | 12 |
| debugging-08 | 45 | 15 | 0.333 | 27 | 11 |
| explanation-01 | 39 | 20 | 0.513 | 20 | 0 |
| explanation-02 | 23 | 22 | 0.957 | 24 | 4 |
| explanation-03 | 33 | 28 | 0.848 | 22 | 5 |
| explanation-04 | 33 | 17 | 0.515 | 21 | 4 |
| explanation-05 | 18 | 15 | 0.833 | 12 | 0 |
| explanation-06 | 27 | 21 | 0.778 | 16 | 4 |
| explanation-07 | 30 | 22 | 0.733 | 30 | 3 |
| explanation-08 | 13 | 8 | 0.615 | 13 | 5 |
| summarization-01 | 6 | 6 | 1.0 | 5 | 0 |
| summarization-02 | 13 | 10 | 0.769 | 12 | 4 |
| summarization-03 | 14 | 12 | 0.857 | 8 | 0 |
| summarization-04 | 13 | 11 | 0.846 | 13 | 1 |
| summarization-05 | 9 | 9 | 1.0 | 8 | 1 |
| summarization-06 | 14 | 14 | 1.0 | 12 | 0 |
| summarization-07 | 16 | 15 | 0.938 | 15 | 2 |
| summarization-08 | 23 | 21 | 0.913 | 20 | 1 |

Median fraction: 0.774 over 32 scored pairs.

Median additions: 3.0 over 32 scored pairs.

Lost facts:

- code-review-01: Mutable default arguments are a classic Python footgun.
- code-review-01: When a caller passes their own list, `roles.append(...)` mutates that list in place.
- code-review-01: Mutating the caller's list silently changes the caller's original list as a side effect, which is surprising and hard to trace.
- code-review-01: The suggested fix raises `ValueError("name is required")` when `name` is falsy.
- code-review-01: The suggested fix calls `db.insert({"name": name, "roles": roles})` and returns `True`.
- code-review-02: `fetch` rejects only on network failure.
- code-review-02: The function assumes `data` always has a `.name` property.
- code-review-02: If the API returns an error object or unexpected shape, `.toUpperCase()` will throw.
- code-review-02: `userId` is not validated or sanitized.
- code-review-02: If `userId` can come from untrusted user input, it should be encoded with `encodeURIComponent(userId)`.
- code-review-02: Encoding `userId` avoids malformed URLs and injection into the URL path.
- code-review-02: The corrected version awaits `fetch` with `encodeURIComponent(userId)` in the URL.
- code-review-03: There is no prior memory stored for this project.
- code-review-03: Some database engines allow chained additional statements via SQL injection.
- code-review-03: Injection is the top OWASP vulnerability.
- code-review-03: The code has no input validation.
- code-review-03: The `status` parameter is not checked against a known set of valid statuses.
- code-review-03: Valid order statuses include open, shipped, and cancelled.
- code-review-03: Unvalidated status input causes typos or bad data to silently return empty results.
- code-review-03: A database error from `cursor.execute` will propagate as a raw exception with no context about the query or inputs that caused it.
- code-review-03: The code has no type hints.
- code-review-03: The function signature gives no indication of expected types.
- code-review-03: Appropriate type hints for the function would be `cursor: Cursor, customer_name: str, status: str) -> list[tuple]`.
- code-review-03: The SQL injection is the only issue that actually matters in this code.
- code-review-04: Individual bytecode operations are atomic in CPython.
- code-review-04: The original code would break under PyPy under some conditions.
- code-review-04: The fixed version uses `with self._lock` in `increment`, `reset`, and the `value` property.
- code-review-04: The fixed version gives callers a safe way to read the current value.
- code-review-05: If no `*.tmp` files exist, `rm -rf *.tmp` attempts to remove a literal file named `*.tmp` and errors.
- code-review-05: The script handles neither the no-matching-`*.log` case nor the no-matching-`*.tmp` case.
- code-review-05: The final success message is misleading because it prints even on partial or total failure.
- code-review-05: `gzip $f` will fail or prompt if a `.gz` file of the same name already exists.
- code-review-05: The script provides no `-f` flag or other handling for a pre-existing `.gz` file.
- code-review-05: The script performs no sanity check on the directory argument, such as rejecting `.` or `/`.
- code-review-06: The code uses `merged.pop(key, None)` when an override value is `None`.
- code-review-06: Treating `None` as a delete sentinel is a common convention in layered config systems such as Helm and Ansible.
- code-review-06: `merged.pop(key, None)` makes deleting a key that does not exist in `base` a silent no-op.
- code-review-06: The silent no-op on a missing key can mask a typo'd key name with no error or warning.
- code-review-06: The resulting stack trace is far from the actual mistake and is confusing.
- code-review-06: When a key is replaced wholesale in the `else` branch, `merged[key]` becomes the exact same object passed in `override`.
- code-review-06: Later mutation of either `merged` or `override` leaks into the other.
- code-review-06: The aliasing issue can be fixed by using `copy.deepcopy` or a proper deep-merge-copy.
- code-review-06: Merging lists is ambiguous because it is unclear whether to append, dedupe, or merge by index.
- code-review-06: The function performs no validation of the top-level `base` and `override` types.
- code-review-06: If `base` is not dict-like, `dict(base)` may raise a strange error.
- code-review-06: If `base` is an iterable of pairs, such as a list of tuples, `dict(base)` may silently succeed instead of failing clearly.
- code-review-06: The lack of top-level type validation is likely an oversight and warrants an explicit type check with a clear error message.
- code-review-06: The silent no-op when deleting a missing key is a side effect of the `None`-as-sentinel design rather than a separately chosen behavior.
- code-review-06: The `None`-as-delete behavior should stay as-is only if downstream configs never need to set a real `None` value.
- code-review-07: Swallowing non-retryable errors hides bugs and is the most dangerous problem in the code.
- code-review-07: Exponential backoff would be expressed as something like 1000 * 2 ** i.
- code-review-07: Axios exposes HTTP status at err.response.status rather than err.status.
- code-review-07: Retries will silently break if the underlying HTTP client changes.
- code-review-07: There is no maximum-delay cap and no total-timeout.
- code-review-07: The code uses attempts = 3 with a loop condition of i < attempts.
- code-review-07: attempts = 3 with i < attempts yields 3 total tries and 2 waits.
- code-review-07: The distinction between '3 attempts' and '3 retries' is a common source of off-by-one confusion downstream.
- code-review-07: A cache-warming job that should not crash a pipeline is an example of a caller that might want fail-soft behavior.
- code-review-07: Retrying 429 and 5xx but not other 4xx is a defensible retry policy.
- code-review-07: The retry policy is reasonable even though its implementation swallows errors instead of throwing.
- code-review-07: Changing the function requires finding and checking every call site for === null or truthy checks.
- code-review-08: The unconditional deletion of tmp-/.part files is the most dangerous line in the file.
- code-review-08: The tmp-/.part deletion should almost certainly have an age threshold, such as only removing files older than an hour.
- code-review-08: A broken symlink or a permissions error will raise an exception and abort clean() entirely.
- code-review-08: The script has no dry-run mode.
- code-review-08: The lack of dry-run mode and logging makes incidents hard to diagnose after the fact for a scheduled, unattended, destructive script.
- code-review-08: ROOT is a hardcoded absolute path with no override mechanism.
- code-review-08: The hardcoded ROOT makes the script hard to test safely without editing the source.
- code-review-08: The module-level CUTOFF is almost certainly an oversight rather than a deliberate choice.
- code-review-08: The missing try/except, directory crash, cap not applying to tmp/.part, and absence of logging read as gaps rather than deliberate choices.
- debugging-01: The case mismatch causes the error `KeyError: 'Port'`.
- debugging-01: The corrected `get_url(cfg)` function returns the f-string `f"http://{cfg['host']}:{cfg['port']}/api"`.
- debugging-02: Class bodies are implicitly in strict mode.
- debugging-02: Inside the callback, `this` is `undefined`.
- debugging-02: `this.seconds += 1` should throw `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: `this.seconds += 1` should not log `NaN`.
- debugging-02: `setInterval(function () { ... }.bind(this), 1000)` is an alternative fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-04: The non-ASCII byte occurs at byte offset 512 in the file.
- debugging-04: The ascii codec rejects any byte greater than or equal to 0x80.
- debugging-04: The matching encoding is almost always UTF-8.
- debugging-04: Encoding can be detected at runtime instead of hardcoded.
- debugging-06: The working directory contains no files.
- debugging-06: A "pool exhausted" error means the job could not obtain a connection from its database connection pool within 30 seconds.
- debugging-06: A "pool exhausted" error does not indicate that the database was slow to execute a query.
- debugging-06: The error indicates contention for the connection pool rather than slowness of the query.
- debugging-06: Static configuration bugs do not usually produce intermittent failures.
- debugging-06: The observed failure window is 02:13:30 to 02:14:41.
- debugging-06: Postgres exposes connection state through pg_stat_activity, including application_name and state columns.
- debugging-06: pgbouncer and HikariCP are pool layers that can expose active and idle connection counts.
- debugging-06: A connection leak would show pool usage trending upward over the night rather than spiking suddenly.
- debugging-06: Log retention for the services is currently 7 days or less.
- debugging-06: The export job raises a TimeoutError when it fails to acquire a connection.
- debugging-06: A dedicated pool or connection budget for the export job can be configured via a separate pgbouncer pool or a database role with a max_connections reservation.
- debugging-07: Cross-test contamination from shared state is the classic pytest-xdist flake pattern.
- debugging-07: A silent write failure is a leading suspect for the failure.
- debugging-07: A rate limit, connection pool exhaustion, or transient error on the third seed call could go unnoticed if the test assumes a 201 or 200 response without asserting on it.
- debugging-07: Database read-replica lag or a stale MVCC snapshot is a less likely cause but worth ruling out.
- debugging-07: Read-replica lag or a stale MVCC snapshot could occur if the digest read hits a different connection or replica than the writes.
- debugging-07: Running `pytest -n 4` or higher locally in a loop can help narrow down the cause.
- debugging-07: If the test never flakes when run locally in a loop with parallelism, that points more toward CI-specific resource contention than a pure logic bug.
- debugging-07: Asserting on the response status of all three seed calls instead of assuming success would quickly rule the silent write failure case in or out.
- debugging-07: Temporarily adding a retry or poll-with-timeout around the digest read, fetching until the count stabilizes or times out, is a diagnostic step.
- debugging-07: Most CI systems still capture stdout even without artifact storage.
- debugging-07: If the digest query uses a time window or a delayed-propagation index, that is almost certainly the root cause given the load-dependent symptom.
- debugging-07: The retry/poll experiment is the fastest way to confirm or rule out the async race.
- debugging-07: The async race is the most likely explanation given the parallelism-only correlation.
- debugging-08: The working directory is empty and contains no code.
- debugging-08: Because no code is present, the question is a pure diagnostic-reasoning question.
- debugging-08: Memory growth that persists through quiet nights rules out a diurnal working-set effect such as daytime cache warming or delayed GC.
- debugging-08: The observed pattern means reachable objects are actually accumulating.
- debugging-08: A correctly functioning bounded cache would plateau rather than show continuous growth.
- debugging-08: The correlation with campaigns indicates the traffic-proportional leak scales with webhook content or diversity rather than raw request count.
- debugging-08: Campaigns typically change payload shape and cardinality more than they change raw request volume.
- debugging-08: A size-bounded cache with correct eviction cannot grow past its bound.
- debugging-08: Examples of unbounded-cardinality tracking include metrics labels, log context fields, per-order caches, and idempotency-key maps.
- debugging-08: Campaigns introduce new promo codes, SKUs, and campaign IDs.
- debugging-08: Using request-derived values as map keys or metric labels without eviction produces a leak that scales with distinct traffic.
- debugging-08: A leak scaling with distinct traffic matches the observation of faster growth in campaign weeks better than one scaling with raw request count.
- debugging-08: A check for cause 1 is to grep for metrics and logging calls that use request-derived values such as campaign_id, order_id, or sku as labels or map keys.
- debugging-08: A check for cause 1 is to confirm those structures have bounded cardinality or TTL eviction.
- debugging-08: A check for cause 1 is to compare distinct campaign and SKU counts against the memory growth rate across several weeks.
- debugging-08: Campaign products carry more images and fields, making entries larger.
- debugging-08: Other eviction failures include a weigher or size function that under-counts, and a secondary index or listener list that mirrors the cache without its own bound.
- debugging-08: A check for cause 2 is to instrument the cache to track live entry count, total weight, and eviction count over the day.
- debugging-08: If cache entry count stays flat while heap keeps climbing, the cache is not the cause.
- debugging-08: If eviction count stalls while insert count climbs, eviction is broken.
- debugging-08: Examples of webhook-path resource leaks include unclosed HTTP connections or streams, retry timers, per-event listeners never removed, and queues growing under backpressure.
- debugging-08: A check for cause 3 is to load-test the canary with synthetic webhook traffic including campaign-shaped payloads while watching connection counts, thread counts, and open file descriptors.
- debugging-08: Usual suspects for a baseline leak include scheduled or background jobs such as health checks, connection-pool keepalive, TLS session cache, DNS cache, and log buffers.
- debugging-08: Usual suspects for a baseline leak also include runtime-level growth such as metaspace from dynamic class or proxy generation, thread-stack retention, and native or off-heap buffers not tracked by heap size.
- debugging-08: A check for cause 4 is to run the canary alone and take heap dumps or object-count snapshots at fixed intervals.
- debugging-08: Step-shaped growth correlates with a cron or schedule, while smooth growth does not.
- debugging-08: No heap profile currently exists for the system.
- debugging-08: Taking heap dumps on the canary is the highest-leverage next step.
- debugging-08: Heap dumps on the canary isolate the baseline leak (cause 4) from causes 1 through 3.
- debugging-08: Diffing heap histograms across a few hours will likely reveal whether the leak is at the JVM/runtime level or in an application-level collection.
- explanation-01: A hash map stores key-value pairs.
- explanation-01: Collisions are inevitable because the array has a limited number of slots.
- explanation-01: Collisions remain a matter of probability even with a good hash function.
- explanation-01: The probability math behind hash collisions is the same as the birthday problem.
- explanation-01: The collection in a separate-chaining bucket is usually a linked list, and sometimes a tree or dynamic array.
- explanation-01: Quadratic probing tries index + 1 squared, index + 2 squared, and so on.
- explanation-01: Quadratic probing reduces clustering.
- explanation-01: An open-addressed array must be resized before it fills up completely, because you cannot insert into a full array.
- explanation-01: Deletion in separate chaining is easy: remove the node from the list.
- explanation-01: Deletion in open addressing cannot simply empty the slot, as that would break probe chains for other entries.
- explanation-01: Deletion in open addressing usually needs a tombstone marker.
- explanation-01: Chaining is simpler to reason about and tolerates high load factors better.
- explanation-01: Open addressing is more complex to implement correctly, especially deletion.
- explanation-01: Most general-purpose hash maps use chaining.
- explanation-01: Java's HashMap uses chaining.
- explanation-01: Java's HashMap upgrades long chains to trees for worst-case performance.
- explanation-01: Python's dict uses open addressing.
- explanation-01: Many high-performance C++ hash maps use open addressing.
- explanation-01: Open addressing is chosen in those implementations for memory and cache benefits.
- explanation-02: Collaborative editing, CMS records, and REST APIs with 'last write wins' semantics via ETags are examples suited to optimistic locking.
- explanation-03: The receiver's advertised window caps data based on the receiver's buffer space.
- explanation-03: Historically, the initial cwnd was 1 segment.
- explanation-03: Modern implementations typically start with a cwnd of around 10 segments (~14KB).
- explanation-03: A connection that encounters congestion backs off after just one or two round trips rather than many.
- explanation-03: If loss is detected after congestion avoidance begins, the sender cuts its rate back down.
- explanation-04: A process is an independent instance of a running program.
- explanation-04: A process has its own memory address space, file descriptors, and OS resources.
- explanation-04: All threads in a process share the same address space, heap, and file descriptors.
- explanation-04: Each thread has its own stack and register state.
- explanation-04: A supervisor can restart a crashed process.
- explanation-04: nginx uses worker processes.
- explanation-04: Job queues often use processes.
- explanation-04: Separate processes each get their own Python interpreter and GIL.
- explanation-04: Python's multiprocessing module uses processes and the threading module uses threads.
- explanation-04: The OS can apply separate memory limits, CPU quotas, priorities, and cgroups per process.
- explanation-04: Per-process resource limits are useful for sandboxing untrusted code.
- explanation-04: Per-process resource limits can prevent one workload from starving others.
- explanation-04: Chrome's renderer processes run with fewer privileges than the browser process.
- explanation-04: High-throughput I/O-bound servers and GUI event loops with background work are cases where threads fit better.
- explanation-04: Shared memory between threads avoids the cost of IPC such as pipes, sockets, and serialization.
- explanation-04: Separate processes require IPC to communicate.
- explanation-05: Program roots include globals, the stack, and active closures.
- explanation-05: Examples of long-lived objects include a global event bus and a DOM element.
- explanation-05: Garbage collection prevents dangling pointers.
- explanation-06: A slow API can be caused by lock contention.
- explanation-06: A slow API can be caused by an inefficient endpoint doing unnecessary work.
- explanation-06: Stale data served after writes is a classic source of confusing production issues.
- explanation-06: Redis is an example of a service added when introducing a cache.
- explanation-06: Caching requires deciding how fresh cached data needs to be.
- explanation-06: Deciding cache freshness is a product or business decision, not just a technical one.
- explanation-07: Modern NVMe-backed cloud instances make multi-terabyte single-instance Postgres more feasible.
- explanation-07: Sharding only addresses write throughput and total storage exceeding one machine's practical limits.
- explanation-07: Sharding does not fix badly performing queries.
- explanation-07: Sharding does not fix connection exhaustion.
- explanation-07: Relevant metrics to collect before deciding include rows/day, GB/month, and QPS trend.
- explanation-07: Cross-shard limitations force application-level workarounds such as denormalization and distributed transactions, which introduce bugs.
- explanation-07: Growth instrumentation should track storage per month, QPS per month, and table-level growth.
- explanation-07: Suggested thresholds for revisiting the sharding decision are approaching the low hundreds of GB to TB range, or write throughput saturating a single primary.
- explanation-08: The improvement could be anywhere from 2% to 60%, depending on payload size and where request time is actually spent.
- explanation-08: Large payloads, high request rates, and tight latency budgets are conditions under which serialization takes a large share of request time.
- explanation-08: Binary formats often produce larger gains in wire size than in CPU time.
- explanation-08: Wrapping existing JSON encode/decode calls with a timer for a day is a cheap way to obtain real measurements.
- explanation-08: Running a benchmark on a representative payload sample comparing the language's JSON library against a candidate binary format is a cheap way to obtain real measurements.
- summarization-02: The incorrect pool size exhausted the database connection pool.
- summarization-02: The incident caused approximately 12% checkout errors.
- summarization-02: The incident ran from 09:14 to 09:48 UTC.
- summarization-03: Under the proposal, uploads would save the original image.
- summarization-03: The worker would update the record when thumbnail generation is done.
- summarization-04: The Reports page has an "Export" button that offers PDF and CSV options.
- summarization-04: Clicking the Export button and choosing the PDF option initially results in nothing happening.
- summarization-07: The task is a straightforward summarization task requiring no prior context.
- summarization-08: Suggested follow-up remedies include adding progress indicators or time estimates.
- summarization-08: The admin-versus-regular-user default settings observation was not included as a top-3 finding because it is too weak to act on.

Added facts (styled only):

- code-review-01: `name` isn't checked for type, emptiness, or duplicates before insertion.
- code-review-01: Appending `"member"` unconditionally means callers can't create a user without that role.
- code-review-02: Because `fetch` does not reject on HTTP error statuses, a bad request silently produces malformed `data`.
- code-review-02: Without a `res.ok` check, calling `res.json()` on an error page (such as an HTML 404 page) throws a confusing parse error instead of a clear "request failed" message.
- code-review-02: The corrected implementation awaits `fetch(`/api/users/${userId}`)`, throws an `Error` with the status when `res.ok` is false, awaits `res.json()`, and returns `data.name.toUpperCase()`.
- code-review-03: `SELECT *` retrieves every column even when callers need only a few.
- code-review-03: The function assumes `cursor` is a valid, open connection.
- code-review-03: Not managing the connection lifecycle inside the function may be acceptable if callers already manage it.
- code-review-04: A stale write from `increment()` can overwrite a `reset()`, leaving `value` at 1 instead of 0.
- code-review-04: In the fixed version, `__init__` sets `self.value = 0` and creates `self._lock = threading.Lock()`.
- code-review-04: In the fixed version, `increment()` executes `self.value += 1` inside a `with self._lock:` block.
- code-review-04: In the fixed version, `reset()` executes `self.value = 0` inside a `with self._lock:` block.
- code-review-05: When no `.log` files exist, the loop silently does nothing, which is noisy but harmless.
- code-review-05: `echo Cleaned $BACKUP_DIR` is unquoted, a minor issue that is inconsistent with fixing quoting elsewhere.
- code-review-05: The fixed version exits with status 1 and prints a usage message to stderr when `$BACKUP_DIR` is empty or is not a directory.
- code-review-06: A dict in `base` can be fully replaced by a non-dict in `override`, and vice versa, once fix #1 is applied.
- code-review-06: Strict type-matching would make the merge far more rigid.
- code-review-06: Problems #1 and #2 are correctness bugs rather than style issues.
- code-review-06: Problems #4, #5, and #6 are likely deliberate behaviors.
- code-review-07: The helper hides failures in three different ways depending on which branch is taken.
- code-review-07: The inconsistency between the failure paths is the core problem with the helper.
- code-review-07: The backoff calculation has an off-by-one error.
- code-review-07: The backoff was almost certainly intended to be 1000 * (i + 1).
- code-review-07: Comparisons against undefined always evaluate to false.
- code-review-07: When attempts <= 0, fn is never called.
- code-review-07: When attempts <= 0, the function returns undefined without trying.
- code-review-07: Nothing in the shown code validates the attempts parameter.
- code-review-07: Treating unrecognized errors as immediately fatal could be a deliberate 'fail closed, don't retry unknown error types' choice.
- code-review-07: A deliberate fail-closed design should check explicitly for the absence of .status.
- code-review-07: The current code relies on undefined >= 500 being falsy.
- code-review-07: The immediate-first-retry behavior reads more like an off-by-one than a design choice.
- code-review-07: The safest read is to assume nothing in the helper is deliberate except possibly the 'never throw' behavior.
- code-review-07: The remaining behaviors should be treated as bugs to fix rather than behavior to preserve.
- code-review-08: When the loop crashes, the caller loses even the partial 'removed' count.
- code-review-08: Temp and partial files are usually treated as safe to sweep.
- code-review-08: With no minimum-age buffer, deleting .part files is a live race unless the writer guarantees atomic rename-into-place.
- code-review-08: The asymmetry between the two branches' caps is undocumented in the code.
- code-review-08: The script permanently destroys data on a schedule that nobody currently owns.
- code-review-08: Items 4, 5, and 6 are likely deliberate but unverified.
- code-review-08: Item 1 depends entirely on how the scheduler runs the script.
- code-review-08: Items 2, 3, and 7 are almost certainly bugs rather than design decisions.
- debugging-01: Line 4 looks up cfg['Port'] with a capitalized P.
- debugging-02: When a regular function is invoked as a plain function, `this` becomes the global object.
- debugging-02: Incrementing `this.seconds` in the regular-function callback produces `NaN`.
- debugging-04: errors="ignore" is a valid value for the errors argument of open().
- debugging-05: In the fixed version, the parameter defaults to `None` and the list is built inside the function body with `tags = list(tags) if tags is not None else ["draft"]`.
- debugging-06: The connection pool recovers within a minute.
- debugging-06: Retry attempt 2 also fails, after which the job gives up.
- debugging-06: In a leak scenario, each retry checks out a new connection without the failed connection being returned.
- debugging-06: Queries blocked on locks sit on a connection while waiting.
- debugging-06: A transient network blip could cause connections to hang rather than close cleanly, reducing the effective pool size.
- debugging-06: Instrumenting the export job's pool size, in-use count, and queue depth on every checkout would distinguish a connection leak from external contention.
- debugging-06: If failures continue after giving the export job a dedicated pool, the leak or undersizing explanation is correct.
- debugging-06: Current log retention captures only the last two lines of the failure window.
- debugging-07: Parallelism-driven state leakage is the most likely cause of the flake.
- debugging-07: The digest query likely lacks proper isolation.
- debugging-07: If the digest pulls events by time window rather than by a scoped key such as user ID or session ID, a parallel worker's seeded events could crowd out the test's events.
- debugging-07: Running the suite with `-n 1` uses a single worker.
- debugging-07: If the flake disappears under a single worker, the cause is shared state or worker contention rather than a pure timing bug in the digest logic.
- debugging-07: pytest-xdist supports a `--dist=loadscope` distribution mode.
- debugging-07: A per-worker database URL can be keyed on the `PYTEST_XDIST_WORKER` environment variable.
- debugging-07: pytest-xdist provides a `@pytest.mark.xdist_group` marker.
- debugging-07: The failing test is named `test_digest_contains_all_events`.
- debugging-07: Asserting write durability before requesting the digest can be done by polling for the record or using `select_for_update`/read-your-writes consistency.
- debugging-07: A mock of `datetime.now()` could be accidentally shared or reset by a concurrent test in the same process.
- debugging-07: Running the suite with a single worker is a cheap first diagnostic step.
- debugging-08: Campaign-time acceleration tracks rising order volume, not just webhook count.
- debugging-08: The canary result only rules out webhooks, not orders.
- debugging-08: If cache entry count is flat but memory rises, the cause is size drift or a retention bug in eviction rather than the bound itself.
- debugging-08: Allocator/GC fragmentation is mostly ruled out.
- debugging-08: Fragmentation usually appears as memory that does not return to the OS but stops growing once allocation patterns stabilize.
- debugging-08: Fragmentation would not typically keep ratcheting up through quiet nights with no new large allocations.
- debugging-08: Checking for fragmentation is cheap.
- debugging-08: If RSS tracks live object size closely, the problem is a real leak rather than fragmentation.
- debugging-08: Diffing /proc/<pid>/smaps or pmap segments before and after a campaign day shows whether growth is inside or outside the heap.
- debugging-08: The canary comparison and the growth-versus-volume correlation are cheap checks.
- debugging-08: Those two checks will reveal whether one leak or two is being chased.
- explanation-02: An example optimistic update statement is: UPDATE products SET price = 20, version = 6 WHERE id = 42 AND version = 5.
- explanation-02: An example pessimistic locking statement is: SELECT * FROM accounts WHERE id = 1 FOR UPDATE.
- explanation-02: Pessimistic locking suits workflows where retries are expensive or user-visible.
- explanation-02: Optimistic locking should be the default choice.
- explanation-03: At the start of a connection, a fast local link, a congested backbone, and a slow satellite hop are indistinguishable to the sender.
- explanation-03: Early TCP implementations sent as much data as the receiver's window allowed.
- explanation-03: Sending as much data as the receiver's window allowed caused congestion collapse on the early internet.
- explanation-03: Congestion collapse involved too many senders sending at full speed into shared links, routers dropping packets, and senders retransmitting.
- explanation-03: The ssthresh threshold is left over from a previous slowdown.
- explanation-04: Creating a process duplicates memory and resources.
- explanation-04: Flaky plugins, browser tabs, and workers running untrusted code are examples of work that might crash or leak memory.
- explanation-04: Python and Ruby threads cannot run Python/Ruby bytecode on multiple cores at once because of the global interpreter lock.
- explanation-04: Threads still help with I/O-bound work in languages with a GIL because I/O releases the lock.
- explanation-06: Writes still have to hit the database even when a cache is present.
- explanation-06: Writes often have to hit the cache as well in order to stay consistent.
- explanation-06: Slowness can be caused by network latency.
- explanation-06: Profiling a service with an APM tool or coarse timing logs shows whether time goes to app code, network, or database.
- explanation-07: Sharding solves single-node CPU and memory limits.
- explanation-07: Sharding is the wrong tool when the real problem is disk size or read load.
- explanation-07: Growth projections at 6, 12, and 24 months should be requested from the product team.
- explanation-08: Serialization accounting for 40% of request time is common for large, deeply nested payloads.
- explanation-08: Binary formats provide the greatest benefit on numeric-heavy or repetitive data.
- explanation-08: The performance gap between binary formats and JSON narrows for payloads consisting mostly of short strings.
- explanation-08: Reducing wire size only helps if bandwidth, rather than CPU, is the bottleneck.
- explanation-08: Migrating to a binary format carries costs including schema management, tooling, and debugging friction.
- summarization-02: A page was sent at 09:21.
- summarization-02: The team caught the issue within 7 minutes.
- summarization-02: A rollback was completed by 09:48.
- summarization-02: Detection and response worked well during the incident.
- summarization-04: The Reports page has a month selector (e.g., March can be selected).
- summarization-05: Ada is to run the payments database migration dry run.
- summarization-07: The worker crash could stem from staging's newer kernel.
- summarization-07: Staging runs a newer kernel than production.
- summarization-08: Both of the possible gaps need follow-up before the team acts on them.

### classic-concise

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 25 | 24 | 0.96 | 22 | 1 |
| code-review-02 | 23 | 13 | 0.565 | 12 | 3 |
| code-review-03 | 26 | 15 | 0.577 | 16 | 3 |
| code-review-04 | 26 | 15 | 0.577 | 17 | 6 |
| code-review-05 | 27 | 20 | 0.741 | 35 | 9 |
| code-review-06 | 39 | 28 | 0.718 | 24 | 3 |
| code-review-07 | 43 | 31 | 0.721 | 30 | 7 |
| code-review-08 | 36 | 28 | 0.778 | 31 | 5 |
| debugging-01 | 8 | 7 | 0.875 | 7 | 0 |
| debugging-02 | 20 | 13 | 0.65 | 8 | 2 |
| debugging-03 | 11 | 8 | 0.727 | 4 | 0 |
| debugging-04 | 12 | 9 | 0.75 | 9 | 0 |
| debugging-05 | 20 | 20 | 1.0 | 13 | 3 |
| debugging-06 | 26 | 12 | 0.462 | 31 | 10 |
| debugging-07 | 30 | 15 | 0.5 | 27 | 13 |
| debugging-08 | 45 | 12 | 0.267 | 33 | 19 |
| explanation-01 | 39 | 29 | 0.744 | 26 | 2 |
| explanation-02 | 23 | 21 | 0.913 | 21 | 10 |
| explanation-03 | 33 | 25 | 0.758 | 23 | 6 |
| explanation-04 | 33 | 20 | 0.606 | 31 | 2 |
| explanation-05 | 18 | 14 | 0.778 | 16 | 0 |
| explanation-06 | 27 | 20 | 0.741 | 21 | 1 |
| explanation-07 | 30 | 15 | 0.5 | 24 | 10 |
| explanation-08 | 13 | 6 | 0.462 | 15 | 2 |
| summarization-01 | 6 | 6 | 1.0 | 5 | 0 |
| summarization-02 | 13 | 10 | 0.769 | 15 | 4 |
| summarization-03 | 14 | 14 | 1.0 | 12 | 0 |
| summarization-04 | 13 | 12 | 0.923 | 11 | 1 |
| summarization-05 | 9 | 9 | 1.0 | 10 | 1 |
| summarization-06 | 14 | 13 | 0.929 | 12 | 1 |
| summarization-07 | 16 | 15 | 0.938 | 14 | 3 |
| summarization-08 | 23 | 17 | 0.739 | 23 | 3 |

Median fraction: 0.742 over 32 scored pairs.

Median additions: 3.0 over 32 scored pairs.

Lost facts:

- code-review-01: The suggested fix raises `ValueError("name is required")` when `name` is falsy.
- code-review-02: The function does not properly return a promise representing the eventual value.
- code-review-02: `fetch` rejects only on network failure.
- code-review-02: The function does not handle malformed JSON.
- code-review-02: The function does not validate the shape of the response.
- code-review-02: The function assumes `data` always has a `.name` property.
- code-review-02: If the API returns an error object or unexpected shape, `.toUpperCase()` will throw.
- code-review-02: `userId` is not validated or sanitized.
- code-review-02: If `userId` can come from untrusted user input, it should be encoded with `encodeURIComponent(userId)`.
- code-review-02: Encoding `userId` avoids malformed URLs and injection into the URL path.
- code-review-02: The corrected version awaits `fetch` with `encodeURIComponent(userId)` in the URL.
- code-review-03: There is no prior memory stored for this project.
- code-review-03: Injection is the top OWASP vulnerability.
- code-review-03: The `status` parameter is not checked against a known set of valid statuses.
- code-review-03: Valid order statuses include open, shipped, and cancelled.
- code-review-03: Unvalidated status input causes typos or bad data to silently return empty results.
- code-review-03: A database error from `cursor.execute` will propagate as a raw exception with no context about the query or inputs that caused it.
- code-review-03: The code has no type hints.
- code-review-03: The function signature gives no indication of expected types.
- code-review-03: Appropriate type hints for the function would be `cursor: Cursor, customer_name: str, status: str) -> list[tuple]`.
- code-review-03: The SQL injection is the only issue that actually matters in this code.
- code-review-03: The remaining issues are minor hardening or style points.
- code-review-04: The assignment `self.value = 0` is itself atomic in CPython.
- code-review-04: The atomicity of `self.value = 0` in CPython is due to the GIL.
- code-review-04: A plain attribute read of `counter.value` is safe from torn reads in CPython.
- code-review-04: A plain attribute read of `counter.value` is not safe from being logically stale between check and use in calling code.
- code-review-04: Individual bytecode operations are atomic in CPython.
- code-review-04: The correctness of the original code depends on incidental interpreter details rather than an actual contract.
- code-review-04: Relying on GIL semantics is fragile.
- code-review-04: The original code would break under free-threaded/no-GIL Python builds.
- code-review-04: The original code would break under PyPy under some conditions.
- code-review-04: The fixed version uses `with self._lock` in `increment`, `reset`, and the `value` property.
- code-review-04: The fixed version gives callers a safe way to read the current value.
- code-review-05: With a missing argument, the script runs `rm -rf *.tmp` in the user's home directory, causing silent data loss.
- code-review-05: If no `*.log` files exist, `ls *.log` prints an error to stderr.
- code-review-05: The script prints "Cleaned $BACKUP_DIR" regardless of whether any operation actually succeeded.
- code-review-05: The final success message is misleading because it prints even on partial or total failure.
- code-review-05: `gzip $f` will fail or prompt if a `.gz` file of the same name already exists.
- code-review-05: The script provides no `-f` flag or other handling for a pre-existing `.gz` file.
- code-review-05: The script performs no sanity check on the directory argument, such as rejecting `.` or `/`.
- code-review-06: The code uses `merged.pop(key, None)` when an override value is `None`.
- code-review-06: Treating `None` as a delete sentinel is a common convention in layered config systems such as Helm and Ansible.
- code-review-06: `merged.pop(key, None)` makes deleting a key that does not exist in `base` a silent no-op.
- code-review-06: The silent no-op on a missing key can mask a typo'd key name with no error or warning.
- code-review-06: The resulting stack trace is far from the actual mistake and is confusing.
- code-review-06: Merging lists is ambiguous because it is unclear whether to append, dedupe, or merge by index.
- code-review-06: The function performs no validation of the top-level `base` and `override` types.
- code-review-06: If `base` is not dict-like, `dict(base)` may raise a strange error.
- code-review-06: If `base` is an iterable of pairs, such as a list of tuples, `dict(base)` may silently succeed instead of failing clearly.
- code-review-06: The lack of top-level type validation is likely an oversight and warrants an explicit type check with a clear error message.
- code-review-06: The silent no-op when deleting a missing key is a side effect of the `None`-as-sentinel design rather than a separately chosen behavior.
- code-review-07: Swallowing non-retryable errors hides bugs and is the most dangerous problem in the code.
- code-review-07: Exponential backoff would be expressed as something like 1000 * 2 ** i.
- code-review-07: Lack of jitter is a classic retry-logic mistake.
- code-review-07: Plain Error objects, thrown strings, and fetch network failures do not set a .status property.
- code-review-07: The code uses attempts = 3 with a loop condition of i < attempts.
- code-review-07: attempts = 3 with i < attempts yields 3 total tries and 2 waits.
- code-review-07: The distinction between '3 attempts' and '3 retries' is a common source of off-by-one confusion downstream.
- code-review-07: A cache-warming job that should not crash a pipeline is an example of a caller that might want fail-soft behavior.
- code-review-07: Retrying 429 and 5xx but not other 4xx is a defensible retry policy.
- code-review-07: 429 and 5xx errors are classically transient while other 4xx errors are not.
- code-review-07: The retry policy is reasonable even though its implementation swallows errors instead of throwing.
- code-review-07: The biggest risk in the function is that it can never throw, not the backoff math.
- code-review-08: The tmp-/.part deletion should almost certainly have an age threshold, such as only removing files older than an hour.
- code-review-08: A broken symlink or a permissions error will raise an exception and abort clean() entirely.
- code-review-08: os.listdir returns entries in filesystem-dependent order, not sorted by age.
- code-review-08: When the 500-item cap takes effect, it does not necessarily remove the oldest 500 files, just the first 500 in directory order.
- code-review-08: ROOT is a hardcoded absolute path with no override mechanism.
- code-review-08: The hardcoded ROOT makes the script hard to test safely without editing the source.
- code-review-08: The person reviewing the script did not set up its schedule.
- code-review-08: The module-level CUTOFF is almost certainly an oversight rather than a deliberate choice.
- debugging-01: The corrected `get_url(cfg)` function returns the f-string `f"http://{cfg['host']}:{cfg['port']}/api"`.
- debugging-02: Class bodies are implicitly in strict mode.
- debugging-02: Inside the callback, `this` is `undefined`.
- debugging-02: `this.seconds += 1` should throw `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: `this.seconds += 1` should not log `NaN`.
- debugging-02: If `NaN` is observed instead of a thrown error, the callback is likely not running in strict mode in that setup.
- debugging-02: `setInterval(function () { ... }.bind(this), 1000)` is an alternative fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-03: The buggy loop skips the final window `[3, 4]`.
- debugging-03: The window `[3, 4]` has a sum of 7.
- debugging-03: With the fix, `moving_sum([1, 2, 3, 4], 2)` returns `[3, 5, 7]`.
- debugging-04: The non-ASCII byte occurs at byte offset 512 in the file.
- debugging-04: The matching encoding is almost always UTF-8.
- debugging-04: charset-normalizer and chardet are libraries that detect character encoding.
- debugging-06: The working directory contains no files.
- debugging-06: A "pool exhausted" error means the job could not obtain a connection from its database connection pool within 30 seconds.
- debugging-06: A "pool exhausted" error does not indicate that the database was slow to execute a query.
- debugging-06: The failures occur roughly once a week.
- debugging-06: Static configuration bugs do not usually produce intermittent failures.
- debugging-06: A connection leak would explain failures not tied to a specific batch and would explain why retries also fail.
- debugging-06: A long-running or blocking analytics query holding locks could cause export queries to queue for connections instead of failing fast on lock wait.
- debugging-06: The observed failure window is 02:13:30 to 02:14:41.
- debugging-06: Postgres exposes connection state through pg_stat_activity, including application_name and state columns.
- debugging-06: pgbouncer and HikariCP are pool layers that can expose active and idle connection counts.
- debugging-06: "idle in transaction" is a Postgres connection state.
- debugging-06: The relevant logs are rotated away before they can be examined.
- debugging-06: Log retention for the services is currently 7 days or less.
- debugging-06: The export job raises a TimeoutError when it fails to acquire a connection.
- debugging-07: Slower and more variable execution causes a race window to open more often.
- debugging-07: Cross-test contamination from shared state is the classic pytest-xdist flake pattern.
- debugging-07: If the digest filters events by a timestamp window such as 'last N minutes' or a bucket boundary, slow seeding under load could push the third event's timestamp just outside the window.
- debugging-07: A rate limit, connection pool exhaustion, or transient error on the third seed call could go unnoticed if the test assumes a 201 or 200 response without asserting on it.
- debugging-07: Database read-replica lag or a stale MVCC snapshot is a less likely cause but worth ruling out.
- debugging-07: If the test never flakes when run locally in a loop with parallelism, that points more toward CI-specific resource contention than a pure logic bug.
- debugging-07: Asserting on the response status of all three seed calls instead of assuming success would quickly rule the silent write failure case in or out.
- debugging-07: Temporarily adding a retry or poll-with-timeout around the digest read, fetching until the count stabilizes or times out, is a diagnostic step.
- debugging-07: If a retry/poll around the digest read fixes the failure, it confirms an async race and indicates where to add proper synchronization rather than a test-side workaround.
- debugging-07: Grepping for fixture scope on anything shared between tests, such as `scope="session"` fixtures, global DB truncation, or shared tenant IDs, is a diagnostic step.
- debugging-07: If shared-scope fixtures are found, they should be scoped per-test or per-worker.
- debugging-07: Most CI systems still capture stdout even without artifact storage.
- debugging-07: If the digest query uses a time window or a delayed-propagation index, that is almost certainly the root cause given the load-dependent symptom.
- debugging-07: The retry/poll experiment is the fastest way to confirm or rule out the async race.
- debugging-07: The async race is the most likely explanation given the parallelism-only correlation.
- debugging-08: The working directory is empty and contains no code.
- debugging-08: Because no code is present, the question is a pure diagnostic-reasoning question.
- debugging-08: Memory growth that persists through quiet nights rules out a diurnal working-set effect such as daytime cache warming or delayed GC.
- debugging-08: The observed pattern means reachable objects are actually accumulating.
- debugging-08: A correctly functioning bounded cache would plateau rather than show continuous growth.
- debugging-08: The canary evidence implies at least two leaks: a baseline leak independent of traffic and a traffic-proportional leak.
- debugging-08: The correlation with campaigns indicates the traffic-proportional leak scales with webhook content or diversity rather than raw request count.
- debugging-08: Campaigns typically change payload shape and cardinality more than they change raw request volume.
- debugging-08: The cache bound has been unchanged for a year.
- debugging-08: A size-bounded cache with correct eviction cannot grow past its bound.
- debugging-08: Unbounded-cardinality tracking keyed by request or campaign data is the highest-suspicion cause of the traffic-proportional growth.
- debugging-08: Examples of unbounded-cardinality tracking include metrics labels, log context fields, per-order caches, and idempotency-key maps.
- debugging-08: Campaigns introduce new promo codes, SKUs, and campaign IDs.
- debugging-08: Using request-derived values as map keys or metric labels without eviction produces a leak that scales with distinct traffic.
- debugging-08: A leak scaling with distinct traffic matches the observation of faster growth in campaign weeks better than one scaling with raw request count.
- debugging-08: A check for cause 1 is to grep for metrics and logging calls that use request-derived values such as campaign_id, order_id, or sku as labels or map keys.
- debugging-08: A check for cause 1 is to confirm those structures have bounded cardinality or TTL eviction.
- debugging-08: A check for cause 1 is to compare distinct campaign and SKU counts against the memory growth rate across several weeks.
- debugging-08: An unchanged cache bound does not mean eviction is working.
- debugging-08: Other eviction failures include a weigher or size function that under-counts, and a secondary index or listener list that mirrors the cache without its own bound.
- debugging-08: If cache entry count stays flat while heap keeps climbing, the cache is not the cause.
- debugging-08: If eviction count stalls while insert count climbs, eviction is broken.
- debugging-08: A check for cause 3 is to load-test the canary with synthetic webhook traffic including campaign-shaped payloads while watching connection counts, thread counts, and open file descriptors.
- debugging-08: A check for cause 3 is to take heap dumps before and after a traffic burst and diff object histograms for the fastest-growing type.
- debugging-08: A baseline leak independent of webhooks would explain why the canary grows with zero webhook traffic.
- debugging-08: Usual suspects for a baseline leak include scheduled or background jobs such as health checks, connection-pool keepalive, TLS session cache, DNS cache, and log buffers.
- debugging-08: Usual suspects for a baseline leak also include runtime-level growth such as metaspace from dynamic class or proxy generation, thread-stack retention, and native or off-heap buffers not tracked by heap size.
- debugging-08: A check for cause 4 is to run the canary alone and take heap dumps or object-count snapshots at fixed intervals.
- debugging-08: Step-shaped growth correlates with a cron or schedule, while smooth growth does not.
- debugging-08: A check for native memory issues is to monitor native memory tracking, thread count, and file descriptor count over time.
- debugging-08: Taking heap dumps on the canary is the highest-leverage next step.
- debugging-08: Heap dumps on the canary isolate the baseline leak (cause 4) from causes 1 through 3.
- debugging-08: Diffing heap histograms across a few hours will likely reveal whether the leak is at the JVM/runtime level or in an application-level collection.
- explanation-01: A hash map stores key-value pairs.
- explanation-01: A slot in a hash map's array is called a bucket.
- explanation-01: Collisions are inevitable because the array has a limited number of slots.
- explanation-01: Collisions remain a matter of probability even with a good hash function.
- explanation-01: The probability math behind hash collisions is the same as the birthday problem.
- explanation-01: The collection in a separate-chaining bucket is usually a linked list, and sometimes a tree or dynamic array.
- explanation-01: Quadratic probing tries index + 1 squared, index + 2 squared, and so on.
- explanation-01: Quadratic probing reduces clustering.
- explanation-01: Java's HashMap upgrades long chains to trees for worst-case performance.
- explanation-01: Many high-performance C++ hash maps use open addressing.
- explanation-02: A pessimistic lock blocks other transactions from reading or writing that row until the lock is released.
- explanation-02: Collaborative editing, CMS records, and REST APIs with 'last write wins' semantics via ETags are examples suited to optimistic locking.
- explanation-03: If a sender immediately sent data at the rate the receiver's window allows, it could overwhelm a router or link along the path.
- explanation-03: The congestion window caps how much unacknowledged data the sender may have in flight.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The receiver's advertised window caps data based on the receiver's buffer space.
- explanation-03: Historically, the initial cwnd was 1 segment.
- explanation-03: A connection that encounters congestion backs off after just one or two round trips rather than many.
- explanation-03: If loss is detected after congestion avoidance begins, the sender cuts its rate back down.
- explanation-03: After cutting its rate, the sender often re-enters a slow-start-like ramp-up.
- explanation-04: Each thread has its own stack and register state.
- explanation-04: Threads are cheaper to create than processes.
- explanation-04: Communication between threads occurs through shared memory, with synchronization.
- explanation-04: nginx uses worker processes.
- explanation-04: Job queues often use processes.
- explanation-04: Python's multiprocessing module uses processes and the threading module uses threads.
- explanation-04: The OS can apply separate memory limits, CPU quotas, priorities, and cgroups per process.
- explanation-04: Per-process resource limits are useful for sandboxing untrusted code.
- explanation-04: Per-process resource limits can prevent one workload from starving others.
- explanation-04: Processes can run as different users with different permissions or sandboxes.
- explanation-04: Chrome's renderer processes run with fewer privileges than the browser process.
- explanation-04: Threads are preferable when creation and context-switch overhead matters.
- explanation-04: High-throughput I/O-bound servers and GUI event loops with background work are cases where threads fit better.
- explanation-05: Program roots include globals, the stack, and active closures.
- explanation-05: An example of an unbounded cache leak is caching results keyed by user session without evicting old sessions.
- explanation-05: Examples of long-lived objects include a global event bus and a DOM element.
- explanation-05: Garbage collection prevents dangling pointers.
- explanation-06: A slow API can be caused by an inefficient endpoint doing unnecessary work.
- explanation-06: Timing logs around DB calls versus total request time count as a form of profiling.
- explanation-06: Redis is an example of a service added when introducing a cache.
- explanation-06: Caching requires deciding how fresh cached data needs to be.
- explanation-06: Deciding cache freshness is a product or business decision, not just a technical one.
- explanation-06: The recommended second step is examining the read/write ratio and query patterns after confirming DB reads are the bottleneck.
- explanation-06: If reads do not dominate or are not repetitive, the fix is more likely query optimization, indexing, or reducing round trips.
- explanation-07: Modern NVMe-backed cloud instances make multi-terabyte single-instance Postgres more feasible.
- explanation-07: Sharding is very hard to undo once application code and data are split across shards.
- explanation-07: Data volume, write throughput, and connection/query concurrency are distinct growth problems with different fixes.
- explanation-07: Sharding does not fix connection exhaustion.
- explanation-07: Partitioning, better indexing, connection pooling, and vertical scaling are alternatives to try before sharding for write-heavy workloads.
- explanation-07: pgbouncer is a connection pooling tool for Postgres.
- explanation-07: Relevant metrics to collect before deciding include rows/day, GB/month, and QPS trend.
- explanation-07: The cost of sharding is high for teams without capacity to operate it, regardless of data size.
- explanation-07: A shard key chosen prematurely can turn out wrong as access patterns evolve, requiring a painful re-shard.
- explanation-07: Cross-shard limitations force application-level workarounds such as denormalization and distributed transactions, which introduce bugs.
- explanation-07: Vertical scaling has limits including a single-writer bottleneck, disk I/O, and vacuum falling behind on huge tables.
- explanation-07: Sharding under growth pressure leaves less time to choose a good shard key.
- explanation-07: Growth instrumentation should track storage per month, QPS per month, and table-level growth.
- explanation-07: Suggested thresholds for revisiting the sharding decision are approaching the low hundreds of GB to TB range, or write throughput saturating a single primary.
- explanation-07: Partitioning large tables, read replicas, connection pooling, and archiving cold data provide significant headroom without the commitment of sharding.
- explanation-08: The improvement could be anywhere from 2% to 60%, depending on payload size and where request time is actually spent.
- explanation-08: JSON parsing/serialization being a small share of request time is common when the bottleneck is database queries, network, or business logic.
- explanation-08: Large payloads, high request rates, and tight latency budgets are conditions under which serialization takes a large share of request time.
- explanation-08: Protobuf and msgpack are binary serialization formats.
- explanation-08: Binary formats often produce larger gains in wire size than in CPU time.
- explanation-08: Wrapping existing JSON encode/decode calls with a timer for a day is a cheap way to obtain real measurements.
- explanation-08: Running a benchmark on a representative payload sample comparing the language's JSON library against a candidate binary format is a cheap way to obtain real measurements.
- summarization-02: The production config template specifies a connection pool size of 50.
- summarization-02: The incorrect pool size exhausted the database connection pool.
- summarization-02: The incident ran from 09:14 to 09:48 UTC.
- summarization-04: The Reports page has an "Export" button that offers PDF and CSV options.
- summarization-06: The team has no evidence supporting the retry storm hypothesis.
- summarization-07: The task is a straightforward summarization task requiring no prior context.
- summarization-08: The field-mapping results are a solid signal for a small sample.
- summarization-08: The progress bar finding is characterized as TENTATIVE.
- summarization-08: The impact of the progress bar issue cannot be sized from only 3 data points.
- summarization-08: Suggested follow-up remedies include adding progress indicators or time estimates.
- summarization-08: The template gallery finding is characterized as TENTATIVE with an unclear cause.
- summarization-08: The admin-versus-regular-user default settings observation was not included as a top-3 finding because it is too weak to act on.

Added facts (styled only):

- code-review-01: The function has no default value for `db`.
- code-review-02: Because `fetch` does not reject on HTTP errors, `res.json()` is called on error response bodies as well.
- code-review-02: The corrected `loadProfile` awaits `fetch(`/api/users/${userId}`)` and stores the result in `res`.
- code-review-02: The corrected `loadProfile` throws an Error including the user ID and `res.status` when `res.ok` is false.
- code-review-03: `'; DROP TABLE orders; --` is an example of an SQL injection payload.
- code-review-03: Nothing in the code prevents empty strings from reaching the query.
- code-review-03: Nothing in the code prevents values of the wrong type from reaching the query.
- code-review-04: `reset` can overwrite an increment that happened concurrently.
- code-review-04: Both `increment` and `reset` are non-atomic operations.
- code-review-04: Both `increment` and `reset` look atomic despite not being atomic.
- code-review-04: The fixed `Counter.__init__` sets `self.value = 0`.
- code-review-04: The fixed `increment` performs `self.value += 1` inside a `with self._lock:` block.
- code-review-04: The fixed `reset` sets `self.value = 0` inside a `with self._lock:` block.
- code-review-05: The unquoted `rm -rf *.tmp` and `gzip $f` carry the same word-splitting/globbing risk as the unquoted `cd`.
- code-review-05: If `$1` is empty, `cd ""` fails silently.
- code-review-05: Adding `cd "$BACKUP_DIR" || exit 1` fixes the unchecked `cd`.
- code-review-05: With `nullglob` off, `*.tmp` expands literally to the string `*.tmp` and the command fails harmlessly.
- code-review-05: Behavior of an unmatched glob varies across `sh` implementations.
- code-review-05: If no `.log` files exist, the loop body runs once with `f` set to the literal string `*.log`.
- code-review-05: The literal `*.log` value causes `gzip` to fail on a nonexistent file.
- code-review-05: The script uses no POSIX-incompatible constructs, which is consistent with its `#!/bin/sh` shebang.
- code-review-05: The suggested rewrite uses `gzip -- "$f"` inside a `for f in *.log` loop.
- code-review-06: The merge is asymmetric: if `base[key]` is a dict but `override[key]` is not, the override replaces the whole subtree.
- code-review-06: The asymmetric-merge case and the crash case are the same code branch, not separate behaviors.
- code-review-06: The entire `elif` branch is buggy rather than intentional.
- code-review-07: The zero-backoff behavior is an off-by-one error, and the intent was probably `1000 * (i + 1)`.
- code-review-07: The code does not handle the `Retry-After` header for 429 responses.
- code-review-07: The code uses a guessed linear backoff instead of honoring the `Retry-After` header.
- code-review-07: The code has no logging or instrumentation, so retries and failures happen invisibly.
- code-review-07: The code has no timeout or abort mechanism if `fn` hangs.
- code-review-07: The wrapped function does not preserve `fn.name` or arity.
- code-review-07: Fixing the exhausted-retries case to return null consistently is safe.
- code-review-08: No consumer of the script's return value is shown.
- code-review-08: As written, the constants 45 and 500 are indistinguishable from typos.
- code-review-08: The unconditional, ageless deletion of `tmp-`/`.part` files is probably not deliberate.
- code-review-08: Trusting the ageless deletion requires confirming that the exporter always finishes and renames atomically.
- code-review-08: If the exporter does not rename atomically, the ageless deletion is a live-data-loss bug on slow writes.
- debugging-02: `this.seconds` is `undefined` inside the callback.
- debugging-02: `undefined + 1` evaluates to `NaN`.
- debugging-05: Python evaluates a default argument once, at function definition time.
- debugging-05: The fix uses `None` as a sentinel and copies the passed-in list.
- debugging-05: In the fixed version, `tags` is set to `list(tags)` when `tags` is not `None`, and to `["draft"]` otherwise.
- debugging-06: The failures are not caused by a bug in the export job itself.
- debugging-06: The varying batch number rules out a specific query as a cause.
- debugging-06: Retry amplification occurs when the export job retries failed batches while still holding or re-requesting connections.
- debugging-06: Retry amplification compounds pressure on the pool instead of backing off.
- debugging-06: Failover, lock contention, vacuum, and backup are examples of DB-side stalls.
- debugging-06: Querying the database directly during a live failure can help diagnose the issue.
- debugging-06: Retry backoff should be checked.
- debugging-06: Retrying after 1 second with no backoff adds load when the pool is already starved.
- debugging-06: The current retry behavior has attempt 2 retrying after 1 second.
- debugging-06: The fix is usually one of: raising the pool size, adding query timeouts on the analytics side, or splitting the pool so each service has a reserved minimum.
- debugging-07: A missing await can cause the digest read to fire before the writes commit.
- debugging-07: If the digest query is not scoped tightly enough, a worker running another test in parallel could interleave events.
- debugging-07: If the digest groups by timestamp or dedupes by a key, near-simultaneous events under parallel load could collide and be merged or dropped.
- debugging-07: Events colliding in the same millisecond or under the same idempotency key is a possible dedup collision mode.
- debugging-07: A write can be silently dropped while the API still returns success.
- debugging-07: The failing test is test_digest_contains_all_events in tests/test_notifications.py.
- debugging-07: pytest-repeat provides a --count option for repeating tests.
- debugging-07: The digest query may filter by a run-unique key such as user ID, session, or correlation ID, or by something coarser like a time window.
- debugging-07: A coarse time-window filter is something four parallel workers could collide on.
- debugging-07: If running CI with -n 1 drops the failure rate to zero, that confirms parallelism rather than test logic is the trigger.
- debugging-07: A failure rate that scales with worker count is evidence of shared-resource contention rather than a fixed race window.
- debugging-07: Starting with reproducing the concurrency plus adding targeted logging is the recommended first step.
- debugging-07: Without artifacts, diagnosing the failure amounts to guessing.
- debugging-08: Leaked per-request objects (listeners, timers, connections, promise chains) is the cause that best fits the evidence.
- debugging-08: Campaign weeks bring more webhook and API traffic.
- debugging-08: The canary presumably still serves other (non-webhook) requests.
- debugging-08: Daily memory growth rate can be correlated against request-count metrics rather than wall-clock days.
- debugging-08: If growth tracks request volume rather than calendar time, a per-request leak is likely the dominant driver.
- debugging-08: If cache entry count is flat while RSS rises, the cause is payload size or a metadata/key leak rather than eviction failure.
- debugging-08: Key cardinality explosion can exceed the effectiveness of an entry-count bound or cause thrashing that fragments memory.
- debugging-08: Distinct key count and cache hit rate can be logged daily.
- debugging-08: A falling cache hit rate combined with rising key churn points to cache key cardinality explosion.
- debugging-08: Compression buffers, HTTP client connection pools, and native image/codec libraries are sources of off-heap memory.
- debugging-08: Off-heap memory explains why quiet nights do not reclaim memory even when the heap itself would GC normally.
- debugging-08: pmap and /proc/[pid]/smaps deltas can help triage off-heap memory growth.
- debugging-08: jemalloc or tcmalloc native allocator stats can help triage off-heap memory growth, if those allocators are in use.
- debugging-08: Some runtimes retain memory pages after a logical free due to fragmentation, which resembles a slow leak.
- debugging-08: GC/fragmentation artifact is the least likely of the listed causes, given the canary evidence.
- debugging-08: Fragmentation alone would not explain the campaign correlation or the canary behavior.
- debugging-08: If forcing a GC drops RSS back toward baseline, the cause is fragmentation or GC laziness rather than a true leak.
- debugging-08: The service is restarted weekly.
- debugging-08: A single before/after weekly-restart heap dump diff, or continuous heap-vs-RSS plus request-count time series, would immediately rule one or two of the causes in or out.
- explanation-01: Chaining is simple and never fails.
- explanation-01: Rust's HashMap uses open addressing.
- explanation-02: In the example, an `orders` table has a `version` column.
- explanation-02: In the example, two clerks load order #42 at version 3.
- explanation-02: Clerk A's update `UPDATE orders SET status='shipped', version=4 WHERE id=42 AND version=3` succeeds.
- explanation-02: Clerk B runs the same query with `version=3`, but the row is now version 4, so the query matches zero rows.
- explanation-02: The application detects the zero-row update and asks Clerk B to reload and retry.
- explanation-02: Optimistic locking suits high-read, low-contention workloads such as web apps editing user profiles or shopping carts.
- explanation-02: A bank transfer example uses `SELECT balance FROM accounts WHERE id=1 FOR UPDATE`.
- explanation-02: Any other transaction trying to update or lock account 1 blocks until the first transaction commits or rolls back.
- explanation-02: Blocking other transactions makes both the debit and credit happen against a consistent balance.
- explanation-02: The rule of thumb is to use optimistic locking by default.
- explanation-03: When loss occurs, the sender backs off and switches to congestion avoidance.
- explanation-03: ssthresh stands for slow start threshold.
- explanation-03: ssthresh is an estimate of safe capacity derived from a prior loss event.
- explanation-03: Without slow start, a new connection would send data at whatever rate the application and OS buffers allow.
- explanation-03: Sending at an unrestrained rate can hurt every other connection sharing the link.
- explanation-03: Unrestrained sending caused real internet-wide congestion collapse in the 1980s.
- explanation-04: IPC mechanisms include pipes, sockets, and shared memory.
- explanation-04: Python and Ruby have a global interpreter lock.
- explanation-06: A cache does not help when slowness comes from network latency.
- explanation-07: Monthly GB growth over the last 6-12 months can be used to project future data size.
- explanation-07: Sharding does not fix bad queries, missing indexes, or lock contention.
- explanation-07: Bad queries, missing indexes, and lock contention get worse under sharding.
- explanation-07: Under sharding, queries, migrations, and constraints such as uniqueness and foreign keys require cross-shard coordination.
- explanation-07: Data grows unevenly across shards, requiring repeated rebalancing.
- explanation-07: Shard rebalancing is a live-migration problem.
- explanation-07: Vertical scaling and read replicas have ceilings.
- explanation-07: Hitting the ceilings of vertical scaling or read replicas without warning causes downtime.
- explanation-07: Scaling vertically and adding read replicas is the recommended action now.
- explanation-07: Deferring sharding gives the product team room to find product-market fit.
- explanation-08: If serialization is a small fraction of the total, the effort is better spent elsewhere.
- explanation-08: Migration costs of switching to a binary format include new schemas, tooling, debuggability tradeoffs, and client compatibility.
- summarization-02: The time from page to rollback was 34 minutes.
- summarization-02: Checkout requests failed for 7 minutes before the page fired.
- summarization-02: The page fired at 09:21.
- summarization-02: The incident response worked but detection lagged.
- summarization-04: After clicking the button several more times, four identical "export failed" error banners appear.
- summarization-05: Ada is to run the payments database migration dry run.
- summarization-06: The on-call engineer suspects retry-storm amplification.
- summarization-07: All results other than the median latency improvement are uncertain.
- summarization-07: Staging runs a newer kernel.
- summarization-07: The recommendation is to profile memory and investigate the crash before trusting the tail-latency and stability numbers.
- summarization-08: The progress bar finding is firm on impact and tentative on cause.
- summarization-08: The finding about differing admin/user default preferences is rated tentative.
- summarization-08: There is not enough evidence to call the template gallery observation a finding.

### developer-docs

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 25 | 20 | 0.8 | 30 | 4 |
| code-review-02 | 23 | 18 | 0.783 | 25 | 1 |
| code-review-03 | 26 | 16 | 0.615 | 29 | 12 |
| code-review-04 | 26 | 18 | 0.692 | 21 | 1 |
| code-review-05 | 27 | 16 | 0.593 | 26 | 8 |
| code-review-06 | 39 | 26 | 0.667 | 37 | 4 |
| code-review-07 | 43 | 28 | 0.651 | 33 | 1 |
| code-review-08 | 36 | 32 | 0.889 | 46 | 6 |
| debugging-01 | 8 | 8 | 1.0 | 8 | 0 |
| debugging-02 | 20 | 17 | 0.85 | 17 | 5 |
| debugging-03 | 11 | 11 | 1.0 | 10 | 0 |
| debugging-04 | 12 | 9 | 0.75 | 12 | 3 |
| debugging-05 | 20 | 20 | 1.0 | 15 | 1 |
| debugging-06 | 26 | 12 | 0.462 | 31 | 5 |
| debugging-07 | 30 | 22 | 0.733 | 37 | 9 |
| debugging-08 | 45 | 25 | 0.556 | 37 | 12 |
| explanation-01 | 39 | 21 | 0.538 | 25 | 1 |
| explanation-02 | 23 | 22 | 0.957 | 33 | 10 |
| explanation-03 | 33 | 24 | 0.727 | 28 | 3 |
| explanation-04 | 33 | 21 | 0.636 | 32 | 6 |
| explanation-05 | 18 | 12 | 0.667 | 10 | 0 |
| explanation-06 | 27 | 14 | 0.519 | 17 | 5 |
| explanation-07 | 30 | 0 | 0.0 | 0 | 0 |
| explanation-08 | 13 | 6 | 0.462 | 19 | 4 |
| summarization-01 | 6 | 6 | 1.0 | 10 | 5 |
| summarization-02 | 13 | 13 | 1.0 | 15 | 0 |
| summarization-03 | 14 | 13 | 0.929 | 14 | 0 |
| summarization-04 | 13 | 11 | 0.846 | 10 | 0 |
| summarization-05 | 9 | 7 | 0.778 | 10 | 1 |
| summarization-06 | 14 | 13 | 0.929 | 12 | 0 |
| summarization-07 | 16 | 14 | 0.875 | 13 | 2 |
| summarization-08 | 23 | 19 | 0.826 | 19 | 3 |

Median fraction: 0.764 over 32 scored pairs.

Median additions: 3.0 over 32 scored pairs.

Lost facts:

- code-review-01: There is no duplicate-role protection, so if `roles` already contains `"member"` it is appended again, producing `["member", "member"]`.
- code-review-01: The suggested fix raises `ValueError("name is required")` when `name` is falsy.
- code-review-01: The suggested fix copies the roles argument with `list(roles) if roles else []`.
- code-review-01: The suggested fix appends `"member"` only if it is not already in `roles`.
- code-review-01: The suggested fix calls `db.insert({"name": name, "roles": roles})` and returns `True`.
- code-review-02: `fetch` rejects only on network failure.
- code-review-02: `userId` is not validated or sanitized.
- code-review-02: If `userId` can come from untrusted user input, it should be encoded with `encodeURIComponent(userId)`.
- code-review-02: Encoding `userId` avoids malformed URLs and injection into the URL path.
- code-review-02: The corrected version awaits `fetch` with `encodeURIComponent(userId)` in the URL.
- code-review-03: There is no prior memory stored for this project.
- code-review-03: Some database engines allow chained additional statements via SQL injection.
- code-review-03: Injection is the top OWASP vulnerability.
- code-review-03: The sqlite3 driver uses `?` placeholders instead of `%s`.
- code-review-03: Valid order statuses include open, shipped, and cancelled.
- code-review-03: Unvalidated status input causes typos or bad data to silently return empty results.
- code-review-03: The code has no type hints.
- code-review-03: The function signature gives no indication of expected types.
- code-review-03: Appropriate type hints for the function would be `cursor: Cursor, customer_name: str, status: str) -> list[tuple]`.
- code-review-03: The SQL injection is the only issue that actually matters in this code.
- code-review-04: The assignment `self.value = 0` is itself atomic in CPython.
- code-review-04: The atomicity of `self.value = 0` in CPython is due to the GIL.
- code-review-04: A plain attribute read of `counter.value` is safe from torn reads in CPython.
- code-review-04: Individual bytecode operations are atomic in CPython.
- code-review-04: The correctness of the original code depends on incidental interpreter details rather than an actual contract.
- code-review-04: Relying on GIL semantics is fragile.
- code-review-04: The original code would break under free-threaded/no-GIL Python builds.
- code-review-04: The original code would break under PyPy under some conditions.
- code-review-05: The command `cd $BACKUP_DIR` is unquoted, so with an empty variable it becomes just `cd`.
- code-review-05: Running `cd` with no argument changes the working directory to `$HOME`.
- code-review-05: With a missing argument, the script runs `rm -rf *.tmp` in the user's home directory, causing silent data loss.
- code-review-05: Using `$(ls *.log)` needlessly forks an `ls` process.
- code-review-05: If no `*.tmp` files exist, `rm -rf *.tmp` attempts to remove a literal file named `*.tmp` and errors.
- code-review-05: The script handles neither the no-matching-`*.log` case nor the no-matching-`*.tmp` case.
- code-review-05: The script prints "Cleaned $BACKUP_DIR" regardless of whether any operation actually succeeded.
- code-review-05: The final success message is misleading because it prints even on partial or total failure.
- code-review-05: `gzip $f` will fail or prompt if a `.gz` file of the same name already exists.
- code-review-05: The script provides no `-f` flag or other handling for a pre-existing `.gz` file.
- code-review-05: The script performs no sanity check on the directory argument, such as rejecting `.` or `/`.
- code-review-06: The code uses `merged.pop(key, None)` when an override value is `None`.
- code-review-06: Treating `None` as a delete sentinel is a common convention in layered config systems such as Helm and Ansible.
- code-review-06: `merged.pop(key, None)` makes deleting a key that does not exist in `base` a silent no-op.
- code-review-06: The silent no-op on a missing key can mask a typo'd key name with no error or warning.
- code-review-06: The recursion branch is `elif key in merged and isinstance(merged[key], dict): merged[key] = merge_settings(merged[key], value)`.
- code-review-06: The resulting stack trace is far from the actual mistake and is confusing.
- code-review-06: When a key is replaced wholesale in the `else` branch, `merged[key]` becomes the exact same object passed in `override`.
- code-review-06: Later mutation of either `merged` or `override` leaks into the other.
- code-review-06: The aliasing issue can be fixed by using `copy.deepcopy` or a proper deep-merge-copy.
- code-review-06: Merging lists is ambiguous because it is unclear whether to append, dedupe, or merge by index.
- code-review-06: If `base` is an iterable of pairs, such as a list of tuples, `dict(base)` may silently succeed instead of failing clearly.
- code-review-06: The silent no-op when deleting a missing key is a side effect of the `None`-as-sentinel design rather than a separately chosen behavior.
- code-review-06: The `None`-as-delete behavior should stay as-is only if downstream configs never need to set a real `None` value.
- code-review-07: Exponential backoff would be expressed as something like 1000 * 2 ** i.
- code-review-07: Lack of jitter is a classic retry-logic mistake.
- code-review-07: Plain Error objects, thrown strings, and fetch network failures do not set a .status property.
- code-review-07: Axios exposes HTTP status at err.response.status rather than err.status.
- code-review-07: Retries will silently break if the underlying HTTP client changes.
- code-review-07: There is no maximum-delay cap and no total-timeout.
- code-review-07: The code uses attempts = 3 with a loop condition of i < attempts.
- code-review-07: attempts = 3 with i < attempts yields 3 total tries and 2 waits.
- code-review-07: The distinction between '3 attempts' and '3 retries' is a common source of off-by-one confusion downstream.
- code-review-07: A cache-warming job that should not crash a pipeline is an example of a caller that might want fail-soft behavior.
- code-review-07: Retrying 429 and 5xx but not other 4xx is a defensible retry policy.
- code-review-07: 429 and 5xx errors are classically transient while other 4xx errors are not.
- code-review-07: The retry policy is reasonable even though its implementation swallows errors instead of throwing.
- code-review-07: Changing the function requires finding and checking every call site for === null or truthy checks.
- code-review-07: Some existing call sites may already depend on the current silent-failure behavior.
- code-review-08: The tmp-/.part deletion should almost certainly have an age threshold, such as only removing files older than an hour.
- code-review-08: os.path.getmtime works on a directory.
- code-review-08: The hardcoded ROOT makes the script hard to test safely without editing the source.
- code-review-08: The module-level CUTOFF is almost certainly an oversight rather than a deliberate choice.
- debugging-02: If `NaN` is observed instead of a thrown error, the callback is likely not running in strict mode in that setup.
- debugging-02: `setInterval(function () { ... }.bind(this), 1000)` is an alternative fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-04: The non-ASCII byte occurs at byte offset 512 in the file.
- debugging-04: The matching encoding is almost always UTF-8.
- debugging-04: Passing errors="replace" to open() makes the code more robust when input files may not be valid UTF-8.
- debugging-06: The working directory contains no files.
- debugging-06: A "pool exhausted" error does not indicate that the database was slow to execute a query.
- debugging-06: The error indicates contention for the connection pool rather than slowness of the query.
- debugging-06: The export job's database connection pool is shared with an analytics service.
- debugging-06: The failures occur roughly once a week.
- debugging-06: Static configuration bugs do not usually produce intermittent failures.
- debugging-06: A connection leak would explain failures not tied to a specific batch and would explain why retries also fail.
- debugging-06: The observed failure window is 02:13:30 to 02:14:41.
- debugging-06: Postgres exposes connection state through pg_stat_activity, including application_name and state columns.
- debugging-06: pgbouncer and HikariCP are pool layers that can expose active and idle connection counts.
- debugging-06: "idle in transaction" is a Postgres connection state.
- debugging-06: Log retention for the services is currently 7 days or less.
- debugging-06: The export job raises a TimeoutError when it fails to acquire a connection.
- debugging-06: A dedicated pool or connection budget for the export job can be configured via a separate pgbouncer pool or a database role with a max_connections reservation.
- debugging-07: Cross-test contamination from shared state is the classic pytest-xdist flake pattern.
- debugging-07: A time-windowed digest query is a leading suspect for the failure.
- debugging-07: If the digest filters events by a timestamp window such as 'last N minutes' or a bucket boundary, slow seeding under load could push the third event's timestamp just outside the window.
- debugging-07: If the test never flakes when run locally in a loop with parallelism, that points more toward CI-specific resource contention than a pure logic bug.
- debugging-07: If a retry/poll around the digest read fixes the failure, it confirms an async race and indicates where to add proper synchronization rather than a test-side workaround.
- debugging-07: Most CI systems still capture stdout even without artifact storage.
- debugging-07: If the digest query uses a time window or a delayed-propagation index, that is almost certainly the root cause given the load-dependent symptom.
- debugging-07: The retry/poll experiment is the fastest way to confirm or rule out the async race.
- debugging-08: The working directory is empty and contains no code.
- debugging-08: Because no code is present, the question is a pure diagnostic-reasoning question.
- debugging-08: The correlation with campaigns indicates the traffic-proportional leak scales with webhook content or diversity rather than raw request count.
- debugging-08: Campaigns typically change payload shape and cardinality more than they change raw request volume.
- debugging-08: A size-bounded cache with correct eviction cannot grow past its bound.
- debugging-08: The cache is probably not the primary suspect for unbounded growth.
- debugging-08: Unbounded-cardinality tracking keyed by request or campaign data is the highest-suspicion cause of the traffic-proportional growth.
- debugging-08: Examples of unbounded-cardinality tracking include metrics labels, log context fields, per-order caches, and idempotency-key maps.
- debugging-08: A leak scaling with distinct traffic matches the observation of faster growth in campaign weeks better than one scaling with raw request count.
- debugging-08: A check for cause 1 is to confirm those structures have bounded cardinality or TTL eviction.
- debugging-08: A check for cause 1 is to compare distinct campaign and SKU counts against the memory growth rate across several weeks.
- debugging-08: Campaign products carry more images and fields, making entries larger.
- debugging-08: If cache entry count stays flat while heap keeps climbing, the cache is not the cause.
- debugging-08: If eviction count stalls while insert count climbs, eviction is broken.
- debugging-08: A check for cause 3 is to load-test the canary with synthetic webhook traffic including campaign-shaped payloads while watching connection counts, thread counts, and open file descriptors.
- debugging-08: A check for cause 4 is to run the canary alone and take heap dumps or object-count snapshots at fixed intervals.
- debugging-08: Step-shaped growth correlates with a cron or schedule, while smooth growth does not.
- debugging-08: A check for native memory issues is to monitor native memory tracking, thread count, and file descriptor count over time.
- debugging-08: Taking heap dumps on the canary is the highest-leverage next step.
- debugging-08: Heap dumps on the canary isolate the baseline leak (cause 4) from causes 1 through 3.
- explanation-01: A slot in a hash map's array is called a bucket.
- explanation-01: Collisions are inevitable because the array has a limited number of slots.
- explanation-01: Collisions remain a matter of probability even with a good hash function.
- explanation-01: The probability math behind hash collisions is the same as the birthday problem.
- explanation-01: The collection in a separate-chaining bucket is usually a linked list, and sometimes a tree or dynamic array.
- explanation-01: Quadratic probing tries index + 1 squared, index + 2 squared, and so on.
- explanation-01: Quadratic probing reduces clustering.
- explanation-01: Separate chaining has worse cache performance because linked list nodes are scattered in memory.
- explanation-01: Open addressing has better cache performance because data stays in a contiguous array.
- explanation-01: An open-addressed array must be resized before it fills up completely, because you cannot insert into a full array.
- explanation-01: Chaining is simpler to reason about and tolerates high load factors better.
- explanation-01: Chaining has more memory overhead and worse cache locality than open addressing.
- explanation-01: Most general-purpose hash maps use chaining.
- explanation-01: Java's HashMap uses chaining.
- explanation-01: Java's HashMap upgrades long chains to trees for worst-case performance.
- explanation-01: Python's dict uses open addressing.
- explanation-01: Many high-performance C++ hash maps use open addressing.
- explanation-01: Open addressing is chosen in those implementations for memory and cache benefits.
- explanation-02: Collaborative editing, CMS records, and REST APIs with 'last write wins' semantics via ETags are examples suited to optimistic locking.
- explanation-03: Packets queuing and being dropped due to overload is called congestion.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The receiver's advertised window caps data based on the receiver's buffer space.
- explanation-03: Historically, the initial cwnd was 1 segment.
- explanation-03: Modern implementations typically start with a cwnd of around 10 segments (~14KB).
- explanation-03: A connection that encounters congestion backs off after just one or two round trips rather than many.
- explanation-03: Congestion avoidance uses linear growth.
- explanation-03: If loss is detected after congestion avoidance begins, the sender cuts its rate back down.
- explanation-03: After cutting its rate, the sender often re-enters a slow-start-like ramp-up.
- explanation-04: A process has its own memory address space, file descriptors, and OS resources.
- explanation-04: All threads in a process share the same address space, heap, and file descriptors.
- explanation-04: Each thread has its own stack and register state.
- explanation-04: A supervisor can restart a crashed process.
- explanation-04: Job queues often use processes.
- explanation-04: Python's multiprocessing module uses processes and the threading module uses threads.
- explanation-04: The OS can apply separate memory limits, CPU quotas, priorities, and cgroups per process.
- explanation-04: Per-process resource limits are useful for sandboxing untrusted code.
- explanation-04: Per-process resource limits can prevent one workload from starving others.
- explanation-04: Processes can run as different users with different permissions or sandboxes.
- explanation-04: Chrome's renderer processes run with fewer privileges than the browser process.
- explanation-04: High-throughput I/O-bound servers and GUI event loops with background work are cases where threads fit better.
- explanation-05: Program roots include globals, the stack, and active closures.
- explanation-05: An example of an unbounded cache leak is caching results keyed by user session without evicting old sessions.
- explanation-05: Examples of long-lived objects include a global event bus and a DOM element.
- explanation-05: A listener closure often captures references to other objects.
- explanation-05: Because the closure captures other objects, the whole chain stays reachable and leaks even after the logical owner is done with it.
- explanation-05: Garbage collection prevents dangling pointers.
- explanation-06: A slow API can be caused by slow serialization.
- explanation-06: A slow API can be caused by N+1 queries.
- explanation-06: A slow API can be caused by lock contention.
- explanation-06: A slow API can be caused by an inefficient endpoint doing unnecessary work.
- explanation-06: Caches introduce cache invalidation bugs.
- explanation-06: Cache invalidation bugs can cause stale data to be served after writes.
- explanation-06: Stale data served after writes is a classic source of confusing production issues.
- explanation-06: Caches add operational complexity by requiring another service to run, monitor, and keep available.
- explanation-06: Redis is an example of a service added when introducing a cache.
- explanation-06: Caching requires deciding how fresh cached data needs to be.
- explanation-06: Deciding cache freshness is a product or business decision, not just a technical one.
- explanation-06: The recommended second step is examining the read/write ratio and query patterns after confirming DB reads are the bottleneck.
- explanation-06: If reads do not dominate or are not repetitive, the fix is more likely query optimization, indexing, or reducing round trips.
- explanation-07: 200 GB is a small database size for Postgres.
- explanation-07: A single Postgres instance can comfortably handle multiple terabytes of data with proper indexing, vacuuming, and hardware.
- explanation-07: Modern NVMe-backed cloud instances make multi-terabyte single-instance Postgres more feasible.
- explanation-07: Sharding is an operational and architectural commitment rather than a performance tuning dial.
- explanation-07: Sharding is very hard to undo once application code and data are split across shards.
- explanation-07: Data volume, write throughput, and connection/query concurrency are distinct growth problems with different fixes.
- explanation-07: Sharding only addresses write throughput and total storage exceeding one machine's practical limits.
- explanation-07: Sharding does not fix badly performing queries.
- explanation-07: Sharding does not fix connection exhaustion.
- explanation-07: Read replicas solve read-heavy load without changing the data model.
- explanation-07: Partitioning, better indexing, connection pooling, and vertical scaling are alternatives to try before sharding for write-heavy workloads.
- explanation-07: pgbouncer is a connection pooling tool for Postgres.
- explanation-07: Expecting growth without being able to quantify it is a signal to instrument before changing architecture.
- explanation-07: Relevant metrics to collect before deciding include rows/day, GB/month, and QPS trend.
- explanation-07: Sharding works cleanly only when there is a natural shard key, such as tenant_id or user_id, that most queries filter on.
- explanation-07: Cross-cutting queries such as joins and aggregates spanning entities cause cross-shard query problems under sharding.
- explanation-07: Sharding multiplies operational complexity in migrations, backups, monitoring, and rebalancing.
- explanation-07: The cost of sharding is high for teams without capacity to operate it, regardless of data size.
- explanation-07: A shard key chosen prematurely can turn out wrong as access patterns evolve, requiring a painful re-shard.
- explanation-07: Cross-shard joins and transactions become slow or impossible after sharding.
- explanation-07: Cross-shard limitations force application-level workarounds such as denormalization and distributed transactions, which introduce bugs.
- explanation-07: Operational overhead from sharding begins immediately, before the added capacity is needed.
- explanation-07: Sharding prematurely diverts team velocity from product problems to distributed-systems problems.
- explanation-07: Vertical scaling has limits including a single-writer bottleneck, disk I/O, and vacuum falling behind on huge tables.
- explanation-07: Sharding under growth pressure leaves less time to choose a good shard key.
- explanation-07: Migrating under load is riskier than a planned migration.
- explanation-07: Growth instrumentation should track storage per month, QPS per month, and table-level growth.
- explanation-07: Suggested thresholds for revisiting the sharding decision are approaching the low hundreds of GB to TB range, or write throughput saturating a single primary.
- explanation-07: Partitioning large tables, read replicas, connection pooling, and archiving cold data provide significant headroom without the commitment of sharding.
- explanation-07: The recommendation is to stay on a single Postgres instance and not shard now.
- explanation-08: The improvement could be anywhere from 2% to 60%, depending on payload size and where request time is actually spent.
- explanation-08: JSON parsing/serialization being a small share of request time is common when the bottleneck is database queries, network, or business logic.
- explanation-08: Large payloads, high request rates, and tight latency budgets are conditions under which serialization takes a large share of request time.
- explanation-08: Binary formats often produce larger gains in wire size than in CPU time.
- explanation-08: Wire size reductions matter most when an application is bandwidth-constrained or paying for egress.
- explanation-08: Wrapping existing JSON encode/decode calls with a timer for a day is a cheap way to obtain real measurements.
- explanation-08: Running a benchmark on a representative payload sample comparing the language's JSON library against a candidate binary format is a cheap way to obtain real measurements.
- summarization-03: The worker would update the record when thumbnail generation is done.
- summarization-04: PDF export fails silently on the Reports page.
- summarization-04: The bug was reproduced on the latest version of Firefox.
- summarization-05: The payments database migration dry run is to happen before Thursday.
- summarization-05: Chen is assigned to continue search indexing work.
- summarization-06: The team has no evidence supporting the retry storm hypothesis.
- summarization-07: The task is a straightforward summarization task requiring no prior context.
- summarization-07: All findings other than the median latency drop and the memory increase are provisional.
- summarization-08: The progress bar finding is characterized as TENTATIVE.
- summarization-08: The impact of the progress bar issue cannot be sized from only 3 data points.
- summarization-08: Suggested follow-up remedies include adding progress indicators or time estimates.
- summarization-08: The admin-versus-regular-user default settings observation was not included as a top-3 finding because it is too weak to act on.

Added facts (styled only):

- code-review-01: `db.insert(...)` might return an ID or a status that the caller needs.
- code-review-01: The function does not check `name` for duplicates before the insert.
- code-review-01: The suggested rewrite builds `all_roles` as `[*roles, "member"]`.
- code-review-01: The suggested rewrite returns the result of `db.insert({"name": name, "roles": all_roles})`.
- code-review-02: Mixing async styles makes the control flow harder to follow.
- code-review-03: SQL injection here can let an attacker modify data outside the intended scope.
- code-review-03: `%s`, `?`, and `:name` are placeholder styles used by database drivers.
- code-review-03: The database driver handles escaping safely for parameterized queries.
- code-review-03: Selecting every column wastes bandwidth.
- code-review-03: Missing input validation is less risky when parameterized queries are used.
- code-review-03: Validating `status` against an expected set of values is worthwhile unless the caller already guarantees it.
- code-review-03: `cursor.execute` can raise on a bad connection.
- code-review-03: `cursor.execute` can raise on a syntax error.
- code-review-03: One option is to catch the exception and re-raise it with more context.
- code-review-03: Another option is to leave error handling to the caller.
- code-review-03: Whether to add error handling depends on how the function is used elsewhere in the codebase.
- code-review-03: Whether to add error handling is a judgment call rather than a fix to apply blindly.
- code-review-04: Using two separate locks would let `reset` and `increment` run concurrently and defeat the purpose of locking.
- code-review-05: Appending `|| exit 1` to the `cd` command fixes the unchecked `cd` failure.
- code-review-05: `$1` is used unquoted in the script.
- code-review-05: An unquoted `$1` is subject to word splitting and pathname expansion if the argument contains a space or a glob character.
- code-review-05: If `$1` is empty, `cd ""` either changes to the current directory or fails, depending on the shell.
- code-review-05: An argument can be validated with `[ -z "$1" ] || [ ! -d "$1" ]` followed by a usage message and `exit 1`.
- code-review-05: When no `.log` files exist, `ls *.log` prints an error to stderr while the command substitution still returns unexpected output.
- code-review-05: Adding `pwd` logging or a dry-run mode is advisable before deploying the script to production.
- code-review-05: The suggested rewrite is a `#!/bin/sh` script that sets `set -eu`, validates the argument, does `cd "$BACKUP_DIR" || exit 1`, runs `rm -f -- *.tmp`, gzips each `*.log` file in a glob loop, and echoes `"Cleaned $BACKUP_DIR"`.
- code-review-06: The lack of input validation is probably an omission that assumes trusted internal callers.
- code-review-06: The lack of a recursion guard is not deliberate.
- code-review-06: Regression tests should be written for the `None`-deletion behavior and the dict-vs-non-dict conflict case before changing anything.
- code-review-06: The `None`-deletion behavior and the dict-vs-non-dict conflict case are the two spots where the original author's intent cannot be determined.
- code-review-07: The inconsistent return values indicate a missing `return null;` after the loop.
- code-review-08: os.listdir(ROOT) raises an exception if the directory is missing or unreadable.
- code-review-08: If os.listdir(ROOT) raises, the whole script crashes with no cleanup done and no partial count returned.
- code-review-08: The variable 'removed' is only returned on a clean exit.
- code-review-08: A crash midway loses the 'removed' count with no record of what was deleted before the crash.
- code-review-08: ROOT is set to "/var/data/exports".
- code-review-08: The ROOT constant is a deliberate fixed target path and poses no issue on its own.
- debugging-02: `this.seconds += 1` is evaluated as `this.seconds = this.seconds + 1`.
- debugging-02: `NaN` output occurs when `this` is not `undefined` but some other object that lacks a `seconds` property.
- debugging-02: Examples of such an object are the global object in non-strict code, or a `Timer` instance other than the expected one.
- debugging-02: `undefined + 1` evaluates to `NaN`.
- debugging-02: `this.seconds` is `undefined`, so the addition produces `NaN` on every tick.
- debugging-04: The file is most likely UTF-8 text containing non-ASCII characters, such as accented letters or the Unicode replacement character.
- debugging-04: Opening a file in binary mode ("rb") allows counting newline bytes without decoding.
- debugging-04: The binary-mode line count works regardless of the text encoding.
- debugging-05: Python evaluates default argument values once, at the time the function is defined.
- debugging-06: A connection pool sized for average load can be exhausted when batch processing spikes concurrent requests.
- debugging-06: The failure occurred on 2026-07-29 around 02:14 UTC.
- debugging-06: Pool metrics that can be logged include active connection count, idle count, and wait queue depth.
- debugging-06: MySQL has information_schema.processlist for in-progress or long-running queries.
- debugging-06: Slow query logging can be enabled with a threshold below 30 seconds.
- debugging-07: Asynchronous digest generation can take the form of a queue, a debounce window, or an eventual-consistency read.
- debugging-07: Non-unique test data causing collisions is a possible cause.
- debugging-07: If event IDs, timestamps, or keys aren't randomized per test run, two concurrently running workers can generate colliding records.
- debugging-07: A dedup step in the digest logic could drop one of the colliding records.
- debugging-07: Reproducing the parallelism locally involves running the suite with `-n 4` or the runner's equivalent in a loop 50-100 times.
- debugging-07: If the test fails locally under the same worker count, you have a reproducible case and don't need CI artifacts.
- debugging-07: The failing test can be forced to run in isolation via a dedicated worker group or `-n 0` for that test class while the rest of the suite stays parallel.
- debugging-07: If the flake disappears when the test is serialized, that confirms cross-test or cross-worker interference rather than an issue intrinsic to the test.
- debugging-07: Steps 1-3 are the fastest way to confirm or rule out worker interference without touching CI logging.
- debugging-08: A schema change adding fields to cached product data can increase average entry size.
- debugging-08: An entry that holds a reference to something unbounded, such as a nested list or a per-request object, can increase average entry size.
- debugging-08: Diffing the product data model against a year-old version can show whether cache entries got heavier.
- debugging-08: A test that overfills the cache and checks that old entries are collectible confirms whether eviction actually fires.
- debugging-08: Per-request retention causes include a listener never removed, an entry added to a static collection, a thread-local not cleared, and a callback held by a deferred or future that never completes.
- debugging-08: Plotting memory growth rate against webhook request count, rather than against campaign week, tests for a per-request leak.
- debugging-08: A tight correlation between growth rate and webhook request count confirms a per-request leak.
- debugging-08: Candidate baseline leak sources include scheduled jobs, connection pool churn, log buffers, metrics collection, and GC bookkeeping such as metaspace and code cache.
- debugging-08: Enumerating everything the canary does besides serving webhooks — cron jobs, health checks, metrics scraping, config polling — helps isolate the baseline leak.
- debugging-08: Disabling one background job at a time on the canary and watching whether the growth rate drops isolates the responsible job.
- debugging-08: High-cardinality metrics fit the baseline growth because scheduled jobs also emit metrics.
- debugging-08: A metrics library's registered series count that climbs over time and never drops indicates a leak.
- explanation-01: A hash map handles a collision by storing more than one key at the same index.
- explanation-02: In the example, an inventory system stores a `quantity` and a `version` for each product.
- explanation-02: In the example, two requests read `quantity = 10, version = 5`.
- explanation-02: In the example, the first request updates the row and sets `version = 6`.
- explanation-02: In the example, the second request's update includes `WHERE version = 5`.
- explanation-02: In the example, the `WHERE version = 5` clause matches zero rows after the first request's update.
- explanation-02: In the example, the database rejects the second request's update.
- explanation-02: Optimistic locking fits when conflicts are infrequent and transactions are short.
- explanation-02: In the example, a bank transfer debits one account and credits another.
- explanation-02: In the example, the transaction locks both account rows with `SELECT ... FOR UPDATE`.
- explanation-02: Pessimistic locking fits when transactions are long or involve multiple related rows.
- explanation-03: Dropped packets trigger retransmissions.
- explanation-03: Retransmissions waste bandwidth and make congestion worse.
- explanation-03: ssthresh stands for slow start threshold.
- explanation-04: More processes help when you need failure isolation, want to bypass a language's concurrency limits, or need to scale across machines.
- explanation-04: Python and Ruby use a global interpreter lock that lets only one thread execute bytecode at a time, even on a multi-core machine.
- explanation-04: Threads in Python and Ruby help with I/O-bound work but do not achieve CPU parallelism.
- explanation-04: Processes can run on different machines.
- explanation-04: Independent process lifecycle management fits worker pools, microservices, and systems where capacity is added or removed without touching the rest of the application.
- explanation-04: Threads are the better choice when work is CPU-bound, shares a lot of state, and doesn't need strong isolation.
- explanation-06: The stages of a request to time include application logic, network calls, and database queries.
- explanation-06: Slow queries, missing indexes, and table scans are common causes of slowness that a cache cannot fix.
- explanation-06: Application logs or database metrics can be used to measure the ratio of reads to writes.
- explanation-06: Lookup tables and rarely updated user profiles are examples of hot, mostly-static data.
- explanation-06: In-memory caches, query caches, and content delivery networks are types of caching strategies.
- explanation-08: A recommended next step is to measure typical and worst-case payload sizes.
- explanation-08: A recommended next step is to prototype the binary format on the largest or highest-traffic endpoint.
- explanation-08: The prototype comparison should use end-to-end latency, not just serialization time.
- explanation-08: The migration cost includes client changes, debugging tooling, and schema management.
- summarization-01: The changelog included a build tooling upgrade.
- summarization-01: The changelog included a session module refactor.
- summarization-01: The changelog included a telemetry batching change.
- summarization-01: The build tooling upgrade, session module refactor, and telemetry batching change were omitted from the release notes.
- summarization-01: The build tooling upgrade, session module refactor, and telemetry batching change do not affect what users see or do.
- summarization-05: The payments database migration dry run is due Thursday.
- summarization-07: The crash might be caused by staging's newer kernel.
- summarization-07: Staging runs a newer kernel.
- summarization-08: The participating customers had existing templates.
- summarization-08: The recommendation is to test the template gallery with new customers who have no existing templates before drawing conclusions.
- summarization-08: The template gallery observation is an additional note rather than a main finding.

### plain-language

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 25 | 20 | 0.8 | 22 | 4 |
| code-review-02 | 23 | 14 | 0.609 | 16 | 2 |
| code-review-03 | 26 | 0 | 0.0 | 7 | 6 |
| code-review-04 | 26 | 19 | 0.731 | 23 | 5 |
| code-review-05 | 27 | 19 | 0.704 | 30 | 11 |
| code-review-06 | 39 | 27 | 0.692 | 31 | 5 |
| code-review-07 | 43 | 28 | 0.651 | 37 | 10 |
| code-review-08 | 36 | 31 | 0.861 | 42 | 10 |
| debugging-01 | 8 | 8 | 1.0 | 8 | 0 |
| debugging-02 | 20 | 13 | 0.65 | 17 | 3 |
| debugging-03 | 11 | 11 | 1.0 | 13 | 0 |
| debugging-04 | 12 | 11 | 0.917 | 19 | 5 |
| debugging-05 | 20 | 20 | 1.0 | 14 | 1 |
| debugging-06 | 26 | 7 | 0.269 | 25 | 11 |
| debugging-07 | 30 | 19 | 0.633 | 17 | 6 |
| debugging-08 | 45 | 18 | 0.4 | 35 | 11 |
| explanation-01 | 39 | 17 | 0.436 | 22 | 2 |
| explanation-02 | 23 | 20 | 0.87 | 32 | 0 |
| explanation-03 | 33 | 17 | 0.515 | 23 | 3 |
| explanation-04 | 33 | 19 | 0.576 | 33 | 2 |
| explanation-05 | 18 | 12 | 0.667 | 13 | 0 |
| explanation-06 | 27 | 12 | 0.444 | 20 | 2 |
| explanation-07 | 30 | 16 | 0.533 | 23 | 1 |
| explanation-08 | 13 | 7 | 0.538 | 12 | 2 |
| summarization-01 | 6 | 6 | 1.0 | 6 | 0 |
| summarization-02 | 13 | 9 | 0.692 | 12 | 3 |
| summarization-03 | 14 | 13 | 0.929 | 11 | 0 |
| summarization-04 | 13 | 11 | 0.846 | 13 | 0 |
| summarization-05 | 9 | 6 | 0.667 | 17 | 2 |
| summarization-06 | 14 | 13 | 0.929 | 13 | 0 |
| summarization-07 | 16 | 14 | 0.875 | 15 | 1 |
| summarization-08 | 23 | 20 | 0.87 | 21 | 1 |

Median fraction: 0.692 over 32 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: When a caller passes their own list, `roles.append(...)` mutates that list in place.
- code-review-01: Mutating the caller's list silently changes the caller's original list as a side effect, which is surprising and hard to trace.
- code-review-01: The bare `except` silently swallows the `AttributeError` from a missing `db`.
- code-review-01: The suggested fix raises `ValueError("name is required")` when `name` is falsy.
- code-review-01: The suggested fix copies the roles argument with `list(roles) if roles else []`.
- code-review-02: The function does not properly return a promise representing the eventual value.
- code-review-02: The function does not handle malformed JSON.
- code-review-02: The function does not validate the shape of the response.
- code-review-02: The function assumes `data` always has a `.name` property.
- code-review-02: If the API returns an error object or unexpected shape, `.toUpperCase()` will throw.
- code-review-02: `userId` is not validated or sanitized.
- code-review-02: If `userId` can come from untrusted user input, it should be encoded with `encodeURIComponent(userId)`.
- code-review-02: Encoding `userId` avoids malformed URLs and injection into the URL path.
- code-review-02: The corrected version awaits `fetch` with `encodeURIComponent(userId)` in the URL.
- code-review-03: There is no prior memory stored for this project.
- code-review-03: The code has a SQL injection vulnerability.
- code-review-03: The `customer_name` parameter is concatenated directly into the query string.
- code-review-03: The `status` parameter is concatenated directly into the query string.
- code-review-03: Caller-controlled input such as `customer_name = "x' OR '1'='1"` can alter the query logic.
- code-review-03: SQL injection in this code can exfiltrate other customers' data.
- code-review-03: Some database engines allow chained additional statements via SQL injection.
- code-review-03: Injection is the top OWASP vulnerability.
- code-review-03: SQL injection must be fixed by using parameterized queries.
- code-review-03: Parameterized queries can be written by passing `%s` placeholders and a tuple of values to `cursor.execute`.
- code-review-03: The sqlite3 driver uses `?` placeholders instead of `%s`.
- code-review-03: The code uses `SELECT *`.
- code-review-03: `SELECT *` is fragile if the table schema changes.
- code-review-03: Naming the needed columns explicitly is better than using `SELECT *`.
- code-review-03: The code has no input validation.
- code-review-03: The `status` parameter is not checked against a known set of valid statuses.
- code-review-03: Valid order statuses include open, shipped, and cancelled.
- code-review-03: Unvalidated status input causes typos or bad data to silently return empty results.
- code-review-03: The code has no error handling.
- code-review-03: A database error from `cursor.execute` will propagate as a raw exception with no context about the query or inputs that caused it.
- code-review-03: The code has no type hints.
- code-review-03: The function signature gives no indication of expected types.
- code-review-03: Appropriate type hints for the function would be `cursor: Cursor, customer_name: str, status: str) -> list[tuple]`.
- code-review-03: The SQL injection is the only issue that actually matters in this code.
- code-review-03: The SQL injection should be fixed first.
- code-review-03: The remaining issues are minor hardening or style points.
- code-review-04: The assignment `self.value = 0` is itself atomic in CPython.
- code-review-04: The atomicity of `self.value = 0` in CPython is due to the GIL.
- code-review-04: Individual bytecode operations are atomic in CPython.
- code-review-04: The correctness of the original code depends on incidental interpreter details rather than an actual contract.
- code-review-04: Relying on GIL semantics is fragile.
- code-review-04: The original code would break under free-threaded/no-GIL Python builds.
- code-review-04: The original code would break under PyPy under some conditions.
- code-review-05: The command `cd $BACKUP_DIR` is unquoted, so with an empty variable it becomes just `cd`.
- code-review-05: Running `cd` with no argument changes the working directory to `$HOME`.
- code-review-05: With a missing argument, the script runs `rm -rf *.tmp` in the user's home directory, causing silent data loss.
- code-review-05: If no `*.log` files exist, `ls *.log` prints an error to stderr.
- code-review-05: The script does not use `set -e` or `set -u`.
- code-review-05: `gzip $f` will fail or prompt if a `.gz` file of the same name already exists.
- code-review-05: The script provides no `-f` flag or other handling for a pre-existing `.gz` file.
- code-review-05: The script performs no sanity check on the directory argument, such as rejecting `.` or `/`.
- code-review-06: Treating `None` as a delete sentinel is a common convention in layered config systems such as Helm and Ansible.
- code-review-06: The silent no-op on a missing key can mask a typo'd key name with no error or warning.
- code-review-06: The fix for the mismatch crash is to add `isinstance(value, dict)` to the `elif` condition.
- code-review-06: The aliasing issue can be fixed by using `copy.deepcopy` or a proper deep-merge-copy.
- code-review-06: Merging lists is ambiguous because it is unclear whether to append, dedupe, or merge by index.
- code-review-06: If `base` is not dict-like, `dict(base)` may raise a strange error.
- code-review-06: If `base` is an iterable of pairs, such as a list of tuples, `dict(base)` may silently succeed instead of failing clearly.
- code-review-06: The lack of top-level type validation is likely an oversight and warrants an explicit type check with a clear error message.
- code-review-06: The function has no recursion-depth or cycle protection.
- code-review-06: A self-referential structure in `base` or `override` would cause infinite recursion.
- code-review-06: Infinite recursion is not a realistic concern for normal config data and is minor unless configs are untrusted or programmatically generated.
- code-review-06: The silent no-op when deleting a missing key is a side effect of the `None`-as-sentinel design rather than a separately chosen behavior.
- code-review-07: Swallowing non-retryable errors hides bugs and is the most dangerous problem in the code.
- code-review-07: Exponential backoff would be expressed as something like 1000 * 2 ** i.
- code-review-07: Lack of jitter is a classic retry-logic mistake.
- code-review-07: Plain Error objects, thrown strings, and fetch network failures do not set a .status property.
- code-review-07: Axios exposes HTTP status at err.response.status rather than err.status.
- code-review-07: There is no maximum-delay cap and no total-timeout.
- code-review-07: The code uses attempts = 3 with a loop condition of i < attempts.
- code-review-07: attempts = 3 with i < attempts yields 3 total tries and 2 waits.
- code-review-07: The distinction between '3 attempts' and '3 retries' is a common source of off-by-one confusion downstream.
- code-review-07: A cache-warming job that should not crash a pipeline is an example of a caller that might want fail-soft behavior.
- code-review-07: Retrying 429 and 5xx but not other 4xx is a defensible retry policy.
- code-review-07: 429 and 5xx errors are classically transient while other 4xx errors are not.
- code-review-07: The retry policy is reasonable even though its implementation swallows errors instead of throwing.
- code-review-07: Changing the function requires finding and checking every call site for === null or truthy checks.
- code-review-07: Some existing call sites may already depend on the current silent-failure behavior.
- code-review-08: The script has no dry-run mode.
- code-review-08: The lack of dry-run mode and logging makes incidents hard to diagnose after the fact for a scheduled, unattended, destructive script.
- code-review-08: ROOT is a hardcoded absolute path with no override mechanism.
- code-review-08: The hardcoded ROOT makes the script hard to test safely without editing the source.
- code-review-08: The module-level CUTOFF is almost certainly an oversight rather than a deliberate choice.
- debugging-02: Class bodies are implicitly in strict mode.
- debugging-02: Inside the callback, `this` is `undefined`.
- debugging-02: `this.seconds += 1` should throw `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: `this.seconds += 1` should not log `NaN`.
- debugging-02: If `NaN` is observed instead of a thrown error, the callback is likely not running in strict mode in that setup.
- debugging-02: `setInterval(function () { ... }.bind(this), 1000)` is an alternative fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-04: The code forces encoding="ascii" when opening the file.
- debugging-06: The working directory contains no files.
- debugging-06: A "pool exhausted" error means the job could not obtain a connection from its database connection pool within 30 seconds.
- debugging-06: A "pool exhausted" error does not indicate that the database was slow to execute a query.
- debugging-06: The error indicates contention for the connection pool rather than slowness of the query.
- debugging-06: The export job's database connection pool is shared with an analytics service.
- debugging-06: The failures do not always occur at the same batch number.
- debugging-06: Failures that vary in timing rather than by batch content are consistent with dependence on when another job runs rather than on data content.
- debugging-06: Static configuration bugs do not usually produce intermittent failures.
- debugging-06: A connection leak would gradually deplete the pool over the job's runtime.
- debugging-06: A connection leak would explain failures not tied to a specific batch and would explain why retries also fail.
- debugging-06: Lock-holding by analytics queries is less likely than pure pool starvation.
- debugging-06: The observed failure window is 02:13:30 to 02:14:41.
- debugging-06: Postgres exposes connection state through pg_stat_activity, including application_name and state columns.
- debugging-06: pgbouncer and HikariCP are pool layers that can expose active and idle connection counts.
- debugging-06: "idle in transaction" is a Postgres connection state.
- debugging-06: A connection leak would show pool usage trending upward over the night rather than spiking suddenly.
- debugging-06: Log retention for the services is currently 7 days or less.
- debugging-06: The export job raises a TimeoutError when it fails to acquire a connection.
- debugging-06: A dedicated pool or connection budget for the export job can be configured via a separate pgbouncer pool or a database role with a max_connections reservation.
- debugging-07: Under CI's shared load, with 4 workers competing for CPU and the database, operations are slower and more variable than on a quiet dev machine.
- debugging-07: Slower and more variable execution causes a race window to open more often.
- debugging-07: A silent write failure is a leading suspect for the failure.
- debugging-07: A rate limit, connection pool exhaustion, or transient error on the third seed call could go unnoticed if the test assumes a 201 or 200 response without asserting on it.
- debugging-07: Database read-replica lag or a stale MVCC snapshot is a less likely cause but worth ruling out.
- debugging-07: Read-replica lag or a stale MVCC snapshot could occur if the digest read hits a different connection or replica than the writes.
- debugging-07: If the test never flakes when run locally in a loop with parallelism, that points more toward CI-specific resource contention than a pure logic bug.
- debugging-07: Asserting on the response status of all three seed calls instead of assuming success would quickly rule the silent write failure case in or out.
- debugging-07: Most CI systems still capture stdout even without artifact storage.
- debugging-07: If the digest query uses a time window or a delayed-propagation index, that is almost certainly the root cause given the load-dependent symptom.
- debugging-07: The retry/poll experiment is the fastest way to confirm or rule out the async race.
- debugging-08: The working directory is empty and contains no code.
- debugging-08: Because no code is present, the question is a pure diagnostic-reasoning question.
- debugging-08: Memory growth that persists through quiet nights rules out a diurnal working-set effect such as daytime cache warming or delayed GC.
- debugging-08: The correlation with campaigns indicates the traffic-proportional leak scales with webhook content or diversity rather than raw request count.
- debugging-08: Campaigns typically change payload shape and cardinality more than they change raw request volume.
- debugging-08: Unbounded-cardinality tracking keyed by request or campaign data is the highest-suspicion cause of the traffic-proportional growth.
- debugging-08: Examples of unbounded-cardinality tracking include metrics labels, log context fields, per-order caches, and idempotency-key maps.
- debugging-08: Campaigns introduce new promo codes, SKUs, and campaign IDs.
- debugging-08: Using request-derived values as map keys or metric labels without eviction produces a leak that scales with distinct traffic.
- debugging-08: A leak scaling with distinct traffic matches the observation of faster growth in campaign weeks better than one scaling with raw request count.
- debugging-08: A check for cause 1 is to grep for metrics and logging calls that use request-derived values such as campaign_id, order_id, or sku as labels or map keys.
- debugging-08: A check for cause 1 is to confirm those structures have bounded cardinality or TTL eviction.
- debugging-08: A check for cause 1 is to compare distinct campaign and SKU counts against the memory growth rate across several weeks.
- debugging-08: Campaign products carry more images and fields, making entries larger.
- debugging-08: Other eviction failures include a weigher or size function that under-counts, and a secondary index or listener list that mirrors the cache without its own bound.
- debugging-08: A check for cause 2 is to instrument the cache to track live entry count, total weight, and eviction count over the day.
- debugging-08: If cache entry count stays flat while heap keeps climbing, the cache is not the cause.
- debugging-08: If eviction count stalls while insert count climbs, eviction is broken.
- debugging-08: Examples of webhook-path resource leaks include unclosed HTTP connections or streams, retry timers, per-event listeners never removed, and queues growing under backpressure.
- debugging-08: A check for cause 3 is to load-test the canary with synthetic webhook traffic including campaign-shaped payloads while watching connection counts, thread counts, and open file descriptors.
- debugging-08: A check for cause 3 is to take heap dumps before and after a traffic burst and diff object histograms for the fastest-growing type.
- debugging-08: Usual suspects for a baseline leak include scheduled or background jobs such as health checks, connection-pool keepalive, TLS session cache, DNS cache, and log buffers.
- debugging-08: Usual suspects for a baseline leak also include runtime-level growth such as metaspace from dynamic class or proxy generation, thread-stack retention, and native or off-heap buffers not tracked by heap size.
- debugging-08: Step-shaped growth correlates with a cron or schedule, while smooth growth does not.
- debugging-08: If heap looks flat but RSS climbs, off-heap or native memory is the likely culprit.
- debugging-08: A check for native memory issues is to monitor native memory tracking, thread count, and file descriptor count over time.
- debugging-08: Diffing heap histograms across a few hours will likely reveal whether the leak is at the JVM/runtime level or in an application-level collection.
- explanation-01: A slot in a hash map's array is called a bucket.
- explanation-01: The probability math behind hash collisions is the same as the birthday problem.
- explanation-01: The collection in a separate-chaining bucket is usually a linked list, and sometimes a tree or dynamic array.
- explanation-01: Linear probing tries index + 1, index + 2, and so on.
- explanation-01: Quadratic probing tries index + 1 squared, index + 2 squared, and so on.
- explanation-01: Quadratic probing reduces clustering.
- explanation-01: Double hashing uses a second hash function to compute the step size.
- explanation-01: Separate chaining has worse cache performance because linked list nodes are scattered in memory.
- explanation-01: Open addressing has better cache performance because data stays in a contiguous array.
- explanation-01: An open-addressed array must be resized before it fills up completely, because you cannot insert into a full array.
- explanation-01: Deletion in separate chaining is easy: remove the node from the list.
- explanation-01: Deletion in open addressing cannot simply empty the slot, as that would break probe chains for other entries.
- explanation-01: Deletion in open addressing usually needs a tombstone marker.
- explanation-01: Chaining has more memory overhead and worse cache locality than open addressing.
- explanation-01: Open addressing is more memory-efficient and faster in practice when load factor is kept low.
- explanation-01: Open addressing is more complex to implement correctly, especially deletion.
- explanation-01: Most general-purpose hash maps use chaining.
- explanation-01: Java's HashMap uses chaining.
- explanation-01: Java's HashMap upgrades long chains to trees for worst-case performance.
- explanation-01: Python's dict uses open addressing.
- explanation-01: Many high-performance C++ hash maps use open addressing.
- explanation-01: Open addressing is chosen in those implementations for memory and cache benefits.
- explanation-02: A pessimistic lock blocks other transactions from reading or writing that row until the lock is released.
- explanation-02: Financial transfers and inventory decrement at checkout are examples suited to pessimistic locking.
- explanation-02: Collaborative editing, CMS records, and REST APIs with 'last write wins' semantics via ETags are examples suited to optimistic locking.
- explanation-03: If a sender immediately sent data at the rate the receiver's window allows, it could overwhelm a router or link along the path.
- explanation-03: Packets queuing and being dropped due to overload is called congestion.
- explanation-03: If every connection ramped up to full speed instantly, congestion could cascade badly.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The receiver's advertised window caps data based on the receiver's buffer space.
- explanation-03: Historically, the initial cwnd was 1 segment.
- explanation-03: Modern implementations typically start with a cwnd of around 10 segments (~14KB).
- explanation-03: During slow start, cwnd increases roughly by one segment per ACK received.
- explanation-03: On detecting loss, the sender backs off.
- explanation-03: The name 'slow start' is somewhat misleading.
- explanation-03: Compared to a linear ramp-up, exponential growth is a reasonably aggressive way to find network capacity quickly.
- explanation-03: Slow start lets a connection on a fast, uncongested path such as within a datacenter ramp up quickly.
- explanation-03: A connection that encounters congestion backs off after just one or two round trips rather than many.
- explanation-03: Congestion avoidance uses linear growth.
- explanation-03: If loss is detected after congestion avoidance begins, the sender cuts its rate back down.
- explanation-03: After cutting its rate, the sender often re-enters a slow-start-like ramp-up.
- explanation-04: A process has its own memory address space, file descriptors, and OS resources.
- explanation-04: All threads in a process share the same address space, heap, and file descriptors.
- explanation-04: Each thread has its own stack and register state.
- explanation-04: Communication between threads occurs through shared memory, with synchronization.
- explanation-04: A supervisor can restart a crashed process.
- explanation-04: nginx uses worker processes.
- explanation-04: Job queues often use processes.
- explanation-04: Separate processes each get their own Python interpreter and GIL.
- explanation-04: Python's multiprocessing module uses processes and the threading module uses threads.
- explanation-04: The OS can apply separate memory limits, CPU quotas, priorities, and cgroups per process.
- explanation-04: Per-process resource limits are useful for sandboxing untrusted code.
- explanation-04: Per-process resource limits can prevent one workload from starving others.
- explanation-04: Chrome's renderer processes run with fewer privileges than the browser process.
- explanation-04: High-throughput I/O-bound servers and GUI event loops with background work are cases where threads fit better.
- explanation-05: Program roots include globals, the stack, and active closures.
- explanation-05: An example of an unbounded cache leak is caching results keyed by user session without evicting old sessions.
- explanation-05: Examples of long-lived objects include a global event bus and a DOM element.
- explanation-05: A listener closure often captures references to other objects.
- explanation-05: Because the closure captures other objects, the whole chain stays reachable and leaks even after the logical owner is done with it.
- explanation-05: Garbage collection prevents dangling pointers.
- explanation-06: A slow API can be caused by slow serialization.
- explanation-06: A slow API can be caused by N+1 queries.
- explanation-06: A slow API can be caused by a chatty external API call.
- explanation-06: A slow API can be caused by lock contention.
- explanation-06: Timing logs around DB calls versus total request time count as a form of profiling.
- explanation-06: A cache serves data instead of hitting the database.
- explanation-06: Caches introduce cache invalidation bugs.
- explanation-06: Cache invalidation bugs can cause stale data to be served after writes.
- explanation-06: Stale data served after writes is a classic source of confusing production issues.
- explanation-06: Caches add operational complexity by requiring another service to run, monitor, and keep available.
- explanation-06: Redis is an example of a service added when introducing a cache.
- explanation-06: Caching requires deciding how fresh cached data needs to be.
- explanation-06: Deciding cache freshness is a product or business decision, not just a technical one.
- explanation-06: The recommended first step is adding basic timing instrumentation to see where request time goes.
- explanation-06: The recommended second step is examining the read/write ratio and query patterns after confirming DB reads are the bottleneck.
- explanation-07: Modern NVMe-backed cloud instances make multi-terabyte single-instance Postgres more feasible.
- explanation-07: Sharding only addresses write throughput and total storage exceeding one machine's practical limits.
- explanation-07: Sharding does not fix badly performing queries.
- explanation-07: Sharding does not fix connection exhaustion.
- explanation-07: Partitioning, better indexing, connection pooling, and vertical scaling are alternatives to try before sharding for write-heavy workloads.
- explanation-07: pgbouncer is a connection pooling tool for Postgres.
- explanation-07: Relevant metrics to collect before deciding include rows/day, GB/month, and QPS trend.
- explanation-07: Sharding works cleanly only when there is a natural shard key, such as tenant_id or user_id, that most queries filter on.
- explanation-07: The cost of sharding is high for teams without capacity to operate it, regardless of data size.
- explanation-07: Cross-shard limitations force application-level workarounds such as denormalization and distributed transactions, which introduce bugs.
- explanation-07: Vertical scaling has limits including a single-writer bottleneck, disk I/O, and vacuum falling behind on huge tables.
- explanation-07: Growth instrumentation should track storage per month, QPS per month, and table-level growth.
- explanation-07: Suggested thresholds for revisiting the sharding decision are approaching the low hundreds of GB to TB range, or write throughput saturating a single primary.
- explanation-07: Partitioning large tables, read replicas, connection pooling, and archiving cold data provide significant headroom without the commitment of sharding.
- explanation-08: The improvement could be anywhere from 2% to 60%, depending on payload size and where request time is actually spent.
- explanation-08: Large payloads, high request rates, and tight latency budgets are conditions under which serialization takes a large share of request time.
- explanation-08: Binary formats often produce larger gains in wire size than in CPU time.
- explanation-08: Wire size reductions matter most when an application is bandwidth-constrained or paying for egress.
- explanation-08: Wire size reductions matter less on a fast internal network.
- explanation-08: Wrapping existing JSON encode/decode calls with a timer for a day is a cheap way to obtain real measurements.
- summarization-02: The incorrect pool size exhausted the database connection pool.
- summarization-02: The incident caused approximately 12% checkout errors.
- summarization-02: The incident lasted 34 minutes.
- summarization-02: The incident ran from 09:14 to 09:48 UTC.
- summarization-03: The worker would update the record when thumbnail generation is done.
- summarization-04: The Reports page has an "Export" button that offers PDF and CSV options.
- summarization-04: The bug was reproduced on the latest version of Firefox.
- summarization-05: The payments database migration dry run is to happen before Thursday.
- summarization-05: Ada is assigned to check with the mobile team's lead about whether the mobile team was informed of the API deprecation.
- summarization-05: Chen is assigned to continue search indexing work.
- summarization-06: The team has no evidence supporting the retry storm hypothesis.
- summarization-07: The task is a straightforward summarization task requiring no prior context.
- summarization-07: All findings other than the median latency drop and the memory increase are provisional.
- summarization-08: The impact of the progress bar issue cannot be sized from only 3 data points.
- summarization-08: Suggested follow-up remedies include adding progress indicators or time estimates.
- summarization-08: The admin-versus-regular-user default settings observation was not included as a top-3 finding because it is too weak to act on.

Added facts (styled only):

- code-review-01: The function provides no default value for the `db` parameter.
- code-review-01: A better practice is to catch a specific exception, such as the one raised by the database driver.
- code-review-01: The function does not validate that `roles` contains valid values before inserting.
- code-review-01: A `try`/`except` should be added back around `db.insert` only if there is a specific exception type to catch and a real recovery action to take.
- code-review-02: Marking the function `async` without using `await` makes it appear to wait for the fetch when it does not.
- code-review-02: If the network request fails or the server returns an error status, the failure is silent and `profile` remains `undefined`.
- code-review-03: The assistant runs a Bash command to read a memory index file.
- code-review-03: The memory index file is named MEMORY.md.
- code-review-03: The MEMORY.md path is /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-ypo5u9lk/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-b0vsmkza/memory/MEMORY.md
- code-review-03: The command suppresses error output by redirecting stderr to /dev/null.
- code-review-03: The command prints "no memory file" if reading the file fails.
- code-review-03: The Bash tool call is described as "Check memory index".
- code-review-04: Lost updates happen often under load.
- code-review-04: The fixed `Counter.__init__` sets `self.value = 0` and `self._lock = threading.Lock()`.
- code-review-04: In the fixed version, `increment` performs `self.value += 1` inside `with self._lock`.
- code-review-04: In the fixed version, `reset` sets `self.value = 0` inside `with self._lock`.
- code-review-04: In the fixed version, `get` returns `self.value` inside `with self._lock`.
- code-review-05: Appending `|| exit 1` to the `cd` command guards against `cd` failure.
- code-review-05: `cd ""` may fail silently or change to the user's home directory, and the behavior varies by shell.
- code-review-05: The argument can be validated with `[ -z "$1" ]` followed by a usage message to stderr and `exit 1`.
- code-review-05: The unmatched-glob behavior of `rm -rf *.tmp` is not dangerous.
- code-review-05: If there are no `.log` files, the loop will try to gzip a file literally named `*.log`, which fails with an error.
- code-review-05: `bash` supports `nullglob` to guard against zero glob matches.
- code-review-05: Plain `sh` does not support `nullglob`.
- code-review-05: `gzip $f` or `gzip "$f"` misbehaves if a filename starts with `-`, such as `-rf.log`, because it could be interpreted as a command-line option.
- code-review-05: Using `gzip -- "$f"` prevents filenames starting with `-` from being interpreted as options.
- code-review-05: `rm -r` is normally for deleting directories.
- code-review-05: Keeping `-r` raises the risk if the glob ever matches something unexpected.
- code-review-06: A merge function that leaks references back into its inputs defeats the point of merging.
- code-review-06: The function has no type hints.
- code-review-06: The absence of documentation and type hints is not a bug by itself.
- code-review-06: Without documentation, one cannot tell whether the `None`-deletes-key behavior and the dict-only merge behavior are intended features or accidents.
- code-review-06: The recommendation is to write tests pinning down each of the described behaviors, especially the two bugs, before anyone changes the function again.
- code-review-07: Suppressing errors makes calling code simpler but makes debugging harder.
- code-review-07: The `.status` convention may be intentional if the library targets a specific HTTP client, but it is fragile for unknown callers.
- code-review-07: Two different failure paths (`return null` and falling off the end of the loop) look identical to the caller.
- code-review-07: There is no logging.
- code-review-07: Without logging there is no way to see that a retry or a suppressed failure happened, making production issues hard to diagnose.
- code-review-07: `this` is not preserved.
- code-review-07: `fn(...args)` calls `fn` as a plain function, losing the `this` binding for methods that depend on it.
- code-review-07: The zero-delay first retry is likely accidental.
- code-review-07: The lack of backoff on 5xx errors is likely accidental.
- code-review-07: These three issues contradict the apparent intent of the 429 handling.
- code-review-08: Writing exports to a '.part' suffix before renaming them into place is a common pattern.
- code-review-08: The condition 'removed < 500' gates the elif branch.
- code-review-08: Both cleanup branches share the same 'removed' counter.
- code-review-08: If more than 500 temp files are deleted first, 'removed' exceeds 500 and the age-based cleanup does nothing for the rest of that run.
- code-review-08: The two checks represent unrelated cleanup policies.
- code-review-08: The coupling of the two branches through a shared counter appears accidental rather than intended.
- code-review-08: The function returns a count but records nothing about which files it deleted.
- code-review-08: The 500 cap could be a deliberate throttle to limit blast radius from a bug such as a bad mtime on many files.
- code-review-08: Deleting tmp-/.part files with no minimum age is likely not intentional.
- code-review-08: The recommended first fixes are adding a minimum age check before deleting tmp-/.part files, separating the two delete counters, and wrapping each iteration in a try/except that logs and continues.
- debugging-02: Because setInterval calls the function itself, `this` inside a regular function callback becomes the global object.
- debugging-02: Adding 1 to `undefined` gives NaN.
- debugging-02: Once the value becomes NaN, every following update stays NaN.
- debugging-04: This error usually happens when a file contains non-English text.
- debugging-04: Non-English text includes accented letters, curly quotes, and symbols.
- debugging-04: Adding errors="ignore" to open() lets decoding continue past bytes that don't decode cleanly.
- debugging-04: A file can be opened in binary mode using the "rb" mode string.
- debugging-04: Counting newline bytes in binary mode avoids encoding issues altogether.
- debugging-05: The fix creates a new list inside the function when `tags` is `None`, using `tags = list(DEFAULT_TAGS)`.
- debugging-06: If an error path fails to release a connection, the pool would fill up over days until it runs out.
- debugging-06: A slow connection leak fits a failure pattern of about once a week rather than every night.
- debugging-06: Long-running or blocked queries can be caused by lock contention, a missing index, or a changed query plan.
- debugging-06: If the first attempt's connection isn't released before the retry checks out a new one, each retry adds load instead of relieving it.
- debugging-06: Database server overload from CPU, I/O, or too many total connections across both services can slow every query.
- debugging-06: Pool metrics worth adding include active connections, checked-out time, and wait queue depth.
- debugging-06: Many connection pool libraries support connection leak detection by logging checkout and checkin with a stack trace.
- debugging-06: Leak detection can catch a connection that never gets released.
- debugging-06: Checking the database's slow query log and lock waits for the failure window can rule out a blocking query.
- debugging-06: Comparing the database's max connection limit against the combined pool sizes of both services can reveal a server-side ceiling rather than an application pool limit.
- debugging-06: Running the export job in staging alongside an intentionally heavy analytics query can confirm contention as the cause.
- debugging-07: An example of insufficient scoping is reading 'all recent events' instead of events for the specific test's user or run ID.
- debugging-07: Parallel workers hitting the same identifier is the most common cause of this kind of flake.
- debugging-07: If the test never fails when run alone under four workers, other tests are interfering through shared state rather than a race within the test itself.
- debugging-07: Local parallel reproduction is the fastest way to turn the intermittent CI failure into a failure reproducible locally.
- debugging-07: The test currently fails roughly one run in ten on CI.
- debugging-07: The failing test is test_digest_contains_all_events in tests/test_notifications.py.
- debugging-08: Examples of such unbounded collections include an idempotency-key set, a correlation-ID map, and an audit trail.
- debugging-08: Taking a heap dump early in the week and another right before the restart allows comparison of object counts.
- debugging-08: Eclipse MAT and VisualVM are tools for comparing object counts in heap dumps.
- debugging-08: jstack can be used to check thread count and open connections over the day.
- debugging-08: If cache entry count stays flat but memory keeps climbing, the entries themselves have grown.
- debugging-08: If cache values hold a file handle, a native buffer, or a listener, eviction may remove the reference from the cache without releasing what it points to.
- debugging-08: The eviction listener should be confirmed to actually close or release anything the cache value holds.
- debugging-08: After an eviction, a heap dump can show whether the evicted object is truly unreachable.
- debugging-08: If an evicted object is still retained, the holder of the remaining reference should be searched for.
- debugging-08: Capturing two heap dumps on the canary—one after the weekly restart and one right before the next restart—and diffing them is the fastest way to narrow down the cause.
- debugging-08: The service is restarted weekly.
- explanation-01: Chaining's speed stays steady when the map is nearly full.
- explanation-01: Clustering is when many keys crowd into nearby slots.
- explanation-03: When packets are dropped, the sender must resend them.
- explanation-03: Resending dropped packets wastes bandwidth and slows down other users of the network.
- explanation-03: Slow start trades a small amount of speed at the start of a connection for better stability and fairness across everyone sharing the network.
- explanation-04: Older versions of Ruby use a global interpreter lock.
- explanation-04: Separate processes or services can be restarted, updated, or scaled independently without affecting the rest of the system.
- explanation-06: A cache does not help if the real problem is slow database queries, such as those caused by missing indexes.
- explanation-06: A cache can add overhead to writes.
- explanation-07: Query latency is a signal for whether sharding is needed, specifically whether common queries slow down due to table size or lock contention despite good indexes.
- explanation-08: Profiling a few real requests can reveal typical payload sizes.
- explanation-08: If serialization is under 5-10% of request time, a binary format probably isn't worth the migration cost.
- summarization-02: The response was fast once on-call was paged.
- summarization-02: The team paged on-call within 7 minutes.
- summarization-02: The team rolled back within 27 minutes of the first alert.
- summarization-05: The listed action items came from a sprint planning meeting.
- summarization-05: The sprint planning meeting took place on Monday.
- summarization-07: Staging uses a newer kernel.
- summarization-08: The template gallery observation is not a ranked finding.

### technical-simplified

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 25 | 15 | 0.6 | 19 | 6 |
| code-review-02 | 23 | 14 | 0.609 | 22 | 1 |
| code-review-03 | 26 | 12 | 0.462 | 14 | 3 |
| code-review-04 | 26 | 17 | 0.654 | 19 | 2 |
| code-review-05 | 27 | 20 | 0.741 | 36 | 4 |
| code-review-06 | 39 | 20 | 0.513 | 35 | 10 |
| code-review-07 | 43 | 0 | 0.0 | 7 | 7 |
| code-review-08 | 36 | 32 | 0.889 | 34 | 8 |
| debugging-01 | 8 | 8 | 1.0 | 7 | 0 |
| debugging-02 | 20 | 9 | 0.45 | 12 | 2 |
| debugging-03 | 11 | 11 | 1.0 | 8 | 0 |
| debugging-05 | 20 | 19 | 0.95 | 16 | 2 |
| debugging-06 | 26 | 8 | 0.308 | 19 | 5 |
| debugging-08 | 45 | 0 | 0.0 | 7 | 7 |
| explanation-02 | 23 | 21 | 0.913 | 25 | 7 |
| explanation-03 | 33 | 21 | 0.636 | 24 | 3 |
| explanation-04 | 33 | 20 | 0.606 | 30 | 2 |
| explanation-05 | 18 | 11 | 0.611 | 12 | 2 |
| explanation-06 | 27 | 14 | 0.519 | 15 | 2 |
| explanation-07 | 30 | 15 | 0.5 | 19 | 5 |
| explanation-08 | 13 | 5 | 0.385 | 15 | 7 |
| summarization-01 | 6 | 6 | 1.0 | 6 | 1 |
| summarization-02 | 13 | 10 | 0.769 | 11 | 3 |
| summarization-03 | 14 | 14 | 1.0 | 13 | 0 |
| summarization-04 | 13 | 10 | 0.769 | 11 | 1 |
| summarization-05 | 9 | 8 | 0.889 | 8 | 1 |
| summarization-07 | 16 | 14 | 0.875 | 16 | 1 |

Median fraction: 0.636 over 27 scored pairs.

Median additions: 2 over 27 scored pairs.

Lost facts:

- code-review-01: Mutable default arguments are a classic Python footgun.
- code-review-01: When a caller passes their own list, `roles.append(...)` mutates that list in place.
- code-review-01: Mutating the caller's list silently changes the caller's original list as a side effect, which is surprising and hard to trace.
- code-review-01: The code performs no input validation on `name` for type or emptiness.
- code-review-01: Nothing prevents `add_user("", roles=None)` or `add_user(123)` from reaching `db.insert`.
- code-review-01: There is no duplicate-role protection, so if `roles` already contains `"member"` it is appended again, producing `["member", "member"]`.
- code-review-01: The suggested fix raises `ValueError("name is required")` when `name` is falsy.
- code-review-01: The suggested fix copies the roles argument with `list(roles) if roles else []`.
- code-review-01: The suggested fix appends `"member"` only if it is not already in `roles`.
- code-review-01: The suggested fix lets real database exceptions propagate instead of hiding them silently.
- code-review-02: `fetch` rejects only on network failure.
- code-review-02: The function does not handle malformed JSON.
- code-review-02: The function does not validate the shape of the response.
- code-review-02: The function assumes `data` always has a `.name` property.
- code-review-02: If the API returns an error object or unexpected shape, `.toUpperCase()` will throw.
- code-review-02: `userId` is not validated or sanitized.
- code-review-02: If `userId` can come from untrusted user input, it should be encoded with `encodeURIComponent(userId)`.
- code-review-02: Encoding `userId` avoids malformed URLs and injection into the URL path.
- code-review-02: The corrected version awaits `fetch` with `encodeURIComponent(userId)` in the URL.
- code-review-03: There is no prior memory stored for this project.
- code-review-03: SQL injection in this code can exfiltrate other customers' data.
- code-review-03: Some database engines allow chained additional statements via SQL injection.
- code-review-03: Injection is the top OWASP vulnerability.
- code-review-03: The sqlite3 driver uses `?` placeholders instead of `%s`.
- code-review-03: The `status` parameter is not checked against a known set of valid statuses.
- code-review-03: Valid order statuses include open, shipped, and cancelled.
- code-review-03: Unvalidated status input causes typos or bad data to silently return empty results.
- code-review-03: The code has no error handling.
- code-review-03: A database error from `cursor.execute` will propagate as a raw exception with no context about the query or inputs that caused it.
- code-review-03: The code has no type hints.
- code-review-03: The function signature gives no indication of expected types.
- code-review-03: Appropriate type hints for the function would be `cursor: Cursor, customer_name: str, status: str) -> list[tuple]`.
- code-review-03: The SQL injection is the only issue that actually matters in this code.
- code-review-04: The assignment `self.value = 0` is itself atomic in CPython.
- code-review-04: The atomicity of `self.value = 0` in CPython is due to the GIL.
- code-review-04: A plain attribute read of `counter.value` is safe from torn reads in CPython.
- code-review-04: A plain attribute read of `counter.value` is not safe from being logically stale between check and use in calling code.
- code-review-04: Individual bytecode operations are atomic in CPython.
- code-review-04: The correctness of the original code depends on incidental interpreter details rather than an actual contract.
- code-review-04: Relying on GIL semantics is fragile.
- code-review-04: The original code would break under free-threaded/no-GIL Python builds.
- code-review-04: The original code would break under PyPy under some conditions.
- code-review-05: Using `$(ls *.log)` needlessly forks an `ls` process.
- code-review-05: If no `*.log` files exist, `ls *.log` prints an error to stderr.
- code-review-05: If no `*.tmp` files exist, `rm -rf *.tmp` attempts to remove a literal file named `*.tmp` and errors.
- code-review-05: The script handles neither the no-matching-`*.log` case nor the no-matching-`*.tmp` case.
- code-review-05: The final success message is misleading because it prints even on partial or total failure.
- code-review-05: `gzip $f` will fail or prompt if a `.gz` file of the same name already exists.
- code-review-05: The script provides no `-f` flag or other handling for a pre-existing `.gz` file.
- code-review-06: The code uses `merged.pop(key, None)` when an override value is `None`.
- code-review-06: Treating `None` as a delete sentinel is a common convention in layered config systems such as Helm and Ansible.
- code-review-06: `merged.pop(key, None)` makes deleting a key that does not exist in `base` a silent no-op.
- code-review-06: The silent no-op on a missing key can mask a typo'd key name with no error or warning.
- code-review-06: The recursion branch is `elif key in merged and isinstance(merged[key], dict): merged[key] = merge_settings(merged[key], value)`.
- code-review-06: The `elif` check tests only that `merged[key]` is a dict and never checks that the override `value` is also a dict.
- code-review-06: With `base = {"db": {"host": "x"}}` and `override = {"db": "disabled"}`, the code recurses as `merge_settings({"host": "x"}, "disabled")`.
- code-review-06: That recursive call raises an `AttributeError` when it calls `.items()` on the string `"disabled"`.
- code-review-06: The resulting stack trace is far from the actual mistake and is confusing.
- code-review-06: The dict/non-dict mismatch crash is almost certainly a bug rather than a deliberate design choice.
- code-review-06: The fix for the mismatch crash is to add `isinstance(value, dict)` to the `elif` condition.
- code-review-06: Merging lists is ambiguous because it is unclear whether to append, dedupe, or merge by index.
- code-review-06: Replacing lists wholesale reads as intentional and is a reasonable, common choice.
- code-review-06: If `base` is not dict-like, `dict(base)` may raise a strange error.
- code-review-06: If `base` is an iterable of pairs, such as a list of tuples, `dict(base)` may silently succeed instead of failing clearly.
- code-review-06: The silent no-op when deleting a missing key is a side effect of the `None`-as-sentinel design rather than a separately chosen behavior.
- code-review-06: The dict/non-dict crash and the shallow-copy aliasing are the two issues to fix immediately regardless of intent.
- code-review-06: The dict/non-dict crash is an unguarded runtime failure.
- code-review-06: The `None`-as-delete behavior should stay as-is only if downstream configs never need to set a real `None` value.
- code-review-07: The function returns null on any error that is not a 429 or a 5xx.
- code-review-07: Returning null on non-retryable errors converts 400 responses, TypeErrors, network errors without a .status property, and programmer bugs into a silent null.
- code-review-07: Callers cannot distinguish an operation that succeeded with no result from an operation that failed.
- code-review-07: Swallowing non-retryable errors hides bugs and is the most dangerous problem in the code.
- code-review-07: If the last attempt throws a 429 or 5xx, the loop ends without a return or throw.
- code-review-07: When the loop ends without returning, the function resolves to undefined instead of surfacing the error.
- code-review-07: There is no throw statement anywhere in the catch paths.
- code-review-07: Every failure mode, including exhausting all retries, resolves silently.
- code-review-07: A caller awaiting the function can never catch a failure and can only receive null or undefined.
- code-review-07: The backoff is computed as 1000 * i with i starting at 0.
- code-review-07: Because i starts at 0, the first retry waits 0ms.
- code-review-07: The backoff is linear rather than exponential.
- code-review-07: Exponential backoff would be expressed as something like 1000 * 2 ** i.
- code-review-07: Nothing in the code indicates the zero-millisecond first retry was a deliberate choice rather than an off-by-one error.
- code-review-07: The retry logic includes no jitter.
- code-review-07: Fixed backoff multiples across many concurrent callers retrying against the same failing service cause thundering-herd resynchronization.
- code-review-07: Lack of jitter is a classic retry-logic mistake.
- code-review-07: The code reads err.status, which assumes a specific error shape.
- code-review-07: Plain Error objects, thrown strings, and fetch network failures do not set a .status property.
- code-review-07: Axios exposes HTTP status at err.response.status rather than err.status.
- code-review-07: Errors lacking err.status fall through to return null as if they were permanent 4xx failures.
- code-review-07: Retries will silently break if the underlying HTTP client changes.
- code-review-07: The 5xx branch uses continue immediately with no delay.
- code-review-07: Only the 429 branch applies a delay.
- code-review-07: Retrying 5xx with no backoff will hammer a struggling server.
- code-review-07: There is no maximum-delay cap and no total-timeout.
- code-review-07: For large attempts values, the 429 backoff grows unbounded.
- code-review-07: The code uses attempts = 3 with a loop condition of i < attempts.
- code-review-07: attempts = 3 with i < attempts yields 3 total tries and 2 waits.
- code-review-07: The distinction between '3 attempts' and '3 retries' is a common source of off-by-one confusion downstream.
- code-review-07: Returning null instead of throwing could be an intentional fail-soft design for a caller that treats null as 'no data available'.
- code-review-07: A cache-warming job that should not crash a pipeline is an example of a caller that might want fail-soft behavior.
- code-review-07: Retrying 429 and 5xx but not other 4xx is a defensible retry policy.
- code-review-07: 429 and 5xx errors are classically transient while other 4xx errors are not.
- code-review-07: The retry policy is reasonable even though its implementation swallows errors instead of throwing.
- code-review-07: The undefined return when retries are exhausted on a retryable error is almost certainly not deliberate.
- code-review-07: The undefined return is inconsistent with the 'return null on failure' theory because it returns undefined, not null.
- code-review-07: The null/undefined mismatch is a strong signal of a genuine bug rather than a design choice.
- code-review-07: The biggest risk in the function is that it can never throw, not the backoff math.
- code-review-07: Every failure in the function becomes null or undefined.
- code-review-07: Callers of the function exist that cannot be seen.
- code-review-07: Changing the function requires finding and checking every call site for === null or truthy checks.
- code-review-07: Some existing call sites may already depend on the current silent-failure behavior.
- code-review-08: os.listdir returns entries in filesystem-dependent order, not sorted by age.
- code-review-08: When the 500-item cap takes effect, it does not necessarily remove the oldest 500 files, just the first 500 in directory order.
- code-review-08: The person reviewing the script did not set up its schedule.
- code-review-08: The module-level CUTOFF is almost certainly an oversight rather than a deliberate choice.
- debugging-02: A regular function's `this` is determined by how the function is invoked, not by where it is defined.
- debugging-02: `setInterval` invokes its callback with no receiver.
- debugging-02: Because `setInterval` invokes the callback with no receiver, `this` is not bound to the `Timer` instance.
- debugging-02: Class bodies are implicitly in strict mode.
- debugging-02: In strict mode, an unbound `this` does not fall back to the global object.
- debugging-02: Inside the callback, `this` is `undefined`.
- debugging-02: `this.seconds += 1` should throw `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: `this.seconds += 1` should not log `NaN`.
- debugging-02: If `NaN` is observed instead of a thrown error, the callback is likely not running in strict mode in that setup.
- debugging-02: `setInterval(function () { ... }.bind(this), 1000)` is an alternative fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-05: Dependence on test order and isolation is the classic symptom of the mutable default argument bug.
- debugging-06: The working directory contains no files.
- debugging-06: A "pool exhausted" error means the job could not obtain a connection from its database connection pool within 30 seconds.
- debugging-06: A "pool exhausted" error does not indicate that the database was slow to execute a query.
- debugging-06: The error indicates contention for the connection pool rather than slowness of the query.
- debugging-06: The failures occur roughly once a week.
- debugging-06: Failures that vary in timing rather than by batch content are consistent with dependence on when another job runs rather than on data content.
- debugging-06: Static configuration bugs do not usually produce intermittent failures.
- debugging-06: A connection leak would explain failures not tied to a specific batch and would explain why retries also fail.
- debugging-06: A long-running or blocking analytics query holding locks could cause export queries to queue for connections instead of failing fast on lock wait.
- debugging-06: Lock-holding by analytics queries is less likely than pure pool starvation.
- debugging-06: The observed failure window is 02:13:30 to 02:14:41.
- debugging-06: Postgres exposes connection state through pg_stat_activity, including application_name and state columns.
- debugging-06: pgbouncer and HikariCP are pool layers that can expose active and idle connection counts.
- debugging-06: "idle in transaction" is a Postgres connection state.
- debugging-06: The relevant logs are rotated away before they can be examined.
- debugging-06: Log retention for the services is currently 7 days or less.
- debugging-06: The export job raises a TimeoutError when it fails to acquire a connection.
- debugging-06: A dedicated pool or connection budget for the export job can be configured via a separate pgbouncer pool or a database role with a max_connections reservation.
- debugging-08: The working directory is empty and contains no code.
- debugging-08: Because no code is present, the question is a pure diagnostic-reasoning question.
- debugging-08: Memory growth that persists through quiet nights rules out a diurnal working-set effect such as daytime cache warming or delayed GC.
- debugging-08: The observed pattern means reachable objects are actually accumulating.
- debugging-08: A correctly functioning bounded cache would plateau rather than show continuous growth.
- debugging-08: A canary instance with zero webhook traffic still grows in memory, but more slowly.
- debugging-08: The canary evidence implies at least two leaks: a baseline leak independent of traffic and a traffic-proportional leak.
- debugging-08: The correlation with campaigns indicates the traffic-proportional leak scales with webhook content or diversity rather than raw request count.
- debugging-08: Campaigns typically change payload shape and cardinality more than they change raw request volume.
- debugging-08: The cache bound has been unchanged for a year.
- debugging-08: A size-bounded cache with correct eviction cannot grow past its bound.
- debugging-08: The cache is probably not the primary suspect for unbounded growth.
- debugging-08: The cache is not fully exonerated because eviction could be silently broken or the bound could be miscounting.
- debugging-08: Unbounded-cardinality tracking keyed by request or campaign data is the highest-suspicion cause of the traffic-proportional growth.
- debugging-08: Examples of unbounded-cardinality tracking include metrics labels, log context fields, per-order caches, and idempotency-key maps.
- debugging-08: Campaigns introduce new promo codes, SKUs, and campaign IDs.
- debugging-08: Using request-derived values as map keys or metric labels without eviction produces a leak that scales with distinct traffic.
- debugging-08: A leak scaling with distinct traffic matches the observation of faster growth in campaign weeks better than one scaling with raw request count.
- debugging-08: A check for cause 1 is to grep for metrics and logging calls that use request-derived values such as campaign_id, order_id, or sku as labels or map keys.
- debugging-08: A check for cause 1 is to confirm those structures have bounded cardinality or TTL eviction.
- debugging-08: A check for cause 1 is to compare distinct campaign and SKU counts against the memory growth rate across several weeks.
- debugging-08: Broken or partial eviction in the supposedly bounded cache is a plausible cause.
- debugging-08: An unchanged cache bound does not mean eviction is working.
- debugging-08: A common eviction failure is bounding by entry count while entry byte size varies.
- debugging-08: Campaign products carry more images and fields, making entries larger.
- debugging-08: Other eviction failures include a weigher or size function that under-counts, and a secondary index or listener list that mirrors the cache without its own bound.
- debugging-08: A check for cause 2 is to instrument the cache to track live entry count, total weight, and eviction count over the day.
- debugging-08: If cache entry count stays flat while heap keeps climbing, the cache is not the cause.
- debugging-08: If eviction count stalls while insert count climbs, eviction is broken.
- debugging-08: A traffic-proportional resource leak in the webhook path is a plausible cause.
- debugging-08: Examples of webhook-path resource leaks include unclosed HTTP connections or streams, retry timers, per-event listeners never removed, and queues growing under backpressure.
- debugging-08: A webhook-path leak would explain why the canary, running the same code and background jobs without webhook load, still grows slightly but far less.
- debugging-08: A check for cause 3 is to load-test the canary with synthetic webhook traffic including campaign-shaped payloads while watching connection counts, thread counts, and open file descriptors.
- debugging-08: A check for cause 3 is to take heap dumps before and after a traffic burst and diff object histograms for the fastest-growing type.
- debugging-08: A baseline leak independent of webhooks would explain why the canary grows with zero webhook traffic.
- debugging-08: Usual suspects for a baseline leak include scheduled or background jobs such as health checks, connection-pool keepalive, TLS session cache, DNS cache, and log buffers.
- debugging-08: Usual suspects for a baseline leak also include runtime-level growth such as metaspace from dynamic class or proxy generation, thread-stack retention, and native or off-heap buffers not tracked by heap size.
- debugging-08: A check for cause 4 is to run the canary alone and take heap dumps or object-count snapshots at fixed intervals.
- debugging-08: Step-shaped growth correlates with a cron or schedule, while smooth growth does not.
- debugging-08: If heap looks flat but RSS climbs, off-heap or native memory is the likely culprit.
- debugging-08: A check for native memory issues is to monitor native memory tracking, thread count, and file descriptor count over time.
- debugging-08: No heap profile currently exists for the system.
- debugging-08: Taking heap dumps on the canary is the highest-leverage next step.
- debugging-08: Heap dumps on the canary isolate the baseline leak (cause 4) from causes 1 through 3.
- debugging-08: Diffing heap histograms across a few hours will likely reveal whether the leak is at the JVM/runtime level or in an application-level collection.
- explanation-02: Making the second transaction wait guarantees no lost update.
- explanation-02: Collaborative editing, CMS records, and REST APIs with 'last write wins' semantics via ETags are examples suited to optimistic locking.
- explanation-03: If a sender immediately sent data at the rate the receiver's window allows, it could overwhelm a router or link along the path.
- explanation-03: If every connection ramped up to full speed instantly, congestion could cascade badly.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The receiver's advertised window caps data based on the receiver's buffer space.
- explanation-03: Historically, the initial cwnd was 1 segment.
- explanation-03: Modern implementations typically start with a cwnd of around 10 segments (~14KB).
- explanation-03: Exponential growth finds capacity without guessing a fixed number.
- explanation-03: Slow start lets a connection on a fast, uncongested path such as within a datacenter ramp up quickly.
- explanation-03: A connection that encounters congestion backs off after just one or two round trips rather than many.
- explanation-03: Congestion avoidance uses linear growth.
- explanation-03: If loss is detected after congestion avoidance begins, the sender cuts its rate back down.
- explanation-03: After cutting its rate, the sender often re-enters a slow-start-like ramp-up.
- explanation-04: Each thread has its own stack and register state.
- explanation-04: Communication between threads occurs through shared memory, with synchronization.
- explanation-04: A supervisor can restart a crashed process.
- explanation-04: nginx uses worker processes.
- explanation-04: Browsers often use a process per tab.
- explanation-04: Job queues often use processes.
- explanation-04: Separate processes each get their own Python interpreter and GIL.
- explanation-04: Python's multiprocessing module uses processes and the threading module uses threads.
- explanation-04: The OS can apply separate memory limits, CPU quotas, priorities, and cgroups per process.
- explanation-04: Per-process resource limits can prevent one workload from starving others.
- explanation-04: Processes can run as different users with different permissions or sandboxes.
- explanation-04: Chrome's renderer processes run with fewer privileges than the browser process.
- explanation-04: High-throughput I/O-bound servers and GUI event loops with background work are cases where threads fit better.
- explanation-05: Program roots include globals, the stack, and active closures.
- explanation-05: An example of an unbounded cache leak is caching results keyed by user session without evicting old sessions.
- explanation-05: This occurs when a listener or subscriber is registered on a long-lived object and never unregistered.
- explanation-05: Examples of long-lived objects include a global event bus and a DOM element.
- explanation-05: A listener closure often captures references to other objects.
- explanation-05: Because the closure captures other objects, the whole chain stays reachable and leaks even after the logical owner is done with it.
- explanation-05: Garbage collection prevents dangling pointers.
- explanation-06: A slow API can be caused by slow serialization.
- explanation-06: A slow API can be caused by N+1 queries.
- explanation-06: A slow API can be caused by lock contention.
- explanation-06: Timing logs around DB calls versus total request time count as a form of profiling.
- explanation-06: A cache serves data instead of hitting the database.
- explanation-06: Caches introduce cache invalidation bugs.
- explanation-06: Cache invalidation bugs can cause stale data to be served after writes.
- explanation-06: Stale data served after writes is a classic source of confusing production issues.
- explanation-06: Caches add operational complexity by requiring another service to run, monitor, and keep available.
- explanation-06: Redis is an example of a service added when introducing a cache.
- explanation-06: Caching requires deciding how fresh cached data needs to be.
- explanation-06: Deciding cache freshness is a product or business decision, not just a technical one.
- explanation-06: If reads do not dominate or are not repetitive, the fix is more likely query optimization, indexing, or reducing round trips.
- explanation-07: Modern NVMe-backed cloud instances make multi-terabyte single-instance Postgres more feasible.
- explanation-07: Sharding is very hard to undo once application code and data are split across shards.
- explanation-07: Data volume, write throughput, and connection/query concurrency are distinct growth problems with different fixes.
- explanation-07: Sharding does not fix badly performing queries.
- explanation-07: Sharding does not fix connection exhaustion.
- explanation-07: Partitioning, better indexing, connection pooling, and vertical scaling are alternatives to try before sharding for write-heavy workloads.
- explanation-07: pgbouncer is a connection pooling tool for Postgres.
- explanation-07: Expecting growth without being able to quantify it is a signal to instrument before changing architecture.
- explanation-07: Relevant metrics to collect before deciding include rows/day, GB/month, and QPS trend.
- explanation-07: The cost of sharding is high for teams without capacity to operate it, regardless of data size.
- explanation-07: Cross-shard limitations force application-level workarounds such as denormalization and distributed transactions, which introduce bugs.
- explanation-07: Vertical scaling has limits including a single-writer bottleneck, disk I/O, and vacuum falling behind on huge tables.
- explanation-07: Growth instrumentation should track storage per month, QPS per month, and table-level growth.
- explanation-07: Suggested thresholds for revisiting the sharding decision are approaching the low hundreds of GB to TB range, or write throughput saturating a single primary.
- explanation-07: Partitioning large tables, read replicas, connection pooling, and archiving cold data provide significant headroom without the commitment of sharding.
- explanation-08: The improvement could be anywhere from 2% to 60%, depending on payload size and where request time is actually spent.
- explanation-08: JSON parsing/serialization being a small share of request time is common when the bottleneck is database queries, network, or business logic.
- explanation-08: If JSON parsing/serialization accounts for 40% of request time, switching is worth pursuing.
- explanation-08: Large payloads, high request rates, and tight latency budgets are conditions under which serialization takes a large share of request time.
- explanation-08: Binary formats often produce larger gains in wire size than in CPU time.
- explanation-08: Wire size reductions matter most when an application is bandwidth-constrained or paying for egress.
- explanation-08: Wire size reductions matter less on a fast internal network.
- explanation-08: Wrapping existing JSON encode/decode calls with a timer for a day is a cheap way to obtain real measurements.
- summarization-02: The incident caused approximately 12% checkout errors.
- summarization-02: The incident lasted 34 minutes.
- summarization-02: The incident ran from 09:14 to 09:48 UTC.
- summarization-04: PDF export fails silently on the Reports page.
- summarization-04: The Reports page has an "Export" button that offers PDF and CSV options.
- summarization-04: The bug was reproduced on the latest version of Firefox.
- summarization-05: Ada is assigned to check with the mobile team's lead about whether the mobile team was informed of the API deprecation.
- summarization-07: The task is a straightforward summarization task requiring no prior context.
- summarization-07: The worker crash requires further investigation before it can be ruled out.

Added facts (styled only):

- code-review-01: There are four problems in the function.
- code-review-01: The function should catch specific errors, such as `except Exception:` or the exact error type raised by `db.insert`.
- code-review-01: The suggested fix appends "member" to the roles by creating a new list with `roles + ["member"]`.
- code-review-01: The suggested fix catches `Exception as e` and calls `logging.error` with the user name and the error.
- code-review-01: The suggested fix returns `True` on success and `False` after logging an error.
- code-review-01: The suggested fix avoids the shared list, checks that `db` exists, and logs the real error.
- code-review-02: The corrected version awaits `fetch(`/api/users/${userId}`)`.
- code-review-03: Retrieving all columns wastes bandwidth.
- code-review-03: Adding input validation is optional.
- code-review-03: Input validation can prevent confusing database errors.
- code-review-04: A caller can set `counter.value` directly from any thread without going through the class methods.
- code-review-04: Setting `counter.value` directly bypasses any future locking.
- code-review-05: When the glob is unmatched, `gzip` tries to compress a file named `*.log` and fails.
- code-review-05: `$BACKUP_DIR` is unquoted in the final `echo`.
- code-review-05: The unquoted `$BACKUP_DIR` in the final `echo` is a small issue.
- code-review-05: The missing `set -e` is the most dangerous problem in the script.
- code-review-06: If merged[key] is a dict and the override value is not a dict, the code replaces the dict with the new value.
- code-review-06: The code gives no warning when it replaces a dict with a non-dict value.
- code-review-06: The type-mismatch handling is asymmetric and silent in both directions.
- code-review-06: The type-mismatch behavior is likely intended.
- code-review-06: Silent type mismatch can hide config errors, such as a typo that turns a dict into a string.
- code-review-06: The missing recursion limit is likely accidental.
- code-review-06: If a caller passes the wrong type, the error appears deep in the recursion.
- code-review-06: The design appears deliberate in two respects: using None as a delete signal, and merging only when both sides hold a dict.
- code-review-06: The aliasing bug, the shallow copy, the missing recursion limit, and the missing input checks look like bugs from an incomplete implementation rather than deliberate choices.
- code-review-06: The recommendation is to add a docstring stating the None-deletes rule and the type-mismatch behavior.
- code-review-07: The assistant will check memory for relevant context.
- code-review-07: The assistant will review the code after checking memory.
- code-review-07: A bash tool is invoked.
- code-review-07: The bash command runs `cat` on the file /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-ypo5u9lk/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-b0vsmkza/memory/MEMORY.md
- code-review-07: The command suppresses error output by redirecting stderr to /dev/null.
- code-review-07: The command echoes 'NONE' if the cat command fails.
- code-review-07: The tool call's description is 'Check memory index'.
- code-review-08: The script does not check that `ROOT` exists.
- code-review-08: If `ROOT` is missing or not mounted, `os.listdir` raises an error and the run crashes with no clear message.
- code-review-08: The function returns a count of deleted files.
- code-review-08: The exemption of `tmp-`/`.part` files from the cap is not documented.
- code-review-08: If more than 500 files pass the 45-day cutoff between runs, the extra files are not removed until later runs catch up.
- code-review-08: If the backlog grows faster than 500 files per run, the backlog never clears.
- code-review-08: The unbounded deletion of `tmp-`/`.part` files, combined with the missing age check, reads as a bug rather than a deliberate design.
- code-review-08: Adding the minimum age check removes the most dangerous problem with the smallest change.
- debugging-02: Inside the callback, `this.seconds` is `undefined`.
- debugging-02: `undefined + 1` evaluates to `NaN`.
- debugging-05: Python creates a function's default argument value one time, when the function is defined.
- debugging-05: In the fixed code, `tags = list(DEFAULT_TAGS)` is executed when `tags is None`.
- debugging-06: The export job opening too many connections per batch, so that a large batch exhausts the pool, is a plausible cause.
- debugging-06: Running the export job with a larger pool for one week is a way to narrow down the cause.
- debugging-06: If failures stop after increasing the pool size, the pool size was too small.
- debugging-06: Logging the batch size for each failed batch, then checking whether failures correlate with large batches rather than a specific batch number, is a way to narrow down the cause.
- debugging-06: The recommended first step is the pool and active-connection log.
- debugging-08: The assistant checks its memory for relevant context before answering.
- debugging-08: The assistant invokes a bash tool.
- debugging-08: The bash command runs `cat` on the file at /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-ypo5u9lk/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-b0vsmkza/memory/MEMORY.md
- debugging-08: The bash command suppresses error output by redirecting stderr to /dev/null.
- debugging-08: The bash command echoes 'NONE' if the cat command fails.
- debugging-08: The bash tool call's description is 'Check memory index'.
- debugging-08: The memory index file is named MEMORY.md.
- explanation-02: In the example, process A reads a row with `version = 1`.
- explanation-02: In the example, process B reads the same row with `version = 1`.
- explanation-02: In the example, process A updates the row and sets `version = 2`.
- explanation-02: In the example, when process B tries to update the row, the database checks that `version` still equals 1.
- explanation-02: Web applications with many concurrent readers and few concurrent writers are a good fit for optimistic locking.
- explanation-02: In the pessimistic locking example, a process runs `SELECT * FROM accounts WHERE id = 1 FOR UPDATE`.
- explanation-02: Pessimistic locking should be used when conflicts are frequent and the cost of a retry is high.
- explanation-03: Packet loss forces retransmission.
- explanation-03: Retransmission wastes bandwidth.
- explanation-03: After a packet loss, TCP reduces the congestion window and adjusts the threshold.
- explanation-04: A process can have one thread or many threads.
- explanation-04: Threads should be used when tasks must share data quickly and safely.
- explanation-05: When code adds an event listener but never removes it, the listener keeps a reference to its target object.
- explanation-05: A listener that is never removed prevents the garbage collector from freeing its target object.
- explanation-06: The slow part can be the network.
- explanation-06: Finding the slow queries means checking whether specific queries or specific endpoints cause the slowdown.
- explanation-07: The correct sharding decision depends on write throughput, table size versus index size, query patterns, and growth rate.
- explanation-07: If one primary node can accept all writes without queue buildup, sharding is not needed.
- explanation-07: One should check whether the working set of hot data and indexes fits in memory.
- explanation-07: If the working set does not fit in memory, adding memory or using partitioning should be done before sharding.
- explanation-07: Sharding should start only when there is clear evidence of sustained write throughput near the limit of one node, or a working set that no longer fits in memory even after database tuning.
- explanation-08: The gain from switching to a binary format depends on the typical payload size and structure.
- explanation-08: Binary formats save more on numeric-heavy payloads.
- explanation-08: Binary formats save less on small, text-heavy payloads.
- explanation-08: Binary formats gain the most with numbers and binary data.
- explanation-08: Binary formats gain less with strings.
- explanation-08: If payloads are large and numeric-heavy, a binary format can reduce both payload size and CPU time.
- explanation-08: If payloads are small and mostly text, the gain from a binary format is often small.
- summarization-01: Each button's tooltip shows that button's keyboard shortcut.
- summarization-02: The response to the incident was fast and effective.
- summarization-02: The page went out 7 minutes after the errors started.
- summarization-02: The rollback fixed the issue in 27 minutes.
- summarization-04: Clicking the PDF export button several more times causes four "export failed" error banners to appear at once.
- summarization-05: Ada is assigned to run the payments database dry run.
- summarization-07: Staging runs a newer kernel.

## Hedging survival

The judge lists the claims that the unstyled answer presents with uncertainty, then judges each claim in the styled answer: hedged (the uncertainty survives in some form), certain (the claim survives but reads as a fact — the failure this check targets), or absent (the claim is gone, a completeness loss). Survival is hedged / (hedged + certain). The claims that became certain appear verbatim below the table.

### clarity-flow

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 0 | 0 | 0 | 0 | n/a |
| code-review-02 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-03 | 0 | 0 | 0 | 0 | n/a |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-06 | 8 | 4 | 0 | 4 | 1.0 |
| code-review-07 | 5 | 3 | 1 | 1 | 0.75 |
| code-review-08 | 10 | 7 | 3 | 0 | 0.7 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 1 | 0 | 0 | 1 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 2 | 0 | 1 | 1 | 0.0 |
| debugging-05 | 1 | 0 | 1 | 0 | 0.0 |
| debugging-06 | 10 | 7 | 1 | 2 | 0.875 |
| debugging-07 | 9 | 5 | 0 | 4 | 1.0 |
| debugging-08 | 7 | 2 | 1 | 4 | 0.667 |
| explanation-01 | 0 | 0 | 0 | 0 | n/a |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 5 | 0 | 3 | 2 | 0.0 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 3 | 2 | 0 | 1 | 1.0 |
| explanation-07 | 0 | 0 | 0 | 0 | n/a |
| explanation-08 | 3 | 1 | 1 | 1 | 0.5 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 2 | 1 | 0 | 0.667 |

Claims: 77 over 32 judged pairs: 40 hedged, 15 certain, 22 absent.

Median survival: 0.683 over 16 scored pairs.

Claims that became certain:

- code-review-02: The line `return profile.name.toUpperCase()` will throw `Cannot read properties of undefined (reading 'name')` essentially every time — i.e. very nearly always, though not stated as strictly guaranteed on every single call.
- code-review-05: A mistaken invocation could wipe .tmp files somewhere unintended (given the unquoted "$BACKUP_DIR" and the lack of a sanity check rejecting values like `.` or `/`, combined with issue #1).
- code-review-07: The `undefined` return when retries are exhausted on a retryable error is almost certainly not deliberate
- code-review-08: The bugs listed in the first section are likely to cause real problems.
- code-review-08: A TOCTOU race between `listdir` and `getmtime`/`remove` is plausible if the script runs concurrently with itself or alongside the export job.
- code-review-08: When the cap does kick in, it doesn't necessarily remove the oldest 500 files — just whichever 500 happened to come first in directory order.
- debugging-04: The non-ASCII byte 0xc3 at byte offset 512 is likely part of a UTF-8 multi-byte sequence, e.g. an accented character.
- debugging-05: By the time this test runs, DEFAULT_TAGS might already be ["draft", "post", "post"] (or more), making == ["draft", "post"] fail.
- debugging-06: If giving the export job a dedicated pool or connection budget separate from analytics stops the failures, that would confirm shared-pool contention as the cause.
- debugging-08: A traffic-proportional resource leak in the webhook path would explain why the canary — same code and background jobs but no webhook load — still grows slightly but far less.
- explanation-03: If a TCP sender just started blasting data at whatever rate the receiver's window allows, it could easily overwhelm a router or link somewhere in the middle, causing packets to queue up and get dropped.
- explanation-03: If every connection ramped up to full speed instantly, congestion could cascade badly.
- explanation-03: On each ACK the sender increases cwnd roughly by one segment per ACK.
- explanation-08: Without measurements, the improvement from switching is unpredictable — it could be 2% or 60%, depending on payload size and where time actually goes.
- summarization-08: The field-mapping redesign appears to be functioning as intended.

### classic-concise

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 0 | 0 | 0 | 0 | n/a |
| code-review-02 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-03 | 0 | 0 | 0 | 0 | n/a |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-06 | 8 | 5 | 0 | 3 | 1.0 |
| code-review-07 | 5 | 3 | 0 | 2 | 1.0 |
| code-review-08 | 10 | 6 | 3 | 1 | 0.667 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 1 | 0 | 0 | 1 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 2 | 2 | 0 | 0 | 1.0 |
| debugging-05 | 1 | 0 | 1 | 0 | 0.0 |
| debugging-06 | 10 | 7 | 0 | 3 | 1.0 |
| debugging-07 | 9 | 5 | 0 | 4 | 1.0 |
| debugging-08 | 7 | 2 | 3 | 2 | 0.4 |
| explanation-01 | 0 | 0 | 0 | 0 | n/a |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 5 | 1 | 3 | 1 | 0.25 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 3 | 2 | 0 | 1 | 1.0 |
| explanation-07 | 0 | 0 | 0 | 0 | n/a |
| explanation-08 | 3 | 2 | 1 | 0 | 0.667 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 2 | 1 | 0 | 0.667 |

Claims: 77 over 32 judged pairs: 44 hedged, 14 certain, 19 absent.

Median survival: 0.834 over 16 scored pairs.

Claims that became certain:

- code-review-02: The line `return profile.name.toUpperCase()` will throw `Cannot read properties of undefined (reading 'name')` essentially every time — i.e. very nearly always, though not stated as strictly guaranteed on every single call.
- code-review-05: A mistaken invocation could wipe .tmp files somewhere unintended (given the unquoted "$BACKUP_DIR" and the lack of a sanity check rejecting values like `.` or `/`, combined with issue #1).
- code-review-08: The bugs listed in the first section are likely to cause real problems.
- code-review-08: A TOCTOU race between `listdir` and `getmtime`/`remove` is plausible if the script runs concurrently with itself or alongside the export job.
- code-review-08: Everything else (missing try/except, directory crash, cap not applying to tmp/.part, no logging) reads like gaps rather than choices.
- debugging-05: By the time this test runs, DEFAULT_TAGS might already be ["draft", "post", "post"] (or more), making == ["draft", "post"] fail.
- debugging-08: A traffic-proportional resource leak in the webhook path would explain why the canary — same code and background jobs but no webhook load — still grows slightly but far less.
- debugging-08: If heap looks flat but RSS climbs, the cause is likely off-heap/native memory.
- debugging-08: Taking heap dumps on the canary and diffing histograms across a few hours will likely tell you whether you're chasing a JVM/runtime-level leak or an application-level collection, and should narrow the remaining hypotheses quickly.
- explanation-03: If a TCP sender just started blasting data at whatever rate the receiver's window allows, it could easily overwhelm a router or link somewhere in the middle, causing packets to queue up and get dropped.
- explanation-03: If every connection ramped up to full speed instantly, congestion could cascade badly.
- explanation-03: On each ACK the sender increases cwnd roughly by one segment per ACK.
- explanation-08: Without measurements, the improvement from switching is unpredictable — it could be 2% or 60%, depending on payload size and where time actually goes.
- summarization-08: The field-mapping redesign appears to be functioning as intended.

### developer-docs

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 0 | 0 | 0 | 0 | n/a |
| code-review-02 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-03 | 0 | 0 | 0 | 0 | n/a |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-06 | 8 | 4 | 2 | 2 | 0.667 |
| code-review-07 | 5 | 4 | 0 | 1 | 1.0 |
| code-review-08 | 10 | 6 | 4 | 0 | 0.6 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 2 | 1 | 0 | 1 | 1.0 |
| debugging-05 | 1 | 0 | 1 | 0 | 0.0 |
| debugging-06 | 10 | 6 | 1 | 3 | 0.857 |
| debugging-07 | 9 | 5 | 0 | 4 | 1.0 |
| debugging-08 | 7 | 2 | 2 | 3 | 0.5 |
| explanation-01 | 0 | 0 | 0 | 0 | n/a |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 5 | 2 | 2 | 1 | 0.5 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 3 | 2 | 0 | 1 | 1.0 |
| explanation-07 | 0 | 0 | 0 | 0 | n/a |
| explanation-08 | 3 | 1 | 1 | 1 | 0.5 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 2 | 1 | 0 | 0.667 |

Claims: 77 over 32 judged pairs: 43 hedged, 16 certain, 18 absent.

Median survival: 0.667 over 17 scored pairs.

Claims that became certain:

- code-review-02: The line `return profile.name.toUpperCase()` will throw `Cannot read properties of undefined (reading 'name')` essentially every time — i.e. very nearly always, though not stated as strictly guaranteed on every single call.
- code-review-05: A mistaken invocation could wipe .tmp files somewhere unintended (given the unquoted "$BACKUP_DIR" and the lack of a sanity check rejecting values like `.` or `/`, combined with issue #1).
- code-review-06: The shallow-copy aliasing between `merged`, `base`, and `override` is likely unintentional, and probably fine if callers never mutate results afterward — though that's a fragile assumption to leave undocumented.
- code-review-06: If `base` isn't dict-like, `dict(base)` may raise a strange error, or worse, silently "succeed" if `base` happens to be an iterable of pairs (e.g. a list of tuples).
- code-review-08: A TOCTOU race between `listdir` and `getmtime`/`remove` is plausible if the script runs concurrently with itself or alongside the export job.
- code-review-08: When the cap does kick in, it doesn't necessarily remove the oldest 500 files — just whichever 500 happened to come first in directory order.
- code-review-08: The items in the second section are design smells worth flagging, not necessarily bugs.
- code-review-08: Everything else (missing try/except, directory crash, cap not applying to tmp/.part, no logging) reads like gaps rather than choices.
- debugging-05: By the time this test runs, DEFAULT_TAGS might already be ["draft", "post", "post"] (or more), making == ["draft", "post"] fail.
- debugging-06: The listed causes are the most plausible ones, ranked by likelihood, for the pool exhaustion errors.
- debugging-08: If heap looks flat but RSS climbs, the cause is likely off-heap/native memory.
- debugging-08: Taking heap dumps on the canary and diffing histograms across a few hours will likely tell you whether you're chasing a JVM/runtime-level leak or an application-level collection, and should narrow the remaining hypotheses quickly.
- explanation-03: If every connection ramped up to full speed instantly, congestion could cascade badly.
- explanation-03: On each ACK the sender increases cwnd roughly by one segment per ACK.
- explanation-08: Without measurements, the improvement from switching is unpredictable — it could be 2% or 60%, depending on payload size and where time actually goes.
- summarization-08: The field-mapping redesign appears to be functioning as intended.

### plain-language

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 0 | 0 | 0 | 0 | n/a |
| code-review-02 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-03 | 0 | 0 | 0 | 0 | n/a |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 1 | 1 | 0 | 0 | 1.0 |
| code-review-06 | 8 | 3 | 1 | 4 | 0.75 |
| code-review-07 | 5 | 4 | 0 | 1 | 1.0 |
| code-review-08 | 10 | 8 | 1 | 1 | 0.889 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 1 | 0 | 0 | 1 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 2 | 2 | 0 | 0 | 1.0 |
| debugging-05 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-06 | 10 | 6 | 1 | 3 | 0.857 |
| debugging-07 | 9 | 6 | 0 | 3 | 1.0 |
| debugging-08 | 7 | 4 | 0 | 3 | 1.0 |
| explanation-01 | 0 | 0 | 0 | 0 | n/a |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 5 | 3 | 0 | 2 | 1.0 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 3 | 3 | 0 | 0 | 1.0 |
| explanation-07 | 0 | 0 | 0 | 0 | n/a |
| explanation-08 | 3 | 1 | 1 | 1 | 0.5 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 2 | 1 | 0 | 0.667 |

Claims: 77 over 32 judged pairs: 51 hedged, 6 certain, 20 absent.

Median survival: 1.0 over 16 scored pairs.

Claims that became certain:

- code-review-02: The line `return profile.name.toUpperCase()` will throw `Cannot read properties of undefined (reading 'name')` essentially every time — i.e. very nearly always, though not stated as strictly guaranteed on every single call.
- code-review-06: The crash when `base[key]` is a dict but `override[key]` isn't is almost certainly a bug rather than a deliberate design choice.
- code-review-08: When the cap does kick in, it doesn't necessarily remove the oldest 500 files — just whichever 500 happened to come first in directory order.
- debugging-06: If a heavy analytics job runs right before or during the 02:13:30–02:14:41 window on failure nights, that would be the smoking gun.
- explanation-08: Without measurements, the improvement from switching is unpredictable — it could be 2% or 60%, depending on payload size and where time actually goes.
- summarization-08: The field-mapping redesign appears to be functioning as intended.

### technical-simplified

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 0 | 0 | 0 | 0 | n/a |
| code-review-02 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-03 | 0 | 0 | 0 | 0 | n/a |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-06 | 8 | 4 | 0 | 4 | 1.0 |
| code-review-07 | 5 | 0 | 0 | 5 | n/a |
| code-review-08 | 10 | 5 | 4 | 1 | 0.556 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 1 | 0 | 0 | 1 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-05 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-06 | 10 | 4 | 1 | 5 | 0.8 |
| debugging-08 | 7 | 0 | 0 | 7 | n/a |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 5 | 1 | 1 | 3 | 0.5 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 3 | 2 | 0 | 1 | 1.0 |
| explanation-07 | 0 | 0 | 0 | 0 | n/a |
| explanation-08 | 3 | 0 | 1 | 2 | 0.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 59 over 27 judged pairs: 20 hedged, 9 certain, 30 absent.

Median survival: 0.678 over 10 scored pairs.

Claims that became certain:

- code-review-02: The line `return profile.name.toUpperCase()` will throw `Cannot read properties of undefined (reading 'name')` essentially every time — i.e. very nearly always, though not stated as strictly guaranteed on every single call.
- code-review-05: A mistaken invocation could wipe .tmp files somewhere unintended (given the unquoted "$BACKUP_DIR" and the lack of a sanity check rejecting values like `.` or `/`, combined with issue #1).
- code-review-08: The bugs listed in the first section are likely to cause real problems.
- code-review-08: The unconditional deletion of `tmp-`/`.part` files almost certainly should have an age threshold (e.g., only remove if older than an hour), unless the export pipeline guarantees these names are never touched while a writer holds them open.
- code-review-08: A TOCTOU race between `listdir` and `getmtime`/`remove` is plausible if the script runs concurrently with itself or alongside the export job.
- code-review-08: Everything else (missing try/except, directory crash, cap not applying to tmp/.part, no logging) reads like gaps rather than choices.
- debugging-06: A connection leak would likely show pool usage trending up over the night rather than spiking suddenly.
- explanation-03: On each ACK the sender increases cwnd roughly by one segment per ACK.
- explanation-08: Without measurements, the improvement from switching is unpredictable — it could be 2% or 60%, depending on payload size and where time actually goes.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 609, measured: 609.
Mean duration: 14500 ms. Mean wall: 26530 ms. Mean startup: 12030 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 609, measured: 609.
Input tokens: 1218 uncached, 1188132 cache write, 1251678 cache read. Output tokens: 712904.
Cache-read share: 0.513.

## Warnings

- technical-simplified/explanation-01: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/summarization-08: the pair failed the gate, excluded
- technical-simplified/debugging-04: the pair failed the gate, excluded
- technical-simplified/debugging-07: the pair failed the gate, excluded
