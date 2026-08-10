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

Judge: opus. Judged on 2026-08-10T07:50:10+00:00.

## Completeness (fact survival)

The judge lists the facts of the unstyled answer, then checks each fact against the styled answer. The fraction is the share of the facts that survive. The judge also lists the facts of the styled answer and checks each fact against the unstyled answer: a styled fact that the unstyled answer does not state is an addition. The lost facts and the added facts appear verbatim below the table.

### clarity-flow

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 28 | 25 | 0.893 | 21 | 4 |
| code-review-02 | 20 | 17 | 0.85 | 19 | 3 |
| code-review-03 | 25 | 18 | 0.72 | 14 | 1 |
| code-review-04 | 27 | 14 | 0.519 | 15 | 3 |
| code-review-05 | 29 | 23 | 0.793 | 28 | 5 |
| code-review-06 | 31 | 19 | 0.613 | 29 | 8 |
| code-review-07 | 44 | 32 | 0.727 | 33 | 5 |
| code-review-08 | 4 | 0 | 0.0 | 36 | 36 |
| debugging-01 | 9 | 9 | 1.0 | 7 | 0 |
| debugging-02 | 15 | 15 | 1.0 | 17 | 0 |
| debugging-03 | 11 | 11 | 1.0 | 10 | 0 |
| debugging-04 | 17 | 10 | 0.588 | 13 | 2 |
| debugging-05 | 20 | 18 | 0.9 | 12 | 2 |
| debugging-06 | 30 | 17 | 0.567 | 16 | 6 |
| debugging-07 | 21 | 13 | 0.619 | 31 | 14 |
| debugging-08 | 46 | 10 | 0.217 | 36 | 14 |
| explanation-01 | 37 | 25 | 0.676 | 25 | 2 |
| explanation-02 | 26 | 20 | 0.769 | 26 | 9 |
| explanation-03 | 41 | 25 | 0.61 | 27 | 3 |
| explanation-04 | 41 | 27 | 0.659 | 26 | 1 |
| explanation-05 | 17 | 13 | 0.765 | 12 | 0 |
| explanation-06 | 26 | 20 | 0.769 | 17 | 0 |
| explanation-07 | 33 | 19 | 0.576 | 31 | 11 |
| explanation-08 | 10 | 8 | 0.8 | 16 | 7 |
| summarization-01 | 8 | 4 | 0.5 | 5 | 1 |
| summarization-02 | 15 | 10 | 0.667 | 16 | 6 |
| summarization-03 | 15 | 15 | 1.0 | 13 | 0 |
| summarization-04 | 15 | 15 | 1.0 | 13 | 0 |
| summarization-05 | 8 | 8 | 1.0 | 8 | 0 |
| summarization-06 | 13 | 12 | 0.923 | 11 | 0 |
| summarization-07 | 3 | 0 | 0.0 | 12 | 12 |
| summarization-08 | 18 | 16 | 0.889 | 22 | 2 |

Median fraction: 0.746 over 32 scored pairs.

Median additions: 2.5 over 32 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python footgun.
- code-review-01: Nothing prevents duplicate users or empty names.
- code-review-01: The bare bool return makes debugging and logging impossible for callers.
- code-review-02: The error thrown is `Cannot read properties of undefined (reading 'name')`.
- code-review-02: Because the function never uses `await`, the `async` keyword gains none of its benefits.
- code-review-02: The fixed version awaits `res.json()` and returns `data.name.toUpperCase()`.
- code-review-03: No relevant context was found stored in memory.
- code-review-03: SQL injection is the OWASP #1 issue.
- code-review-03: The caller cannot distinguish a failed call from one that returned no rows.
- code-review-03: Whether error handling is needed depends on how the caller handles the result.
- code-review-03: Returning raw rows ties callers to the DB driver's row representation rather than a defined interface such as a dict or dataclass.
- code-review-03: The return-type coupling issue is minor and depends on codebase conventions.
- code-review-03: The remaining issues are stylistic or robustness judgments that depend on the codebase's conventions.
- code-review-04: Preemption between read and write can happen mid-bytecode because of the GIL's bytecode-boundary switching.
- code-review-04: The unsynchronized read-modify-write is guaranteed unsafe on non-CPython implementations.
- code-review-04: The operation would also be unsafe if `value` involved a `+=` on a non-atomic object.
- code-review-04: The outcome of a concurrent reset and increment is not documented.
- code-review-04: The class is documented by its usage as multi-threaded, but nothing in the implementation enforces thread safety.
- code-review-04: No `get()` or `value` accessor is shown being used.
- code-review-04: If callers read `counter.value` directly from another thread, that read is not synchronized with writes.
- code-review-04: An unsynchronized read of the counter can return a stale value.
- code-review-04: Torn reads are not a real risk for a Python `int` reference itself.
- code-review-04: The counter's value can be arbitrarily stale relative to other threads' operations, giving no ordering guarantees.
- code-review-04: The fix is to wrap mutations, and ideally reads, in a lock.
- code-review-04: The fixed `Counter` class creates a `threading.Lock` in `__init__` and acquires it in `increment`, `reset`, and the `value` property.
- code-review-04: In the fixed version, the `value` property returns a consistent snapshot instead of racing with in-progress mutations.
- code-review-05: A listing of the memory directory was run and no relevant memory was found.
- code-review-05: A safe form of the directory change is `cd "$BACKUP_DIR" || exit 1`.
- code-review-05: The loop doing nothing when no `.log` files exist is accidental rather than by design.
- code-review-05: `gzip` failures are not checked, so the loop continues silently if a `.log` file is locked or unwritable.
- code-review-05: The final "Cleaned" message is misleading because it implies success regardless of the actual outcome.
- code-review-05: The suggested rewrite uses `#!/bin/sh`, `set -eu`, `BACKUP_DIR=${1:?Usage: $0 <backup_dir>}`, quoted `cd`, `rm -f -- *.tmp`, a `for f in *.log` loop with an `[ -e "$f" ] || continue` guard, `gzip -- "$f"`, and a quoted echo.
- code-review-06: The function performs no input validation.
- code-review-06: If `base` is not dict-like, `dict(base)` raises a confusing `TypeError` or `ValueError`.
- code-review-06: Callers receive a raw traceback into the function's internals rather than a meaningful config error.
- code-review-06: Deeply nested dicts will exceed the recursion limit.
- code-review-06: The function uses an `is None` check rather than a falsy check.
- code-review-06: The `is None` check avoids treating `0`, `""`, `False`, and `[]` as unset.
- code-review-06: If `merged[key]` is a dict and the override value is not (or vice versa), no error is raised.
- code-review-06: On a type mismatch, the override value replaces the entire subtree.
- code-review-06: A typo'd override, such as a string where a nested settings block was expected, silently removes an entire section rather than failing loudly.
- code-review-06: Merging lists is ambiguous regarding whether to append, replace, or dedupe.
- code-review-06: Accepting new keys means typo'd keys are silently accepted as new settings instead of raising an error.
- code-review-06: There are no tests for the function.
- code-review-07: Some old codebases use a 'never throw' contract so callers don't need try/catch.
- code-review-07: Network failures and timeouts are exactly the transient errors that retry logic usually exists for.
- code-review-07: The backoff is fixed and linear with no jitter and no maximum delay cap.
- code-review-07: There is no logging and no error wrapping in the function.
- code-review-07: If `attempts` is 0 or negative, the loop body never runs and `fn` is never invoked.
- code-review-07: With `attempts <= 0`, the function resolves to undefined.
- code-review-07: The default value of `attempts` is 3.
- code-review-07: The wrapper calls `fn(...args)` as a plain function, dropping `this` binding.
- code-review-07: If a caller passes an unbound method such as `withRetry(obj.method)`, `this` inside `fn` will be undefined or wrong.
- code-review-07: The user said they cannot verify whether callers passing unbound methods exist.
- code-review-07: The recommended first fix is making the return contract consistent, by either always throwing on unrecoverable failure or always returning null for every failure path including exhausted retries.
- code-review-07: The helper makes 3 attempts by default.
- code-review-08: The speaker will check memory for relevant context before proceeding.
- code-review-08: The memory may contain context on the project.
- code-review-08: The memory may contain context on the user's review preferences.
- code-review-08: A Read action was performed.
- debugging-04: The byte 0xc3 starts a multi-byte UTF-8 sequence.
- debugging-04: Characters such as é and ñ are encoded by multi-byte UTF-8 sequences beginning with 0xc3.
- debugging-04: The ascii encoding rejects any byte greater than or equal to 0x80.
- debugging-04: Opening a file in binary mode with open(path, "rb") allows counting lines regardless of encoding.
- debugging-04: Binary mode avoids decoding the file entirely.
- debugging-04: Iterating a binary-mode file counts \n-delimited chunks.
- debugging-04: Binary mode is the safest option when the file's encoding is unknown or mixed.
- debugging-05: The fixed function assigns `tags = ["draft"]` when `tags is None`.
- debugging-05: The fixed function uses `tags = tags + ["post"]`, which creates a new list.
- debugging-06: A non-fixed batch number and a weekly cadence fit a timing coincidence better than a data-dependent bug.
- debugging-06: A specific bad row would reliably cause failure on the same batch every time.
- debugging-06: Holding connections open too long is a more likely cause than the pool simply being undersized.
- debugging-06: Database-side degradation from autovacuum, backups, a maintenance window, or a shared DB connection limit can increase per-query latency.
- debugging-06: Increased per-query latency can cause connections to be held longer than the 30-second timeout budget allows.
- debugging-06: The job has a 30-second timeout budget.
- debugging-06: pg_stat_activity is a source of DB-side state showing long-running queries, locks, and connection counts.
- debugging-06: The application logs are rotated, so log data from failures is lost.
- debugging-06: The available log data from the failure was only a fragment.
- debugging-06: The pool topology may be either one pool per worker or one pool shared across all workers.
- debugging-06: If pools are per-worker, worker-3 being singled out could indicate uneven batch distribution rather than global pool exhaustion.
- debugging-06: worker-3 was the worker singled out in the failure.
- debugging-06: The DB-side snapshot and the analytics-schedule correlation are the cheapest diagnostics to set up.
- debugging-07: Two families of cause fit the signature of a parallelism-only flake: a real race in the application and a test isolation problem in xdist workers.
- debugging-07: A real race in the app is the most likely cause.
- debugging-07: Under CI CPU and IO contention from four workers competing for cores, processing of the third event can lag past the fixed wait the test uses before requesting the digest.
- debugging-07: Adding a failure-only diagnostic recording worker id, event IDs and timestamps as created, and the raw digest response, and uploading it as a CI artifact even for transient failures, is the highest-leverage first step.
- debugging-07: If workers share one database, that is likely the culprit and is usually the cheaper fix.
- debugging-07: Logging server-side when each event is created and when the digest is computed, including windowing boundaries, would show on the next failure whether the third event was never created, created but excluded by a time window, or created and then overwritten.
- debugging-07: Artificially adding latency to event creation or oversubscribing workers (for example `-n 8` on a 4-core box) increases contention and can reproduce the failure faster.
- debugging-07: If the failure rate climbs with more contention, that strongly confirms a race rather than isolation bleed.
- debugging-08: The service's memory grows about 2% per day.
- debugging-08: Growth that is worse during campaigns indicates growth tracks distinct new data (new SKUs, promo codes, campaign IDs) rather than raw request count.
- debugging-08: Memory that never drops overnight rules out GC backlog or a young-generation effect that a quiet period would let the collector clean up.
- debugging-08: Memory that never drops overnight means the growing data is either still reachable (a real leak) or is native/off-heap fragmentation that GC cannot touch.
- debugging-08: The most plausible cause is cache eviction that does not actually free memory.
- debugging-08: Lingering references to evicted objects can come from a removal listener that registers something globally, a subscriber list, or a callback captured in a closure.
- debugging-08: Keys with broken equals/hashCode can make a cache believe it evicted something it did not evict.
- debugging-08: Baseline traffic alone churns the cache and leaks a small amount of memory.
- debugging-08: Campaigns push more distinct product and promo keys through the cache, causing more churn and more leaked evictions.
- debugging-08: Leaked objects that are strongly reachable cannot be reclaimed by GC overnight.
- debugging-08: Logging cache size, hit rate, and eviction count over a day can confirm whether entry count stays flat while memory grows.
- debugging-08: `jmap -histo` produces a class histogram that can be taken at two points in a day and diffed.
- debugging-08: If a cached value's class count matches the cache bound while memory keeps climbing, a wrapper or listener object may be growing instead.
- debugging-08: Grepping for `removalListener` or `onEvict`-style hooks can reveal listeners that do not detach fully.
- debugging-08: The second most plausible cause is unbounded metric or log label cardinality.
- debugging-08: Emitting metrics or logs with dynamic labels such as product ID, promo code, or campaign ID creates new time series for every new campaign.
- debugging-08: New time series created by dynamic labels live forever in the metrics client's registry.
- debugging-08: Unbounded label cardinality matches the campaign correlation, the baseline-only canary growth, and the lack of overnight recovery.
- debugging-08: Normal traffic still creates some new metric labels, just fewer than campaign traffic.
- debugging-08: Metrics registries are maps that are never cleared.
- debugging-08: Most metrics client libraries expose a count of registry size.
- debugging-08: The third most plausible cause is a webhook-specific registration leak.
- debugging-08: Grepping for global Map/Set/List structures written to inside webhook handlers can reveal a registration leak.
- debugging-08: Sizes of suspect global structures can be compared between canary and prod via a debug endpoint or periodic size logging.
- debugging-08: The fourth plausible cause is native/off-heap growth from connections, buffers, or fragmentation.
- debugging-08: If the measured memory is RSS rather than a managed heap, growing connection pools, unreturned buffers, or allocator fragmentation from webhook HTTP calls would produce identical symptoms.
- debugging-08: Native/off-heap growth does not show up in heap-only checks.
- debugging-08: Native/off-heap growth can coexist with the cache, metrics, and webhook registration causes.
- debugging-08: RSS can be separated from heap-reported usage using JVM Native Memory Tracking, or `ps` / `/proc/<pid>/status` versus GC/heap stats in other runtimes.
- debugging-08: Open file descriptor and socket counts can be tracked with `lsof` and `ss`.
- debugging-08: A steady climb in file descriptor or socket count points to native growth.
- debugging-08: Comparing canary and prod class/object histograms at the start and end of a campaign day is the cheapest way to identify which structure is growing without a full profile.
- debugging-08: Cache stats and metrics-registry size can be logged on an interval and overlaid against the memory curve.
- debugging-08: Thread count and FD/socket count should be tracked over the day, especially on the webhook-heavy instance.
- debugging-08: Once a candidate class is identified, the code can be grepped for all places holding a reference to it outside the known cache or collection.
- debugging-08: This investigation approach requires no profiler.
- explanation-01: The internal array of a hash map is called the bucket array.
- explanation-01: The bucket array is finite while the set of possible keys is in theory infinite.
- explanation-01: Collisions are unavoidable in a hash map.
- explanation-01: In chaining, large buckets may use a tree instead of a list.
- explanation-01: Chaining delete hashes the key and removes the matching entry from the list.
- explanation-01: Most textbook hash map implementations use chaining by default.
- explanation-01: Quadratic probing and double hashing give better spread than linear probing.
- explanation-01: In open addressing, clearing a deleted slot breaks the probe chain for later lookups.
- explanation-01: Open addressing deletion usually requires a special tombstone marker.
- explanation-01: Deletion is simple in chaining and awkward in open addressing.
- explanation-01: Open addressing requires more careful tuning and more complex deletion logic.
- explanation-01: A good hash function that spreads keys evenly is what keeps collisions rare.
- explanation-02: In the example, a row is read with `version = 5`, edited in memory, then updated with `UPDATE products SET price = 19.99, version = 6 WHERE id = 42 AND version = 5;`.
- explanation-02: REST APIs editing independent records are an example use case for optimistic locking.
- explanation-02: A pessimistic locking example uses `BEGIN;`, `SELECT * FROM products WHERE id = 42 FOR UPDATE;`, `UPDATE products SET price = 19.99 WHERE id = 42;`, and `COMMIT;`.
- explanation-02: Other transactions trying to run `SELECT ... FOR UPDATE` on id=42 block at that statement.
- explanation-02: Generating sequential invoice numbers is an example use case for pessimistic locking.
- explanation-02: The recommended default is to use optimistic locking.
- explanation-03: Packet loss from overflowing router buffers harms all users on that network path.
- explanation-03: The congestion window caps how much unacknowledged data the sender may have in flight at once.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The receiver's advertised window reflects the receiver's buffer space.
- explanation-03: Historically, the initial cwnd was 1 segment.
- explanation-03: The initial cwnd is now typically around 10 segments.
- explanation-03: RFC 6928 specifies the initial congestion window of about 10 segments.
- explanation-03: The sender sends up to cwnd worth of data and then waits for ACKs.
- explanation-03: One round-trip's worth of ACKs returns roughly together.
- explanation-03: An example cwnd progression during slow start is 10 → 20 → 40 → 80.
- explanation-03: Congestion avoidance grows the window linearly rather than exponentially.
- explanation-03: Earlier TCP implementations immediately sent as much data as the receiver's window allowed.
- explanation-03: After slow start, TCP hands off to steadier mechanisms including congestion avoidance and loss/ECN-triggered backoff.
- explanation-03: Slow start recurs after a connection has been idle.
- explanation-03: Slow start recurs after a timeout-based loss.
- explanation-03: Slow start recurs in those cases because the old cwnd value may no longer reflect current network conditions.
- explanation-04: A process is an independent instance of a running program.
- explanation-04: A process has its own file descriptors.
- explanation-04: All threads in a process share the same file descriptors.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own register state.
- explanation-04: Supervisors like systemd favor a process-per-task model.
- explanation-04: Processes can run under different users.
- explanation-04: Processes can run under different sandboxes, such as seccomp or containers.
- explanation-04: Processes can run at different privilege levels.
- explanation-04: Threads cannot be isolated by user, sandbox, or privilege level because they share the same address space and credentials.
- explanation-04: Processes can be killed, restarted, or resource-limited independently.
- explanation-04: Processes can be resource-limited via cgroups and ulimits.
- explanation-04: Inter-process communication mechanisms include pipes, sockets, and shared memory.
- explanation-04: Threads are preferable for many short-lived concurrent tasks, such as handling I/O-bound requests.
- explanation-05: Examples of long-lived objects include a global event bus, a DOM node, and a singleton.
- explanation-05: Closures capturing more than they need are a frequent cause of memory leaks.
- explanation-05: Detached-but-referenced resources are a frequent cause of memory leaks.
- explanation-05: A removed DOM node that is still referenced by JavaScript code is an example of a detached-but-referenced resource.
- explanation-06: In a write-heavy workload, writes still hit the database.
- explanation-06: A product page fetched thousands of times is an example of a repeat-query workload that benefits from caching.
- explanation-06: If each query has different parameters, nothing repeats in the cache.
- explanation-06: Checking the slow query log and running EXPLAIN on the heaviest queries is a recommended diagnostic step.
- explanation-06: Profiling first reveals which specific queries or endpoints to target rather than caching everything.
- explanation-06: Redis is an example of a cache.
- explanation-07: 200 GB of data growing at 10% per year is a non-event.
- explanation-07: If a product team cannot estimate its data growth rate, that usually means the product isn't proven yet.
- explanation-07: An unproven product is a strong argument against sharding.
- explanation-07: Sharding fixes write throughput problems.
- explanation-07: Sharding does nothing to fix slow queries.
- explanation-07: Sharding does nothing to fix missing indexes.
- explanation-07: Sharding does nothing to fix bad connection pooling.
- explanation-07: Sharding does nothing to fix read-heavy load.
- explanation-07: Modern hardware can handle multi-terabyte Postgres instances with proper indexing, partitioning, and tuning.
- explanation-07: A 200 GB deployment likely has 5-10x headroom before vertical scaling plus read replicas stop working.
- explanation-07: Sharding requires a shard key that distributes data evenly.
- explanation-07: Under sharding, cross-shard transactions, joins, and unique constraints become permanent application-level problems.
- explanation-07: Migrating under pressure is riskier but still doable.
- explanation-07: Sharding is a one-way architectural door.
- explanation-08: Serialization is usually a small slice of total request time.
- explanation-08: The speaker can help set up that profiling.
- summarization-01: App startup is now up to 40% faster.
- summarization-01: Internal-only changes were omitted from the release notes.
- summarization-01: The omitted internal changes include build tooling, a module refactor, and the telemetry interval.
- summarization-01: The omitted internal changes do not affect user-facing behavior.
- summarization-02: The config review checklist likely does not cover other performance-critical settings.
- summarization-02: The team was paged at 09:21.
- summarization-02: Detection-to-mitigation took approximately 34 minutes.
- summarization-02: The detection-to-mitigation response was reactive rather than preventive.
- summarization-02: A pre-deploy check or an automated diff/alert on config value changes could have caught the issue before it reached production.
- summarization-06: The on-call engineer suspects connection-pool exhaustion in the payments client.
- summarization-07: The speaker is checking memory for relevant context.
- summarization-07: The check is being done before writing a summary.
- summarization-07: A summary is going to be written.
- summarization-08: The progress bar finding is rated Firm for the abandonment behavior and Tentative for the cause.
- summarization-08: The cause of the abandonment (perceived versus real stall) is inferred rather than confirmed.

Added facts (styled only):

- code-review-01: The function has no duplicate check, so "member" is appended even if it is already in `roles`.
- code-review-01: Returning `True`/`False` loses the inserted record, the generated ID, and the specific failure reason.
- code-review-01: The fixed `add_user` raises `ValueError("name is required")` when `name` is falsy.
- code-review-01: The fixed version appends "member" only if it is not already in `roles`.
- code-review-02: `fetch` only rejects on network failures.
- code-review-02: Any rejection in the discarded `.then()` chain becomes an unhandled promise rejection that the caller never sees.
- code-review-02: A corrected version awaits `fetch(`/api/users/${userId}`)`, throws an `Error` with the status when `res.ok` is false, awaits `res.json()`, and returns `profile.name.toUpperCase()`.
- code-review-03: A malformed query or connection failure propagates as a raw driver exception with no context about which lookup failed.
- code-review-04: In the fixed version, `Counter.__init__` sets `self.value = 0` and `self._lock = threading.Lock()`.
- code-review-04: In the fixed version, `increment` executes `self.value += 1` while holding `self._lock`.
- code-review-04: In the fixed version, `reset` executes `self.value = 0` while holding `self._lock`.
- code-review-05: `rm -rf *.tmp` should be written as `rm -rf -- *.tmp`.
- code-review-05: The `--` separator protects against filenames that start with a hyphen.
- code-review-05: The suggested rewrite checks `[ -d "$BACKUP_DIR" ]` and exits with an error message to stderr if it is not a directory.
- code-review-05: The suggested rewrite loops over *.tmp and *.log with an `[ -e "$f" ]` existence test before acting.
- code-review-05: The suggested rewrite uses `rm -f -- "$f"` and `gzip -- "$f"`.
- code-review-06: The `elif` branch only checks `isinstance(merged[key], dict)`.
- code-review-06: The code never checks whether `value` is also a dict.
- code-review-06: If `base` has `{"db": {"host": "x"}}` and `override` has `{"db": "disabled"}`, the code calls `merge_settings({"host": "x"}, "disabled")`.
- code-review-06: That call then invokes `"disabled".items()` and raises `AttributeError`.
- code-review-06: Any caller that lets a user replace a nested-object setting with a scalar will hit this crash.
- code-review-06: Wholesale replacement of non-dict collections is standard for settings-merge functions.
- code-review-06: There is no way to force a full replace of a nested dict.
- code-review-06: `dict(base)` silently downgrades any dict subclass, such as `OrderedDict` or a custom mapping, to a plain `dict`.
- code-review-07: When i === attempts - 1 and the error is a 429, the code still awaits setTimeout before discovering the loop is over.
- code-review-07: The delay on the final attempt accomplishes nothing.
- code-review-07: 429 errors get exponential-ish backoff while 5xx errors are retried immediately.
- code-review-07: If args contains stateful values such as a FormData, a stream, or an AbortSignal, replaying them across retries may fail silently or misbehave.
- code-review-07: The function has no way to guard against stateful args because it just re-passes ...args.
- code-review-08: The script contains real bugs as well as several risky choices that could be intentional.
- code-review-08: os.remove raises IsADirectoryError when called on a directory.
- code-review-08: Directories under ROOT whose names start with 'tmp-' or that are old will cause the deletion loop to crash mid-run.
- code-review-08: When the loop dies mid-run, there is no logging of what was already deleted or what remains.
- code-review-08: The sequence os.listdir → os.path.getmtime → os.remove is a TOCTOU race.
- code-review-08: If another process deletes a file between the listing and the stat/remove, the script raises FileNotFoundError and the run is killed.
- code-review-08: The script runs on a schedule.
- code-review-08: Overlapping or concurrent jobs writing to the same directory make the TOCTOU race likely rather than hypothetical.
- code-review-08: Broken symlinks cause getmtime to crash, producing the same failure mode.
- code-review-08: The file has no entry point; nothing in the file calls clean().
- code-review-08: Whatever schedules the script must invoke it via something like python -c "import x; x.clean()".
- code-review-08: CUTOFF is computed once at import time rather than per call.
- code-review-08: If a long-lived process calls clean() repeatedly instead of spawning a fresh interpreter, the 45-day cutoff never moves and every run after the first uses a stale cutoff.
- code-review-08: The stale cutoff bug is invisible until someone checks why old files aren't being swept.
- code-review-08: Files matching 'tmp-' or '.part' are deleted regardless of age, with no mtime check.
- code-review-08: A one-second-old file matching the tmp-/.part pattern is deleted just as readily as a month-old one.
- code-review-08: Incremental writes to tmp-* or *.part files are a common naming convention for in-progress writes.
- code-review-08: The script can delete another process's file mid-write.
- code-review-08: The unconditional tmp-/.part deletion is the highest-risk line in the script.
- code-review-08: The 500-item cap guards only the age-based branch and not the pattern-based branch.
- code-review-08: tmp-/.part deletions are unbounded per run while old-file deletions are capped at 500.
- code-review-08: os.listdir gives no ordering guarantee.
- code-review-08: Which old files survive past the 500-item cap on a given run is arbitrary rather than oldest-first or otherwise principled.
- code-review-08: The script has no dry-run mode and no logging of removed filenames.
- code-review-08: The script has unattended production delete authority and no audit trail for reconstructing what happened.
- code-review-08: The script does not handle ROOT being missing, unmounted, or empty.
- code-review-08: os.listdir throws on a missing path.
- code-review-08: A failed mount that resolves to an empty local directory would silently no-op rather than fail loudly.
- code-review-08: The 45-day cutoff and 500-item cap read like deliberate retention and throttling policy, such as a compliance window and a blast-radius limit.
- code-review-08: There are zero comments or configuration for the cutoff and cap values, so they cannot be confirmed as still correct and cannot be safely changed.
- code-review-08: Immediate deletion of tmp-/.part files without an age check may be intentional on the theory that such files are leftover garbage from crashed jobs.
- code-review-08: Treating tmp-/.part files as crash leftovers is a reasonable policy.
- code-review-08: As written, the script does not distinguish a file orphaned three days ago from one being written right now.
- code-review-08: The tmp-/.part branch should require an age threshold, for example only deleting such files older than an hour, to close the race with active writers.
- code-review-08: The top recommended single fix is adding an age check to the tmp-/.part branch.
- code-review-08: The tmp-/.part branch is the part most likely to be silently deleting another process's in-progress output.
- debugging-04: Using errors="replace" or errors="ignore" is acceptable when exact byte fidelity does not matter.
- debugging-04: Exact byte fidelity does not matter for counting lines.
- debugging-05: The fixed version uses `tags=None` as the default and assigns `tags = list(DEFAULT_TAGS)` when `tags` is None.
- debugging-05: The fix also protects any caller who passes in their own list.
- debugging-06: An undersized connection pool is the most likely cause of the failures.
- debugging-06: The failure only occurs when both workloads spike at the same time.
- debugging-06: The observed failure occurred between 02:13 and 02:15 UTC on 2026-07-29.
- debugging-06: A connection leak appears as idle connections accumulating over time rather than a sudden spike.
- debugging-06: The database has its own max_connections limit that the configured max pool size should be checked against.
- debugging-06: The analytics service may have its own separate pool competing for the same database connection limit.
- debugging-07: If test setup and the digest read use different DB connections or transactions and the isolation level permits it, the third insert may not be visible to the read.
- debugging-07: Transaction isolation and connection pooling visibility problems get worse under contention.
- debugging-07: A query LIMIT combined with events lacking a stable sort key would not drop a count under normal conditions.
- debugging-07: Shared test state to look for includes a shared test DB, a global counter, a fixed user ID, and a fixed digest window.
- debugging-07: A digest window defined as 'events from today' is an example of a non-worker-scoped fixed window.
- debugging-07: `pytest-xdist` gives each worker its own process.
- debugging-07: The CI system keeps no artifacts.
- debugging-07: The worker ID is available in the `PYTEST_XDIST_WORKER` environment variable.
- debugging-07: The current failure output is a bare '2 == 3'.
- debugging-07: Adding an explicit wait-for-consistency call or a short-timeout poll before requesting the digest tests the eventual-consistency hypothesis.
- debugging-07: If the flake disappears after adding a synchronization point, that confirms a race rather than a logic bug.
- debugging-07: Running CI with `-n 1` keeps CI's environment but makes execution serial.
- debugging-07: Running CI serially separates a concurrency bug from CI simply being slower and hitting a real timeout.
- debugging-07: Step 1, reproducing the flake locally under `-n 4`, should be done first.
- debugging-08: The other leak is a slower baseline leak unrelated to traffic.
- debugging-08: The four clues split into two mechanisms.
- debugging-08: Traffic-proportional growth that survives quiet nights points to objects retained per request.
- debugging-08: Per-request retained objects can take the form of promises or timers that never resolve.
- debugging-08: Comparing growth rate against webhook request-rate metrics over several days can confirm the webhook-driven leak.
- debugging-08: A tight correlation between growth rate and webhook request rate would confirm the webhook-driven leak.
- debugging-08: Candidate sources of the baseline leak include background jobs, log buffers, connection pools, and metrics or histogram objects that accumulate unbounded labels.
- debugging-08: The cache is a secondary suspect rather than the primary one.
- debugging-08: The cache code has not changed in a year.
- debugging-08: A size-bounded, unchanged cache fits a 'grows then plateaus' pattern rather than 'grows every day forever'.
- debugging-08: Growing entry size could come from product descriptions or images getting bigger.
- debugging-08: No heap profile has been taken yet.
- debugging-08: The suggested next step is to obtain a heap profile.
- debugging-08: Snapshotting a production instance under campaign load isolates the webhook leak.
- explanation-01: Most general-purpose hash maps use chaining for its predictable worst case.
- explanation-01: Performance-critical hash maps use open addressing for cache efficiency.
- explanation-02: In an example of optimistic locking, two admins open the same e-commerce product to edit its price.
- explanation-02: In that example, each admin holds the row's version = 5.
- explanation-02: In that example, Admin A saves first and the row becomes version = 6.
- explanation-02: In that example, Admin B's save runs UPDATE products SET price = ? WHERE id = ? AND version = 5.
- explanation-02: In that example, Admin B's update matches zero rows.
- explanation-02: In that example, the app detects the conflict and reloads Admin B's form.
- explanation-02: Optimistic locking fits when holding a lock for the duration of user think-time would waste resources.
- explanation-02: In a bank transfer example, the transaction runs SELECT balance FROM accounts WHERE id = 123 FOR UPDATE.
- explanation-02: That SELECT ... FOR UPDATE locks the row so no concurrent transaction can debit the same account until the transfer commits or rolls back.
- explanation-03: A connection's path might be a fast local link or a congested overseas link.
- explanation-03: During congestion collapse, overloaded links spent most of their capacity retransmitting lost packets instead of moving new data.
- explanation-03: ssthresh is set from a previous slowdown.
- explanation-04: Process switching is costly because the CPU must swap out an entire memory mapping.
- explanation-07: A growth rate is the one input that sharding decisions actually require.
- explanation-07: Choosing a shard key without knowing the growth rate is a guess likely to be undone later.
- explanation-07: Sharding pays off when a single instance will hit a hard limit within a plannable time horizon.
- explanation-07: Hard limits that motivate sharding include disk, IOPS, and vertical-scale cost.
- explanation-07: The product team said it cannot say how much the data will grow.
- explanation-07: Cheaper alternatives to sharding include bigger disks, read replicas, connection pooling, better indexes, partitioning within one instance, and moving cold data to cheaper storage.
- explanation-07: Tenant ID, user ID, and region are examples of natural shard keys.
- explanation-07: Sharding is worth it only once a team has the tooling and bandwidth to run a distributed system reliably.
- explanation-07: Vertical scaling has a real ceiling in both cost and hardware.
- explanation-07: Recommended optimizations are indexes, partitioning, read replicas, and archiving cold data.
- explanation-07: Disk usage, write volume, and query latency should be tracked monthly.
- explanation-08: Protobuf, MessagePack, and FlatBuffers are binary formats.
- explanation-08: Binary formats typically cut payload size 20-50% versus JSON.
- explanation-08: Binary formats typically cut serialization CPU time 2-10x versus JSON.
- explanation-08: Serialization taking about 5% of a request's time is common when the bottleneck is a database call or network round-trip.
- explanation-08: Serialization taking about 40% of a request's time is common in high-throughput internal RPC.
- explanation-08: Smaller payloads help most when bandwidth or client-side parsing is the constraint.
- explanation-08: Bandwidth or client-side parsing is typically the constraint for mobile clients, large payloads, and high request volume.
- summarization-01: The app now starts up about 40% faster.
- summarization-02: A deployment on the prior night dropped the checkout service's DB connection pool size from 50 to 5 connections.
- summarization-02: The reduced connection pool was exhausted under load.
- summarization-02: The pool exhaustion caused approximately 12% error rates.
- summarization-02: The elevated error rates lasted 34 minutes.
- summarization-02: The incident ran from 09:14 to 09:48 UTC.
- summarization-02: Staging intentionally uses small connection pool sizes.
- summarization-07: The staging test ran for six hours.
- summarization-07: The staging test cut median latency by 18%.
- summarization-07: Tail latency appeared to improve during the test.
- summarization-07: Staging traffic runs smoother than production traffic.
- summarization-07: The p99 latency gain is likely optimistic rather than confirmed.
- summarization-07: Memory per worker rose by about 60 MB.
- summarization-07: The larger buffer pool is the suspected cause of the memory increase.
- summarization-07: The memory increase has not been profiled to confirm its cause.
- summarization-07: One worker crashed once during the test.
- summarization-07: The crash may be tied to staging's newer kernel rather than the batcher.
- summarization-07: Staging runs a newer kernel.
- summarization-07: A batcher bug has not yet been ruled out as the cause of the crash.
- summarization-08: The large-file upload finding is rated as tentative but worth prioritizing.
- summarization-08: The small sample size makes the large-file upload finding tentative.

### classic-concise

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 28 | 24 | 0.857 | 17 | 3 |
| code-review-02 | 20 | 19 | 0.95 | 16 | 2 |
| code-review-03 | 25 | 11 | 0.44 | 17 | 4 |
| code-review-04 | 27 | 20 | 0.741 | 19 | 2 |
| code-review-05 | 29 | 23 | 0.793 | 27 | 3 |
| code-review-06 | 31 | 25 | 0.806 | 26 | 7 |
| code-review-07 | 44 | 27 | 0.614 | 40 | 15 |
| code-review-08 | 4 | 0 | 0.0 | 32 | 32 |
| debugging-01 | 9 | 8 | 0.889 | 6 | 0 |
| debugging-02 | 15 | 10 | 0.667 | 8 | 1 |
| debugging-03 | 11 | 8 | 0.727 | 5 | 0 |
| debugging-04 | 17 | 7 | 0.412 | 10 | 1 |
| debugging-05 | 20 | 17 | 0.85 | 13 | 2 |
| debugging-06 | 30 | 20 | 0.667 | 23 | 5 |
| debugging-07 | 21 | 13 | 0.619 | 25 | 10 |
| debugging-08 | 46 | 23 | 0.5 | 34 | 16 |
| explanation-01 | 37 | 25 | 0.676 | 22 | 1 |
| explanation-02 | 26 | 21 | 0.808 | 24 | 1 |
| explanation-03 | 41 | 26 | 0.634 | 22 | 6 |
| explanation-04 | 41 | 28 | 0.683 | 23 | 4 |
| explanation-05 | 17 | 13 | 0.765 | 14 | 1 |
| explanation-06 | 26 | 17 | 0.654 | 13 | 0 |
| explanation-07 | 33 | 25 | 0.758 | 21 | 3 |
| explanation-08 | 10 | 7 | 0.7 | 14 | 9 |
| summarization-01 | 8 | 5 | 0.625 | 5 | 1 |
| summarization-02 | 15 | 14 | 0.933 | 13 | 2 |
| summarization-03 | 15 | 15 | 1.0 | 12 | 0 |
| summarization-04 | 15 | 12 | 0.8 | 12 | 2 |
| summarization-05 | 8 | 6 | 0.75 | 10 | 0 |
| summarization-06 | 13 | 12 | 0.923 | 13 | 1 |
| summarization-07 | 3 | 0 | 0.0 | 15 | 15 |
| summarization-08 | 18 | 17 | 0.944 | 15 | 0 |

Median fraction: 0.734 over 32 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python footgun.
- code-review-01: Nothing prevents duplicate users or empty names.
- code-review-01: The bare bool return makes debugging and logging impossible for callers.
- code-review-01: The fixed version lets real exceptions propagate so callers can handle or log them.
- code-review-02: The fixed version throws an `Error` with the message `Failed to load profile: ${res.status}` when `res.ok` is false.
- code-review-03: Memory was checked for relevant context before the review was written.
- code-review-03: No relevant context was found stored in memory.
- code-review-03: SQL injection is the OWASP #1 issue.
- code-review-03: sqlite3 uses `?` placeholders instead of `%s`.
- code-review-03: Placeholder syntax is database-driver-specific.
- code-review-03: The code performs no input validation.
- code-review-03: The code does not check that `customer_name` and `status` are non-empty strings or of the expected type before use.
- code-review-03: The caller cannot distinguish a failed call from one that returned no rows.
- code-review-03: Whether error handling is needed depends on how the caller handles the result.
- code-review-03: The function returns raw `fetchall()` tuples/rows directly.
- code-review-03: Returning raw rows ties callers to the DB driver's row representation rather than a defined interface such as a dict or dataclass.
- code-review-03: The return-type coupling issue is minor and depends on codebase conventions.
- code-review-03: The SQL injection is the only issue that must be fixed regardless of context.
- code-review-03: The remaining issues are stylistic or robustness judgments that depend on the codebase's conventions.
- code-review-04: Preemption between read and write can happen mid-bytecode because of the GIL's bytecode-boundary switching.
- code-review-04: The operation would also be unsafe if `value` involved a `+=` on a non-atomic object.
- code-review-04: The outcome of a concurrent reset and increment is not documented.
- code-review-04: The class is documented by its usage as multi-threaded, but nothing in the implementation enforces thread safety.
- code-review-04: No `get()` or `value` accessor is shown being used.
- code-review-04: Torn reads are not a real risk for a Python `int` reference itself.
- code-review-04: The counter's value can be arbitrarily stale relative to other threads' operations, giving no ordering guarantees.
- code-review-05: A listing of the memory directory was run and no relevant memory was found.
- code-review-05: A safe form of the directory change is `cd "$BACKUP_DIR" || exit 1`.
- code-review-05: `nullglob` is off by default in `sh`.
- code-review-05: If no `.log` files exist, `*.log` expands literally, `ls *.log` writes an error to stderr, and the command substitution returns nothing, so the loop does nothing.
- code-review-05: The loop doing nothing when no `.log` files exist is accidental rather than by design.
- code-review-05: The script does not check that `$BACKUP_DIR` is a directory before operating on it.
- code-review-06: If `base` is not dict-like, `dict(base)` raises a confusing `TypeError` or `ValueError`.
- code-review-06: Deeply nested dicts will exceed the recursion limit.
- code-review-06: The function uses an `is None` check rather than a falsy check.
- code-review-06: The `is None` check avoids treating `0`, `""`, `False`, and `[]` as unset.
- code-review-06: Accepting new keys means typo'd keys are silently accepted as new settings instead of raising an error.
- code-review-06: There are no tests for the function.
- code-review-07: Some old codebases use a 'never throw' contract so callers don't need try/catch.
- code-review-07: The user said callers exist that they cannot see.
- code-review-07: The checks `err.status === 429` and `err.status >= 500` assume err always has a numeric .status property.
- code-review-07: Network failures and timeouts are exactly the transient errors that retry logic usually exists for.
- code-review-07: Treating non-HTTP errors as terminal looks like an oversight rather than intent.
- code-review-07: There is no logging and no error wrapping in the function.
- code-review-07: If `attempts` is 0 or negative, the loop body never runs and `fn` is never invoked.
- code-review-07: With `attempts <= 0`, the function resolves to undefined.
- code-review-07: The default value of `attempts` is 3.
- code-review-07: The wrapper calls `fn(...args)` as a plain function, dropping `this` binding.
- code-review-07: If a caller passes an unbound method such as `withRetry(obj.method)`, `this` inside `fn` will be undefined or wrong.
- code-review-07: The user said they cannot verify whether callers passing unbound methods exist.
- code-review-07: Retrying 429 with backoff, retrying 5xx, and not retrying other errors is likely a deliberate policy choice.
- code-review-07: The lack of retry for errors without .status is likely a bug and an oversight.
- code-review-07: Whether the absence of backoff before retrying 5xx is deliberate or a bug is unclear.
- code-review-07: The recommended first fix is making the return contract consistent, by either always throwing on unrecoverable failure or always returning null for every failure path including exhausted retries.
- code-review-07: The helper makes 3 attempts by default.
- code-review-08: The speaker will check memory for relevant context before proceeding.
- code-review-08: The memory may contain context on the project.
- code-review-08: The memory may contain context on the user's review preferences.
- code-review-08: A Read action was performed.
- debugging-01: The corrected get_url function returns f"http://{cfg['host']}:{cfg['port']}/api".
- debugging-02: In strict mode and in modules, `this` in such a callback is undefined.
- debugging-02: Accessing `this.seconds` when `this` is undefined throws a TypeError: Cannot read properties of undefined.
- debugging-02: Seeing NaN instead indicates the function ran in a non-strict context where `this` resolved to the global object.
- debugging-02: Calling .bind(this) on the function is an alternative fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-03: The sum of the window `[3,4]` is 7.
- debugging-03: `moving_sum` returns the sum of each window of the given size.
- debugging-03: The fixed `moving_sum([1, 2, 3, 4], 2)` returns `[3, 5, 7]`.
- debugging-04: The byte 0xc3 starts a multi-byte UTF-8 sequence.
- debugging-04: Characters such as é and ñ are encoded by multi-byte UTF-8 sequences beginning with 0xc3.
- debugging-04: The code forces encoding="ascii".
- debugging-04: The ascii encoding rejects any byte greater than or equal to 0x80.
- debugging-04: Passing errors="ignore" with encoding="utf-8" tolerates bad bytes.
- debugging-04: charset-normalizer is a library that can detect the actual encoding of a file.
- debugging-04: Opening a file in binary mode with open(path, "rb") allows counting lines regardless of encoding.
- debugging-04: Binary mode avoids decoding the file entirely.
- debugging-04: Iterating a binary-mode file counts \n-delimited chunks.
- debugging-04: Binary mode is the safest option when the file's encoding is unknown or mixed.
- debugging-05: The test passes when run alone.
- debugging-05: The extra appended entries make the test's equality check fail.
- debugging-05: The fixed function uses `tags = tags + ["post"]`, which creates a new list.
- debugging-06: The failure occurs about once a week.
- debugging-06: A non-fixed batch number and a weekly cadence fit a timing coincidence better than a data-dependent bug.
- debugging-06: A connection leak does not explain the weekly periodicity as cleanly as analytics-job contention does.
- debugging-06: Increased per-query latency can cause connections to be held longer than the 30-second timeout budget allows.
- debugging-06: The job has a 30-second timeout budget.
- debugging-06: The problem cannot be reproduced on demand.
- debugging-06: The pool topology may be either one pool per worker or one pool shared across all workers.
- debugging-06: If pools are per-worker, worker-3 being singled out could indicate uneven batch distribution rather than global pool exhaustion.
- debugging-06: worker-3 was the worker singled out in the failure.
- debugging-06: The DB-side snapshot and the analytics-schedule correlation are the cheapest diagnostics to set up.
- debugging-07: Under CI CPU and IO contention from four workers competing for cores, processing of the third event can lag past the fixed wait the test uses before requesting the digest.
- debugging-07: If the digest query is windowed by time, slower request round-trips under load could push the third event's timestamp outside the window.
- debugging-07: Examples of shared state include the same digest bucket, the same default user, and the same 'latest N events' query with no test-specific filter.
- debugging-07: Adding a failure-only diagnostic recording worker id, event IDs and timestamps as created, and the raw digest response, and uploading it as a CI artifact even for transient failures, is the highest-leverage first step.
- debugging-07: If workers share one database, that is likely the culprit and is usually the cheaper fix.
- debugging-07: Logging server-side when each event is created and when the digest is computed, including windowing boundaries, would show on the next failure whether the third event was never created, created but excluded by a time window, or created and then overwritten.
- debugging-07: Artificially adding latency to event creation or oversubscribing workers (for example `-n 8` on a 4-core box) increases contention and can reproduce the failure faster.
- debugging-07: If the failure rate climbs with more contention, that strongly confirms a race rather than isolation bleed.
- debugging-08: The service's memory grows about 2% per day.
- debugging-08: Growth that is worse during campaigns indicates growth tracks distinct new data (new SKUs, promo codes, campaign IDs) rather than raw request count.
- debugging-08: Memory never drops overnight.
- debugging-08: Memory that never drops overnight rules out GC backlog or a young-generation effect that a quiet period would let the collector clean up.
- debugging-08: Memory that never drops overnight means the growing data is either still reachable (a real leak) or is native/off-heap fragmentation that GC cannot touch.
- debugging-08: The service has a size-bounded cache whose bound has been unchanged for a year.
- debugging-08: The most plausible cause is cache eviction that does not actually free memory.
- debugging-08: Keys with broken equals/hashCode can make a cache believe it evicted something it did not evict.
- debugging-08: Baseline traffic alone churns the cache and leaks a small amount of memory.
- debugging-08: Campaigns push more distinct product and promo keys through the cache, causing more churn and more leaked evictions.
- debugging-08: If a cached value's class count matches the cache bound while memory keeps climbing, a wrapper or listener object may be growing instead.
- debugging-08: Grepping for `removalListener` or `onEvict`-style hooks can reveal listeners that do not detach fully.
- debugging-08: The second most plausible cause is unbounded metric or log label cardinality.
- debugging-08: Emitting metrics or logs with dynamic labels such as product ID, promo code, or campaign ID creates new time series for every new campaign.
- debugging-08: New time series created by dynamic labels live forever in the metrics client's registry.
- debugging-08: Unbounded label cardinality matches the campaign correlation, the baseline-only canary growth, and the lack of overnight recovery.
- debugging-08: Normal traffic still creates some new metric labels, just fewer than campaign traffic.
- debugging-08: Metrics registries are maps that are never cleared.
- debugging-08: Most metrics client libraries expose a count of registry size.
- debugging-08: Sizes of suspect global structures can be compared between canary and prod via a debug endpoint or periodic size logging.
- debugging-08: Comparing canary and prod class/object histograms at the start and end of a campaign day is the cheapest way to identify which structure is growing without a full profile.
- debugging-08: Cache stats and metrics-registry size can be logged on an interval and overlaid against the memory curve.
- debugging-08: This investigation approach requires no profiler.
- explanation-01: The internal array of a hash map is called the bucket array.
- explanation-01: The bucket array is finite while the set of possible keys is in theory infinite.
- explanation-01: Collisions are unavoidable in a hash map.
- explanation-01: In chaining, large buckets may use a tree instead of a list.
- explanation-01: Java's HashMap uses chaining by default.
- explanation-01: Most textbook hash map implementations use chaining by default.
- explanation-01: Linear probing tries index+1, then index+2, and so on.
- explanation-01: Quadratic probing and double hashing give better spread than linear probing.
- explanation-01: In open addressing, clearing a deleted slot breaks the probe chain for later lookups.
- explanation-01: Python's dict uses open addressing.
- explanation-01: Chaining is simpler to reason about and tolerates a high load factor.
- explanation-01: A good hash function that spreads keys evenly is what keeps collisions rare.
- explanation-02: In the example, a row is read with `version = 5`, edited in memory, then updated with `UPDATE products SET price = 19.99, version = 6 WHERE id = 42 AND version = 5;`.
- explanation-02: A pessimistic locking example uses `BEGIN;`, `SELECT * FROM products WHERE id = 42 FOR UPDATE;`, `UPDATE products SET price = 19.99 WHERE id = 42;`, and `COMMIT;`.
- explanation-02: Other transactions trying to run `SELECT ... FOR UPDATE` on id=42 block at that statement.
- explanation-02: Generating sequential invoice numbers is an example use case for pessimistic locking.
- explanation-02: The recommended default is to use optimistic locking.
- explanation-03: Routers between sender and receiver have limited buffer space.
- explanation-03: Packet loss from overflowing router buffers harms all users on that network path.
- explanation-03: A sender that is too conservative wastes available bandwidth.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The receiver's advertised window reflects the receiver's buffer space.
- explanation-03: Historically, the initial cwnd was 1 segment.
- explanation-03: RFC 6928 specifies the initial congestion window of about 10 segments.
- explanation-03: Exponential growth is a compromise between probing the network gently and reaching a reasonable sending rate quickly.
- explanation-03: Slow start reaches a reasonable sending rate within a handful of round trips.
- explanation-03: Linear growth from 1 segment would take far too long to reach useful throughput on high-bandwidth paths.
- explanation-03: After slow start, TCP hands off to steadier mechanisms including congestion avoidance and loss/ECN-triggered backoff.
- explanation-03: Those steadier mechanisms fine-tune around the capacity estimate for the rest of the connection's life.
- explanation-03: Slow start recurs after a connection has been idle.
- explanation-03: Slow start recurs after a timeout-based loss.
- explanation-03: Slow start recurs in those cases because the old cwnd value may no longer reflect current network conditions.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own register state.
- explanation-04: Switching between threads is cheaper than switching between processes.
- explanation-04: Threads are cheaper than processes because there is no memory space to duplicate or isolate.
- explanation-04: Supervisors like systemd favor a process-per-task model.
- explanation-04: Erlang's OTP favors a process-per-task model.
- explanation-04: Processes can run under different users.
- explanation-04: Processes can run under different sandboxes, such as seccomp or containers.
- explanation-04: Processes can run at different privilege levels.
- explanation-04: Threads cannot be isolated by user, sandbox, or privilege level because they share the same address space and credentials.
- explanation-04: Processes can be resource-limited via cgroups and ulimits.
- explanation-04: Inter-process communication mechanisms include pipes, sockets, and shared memory.
- explanation-04: For lightweight concurrent tasks, the overhead of separate memory spaces would dominate.
- explanation-05: Examples of long-lived objects include a global event bus, a DOM node, and a singleton.
- explanation-05: Closures capturing more than they need are a frequent cause of memory leaks.
- explanation-05: Detached-but-referenced resources are a frequent cause of memory leaks.
- explanation-05: A removed DOM node that is still referenced by JavaScript code is an example of a detached-but-referenced resource.
- explanation-06: A cache in front of the database does not help when slowness comes from N+1 queries.
- explanation-06: A cache in front of the database does not help when slowness comes from missing indexes.
- explanation-06: In a write-heavy workload, writes still hit the database.
- explanation-06: Adding a cache introduces the additional cost of invalidating or updating the cache on writes.
- explanation-06: A cache adds real complexity, including staleness bugs and invalidation logic.
- explanation-06: A product page fetched thousands of times is an example of a repeat-query workload that benefits from caching.
- explanation-06: Checking the slow query log and running EXPLAIN on the heaviest queries is a recommended diagnostic step.
- explanation-06: Profiling first reveals which specific queries or endpoints to target rather than caching everything.
- explanation-06: Redis is an example of a cache.
- explanation-07: If a product team cannot estimate its data growth rate, that usually means the product isn't proven yet.
- explanation-07: An unproven product is a strong argument against sharding.
- explanation-07: Sharding does nothing to fix slow queries.
- explanation-07: Sharding does nothing to fix missing indexes.
- explanation-07: Sharding does nothing to fix bad connection pooling.
- explanation-07: Sharding does nothing to fix read-heavy load.
- explanation-07: Sharding requires a shard key that distributes data evenly.
- explanation-07: Sharding is a one-way architectural door.
- explanation-08: Serialization is usually a small slice of total request time.
- explanation-08: Network I/O, database queries, and business logic often dominate total request time.
- explanation-08: The speaker can help set up that profiling.
- summarization-01: Internal-only changes were omitted from the release notes.
- summarization-01: The omitted internal changes include build tooling, a module refactor, and the telemetry interval.
- summarization-01: The omitted internal changes do not affect user-facing behavior.
- summarization-02: The detection-to-mitigation response was reactive rather than preventive.
- summarization-04: The report selected to reproduce the bug is the "March" report.
- summarization-04: Reproducing the bug involves clicking the export button and choosing PDF rather than CSV.
- summarization-04: The bug was reproduced on two different machines.
- summarization-05: Ada is to check with the mobile team's lead to confirm the mobile team has been informed of the API deprecation.
- summarization-05: Chen is to continue search indexing work.
- summarization-06: Connection-pool exhaustion and a retry storm are the leading but unconfirmed hypotheses for the root cause.
- summarization-07: The speaker is checking memory for relevant context.
- summarization-07: The check is being done before writing a summary.
- summarization-07: A summary is going to be written.
- summarization-08: The progress bar finding is rated Firm for the abandonment behavior and Tentative for the cause.

Added facts (styled only):

- code-review-01: The code has no duplicate-role check, so calling it twice appends `"member"` twice.
- code-review-01: The suggested fix copies the incoming roles with `list(roles)` and appends `"member"` only if it is not already present.
- code-review-01: The suggested fix catches `Exception` and calls `logger.exception` before returning `False`.
- code-review-02: The function returns a string but never resolves it correctly.
- code-review-02: The corrected implementation throws an `Error` including the user ID and `res.status` when `res.ok` is false.
- code-review-03: The unhandled exception propagates without added context.
- code-review-03: The function has no type hints.
- code-review-03: Adding the type hints `customer_name: str, status: str` would make the function's contract clear.
- code-review-03: Type hints would let static analysis tools catch misuse.
- code-review-04: In CPython, that read/write race is not a correctness bug because of the GIL.
- code-review-04: Relying on the GIL for that safety is undefined behavior.
- code-review-05: If no `.log` files match, the loop body runs once on the literal string `*.log`.
- code-review-05: In that case `gzip` fails because the file does not exist.
- code-review-05: The suggested rewrite uses `rm -f -- *.tmp 2>/dev/null || true`.
- code-review-06: Deleting a key by setting it to `None` only works if the key already exists in `merged` at that level.
- code-review-06: `merge_settings({}, {"a": {"b": None}})` deletes nothing and instead sets `merged["a"] = {"b": None}`, storing `None` as a real value.
- code-review-06: Top-level deletion and nested deletion behave differently for the same intent.
- code-review-06: Using `None` as a delete sentinel is common in config-merge utilities such as Ansible and Django settings overlays.
- code-review-06: Some merge utilities expect list-append semantics.
- code-review-06: The `None`-deletes-key behavior is the most important and least discoverable behavior in the function.
- code-review-06: The `None`-deletion and type-mismatch-overwrite behaviors are almost certainly load-bearing somewhere in the codebase.
- code-review-07: Callers cannot distinguish a successful result of `undefined` from exhausted retries.
- code-review-07: Returning `null` for unrelated errors is error hiding rather than error handling.
- code-review-07: If `err` is `null`, accessing `err.status` throws inside the `catch` block.
- code-review-07: An exception thrown inside the `catch` block is not caught anywhere in the function.
- code-review-07: That uncaught exception propagates out of the function unpredictably.
- code-review-07: Most libraries use the name "backoff" for an exponential pattern.
- code-review-07: Without a cap, large `attempts` values can stall for a long time.
- code-review-07: On the final 429, the function sleeps `1000 * (attempts-1)` ms before exiting the loop and returning `undefined`.
- code-review-07: The sleep on the last attempt is wasted latency.
- code-review-07: There is no documentation of what each return shape means.
- code-review-07: The wasted final-attempt sleep is likely a bug.
- code-review-07: Unknown callers may already depend on the `null`/`undefined` distinction.
- code-review-07: Actual call sites should be confirmed before changing the return contract.
- code-review-07: The crash on non-object throws is safe to fix regardless of callers.
- code-review-07: The 5xx-with-no-backoff issue is safe to fix regardless of callers.
- code-review-08: `os.remove` raises `IsADirectoryError` when called on a directory.
- code-review-08: The script crashes on subdirectories inside `ROOT`.
- code-review-08: `os.path.getmtime` works on directories without error.
- code-review-08: The subdirectory crash only occurs when a directory also passes the age check, making the failure intermittent and unpredictable.
- code-review-08: The `tmp-`/`.part` branch deletes files with no age check.
- code-review-08: The `tmp-`/`.part` branch can delete a file that an export job is currently mid-write to, such as `tmp-12345`.
- code-review-08: The unconditional `tmp-`/`.part` deletion is the most dangerous bug in the script.
- code-review-08: The `elif` branch includes an age gate, showing the author considered not touching fresh files in that case.
- code-review-08: The script has no exception handling anywhere.
- code-review-08: `os.path.getmtime` and `os.remove` can raise `FileNotFoundError` if a file is removed by another process between the `listdir` call and the call.
- code-review-08: `os.path.getmtime` and `os.remove` can raise `PermissionError`.
- code-review-08: One bad file aborts the entire run.
- code-review-08: Work completed before an aborting error is silently lost because there is no partial-progress log.
- code-review-08: The script does not check that `ROOT` exists.
- code-review-08: If the export mount is not attached, `/var/data/exports` may still exist as an empty or stale local directory.
- code-review-08: If the mount is missing, the script will not error and will quietly operate on the wrong filesystem.
- code-review-08: The `removed < 500` cap throttles age-based deletions but not `tmp-`/`.part` deletions.
- code-review-08: Total deletions per run are effectively unbounded.
- code-review-08: `os.listdir` returns entries in filesystem-dependent order, not sorted by mtime.
- code-review-08: The 500-file cap does not delete oldest files first; which 500 files get deleted is arbitrary.
- code-review-08: `CUTOFF` is computed at import time rather than per call.
- code-review-08: If the module is imported once into a long-running scheduler process, `CUTOFF` never advances and the 45-day window becomes a fixed date.
- code-review-08: The script does not log what was deleted.
- code-review-08: `removed` is returned but no filenames, counts, or errors are written anywhere.
- code-review-08: The script permanently deletes production export data with no audit trail.
- code-review-08: `86400 * 45` represents a 45-day retention window.
- code-review-08: The 45-day retention window looks deliberate and is a plausible business retention window.
- code-review-08: The intent of the `removed < 500` cap (bounding blast radius per run) looks deliberate.
- code-review-08: The implementation of the `removed < 500` cap looks like an oversight because it covers only one branch and has no ordering.
- code-review-08: Unconditional deletion of `tmp-`/`.part` files looks accidental and is inconsistent with the caution shown in the other branch.
- code-review-08: The two most urgent fixes are adding an age threshold to the `tmp-`/`.part` branch and wrapping each deletion in a `try`/`except`.
- code-review-08: The remaining issues are design and observability gaps that will not cause an outage by themselves.
- debugging-02: Because `this` is not the instance, `this.seconds` evaluates to `undefined`.
- debugging-04: Detecting the encoding is preferable to assuming UTF-8 when the encoding is unknown or mixed.
- debugging-05: In the fixed code, DEFAULT_TAGS is ["draft"].
- debugging-05: When tags is None, the fixed code assigns tags = list(DEFAULT_TAGS), a copy of DEFAULT_TAGS.
- debugging-06: The failures are not caused by a code bug in the export job.
- debugging-06: The nightly analytics query involves aggregation and a full scan.
- debugging-06: A connection leak can occur when a code path fails to release a connection on error or retry.
- debugging-06: If the sum of both services' pool max_size exceeds the database's max_connections, connection exhaustion is structural rather than incidental.
- debugging-06: The fix is either isolating pools with dedicated connections per service or fixing the connection leak.
- debugging-07: The pytest flag `-p no:randomly` (or equivalent) can be used to run the suite serially in CI.
- debugging-07: `pytest tests/test_notifications.py -n 4 --count=50` repeatedly runs a test file under parallelism.
- debugging-07: The `--count` option requires the `pytest-repeat` plugin.
- debugging-07: Inserting a poll/retry with a short timeout before asserting on the digest is a diagnostic technique.
- debugging-07: If retrying makes the flake vanish, the cause is a race rather than a logic bug.
- debugging-07: `-v --tb=long` produces verbose pytest output with long tracebacks.
- debugging-07: `pytest --capture=no` or a custom `pytest_runtest_makereport` hook can be used to dump the digest response body and event IDs on assertion failure.
- debugging-07: `.delay()`, `asyncio.create_task`, message-queue publishes, and `after_commit` hooks are signs of async dispatch in seeding code.
- debugging-07: Grepping the seeding code for async dispatch is the fastest way to confirm whether the write path is synchronous.
- debugging-07: Reproducing the failure under controlled parallelism is cheap and will indicate within an hour whether the problem is a race or a shared-fixture bug.
- debugging-08: The canary instance proves a traffic-independent leak exists.
- debugging-08: A background job unrelated to webhooks can accumulate state on each tick.
- debugging-08: Cron jobs, health checks, metrics scrapes, and connection-pool churn are examples of background jobs that can accumulate state.
- debugging-08: If silencing the canary's own background jobs stops memory growth, those jobs are the cause.
- debugging-08: A growing thread or goroutine count over time can be observed via jstack or a goroutine/thread list dump.
- debugging-08: Diffing two heap snapshots taken hours apart with no requests in between can reveal a traffic-independent leak.
- debugging-08: Event listeners, retry queues, dead-letter arrays, and promises/closures appended to a global structure on each request and never trimmed are examples of unreleased per-webhook allocations.
- debugging-08: Per-instance memory growth can be correlated against request-count metrics.
- debugging-08: Firing a synthetic burst of webhook traffic at a test instance and diffing the heap before and after can identify the traffic-driven leak.
- debugging-08: If product payloads have grown over the year, retained memory grows even with a stable cache entry count.
- debugging-08: A flat entry count combined with a near-zero eviction rate indicates the cache bound isn't triggering.
- debugging-08: Open FD/socket counts on the canary can be compared against a normal instance.
- debugging-08: The biggest gap is that the diagnosis is being done blind without a heap profile.
- debugging-08: A heap profile should be obtained before the next scheduled restart.
- debugging-08: pprof, jemalloc, and a heap dump on SIGQUIT are cheap sampling heap-profile options.
- debugging-08: A heap profile artifact will likely identify the cause in minutes instead of days of correlation.
- explanation-01: In open addressing, clustering can hurt performance if the probing scheme is weak.
- explanation-02: Optimistic locking suits workloads where users edit different records most of the time, such as editing a document or updating a cart.
- explanation-03: Dropped packets cause wasted retransmissions and congestion collapse.
- explanation-03: Congestion collapse nearly broke the early internet in 1986.
- explanation-03: Every packet in a window generates an ACK.
- explanation-03: On loss, TCP cuts ssthresh, typically to half the current cwnd, and backs off.
- explanation-03: The exact behavior on loss depends on the congestion control algorithm.
- explanation-03: Reno, CUBIC, and BBR are congestion control algorithms.
- explanation-04: Threads in the same process run independently.
- explanation-04: Python and Ruby are languages with a global interpreter lock.
- explanation-04: Browsers sandbox tabs in separate processes for security isolation.
- explanation-04: Processes are preferable when true CPU parallelism is needed outside a GIL-bound language.
- explanation-05: A cache keyed by request ID that is never evicted is an example of a collection that accumulates entries without removal.
- explanation-07: CPU, IOPS, and connection limits bottleneck before disk size does.
- explanation-07: The loss of cross-shard transactional guarantees causes problems that surface months later.
- explanation-07: Migrating to sharding under load is harder than building sharded from day one.
- explanation-08: If serialization is 2% of request time, a binary format that is 5x faster saves only 1.6% end to end.
- explanation-08: A 1.6% end-to-end saving would be swamped by network and database time.
- explanation-08: If serialization is 40% of request time, the payoff from a binary format is real.
- explanation-08: The fraction of request latency spent in JSON encode/decode can be measured with a flame graph or timers around the calls.
- explanation-08: Different serialization formats optimize different things.
- explanation-08: Protobuf optimizes both CPU and payload size.
- explanation-08: msgpack mostly optimizes CPU and yields modest size gains.
- explanation-08: Benchmarking a candidate format against real payloads yields an expected speedup.
- explanation-08: The costs of adopting a binary format include schema management, client-side tooling, debuggability, and migration effort across all clients.
- summarization-01: Cold start is about 40% quicker.
- summarization-02: Errors began at 09:14.
- summarization-02: Current alerting covers downstream error rate but not connection pool saturation.
- summarization-04: PDF export fails silently on the Reports page.
- summarization-04: The issue was reproduced by two different users.
- summarization-06: The restart's success is consistent with several possible causes.
- summarization-07: A staging test of the new batcher ran for six hours.
- summarization-07: The staging test shows the new batcher cuts median latency by 18%.
- summarization-07: Apart from the median latency result, the other findings are guesses rather than established facts.
- summarization-07: The p99 latency gains appear to be real.
- summarization-07: The p99 gains likely overstate the impact that would be seen in production.
- summarization-07: Staging traffic is smoother than production traffic.
- summarization-07: Per-worker memory usage grew by 60 MB.
- summarization-07: The 60 MB per-worker memory growth is presumed to come from the larger buffer pool.
- summarization-07: The memory growth has not been profiled.
- summarization-07: A single worker crashed during the test.
- summarization-07: The worker crash could be caused by staging's newer kernel.
- summarization-07: The worker crash could be caused by an undiscovered bug in the batcher.
- summarization-07: Staging runs a newer kernel than production.
- summarization-07: The recommendation is to confirm the p99 results on production-like traffic before rollout.
- summarization-07: The recommendation is to profile memory usage before rollout.

### developer-docs

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 28 | 26 | 0.929 | 23 | 3 |
| code-review-02 | 20 | 0 | 0.0 | 4 | 4 |
| code-review-03 | 25 | 15 | 0.6 | 27 | 7 |
| code-review-04 | 27 | 18 | 0.667 | 17 | 3 |
| code-review-05 | 29 | 26 | 0.897 | 27 | 4 |
| code-review-06 | 31 | 23 | 0.742 | 29 | 12 |
| code-review-07 | 44 | 34 | 0.773 | 37 | 8 |
| code-review-08 | 4 | 0 | 0.0 | 33 | 33 |
| debugging-01 | 9 | 9 | 1.0 | 9 | 0 |
| debugging-02 | 15 | 9 | 0.6 | 10 | 1 |
| debugging-03 | 11 | 11 | 1.0 | 9 | 0 |
| debugging-04 | 17 | 9 | 0.529 | 15 | 5 |
| debugging-05 | 20 | 18 | 0.9 | 14 | 2 |
| debugging-06 | 30 | 0 | 0.0 | 5 | 5 |
| debugging-07 | 21 | 9 | 0.429 | 33 | 11 |
| debugging-08 | 46 | 10 | 0.217 | 33 | 20 |
| explanation-01 | 37 | 26 | 0.703 | 25 | 1 |
| explanation-02 | 26 | 18 | 0.692 | 23 | 3 |
| explanation-03 | 41 | 25 | 0.61 | 22 | 5 |
| explanation-04 | 41 | 38 | 0.927 | 35 | 5 |
| explanation-05 | 17 | 10 | 0.588 | 12 | 0 |
| explanation-06 | 26 | 19 | 0.731 | 29 | 7 |
| explanation-07 | 33 | 19 | 0.576 | 29 | 8 |
| explanation-08 | 10 | 8 | 0.8 | 18 | 9 |
| summarization-01 | 8 | 5 | 0.625 | 6 | 0 |
| summarization-02 | 15 | 10 | 0.667 | 10 | 2 |
| summarization-03 | 15 | 0 | 0.0 | 4 | 4 |
| summarization-04 | 15 | 13 | 0.867 | 14 | 3 |
| summarization-05 | 8 | 6 | 0.75 | 15 | 2 |
| summarization-06 | 13 | 12 | 0.923 | 12 | 0 |
| summarization-07 | 3 | 0 | 0.0 | 13 | 13 |
| summarization-08 | 18 | 17 | 0.944 | 18 | 3 |

Median fraction: 0.679 over 32 scored pairs.

Median additions: 4.0 over 32 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python footgun.
- code-review-01: Nothing prevents duplicate users or empty names.
- code-review-02: The function's `fetch(...).then(...)` call starts an async operation that is not awaited.
- code-review-02: The `return profile.name.toUpperCase()` line executes immediately, before the promise resolves.
- code-review-02: At the time `return profile.name.toUpperCase()` runs, `profile` is still `undefined`.
- code-review-02: Accessing `profile.name` when `profile` is `undefined` throws a `TypeError`.
- code-review-02: The error thrown is `Cannot read properties of undefined (reading 'name')`.
- code-review-02: The function is marked `async` but never uses `await`.
- code-review-02: Because the function never uses `await`, the `async` keyword gains none of its benefits.
- code-review-02: The function returns a promise that resolves to a crash rather than to a value.
- code-review-02: The function has no `.catch()` or `try/catch` error handling.
- code-review-02: The function lacks error handling for network failures.
- code-review-02: The function lacks error handling for non-OK HTTP statuses such as 404 or 500.
- code-review-02: `fetch` does not reject on HTTP error statuses.
- code-review-02: Because `fetch` does not reject on HTTP error statuses, a failed request would still try to parse JSON.
- code-review-02: The function lacks error handling for malformed JSON.
- code-review-02: The function does not validate the shape of the response.
- code-review-02: The function assumes `data` always has a `.name` property.
- code-review-02: If the API returns an error object or something unexpected, the function fails silently or throws later.
- code-review-02: The fixed version awaits `fetch(`/api/users/${userId}`)` and assigns the result to `res`.
- code-review-02: The fixed version throws an `Error` with the message `Failed to load profile: ${res.status}` when `res.ok` is false.
- code-review-02: The fixed version awaits `res.json()` and returns `data.name.toUpperCase()`.
- code-review-03: Memory was checked for relevant context before the review was written.
- code-review-03: No relevant context was found stored in memory.
- code-review-03: SQL injection is the OWASP #1 issue.
- code-review-03: sqlite3 uses `?` placeholders instead of `%s`.
- code-review-03: The caller cannot distinguish a failed call from one that returned no rows.
- code-review-03: Whether error handling is needed depends on how the caller handles the result.
- code-review-03: Returning raw rows ties callers to the DB driver's row representation rather than a defined interface such as a dict or dataclass.
- code-review-03: The return-type coupling issue is minor and depends on codebase conventions.
- code-review-03: The SQL injection is the only issue that must be fixed regardless of context.
- code-review-03: The remaining issues are stylistic or robustness judgments that depend on the codebase's conventions.
- code-review-04: Preemption between read and write can happen mid-bytecode because of the GIL's bytecode-boundary switching.
- code-review-04: The unsynchronized read-modify-write is guaranteed unsafe on non-CPython implementations.
- code-review-04: The operation would also be unsafe if `value` involved a `+=` on a non-atomic object.
- code-review-04: Two threads can both read `current = 5` and then both write `6`, losing one increment.
- code-review-04: Depending on timing, the counter could end up as either `0` or `1` after a concurrent reset and increment.
- code-review-04: The outcome of a concurrent reset and increment is not documented.
- code-review-04: The class is documented by its usage as multi-threaded, but nothing in the implementation enforces thread safety.
- code-review-04: Torn reads are not a real risk for a Python `int` reference itself.
- code-review-04: The counter's value can be arbitrarily stale relative to other threads' operations, giving no ordering guarantees.
- code-review-05: A listing of the memory directory was run and no relevant memory was found.
- code-review-05: The loop doing nothing when no `.log` files exist is accidental rather than by design.
- code-review-05: The final "Cleaned" message is misleading because it implies success regardless of the actual outcome.
- code-review-06: If `base` is not dict-like, `dict(base)` raises a confusing `TypeError` or `ValueError`.
- code-review-06: Deeply nested dicts will exceed the recursion limit.
- code-review-06: The `is None` check avoids treating `0`, `""`, `False`, and `[]` as unset.
- code-review-06: If `merged[key]` is a dict and the override value is not (or vice versa), no error is raised.
- code-review-06: On a type mismatch, the override value replaces the entire subtree.
- code-review-06: A typo'd override, such as a string where a nested settings block was expected, silently removes an entire section rather than failing loudly.
- code-review-06: Merging lists is ambiguous regarding whether to append, replace, or dedupe.
- code-review-06: Accepting new keys means typo'd keys are silently accepted as new settings instead of raising an error.
- code-review-07: Some old codebases use a 'never throw' contract so callers don't need try/catch.
- code-review-07: The user said callers exist that they cannot see.
- code-review-07: Network failures and timeouts are exactly the transient errors that retry logic usually exists for.
- code-review-07: `1000 * (i + 1)` was probably the intended delay formula if backoff before every retry was intended.
- code-review-07: The default value of `attempts` is 3.
- code-review-07: The user said they cannot verify whether callers passing unbound methods exist.
- code-review-07: Retrying 429 with backoff, retrying 5xx, and not retrying other errors is likely a deliberate policy choice.
- code-review-07: Swallowing terminal errors as null instead of throwing is likely a deliberate fail-soft contract.
- code-review-07: The recommended first fix is making the return contract consistent, by either always throwing on unrecoverable failure or always returning null for every failure path including exhausted retries.
- code-review-07: The helper makes 3 attempts by default.
- code-review-08: The speaker will check memory for relevant context before proceeding.
- code-review-08: The memory may contain context on the project.
- code-review-08: The memory may contain context on the user's review preferences.
- code-review-08: A Read action was performed.
- debugging-02: In strict mode and in modules, `this` in such a callback is undefined.
- debugging-02: Class bodies are implicitly strict mode.
- debugging-02: Because class bodies are strict, `this` in the callback is undefined.
- debugging-02: Accessing `this.seconds` when `this` is undefined throws a TypeError: Cannot read properties of undefined.
- debugging-02: Seeing NaN instead indicates the function ran in a non-strict context where `this` resolved to the global object.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-04: The byte 0xc3 starts a multi-byte UTF-8 sequence.
- debugging-04: Characters such as é and ñ are encoded by multi-byte UTF-8 sequences beginning with 0xc3.
- debugging-04: The code forces encoding="ascii".
- debugging-04: Passing errors="ignore" with encoding="utf-8" tolerates bad bytes.
- debugging-04: Opening a file in binary mode with open(path, "rb") allows counting lines regardless of encoding.
- debugging-04: Binary mode avoids decoding the file entirely.
- debugging-04: Iterating a binary-mode file counts \n-delimited chunks.
- debugging-04: Binary mode is the safest option when the file's encoding is unknown or mixed.
- debugging-05: The fixed function uses `tags = tags + ["post"]`, which creates a new list.
- debugging-05: Calling `tags.append("post")` on the newly created list is an equivalent alternative.
- debugging-06: The described failure is a classic connection-pool exhaustion pattern.
- debugging-06: A shared-resource suspect (the analytics service) was already named in the user's setup.
- debugging-06: Contention with the analytics service is the most plausible cause of the failures.
- debugging-06: The analytics service may run its own scheduled jobs such as rollups, refreshes, or backups.
- debugging-06: If an analytics job overlaps the export window, it can hold connections or locks long enough to starve the shared connection pool.
- debugging-06: The failure does not always occur on the same batch number.
- debugging-06: The failure occurs about once a week.
- debugging-06: A non-fixed batch number and a weekly cadence fit a timing coincidence better than a data-dependent bug.
- debugging-06: A specific bad row would reliably cause failure on the same batch every time.
- debugging-06: Long-running or lock-blocked queries on the shared database can hold connections open far longer than usual.
- debugging-06: Holding connections open too long is a more likely cause than the pool simply being undersized.
- debugging-06: A connection leak in the export job or the analytics service could slowly consume pool capacity over a run.
- debugging-06: A connection leak would explain intermittent failures that appear only after enough connections leak during a long or heavy night.
- debugging-06: A connection leak does not explain the weekly periodicity as cleanly as analytics-job contention does.
- debugging-06: Database-side degradation from autovacuum, backups, a maintenance window, or a shared DB connection limit can increase per-query latency.
- debugging-06: Increased per-query latency can cause connections to be held longer than the 30-second timeout budget allows.
- debugging-06: The job has a 30-second timeout budget.
- debugging-06: The current setup only shows the timeout symptom and gives no visibility into pool state.
- debugging-06: There is currently no way to tell whether the pool drained slowly or spiked suddenly.
- debugging-06: Correlating the analytics service's schedule with failures is the highest-value check given the existing suspicion of resource sharing.
- debugging-06: The failure occurred at 02:14.
- debugging-06: pg_stat_activity is a source of DB-side state showing long-running queries, locks, and connection counts.
- debugging-06: The problem cannot be reproduced on demand.
- debugging-06: The application logs are rotated, so log data from failures is lost.
- debugging-06: The available log data from the failure was only a fragment.
- debugging-06: The pool topology may be either one pool per worker or one pool shared across all workers.
- debugging-06: If pools are per-worker, worker-3 being singled out could indicate uneven batch distribution rather than global pool exhaustion.
- debugging-06: worker-3 was the worker singled out in the failure.
- debugging-06: The DB-side snapshot and the analytics-schedule correlation are the cheapest diagnostics to set up.
- debugging-06: Those two checks are the most likely to confirm or rule out the overlapping-analytics-job theory.
- debugging-07: Two families of cause fit the signature of a parallelism-only flake: a real race in the application and a test isolation problem in xdist workers.
- debugging-07: Under CI CPU and IO contention from four workers competing for cores, processing of the third event can lag past the fixed wait the test uses before requesting the digest.
- debugging-07: Examples of shared state include the same digest bucket, the same default user, and the same 'latest N events' query with no test-specific filter.
- debugging-07: Event ID generation that is not collision-safe under concurrent creation, such as timestamp-based IDs with coarse resolution, could cause two events to collide and overwrite each other, silently dropping one.
- debugging-07: Adding a failure-only diagnostic recording worker id, event IDs and timestamps as created, and the raw digest response, and uploading it as a CI artifact even for transient failures, is the highest-leverage first step.
- debugging-07: Without such diagnostics the debugging is being done blind.
- debugging-07: Running `pytest -n 4` repeatedly, in a loop or with pytest-repeat, should surface a ~10% failure rate within a few dozen runs.
- debugging-07: If workers share one database, that is likely the culprit and is usually the cheaper fix.
- debugging-07: Logging server-side when each event is created and when the digest is computed, including windowing boundaries, would show on the next failure whether the third event was never created, created but excluded by a time window, or created and then overwritten.
- debugging-07: Artificially adding latency to event creation or oversubscribing workers (for example `-n 8` on a 4-core box) increases contention and can reproduce the failure faster.
- debugging-07: If the failure rate climbs with more contention, that strongly confirms a race rather than isolation bleed.
- debugging-07: Knowing whether event creation is synchronous (the API call blocks until the event is queryable) or how the digest selects events (time window versus 'last N') would allow narrowing the diagnosis further.
- debugging-08: The service's memory grows about 2% per day.
- debugging-08: Growth that is worse during campaigns indicates growth tracks distinct new data (new SKUs, promo codes, campaign IDs) rather than raw request count.
- debugging-08: Memory never drops overnight.
- debugging-08: Memory that never drops overnight rules out GC backlog or a young-generation effect that a quiet period would let the collector clean up.
- debugging-08: Memory that never drops overnight means the growing data is either still reachable (a real leak) or is native/off-heap fragmentation that GC cannot touch.
- debugging-08: The most plausible cause is cache eviction that does not actually free memory.
- debugging-08: Entries can be evicted from a cache map, keeping the count bounded, while the evicted objects remain referenced elsewhere.
- debugging-08: Lingering references to evicted objects can come from a removal listener that registers something globally, a subscriber list, or a callback captured in a closure.
- debugging-08: Keys with broken equals/hashCode can make a cache believe it evicted something it did not evict.
- debugging-08: Baseline traffic alone churns the cache and leaks a small amount of memory.
- debugging-08: Campaigns push more distinct product and promo keys through the cache, causing more churn and more leaked evictions.
- debugging-08: Leaked objects that are strongly reachable cannot be reclaimed by GC overnight.
- debugging-08: Logging cache size, hit rate, and eviction count over a day can confirm whether entry count stays flat while memory grows.
- debugging-08: `jmap -histo` produces a class histogram that can be taken at two points in a day and diffed.
- debugging-08: If a cached value's class count matches the cache bound while memory keeps climbing, a wrapper or listener object may be growing instead.
- debugging-08: Grepping for `removalListener` or `onEvict`-style hooks can reveal listeners that do not detach fully.
- debugging-08: The second most plausible cause is unbounded metric or log label cardinality.
- debugging-08: Emitting metrics or logs with dynamic labels such as product ID, promo code, or campaign ID creates new time series for every new campaign.
- debugging-08: New time series created by dynamic labels live forever in the metrics client's registry.
- debugging-08: Unbounded label cardinality matches the campaign correlation, the baseline-only canary growth, and the lack of overnight recovery.
- debugging-08: Normal traffic still creates some new metric labels, just fewer than campaign traffic.
- debugging-08: Metrics registries are maps that are never cleared.
- debugging-08: Most metrics client libraries expose a count of registry size.
- debugging-08: The third most plausible cause is a webhook-specific registration leak.
- debugging-08: Grepping for global Map/Set/List structures written to inside webhook handlers can reveal a registration leak.
- debugging-08: Sizes of suspect global structures can be compared between canary and prod via a debug endpoint or periodic size logging.
- debugging-08: The fourth plausible cause is native/off-heap growth from connections, buffers, or fragmentation.
- debugging-08: If the measured memory is RSS rather than a managed heap, growing connection pools, unreturned buffers, or allocator fragmentation from webhook HTTP calls would produce identical symptoms.
- debugging-08: Native/off-heap growth can coexist with the cache, metrics, and webhook registration causes.
- debugging-08: Open file descriptor and socket counts can be tracked with `lsof` and `ss`.
- debugging-08: A steady climb in file descriptor or socket count points to native growth.
- debugging-08: Comparing canary and prod class/object histograms at the start and end of a campaign day is the cheapest way to identify which structure is growing without a full profile.
- debugging-08: Cache stats and metrics-registry size can be logged on an interval and overlaid against the memory curve.
- debugging-08: Thread count and FD/socket count should be tracked over the day, especially on the webhook-heavy instance.
- debugging-08: Once a candidate class is identified, the code can be grepped for all places holding a reference to it outside the known cache or collection.
- debugging-08: This investigation approach requires no profiler.
- explanation-01: The internal array of a hash map is called the bucket array.
- explanation-01: The bucket array is finite while the set of possible keys is in theory infinite.
- explanation-01: Collisions are unavoidable in a hash map.
- explanation-01: In chaining, large buckets may use a tree instead of a list.
- explanation-01: Java's HashMap uses chaining by default.
- explanation-01: Most textbook hash map implementations use chaining by default.
- explanation-01: Quadratic probing and double hashing give better spread than linear probing.
- explanation-01: Python's dict uses open addressing.
- explanation-01: Chaining is simpler to reason about and tolerates a high load factor.
- explanation-01: Open addressing typically requires keeping the load factor under about 70%.
- explanation-01: A good hash function that spreads keys evenly is what keeps collisions rare.
- explanation-02: An optimistic locking example uses a `products` table with a `version` column.
- explanation-02: In the example, a row is read with `version = 5`, edited in memory, then updated with `UPDATE products SET price = 19.99, version = 6 WHERE id = 42 AND version = 5;`.
- explanation-02: REST APIs editing independent records are an example use case for optimistic locking.
- explanation-02: A pessimistic locking example uses `BEGIN;`, `SELECT * FROM products WHERE id = 42 FOR UPDATE;`, `UPDATE products SET price = 19.99 WHERE id = 42;`, and `COMMIT;`.
- explanation-02: Other transactions trying to run `SELECT ... FOR UPDATE` on id=42 block at that statement.
- explanation-02: Inventory decrements at checkout are an example use case for pessimistic locking.
- explanation-02: Generating sequential invoice numbers is an example use case for pessimistic locking.
- explanation-02: The recommended default is to use optimistic locking.
- explanation-03: Packet loss from overflowing router buffers harms all users on that network path.
- explanation-03: A sender that is too conservative wastes available bandwidth.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The receiver's advertised window reflects the receiver's buffer space.
- explanation-03: Historically, the initial cwnd was 1 segment.
- explanation-03: The initial cwnd is now typically around 10 segments.
- explanation-03: RFC 6928 specifies the initial congestion window of about 10 segments.
- explanation-03: An example cwnd progression during slow start is 10 → 20 → 40 → 80.
- explanation-03: Slow start is called 'slow' relative to immediately sending as much data as the receiver's window allows.
- explanation-03: Earlier TCP implementations immediately sent as much data as the receiver's window allowed.
- explanation-03: Congestion collapse became a real problem in the mid-1980s.
- explanation-03: Linear growth from 1 segment would take far too long to reach useful throughput on high-bandwidth paths.
- explanation-03: After slow start, TCP hands off to steadier mechanisms including congestion avoidance and loss/ECN-triggered backoff.
- explanation-03: Those steadier mechanisms fine-tune around the capacity estimate for the rest of the connection's life.
- explanation-03: Slow start recurs after a connection has been idle.
- explanation-03: Slow start recurs in those cases because the old cwnd value may no longer reflect current network conditions.
- explanation-04: Supervisors like systemd favor a process-per-task model.
- explanation-04: Erlang's OTP favors a process-per-task model.
- explanation-04: Processes can run under different users.
- explanation-05: Examples of long-lived objects include a global event bus, a DOM node, and a singleton.
- explanation-05: A long-lived object keeps a reference to a registered callback and to everything that callback closes over.
- explanation-05: An unregistered callback and its captured state stay reachable forever.
- explanation-05: Closures capturing more than they need are a frequent cause of memory leaks.
- explanation-05: Static or global collections accumulating objects are a frequent cause of memory leaks.
- explanation-05: Detached-but-referenced resources are a frequent cause of memory leaks.
- explanation-05: A removed DOM node that is still referenced by JavaScript code is an example of a detached-but-referenced resource.
- explanation-06: A cache in front of the database does not help when slowness comes from N+1 queries.
- explanation-06: A cache in front of the database does not help when slowness comes from missing indexes.
- explanation-06: A cache in front of the database does not help when slowness comes from slow serialization.
- explanation-06: A product page fetched thousands of times is an example of a repeat-query workload that benefits from caching.
- explanation-06: Checking the slow query log and running EXPLAIN on the heaviest queries is a recommended diagnostic step.
- explanation-06: The fix for slow queries is often an index rather than a cache.
- explanation-06: Redis is an example of a cache.
- explanation-07: 200 GB of data growing at 10% per year is a non-event.
- explanation-07: 200 GB of data doubling every quarter is a materially different situation from slow growth.
- explanation-07: If a product team cannot estimate its data growth rate, that usually means the product isn't proven yet.
- explanation-07: An unproven product is a strong argument against sharding.
- explanation-07: Sharding does nothing to fix slow queries.
- explanation-07: Sharding does nothing to fix missing indexes.
- explanation-07: Sharding does nothing to fix bad connection pooling.
- explanation-07: Sharding does nothing to fix read-heavy load.
- explanation-07: Modern hardware can handle multi-terabyte Postgres instances with proper indexing, partitioning, and tuning.
- explanation-07: A 200 GB deployment likely has 5-10x headroom before vertical scaling plus read replicas stop working.
- explanation-07: Sharding requires a shard key that distributes data evenly.
- explanation-07: Migrating under pressure is riskier but still doable.
- explanation-07: A later scaling path is to partition, add replicas, and then shard only if truly needed.
- explanation-07: The recommended course is to stay single-instance, invest in indexing and query optimization, use partitioning for large tables, and add read replicas as read load grows.
- explanation-08: Serialization is usually a small slice of total request time.
- explanation-08: Network I/O, database queries, and business logic often dominate total request time.
- summarization-01: Internal-only changes were omitted from the release notes.
- summarization-01: The omitted internal changes include build tooling, a module refactor, and the telemetry interval.
- summarization-01: The omitted internal changes do not affect user-facing behavior.
- summarization-02: The config review checklist likely does not cover other performance-critical settings.
- summarization-02: The team was paged at 09:21.
- summarization-02: The issue was resolved by 09:48.
- summarization-02: Detection-to-mitigation took approximately 34 minutes.
- summarization-02: The detection-to-mitigation response was reactive rather than preventive.
- summarization-03: The proposal moves thumbnail generation off the critical upload path.
- summarization-03: The proposal moves thumbnail generation into an asynchronous background queue.
- summarization-03: Synchronous thumbnail generation currently adds 800ms to 3s per upload.
- summarization-03: Synchronous thumbnail generation consumes web worker capacity.
- summarization-03: Under the proposal, uploads would store the original image.
- summarization-03: Under the proposal, uploads would enqueue a job.
- summarization-03: Under the proposal, uploads would return a placeholder URL immediately.
- summarization-03: A new worker pool would process thumbnails.
- summarization-03: The new worker pool would update records once thumbnails are ready.
- summarization-03: Implementation requires a new queue topic.
- summarization-03: Implementation requires a worker deployment.
- summarization-03: Implementation requires a placeholder asset.
- summarization-03: The main tradeoff is a visible delay before real thumbnails appear during high load.
- summarization-03: The team plans to address the delay with queue autoscaling.
- summarization-03: The estimated effort is two weeks for one engineer.
- summarization-04: One error banner appears per click of the PDF export button.
- summarization-04: The bug was reproduced on two different machines.
- summarization-05: Ada is to check with the mobile team's lead to confirm the mobile team has been informed of the API deprecation.
- summarization-05: There is an API deprecation that the mobile team needs to be informed about.
- summarization-06: Connection-pool exhaustion and a retry storm are the leading but unconfirmed hypotheses for the root cause.
- summarization-07: The speaker is checking memory for relevant context.
- summarization-07: The check is being done before writing a summary.
- summarization-07: A summary is going to be written.
- summarization-08: The progress bar finding is rated Firm for the abandonment behavior and Tentative for the cause.

Added facts (styled only):

- code-review-01: The recommended fix is to catch a specific exception, such as the database driver's exception type, and log or re-raise it
- code-review-01: The corrected version raises `ValueError("name is required")` when `name` is falsy
- code-review-01: The corrected version appends `"member"` only if it is not already present in the roles list
- code-review-02: The speaker intends to check memory for relevant preferences before doing anything else.
- code-review-02: A file exists at /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-sshypran/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-taprfbjr/memory/MEMORY.md
- code-review-02: The memory directory for the project is located at /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-sshypran/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-taprfbjr/memory/
- code-review-02: The file MEMORY.md is the item to be read.
- code-review-03: %s, ?, and :name are placeholder syntaxes used by database drivers.
- code-review-03: The function has no type hints.
- code-review-03: Type hints document the expected input and return types.
- code-review-03: Type hints let static analysis catch type mismatches.
- code-review-03: The function has no docstring.
- code-review-03: A one-line docstring would clarify what the function returns.
- code-review-03: A one-line docstring would clarify how status is expected to be matched.
- code-review-04: Because there is no accessor method, callers must access `self.value` directly.
- code-review-04: Accessing `self.value` directly bypasses any protection later added to the class.
- code-review-04: A leading underscore on `_value` signals that callers should go through the methods instead of touching the attribute directly.
- code-review-05: The script has several bugs, most of them dangerous.
- code-review-05: If `BACKUP_DIR` does not exist or `$1` is missing, `cd` fails but the script continues.
- code-review-05: If the `ls` error text gets mixed into stdout by a shell quirk, the loop processes garbage.
- code-review-05: Placing `--` before the glob and filenames prevents a filename like `-rf` from being interpreted as an option.
- code-review-06: The function never checks whether the override value is a dict.
- code-review-06: If `base[key]` is a dict and `override[key]` is not, the recursive call runs `value.items()` on a non-dict and raises `AttributeError`.
- code-review-06: `merge_settings({"db": {"host": "x"}}, {"db": "disabled"})` crashes instead of replacing the value.
- code-review-06: Recursive merging of nested dicts is the stated purpose of the function.
- code-review-06: List-merging is rarely wanted by default.
- code-review-06: Key order in the result follows `base` first, then new `override` keys.
- code-review-06: The key ordering behavior is incidental rather than a deliberate decision.
- code-review-06: Key order only matters if something downstream relies on dict order, such as serialization or display.
- code-review-06: Guarding against cycles is not worth it unless configs come from untrusted input.
- code-review-06: The None-as-delete behavior and the type-mismatch crash should be resolved with whoever owns the config schema before writing tests.
- code-review-06: Those two issues determine what 'correct' means for the function.
- code-review-06: Everything else can be locked in with tests documenting current behavior.
- code-review-07: A caller checking `=== null` cannot distinguish giving up after retries from hitting a non-retryable error.
- code-review-07: Immediately retrying a struggling server defeats the purpose of the retry helper.
- code-review-07: If a caller passes a bound method such as `withRetry(obj.method)`, `this` is lost and the wrapped call breaks.
- code-review-07: The code has no idempotency check.
- code-review-07: Retrying on 429/5xx assumes `fn` is safe to call more than once.
- code-review-07: If `fn` is a `POST` or `DELETE` that partially succeeded before erroring, retrying can duplicate the side effect.
- code-review-07: The missing idempotency check is a design gap rather than a code bug.
- code-review-07: Changing the error-return behavior requires a deliberate rollout rather than a silent fix.
- code-review-08: `os.path.getmtime` and `os.remove` in the script assume every entry in `ROOT` is a file.
- code-review-08: If `ROOT` contains a directory, `os.remove` raises `IsADirectoryError`.
- code-review-08: An `IsADirectoryError` from `os.remove` stops the whole run.
- code-review-08: Between `os.listdir` and `os.remove`, another process can delete the same file.
- code-review-08: If the file is already gone, `os.remove` raises `FileNotFoundError` and stops the run.
- code-review-08: The script targets files matching `tmp-` and `.part`.
- code-review-08: `tmp-` and `.part` names suggest the files are written by an active process.
- code-review-08: The condition `removed < 500` is checked before the removal happens.
- code-review-08: Because the cap is checked before removal, the function can remove up to 501 files rather than 500.
- code-review-08: Only the age-based branch checks `removed < 500`.
- code-review-08: The 500-file cap does not apply to `tmp-`/`.part` file removals.
- code-review-08: If there are 10,000 stale `tmp-` files, the cap has no effect.
- code-review-08: The safety limit does not actually bound total deletions.
- code-review-08: The order returned by `os.listdir` is unspecified, filesystem-dependent, and not sorted.
- code-review-08: Which 500 old files are spared under the cap is arbitrary because of unspecified listing order.
- code-review-08: Two runs on the same directory could delete different files.
- code-review-08: The script has no error handling and no logging.
- code-review-08: A single unexpected file (permission error, broken symlink, or a race condition) kills the whole cleanup.
- code-review-08: On crash, the script reports nothing about what happened before the crash.
- code-review-08: The script has no dry-run mode and no audit trail.
- code-review-08: A scheduled deletion job with no logging of what it removed is hard to debug after the fact.
- code-review-08: The user did not set up the schedule and does not know its intent.
- code-review-08: The script defines `CUTOFF = 86400 * 45`, a 45-day retention period.
- code-review-08: `removed < 500` represents a 500-file cap per run.
- code-review-08: The 45-day retention and 500-file cap look like intentional policy decisions rather than accidents.
- code-review-08: There is no comment or ticket reference explaining the constants.
- code-review-08: Without documentation, it is unknown whether 45 days is a compliance/retention requirement or a guess.
- code-review-08: Without documentation, it is unknown whether 500 is a rate limit to avoid overwhelming storage I/O or an arbitrary number that worked in testing.
- code-review-08: Without documentation, it is unknown whether the missing cap on `tmp-`/`.part` removal is intentional or an oversight.
- code-review-08: The recommendation is to find out why the schedule exists and who owns it before changing behavior.
- code-review-08: The recommendation is to add per-file exception handling that skips and logs instead of crashing.
- code-review-08: The recommendation is to apply the cap uniformly across both removal branches.
- code-review-08: The recommendation is to record the reasoning for the values 45 and 500 as comments.
- debugging-02: The arrow function approach is more common than `.bind(this)` in modern JavaScript code.
- debugging-04: UTF-8 is the safest default encoding to use.
- debugging-04: UTF-8 is a superset of ASCII.
- debugging-04: UTF-8 handles most modern text files.
- debugging-04: The `errors="replace"` option substitutes undecodable bytes with a placeholder character instead of raising an exception.
- debugging-04: `errors="replace"` should only be used if byte-for-byte accuracy is not needed.
- debugging-05: In the fixed code, DEFAULT_TAGS is defined as ["draft"].
- debugging-05: In the fixed code, make_post checks if tags is None and assigns tags = list(DEFAULT_TAGS).
- debugging-06: The speaker is checking memory for relevant context on the project before answering.
- debugging-06: A memory index file named MEMORY.md is expected at /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-sshypran/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-taprfbjr/memory/MEMORY.md
- debugging-06: The command reads that MEMORY.md file with cat.
- debugging-06: The command suppresses error output by redirecting stderr to /dev/null.
- debugging-06: The command prints "no memory file" if reading the file fails.
- debugging-07: Contention for the database connection pool or a shared cache raises the odds of the read landing in the gap between write and visibility.
- debugging-07: Connection pool exhaustion or transaction isolation is a possible cause.
- debugging-07: Four workers sharing a connection pool with too few connections could mean a write's transaction hasn't committed when a different connection reads.
- debugging-07: The command `pytest tests/test_notifications.py::test_digest_contains_all_events -n 4 --count 300` runs the test 300 times with four workers.
- debugging-07: The `--count` flag requires pytest-repeat or a shell loop equivalent.
- debugging-07: Reproducing locally allows debugging without waiting on CI.
- debugging-07: The diagnostic changes can be pushed as a throwaway branch that runs the flaky test 50 times in CI.
- debugging-07: Inserting an explicit wait or poll until the event count reaches 3, with a timeout, adds a synchronization point.
- debugging-07: If the test passes reliably after adding synchronization, that confirms a race and provides a real fix.
- debugging-07: Running CI with a single worker in the same environment separates parallel test execution from environment differences as the cause.
- debugging-07: Step 1 is the fastest way to confirm or rule out worker count as the trigger.
- debugging-08: One leak is a baseline leak that runs regardless of traffic.
- debugging-08: Because the canary grows without webhook traffic, something runs independent of request volume.
- debugging-08: Possible sources of the background leak include a timer, a scheduled job, a metrics/logging buffer, a connection pool, or a periodic config/feature-flag refresh that accumulates state each cycle.
- debugging-08: Taking two heap dumps on the canary, one in the morning and one before the weekly restart, and diffing retained object counts by type can check for the background leak.
- debugging-08: The canary is restarted weekly.
- debugging-08: Because growth accelerates during campaigns, something scales with traffic volume.
- debugging-08: Request- or webhook-driven leak sources include event listeners or callbacks registered per request and never removed, promises or timers left pending, or connection/socket objects not fully released after a webhook completes.
- debugging-08: Load-testing the webhook endpoint in isolation and watching RSS can check for a request-driven leak.
- debugging-08: If RSS climbs without returning to baseline after load stops, a request-scoped leak is confirmed.
- debugging-08: Product payloads have grown over the year with more variants, images, and promo metadata added for campaigns.
- debugging-08: Spiking key cardinality churns the cache and holds more distinct large entries at once.
- debugging-08: Logging the cache's byte size over time and comparing average entry size on a campaign day versus a quiet day can check for cache entries growing in size.
- debugging-08: Writing a test that pushes past the cache bound and verifies old entries are freed confirms that eviction actually fires under load.
- debugging-08: `process.memoryUsage()` reports heap-in-use in Node.
- debugging-08: GC logs report heap-in-use in the JVM.
- debugging-08: `runtime.MemStats` reports heap-in-use in Go.
- debugging-08: If RSS keeps growing while heap-in-use stays flat, the cause is fragmentation rather than a leak.
- debugging-08: Fragmentation points toward allocator tuning rather than code changes.
- debugging-08: A heap dump diff on the canary is the fastest way to rule in or out causes 1 and 3.
- debugging-08: The recommended order is to start with a heap dump diff on the canary before load-testing the webhook path.
- explanation-01: Load factor is the number of entries the map holds relative to its array size.
- explanation-02: In the example, a transaction reads a row with version = 3, changes a value, and commits with UPDATE ... SET value = ?, version = 4 WHERE id = ? AND version = 3.
- explanation-02: A lost update in financial transactions could cause real financial loss.
- explanation-02: The failure mode of pessimistic locking is waiting for a lock, or deadlock.
- explanation-03: When a TCP connection starts, the sender does not know how many other connections share the path.
- explanation-03: If a sender transmitted at full speed immediately, it could trigger retransmissions that waste bandwidth.
- explanation-03: Every segment in a window can trigger an ACK.
- explanation-03: ssthresh stands for slow start threshold.
- explanation-03: On packet loss, TCP reduces ssthresh and the congestion window, and the ramp-up process restarts more cautiously.
- explanation-04: Python and Ruby serialize thread execution for CPU-bound code because of a global interpreter lock.
- explanation-04: Web servers and browsers use separate processes per request or per tab for fault isolation.
- explanation-04: Processes are preferable when work spans multiple machines or restarts independently.
- explanation-04: A process can be killed, restarted, or migrated without touching the rest of the application.
- explanation-04: Independent process lifecycle suits worker pools and microservices.
- explanation-06: A cache only helps when three conditions hold.
- explanation-06: If every request asks for different data, the cache stays empty.
- explanation-06: A write-heavy workload spends more effort maintaining the cache than it saves on reads.
- explanation-06: Adding a cache without profiling is like replacing a car part before checking what is wrong with the car.
- explanation-06: Adding a cache introduces a new component that can hide the real problem.
- explanation-06: The read-to-write mix can be measured by logging queries for a day or checking existing database metrics.
- explanation-06: If writes dominate or each request reads unique data, indexing, query optimization, or connection pooling are better options than caching.
- explanation-07: Vertical scaling no longer improving p99 query latency is a threshold that would push toward sharding.
- explanation-07: Vertical scaling consists of adding more CPU, more RAM, and faster disks.
- explanation-07: Having the engineering time to operate a distributed system and its failure modes is a factor that would push toward sharding.
- explanation-07: The product team cannot estimate growth.
- explanation-07: Without replicas, a single instance remains a single point of failure for both reads and writes.
- explanation-07: Vacuum, backup, and index maintenance windows grow longer as the dataset grows and can begin to affect availability.
- explanation-07: Staying single-instance risks underinvestment in query optimization and indexing, because adding capacity is always the easier short-term fix.
- explanation-07: Instrumentation should track storage growth rate, write and read throughput, query latency percentiles, and connection counts.
- explanation-08: For small payloads of a few hundred bytes, the fixed costs of a request dominate.
- explanation-08: Fixed costs of a request include network round trip, TLS, and connection handling.
- explanation-08: For small payloads, the choice of serialization format barely matters.
- explanation-08: If serialization and deserialization take 2% of total request time, a 5x faster codec saves about 1.6% overall.
- explanation-08: If serialization and deserialization take 40% of total request time, a 5x faster codec saves about 32% overall.
- explanation-08: The recommendation is to prototype the proposed binary format on the same payloads and compare serialization time, payload size, and CPU cost directly.
- explanation-08: The author offers to help set up benchmarks for the profiling and prototyping steps.
- explanation-08: Setting up those benchmarks requires knowing which binary format the colleague has in mind.
- explanation-08: Protocol Buffers, MessagePack, and FlatBuffers are examples of binary formats.
- summarization-02: A rollback restored a lower connection pool value taken from staging.
- summarization-02: The connection pool ran out under normal load.
- summarization-03: The speaker intends to check for relevant memory before responding.
- summarization-03: The speaker runs a shell command to read the file at /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-sshypran/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-taprfbjr/memory/MEMORY.md
- summarization-03: The memory index file is named MEMORY.md.
- summarization-03: The command suppresses error output by redirecting stderr to /dev/null.
- summarization-04: The expected result is that the PDF downloads.
- summarization-04: Four identical "export failed" error banners appear.
- summarization-04: The issue was reproduced by two different users.
- summarization-05: A sprint planning meeting took place on Monday.
- summarization-05: The listed action items come from Monday's sprint planning.
- summarization-07: A staging test of the new request batcher ran for six hours.
- summarization-07: The new request batcher cuts median latency by 18% in the staging test.
- summarization-07: All results other than the median latency reduction are uncertain.
- summarization-07: Tail latency (p99) might also improve.
- summarization-07: Staging traffic is smoother than production traffic.
- summarization-07: The p99 latency improvement number is probably optimistic.
- summarization-07: Memory use per worker grew by about 60 MB.
- summarization-07: The larger buffer pool is suspected to cause the increased memory use.
- summarization-07: The memory increase has not been profiled to confirm its cause.
- summarization-07: One worker crashed once during the run.
- summarization-07: The crash might be unrelated to the batcher.
- summarization-07: Staging uses a newer kernel.
- summarization-07: A batcher bug cannot yet be ruled out as the cause of the crash.
- summarization-08: The finding that the progress bar drives abandonment is classified as tentative.
- summarization-08: The sample is too small to confirm the link between the progress bar and abandonment.
- summarization-08: The remarks about differing default settings for admins and users were unprompted.

### plain-language

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 28 | 0 | 0.0 | 5 | 5 |
| code-review-02 | 20 | 15 | 0.75 | 18 | 3 |
| code-review-03 | 25 | 15 | 0.6 | 17 | 2 |
| code-review-04 | 27 | 16 | 0.593 | 22 | 2 |
| code-review-05 | 29 | 20 | 0.69 | 32 | 5 |
| code-review-06 | 31 | 17 | 0.548 | 33 | 10 |
| code-review-07 | 44 | 0 | 0.0 | 4 | 4 |
| code-review-08 | 4 | 1 | 0.25 | 0 | 0 |
| debugging-01 | 9 | 9 | 1.0 | 8 | 0 |
| debugging-02 | 15 | 8 | 0.533 | 16 | 2 |
| debugging-03 | 11 | 11 | 1.0 | 18 | 0 |
| debugging-04 | 17 | 8 | 0.471 | 12 | 4 |
| debugging-05 | 20 | 18 | 0.9 | 14 | 3 |
| debugging-06 | 30 | 0 | 0.0 | 0 | 0 |
| debugging-07 | 21 | 12 | 0.571 | 35 | 11 |
| debugging-08 | 46 | 20 | 0.435 | 33 | 11 |
| explanation-01 | 37 | 32 | 0.865 | 40 | 4 |
| explanation-02 | 26 | 18 | 0.692 | 22 | 0 |
| explanation-03 | 41 | 21 | 0.512 | 26 | 3 |
| explanation-04 | 41 | 30 | 0.732 | 38 | 3 |
| explanation-05 | 17 | 10 | 0.588 | 16 | 3 |
| explanation-06 | 26 | 16 | 0.615 | 25 | 1 |
| explanation-07 | 33 | 25 | 0.758 | 40 | 5 |
| explanation-08 | 10 | 9 | 0.9 | 14 | 8 |
| summarization-01 | 8 | 5 | 0.625 | 6 | 1 |
| summarization-02 | 15 | 12 | 0.8 | 15 | 3 |
| summarization-03 | 15 | 14 | 0.933 | 15 | 2 |
| summarization-04 | 15 | 11 | 0.733 | 10 | 1 |
| summarization-05 | 8 | 6 | 0.75 | 11 | 2 |
| summarization-06 | 13 | 12 | 0.923 | 14 | 0 |
| summarization-07 | 3 | 0 | 0.0 | 15 | 15 |
| summarization-08 | 18 | 17 | 0.944 | 24 | 2 |

Median fraction: 0.657 over 32 scored pairs.

Median additions: 3.0 over 32 scored pairs.

Lost facts:

- code-review-01: The parameter default `roles=[]` is a mutable default argument.
- code-review-01: A mutable default list is created once at function definition time.
- code-review-01: The default list is shared across all calls that do not pass `roles`.
- code-review-01: Each call that omits `roles` mutates and appends to the same shared list.
- code-review-01: Because of the shared default list, users accumulate roles from previous calls.
- code-review-01: The mutable default argument is a classic Python footgun.
- code-review-01: A bare `except:` catches everything, including `KeyboardInterrupt` and `SystemExit`.
- code-review-01: The bare `except:` silently swallows all errors with no logging.
- code-review-01: Errors swallowed by the bare except include bugs like `db` being `None` and network failures.
- code-review-01: Callers receive `False` with no information about what went wrong.
- code-review-01: The `db=None` default is used with no check that `db` was provided.
- code-review-01: If `db` is not passed, `db.insert(...)` raises an `AttributeError`.
- code-review-01: The `AttributeError` from a missing `db` is hidden by the bare except and the function just returns `False`.
- code-review-01: There is no validation that `db` is actually usable.
- code-review-01: The function performs no input validation.
- code-review-01: `name` is not checked for type or emptiness.
- code-review-01: Nothing prevents duplicate users or empty names.
- code-review-01: `roles.append("member")` mutates a caller-supplied list in place as a side effect.
- code-review-01: Mutating the caller's list can surprise a caller that still holds a reference to it.
- code-review-01: The function's return value is a bare bool.
- code-review-01: Returning `True`/`False` gives no detail on the failure reason.
- code-review-01: The bare bool return makes debugging and logging impossible for callers.
- code-review-01: The fixed version raises `ValueError("db is required")` when `db` is `None`.
- code-review-01: The fixed version uses `roles = list(roles) if roles else []` to copy the input list.
- code-review-01: The fixed version uses `roles=None` as the default instead of `[]`.
- code-review-01: The fixed version avoids mutating the caller's list.
- code-review-01: The fixed version makes the missing-`db` failure explicit instead of silently swallowed.
- code-review-01: The fixed version lets real exceptions propagate so callers can handle or log them.
- code-review-02: The function returns a promise that resolves to a crash rather than to a value.
- code-review-02: The function lacks error handling for malformed JSON.
- code-review-02: The function does not validate the shape of the response.
- code-review-02: The function assumes `data` always has a `.name` property.
- code-review-02: The fixed version throws an `Error` with the message `Failed to load profile: ${res.status}` when `res.ok` is false.
- code-review-03: Memory was checked for relevant context before the review was written.
- code-review-03: No relevant context was found stored in memory.
- code-review-03: SQL injection is the OWASP #1 issue.
- code-review-03: The code performs no input validation.
- code-review-03: The code does not check that `customer_name` and `status` are non-empty strings or of the expected type before use.
- code-review-03: The caller cannot distinguish a failed call from one that returned no rows.
- code-review-03: Returning raw rows ties callers to the DB driver's row representation rather than a defined interface such as a dict or dataclass.
- code-review-03: The return-type coupling issue is minor and depends on codebase conventions.
- code-review-03: The SQL injection is the only issue that must be fixed regardless of context.
- code-review-03: The remaining issues are stylistic or robustness judgments that depend on the codebase's conventions.
- code-review-04: Preemption between read and write can happen mid-bytecode because of the GIL's bytecode-boundary switching.
- code-review-04: The unsynchronized read-modify-write is guaranteed unsafe on non-CPython implementations.
- code-review-04: The operation would also be unsafe if `value` involved a `+=` on a non-atomic object.
- code-review-04: Depending on timing, the counter could end up as either `0` or `1` after a concurrent reset and increment.
- code-review-04: The outcome of a concurrent reset and increment is not documented.
- code-review-04: The class is documented by its usage as multi-threaded, but nothing in the implementation enforces thread safety.
- code-review-04: Torn reads are not a real risk for a Python `int` reference itself.
- code-review-04: The counter's value can be arbitrarily stale relative to other threads' operations, giving no ordering guarantees.
- code-review-04: The fix is to wrap mutations, and ideally reads, in a lock.
- code-review-04: The fixed `Counter` class creates a `threading.Lock` in `__init__` and acquires it in `increment`, `reset`, and the `value` property.
- code-review-04: In the fixed version, the `value` property returns a consistent snapshot instead of racing with in-progress mutations.
- code-review-05: A listing of the memory directory was run and no relevant memory was found.
- code-review-05: If the script is run with no arguments, `$1` is empty and `cd $BACKUP_DIR` becomes `cd` with no argument.
- code-review-05: `cd` with no argument changes to `$HOME`.
- code-review-05: An empty `BACKUP_DIR` combined with `rm -rf *.tmp` could delete `.tmp` files in the user's home directory.
- code-review-05: If no `.tmp` files exist, most shells leave the literal string `*.tmp` unexpanded.
- code-review-05: With no matching files, `rm -rf *.tmp` tries to remove a file literally named `*.tmp` and fails silently.
- code-review-05: If no `.log` files exist, `*.log` expands literally, `ls *.log` writes an error to stderr, and the command substitution returns nothing, so the loop does nothing.
- code-review-05: The loop doing nothing when no `.log` files exist is accidental rather than by design.
- code-review-05: The suggested rewrite uses `#!/bin/sh`, `set -eu`, `BACKUP_DIR=${1:?Usage: $0 <backup_dir>}`, quoted `cd`, `rm -f -- *.tmp`, a `for f in *.log` loop with an `[ -e "$f" ] || continue` guard, `gzip -- "$f"`, and a quoted echo.
- code-review-06: When `override` introduces a new nested dict, it is inserted by reference via `merged[key] = value`.
- code-review-06: The returned config can alias pieces of `override`.
- code-review-06: The depth of copying in the function is inconsistent across nested dicts.
- code-review-06: Nested dicts that pass through a recursive `merge_settings` call get copied.
- code-review-06: Nested dicts that are never touched or are freshly inserted do not get copied.
- code-review-06: The function performs no input validation.
- code-review-06: If `base` is not dict-like, `dict(base)` raises a confusing `TypeError` or `ValueError`.
- code-review-06: Callers receive a raw traceback into the function's internals rather than a meaningful config error.
- code-review-06: If `merged[key]` is a dict and the override value is not (or vice versa), no error is raised.
- code-review-06: On a type mismatch, the override value replaces the entire subtree.
- code-review-06: A typo'd override, such as a string where a nested settings block was expected, silently removes an entire section rather than failing loudly.
- code-review-06: `override` can introduce brand-new keys not present in `base`.
- code-review-06: Accepting new keys means typo'd keys are silently accepted as new settings instead of raising an error.
- code-review-06: There are no tests for the function.
- code-review-07: The for loop in the function has no return statement after it.
- code-review-07: If every attempt hits a 429 or 5xx error, the loop ends and the function implicitly returns undefined.
- code-review-07: The function has an explicit `return null` for non-retryable errors.
- code-review-07: The function returns null when it gives up immediately and undefined when it gives up after retrying.
- code-review-07: The asymmetry between null and undefined looks like a forgotten `return null;` after the loop rather than an intentional two-state signal.
- code-review-07: Caller code that checks `if (result === null)` to detect failure will silently miss the exhausted-retries case.
- code-review-07: On any error that isn't a 429 or status >= 500, the function returns null rather than throwing.
- code-review-07: Some old codebases use a 'never throw' contract so callers don't need try/catch.
- code-review-07: The function's return contract is three-valued: a real result, null, or undefined.
- code-review-07: A three-valued return contract is easy for a caller to get wrong.
- code-review-07: The user said callers exist that they cannot see.
- code-review-07: The checks `err.status === 429` and `err.status >= 500` assume err always has a numeric .status property.
- code-review-07: A plain Error, a network failure (ECONNRESET, DNS failure, fetch TypeError), or a timeout has no .status property.
- code-review-07: `undefined === 429` and `undefined >= 500` both evaluate to false.
- code-review-07: For errors without a .status, the function falls to `return null` on the very first attempt with no retry at all.
- code-review-07: Network failures and timeouts are exactly the transient errors that retry logic usually exists for.
- code-review-07: Treating non-HTTP errors as terminal looks like an oversight rather than intent.
- code-review-07: A 429 response waits `1000 * i` milliseconds before retrying.
- code-review-07: A 5xx response is retried immediately with no delay.
- code-review-07: Retrying instantly against a struggling server returning 5xx is the worse behavior.
- code-review-07: The variable `i` starts at 0.
- code-review-07: The delay on the first retry is `1000 * 0 = 0` milliseconds.
- code-review-07: A 429 gets retried immediately, then waits 1 second, then 2 seconds.
- code-review-07: `1000 * (i + 1)` was probably the intended delay formula if backoff before every retry was intended.
- code-review-07: The backoff is fixed and linear with no jitter and no maximum delay cap.
- code-review-07: Backoff without jitter risks synchronized retry storms across concurrent callers.
- code-review-07: The original error's message, status, and stack are discarded whether the failure is swallowed as null or dropped as undefined.
- code-review-07: There is no logging and no error wrapping in the function.
- code-review-07: A caller has no way to distinguish 'server said 400', 'network died', and 'succeeded with a null result'.
- code-review-07: If `attempts` is 0 or negative, the loop body never runs and `fn` is never invoked.
- code-review-07: With `attempts <= 0`, the function resolves to undefined.
- code-review-07: The default value of `attempts` is 3.
- code-review-07: The wrapper calls `fn(...args)` as a plain function, dropping `this` binding.
- code-review-07: If a caller passes an unbound method such as `withRetry(obj.method)`, `this` inside `fn` will be undefined or wrong.
- code-review-07: The user said they cannot verify whether callers passing unbound methods exist.
- code-review-07: Retrying 429 with backoff, retrying 5xx, and not retrying other errors is likely a deliberate policy choice.
- code-review-07: Swallowing terminal errors as null instead of throwing is likely a deliberate fail-soft contract.
- code-review-07: Falling off the loop into undefined after exhausting retries is likely a bug from a missing final `return null`.
- code-review-07: The lack of retry for errors without .status is likely a bug and an oversight.
- code-review-07: Whether the absence of backoff before retrying 5xx is deliberate or a bug is unclear.
- code-review-07: Whether the 0ms delay on the first 429 retry is deliberate or an off-by-one bug is unclear.
- code-review-07: The recommended first fix is making the return contract consistent, by either always throwing on unrecoverable failure or always returning null for every failure path including exhausted retries.
- code-review-07: The function's current return contract is neither always-throwing nor always-returning-a-single-sentinel.
- code-review-07: The helper makes 3 attempts by default.
- code-review-08: The memory may contain context on the project.
- code-review-08: The memory may contain context on the user's review preferences.
- code-review-08: A Read action was performed.
- debugging-02: In strict mode and in modules, `this` in such a callback is undefined.
- debugging-02: Class bodies are implicitly strict mode.
- debugging-02: Because class bodies are strict, `this` in the callback is undefined.
- debugging-02: Accessing `this.seconds` when `this` is undefined throws a TypeError: Cannot read properties of undefined.
- debugging-02: Seeing NaN instead indicates the function ran in a non-strict context where `this` resolved to the global object.
- debugging-02: Calling .bind(this) on the function is an alternative fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-04: The byte 0xc3 starts a multi-byte UTF-8 sequence.
- debugging-04: Characters such as é and ñ are encoded by multi-byte UTF-8 sequences beginning with 0xc3.
- debugging-04: Encoding can be detected if the file is not guaranteed to be UTF-8.
- debugging-04: chardet is a library that can detect the actual encoding of a file.
- debugging-04: charset-normalizer is a library that can detect the actual encoding of a file.
- debugging-04: Opening a file in binary mode with open(path, "rb") allows counting lines regardless of encoding.
- debugging-04: Binary mode avoids decoding the file entirely.
- debugging-04: Iterating a binary-mode file counts \n-delimited chunks.
- debugging-04: Binary mode is the safest option when the file's encoding is unknown or mixed.
- debugging-05: The fixed function uses `tags = tags + ["post"]`, which creates a new list.
- debugging-05: Calling `tags.append("post")` on the newly created list is an equivalent alternative.
- debugging-06: The described failure is a classic connection-pool exhaustion pattern.
- debugging-06: A shared-resource suspect (the analytics service) was already named in the user's setup.
- debugging-06: Contention with the analytics service is the most plausible cause of the failures.
- debugging-06: The analytics service may run its own scheduled jobs such as rollups, refreshes, or backups.
- debugging-06: If an analytics job overlaps the export window, it can hold connections or locks long enough to starve the shared connection pool.
- debugging-06: The failure does not always occur on the same batch number.
- debugging-06: The failure occurs about once a week.
- debugging-06: A non-fixed batch number and a weekly cadence fit a timing coincidence better than a data-dependent bug.
- debugging-06: A specific bad row would reliably cause failure on the same batch every time.
- debugging-06: Long-running or lock-blocked queries on the shared database can hold connections open far longer than usual.
- debugging-06: Holding connections open too long is a more likely cause than the pool simply being undersized.
- debugging-06: A connection leak in the export job or the analytics service could slowly consume pool capacity over a run.
- debugging-06: A connection leak would explain intermittent failures that appear only after enough connections leak during a long or heavy night.
- debugging-06: A connection leak does not explain the weekly periodicity as cleanly as analytics-job contention does.
- debugging-06: Database-side degradation from autovacuum, backups, a maintenance window, or a shared DB connection limit can increase per-query latency.
- debugging-06: Increased per-query latency can cause connections to be held longer than the 30-second timeout budget allows.
- debugging-06: The job has a 30-second timeout budget.
- debugging-06: The current setup only shows the timeout symptom and gives no visibility into pool state.
- debugging-06: There is currently no way to tell whether the pool drained slowly or spiked suddenly.
- debugging-06: Correlating the analytics service's schedule with failures is the highest-value check given the existing suspicion of resource sharing.
- debugging-06: The failure occurred at 02:14.
- debugging-06: pg_stat_activity is a source of DB-side state showing long-running queries, locks, and connection counts.
- debugging-06: The problem cannot be reproduced on demand.
- debugging-06: The application logs are rotated, so log data from failures is lost.
- debugging-06: The available log data from the failure was only a fragment.
- debugging-06: The pool topology may be either one pool per worker or one pool shared across all workers.
- debugging-06: If pools are per-worker, worker-3 being singled out could indicate uneven batch distribution rather than global pool exhaustion.
- debugging-06: worker-3 was the worker singled out in the failure.
- debugging-06: The DB-side snapshot and the analytics-schedule correlation are the cheapest diagnostics to set up.
- debugging-06: Those two checks are the most likely to confirm or rule out the overlapping-analytics-job theory.
- debugging-07: On a dev machine there is no contention, so event processing always finishes in time.
- debugging-07: Examples of shared state include the same digest bucket, the same default user, and the same 'latest N events' query with no test-specific filter.
- debugging-07: Event ID generation that is not collision-safe under concurrent creation, such as timestamp-based IDs with coarse resolution, could cause two events to collide and overwrite each other, silently dropping one.
- debugging-07: Adding a failure-only diagnostic recording worker id, event IDs and timestamps as created, and the raw digest response, and uploading it as a CI artifact even for transient failures, is the highest-leverage first step.
- debugging-07: Confirming that each xdist worker gets an isolated DB, schema, or namespace is a check worth doing.
- debugging-07: If workers share one database, that is likely the culprit and is usually the cheaper fix.
- debugging-07: Logging server-side when each event is created and when the digest is computed, including windowing boundaries, would show on the next failure whether the third event was never created, created but excluded by a time window, or created and then overwritten.
- debugging-07: Artificially adding latency to event creation or oversubscribing workers (for example `-n 8` on a 4-core box) increases contention and can reproduce the failure faster.
- debugging-07: If the failure rate climbs with more contention, that strongly confirms a race rather than isolation bleed.
- debugging-08: The service's memory grows about 2% per day.
- debugging-08: Growth that is worse during campaigns indicates growth tracks distinct new data (new SKUs, promo codes, campaign IDs) rather than raw request count.
- debugging-08: Memory never drops overnight.
- debugging-08: Memory that never drops overnight rules out GC backlog or a young-generation effect that a quiet period would let the collector clean up.
- debugging-08: Memory that never drops overnight means the growing data is either still reachable (a real leak) or is native/off-heap fragmentation that GC cannot touch.
- debugging-08: Canary growth without webhooks implies there are at least two sources: a baseline leak under normal traffic and something webhooks amplify.
- debugging-08: The service has a size-bounded cache whose bound has been unchanged for a year.
- debugging-08: A stable cache bound does not rule out the cache as the cause.
- debugging-08: A cache bound may be enforced on entry count without being enforced in memory.
- debugging-08: Keys with broken equals/hashCode can make a cache believe it evicted something it did not evict.
- debugging-08: Leaked objects that are strongly reachable cannot be reclaimed by GC overnight.
- debugging-08: Logging cache size, hit rate, and eviction count over a day can confirm whether entry count stays flat while memory grows.
- debugging-08: Grepping for `removalListener` or `onEvict`-style hooks can reveal listeners that do not detach fully.
- debugging-08: The second most plausible cause is unbounded metric or log label cardinality.
- debugging-08: Emitting metrics or logs with dynamic labels such as product ID, promo code, or campaign ID creates new time series for every new campaign.
- debugging-08: New time series created by dynamic labels live forever in the metrics client's registry.
- debugging-08: Unbounded label cardinality matches the campaign correlation, the baseline-only canary growth, and the lack of overnight recovery.
- debugging-08: Normal traffic still creates some new metric labels, just fewer than campaign traffic.
- debugging-08: Metrics registries are maps that are never cleared.
- debugging-08: Most metrics client libraries expose a count of registry size.
- debugging-08: The third most plausible cause is a webhook-specific registration leak.
- debugging-08: Sizes of suspect global structures can be compared between canary and prod via a debug endpoint or periodic size logging.
- debugging-08: The fourth plausible cause is native/off-heap growth from connections, buffers, or fragmentation.
- debugging-08: Native/off-heap growth can coexist with the cache, metrics, and webhook registration causes.
- debugging-08: Cache stats and metrics-registry size can be logged on an interval and overlaid against the memory curve.
- debugging-08: This investigation approach requires no profiler.
- explanation-01: Most textbook hash map implementations use chaining by default.
- explanation-01: Quadratic probing and double hashing give better spread than linear probing.
- explanation-01: Python's dict uses open addressing.
- explanation-01: Open addressing typically requires keeping the load factor under about 70%.
- explanation-01: A good hash function that spreads keys evenly is what keeps collisions rare.
- explanation-02: An optimistic locking example uses a `products` table with a `version` column.
- explanation-02: In the example, a row is read with `version = 5`, edited in memory, then updated with `UPDATE products SET price = 19.99, version = 6 WHERE id = 42 AND version = 5;`.
- explanation-02: REST APIs editing independent records are an example use case for optimistic locking.
- explanation-02: A pessimistic locking example uses `BEGIN;`, `SELECT * FROM products WHERE id = 42 FOR UPDATE;`, `UPDATE products SET price = 19.99 WHERE id = 42;`, and `COMMIT;`.
- explanation-02: Other transactions trying to run `SELECT ... FOR UPDATE` on id=42 block at that statement.
- explanation-02: Inventory decrements at checkout are an example use case for pessimistic locking.
- explanation-02: Generating sequential invoice numbers is an example use case for pessimistic locking.
- explanation-02: The recommended default is to use optimistic locking.
- explanation-03: Packet loss from overflowing router buffers harms all users on that network path.
- explanation-03: A sender that is too conservative wastes available bandwidth.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The receiver's advertised window reflects the receiver's buffer space.
- explanation-03: Historically, the initial cwnd was 1 segment.
- explanation-03: The initial cwnd is now typically around 10 segments.
- explanation-03: RFC 6928 specifies the initial congestion window of about 10 segments.
- explanation-03: One round-trip's worth of ACKs returns roughly together.
- explanation-03: An example cwnd progression during slow start is 10 → 20 → 40 → 80.
- explanation-03: The threshold at which TCP leaves slow start is called ssthresh.
- explanation-03: Congestion avoidance grows the window linearly rather than exponentially.
- explanation-03: Slow start is called 'slow' relative to immediately sending as much data as the receiver's window allows.
- explanation-03: Earlier TCP implementations immediately sent as much data as the receiver's window allowed.
- explanation-03: Congestion collapse became a real problem in the mid-1980s.
- explanation-03: Linear growth from 1 segment would take far too long to reach useful throughput on high-bandwidth paths.
- explanation-03: After slow start, TCP hands off to steadier mechanisms including congestion avoidance and loss/ECN-triggered backoff.
- explanation-03: Those steadier mechanisms fine-tune around the capacity estimate for the rest of the connection's life.
- explanation-03: Slow start recurs after a connection has been idle.
- explanation-03: Slow start recurs after a timeout-based loss.
- explanation-03: Slow start recurs in those cases because the old cwnd value may no longer reflect current network conditions.
- explanation-04: A process has its own file descriptors.
- explanation-04: A process has its own OS-level resources.
- explanation-04: All threads in a process share the same file descriptors.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own register state.
- explanation-04: Switching between threads is cheaper than switching between processes.
- explanation-04: Browsers such as Chrome run tabs as separate processes.
- explanation-04: Supervisors like systemd favor a process-per-task model.
- explanation-04: Erlang's OTP favors a process-per-task model.
- explanation-04: Processes can be resource-limited via cgroups and ulimits.
- explanation-04: Inter-process communication mechanisms include pipes, sockets, and shared memory.
- explanation-05: Examples of long-lived objects include a global event bus, a DOM node, and a singleton.
- explanation-05: A long-lived object keeps a reference to a registered callback and to everything that callback closes over.
- explanation-05: An unregistered callback and its captured state stay reachable forever.
- explanation-05: Closures capturing more than they need are a frequent cause of memory leaks.
- explanation-05: Static or global collections accumulating objects are a frequent cause of memory leaks.
- explanation-05: Detached-but-referenced resources are a frequent cause of memory leaks.
- explanation-05: A removed DOM node that is still referenced by JavaScript code is an example of a detached-but-referenced resource.
- explanation-06: A cache in front of the database does not help when an API is slow due to CPU-bound work.
- explanation-06: A cache in front of the database does not help when slowness comes from N+1 queries.
- explanation-06: A cache in front of the database does not help when slowness comes from missing indexes.
- explanation-06: A cache in front of the database does not help when slowness comes from slow serialization.
- explanation-06: In a write-heavy workload, writes still hit the database.
- explanation-06: A cache is another moving part that can fail or get out of sync with the database.
- explanation-06: A product page fetched thousands of times is an example of a repeat-query workload that benefits from caching.
- explanation-06: If each query has different parameters, nothing repeats in the cache.
- explanation-06: Checking the slow query log and running EXPLAIN on the heaviest queries is a recommended diagnostic step.
- explanation-06: Redis is an example of a cache.
- explanation-07: If a product team cannot estimate its data growth rate, that usually means the product isn't proven yet.
- explanation-07: An unproven product is a strong argument against sharding.
- explanation-07: Sharding does nothing to fix bad connection pooling.
- explanation-07: Sharding does nothing to fix read-heavy load.
- explanation-07: A 200 GB deployment likely has 5-10x headroom before vertical scaling plus read replicas stop working.
- explanation-07: Sharding requires a shard key that distributes data evenly.
- explanation-07: Under sharding, cross-shard transactions, joins, and unique constraints become permanent application-level problems.
- explanation-07: Sharding multiplies operational complexity because N databases must be backed up, migrated, monitored, and patched.
- explanation-08: Serialization performance can matter a lot when pushing large payloads at high throughput.
- summarization-01: Internal-only changes were omitted from the release notes.
- summarization-01: The omitted internal changes include build tooling, a module refactor, and the telemetry interval.
- summarization-01: The omitted internal changes do not affect user-facing behavior.
- summarization-02: The team was paged at 09:21.
- summarization-02: Detection-to-mitigation took approximately 34 minutes.
- summarization-02: The detection-to-mitigation response was reactive rather than preventive.
- summarization-03: The new worker pool would update records once thumbnails are ready.
- summarization-04: The report selected to reproduce the bug is the "March" report.
- summarization-04: One error banner appears per click of the PDF export button.
- summarization-04: The bug was reproduced on the latest version of Firefox.
- summarization-04: The bug was reproduced on two different machines.
- summarization-05: Ada is to check with the mobile team's lead to confirm the mobile team has been informed of the API deprecation.
- summarization-05: There is an API deprecation that the mobile team needs to be informed about.
- summarization-06: The on-call engineer suspects connection-pool exhaustion in the payments client.
- summarization-07: The speaker is checking memory for relevant context.
- summarization-07: The check is being done before writing a summary.
- summarization-07: A summary is going to be written.
- summarization-08: The progress bar finding is rated Firm for the abandonment behavior and Tentative for the cause.

Added facts (styled only):

- code-review-01: The speaker will check their memory before answering.
- code-review-01: The speaker's memory may contain saved preferences about code reviews.
- code-review-01: There is a tool named TmuxExecute.
- code-review-01: TmuxExecute runs a command in a persistent shell session.
- code-review-01: TmuxExecute accepts an optional timeout.
- code-review-02: fetch only rejects on network failure.
- code-review-02: Without checking res.ok, the caller gets a confusing TypeError instead of a clear "user not found" message.
- code-review-02: In an async function, an unhandled rejection produces a rejected promise with no clear error message for the caller.
- code-review-03: The placeholder %s is used for MySQL and psycopg2.
- code-review-03: The propagated exception carries no context about which query failed.
- code-review-04: Adding a get_value() method would not guarantee the value read is up to date at the microsecond it is used, because another thread could change it right after.
- code-review-04: Values becoming stale immediately after a read is expected in concurrent code.
- code-review-05: `cd ""` typically leaves you in the current directory, though behavior varies by shell.
- code-review-05: `rm -rf *.tmp` is the most dangerous line in the script.
- code-review-05: `for f in $(ls *.log)` fails outright if no `.log` files exist.
- code-review-05: The `#!/bin/sh` shebang is appropriate because the script uses no bash-only features.
- code-review-05: If bash-specific syntax is added later, the shebang must be updated.
- code-review-06: The function only checks that the base value is a dict, using the condition `elif key in merged and isinstance(merged[key], dict)`.
- code-review-06: The function never checks that the override value is also a dict.
- code-review-06: If base[key] is a dict but override[key] is a non-dict such as a string, number, or False, the code calls merge_settings(merged[key], value).
- code-review-06: Inside that recursive call, value.items() fails because value is not a dict.
- code-review-06: The mismatched-type case raises an AttributeError instead of having the override replace the whole sub-dict.
- code-review-06: The fix for the mismatched-type bug is to add `and isinstance(value, dict)` to the condition.
- code-review-06: The function name merge_settings gives no hint that the function also deletes keys.
- code-review-06: The crash on mismatched types is classified as a bug that needs a type check on value.
- code-review-06: The two issues to fix first are the type-check gap and the shallow-copy behavior.
- code-review-06: The type-check gap causes real crashes.
- code-review-07: The assistant will check its memory for prior guidance on how the user likes code reviews done.
- code-review-07: The assistant will review the function after checking memory.
- code-review-07: There is prior guidance from the user about how code reviews should be done.
- code-review-07: The memory index file is located at /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-sshypran/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-taprfbjr/memory/MEMORY.md
- debugging-02: In the buggy code, `this.seconds` evaluates to `undefined`.
- debugging-02: Because of this, `this.seconds` becomes `NaN` permanently.
- debugging-04: The byte 0xc3 appears at position 512 in the file.
- debugging-04: UTF-8 covers ASCII plus a much larger set of characters.
- debugging-04: Passing errors="replace" swaps bad bytes for a placeholder.
- debugging-04: Passing errors="ignore" drops bad bytes.
- debugging-05: In the fixed version, `tags = list(DEFAULT_TAGS)` when `tags is None` gives each call a fresh copy of `DEFAULT_TAGS`.
- debugging-05: A mutable object such as a list, dict, or set should never be used as a default argument value.
- debugging-05: This bug appears any time a mutable object is used as a default argument value.
- debugging-07: If reads go to a replica and writes go to a primary, replication lag can hide recent writes from the digest.
- debugging-07: A cached digest or event count computed just before the third event lands can cause the same failure.
- debugging-07: A temporary print or log line that appears in CI output will help despite the lack of stored artifacts.
- debugging-07: Isolating the test means running it alone with 4 workers as the only test in the run.
- debugging-07: If the isolated test still fails occasionally, the cause is internal timing between seed and read rather than cross-test interference.
- debugging-07: If the test fails only when other tests run alongside it, the cause lies in shared fixtures, shared IDs, or shared time windows.
- debugging-07: Temporarily adding a poll-and-retry after seeding, or a fixed short sleep, and rerunning many times is a diagnostic step.
- debugging-07: If adding a synchronization point makes the failure disappear, that confirms an eventual-consistency gap.
- debugging-07: Checking whether the digest reads from the primary database directly or through a cache, search index, or read replica identifies the data source.
- debugging-07: The digest's data source is usually where the real fix belongs.
- debugging-07: The fix is usually either making the seed call synchronous with the digest's data source or making the test explicitly wait for consistency.
- debugging-08: `jmap -histo:live` is a Java command for taking a heap histogram.
- debugging-08: A heap histogram diff often points directly at the cause of memory growth.
- debugging-08: The canary instance still runs background reads or refresh jobs.
- debugging-08: Background reads or refresh jobs on the canary cause the same cache churn at a smaller scale, explaining why the canary still grows but more slowly.
- debugging-08: A heap dump's dominator tree can be used to trace what holds a reference to a leaking object.
- debugging-08: The canary adds a few entries from its own internal or retry traffic, which explains its slower growth.
- debugging-08: A background job running on every instance — such as a scheduled task, metrics collector, or log buffer — may retain data it never releases.
- debugging-08: Disabling background jobs one at a time on a staging instance and watching whether the growth curve flattens can identify a leaking background job.
- debugging-08: The heap histogram diff will likely confirm cause 1 or cause 2 directly.
- debugging-08: If the growing type is not obvious from the heap, the recommended next steps are comparing RSS to heap and disabling background jobs on staging.
- debugging-08: Checking RSS versus heap and disabling background jobs on staging serve to isolate the baseline growth seen on the canary.
- explanation-01: Python's dict uses a variation of chaining in earlier design terms.
- explanation-01: Most general-purpose hash maps resize themselves once they get too full.
- explanation-01: Resizing a hash map means growing the array and rehashing everything.
- explanation-01: Resizing keeps collisions rare regardless of the collision-handling strategy used.
- explanation-03: Dropped packets waste bandwidth and cause delays.
- explanation-03: Dropped packets cause delays because the sender has to detect the loss and resend the data.
- explanation-03: In congestion collapse, most of the traffic is retransmissions and almost no data gets through.
- explanation-04: Web servers often use one process per worker to allow independent restarts.
- explanation-04: I/O-bound work includes waiting on a network call, a disk read, or a database query.
- explanation-04: While one thread waits on I/O, another thread can run.
- explanation-05: During a memory leak, the program uses more and more memory over time even though the retained data serves no purpose.
- explanation-05: A memory leak can slow a program down.
- explanation-05: A memory leak can crash a program.
- explanation-06: Checking the read-to-write mix involves counting how many requests are reads compared to writes over a normal day.
- explanation-07: The assistant is checking its memory for relevant context before answering.
- explanation-07: Even a rough growth guess allows calculation of a doubling time.
- explanation-07: Scrambling to shard under pressure leaves less time to test the migration.
- explanation-07: Quick fixes such as bigger hardware, replicas, and caching can mask the need for sharding.
- explanation-07: Quick fixes can make an eventual sharding project more complex because more data and more application logic must be migrated at once.
- explanation-08: Switching serialization formats only speeds things up if serialization is a large share of request time.
- explanation-08: A few percent reduction in request time is not a meaningful speedup.
- explanation-08: A binary format may meaningfully shrink payload size.
- explanation-08: Serialization's share of total request time can be determined by profiling a few representative requests.
- explanation-08: If serialization time is under 5-10% of total request time, switching formats is likely not worth it.
- explanation-08: Switching serialization formats incurs the cost of format migration.
- explanation-08: Switching serialization formats incurs the cost of tooling changes.
- explanation-08: Switching to a binary serialization format costs human-readability.
- summarization-01: The app now starts about 40% faster.
- summarization-02: The incorrect pool size exhausted the database connection pool.
- summarization-02: The outage caused errors for about 12% of checkout requests.
- summarization-02: The outage ran from 09:14 to 09:48 UTC.
- summarization-03: Under the proposal, uploads would finish in under 100ms.
- summarization-03: Uploads currently take 800ms to 3 seconds.
- summarization-04: A colleague observed the failure on Chrome.
- summarization-05: The listed action items come from a sprint planning meeting.
- summarization-05: Chen's search indexing work and demo are due Friday.
- summarization-07: A new request batcher was tested against the current request batcher on staging.
- summarization-07: The test ran for six hours.
- summarization-07: Median latency dropped 18%.
- summarization-07: The median latency drop is a clear, data-backed result.
- summarization-07: Tail latency (p99) may have improved as well.
- summarization-07: Staging traffic is smoother than production traffic.
- summarization-07: The p99 improvement figure is likely too optimistic.
- summarization-07: Memory use per worker rose by about 60 MB.
- summarization-07: The memory increase is guessed to come from the larger buffer pool.
- summarization-07: The memory increase has not been profiled to confirm its cause.
- summarization-07: One worker crashed once during the run.
- summarization-07: It is not yet known whether the batcher caused the crash.
- summarization-07: The crash may be linked to staging's newer kernel.
- summarization-07: Staging runs a newer kernel.
- summarization-07: More testing is needed before drawing conclusions about the crash, memory growth, and tail latency.
- summarization-08: The finding about large-file uploads is tentative but worth acting on.
- summarization-08: With only three participants, the large-file upload finding is tentative.

### technical-simplified

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 28 | 22 | 0.786 | 21 | 4 |
| code-review-02 | 20 | 13 | 0.65 | 14 | 0 |
| code-review-04 | 27 | 17 | 0.63 | 17 | 0 |
| code-review-05 | 29 | 22 | 0.759 | 23 | 6 |
| code-review-07 | 44 | 27 | 0.614 | 30 | 6 |
| code-review-08 | 4 | 0 | 0.0 | 38 | 38 |
| debugging-01 | 9 | 9 | 1.0 | 7 | 0 |
| debugging-02 | 15 | 9 | 0.6 | 14 | 1 |
| debugging-03 | 11 | 11 | 1.0 | 9 | 0 |
| debugging-04 | 17 | 11 | 0.647 | 14 | 2 |
| debugging-05 | 20 | 17 | 0.85 | 12 | 0 |
| debugging-06 | 30 | 13 | 0.433 | 22 | 10 |
| explanation-01 | 37 | 17 | 0.459 | 18 | 1 |
| explanation-02 | 26 | 18 | 0.692 | 25 | 2 |
| explanation-03 | 41 | 22 | 0.537 | 20 | 2 |
| explanation-04 | 41 | 26 | 0.634 | 24 | 1 |
| explanation-05 | 17 | 12 | 0.706 | 13 | 0 |
| explanation-06 | 26 | 19 | 0.731 | 21 | 2 |
| explanation-07 | 33 | 18 | 0.545 | 19 | 2 |
| summarization-01 | 8 | 5 | 0.625 | 5 | 1 |
| summarization-02 | 15 | 9 | 0.6 | 13 | 2 |
| summarization-03 | 15 | 14 | 0.933 | 13 | 0 |
| summarization-04 | 15 | 13 | 0.867 | 14 | 2 |
| summarization-05 | 8 | 6 | 0.75 | 13 | 1 |
| summarization-06 | 13 | 0 | 0.0 | 6 | 6 |
| summarization-08 | 18 | 15 | 0.833 | 18 | 3 |

Median fraction: 0.649 over 26 scored pairs.

Median additions: 2.0 over 26 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python footgun.
- code-review-01: Nothing prevents duplicate users or empty names.
- code-review-01: `roles.append("member")` mutates a caller-supplied list in place as a side effect.
- code-review-01: Mutating the caller's list can surprise a caller that still holds a reference to it.
- code-review-01: The fixed version raises `ValueError("db is required")` when `db` is `None`.
- code-review-01: The fixed version uses `roles = list(roles) if roles else []` to copy the input list.
- code-review-02: Accessing `profile.name` when `profile` is `undefined` throws a `TypeError`.
- code-review-02: The error thrown is `Cannot read properties of undefined (reading 'name')`.
- code-review-02: The function returns a promise that resolves to a crash rather than to a value.
- code-review-02: The function lacks error handling for malformed JSON.
- code-review-02: The function does not validate the shape of the response.
- code-review-02: The function assumes `data` always has a `.name` property.
- code-review-02: If the API returns an error object or something unexpected, the function fails silently or throws later.
- code-review-04: Preemption between read and write can happen mid-bytecode because of the GIL's bytecode-boundary switching.
- code-review-04: The unsynchronized read-modify-write is guaranteed unsafe on non-CPython implementations.
- code-review-04: The operation would also be unsafe if `value` involved a `+=` on a non-atomic object.
- code-review-04: Two threads can both read `current = 5` and then both write `6`, losing one increment.
- code-review-04: Depending on timing, the counter could end up as either `0` or `1` after a concurrent reset and increment.
- code-review-04: The outcome of a concurrent reset and increment is not documented.
- code-review-04: The class is documented by its usage as multi-threaded, but nothing in the implementation enforces thread safety.
- code-review-04: No `get()` or `value` accessor is shown being used.
- code-review-04: Torn reads are not a real risk for a Python `int` reference itself.
- code-review-04: The counter's value can be arbitrarily stale relative to other threads' operations, giving no ordering guarantees.
- code-review-05: A listing of the memory directory was run and no relevant memory was found.
- code-review-05: If no `.log` files exist, `*.log` expands literally, `ls *.log` writes an error to stderr, and the command substitution returns nothing, so the loop does nothing.
- code-review-05: The loop doing nothing when no `.log` files exist is accidental rather than by design.
- code-review-05: `gzip` failures are not checked, so the loop continues silently if a `.log` file is locked or unwritable.
- code-review-05: The final "Cleaned" message is misleading because it implies success regardless of the actual outcome.
- code-review-05: The suggested rewrite uses `#!/bin/sh`, `set -eu`, `BACKUP_DIR=${1:?Usage: $0 <backup_dir>}`, quoted `cd`, `rm -f -- *.tmp`, a `for f in *.log` loop with an `[ -e "$f" ] || continue` guard, `gzip -- "$f"`, and a quoted echo.
- code-review-05: The rewrite fixes missing-argument handling, unsafe `cd`, quoting, the `ls`-in-a-loop anti-pattern, and the unhandled no-match glob case, and fails fast on unexpected errors via `set -eu`.
- code-review-07: The asymmetry between null and undefined looks like a forgotten `return null;` after the loop rather than an intentional two-state signal.
- code-review-07: Some old codebases use a 'never throw' contract so callers don't need try/catch.
- code-review-07: The user said callers exist that they cannot see.
- code-review-07: A plain Error, a network failure (ECONNRESET, DNS failure, fetch TypeError), or a timeout has no .status property.
- code-review-07: Network failures and timeouts are exactly the transient errors that retry logic usually exists for.
- code-review-07: `1000 * (i + 1)` was probably the intended delay formula if backoff before every retry was intended.
- code-review-07: Backoff without jitter risks synchronized retry storms across concurrent callers.
- code-review-07: There is no logging and no error wrapping in the function.
- code-review-07: If `attempts` is 0 or negative, the loop body never runs and `fn` is never invoked.
- code-review-07: With `attempts <= 0`, the function resolves to undefined.
- code-review-07: The default value of `attempts` is 3.
- code-review-07: The user said they cannot verify whether callers passing unbound methods exist.
- code-review-07: Falling off the loop into undefined after exhausting retries is likely a bug from a missing final `return null`.
- code-review-07: Whether the absence of backoff before retrying 5xx is deliberate or a bug is unclear.
- code-review-07: Whether the 0ms delay on the first 429 retry is deliberate or an off-by-one bug is unclear.
- code-review-07: The recommended first fix is making the return contract consistent, by either always throwing on unrecoverable failure or always returning null for every failure path including exhausted retries.
- code-review-07: The helper makes 3 attempts by default.
- code-review-08: The speaker will check memory for relevant context before proceeding.
- code-review-08: The memory may contain context on the project.
- code-review-08: The memory may contain context on the user's review preferences.
- code-review-08: A Read action was performed.
- debugging-02: Class bodies are implicitly strict mode.
- debugging-02: Because class bodies are strict, `this` in the callback is undefined.
- debugging-02: Accessing `this.seconds` when `this` is undefined throws a TypeError: Cannot read properties of undefined.
- debugging-02: Seeing NaN instead indicates the function ran in a non-strict context where `this` resolved to the global object.
- debugging-02: Calling .bind(this) on the function is an alternative fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-04: Characters such as é and ñ are encoded by multi-byte UTF-8 sequences beginning with 0xc3.
- debugging-04: charset-normalizer is a library that can detect the actual encoding of a file.
- debugging-04: Opening a file in binary mode with open(path, "rb") allows counting lines regardless of encoding.
- debugging-04: Binary mode avoids decoding the file entirely.
- debugging-04: Iterating a binary-mode file counts \n-delimited chunks.
- debugging-04: Binary mode is the safest option when the file's encoding is unknown or mixed.
- debugging-05: The fixed function uses `tags = tags + ["post"]`, which creates a new list.
- debugging-05: Calling `tags.append("post")` on the newly created list is an equivalent alternative.
- debugging-05: `DEFAULT_TAGS` is module-level state.
- debugging-06: Contention with the analytics service is the most plausible cause of the failures.
- debugging-06: A specific bad row would reliably cause failure on the same batch every time.
- debugging-06: Holding connections open too long is a more likely cause than the pool simply being undersized.
- debugging-06: A connection leak does not explain the weekly periodicity as cleanly as analytics-job contention does.
- debugging-06: Database-side degradation from autovacuum, backups, a maintenance window, or a shared DB connection limit can increase per-query latency.
- debugging-06: The job has a 30-second timeout budget.
- debugging-06: Correlating the analytics service's schedule with failures is the highest-value check given the existing suspicion of resource sharing.
- debugging-06: The failure occurred at 02:14.
- debugging-06: pg_stat_activity is a source of DB-side state showing long-running queries, locks, and connection counts.
- debugging-06: The problem cannot be reproduced on demand.
- debugging-06: The application logs are rotated, so log data from failures is lost.
- debugging-06: The available log data from the failure was only a fragment.
- debugging-06: The pool topology may be either one pool per worker or one pool shared across all workers.
- debugging-06: If pools are per-worker, worker-3 being singled out could indicate uneven batch distribution rather than global pool exhaustion.
- debugging-06: worker-3 was the worker singled out in the failure.
- debugging-06: The DB-side snapshot and the analytics-schedule correlation are the cheapest diagnostics to set up.
- debugging-06: Those two checks are the most likely to confirm or rule out the overlapping-analytics-job theory.
- explanation-01: The internal array of a hash map is called the bucket array.
- explanation-01: The bucket array is finite while the set of possible keys is in theory infinite.
- explanation-01: Collisions are unavoidable in a hash map.
- explanation-01: In chaining, large buckets may use a tree instead of a list.
- explanation-01: Chaining delete hashes the key and removes the matching entry from the list.
- explanation-01: Java's HashMap uses chaining by default.
- explanation-01: Most textbook hash map implementations use chaining by default.
- explanation-01: Quadratic probing and double hashing give better spread than linear probing.
- explanation-01: Open addressing lookup hashes the key, checks that slot, and follows the probe sequence until the key or an empty slot is found.
- explanation-01: In open addressing, clearing a deleted slot breaks the probe chain for later lookups.
- explanation-01: Open addressing deletion usually requires a special tombstone marker.
- explanation-01: Python's dict uses open addressing.
- explanation-01: Chaining has poor cache behavior because list nodes are scattered in memory.
- explanation-01: Open addressing has good cache behavior because probing stays within the array.
- explanation-01: Deletion is simple in chaining and awkward in open addressing.
- explanation-01: Chaining is simpler to reason about and tolerates a high load factor.
- explanation-01: Chaining pays a memory and cache-locality cost.
- explanation-01: Open addressing is more memory-efficient and cache-friendly.
- explanation-01: Open addressing requires more careful tuning and more complex deletion logic.
- explanation-01: A good hash function that spreads keys evenly is what keeps collisions rare.
- explanation-02: An optimistic locking example uses a `products` table with a `version` column.
- explanation-02: In the example, a row is read with `version = 5`, edited in memory, then updated with `UPDATE products SET price = 19.99, version = 6 WHERE id = 42 AND version = 5;`.
- explanation-02: REST APIs editing independent records are an example use case for optimistic locking.
- explanation-02: A pessimistic locking example uses `BEGIN;`, `SELECT * FROM products WHERE id = 42 FOR UPDATE;`, `UPDATE products SET price = 19.99 WHERE id = 42;`, and `COMMIT;`.
- explanation-02: Other transactions trying to run `SELECT ... FOR UPDATE` on id=42 block at that statement.
- explanation-02: Inventory decrements at checkout are an example use case for pessimistic locking.
- explanation-02: Generating sequential invoice numbers is an example use case for pessimistic locking.
- explanation-02: The recommended default is to use optimistic locking.
- explanation-03: This condition of overloading the network path is called 'congestion'.
- explanation-03: A sender that is too conservative wastes available bandwidth.
- explanation-03: TCP has no mechanism to directly ask the network how fast it can send.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The receiver's advertised window reflects the receiver's buffer space.
- explanation-03: Historically, the initial cwnd was 1 segment.
- explanation-03: The initial cwnd is now typically around 10 segments.
- explanation-03: RFC 6928 specifies the initial congestion window of about 10 segments.
- explanation-03: One round-trip's worth of ACKs returns roughly together.
- explanation-03: An example cwnd progression during slow start is 10 → 20 → 40 → 80.
- explanation-03: Slow start is called 'slow' relative to immediately sending as much data as the receiver's window allows.
- explanation-03: Earlier TCP implementations immediately sent as much data as the receiver's window allowed.
- explanation-03: Congestion collapse became a real problem in the mid-1980s.
- explanation-03: Linear growth from 1 segment would take far too long to reach useful throughput on high-bandwidth paths.
- explanation-03: After slow start, TCP hands off to steadier mechanisms including congestion avoidance and loss/ECN-triggered backoff.
- explanation-03: Those steadier mechanisms fine-tune around the capacity estimate for the rest of the connection's life.
- explanation-03: Slow start recurs after a connection has been idle.
- explanation-03: Slow start recurs after a timeout-based loss.
- explanation-03: Slow start recurs in those cases because the old cwnd value may no longer reflect current network conditions.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own register state.
- explanation-04: Switching between threads is cheaper than switching between processes.
- explanation-04: Threads are cheaper than processes because there is no memory space to duplicate or isolate.
- explanation-04: Browsers such as Chrome run tabs as separate processes.
- explanation-04: Supervisors like systemd favor a process-per-task model.
- explanation-04: Erlang's OTP favors a process-per-task model.
- explanation-04: Spawning multiple processes with Python's multiprocessing gives each process its own interpreter and GIL.
- explanation-04: Processes can run under different users.
- explanation-04: Processes can run under different sandboxes, such as seccomp or containers.
- explanation-04: Processes can run at different privilege levels.
- explanation-04: Threads cannot be isolated by user, sandbox, or privilege level because they share the same address space and credentials.
- explanation-04: Processes can be resource-limited via cgroups and ulimits.
- explanation-04: Independent process lifecycle management suits worker pools where a hung or leaking worker should be recycled without affecting others.
- explanation-04: Inter-process communication mechanisms include pipes, sockets, and shared memory.
- explanation-05: Examples of long-lived objects include a global event bus, a DOM node, and a singleton.
- explanation-05: Closures capturing more than they need are a frequent cause of memory leaks.
- explanation-05: Static or global collections accumulating objects are a frequent cause of memory leaks.
- explanation-05: Detached-but-referenced resources are a frequent cause of memory leaks.
- explanation-05: A removed DOM node that is still referenced by JavaScript code is an example of a detached-but-referenced resource.
- explanation-06: In a write-heavy workload, writes still hit the database.
- explanation-06: A product page fetched thousands of times is an example of a repeat-query workload that benefits from caching.
- explanation-06: If each query has different parameters, nothing repeats in the cache.
- explanation-06: Adding basic timing or tracing to slow endpoints lets you measure DB query time versus everything else.
- explanation-06: Checking the slow query log and running EXPLAIN on the heaviest queries is a recommended diagnostic step.
- explanation-06: The fix for slow queries is often an index rather than a cache.
- explanation-06: Redis is an example of a cache.
- explanation-07: 200 GB of data growing at 10% per year is a non-event.
- explanation-07: If a product team cannot estimate its data growth rate, that usually means the product isn't proven yet.
- explanation-07: An unproven product is a strong argument against sharding.
- explanation-07: Sharding does nothing to fix slow queries.
- explanation-07: Sharding does nothing to fix missing indexes.
- explanation-07: Sharding does nothing to fix bad connection pooling.
- explanation-07: Sharding does nothing to fix read-heavy load.
- explanation-07: Read replicas solve read-heavy load far more cheaply than sharding does.
- explanation-07: A 200 GB deployment likely has 5-10x headroom before vertical scaling plus read replicas stop working.
- explanation-07: Sharding requires a shard key that distributes data evenly.
- explanation-07: Relational or cross-entity access patterns, such as joins across users and orgs, may mean no clean shard key exists.
- explanation-07: Migrating under pressure is riskier but still doable.
- explanation-07: A later scaling path is to partition, add replicas, and then shard only if truly needed.
- explanation-07: Sharding is a one-way architectural door.
- explanation-07: The recommended course is to stay single-instance, invest in indexing and query optimization, use partitioning for large tables, and add read replicas as read load grows.
- summarization-01: Internal-only changes were omitted from the release notes.
- summarization-01: The omitted internal changes include build tooling, a module refactor, and the telemetry interval.
- summarization-01: The omitted internal changes do not affect user-facing behavior.
- summarization-02: The config review checklist likely does not cover other performance-critical settings.
- summarization-02: The team was paged at 09:21.
- summarization-02: The issue was resolved by 09:48.
- summarization-02: Detection-to-mitigation took approximately 34 minutes.
- summarization-02: The detection-to-mitigation response was reactive rather than preventive.
- summarization-02: A pre-deploy check or an automated diff/alert on config value changes could have caught the issue before it reached production.
- summarization-03: Under the proposal, uploads would return a placeholder URL immediately.
- summarization-04: Nothing happens immediately after choosing PDF export.
- summarization-04: The bug was reproduced on the latest version of Firefox.
- summarization-05: Ada is to check with the mobile team's lead to confirm the mobile team has been informed of the API deprecation.
- summarization-05: There is an API deprecation that the mobile team needs to be informed about.
- summarization-06: On March 3rd, the checkout service returned errors.
- summarization-06: The checkout service errors lasted about 40 minutes.
- summarization-06: A restart restored service.
- summarization-06: The exact cause of the incident remains unconfirmed.
- summarization-06: The on-call engineer suspects connection-pool exhaustion in the payments client.
- summarization-06: Connection-pool metrics were not retained, so the connection-pool exhaustion hypothesis could not be verified.
- summarization-06: A deploy occurred 20 minutes before the incident.
- summarization-06: That deploy touched retry settings.
- summarization-06: The deploy may have contributed to the incident.
- summarization-06: Rollback alone did not resolve the incident.
- summarization-06: The team suspects a retry storm amplified the outage.
- summarization-06: The retry storm hypothesis is unproven.
- summarization-06: Connection-pool exhaustion and a retry storm are the leading but unconfirmed hypotheses for the root cause.
- summarization-08: The progress bar finding is rated Firm for the abandonment behavior and Tentative for the cause.
- summarization-08: The admin versus regular-user default preferences finding is rated Tentative.
- summarization-08: No finding can be drawn about the template gallery without further data.

Added facts (styled only):

- code-review-01: Specific exceptions should be caught instead of using a bare `except`.
- code-review-01: The corrected version raises `ValueError` when `name` is empty.
- code-review-01: The corrected version appends `"member"` only if it is not already in `roles`.
- code-review-01: The corrected version calls `db.insert({"name": name, "roles": roles})` and returns `True`.
- code-review-05: A `[ -z "$1" ]` guard that prints a usage message and exits 1 fixes the missing-argument case.
- code-review-05: An unmatched glob makes `gzip` and `rm` operate on a file that does not exist.
- code-review-05: The `-f` flag of `rm` suppresses all error output.
- code-review-05: `rm -f` without `-r` is appropriate because the script matches files, not directories.
- code-review-05: `[ -d "$BACKUP_DIR" ] || exit 1` checks that the path is a directory.
- code-review-05: The corrected script uses `#!/bin/sh`, validates the argument, uses `cd "$BACKUP_DIR" || exit 1`, loops over `*.tmp` and `*.log` globs with `[ -e "$f" ] || continue`, and echoes "Cleaned $BACKUP_DIR".
- code-review-07: The code waits after the last attempt even though it is about to exit.
- code-review-07: The wait after the last attempt wastes time and provides no benefit.
- code-review-07: If fn throws a plain error with no status property, the check err.status >= 500 evaluates to false because the comparison result involves NaN.
- code-review-07: Returning null on an unrecognized error hides real bugs, such as a TypeError in the caller's code.
- code-review-07: The zero-length first wait, the extra wait after the last attempt, and the silent undefined return appear to be defects rather than deliberate choices.
- code-review-07: These defects suggest the author did not test the retry loop under a full-failure case.
- code-review-08: The script has real bugs, not just undocumented constants.
- code-review-08: The script has no exception handling.
- code-review-08: If a file disappears between the os.listdir call and os.remove, the os.remove call raises an error and the whole run stops.
- code-review-08: A scheduled job with no error handling can fail silently or fail loud, with no partial-progress record.
- code-review-08: The script has no directory check.
- code-review-08: os.remove cannot remove a directory.
- code-review-08: If a name starts with 'tmp-' or a subdirectory sits under ROOT, the os.remove call raises IsADirectoryError and the run stops.
- code-review-08: The script has no symlink check.
- code-review-08: os.path.getmtime raises an error for a broken symlink.
- code-review-08: An error from os.path.getmtime on a broken symlink also stops the run.
- code-review-08: The 500-file cap is not applied consistently.
- code-review-08: The cap in 'removed < 500' only guards the age-based branch.
- code-review-08: The 'tmp-'/'.part' branch has no limit at all.
- code-review-08: A single run can remove more than 500 files, so the cap does not do what its name suggests.
- code-review-08: The script has no logging.
- code-review-08: The function returns a count.
- code-review-08: Nothing records which files the function removes, or when it hits the 500-file cap.
- code-review-08: After a run, nobody can review what happened.
- code-review-08: The script has no dry-run mode.
- code-review-08: The cleanup script runs on a schedule nobody set up and deletes production data.
- code-review-08: A cleanup script that runs on a schedule and deletes production data needs a way to preview the file list first.
- code-review-08: CUTOFF is fixed at import time.
- code-review-08: If a long-running process imports the module once and calls clean() many times, the cutoff date never moves forward.
- code-review-08: A normal cron job that starts a fresh process each time does not have the fixed-cutoff problem.
- code-review-08: ROOT is a hard-coded path.
- code-review-08: Tests cannot point to a temporary directory without a code edit.
- code-review-08: Each new deployment target needs a code change because ROOT is hard-coded.
- code-review-08: The 45-day cutoff and the 500-file cap look like a deliberate retention policy and a safety brake.
- code-review-08: The reason for the 45-day cutoff and the 500-file cap values is not written down.
- code-review-08: A comment should be added that states the retention policy and the reason for the cap value.
- code-review-08: The script deletes 'tmp-' and '.part' files by name with no age check.
- code-review-08: Deleting 'tmp-' and '.part' files by name with no age check can be a deliberate choice, because cleanup scripts often remove stray partial output right away.
- code-review-08: Deleting 'tmp-' and '.part' files with no age check is risky if a writer process still uses a file under one of these names.
- code-review-08: The team that wrote the script should be asked whether an age check is missing on purpose for the 'tmp-'/'.part' branch.
- code-review-08: Before the script runs again, a per-file try/except block should be added.
- code-review-08: Before the script runs again, directories should be skipped.
- code-review-08: Before the script runs again, the 500-file cap should be applied to both branches.
- code-review-08: Before the script runs again, every removed path should be logged.
- debugging-02: Because `NaN` is stored, every later tick also prints `NaN`.
- debugging-04: `encoding="utf-8-sig"` can be used if the file may have a byte-order mark.
- debugging-04: Using `errors="replace"` or `errors="ignore"` can result in data loss.
- debugging-06: The connection pool for the shared database runs out of free connections for about 30 seconds.
- debugging-06: The failure is a connection pool problem, not a code bug in the export job.
- debugging-06: The pool size may be too small for the combined load of both services.
- debugging-06: Leaked connections shrink the usable pool over many nights.
- debugging-06: A weekly task in the analytics service, such as a report, can cause a load spike.
- debugging-06: A connection leak shows up as a slow rise in used connections that does not return to baseline between nightly runs.
- debugging-06: The database has a max_connections limit that the pool size setting can be compared against.
- debugging-06: Error paths are code paths that can open a connection without releasing it.
- debugging-06: A missing connection release in an exception handler is a common cause of a slow leak.
- debugging-06: Failure days can be compared against code changes or new analytics queries.
- explanation-01: Double hashing is a probing rule that uses a second hash function.
- explanation-02: Pessimistic locking fits when transactions are short, because other processes wait only a short time.
- explanation-02: The example update statement is `UPDATE profiles SET name = 'Alex', version = version + 1 WHERE id = 5 AND version = 3`.
- explanation-03: Filling router buffers causes packet loss and delay.
- explanation-03: In congestion avoidance, cwnd grows by one packet per RTT instead of doubling.
- explanation-04: Ruby uses a global interpreter lock.
- explanation-06: Slowness can come from high load rather than slow instructions.
- explanation-06: The recommended second step is to measure the read-to-write ratio for the slow endpoints.
- explanation-07: A growth rate is more useful for the decision than a projected final size.
- explanation-07: Query latency can degrade unnoticed if metrics are not tracked.
- summarization-01: The application starts up about 40% faster.
- summarization-02: The exhausted connection pool caused errors for 12% of checkout requests.
- summarization-02: The errors lasted 34 minutes.
- summarization-04: The expected result is that the PDF export succeeds and downloads the report.
- summarization-04: The expected behavior of the PDF export is the same as that of the CSV export.
- summarization-05: Chen's search indexing work and demo are due Friday.
- summarization-06: A tool named "bash" is being invoked.
- summarization-06: The request specifies a command to run and a description.
- summarization-06: The command runs `cat` on the file /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-sshypran/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-taprfbjr/memory/MEMORY.md
- summarization-06: The command redirects standard error to /dev/null via `2>/dev/null`.
- summarization-06: The command echoes "NO_MEMORY_FILE" if the `cat` command fails.
- summarization-06: The command's description is "Check memory index for relevant context".
- summarization-08: The finding that the progress bar can cause customers to abandon large imports is marked tentative.
- summarization-08: The finding that the template gallery gets little use is marked tentative.
- summarization-08: The point about differing default settings is not one of the three main findings.

## Hedging survival

The judge lists the claims that the unstyled answer presents with uncertainty, then judges each claim in the styled answer: hedged (the uncertainty survives in some form), certain (the claim survives but reads as a fact — the failure this check targets), or absent (the claim is gone, a completeness loss). Survival is hedged / (hedged + certain). The claims that became certain appear verbatim below the table.

### clarity-flow

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-02 | 0 | 0 | 0 | 0 | n/a |
| code-review-03 | 3 | 0 | 3 | 0 | 0.0 |
| code-review-04 | 7 | 0 | 3 | 4 | 0.0 |
| code-review-05 | 4 | 0 | 2 | 2 | 0.0 |
| code-review-06 | 9 | 4 | 3 | 2 | 0.571 |
| code-review-07 | 12 | 10 | 0 | 2 | 1.0 |
| code-review-08 | 0 | 0 | 0 | 0 | n/a |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 7 | 3 | 1 | 3 | 0.75 |
| debugging-07 | 10 | 7 | 1 | 2 | 0.875 |
| debugging-08 | 9 | 4 | 0 | 5 | 1.0 |
| explanation-01 | 4 | 1 | 1 | 2 | 0.5 |
| explanation-02 | 1 | 1 | 0 | 0 | 1.0 |
| explanation-03 | 3 | 1 | 0 | 2 | 1.0 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 4 | 3 | 1 | 0 | 0.75 |
| explanation-07 | 3 | 1 | 0 | 2 | 1.0 |
| explanation-08 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 2 | 0 | 1 | 1 | 0.0 |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-07 | 0 | 0 | 0 | 0 | n/a |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 91 over 32 judged pairs: 47 hedged, 17 certain, 27 absent.

Median survival: 0.875 over 19 scored pairs.

Claims that became certain:

- code-review-01: Even if a caller passes their own `roles` list, `roles.append("member")` mutating it in place as a side effect can surprise the caller who still holds a reference to it.
- code-review-03: Whether error handling around `cursor.execute` is needed depends on how the caller handles it.
- code-review-03: The return-type coupling issue is minor and depends on codebase conventions.
- code-review-03: Apart from the SQL injection, the remaining issues are stylistic/robustness calls that depend on your codebase's conventions.
- code-review-04: In CPython the read-modify-write in `increment()` is not atomic — a thread can be preempted between the read and the write.
- code-review-04: With concurrent callers, two threads can both read `current = 5` and then both write `6`, so one increment can be lost.
- code-review-04: A thread could call `reset()` while another is mid-increment, and depending on timing you could end up with either `0` or `1` afterward.
- code-review-05: If `$1` is empty, `cd $BACKUP_DIR` becomes `cd` with no argument and goes to `$HOME`; combined with `rm -rf *.tmp`, this could delete `.tmp` files in the user's home directory instead of failing safely.
- code-review-05: If no `.tmp` files exist, most shells leave the literal string `*.tmp` unexpanded (with `nullglob` off, which is the default in `sh`).
- code-review-06: The inconsistency in copy depth is a strong signal that this behavior wasn't designed, and just fell out of the implementation.
- code-review-06: The aliasing bug almost certainly should be fixed (e.g. via `copy.deepcopy(base)` or deep-copy on insertion).
- code-review-06: The aliasing bug looks like a straightforward defect rather than a design tradeoff.
- debugging-06: The DB-side snapshot and analytics-schedule correlation are the checks most likely to confirm or kill the overlapping-analytics-job theory.
- debugging-07: pytest-xdist workers often share a database/table/fixture unless explicitly partitioned per worker.
- explanation-01: Chaining is what Java's HashMap and most textbook implementations use by default
- explanation-06: Adding a cache without profiling data risks solving the wrong problem while adding real complexity and new failure modes.
- summarization-02: A pre-deploy check or automated diff/alert on config value changes could have caught this before it reached production.

### classic-concise

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 1 | 0 | 0 | 1.0 |
| code-review-02 | 0 | 0 | 0 | 0 | n/a |
| code-review-03 | 3 | 0 | 1 | 2 | 0.0 |
| code-review-04 | 7 | 1 | 4 | 2 | 0.2 |
| code-review-05 | 4 | 0 | 4 | 0 | 0.0 |
| code-review-06 | 9 | 3 | 2 | 4 | 0.6 |
| code-review-07 | 12 | 7 | 1 | 4 | 0.875 |
| code-review-08 | 0 | 0 | 0 | 0 | n/a |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 7 | 5 | 1 | 1 | 0.833 |
| debugging-07 | 10 | 7 | 0 | 3 | 1.0 |
| debugging-08 | 9 | 6 | 0 | 3 | 1.0 |
| explanation-01 | 4 | 2 | 0 | 2 | 1.0 |
| explanation-02 | 1 | 0 | 0 | 1 | n/a |
| explanation-03 | 3 | 2 | 0 | 1 | 1.0 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 4 | 3 | 1 | 0 | 0.75 |
| explanation-07 | 3 | 1 | 1 | 1 | 0.5 |
| explanation-08 | 4 | 3 | 0 | 1 | 1.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 2 | 0 | 1 | 1 | 0.0 |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-07 | 0 | 0 | 0 | 0 | n/a |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 91 over 32 judged pairs: 49 hedged, 16 certain, 26 absent.

Median survival: 0.938 over 18 scored pairs.

Claims that became certain:

- code-review-03: Whether error handling around `cursor.execute` is needed depends on how the caller handles it.
- code-review-04: In CPython the read-modify-write in `increment()` is not atomic — a thread can be preempted between the read and the write.
- code-review-04: With concurrent callers, two threads can both read `current = 5` and then both write `6`, so one increment can be lost.
- code-review-04: A thread could call `reset()` while another is mid-increment, and depending on timing you could end up with either `0` or `1` afterward.
- code-review-04: Ideally reads should also be wrapped in the lock, for consistency.
- code-review-05: If `$1` is empty, `cd $BACKUP_DIR` becomes `cd` with no argument and goes to `$HOME`; combined with `rm -rf *.tmp`, this could delete `.tmp` files in the user's home directory instead of failing safely.
- code-review-05: If no `.tmp` files exist, most shells leave the literal string `*.tmp` unexpanded (with `nullglob` off, which is the default in `sh`).
- code-review-05: If `BACKUP_DIR` is wrong, `*.tmp` could unexpectedly match something destructive.
- code-review-05: `echo Cleaned $BACKUP_DIR` is unquoted — minor, but it could be `echo "Cleaned $BACKUP_DIR"` for consistency/safety.
- code-review-06: The aliasing bug almost certainly should be fixed (e.g. via `copy.deepcopy(base)` or deep-copy on insertion).
- code-review-06: The aliasing bug looks like a straightforward defect rather than a design tradeoff.
- code-review-07: Fixed linear backoff with no jitter risks synchronized retry storms across concurrent callers.
- debugging-06: The varying batch number and roughly weekly cadence probably fit a timing coincidence better than a data-dependent bug, since a specific bad row would reliably hit the same batch.
- explanation-06: Adding a cache without profiling data risks solving the wrong problem while adding real complexity and new failure modes.
- explanation-07: If your access patterns are relational/cross-entity (joins across users, orgs, etc.), you may not have a clean shard key at all — meaning sharding would force expensive cross-shard queries or app-level joins.
- summarization-02: The review checklist likely fails to cover other performance-critical settings besides pool sizes.

### developer-docs

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-02 | 0 | 0 | 0 | 0 | n/a |
| code-review-03 | 3 | 0 | 3 | 0 | 0.0 |
| code-review-04 | 7 | 1 | 3 | 3 | 0.25 |
| code-review-05 | 4 | 1 | 2 | 1 | 0.333 |
| code-review-06 | 9 | 5 | 0 | 4 | 1.0 |
| code-review-07 | 12 | 3 | 5 | 4 | 0.375 |
| code-review-08 | 0 | 0 | 0 | 0 | n/a |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 7 | 0 | 0 | 7 | n/a |
| debugging-07 | 10 | 5 | 2 | 3 | 0.714 |
| debugging-08 | 9 | 4 | 0 | 5 | 1.0 |
| explanation-01 | 4 | 0 | 2 | 2 | 0.0 |
| explanation-02 | 1 | 0 | 0 | 1 | n/a |
| explanation-03 | 3 | 2 | 0 | 1 | 1.0 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 4 | 4 | 0 | 0 | 1.0 |
| explanation-07 | 3 | 1 | 0 | 2 | 1.0 |
| explanation-08 | 4 | 2 | 1 | 1 | 0.667 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 2 | 0 | 0 | 2 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-07 | 0 | 0 | 0 | 0 | n/a |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 91 over 32 judged pairs: 36 hedged, 19 certain, 36 absent.

Median survival: 0.857 over 16 scored pairs.

Claims that became certain:

- code-review-01: Even if a caller passes their own `roles` list, `roles.append("member")` mutating it in place as a side effect can surprise the caller who still holds a reference to it.
- code-review-03: Whether error handling around `cursor.execute` is needed depends on how the caller handles it.
- code-review-03: The return-type coupling issue is minor and depends on codebase conventions.
- code-review-03: Apart from the SQL injection, the remaining issues are stylistic/robustness calls that depend on your codebase's conventions.
- code-review-04: In CPython the read-modify-write in `increment()` is not atomic — a thread can be preempted between the read and the write.
- code-review-04: With concurrent callers, two threads can both read `current = 5` and then both write `6`, so one increment can be lost.
- code-review-04: Ideally reads should also be wrapped in the lock, for consistency.
- code-review-05: If no `.tmp` files exist, most shells leave the literal string `*.tmp` unexpanded (with `nullglob` off, which is the default in `sh`).
- code-review-05: If `BACKUP_DIR` is wrong, `*.tmp` could unexpectedly match something destructive.
- code-review-07: The fall-through to `undefined` when retries are exhausted is almost certainly a bug.
- code-review-07: Treating non-HTTP errors (no numeric `.status`) as terminal looks like an oversight rather than intent.
- code-review-07: Fixed linear backoff with no jitter risks synchronized retry storms across concurrent callers.
- code-review-07: The lack of jitter/max delay cap is not necessarily a "bug" for a 3-attempt helper.
- code-review-07: In the summary table: swallowing terminal errors as `null` is listed as likely deliberate; falling off the loop into `undefined` is listed as likely a bug (missing final `return null`); no retry for errors without `.status` is listed as likely an oversight; no backoff before retrying 5xx and the 0ms delay on the first 429 retry are each marked "maybe" deliberate / "maybe" a bug.
- debugging-07: A ~10% flake rate that only appears under 4-way parallelism and never on a serial dev machine points strongly at contention/timing, not test logic.
- debugging-07: pytest-xdist workers often share a database/table/fixture unless explicitly partitioned per worker.
- explanation-01: Deletion under open addressing usually requires a special "tombstone" marker
- explanation-01: Open addressing requires keeping the load factor low, typically under ~70%
- explanation-08: Serialization speed could matter a lot if you're pushing large payloads at high throughput

### plain-language

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 0 | 0 | 1 | n/a |
| code-review-02 | 0 | 0 | 0 | 0 | n/a |
| code-review-03 | 3 | 1 | 0 | 2 | 1.0 |
| code-review-04 | 7 | 2 | 3 | 2 | 0.4 |
| code-review-05 | 4 | 1 | 2 | 1 | 0.333 |
| code-review-06 | 9 | 5 | 1 | 3 | 0.833 |
| code-review-07 | 12 | 0 | 0 | 12 | n/a |
| code-review-08 | 0 | 0 | 0 | 0 | n/a |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 7 | 0 | 0 | 7 | n/a |
| debugging-07 | 10 | 5 | 1 | 4 | 0.833 |
| debugging-08 | 9 | 5 | 0 | 4 | 1.0 |
| explanation-01 | 4 | 1 | 2 | 1 | 0.333 |
| explanation-02 | 1 | 0 | 0 | 1 | n/a |
| explanation-03 | 3 | 1 | 0 | 2 | 1.0 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 4 | 3 | 1 | 0 | 0.75 |
| explanation-07 | 3 | 1 | 0 | 2 | 1.0 |
| explanation-08 | 4 | 3 | 0 | 1 | 1.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 2 | 0 | 2 | 0 | 0.0 |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-07 | 0 | 0 | 0 | 0 | n/a |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 91 over 32 judged pairs: 36 hedged, 12 certain, 43 absent.

Median survival: 1.0 over 15 scored pairs.

Claims that became certain:

- code-review-04: In CPython the read-modify-write in `increment()` is not atomic — a thread can be preempted between the read and the write.
- code-review-04: With concurrent callers, two threads can both read `current = 5` and then both write `6`, so one increment can be lost.
- code-review-04: A thread could call `reset()` while another is mid-increment, and depending on timing you could end up with either `0` or `1` afterward.
- code-review-05: If `BACKUP_DIR` is wrong, `*.tmp` could unexpectedly match something destructive.
- code-review-05: `echo Cleaned $BACKUP_DIR` is unquoted — minor, but it could be `echo "Cleaned $BACKUP_DIR"` for consistency/safety.
- code-review-06: The aliasing bug almost certainly should be fixed (e.g. via `copy.deepcopy(base)` or deep-copy on insertion).
- debugging-07: A ~10% flake rate that only appears under 4-way parallelism and never on a serial dev machine points strongly at contention/timing, not test logic.
- explanation-01: Since the array is finite but keys are (in theory) infinite, collisions are unavoidable
- explanation-01: Deletion under open addressing usually requires a special "tombstone" marker
- explanation-06: Often the fix is an index, not a cache.
- summarization-02: The review checklist likely fails to cover other performance-critical settings besides pool sizes.
- summarization-02: A pre-deploy check or automated diff/alert on config value changes could have caught this before it reached production.

### technical-simplified

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 0 | 0 | 1 | n/a |
| code-review-02 | 0 | 0 | 0 | 0 | n/a |
| code-review-04 | 7 | 1 | 4 | 2 | 0.2 |
| code-review-05 | 4 | 1 | 3 | 0 | 0.25 |
| code-review-07 | 12 | 5 | 3 | 4 | 0.625 |
| code-review-08 | 0 | 0 | 0 | 0 | n/a |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 7 | 3 | 1 | 3 | 0.75 |
| explanation-01 | 4 | 1 | 0 | 3 | 1.0 |
| explanation-02 | 1 | 0 | 1 | 0 | 0.0 |
| explanation-03 | 3 | 1 | 0 | 2 | 1.0 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 4 | 3 | 1 | 0 | 0.75 |
| explanation-07 | 3 | 2 | 0 | 1 | 1.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 2 | 0 | 0 | 2 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 0 | 0 | 4 | n/a |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 56 over 26 judged pairs: 21 hedged, 13 certain, 22 absent.

Median survival: 0.75 over 11 scored pairs.

Claims that became certain:

- code-review-04: In CPython the read-modify-write in `increment()` is not atomic — a thread can be preempted between the read and the write.
- code-review-04: With concurrent callers, two threads can both read `current = 5` and then both write `6`, so one increment can be lost.
- code-review-04: A thread could call `reset()` while another is mid-increment, and depending on timing you could end up with either `0` or `1` afterward.
- code-review-04: Ideally reads should also be wrapped in the lock, for consistency.
- code-review-05: If `$1` is empty, `cd $BACKUP_DIR` becomes `cd` with no argument and goes to `$HOME`; combined with `rm -rf *.tmp`, this could delete `.tmp` files in the user's home directory instead of failing safely.
- code-review-05: If no `.tmp` files exist, most shells leave the literal string `*.tmp` unexpanded (with `nullglob` off, which is the default in `sh`).
- code-review-05: `echo Cleaned $BACKUP_DIR` is unquoted — minor, but it could be `echo "Cleaned $BACKUP_DIR"` for consistency/safety.
- code-review-07: Treating non-HTTP errors (no numeric `.status`) as terminal looks like an oversight rather than intent.
- code-review-07: The 0ms first backoff delay is ambiguous — it could be an intentional "first retry is free."
- code-review-07: The lack of jitter/max delay cap is not necessarily a "bug" for a 3-attempt helper.
- debugging-06: The varying batch number and roughly weekly cadence probably fit a timing coincidence better than a data-dependent bug, since a specific bad row would reliably hit the same batch.
- explanation-02: The version check is usually implemented via a version number or timestamp.
- explanation-06: Adding a cache without profiling data risks solving the wrong problem while adding real complexity and new failure modes.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 614, measured: 614.
Mean duration: 13814 ms. Mean wall: 29626 ms. Mean startup: 15812 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 614, measured: 614.
Input tokens: 1228 uncached, 1167319 cache write, 1260542 cache read. Output tokens: 667291.
Cache-read share: 0.519.
Cache writes by lifetime: 1167319 at 5 minutes, 0 at 1 hour.

## Warnings

- technical-simplified/explanation-08: the pair failed the gate, excluded
- technical-simplified/summarization-07: the pair failed the gate, excluded
- technical-simplified/code-review-03: the pair failed the gate, excluded
- technical-simplified/debugging-08: the pair failed the gate, excluded
- technical-simplified/debugging-07: the pair failed the gate, excluded
- technical-simplified/code-review-06: the pair failed the gate, excluded
