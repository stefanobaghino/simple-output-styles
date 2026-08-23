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

Judge: opus. Judged on 2026-08-22T09:32:02+00:00.

## Completeness (fact survival)

The judge lists the facts of the unstyled answer, then checks each fact against the styled answer. The fraction is the share of the facts that survive. The judge also lists the facts of the styled answer and checks each fact against the unstyled answer: a styled fact that the unstyled answer does not state is an addition. The lost facts and the added facts appear verbatim below the table.

### actionable-clarity

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 31 | 25 | 0.806 | 31 | 6 |
| code-review-02 | 18 | 15 | 0.833 | 25 | 4 |
| code-review-03 | 28 | 17 | 0.607 | 23 | 5 |
| code-review-04 | 24 | 19 | 0.792 | 23 | 7 |
| code-review-05 | 32 | 22 | 0.688 | 44 | 10 |
| code-review-06 | 43 | 32 | 0.744 | 35 | 7 |
| code-review-07 | 56 | 43 | 0.768 | 40 | 11 |
| code-review-08 | 54 | 43 | 0.796 | 42 | 9 |
| debugging-01 | 6 | 6 | 1.0 | 7 | 0 |
| debugging-02 | 14 | 10 | 0.714 | 11 | 0 |
| debugging-03 | 12 | 12 | 1.0 | 9 | 1 |
| debugging-04 | 15 | 9 | 0.6 | 14 | 1 |
| debugging-05 | 15 | 14 | 0.933 | 16 | 0 |
| debugging-06 | 24 | 16 | 0.667 | 26 | 5 |
| debugging-07 | 30 | 17 | 0.567 | 40 | 21 |
| debugging-08 | 50 | 19 | 0.38 | 45 | 15 |
| explanation-01 | 43 | 28 | 0.651 | 38 | 6 |
| explanation-02 | 28 | 19 | 0.679 | 31 | 12 |
| explanation-03 | 38 | 30 | 0.789 | 31 | 4 |
| explanation-04 | 41 | 30 | 0.732 | 34 | 0 |
| explanation-05 | 19 | 14 | 0.737 | 20 | 2 |
| explanation-06 | 32 | 18 | 0.562 | 32 | 10 |
| explanation-07 | 28 | 22 | 0.786 | 39 | 15 |
| explanation-08 | 15 | 7 | 0.467 | 17 | 9 |
| summarization-01 | 5 | 5 | 1.0 | 10 | 5 |
| summarization-02 | 14 | 13 | 0.929 | 15 | 5 |
| summarization-03 | 13 | 11 | 0.846 | 12 | 3 |
| summarization-04 | 16 | 12 | 0.75 | 19 | 5 |
| summarization-05 | 8 | 8 | 1.0 | 11 | 1 |
| summarization-06 | 12 | 12 | 1.0 | 13 | 1 |
| summarization-07 | 18 | 16 | 0.889 | 14 | 0 |
| summarization-08 | 19 | 15 | 0.789 | 20 | 3 |

Median fraction: 0.777 over 32 scored pairs.

Median additions: 5.0 over 32 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python pitfall.
- code-review-01: The function does not check whether `"member"` is already in `roles`.
- code-review-01: If `roles` already contains `"member"`, it gets added a second time.
- code-review-01: The fixed version uses `roles = list(roles) if roles else []`.
- code-review-01: The fixed version appends `"member"` only if it is not already in `roles`.
- code-review-01: The fixed version prevents duplicate roles.
- code-review-02: The code does not validate that `data` has a `name` property.
- code-review-02: If the API returns an unexpected value such as an error object, `.name` could be `undefined` and `.toUpperCase()` would throw.
- code-review-02: The fixed version removes the unused `profile` variable and the unused promise chain.
- code-review-03: If `customer_name` or `status` is not a string (e.g. `None`), the `+` concatenation raises a `TypeError`.
- code-review-03: The resulting `TypeError` produces a confusing stack trace rather than a clear error.
- code-review-03: The function has no error handling.
- code-review-03: `cursor.execute` can raise exceptions, such as from a bad connection or a lock timeout.
- code-review-03: Exceptions from `cursor.execute` propagate with no context added.
- code-review-03: Whether the lack of error handling is acceptable depends on the application's conventions.
- code-review-03: It is worth considering whether callers expect a wrapped or logged exception.
- code-review-03: The function has no pagination or limit.
- code-review-03: The function could return unbounded result sets on a wildcard-like match.
- code-review-03: The lack of pagination is more of a design consideration than a bug.
- code-review-03: The SQL injection issue is the only problem that actually needs fixing.
- code-review-04: The lost-update bug is a classic TOCTOU/lost-update bug.
- code-review-04: The race condition gets worse under load.
- code-review-04: The window between the read and the write is exactly when a context switch is likely.
- code-review-04: The assignment `self.value = 0` is a single bytecode-level store.
- code-review-04: PyPy has an STM mode.
- code-review-05: If $1 is empty, `cd $BACKUP_DIR` becomes a bare `cd`, which changes to $HOME.
- code-review-05: If the script cds to $HOME, `rm -rf *.tmp` deletes .tmp files from the home directory instead of failing.
- code-review-05: If no .log files exist, `*.log` will not expand unless `nullglob` is set.
- code-review-05: `nullglob` is not available in POSIX sh.
- code-review-05: If no .log files exist, `ls *.log` prints an error to stderr.
- code-review-05: The script has no argument count check and should verify `$#` before proceeding.
- code-review-05: The script does not check that BACKUP_DIR is actually a directory before running `cd`.
- code-review-05: The script lacks `set -u`, which would have caught the empty-$1 problem.
- code-review-05: The suggested rewrite exits with status 1 and a usage message on stderr when `$#` is not 1.
- code-review-05: The suggested rewrite exits with status 1 and an error message on stderr when BACKUP_DIR is not a directory.
- code-review-06: Recursive merging of a key produces no aliasing.
- code-review-06: Deletion via None only works when merging into a dict that already exists at that key.
- code-review-06: None values inside a newly-introduced nested dict are stored literally instead of being treated as deletions.
- code-review-06: The None sentinel means different things depending on whether the key already existed as a dict.
- code-review-06: Recursive merging applies only to `dict`, not to other mapping types.
- code-review-06: Custom Mapping subclasses and OrderedDict are examples of types not merged recursively.
- code-review-06: The `isinstance(..., dict)` check is strict rather than duck-typed.
- code-review-06: The function always returns a plain dict.
- code-review-06: If base is a dict subclass, subclass-specific behavior is lost in the return value.
- code-review-06: The function has no docstring and no type hints.
- code-review-06: The shallow-copy sharing and the asymmetric nested None deletion are subtler correctness traps that should at least be documented.
- code-review-07: Any non-retryable error, including 4xx other than 429 and exhausted retries, is converted into a null return rather than propagated.
- code-review-07: A caller that awaits withRetry(fn)() and dereferences the result without a null check will get a confusing downstream error far from the real cause.
- code-review-07: The attempts parameter counts total tries rather than retries.
- code-review-07: A default attempts of 3 means fn is called at most 3 times total, not 3 retries after an original attempt.
- code-review-07: The attempts naming ambiguity is not a bug per se.
- code-review-07: The attempts semantics are worth confirming with any caller who tuned the value expecting different semantics.
- code-review-07: The lack of cap and jitter likely never mattered because the default attempts is 3.
- code-review-07: The code loses this binding.
- code-review-07: The wrapped function is invoked as fn(...args) and is not bound to any receiver.
- code-review-07: If a hidden caller wrapped an object method expecting this to refer to the object, it will break silently or throw.
- code-review-07: An error thrown from a lost this binding would itself be swallowed by the null-returning and status-assumption behavior.
- code-review-07: Distinguishing 429 (retry with delay) from other 4xx (don't retry) is likely deliberate.
- code-review-07: The accidental issues resemble logic slips from editing retry logic without re-testing all branches.
- code-review-08: os.path.getmtime works on directories.
- code-review-08: An aborted run produces only a traceback, visible if run interactively.
- code-review-08: Deleting oldest first would require sorting by mtime.
- code-review-08: os.remove unlinks the symlink itself rather than the target.
- code-review-08: The unconditional tmp/part deletion is very likely not deliberate.
- code-review-08: The constants have no comments, no config, and no environment variable override.
- code-review-08: The 45-day and 500 values were previously flagged by the user as magic numbers with no rationale.
- code-review-08: The 45-day value may be tied to a legal retention policy.
- code-review-08: As written, the constants are indistinguishable from arbitrary defaults.
- code-review-08: A dry-run mode is standard practice for scheduled deletion scripts.
- code-review-08: Without a dry-run mode, behavior cannot be safely tested in production without risking real deletions.
- debugging-02: The NaN value produced is what gets logged to the console.
- debugging-02: The incremented value is assigned onto the global object rather than the Timer instance.
- debugging-02: Calling .bind(this) on a regular function callback is an alternative fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` inside it is an alternative fix.
- debugging-04: The file contains a non-ASCII byte 0xc3 at byte 512.
- debugging-04: UTF-8 is the most common encoding to use for such files.
- debugging-04: Using errors="replace" can mangle unusual characters.
- debugging-04: Mangling characters is acceptable if only line counts matter rather than content.
- debugging-04: The libraries chardet and charset-normalizer can detect a file's encoding.
- debugging-04: Counting b"\n" bytes in binary mode counts lines without decoding.
- debugging-05: The fixed make_post sets tags to list(DEFAULT_TAGS) when tags is None.
- debugging-06: A connection leak in the export job's retry path is a plausible cause.
- debugging-06: The export job's timeout and exception paths should be audited to confirm they always return the connection.
- debugging-06: Another nightly cron job scheduled near 02:14 UTC could be overlapping with the export job.
- debugging-06: Pool-utilization metrics worth adding include in-use count, wait queue depth, and wait time.
- debugging-06: Continuous pool-utilization metrics show whether the problem is a slow leak or a sudden spike.
- debugging-06: Summing all services' maximum pool sizes and comparing that total against the database's max_connections checks for oversubscription.
- debugging-06: Setting an alert on pool wait time or queue depth at a threshold below the 30s timeout would page someone with full context during the next occurrence.
- debugging-06: The relevant log fragment for the failure was lost to log rotation.
- debugging-07: A read-after-write race on an async pipeline is the most common cause of flakes where a count is short by exactly one.
- debugging-07: GC pauses, container throttling, and noisy neighbors can starve a CI machine.
- debugging-07: pytest includes a custom assertion message in the failure log even without artifact storage.
- debugging-07: `pytest -n 4 --count 200` combines pytest-xdist with pytest-repeat.
- debugging-07: If the test only flakes when the full suite runs, shared fixture or account contamination from other tests is the likely cause rather than a bug in the test in isolation.
- debugging-07: `-k test_digest_contains_all_events` filters a pytest run to a single test while still collecting the rest of the suite.
- debugging-07: If adding a short poll/retry loop before reading the digest makes the flake disappear, that strongly indicates an async or eventual-consistency race rather than a data-isolation bug.
- debugging-07: Per-test isolation can be achieved with `uuid4()` IDs or freezegun-style time control instead of hardcoded constants.
- debugging-07: If the user/org ID and time window are shared constants, the correct fix is fixture isolation rather than retries.
- debugging-07: Under READ COMMITTED isolation, when the app writes on a different connection or transaction than the test's setup, stale reads can occur and be worsened by connection pool pressure from four workers.
- debugging-07: Logging seed results and digest contents on failure, combined with testing whether a poll/retry removes the flake, gives the fastest diagnostic signal.
- debugging-07: That combination can distinguish a race condition from a shared-state isolation bug within one or two CI flakes.
- debugging-07: A race condition and a shared-state isolation bug require different fixes: adding a read-your-writes guarantee versus isolating test fixtures.
- debugging-08: Memory growth that survives quiet nights rules out normal cache/GC churn.
- debugging-08: True garbage gets collected regardless of load.
- debugging-08: Growth that survives quiet nights points to objects still reachable from live roots, indicating an actual leak rather than mere heap pressure.
- debugging-08: A bounded cache with an unchanged bound and no code changes in a year is a less likely root cause.
- debugging-08: Eviction bugs are possible even in code that has not changed in a long time.
- debugging-08: The most likely hypothesis is a reference leak outside the cache.
- debugging-08: ThreadLocal or MDC context leaking on pooled threads is a possible reference leak source.
- debugging-08: A reference leak explains why quiet nights do not recover memory, because the objects are held by real GC roots.
- debugging-08: A reference leak explains why the canary still grows slowly, because its own scheduled or background traffic hits the same code path.
- debugging-08: `jcmd <pid> GC.class_histogram` produces a heap class histogram on the JVM.
- debugging-08: Grepping for ThreadLocal usage in request-handling code that is not cleared on completion is a useful check.
- debugging-08: A metrics or observability cardinality leak is the second-ranked hypothesis.
- debugging-08: Using product or campaign identifiers as metric labels causes each new campaign to introduce new unique label combinations.
- debugging-08: Unique metric label combinations can live forever in the metrics registry.
- debugging-08: A metrics cardinality leak matches the correlation between memory growth and marketing campaigns.
- debugging-08: A metrics cardinality leak matches growth without webhooks because the canary still emits its own metrics.
- debugging-08: Checking the unique series count on the /metrics endpoint over a week tests the metrics cardinality hypothesis.
- debugging-08: A metrics registry size that climbs and never resets indicates the leak.
- debugging-08: The metrics registry check can be done without a heap profiler.
- debugging-08: An eviction path that fails to clear a secondary index or reference to the evicted entry can cause a leak in a bounded cache.
- debugging-08: Logging cache item count versus configured limit, eviction rate, and average serialized entry size tests the cache hypothesis.
- debugging-08: Off-heap or native allocation is the fourth-ranked hypothesis.
- debugging-08: More traffic leads to more connections and buffers, matching the campaign correlation.
- debugging-08: JVM native memory tracking is enabled with -XX:NativeMemoryTracking.
- debugging-08: Allocator fragmentation is the fifth-ranked, lower-priority hypothesis.
- debugging-08: Standard allocators such as glibc malloc do not always return freed memory to the OS.
- debugging-08: RSS can ratchet upward with allocation churn and never return to baseline due to fragmentation.
- debugging-08: More request churn produces more fragmentation.
- debugging-08: Setting MALLOC_ARENA_MAX=1 or swapping in jemalloc or tcmalloc on a test instance tests the fragmentation hypothesis.
- debugging-08: Comparing live-heap size from GC logs against process RSS helps detect fragmentation.
- debugging-08: The canary's lower, steadier growth rate makes the responsible class or allocation site easier to isolate from noise.
- explanation-01: A hash map runs a key through a hash function that turns the key into a number.
- explanation-01: A hash map typically uses hash modulo array size (hash % array_size) to pick a slot in an underlying array.
- explanation-01: There are infinitely many possible keys but only a finite number of buckets.
- explanation-01: Because keys are infinite and buckets are finite, two keys will eventually land in the same bucket.
- explanation-01: The inevitability of collisions is the same idea as the birthday paradox.
- explanation-01: The collection in a chaining bucket is usually a linked list, and sometimes a small array or a tree.
- explanation-01: Chaining is simple to implement.
- explanation-01: In the worst case, where everything hashes to one bucket, chaining lookup degrades to O(n) list traversal.
- explanation-01: Linear probing tries successive slots at index + 1, index + 2, and so on.
- explanation-01: Quadratic probing jumps by increasing squares, such as index + 1, index + 4, index + 9.
- explanation-01: Quadratic probing reduces clustering.
- explanation-01: Double hashing uses a second hash function to compute the probe step size.
- explanation-01: Open addressing performance degrades sharply as the table fills up because clustering gets worse.
- explanation-01: Both chaining and open addressing rely on resizing the underlying array and rehashing all entries once the load factor gets too high.
- explanation-01: Resizing and rehashing keep collisions manageable and keep operations close to O(1).
- explanation-02: PostgreSQL and MySQL support pessimistic locking via SELECT ... FOR UPDATE.
- explanation-02: Seat reservations are an example use case for pessimistic locking.
- explanation-02: Pessimistic locking is also good when the work between read and write is short, keeping lock hold time low.
- explanation-02: Editing a user profile is an example use case for optimistic locking.
- explanation-02: Editing a document in a CMS is an example use case for optimistic locking.
- explanation-02: Optimistic locking works well in stateless and distributed systems.
- explanation-02: Holding a database lock across a network round-trip or user think-time would be costly.
- explanation-02: As a rule of thumb, high contention with a short critical section favors pessimistic locking.
- explanation-02: As a rule of thumb, low contention with long user-facing gaps between read and write favors optimistic locking.
- explanation-03: A starting TCP sender does not know how many other connections share the path's bandwidth.
- explanation-03: A starting TCP sender does not know how much buffering exists in routers along the path.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The receiver's advertised window limits data based on the receiver's buffer space.
- explanation-03: RFC 6928 specifies the initial congestion window of 10 segments.
- explanation-03: Growing linearly from the start would waste available bandwidth, especially on high-bandwidth, high-latency links.
- explanation-03: If a loss is detected after congestion avoidance begins, TCP reduces its rate, for example by cutting cwnd.
- explanation-03: TCP's congestion control philosophy allows millions of independent connections to share the internet's capacity without a central coordinator.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own register state, including the instruction pointer.
- explanation-04: Sharing memory between threads requires locks or synchronization.
- explanation-04: Process creation overhead includes creating a new address space and copy-on-write page tables.
- explanation-04: Examples of work worth isolating in a process include processing untrusted input, running third-party plugins, and rendering a webpage.
- explanation-04: Gunicorn uses worker processes.
- explanation-04: nginx uses worker processes.
- explanation-04: Process boundaries can be further restricted with seccomp, containers, or chroot.
- explanation-04: With many threads, growing amounts of shared mutable state need locks.
- explanation-04: Lock contention, deadlocks, and race conditions become harder to reason about as thread count grows.
- explanation-04: Explicit message passing is often easier to get correct than shared mutable state, though slower.
- explanation-05: Garbage collection prevents leaks caused by forgotten pointers.
- explanation-05: A collection can be reachable by being a static field or a singleton.
- explanation-05: Long-lived objects that listeners attach to include event emitters, DOM elements, and global buses.
- explanation-05: A closure often captures its enclosing scope.
- explanation-05: Timers or intervals holding references that are never cleared can cause memory leaks.
- explanation-06: Slow serialization is a possible cause of slowness.
- explanation-06: Adding a cache introduces new failure modes.
- explanation-06: Stale data is a failure mode introduced by caching.
- explanation-06: Cache invalidation bugs are a failure mode introduced by caching.
- explanation-06: A cache requires extra infrastructure to run.
- explanation-06: The user said they do not know the read/write mix of the service.
- explanation-06: If a workload is read-heavy but each read is already cheap, caching saves little.
- explanation-06: An indexed lookup is an example of a cheap read.
- explanation-06: Complex joins, aggregations, and external calls are examples of expensive reads.
- explanation-06: An APM tool can be used to measure request timing.
- explanation-06: Slow query logs can be checked to diagnose database performance.
- explanation-06: Running EXPLAIN on queries reveals whether they perform full table scans or are missing indexes.
- explanation-06: A slow API is often caused by a missing index or an N+1 query.
- explanation-06: Fixing a missing index or N+1 query is a smaller fix than building a cache layer.
- explanation-07: Multi-tenant data keyed by customer_id shards cleanly at a later date with low regret.
- explanation-07: Managed Postgres offerings such as RDS, Aurora, and Cloud SQL scale to tens of terabytes.
- explanation-07: Team capacity is a factor in the sharding decision.
- explanation-07: Sharding is worth its complexity only once an organization is actually paying a cost for not having it.
- explanation-07: Waiting risks that no natural shard key is designed into the schema, making eventual sharding a bigger rewrite.
- explanation-07: A single Postgres instance without replicas is a single point of failure.
- explanation-08: Speedups from switching from JSON to a binary format vary widely, ranging from negligible to 5-10x.
- explanation-08: If JSON encoding/decoding is 40% of request time, switching to a binary format is worth doing.
- explanation-08: Binary formats mainly win on numeric-heavy or repetitive-schema payloads.
- explanation-08: Binary formats give smaller payload size and faster parsing.
- explanation-08: Text-heavy or highly variable JSON payloads see much smaller gains from binary formats.
- explanation-08: A flamegraph or simple timers around JSON.parse/stringify equivalents can be used to profile serialization time.
- explanation-08: Typical payload sizes can be measured by logging them.
- explanation-08: Profiling the request path and measuring payload sizes takes roughly an hour of work.
- summarization-02: The smaller connection pool exhausted the available database connections.
- summarization-03: The change frees up web workers.
- summarization-03: The background worker pool would update the record after generating thumbnails.
- summarization-04: The bug is reproduced by clicking the "Export" button and then selecting the PDF option.
- summarization-04: After clicking the PDF export option, nothing happens initially.
- summarization-04: The issue was reproduced on the latest version of Firefox.
- summarization-04: The issue is likely a backend/server-side problem.
- summarization-07: The assistant checked its memory for relevant context on communication preferences before responding.
- summarization-07: No relevant information was found in memory.
- summarization-08: The stuck-progress-bar issue is a perception/feedback issue rather than a functional bug.
- summarization-08: The finding that the progress bar causes abandonment is rated as tentative but concerning.
- summarization-08: The recommendation is to prioritize investigating the link between the progress bar and abandonment.
- summarization-08: The progress-bar/abandonment finding is prioritized because of its behavioral impact despite the small sample size.

Added facts (styled only):

- code-review-01: The function has five problems.
- code-review-01: The most serious problem in the function is the mutable default argument.
- code-review-01: The recommended alternative is to catch a specific exception, or at least `Exception`, and log it.
- code-review-01: Whether an invalid `name` is a problem depends on what `db.insert` and downstream code expect.
- code-review-01: The suggested rewrite uses `roles = roles + ["member"]` to avoid mutating the caller's list.
- code-review-01: The caller usually has more context on what to do about a failure.
- code-review-02: `return profile.name.toUpperCase()` runs immediately after `profile` is declared.
- code-review-02: The code does not validate `userId`.
- code-review-02: If `userId` is undefined or empty, the request still fires to `/api/users/undefined`.
- code-review-02: The caller only finds out about an invalid `userId` from a failed or wrong response.
- code-review-03: Passing `status = "x' OR '1'='1"` returns every row in the table.
- code-review-03: With parameterized queries, the database driver handles escaping.
- code-review-03: If a column is renamed, code that indexes into the row by position breaks silently.
- code-review-03: `status` may be expected to be one of a small fixed set of values, such as "pending", "shipped", or "cancelled".
- code-review-03: Validating `status` against an allowed set before querying catches typos and unexpected values early.
- code-review-04: The class has exactly one real bug: `increment` is not atomic.
- code-review-04: Even if `increment` were made atomic in isolation, `reset` could still interleave between `increment`'s read and write.
- code-review-04: Reading `value` from outside the class is unsynchronized.
- code-review-04: Code that reads `counter.value` while another thread is mid-`increment` sees a value not guaranteed to reflect a completed operation.
- code-review-04: If external reads need to be consistent with writes, they should go through a locked accessor.
- code-review-04: Relying on the GIL breaks under other Python implementations such as Jython.
- code-review-04: In the corrected implementation, `value` is exposed as a property that acquires the lock before returning the stored value.
- code-review-05: With an empty argument, cd may leave the shell in the current directory.
- code-review-05: cd can fail because of a bad path or lack of permission.
- code-review-05: Appending || exit 1 to cd "$BACKUP_DIR" checks that cd succeeded.
- code-review-05: The -f flag on rm hides errors.
- code-review-05: Dropping -f from rm makes failures visible.
- code-review-05: The cd check should be in place before addressing the rm flags.
- code-review-05: rm -rf *.tmp fails silently when no .tmp files exist.
- code-review-05: rm reports "no such file" when given the literal string *.tmp.
- code-review-05: gzip fails if a file is already gzipped or unwritable.
- code-review-05: Placing -- before glob expansions guards against filenames starting with - being parsed as options.
- code-review-06: Treating None as "delete the key" is the defining trait of JSON Merge Patch.
- code-review-06: Replacing lists wholesale matches merge-patch semantics and is likely intentional.
- code-review-06: The function offers no way to fully replace a nested dict; it only supports adding, removing, or changing individual keys.
- code-review-06: To wipe a nested dict, the caller must explicitly null out every key it contains.
- code-review-06: The inability to fully replace a nested dict is inherent to the merge-patch model.
- code-review-06: RFC 7386's reference algorithm would treat a non-dict base value as {} and merge into it.
- code-review-06: The function's handling of a non-dict base value with a dict override value differs from the standard merge-patch algorithm.
- code-review-07: The retry helper contains one clear bug.
- code-review-07: It is possible the author wanted an instant first retry.
- code-review-07: An example of a fail-soft pattern is treating a failed optional fetch as 'no value'.
- code-review-07: Callers cannot distinguish 'legitimately got null' from 'call failed'.
- code-review-07: The lack of jitter and cap may be an accepted simplification rather than an oversight, since the delay is linear rather than exponential.
- code-review-07: A `501 Not Implemented` will never succeed on retry.
- code-review-07: A `503 Service Unavailable` can succeed on retry.
- code-review-07: Treating all 5xx codes the same is a defensible simplification.
- code-review-07: Treating all 5xx codes the same is worth confirming with the code owner if `fn` can return `501`.
- code-review-07: The check should cover whether callers test `=== null` versus `=== undefined`, or rely on `null` meaning something specific.
- code-review-07: The safest fix is to rethrow the original error on both exhaustion and non-retryable failures, dropping the `null`/`undefined` return entirely.
- code-review-08: The script never calls `clean()`.
- code-review-08: As shown, running the file does nothing.
- code-review-08: There is no `if __name__ == "__main__": clean()` in the file.
- code-review-08: No other caller of `clean()` is shown.
- code-review-08: If this file is the actual scheduled entry point, it silently does nothing every run.
- code-review-08: `os.listdir`, `os.path.getmtime`, and `os.remove` can all raise exceptions.
- code-review-08: If export files get touched or appended after creation, mtime resets and files may never age out as intended.
- code-review-08: Whether using `getmtime` is correct depends on how exports are written, which is unclear from the script alone.
- code-review-08: Logging may happen at the scheduler/wrapper level.
- debugging-03: `sum(values[i : i + window])` computes the sum of the window starting at index i.
- debugging-04: ASCII only allows bytes 0 through 127.
- debugging-06: The failures occur about once a week.
- debugging-06: The analytics service's logs are subject to rotation, so only retained logs cover past failure windows.
- debugging-06: A 30-plus-second blocking query on the analytics side matches the exact timeout value in the log.
- debugging-06: A connection leak is unlikely to explain weekly failure timing unless something triggers it on a regular cycle.
- debugging-06: A weekly-recurring analytics job such as a cron task, scheduled report, or backup could explain failures occurring about once a week.
- debugging-07: The failure occurs only under 4-way parallelism.
- debugging-07: The failure never occurs when the test is run serially.
- debugging-07: Under serial execution there is no contention, so the race window never manifests.
- debugging-07: Cross-worker interference would more likely produce an extra or wrong event than a consistent off-by-one, making it a secondary suspect.
- debugging-07: If the digest filters events by a timestamp window using a strict inequality (`>` instead of `>=`) or truncates timestamp precision, an event created exactly at the boundary could be excluded.
- debugging-07: Under load, the seed calls and the digest call are more likely to land on the same timestamp tick.
- debugging-07: The timestamp-tick collision would make a boundary bug visible only under CI's timing conditions.
- debugging-07: Local reproduction would allow iterating locally instead of waiting for a CI failure.
- debugging-07: The test fails in CI roughly 1 run in 10.
- debugging-07: Possible CI-specific causes include slower or contended CI hardware, a different DB backend, or a shared CI service.
- debugging-07: Failure-time diagnostics could log the full digest response, the three create responses with timestamps, and the worker ID, and upload them as a CI artifact.
- debugging-07: CI and the development environment may use different DB backends, such as SQLite in CI versus Postgres locally.
- debugging-07: SQLite under concurrent access from 4 workers is prone to locking and visibility issues.
- debugging-07: A real database server would not exhibit those SQLite locking and visibility issues.
- debugging-07: A SQLite-versus-Postgres difference would explain why the failure never happens on a developer machine.
- debugging-07: The failure never happens on a developer machine.
- debugging-07: The parallelism variable can be bisected by running the test in isolation with `pytest -n0` or a `pytest.mark.serial` group while the rest of the suite stays parallel in CI.
- debugging-07: If the flake disappears when the test runs in isolation, that confirms a timing-window race rather than a CI-environment issue unrelated to worker count.
- debugging-07: Inspecting the digest query's timestamp filter logic is a quick code read that costs nothing and might reveal a boundary bug without reproducing the failure.
- debugging-07: Asserting on every create call and attempting local reproduction are the cheapest first steps.
- debugging-07: Whether the failure is reproducible on demand determines whether it can be debugged directly or requires relying on artifact logging.
- debugging-08: The evidence points to two memory leaks stacked on top of each other.
- debugging-08: Direct buffers, TLS session caches, DNS caches, and connection-pool socket buffers are possible sources of off-heap growth.
- debugging-08: Examples of accumulating job state include a metrics map keyed by timestamp and a growing list of scheduled futures.
- debugging-08: The canary likely still serves normal read traffic.
- debugging-08: A retry queue for failed webhook deliveries with no cap or expiry is a candidate cause.
- debugging-08: To check the webhook-proportional leak, run allocation profiling tagged by request path during a high-traffic window versus a quiet one.
- debugging-08: async-profiler in allocation mode is an example tool for allocation profiling.
- debugging-08: There may be multiple cache instances instead of a single singleton.
- debugging-08: With multiple cache instances, each instance individually respects the bound but total memory is unbounded.
- debugging-08: New cache instances can be created by a DI scoping bug or a new-cache-per-request/session pattern.
- debugging-08: Old cache instances remaining referenced somewhere makes total memory unbounded.
- debugging-08: To check the multiple-instance hypothesis, check the live instance count of the cache class in a heap histogram.
- debugging-08: A cache class instance count greater than one and climbing indicates the multiple-instance bug, independent of the bound value.
- debugging-08: The recommended first step is capturing heap dumps on both the canary and a normal instance, once near the start of a week and once near the end, then diffing the class histograms.
- debugging-08: Diffing the class histograms will confirm or rule out each hypothesis directly.
- explanation-01: Open addressing fails outright once the array has no empty slots left.
- explanation-01: Chaining pays a small, constant memory and cache cost for every lookup, even when there is no collision.
- explanation-01: Most general-purpose hash maps use either chaining or open addressing under the hood.
- explanation-01: Python's dict uses open addressing.
- explanation-01: Java's HashMap uses chaining.
- explanation-01: You rarely need to implement collision handling yourself.
- explanation-02: In the example, a product page shows stock of 10 units with version = 5.
- explanation-02: In the example, two admins open the edit form at the same time and both try to change the price.
- explanation-02: When Admin A saves first, the database updates the row and increments version to 6.
- explanation-02: Admin B's save runs `UPDATE products SET price = ? WHERE id = ? AND version = 5`.
- explanation-02: Admin B's update matches zero rows because the version moved to 6.
- explanation-02: The application detects the zero-row update and tells Admin B to reload and retry.
- explanation-02: Optimistic locking fits when conflicts are rare and reads far outnumber writes.
- explanation-02: A bank transfer debits one account and credits another.
- explanation-02: In the example, the transaction runs `SELECT balance FROM accounts WHERE id = ? FOR UPDATE` on both rows.
- explanation-02: Waiting prevents both transfers from reading a stale balance and causing an incorrect final total.
- explanation-02: Pessimistic locking guarantees correctness without retries.
- explanation-02: Pessimistic locking risks deadlocks if locks are acquired in inconsistent orders.
- explanation-03: Dropped packets lead to retransmissions and wasted bandwidth.
- explanation-03: Congestion collapse actually happened on the early internet in 1986.
- explanation-03: The 1986 congestion collapse motivated the design of TCP congestion control, including slow start.
- explanation-03: ssthresh is usually set from a past congestion event.
- explanation-05: A cache keyed by request ID with no eviction policy is an example of an uncleaned growing collection.
- explanation-05: A UI component subscribing to a global event bus is an example of a listener registration.
- explanation-06: A cache works by keeping a copy of frequently-read data in fast memory so the app avoids querying the database every time.
- explanation-06: Memory used by a cache is faster than the database.
- explanation-06: In a read-heavy workload (many reads, few writes), a cache is likely to help a lot.
- explanation-06: In a read-heavy workload, most requests can be served from the cache instead of the database.
- explanation-06: Every write must also update or invalidate the cache to keep the cache correct.
- explanation-06: The overhead of keeping a cache correct on writes adds complexity and can slow things down.
- explanation-06: A product catalog is an example of data that is read often but rarely changes.
- explanation-06: A live counter is an example of data that changes on almost every write.
- explanation-06: The read/write ratio can be measured from logs or database metrics by comparing SELECT queries to INSERT/UPDATE/DELETE queries.
- explanation-06: Reads dominating is what makes caching effective.
- explanation-07: The growth rate of the dataset is unclear.
- explanation-07: CPU, WAL generation rate, and lock contention are indicators of whether a primary is nearing its write capacity.
- explanation-07: Hot data plus indexes exceeding available memory causes heavy disk I/O.
- explanation-07: Heavy disk I/O from a working set exceeding RAM is a scaling signal.
- explanation-07: Not knowing how much data will grow is different from not knowing how fast it will grow.
- explanation-07: The product team should be asked for a growth rate in units such as GB per month even if the ceiling is unknown.
- explanation-07: A slow, steady growth rate gives years of runway.
- explanation-07: A viral growth spike gives only months of runway.
- explanation-07: Most managed PostgreSQL offerings scale to tens of thousands of IOPS before hitting a hard wall.
- explanation-07: A bad shard key moves the bottleneck to one shard instead of solving it.
- explanation-07: Sharding can fail to solve the original problem, which may recur later.
- explanation-07: Monitoring gaps prevent seeing capacity limits approaching.
- explanation-07: Without alerts on write latency, connection saturation, and disk growth rate, capacity problems are discovered through an outage rather than a dashboard.
- explanation-07: Alert thresholds should be set well before capacity limits, for example at 70% of the instance's proven ceiling.
- explanation-07: Sharding should be revisited only when a shard key matching actual query patterns can be identified.
- explanation-08: If payloads are small, fixed costs such as connection setup, TLS, and routing likely dominate request time.
- explanation-08: When fixed costs dominate, the choice of serialization format matters little.
- explanation-08: A candidate binary format should be benchmarked against the current JSON path using the same real payloads.
- explanation-08: Double-digit percentages of request time would count as a meaningful share for serialization.
- explanation-08: Protocol Buffers and MessagePack are examples of binary serialization formats.
- explanation-08: Binary formats are not human-readable.
- explanation-08: The lack of human readability in binary formats complicates debugging and manual testing.
- explanation-08: Any external clients must support the new format, or both formats must be maintained.
- explanation-08: Migration costs include schema definitions, versioning, and updating all serializers and deserializers.
- summarization-01: The export dialog previously opened to a default location.
- summarization-01: The release includes internal changes to build tooling.
- summarization-01: The release includes an internal refactor of the session module.
- summarization-01: The release includes internal changes to telemetry batching.
- summarization-01: The internal changes do not change how the app looks or behaves.
- summarization-02: The on-call engineer was not paged until 09:21 UTC.
- summarization-02: The on-call engineer was paged 7 minutes after errors started.
- summarization-02: The rollback took 27 minutes to complete after the page.
- summarization-02: The detection delay and rollback duration are both worth reviewing for possible shortening.
- summarization-02: Separating or clearly distinguishing the templates and adding pool size to the review checklist would prevent a repeat of the outage.
- summarization-03: The change cuts 800ms to 3s off every upload.
- summarization-03: The upload endpoint will only store the original image and enqueue a job.
- summarization-03: The change carries one risk.
- summarization-04: The reporter reproduced the bug in Firefox.
- summarization-04: A colleague reproduced the bug in Chrome.
- summarization-04: The exact Firefox version was not confirmed.
- summarization-04: The reporter described their Firefox version as "latest version I think".
- summarization-04: The exact Firefox version is worth pinning down for the ticket if the team needs it.
- summarization-05: The listed action items come from Monday's sprint planning.
- summarization-06: A restart resolved the checkout service errors.
- summarization-08: The progress bar finding is firm on the behavior and tentative on the cause.
- summarization-08: The unused template gallery is not a finding and needs follow-up.
- summarization-08: A suggested follow-up is a task-based test with new customers who lack existing templates.

### clarity-flow

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 31 | 24 | 0.774 | 21 | 1 |
| code-review-02 | 18 | 16 | 0.889 | 15 | 1 |
| code-review-03 | 28 | 14 | 0.5 | 21 | 5 |
| code-review-04 | 24 | 15 | 0.625 | 20 | 8 |
| code-review-05 | 32 | 24 | 0.75 | 26 | 3 |
| code-review-06 | 43 | 28 | 0.651 | 30 | 3 |
| code-review-07 | 56 | 33 | 0.589 | 40 | 14 |
| code-review-08 | 54 | 35 | 0.648 | 34 | 4 |
| debugging-01 | 6 | 5 | 0.833 | 7 | 2 |
| debugging-02 | 14 | 10 | 0.714 | 8 | 0 |
| debugging-03 | 12 | 12 | 1.0 | 11 | 3 |
| debugging-04 | 15 | 6 | 0.4 | 11 | 3 |
| debugging-05 | 15 | 12 | 0.8 | 10 | 1 |
| debugging-06 | 24 | 16 | 0.667 | 39 | 10 |
| debugging-07 | 30 | 10 | 0.333 | 25 | 11 |
| debugging-08 | 50 | 20 | 0.4 | 32 | 9 |
| explanation-01 | 43 | 22 | 0.512 | 25 | 3 |
| explanation-02 | 28 | 18 | 0.643 | 20 | 3 |
| explanation-03 | 38 | 19 | 0.5 | 25 | 3 |
| explanation-04 | 41 | 29 | 0.707 | 30 | 1 |
| explanation-05 | 19 | 14 | 0.737 | 17 | 1 |
| explanation-06 | 32 | 20 | 0.625 | 27 | 3 |
| explanation-07 | 28 | 21 | 0.75 | 24 | 9 |
| explanation-08 | 15 | 7 | 0.467 | 14 | 7 |
| summarization-01 | 5 | 4 | 0.8 | 5 | 1 |
| summarization-02 | 14 | 12 | 0.857 | 15 | 5 |
| summarization-03 | 13 | 11 | 0.846 | 11 | 0 |
| summarization-04 | 16 | 10 | 0.625 | 10 | 0 |
| summarization-05 | 8 | 7 | 0.875 | 9 | 0 |
| summarization-06 | 12 | 12 | 1.0 | 13 | 1 |
| summarization-07 | 18 | 15 | 0.833 | 15 | 0 |
| summarization-08 | 19 | 17 | 0.895 | 17 | 0 |

Median fraction: 0.71 over 32 scored pairs.

Median additions: 3.0 over 32 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python pitfall.
- code-review-01: The function does not check whether `"member"` is already in `roles`.
- code-review-01: If `roles` already contains `"member"`, it gets added a second time.
- code-review-01: The fixed version raises `ValueError("name is required")` when `name` is falsy.
- code-review-01: The fixed version appends `"member"` only if it is not already in `roles`.
- code-review-01: The fixed version calls `db.insert({"name": name, "roles": roles})` and returns `True`.
- code-review-01: The fixed version prevents duplicate roles.
- code-review-02: The `async` keyword makes `loadProfile` return a `Promise`.
- code-review-02: The promise returned by `loadProfile` rejects synchronously due to the `TypeError` rather than because of awaited async work.
- code-review-03: The SQL injection vulnerability is critical.
- code-review-03: A caller passing user-controlled input such as `customer_name = "x' OR '1'='1"` can read, modify, or delete arbitrary data.
- code-review-03: sqlite3 uses `?` as its placeholder.
- code-review-03: psycopg2 uses `%s` as its placeholder.
- code-review-03: MySQLdb uses `%s` as its placeholder.
- code-review-03: If `customer_name` or `status` is not a string (e.g. `None`), the `+` concatenation raises a `TypeError`.
- code-review-03: The resulting `TypeError` produces a confusing stack trace rather than a clear error.
- code-review-03: Whether the lack of error handling is acceptable depends on the application's conventions.
- code-review-03: It is worth considering whether callers expect a wrapped or logged exception.
- code-review-03: The function has no pagination or limit.
- code-review-03: The function could return unbounded result sets on a wildcard-like match.
- code-review-03: The lack of pagination is more of a design consideration than a bug.
- code-review-03: The SQL injection issue is the only problem that actually needs fixing.
- code-review-03: All the other issues identified are secondary.
- code-review-04: The race condition gets worse under load.
- code-review-04: The window between the read and the write is exactly when a context switch is likely.
- code-review-04: The plain assignment `self.value = 0` is atomic in CPython.
- code-review-04: The atomicity of that assignment in CPython is provided by the GIL.
- code-review-04: The assignment `self.value = 0` is a single bytecode-level store.
- code-review-04: The atomicity of that assignment is a CPython implementation detail, not a guarantee of the Python language.
- code-review-04: Relying on CPython's assignment atomicity is fragile and non-portable to other Python implementations.
- code-review-04: PyPy has an STM mode.
- code-review-04: Python 3.13 has a free-threaded (no-GIL) build.
- code-review-05: If no .log files exist, `ls *.log` prints an error to stderr.
- code-review-05: The script lacks `set -u`, which would have caught the empty-$1 problem.
- code-review-05: The suggested rewrite uses `#!/bin/sh` with `set -eu`.
- code-review-05: The suggested rewrite exits with status 1 and a usage message on stderr when `$#` is not 1.
- code-review-05: The suggested rewrite exits with status 1 and an error message on stderr when BACKUP_DIR is not a directory.
- code-review-05: The suggested rewrite uses `rm -f -- *.tmp` instead of `rm -rf *.tmp`.
- code-review-05: The suggested rewrite uses `for f in *.log` with a `[ -e "$f" ] || continue` guard.
- code-review-05: The suggested rewrite calls `gzip -- "$f"` with the filename quoted.
- code-review-06: The JSON Merge Patch spec checks the patch value's type rather than the target's type.
- code-review-06: Recursive merging of a key produces no aliasing.
- code-review-06: When the override introduces a new key whose value is a dict, the code takes the `else` branch.
- code-review-06: The `else` branch assigns `merged[key] = value`, storing the value by reference.
- code-review-06: Storing the override value by reference makes the merged dict share the nested dict object with the override.
- code-review-06: The aliasing of newly-introduced nested dicts is an unintentional bug.
- code-review-06: Deletion via None only works when merging into a dict that already exists at that key.
- code-review-06: If the override introduces a brand-new nested dict, the whole dict is assigned as-is.
- code-review-06: None values inside a newly-introduced nested dict are stored literally instead of being treated as deletions.
- code-review-06: The None sentinel means different things depending on whether the key already existed as a dict.
- code-review-06: Custom Mapping subclasses and OrderedDict are examples of types not merged recursively.
- code-review-06: The function has no docstring and no type hints.
- code-review-06: The absence of a documented contract makes the analysis guesswork.
- code-review-06: The crash on a dict-to-non-dict override and the aliasing of newly-introduced nested dicts are genuine bugs to fix.
- code-review-06: The shallow-copy sharing and the asymmetric nested None deletion are subtler correctness traps that should at least be documented.
- code-review-07: The 429 branch waits before retrying.
- code-review-07: The >=500 branch calls continue with zero delay.
- code-review-07: There is no backoff for 5xx errors.
- code-review-07: Immediately retrying a struggling server is likely a bug rather than a deliberate asymmetry for a helper meant to provide polite retry behavior.
- code-review-07: The backoff calculation is an off-by-one error.
- code-review-07: The backoff was probably intended to be 1000 * (i + 1) or 2 ** i * 1000.
- code-review-07: Any non-retryable error, including 4xx other than 429 and exhausted retries, is converted into a null return rather than propagated.
- code-review-07: A caller that awaits withRetry(fn)() and dereferences the result without a null check will get a confusing downstream error far from the real cause.
- code-review-07: The design should probably preserve the original error, for example by attaching it, logging it, or returning a result object.
- code-review-07: The attempts parameter counts total tries rather than retries.
- code-review-07: The default value of attempts is 3.
- code-review-07: A default attempts of 3 means fn is called at most 3 times total, not 3 retries after an original attempt.
- code-review-07: The attempts naming ambiguity is not a bug per se.
- code-review-07: The attempts semantics are worth confirming with any caller who tuned the value expecting different semantics.
- code-review-07: Unbounded backoff is fine for small attempts values.
- code-review-07: The lack of cap and jitter likely never mattered because the default attempts is 3.
- code-review-07: The zero-delay first backoff is likely accidental.
- code-review-07: The absence of backoff on 5xx is likely accidental.
- code-review-07: The accidental issues resemble logic slips from editing retry logic without re-testing all branches.
- code-review-07: The null-swallowing contract should be confirmed explicitly before relying on it further.
- code-review-07: The code can be rewritten with corrected backoff, consistent failure semantics, and error preservation.
- code-review-07: Unknown callers may depend on the current null/undefined-swallowing behavior.
- code-review-07: Changing the return contract should be a deliberate, separate decision rather than a quiet fix.
- code-review-08: An aborted run produces only a traceback, visible if run interactively.
- code-review-08: os.listdir returns entries in an arbitrary, filesystem-dependent order.
- code-review-08: Because of arbitrary listing order plus the 500-item cap, which files get removed near the cap is essentially random.
- code-review-08: The script does not delete oldest files first.
- code-review-08: Deleting oldest first would require sorting by mtime.
- code-review-08: os.remove unlinks the symlink itself rather than the target.
- code-review-08: The unconditional tmp/part deletion is very likely not deliberate.
- code-review-08: The constants have no comments, no config, and no environment variable override.
- code-review-08: The 45-day and 500 values were previously flagged by the user as magic numbers with no rationale.
- code-review-08: The rationale for the 45-day and 500 values must come from whoever wrote the code or from data-retention/compliance requirements.
- code-review-08: The 45-day value may be tied to a legal retention policy.
- code-review-08: As written, the constants are indistinguishable from arbitrary defaults.
- code-review-08: The script has no --dry-run mode.
- code-review-08: A dry-run mode is standard practice for scheduled deletion scripts.
- code-review-08: The absence of a dry-run mode is a gap rather than a bug.
- code-review-08: Without a dry-run mode, behavior cannot be safely tested in production without risking real deletions.
- code-review-08: The variable 'removed' is computed but is not logged or returned anywhere visible in the snippet.
- code-review-08: If 'removed' is meant to feed monitoring or alerting, that plumbing is missing.
- code-review-08: The likely genuine bugs are the cap not applying to tmp/part deletions, lack of exception isolation, arbitrary deletion order under the cap, and import-time CUTOFF computation.
- debugging-01: The fix is to have get_url return f"http://{cfg['host']}:{cfg['port']}/api".
- debugging-02: The NaN value produced is what gets logged to the console.
- debugging-02: The incremented value is assigned onto the global object rather than the Timer instance.
- debugging-02: Calling .bind(this) on a regular function callback is an alternative fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` inside it is an alternative fix.
- debugging-04: The file contains a non-ASCII byte 0xc3 at byte 512.
- debugging-04: The 0xc3 byte likely represents an accented character.
- debugging-04: UTF-8 is the most common encoding to use for such files.
- debugging-04: Using errors="replace" can mangle unusual characters.
- debugging-04: Mangling characters is acceptable if only line counts matter rather than content.
- debugging-04: The libraries chardet and charset-normalizer can detect a file's encoding.
- debugging-04: Opening a file in binary mode with "rb" avoids decoding entirely.
- debugging-04: Counting b"\n" bytes in binary mode counts lines without decoding.
- debugging-04: Iterating over a file object opened in binary mode yields lines.
- debugging-05: DEFAULT_TAGS is initially ["draft"].
- debugging-05: When the test runs alone, one call to make_post produces tags equal to ["draft", "post"].
- debugging-05: In that case the test's assertion fails, for example because the list is ["draft", "post", "post"].
- debugging-06: An undersized pool relative to the database's max_connections is a plausible cause.
- debugging-06: If the combined pool sizes of the export job, the analytics service, and other clients exceed the database's max_connections, requests queue at the database even when each service's own pool appears to have headroom.
- debugging-06: Another nightly cron job scheduled near 02:14 UTC could be overlapping with the export job.
- debugging-06: Pool-utilization metrics worth adding include in-use count, wait queue depth, and wait time.
- debugging-06: Querying pg_stat_activity or an equivalent view during a live failure window, filtered by application or user, shows who is holding connections and whether any are idle in transaction or long-running.
- debugging-06: Summing all services' maximum pool sizes and comparing that total against the database's max_connections checks for oversubscription.
- debugging-06: Setting an alert on pool wait time or queue depth at a threshold below the 30s timeout would page someone with full context during the next occurrence.
- debugging-06: The relevant log fragment for the failure was lost to log rotation.
- debugging-07: A read-after-write race on an async pipeline is the most common cause of flakes where a count is short by exactly one.
- debugging-07: If an API call returns after the HTTP handler responds but before the DB transaction commits, a fast subsequent read can miss the write.
- debugging-07: Deferred commits can occur when the commit happens in a background hook or when the ORM session flush is deferred.
- debugging-07: A missing await or commit boundary produces intermittent, load-sensitive failures that are exactly one event short.
- debugging-07: If a digest query means 'events since timestamp X' and X is computed from real wall-clock time, a momentarily starved CI machine can let the first seeded event fall outside the window.
- debugging-07: GC pauses, container throttling, and noisy neighbors can starve a CI machine.
- debugging-07: Time-window boundary failures are more likely under load, which correlates with parallel CI workers competing for CPU.
- debugging-07: If a test does not assert on the response of each seed call, a transient 429 or 500 can silently drop an event and only be noticed at the final assertion.
- debugging-07: Transient 429s or 500s from a shared rate limiter or connection pool exhaustion are more likely when four workers hammer the same DB or API simultaneously.
- debugging-07: pytest includes a custom assertion message in the failure log even without artifact storage.
- debugging-07: Dumping seed event IDs, HTTP status codes, call timestamps, and the raw digest response into the assertion message usually reveals which seed is missing or whether the digest call happened too early.
- debugging-07: `pytest -n 4 --count 200` combines pytest-xdist with pytest-repeat.
- debugging-07: If the test only flakes when the full suite runs, shared fixture or account contamination from other tests is the likely cause rather than a bug in the test in isolation.
- debugging-07: `-k test_digest_contains_all_events` filters a pytest run to a single test while still collecting the rest of the suite.
- debugging-07: Per-test isolation can be achieved with `uuid4()` IDs or freezegun-style time control instead of hardcoded constants.
- debugging-07: If the user/org ID and time window are shared constants, the correct fix is fixture isolation rather than retries.
- debugging-07: Under READ COMMITTED isolation, when the app writes on a different connection or transaction than the test's setup, stale reads can occur and be worsened by connection pool pressure from four workers.
- debugging-07: Logging seed results and digest contents on failure, combined with testing whether a poll/retry removes the flake, gives the fastest diagnostic signal.
- debugging-07: That combination can distinguish a race condition from a shared-state isolation bug within one or two CI flakes.
- debugging-07: A race condition and a shared-state isolation bug require different fixes: adding a read-your-writes guarantee versus isolating test fixtures.
- debugging-08: The cache could still be the root cause if the composition of its entries changed.
- debugging-08: A bound on entry count does not protect against growing entry size.
- debugging-08: ThreadLocal or MDC context leaking on pooled threads is a possible reference leak source.
- debugging-08: A reference leak explains why the canary still grows slowly, because its own scheduled or background traffic hits the same code path.
- debugging-08: `jcmd <pid> GC.class_histogram` produces a heap class histogram on the JVM.
- debugging-08: Grepping for ThreadLocal usage in request-handling code that is not cleared on completion is a useful check.
- debugging-08: A metrics or observability cardinality leak is the second-ranked hypothesis.
- debugging-08: Using product or campaign identifiers as metric labels causes each new campaign to introduce new unique label combinations.
- debugging-08: Unique metric label combinations can live forever in the metrics registry.
- debugging-08: A metrics cardinality leak matches the correlation between memory growth and marketing campaigns.
- debugging-08: A metrics cardinality leak matches growth without webhooks because the canary still emits its own metrics.
- debugging-08: Checking the unique series count on the /metrics endpoint over a week tests the metrics cardinality hypothesis.
- debugging-08: A metrics registry size that climbs and never resets indicates the leak.
- debugging-08: The metrics registry check can be done without a heap profiler.
- debugging-08: Campaigns can increase average cache entry payload size through larger product descriptions or more variants and images.
- debugging-08: Logging cache item count versus configured limit, eviction rate, and average serialized entry size tests the cache hypothesis.
- debugging-08: A capped entry count combined with growing average entry size during campaigns confirms the cache hypothesis.
- debugging-08: Off-heap or native allocation is the fourth-ranked hypothesis.
- debugging-08: Buffers for TLS, compression, and HTTP client connection pools are often native or off-heap.
- debugging-08: Off-heap buffers are not visible to a Java-style heap profiler.
- debugging-08: More traffic leads to more connections and buffers, matching the campaign correlation.
- debugging-08: Off-heap allocation matches the canary growing slowly from its own baseline connections.
- debugging-08: RSS growing while heap usage stays flat indicates off-heap memory growth.
- debugging-08: JVM native memory tracking is enabled with -XX:NativeMemoryTracking.
- debugging-08: pmap or smaps snapshots over time can diagnose native memory growth.
- debugging-08: Standard allocators such as glibc malloc do not always return freed memory to the OS.
- debugging-08: RSS can ratchet upward with allocation churn and never return to baseline due to fragmentation.
- debugging-08: More request churn produces more fragmentation.
- debugging-08: Setting MALLOC_ARENA_MAX=1 or swapping in jemalloc or tcmalloc on a test instance tests the fragmentation hypothesis.
- debugging-08: The canary's lower, steadier growth rate makes the responsible class or allocation site easier to isolate from noise.
- explanation-01: A hash map runs a key through a hash function that turns the key into a number.
- explanation-01: A hash map typically uses hash modulo array size (hash % array_size) to pick a slot in an underlying array.
- explanation-01: A slot in a hash map's underlying array is called a bucket.
- explanation-01: Collisions are not a bug.
- explanation-01: Collisions are unavoidable.
- explanation-01: There are infinitely many possible keys but only a finite number of buckets.
- explanation-01: Because keys are infinite and buckets are finite, two keys will eventually land in the same bucket.
- explanation-01: The inevitability of collisions is the same idea as the birthday paradox.
- explanation-01: The collection in a chaining bucket is usually a linked list, and sometimes a small array or a tree.
- explanation-01: Deletion under chaining is easy because the entry is just removed from the list.
- explanation-01: In the worst case, where everything hashes to one bucket, chaining lookup degrades to O(n) list traversal.
- explanation-01: Quadratic probing jumps by increasing squares, such as index + 1, index + 4, index + 9.
- explanation-01: Quadratic probing reduces clustering.
- explanation-01: Double hashing uses a second hash function to compute the probe step size.
- explanation-01: Open addressing performance degrades sharply as the table fills up because clustering gets worse.
- explanation-01: Deletion under open addressing typically requires a special deleted marker called a tombstone.
- explanation-01: Open addressing needs resizing sooner than chaining at high load factors.
- explanation-01: Tuning open addressing involves keeping the load factor low, often below about 0.7.
- explanation-01: Tuning open addressing involves resizing and rehashing proactively.
- explanation-01: Both chaining and open addressing rely on resizing the underlying array and rehashing all entries once the load factor gets too high.
- explanation-01: Resizing and rehashing keep collisions manageable and keep operations close to O(1).
- explanation-02: PostgreSQL and MySQL support pessimistic locking via SELECT ... FOR UPDATE.
- explanation-02: Seat reservations are an example use case for pessimistic locking.
- explanation-02: Inventory decrements at checkout are an example use case for pessimistic locking.
- explanation-02: Pessimistic locking is also good when the work between read and write is short, keeping lock hold time low.
- explanation-02: Editing a document in a CMS is an example use case for optimistic locking.
- explanation-02: Most web CRUD operations, where two users rarely edit the same record simultaneously, are a use case for optimistic locking.
- explanation-02: Optimistic locking works well in stateless and distributed systems.
- explanation-02: Holding a database lock across a network round-trip or user think-time would be costly.
- explanation-02: As a rule of thumb, high contention with a short critical section favors pessimistic locking.
- explanation-02: As a rule of thumb, low contention with long user-facing gaps between read and write favors optimistic locking.
- explanation-03: A starting TCP sender does not know how many other connections share the path's bandwidth.
- explanation-03: A starting TCP sender does not know how much buffering exists in routers along the path.
- explanation-03: If a sender transmitted as fast as the receiver's window allowed, it could send more data than the network path can handle.
- explanation-03: Congestion collapse is the scenario where the network is congested and throughput collapses.
- explanation-03: Congestion collapse was a real problem on the early internet in the 1980s.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The receiver's advertised window limits data based on the receiver's buffer space.
- explanation-03: Historically, TCP connections began with a congestion window of 1 segment.
- explanation-03: TCP connections now typically begin with a congestion window of 10 segments.
- explanation-03: RFC 6928 specifies the initial congestion window of 10 segments.
- explanation-03: During slow start, the sender increases cwnd by roughly one segment for each ACK received.
- explanation-03: Each round trip generates ACKs for everything sent during that round.
- explanation-03: Congestion avoidance uses linear growth instead of exponential growth.
- explanation-03: Growing linearly from the start would waste available bandwidth, especially on high-bandwidth, high-latency links.
- explanation-03: Linear growth from the start might take a long time to reach a reasonable sending rate.
- explanation-03: If a loss is detected after congestion avoidance begins, TCP reduces its rate, for example by cutting cwnd.
- explanation-03: After a loss, TCP often re-enters a slow-start-like ramp.
- explanation-03: TCP's congestion control philosophy is to start cautious, increase while things go well, and back off sharply at signs of trouble.
- explanation-03: TCP's congestion control philosophy allows millions of independent connections to share the internet's capacity without a central coordinator.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own register state, including the instruction pointer.
- explanation-04: Sharing memory between threads requires locks or synchronization.
- explanation-04: Spawning and switching processes is more expensive than spawning and switching threads.
- explanation-04: Process creation overhead includes creating a new address space and copy-on-write page tables.
- explanation-04: Older Ruby MRI has a global interpreter lock.
- explanation-04: Gunicorn uses worker processes.
- explanation-04: nginx uses worker processes.
- explanation-04: With many threads, growing amounts of shared mutable state need locks.
- explanation-04: Lock contention, deadlocks, and race conditions become harder to reason about as thread count grows.
- explanation-04: Explicit message passing is often easier to get correct than shared mutable state, though slower.
- explanation-04: Processes can be distributed across machines more naturally than threads.
- explanation-05: Root references include global variables and active stack frames.
- explanation-05: Garbage collection prevents leaks caused by forgotten pointers.
- explanation-05: A collection can be reachable by being a static field or a singleton.
- explanation-05: A closure often captures its enclosing scope.
- explanation-05: Timers or intervals holding references that are never cleared can cause memory leaks.
- explanation-06: External API calls are a possible cause of slowness.
- explanation-06: Slow serialization is a possible cause of slowness.
- explanation-06: The user said they do not know the read/write mix of the service.
- explanation-06: If a workload is read-heavy but each read is already cheap, caching saves little.
- explanation-06: An indexed lookup is an example of a cheap read.
- explanation-06: Complex joins, aggregations, and external calls are examples of expensive reads.
- explanation-06: Adding basic request timing and logging reveals which endpoints are actually slow.
- explanation-06: An APM tool can be used to measure request timing.
- explanation-06: Slow query logs can be checked to diagnose database performance.
- explanation-06: Running EXPLAIN on queries reveals whether they perform full table scans or are missing indexes.
- explanation-06: A slow API is often caused by a missing index or an N+1 query.
- explanation-06: Fixing a missing index or N+1 query is a smaller fix than building a cache layer.
- explanation-07: Multi-tenant data keyed by customer_id shards cleanly at a later date with low regret.
- explanation-07: Managed Postgres offerings such as RDS, Aurora, and Cloud SQL scale to tens of terabytes.
- explanation-07: Managed Postgres offerings offer very large instance types.
- explanation-07: Choosing the wrong shard key forces a later re-shard.
- explanation-07: Application-level cross-shard joins and transactions slow down every feature that touches related data.
- explanation-07: Waiting risks that no natural shard key is designed into the schema, making eventual sharding a bigger rewrite.
- explanation-07: A single Postgres instance without replicas is a single point of failure.
- explanation-08: Speedups from switching from JSON to a binary format vary widely, ranging from negligible to 5-10x.
- explanation-08: Two factors determine the payoff of switching to a binary format: the share of latency spent on serialization/parsing, and the payload shape.
- explanation-08: Request latency is composed of serialization/parsing plus network, database queries, and business logic.
- explanation-08: Binary formats mainly win on numeric-heavy or repetitive-schema payloads.
- explanation-08: Text-heavy or highly variable JSON payloads see much smaller gains from binary formats.
- explanation-08: A flamegraph or simple timers around JSON.parse/stringify equivalents can be used to profile serialization time.
- explanation-08: Typical payload sizes can be measured by logging them.
- explanation-08: Profiling the request path and measuring payload sizes takes roughly an hour of work.
- summarization-01: The app now starts up to 40% faster.
- summarization-02: The incident caused approximately 12% error rates for checkout.
- summarization-02: The incident ran from 09:14 to 09:48 UTC.
- summarization-03: The change frees up web workers.
- summarization-03: Uploads would immediately store the original image.
- summarization-04: The bug is reproduced by clicking the "Export" button and then selecting the PDF option.
- summarization-04: The expected behavior is that PDF export downloads successfully.
- summarization-04: The expected PDF export behavior is consistent with the CSV export behavior.
- summarization-04: The issue was reproduced on the latest version of Firefox.
- summarization-04: The issue was reproduced across two different machines/users.
- summarization-04: The issue is likely a backend/server-side problem.
- summarization-05: Chen is assigned to continue the search indexing work.
- summarization-07: The assistant checked its memory for relevant context on communication preferences before responding.
- summarization-07: No relevant information was found in memory.
- summarization-07: Confirming the tail latency result requires a production-like test.
- summarization-08: The recommendation is to prioritize investigating the link between the progress bar and abandonment.
- summarization-08: The progress-bar/abandonment finding is prioritized because of its behavioral impact despite the small sample size.

Added facts (styled only):

- code-review-01: The function has six problems.
- code-review-02: `res.json()` does not reject on a 404 or 500 HTTP status.
- code-review-03: The string `x' OR '1'='1` passed as `status` is an example of an injection payload.
- code-review-03: The function has no type hints.
- code-review-03: The function has no docstring.
- code-review-03: Without type hints or a docstring, callers cannot tell what types `cursor`, `customer_name`, and `status` should be.
- code-review-03: Without type hints or a docstring, callers cannot tell what the return value looks like.
- code-review-04: `reset` performs an unsynchronized read-modify-write operation on shared state.
- code-review-04: Any caller can read or write `value` directly from any thread, bypassing the safety the methods attempt to provide.
- code-review-04: In the fixed version, `__init__` sets `self._value = 0` and `self._lock = threading.Lock()`.
- code-review-04: In the fixed version, `increment` executes `self._value += 1` while holding the lock.
- code-review-04: In the fixed version, `reset` sets `self._value = 0` while holding the lock.
- code-review-04: In the fixed version, `value` is a property that returns `self._value` while holding the lock.
- code-review-04: The fix renames the attribute to `_value` and exposes it through a locked property.
- code-review-04: Renaming the attribute to `_value` and exposing it via a locked property prevents external code from bypassing the synchronization.
- code-review-05: If `$1` is empty or `$BACKUP_DIR` does not exist, `cd $BACKUP_DIR` fails.
- code-review-05: Writing `cd "$BACKUP_DIR" || exit 1` fixes the unchecked `cd`.
- code-review-05: The no-match glob error is harmless but noisy and can be accepted as-is.
- code-review-06: The aliasing bug stays invisible until two callers hold the same base object.
- code-review-06: The type-mismatch crash is the only item listed that is a plain defect rather than a design decision.
- code-review-06: The recommended first step is writing a regression test for the type-mismatch crash.
- code-review-07: The function contains one real bug.
- code-review-07: If `fn` can legitimately return `null` as valid data, callers cannot distinguish success-with-null from failure-with-null.
- code-review-07: Transient network failures are the exact case that retry logic exists for.
- code-review-07: The linear backoff is probably an intentional simple backoff.
- code-review-07: The code ignores any `Retry-After` header and relies on a guessed delay.
- code-review-07: A 501 (Not Implemented) will never succeed no matter how many times it is retried.
- code-review-07: Uniform 5xx retrying is likely a simplification rather than a deliberate choice.
- code-review-07: Uniform 5xx retrying wastes attempts on permanent failures.
- code-review-07: The function has no idempotency guard and retries `fn` blindly.
- code-review-07: If `fn` wraps a non-idempotent call such as a POST that creates a resource, a timeout followed by a retry can cause duplicate side effects.
- code-review-07: Nothing in the code suggests idempotency was considered.
- code-review-07: The returned function is an arrow function.
- code-review-07: Because it is an arrow function, it cannot be bound to a different `this` at call time.
- code-review-07: The overall shape of the code is 401/5xx-only retry, capped attempts, and `null` as a soft-failure sentinel.
- code-review-08: The missing age check on pattern-matched deletions is the most dangerous bug in the script.
- code-review-08: The cutoff is 45 days, written as `86400 * 45`.
- code-review-08: Unconditional deletion of `tmp-`/`.part` names is likely intended to treat those files as always-safe leftovers.
- code-review-08: The missing age check and the missing exception handling should be fixed first.
- debugging-01: The fix should be applied to line 4.
- debugging-01: The corrected line 4 is: return f"http://{cfg['host']}:{cfg['port']}/api"
- debugging-03: With `values = [1, 2, 3, 4]` and `window = 2`, the buggy loop produces the windows `[1,2]` and `[2,3]`.
- debugging-03: The buggy loop misses the window `[3,4]`.
- debugging-03: `i = 2` gives the missing window `[3,4]`.
- debugging-04: The code works correctly on files containing only ASCII.
- debugging-04: UTF-8 is a superset of ASCII.
- debugging-04: UTF-8 decoding handles both pure-ASCII and non-ASCII files.
- debugging-05: The assertion only holds when the test runs first and alone.
- debugging-06: A leak explains the intermittent nature of the failure because it depends on hitting the leaking code path.
- debugging-06: Retry amplification is the fifth most probable cause.
- debugging-06: A retry occurred on attempt 2.
- debugging-06: The retry adds load while the pool is already stressed, worsening a marginal situation.
- debugging-06: The failure window was 02:14:00 to 02:14:41 UTC on 2026-07-29.
- debugging-06: Graphing active connection counts over the past few weeks can reveal an upward trend before failures.
- debugging-06: Giving the export job its own connection pool, or its own database user with a reserved connection limit, is a mitigation independent of root cause.
- debugging-06: Separating the pools would prevent analytics from starving the export job.
- debugging-06: Separating the pools would not fix a leak.
- debugging-06: Separating the pools would remove the shared-resource variable and make future failures easier to attribute.
- debugging-07: Serial test runs never fail.
- debugging-07: Shared state across workers is the single most common source of this symptom.
- debugging-07: The lengthened race window explains why serial runs never hit the failure.
- debugging-07: If events use a timestamp or auto-increment ID for ordering or deduplication, concurrent workers can produce key collisions.
- debugging-07: Key collisions can cause one event to overwrite or shadow another.
- debugging-07: A slow test database under four-way load could cause the third insert or the digest read to exceed a timeout.
- debugging-07: A timeout can be silently dropped without raising if error handling swallows it.
- debugging-07: Reproducing locally with `-n 4` and capturing SQL/API logs recovers the missing diagnostics.
- debugging-07: Each pytest-xdist worker should be confirmed to have its own database or schema rather than a shared one.
- debugging-07: pytest-mock fixtures may reset state per-test but not per-worker.
- debugging-07: The local `-n 4` reproduction is the fastest way to turn an unreproducible CI flake into a locally debuggable problem.
- debugging-08: Two separate causes fit the evidence better than a single leak.
- debugging-08: The other likely cause is a slow baseline leak that runs even without traffic.
- debugging-08: Ruling out the product cache is cheap to do.
- debugging-08: Diffing two heap snapshots taken under load reveals objects whose count scales with request count.
- debugging-08: Eviction logic can fail via an off-by-one error.
- debugging-08: Cache keys can grow unbounded while values are capped.
- debugging-08: If the cause were GC pressure or fragmentation, memory usage would drop back toward baseline during low traffic.
- debugging-08: Fragmentation should only be ruled out after confirming retained-object counts are climbing, not just RSS.
- debugging-08: That snapshot diff alone should reveal whether the baseline leak is background jobs, connection pooling, or something else.
- explanation-01: Most general-purpose hash maps use chaining.
- explanation-01: Java's HashMap uses chaining.
- explanation-01: Python's dict uses open addressing.
- explanation-02: Optimistic locking checks for conflicts only at commit time.
- explanation-02: Low-contention workloads consist of many reads and few conflicting writes.
- explanation-02: In fund transfers, blocking is cheaper than risking an inconsistent retry.
- explanation-03: A network path may cross a fast data-center link or a congested home router.
- explanation-03: Dropped packets cause retransmissions.
- explanation-03: Dropped packets waste bandwidth.
- explanation-04: The difference in memory ownership explains almost everything else about how processes and threads behave.
- explanation-05: Examples of accumulated entries include session data, memoized results, and log entries.
- explanation-06: A cache sits in front of the database.
- explanation-06: Stale-cache bugs are notoriously hard to debug.
- explanation-06: Profiling identifies which endpoint, which query, and which line consumes time.
- explanation-07: The sharding decision depends on growth rate rather than current database size.
- explanation-07: 200 GB growing 10% a year is a different problem than 200 GB doubling every quarter.
- explanation-07: A rough growth trend from historical data is more useful than a forecast from the product team.
- explanation-07: A team needs the operational maturity and tooling for sharding before it needs shards.
- explanation-07: Single-instance headroom would likely have covered another year or two.
- explanation-07: Sharding makes debugging and consistency guarantees harder.
- explanation-07: Hard walls such as vacuum times, replication lag, and connection limits can be hit before sharding infrastructure exists.
- explanation-07: PostgreSQL supports native table partitioning, including by date or tenant.
- explanation-07: Read replicas, native table partitioning, and connection pooling buy significant headroom without the operational cost of sharding.
- explanation-08: If serialization is 40% of request time, a 5x parsing speedup is transformative.
- explanation-08: Payload size matters only insofar as it affects network transfer time or serialization cost.
- explanation-08: A format that is 30% smaller barely matters if bandwidth is not the bottleneck.
- explanation-08: Migrating to a binary format requires rewriting client and server code.
- explanation-08: Migrating away from JSON means losing JSON's debuggability.
- explanation-08: Formats like protobuf add a schema step.
- explanation-08: Without measurement data, an estimate of the improvement is a guess presented as an argument.
- summarization-01: The app starts up roughly 40% faster.
- summarization-02: A deploy copied staging's pool-size setting into production's template.
- summarization-02: The review step could not rely on the file path alone to catch the mismatch.
- summarization-02: Recovery relied on paging and a rollback.
- summarization-02: The rollback took 34 minutes.
- summarization-02: The rollback occurred from 09:14 to 09:48.
- summarization-06: A restart brought the service back.

### classic-concise

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 31 | 24 | 0.774 | 17 | 2 |
| code-review-02 | 18 | 12 | 0.667 | 15 | 1 |
| code-review-03 | 28 | 13 | 0.464 | 16 | 3 |
| code-review-04 | 24 | 15 | 0.625 | 14 | 0 |
| code-review-05 | 32 | 26 | 0.812 | 29 | 2 |
| code-review-06 | 43 | 31 | 0.721 | 25 | 5 |
| code-review-07 | 56 | 39 | 0.696 | 31 | 8 |
| code-review-08 | 54 | 33 | 0.611 | 32 | 3 |
| debugging-01 | 6 | 5 | 0.833 | 7 | 0 |
| debugging-02 | 14 | 10 | 0.714 | 8 | 0 |
| debugging-03 | 12 | 10 | 0.833 | 6 | 2 |
| debugging-04 | 15 | 6 | 0.4 | 11 | 0 |
| debugging-05 | 15 | 14 | 0.933 | 11 | 1 |
| debugging-06 | 24 | 20 | 0.833 | 33 | 12 |
| debugging-07 | 30 | 18 | 0.6 | 38 | 14 |
| debugging-08 | 50 | 14 | 0.28 | 27 | 8 |
| explanation-01 | 43 | 28 | 0.651 | 26 | 5 |
| explanation-02 | 28 | 25 | 0.893 | 22 | 2 |
| explanation-03 | 38 | 24 | 0.632 | 18 | 1 |
| explanation-04 | 41 | 29 | 0.707 | 27 | 2 |
| explanation-05 | 19 | 12 | 0.632 | 14 | 0 |
| explanation-06 | 32 | 16 | 0.5 | 12 | 4 |
| explanation-07 | 28 | 20 | 0.714 | 22 | 7 |
| explanation-08 | 15 | 10 | 0.667 | 11 | 4 |
| summarization-01 | 5 | 4 | 0.8 | 5 | 2 |
| summarization-02 | 14 | 10 | 0.714 | 10 | 0 |
| summarization-03 | 13 | 13 | 1.0 | 13 | 1 |
| summarization-04 | 16 | 13 | 0.812 | 11 | 1 |
| summarization-05 | 8 | 8 | 1.0 | 10 | 0 |
| summarization-06 | 12 | 12 | 1.0 | 12 | 1 |
| summarization-07 | 18 | 13 | 0.722 | 15 | 2 |
| summarization-08 | 19 | 19 | 1.0 | 22 | 1 |

Median fraction: 0.714 over 32 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python pitfall.
- code-review-01: The function does not check whether `"member"` is already in `roles`.
- code-review-01: If `roles` already contains `"member"`, it gets added a second time.
- code-review-01: The fixed version uses `roles = list(roles) if roles else []`.
- code-review-01: The fixed version appends `"member"` only if it is not already in `roles`.
- code-review-01: The fixed version avoids silently swallowing exceptions, leaving handling to the caller.
- code-review-01: The fixed version prevents duplicate roles.
- code-review-02: The `async` keyword makes `loadProfile` return a `Promise`.
- code-review-02: The promise returned by `loadProfile` rejects synchronously due to the `TypeError` rather than because of awaited async work.
- code-review-02: Without a status check, an error page or empty body could be parsed as JSON and produce confusing downstream failures.
- code-review-02: The code does not validate that `data` has a `name` property.
- code-review-02: If the API returns an unexpected value such as an error object, `.name` could be `undefined` and `.toUpperCase()` would throw.
- code-review-02: The fixed version removes the unused `profile` variable and the unused promise chain.
- code-review-03: The SQL injection vulnerability is critical.
- code-review-03: The correct placeholder style (`%s`, `?`, or `:name`) depends on the database driver.
- code-review-03: sqlite3 uses `?` as its placeholder.
- code-review-03: psycopg2 uses `%s` as its placeholder.
- code-review-03: MySQLdb uses `%s` as its placeholder.
- code-review-03: `SELECT *` breaks silently if columns are added, reordered, or removed.
- code-review-03: If `customer_name` or `status` is not a string (e.g. `None`), the `+` concatenation raises a `TypeError`.
- code-review-03: The resulting `TypeError` produces a confusing stack trace rather than a clear error.
- code-review-03: Whether the lack of error handling is acceptable depends on the application's conventions.
- code-review-03: It is worth considering whether callers expect a wrapped or logged exception.
- code-review-03: The function has no pagination or limit.
- code-review-03: The function could return unbounded result sets on a wildcard-like match.
- code-review-03: The lack of pagination is more of a design consideration than a bug.
- code-review-03: The SQL injection issue is the only problem that actually needs fixing.
- code-review-03: All the other issues identified are secondary.
- code-review-04: The race condition gets worse under load.
- code-review-04: The window between the read and the write is exactly when a context switch is likely.
- code-review-04: The plain assignment `self.value = 0` is atomic in CPython.
- code-review-04: The atomicity of that assignment in CPython is provided by the GIL.
- code-review-04: The assignment `self.value = 0` is a single bytecode-level store.
- code-review-04: The atomicity of that assignment is a CPython implementation detail, not a guarantee of the Python language.
- code-review-04: Relying on CPython's assignment atomicity is fragile and non-portable to other Python implementations.
- code-review-04: PyPy has an STM mode.
- code-review-04: Python 3.13 has a free-threaded (no-GIL) build.
- code-review-05: Parsing `ls` output is unreliable and breaks on filenames with spaces, newlines, or glob characters.
- code-review-05: `nullglob` is not available in POSIX sh.
- code-review-05: The script has no argument count check and should verify `$#` before proceeding.
- code-review-05: The script lacks `set -u`, which would have caught the empty-$1 problem.
- code-review-05: The suggested rewrite exits with status 1 and a usage message on stderr when `$#` is not 1.
- code-review-05: The suggested rewrite exits with status 1 and an error message on stderr when BACKUP_DIR is not a directory.
- code-review-06: The JSON Merge Patch spec checks the patch value's type rather than the target's type.
- code-review-06: Recursive merging of a key produces no aliasing.
- code-review-06: Deletion via None only works when merging into a dict that already exists at that key.
- code-review-06: None values inside a newly-introduced nested dict are stored literally instead of being treated as deletions.
- code-review-06: The None sentinel means different things depending on whether the key already existed as a dict.
- code-review-06: Custom Mapping subclasses and OrderedDict are examples of types not merged recursively.
- code-review-06: If base is a dict subclass, subclass-specific behavior is lost in the return value.
- code-review-06: The function has no cycle or self-reference protection.
- code-review-06: A self-referential input would cause infinite recursion.
- code-review-06: The function has no docstring and no type hints.
- code-review-06: The absence of a documented contract makes the analysis guesswork.
- code-review-06: The shallow-copy sharing and the asymmetric nested None deletion are subtler correctness traps that should at least be documented.
- code-review-07: The backoff was probably intended to be 1000 * (i + 1) or 2 ** i * 1000.
- code-review-07: Any non-retryable error, including 4xx other than 429 and exhausted retries, is converted into a null return rather than propagated.
- code-review-07: A caller that awaits withRetry(fn)() and dereferences the result without a null check will get a confusing downstream error far from the real cause.
- code-review-07: The design should probably preserve the original error, for example by attaching it, logging it, or returning a result object.
- code-review-07: The attempts parameter counts total tries rather than retries.
- code-review-07: The default value of attempts is 3.
- code-review-07: A default attempts of 3 means fn is called at most 3 times total, not 3 retries after an original attempt.
- code-review-07: The attempts naming ambiguity is not a bug per se.
- code-review-07: The attempts semantics are worth confirming with any caller who tuned the value expecting different semantics.
- code-review-07: Unbounded backoff is fine for small attempts values.
- code-review-07: The lack of cap and jitter likely never mattered because the default attempts is 3.
- code-review-07: The code loses this binding.
- code-review-07: The wrapped function is invoked as fn(...args) and is not bound to any receiver.
- code-review-07: If a hidden caller wrapped an object method expecting this to refer to the object, it will break silently or throw.
- code-review-07: An error thrown from a lost this binding would itself be swallowed by the null-returning and status-assumption behavior.
- code-review-07: The accidental issues resemble logic slips from editing retry logic without re-testing all branches.
- code-review-07: The code can be rewritten with corrected backoff, consistent failure semantics, and error preservation.
- code-review-08: CUTOFF is computed once at import time rather than per run.
- code-review-08: If the process is long-lived and clean() is called repeatedly in-process, CUTOFF never advances.
- code-review-08: The import-time CUTOFF is likely fine if the script is invoked fresh each run, such as via cron.
- code-review-08: The import-time CUTOFF computation is a latent bug rather than deliberate.
- code-review-08: os.path.getmtime works on directories.
- code-review-08: An aborted run produces only a traceback, visible if run interactively.
- code-review-08: Deleting oldest first would require sorting by mtime.
- code-review-08: os.path.getmtime follows symlinks when stating.
- code-review-08: os.remove unlinks the symlink itself rather than the target.
- code-review-08: The constants have no comments, no config, and no environment variable override.
- code-review-08: The 45-day and 500 values were previously flagged by the user as magic numbers with no rationale.
- code-review-08: The rationale for the 45-day and 500 values must come from whoever wrote the code or from data-retention/compliance requirements.
- code-review-08: The 45-day value may be tied to a legal retention policy.
- code-review-08: As written, the constants are indistinguishable from arbitrary defaults.
- code-review-08: The script has no --dry-run mode.
- code-review-08: A dry-run mode is standard practice for scheduled deletion scripts.
- code-review-08: The absence of a dry-run mode is a gap rather than a bug.
- code-review-08: Without a dry-run mode, behavior cannot be safely tested in production without risking real deletions.
- code-review-08: The variable 'removed' is computed but is not logged or returned anywhere visible in the snippet.
- code-review-08: If 'removed' is meant to feed monitoring or alerting, that plumbing is missing.
- code-review-08: The likely genuine bugs are the cap not applying to tmp/part deletions, lack of exception isolation, arbitrary deletion order under the cap, and import-time CUTOFF computation.
- debugging-01: The fix is to have get_url return f"http://{cfg['host']}:{cfg['port']}/api".
- debugging-02: The NaN value produced is what gets logged to the console.
- debugging-02: The incremented value is assigned onto the global object rather than the Timer instance.
- debugging-02: Calling .bind(this) on a regular function callback is an alternative fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` inside it is an alternative fix.
- debugging-03: The corrected loop produces the output `[3, 5, 7]`.
- debugging-03: `[3, 5, 7]` is the expected output.
- debugging-04: The file contains a non-ASCII byte 0xc3 at byte 512.
- debugging-04: UTF-8 is the most common encoding to use for such files.
- debugging-04: Passing errors="ignore" to open() also prevents a crash on malformed or unexpected bytes.
- debugging-04: Using errors="replace" can mangle unusual characters.
- debugging-04: Mangling characters is acceptable if only line counts matter rather than content.
- debugging-04: The libraries chardet and charset-normalizer can detect a file's encoding.
- debugging-04: Opening a file in binary mode with "rb" avoids decoding entirely.
- debugging-04: Counting b"\n" bytes in binary mode counts lines without decoding.
- debugging-04: Iterating over a file object opened in binary mode yields lines.
- debugging-05: The fixed make_post sets tags to list(DEFAULT_TAGS) when tags is None.
- debugging-06: The export job's timeout and exception paths should be audited to confirm they always return the connection.
- debugging-06: The current connection timeout is 30 seconds.
- debugging-06: Setting an alert on pool wait time or queue depth at a threshold below the 30s timeout would page someone with full context during the next occurrence.
- debugging-06: Correlating schedules and adding pool-utilization metrics are cheap steps that will likely distinguish contention from a leak before direct database inspection is needed.
- debugging-07: A read-after-write race on an async pipeline is the most common cause of flakes where a count is short by exactly one.
- debugging-07: Deferred commits can occur when the commit happens in a background hook or when the ORM session flush is deferred.
- debugging-07: GC pauses, container throttling, and noisy neighbors can starve a CI machine.
- debugging-07: If a test does not assert on the response of each seed call, a transient 429 or 500 can silently drop an event and only be noticed at the final assertion.
- debugging-07: Transient 429s or 500s from a shared rate limiter or connection pool exhaustion are more likely when four workers hammer the same DB or API simultaneously.
- debugging-07: pytest includes a custom assertion message in the failure log even without artifact storage.
- debugging-07: If the test never fails locally under `-n 4`, that is evidence the problem is CI-resource-contention-specific timing rather than a pure test-isolation bug.
- debugging-07: `-k test_digest_contains_all_events` filters a pytest run to a single test while still collecting the rest of the suite.
- debugging-07: If adding a short poll/retry loop before reading the digest makes the flake disappear, that strongly indicates an async or eventual-consistency race rather than a data-isolation bug.
- debugging-07: Per-test isolation can be achieved with `uuid4()` IDs or freezegun-style time control instead of hardcoded constants.
- debugging-07: Logging seed results and digest contents on failure, combined with testing whether a poll/retry removes the flake, gives the fastest diagnostic signal.
- debugging-07: That combination can distinguish a race condition from a shared-state isolation bug within one or two CI flakes.
- debugging-08: Memory growth that survives quiet nights rules out normal cache/GC churn.
- debugging-08: True garbage gets collected regardless of load.
- debugging-08: Growth that survives quiet nights points to objects still reachable from live roots, indicating an actual leak rather than mere heap pressure.
- debugging-08: A bounded cache with an unchanged bound and no code changes in a year is a less likely root cause.
- debugging-08: Eviction bugs are possible even in code that has not changed in a long time.
- debugging-08: The most likely hypothesis is a reference leak outside the cache.
- debugging-08: Idempotency or dedup maps keyed by request or webhook ID with no TTL are a possible reference leak source.
- debugging-08: ThreadLocal or MDC context leaking on pooled threads is a possible reference leak source.
- debugging-08: A reference leak explains why quiet nights do not recover memory, because the objects are held by real GC roots.
- debugging-08: A reference leak explains why the canary still grows slowly, because its own scheduled or background traffic hits the same code path.
- debugging-08: `jcmd <pid> GC.class_histogram` produces a heap class histogram on the JVM.
- debugging-08: Grepping for ThreadLocal usage in request-handling code that is not cleared on completion is a useful check.
- debugging-08: A metrics or observability cardinality leak is the second-ranked hypothesis.
- debugging-08: Using product or campaign identifiers as metric labels causes each new campaign to introduce new unique label combinations.
- debugging-08: Unique metric label combinations can live forever in the metrics registry.
- debugging-08: A metrics cardinality leak matches the correlation between memory growth and marketing campaigns.
- debugging-08: A metrics cardinality leak matches growth without webhooks because the canary still emits its own metrics.
- debugging-08: Checking the unique series count on the /metrics endpoint over a week tests the metrics cardinality hypothesis.
- debugging-08: A metrics registry size that climbs and never resets indicates the leak.
- debugging-08: The metrics registry check can be done without a heap profiler.
- debugging-08: A cache bound bug or entry-size growth is the third-ranked hypothesis.
- debugging-08: An eviction path that fails to clear a secondary index or reference to the evicted entry can cause a leak in a bounded cache.
- debugging-08: Off-heap or native allocation is the fourth-ranked hypothesis.
- debugging-08: Buffers for TLS, compression, and HTTP client connection pools are often native or off-heap.
- debugging-08: Off-heap buffers are not visible to a Java-style heap profiler.
- debugging-08: More traffic leads to more connections and buffers, matching the campaign correlation.
- debugging-08: Off-heap allocation matches the canary growing slowly from its own baseline connections.
- debugging-08: RSS growing while heap usage stays flat indicates off-heap memory growth.
- debugging-08: JVM native memory tracking is enabled with -XX:NativeMemoryTracking.
- debugging-08: pmap or smaps snapshots over time can diagnose native memory growth.
- debugging-08: Allocator fragmentation is the fifth-ranked, lower-priority hypothesis.
- debugging-08: Standard allocators such as glibc malloc do not always return freed memory to the OS.
- debugging-08: RSS can ratchet upward with allocation churn and never return to baseline due to fragmentation.
- debugging-08: More request churn produces more fragmentation.
- debugging-08: Setting MALLOC_ARENA_MAX=1 or swapping in jemalloc or tcmalloc on a test instance tests the fragmentation hypothesis.
- debugging-08: Comparing live-heap size from GC logs against process RSS helps detect fragmentation.
- explanation-01: A hash map stores key-value pairs.
- explanation-01: A hash map runs a key through a hash function that turns the key into a number.
- explanation-01: A hash map typically uses hash modulo array size (hash % array_size) to pick a slot in an underlying array.
- explanation-01: There are infinitely many possible keys but only a finite number of buckets.
- explanation-01: Because keys are infinite and buckets are finite, two keys will eventually land in the same bucket.
- explanation-01: The inevitability of collisions is the same idea as the birthday paradox.
- explanation-01: The collection in a chaining bucket is usually a linked list, and sometimes a small array or a tree.
- explanation-01: In the worst case, where everything hashes to one bucket, chaining lookup degrades to O(n) list traversal.
- explanation-01: Linear probing tries successive slots at index + 1, index + 2, and so on.
- explanation-01: Quadratic probing jumps by increasing squares, such as index + 1, index + 4, index + 9.
- explanation-01: Quadratic probing reduces clustering.
- explanation-01: Double hashing uses a second hash function to compute the probe step size.
- explanation-01: Open addressing performance degrades sharply as the table fills up because clustering gets worse.
- explanation-01: Deletion under open addressing typically requires a special deleted marker called a tombstone.
- explanation-01: Resizing and rehashing keep collisions manageable and keep operations close to O(1).
- explanation-02: PostgreSQL and MySQL support pessimistic locking via SELECT ... FOR UPDATE.
- explanation-02: Editing a document in a CMS is an example use case for optimistic locking.
- explanation-02: Most web CRUD operations, where two users rarely edit the same record simultaneously, are a use case for optimistic locking.
- explanation-03: A starting TCP sender does not know how many other connections share the path's bandwidth.
- explanation-03: A burst of excess data can overwhelm shared routers and harm every connection passing through them.
- explanation-03: Congestion collapse is the scenario where the network is congested and throughput collapses.
- explanation-03: Congestion collapse was a real problem on the early internet in the 1980s.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The receiver's advertised window limits data based on the receiver's buffer space.
- explanation-03: TCP connections now typically begin with a congestion window of 10 segments.
- explanation-03: RFC 6928 specifies the initial congestion window of 10 segments.
- explanation-03: Growing linearly from the start would waste available bandwidth, especially on high-bandwidth, high-latency links.
- explanation-03: Linear growth from the start might take a long time to reach a reasonable sending rate.
- explanation-03: If a loss is detected after congestion avoidance begins, TCP reduces its rate, for example by cutting cwnd.
- explanation-03: After a loss, TCP often re-enters a slow-start-like ramp.
- explanation-03: TCP's congestion control philosophy is to start cautious, increase while things go well, and back off sharply at signs of trouble.
- explanation-03: TCP's congestion control philosophy allows millions of independent connections to share the internet's capacity without a central coordinator.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own register state, including the instruction pointer.
- explanation-04: Sharing memory between threads requires locks or synchronization.
- explanation-04: Process creation overhead includes creating a new address space and copy-on-write page tables.
- explanation-04: Older Ruby MRI has a global interpreter lock.
- explanation-04: Gunicorn uses worker processes.
- explanation-04: nginx uses worker processes.
- explanation-04: Process boundaries can be further restricted with seccomp, containers, or chroot.
- explanation-04: With many threads, growing amounts of shared mutable state need locks.
- explanation-04: Lock contention, deadlocks, and race conditions become harder to reason about as thread count grows.
- explanation-04: Explicit message passing is often easier to get correct than shared mutable state, though slower.
- explanation-04: Processes can be distributed across machines more naturally than threads.
- explanation-05: Root references include global variables and active stack frames.
- explanation-05: Leaked-but-reachable objects cause memory usage to keep growing over time.
- explanation-05: Garbage collection prevents leaks caused by forgotten pointers.
- explanation-05: A collection can be reachable by being a static field or a singleton.
- explanation-05: A closure often captures its enclosing scope.
- explanation-05: Subscriptions to observables or streams that are not disposed can cause memory leaks.
- explanation-05: Timers or intervals holding references that are never cleared can cause memory leaks.
- explanation-06: N+1 queries are a possible cause of slowness.
- explanation-06: CPU-bound work is a possible cause of slowness.
- explanation-06: Lock contention is a possible cause of slowness.
- explanation-06: Slow serialization is a possible cause of slowness.
- explanation-06: A cache only helps with expensive, repeated reads that return the same data.
- explanation-06: A cache does nothing if the bottleneck is a single slow query that is not called often.
- explanation-06: A cache requires extra infrastructure to run.
- explanation-06: The user said they do not know the read/write mix of the service.
- explanation-06: If a workload is read-heavy but each read is already cheap, caching saves little.
- explanation-06: An indexed lookup is an example of a cheap read.
- explanation-06: Complex joins, aggregations, and external calls are examples of expensive reads.
- explanation-06: An APM tool can be used to measure request timing.
- explanation-06: Running EXPLAIN on queries reveals whether they perform full table scans or are missing indexes.
- explanation-06: A slow API is often caused by a missing index or an N+1 query.
- explanation-06: Fixing a missing index or N+1 query is a smaller fix than building a cache layer.
- explanation-06: Knowing where time is spent and the read/write split determines whether caching is worthwhile and what to cache.
- explanation-07: Sharding solves the problem of a dataset being too large for a single machine.
- explanation-07: Multi-tenant data keyed by customer_id shards cleanly at a later date with low regret.
- explanation-07: Managed Postgres offerings such as RDS, Aurora, and Cloud SQL scale to tens of terabytes.
- explanation-07: Managed Postgres offerings offer very large instance types.
- explanation-07: Team capacity is a factor in the sharding decision.
- explanation-07: Waiting risks that no natural shard key is designed into the schema, making eventual sharding a bigger rewrite.
- explanation-07: A single Postgres instance without replicas is a single point of failure.
- explanation-07: A practical middle path is to add read replicas now and monitor write IOPS, CPU, and table growth rate.
- explanation-08: Speedups from switching from JSON to a binary format vary widely, ranging from negligible to 5-10x.
- explanation-08: Two factors determine the payoff of switching to a binary format: the share of latency spent on serialization/parsing, and the payload shape.
- explanation-08: Binary formats mainly win on numeric-heavy or repetitive-schema payloads.
- explanation-08: Text-heavy or highly variable JSON payloads see much smaller gains from binary formats.
- explanation-08: Typical payload sizes can be measured by logging them.
- summarization-01: The app now starts up to 40% faster.
- summarization-02: The incident caused approximately 12% error rates for checkout.
- summarization-02: The incident lasted approximately 34 minutes.
- summarization-02: The incident ran from 09:14 to 09:48 UTC.
- summarization-02: Adding pool size to the config review checklist is a recommended remediation.
- summarization-04: The expected behavior is that PDF export downloads successfully.
- summarization-04: The expected PDF export behavior is consistent with the CSV export behavior.
- summarization-04: The issue is likely a backend/server-side problem.
- summarization-07: The assistant checked its memory for relevant context on communication preferences before responding.
- summarization-07: No relevant information was found in memory.
- summarization-07: A staging comparison of the new request batcher ran for six hours.
- summarization-07: Aside from the median latency and memory findings, the results are uncertain.
- summarization-07: One worker crashed once during the six-hour run.

Added facts (styled only):

- code-review-01: The problems are listed in order of severity.
- code-review-01: One should catch specific exceptions, or at least `Exception`, and log the failure.
- code-review-02: The corrected function returns `profile.name.toUpperCase()`.
- code-review-03: An input containing a quote followed by a semicolon can chain arbitrary additional SQL statements.
- code-review-03: The `status` parameter presumably comes from a fixed set of values, such as "pending" and "shipped".
- code-review-03: Because `status` is unvalidated, typos or bad values pass through as valid queries.
- code-review-05: The fixed version uses `BACKUP_DIR=${1:?usage: $0 <backup_dir>}` to require an argument.
- code-review-05: The fixed version uses `rm -f -- "$f"` and `gzip -- "$f"` with `--` to end option parsing.
- code-review-06: `dict(None)` raises `TypeError`.
- code-review-06: If every key in a nested dict is deleted via `None`, the parent key remains as an empty dict rather than disappearing.
- code-review-06: Replacing lists rather than merging them is consistent with merge-patch behavior.
- code-review-06: `OrderedDict` subclasses count as dicts for the merge check, while arbitrary `Mapping` implementations do not.
- code-review-06: There is no test suite for the code.
- code-review-07: When retries are exhausted, no error is thrown and no signal of failure is given.
- code-review-07: Callers cannot distinguish a successful call that produced no value from a call that gave up after exhausting retries.
- code-review-07: If `fn` can legitimately resolve to `null`, callers cannot distinguish a real result from a swallowed error.
- code-review-07: There is no timeout on `fn` itself.
- code-review-07: A hung call to `fn` blocks forever regardless of the `attempts` value.
- code-review-07: Returning `null` instead of throwing for non-retryable errors appears to be deliberate.
- code-review-07: The retry policy of what to retry looks intentional, while the error-swallowing return values and missing 5xx backoff look like defects.
- code-review-07: Fixing the implicit `undefined` and the immediate 5xx retry are safe, low-risk changes.
- code-review-08: `os.listdir(ROOT)` will throw if the directory is missing.
- code-review-08: The two most dangerous issues are the ungated `tmp-`/`.part` deletion and the missing exception handling.
- code-review-08: These two issues should be fixed before anything else.
- debugging-03: `moving_sum(values, window)` returns the sum of each window of the given size.
- debugging-03: The corrected `moving_sum` appends `sum(values[i : i + window])` to a list for each i in `range(len(values) - window + 1)` and returns that list.
- debugging-05: The fixed function copies tags into a new list when tags is not None, and otherwise uses ["draft"].
- debugging-06: Both services size their connection pools for solo use.
- debugging-06: Connections blocked on locks can exhaust the pool while waiting.
- debugging-06: A network or database blip is a possible cause.
- debugging-06: A brief DB-side stall from failover, autovacuum, or backup can spike latency for all clients at once.
- debugging-06: pg_locks should be checked specifically for lock waits.
- debugging-06: Pool exhaustion during low overall traffic indicates a leak.
- debugging-06: Failures clustering later in a run at higher batch numbers suggests a connection leak.
- debugging-06: Log retention should be increased or a wider window kept around export runs.
- debugging-06: The 5-10 minutes before the first error are needed to see what else was active.
- debugging-06: Using separate pools or a reserved connection quota for the export job would prevent analytics from starving it.
- debugging-06: Staggering the export job's schedule away from analytics' peak window is a quick fix.
- debugging-06: Separate pools and schedule staggering are quick fixes that reduce pain while investigating.
- debugging-07: Another worker's test could trigger a digest read mid-write.
- debugging-07: A shared fixture, a global table, or a missing worker_id-scoped schema are things to check for.
- debugging-07: If the digest filters by timestamp and two events land in the same millisecond, a '<' versus '<=' boundary issue could drop one event.
- debugging-07: A clock-resolution issue could drop an event.
- debugging-07: Reproducing under load should be the first narrowing step.
- debugging-07: An example repro command is `pytest tests/test_notifications.py::test_digest_contains_all_events -n 4 --count=50`.
- debugging-07: Logging what the digest endpoint actually queried, including row IDs and timestamp range, is a recommended diagnostic.
- debugging-07: Adding a small artificial delay in the seed call in a branch build can force the race.
- debugging-07: Running with `--forked` and a per-worker DB can test whether isolating the DB makes the flake vanish.
- debugging-07: If isolating the DB makes the flake vanish, that confirms contention.
- debugging-07: A retry that dumps the raw digest response and queries the DB directly for event rows before re-raising is a recommended capture technique.
- debugging-07: The retry-with-capture should ship as a temporary CI-only diagnostic build, not a permanent test change.
- debugging-07: The tight parallel-loop repro is the fastest way to confirm whether parallelism is the trigger.
- debugging-07: Confirming parallelism as the trigger should precede investing in deeper instrumentation.
- debugging-08: Two causes fit the observed behavior.
- debugging-08: Webhook traffic likely adds a second, faster leak on top of the baseline leak.
- debugging-08: The second webhook-driven leak would explain the acceleration during campaign weeks.
- debugging-08: Correlating webhook request rate against memory growth rate across several days tests the request-driven leak hypothesis.
- debugging-08: A tight correlation beyond the canary's baseline growth points to a request-driven leak.
- debugging-08: Snapshotting a production instance under load isolates the traffic-driven component.
- debugging-08: The canary and production snapshots should be taken at the same relative uptime and then diffed.
- debugging-08: Diffing the snapshots will confirm or eliminate each hypothesis in a single pass.
- explanation-01: Chaining never runs out of room.
- explanation-01: Most general-purpose hash maps use either chaining or open addressing.
- explanation-01: Java's HashMap uses one of chaining or open addressing.
- explanation-01: Python's dict uses one of chaining or open addressing.
- explanation-01: General-purpose hash maps are tuned with a good hash function and automatic resizing to keep collisions rare.
- explanation-02: An optimistic-locking update can be written as: UPDATE accounts SET balance = 100, version = version + 1 WHERE id = 1 AND version = 5.
- explanation-02: E-commerce product edits are a good fit for optimistic locking.
- explanation-03: The name 'slow start' refers to the small initial window, not the speed of growth.
- explanation-04: Browsers use separate processes per tab partly for security isolation.
- explanation-04: Examples of components needing independent lifecycles include a database connection pool, a plugin, and a sandboxed script.
- explanation-06: A cache only helps if the database is the bottleneck.
- explanation-06: The request path can be broken down into app logic, network, and database time.
- explanation-06: The read/write ratio can be checked in query logs or database metrics.
- explanation-06: Redis is an example of a cache.
- explanation-07: Sharding does not solve disk usage problems.
- explanation-07: Connections, IOPS, and CPU are limits worth checking, not just gigabytes of storage.
- explanation-07: Instance size, indexing, and query tuning should be exhausted before considering sharding.
- explanation-07: Growth should be tracked monthly and extrapolated before committing to an architecture.
- explanation-07: Sharding architecture is hard to reverse.
- explanation-07: A single hot table or one runaway tenant is cheaper to fix with partitioning or a targeted read replica than with a full shard rollout.
- explanation-07: Partitioning and read replicas are lighter fixes that are distinct from sharding.
- explanation-08: Protobuf and msgpack are binary serialization formats.
- explanation-08: Binary formats typically reduce payload size by 20-50%.
- explanation-08: Binary formats reduce serialization CPU time by more than they reduce payload size.
- explanation-08: Average and p99 payload size for representative requests can be measured.
- summarization-01: The app now starts about 40% faster.
- summarization-01: Each button's tooltip shows the keyboard shortcut for its action.
- summarization-03: Moving thumbnail generation to a background queue would cut 800ms to 3s off every upload request.
- summarization-04: The PDF export request fails silently.
- summarization-06: A restart fixed the error rates.
- summarization-07: All findings other than the median latency reduction are provisional.
- summarization-07: The recommendation is to profile memory before rollout.
- summarization-08: The template gallery observation needs more data before it counts as a finding.

### concise

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 31 | 24 | 0.774 | 14 | 0 |
| code-review-02 | 18 | 12 | 0.667 | 15 | 1 |
| code-review-03 | 28 | 19 | 0.679 | 21 | 2 |
| code-review-04 | 24 | 14 | 0.583 | 13 | 0 |
| code-review-05 | 32 | 27 | 0.844 | 29 | 5 |
| code-review-06 | 43 | 29 | 0.674 | 24 | 2 |
| code-review-07 | 56 | 44 | 0.786 | 32 | 5 |
| code-review-08 | 54 | 38 | 0.704 | 24 | 1 |
| debugging-01 | 6 | 5 | 0.833 | 6 | 2 |
| debugging-02 | 14 | 10 | 0.714 | 8 | 0 |
| debugging-03 | 12 | 10 | 0.833 | 6 | 0 |
| debugging-04 | 15 | 6 | 0.4 | 9 | 0 |
| debugging-05 | 15 | 15 | 1.0 | 14 | 1 |
| debugging-06 | 24 | 19 | 0.792 | 35 | 16 |
| debugging-07 | 30 | 19 | 0.633 | 27 | 10 |
| debugging-08 | 50 | 31 | 0.62 | 18 | 2 |
| explanation-01 | 43 | 24 | 0.558 | 20 | 1 |
| explanation-02 | 28 | 20 | 0.714 | 19 | 0 |
| explanation-03 | 38 | 17 | 0.447 | 16 | 2 |
| explanation-04 | 41 | 30 | 0.732 | 23 | 3 |
| explanation-05 | 19 | 14 | 0.737 | 9 | 0 |
| explanation-06 | 32 | 21 | 0.656 | 19 | 1 |
| explanation-07 | 28 | 22 | 0.786 | 32 | 16 |
| explanation-08 | 15 | 7 | 0.467 | 12 | 1 |
| summarization-01 | 5 | 4 | 0.8 | 6 | 1 |
| summarization-02 | 14 | 13 | 0.929 | 15 | 5 |
| summarization-03 | 13 | 12 | 0.923 | 13 | 0 |
| summarization-04 | 16 | 13 | 0.812 | 12 | 1 |
| summarization-05 | 8 | 7 | 0.875 | 7 | 1 |
| summarization-06 | 12 | 12 | 1.0 | 13 | 1 |
| summarization-07 | 18 | 15 | 0.833 | 15 | 3 |
| summarization-08 | 19 | 18 | 0.947 | 18 | 2 |

Median fraction: 0.756 over 32 scored pairs.

Median additions: 1.0 over 32 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python pitfall.
- code-review-01: The function does not check whether `"member"` is already in `roles`.
- code-review-01: If `roles` already contains `"member"`, it gets added a second time.
- code-review-01: The fixed version raises `ValueError("name is required")` when `name` is falsy.
- code-review-01: The fixed version appends `"member"` only if it is not already in `roles`.
- code-review-01: The fixed version avoids silently swallowing exceptions, leaving handling to the caller.
- code-review-01: The fixed version prevents duplicate roles.
- code-review-02: The `async` keyword makes `loadProfile` return a `Promise`.
- code-review-02: The promise returned by `loadProfile` rejects synchronously due to the `TypeError` rather than because of awaited async work.
- code-review-02: The `.then` chain is neither returned nor awaited, so any rejection becomes an unhandled promise rejection.
- code-review-02: The code does not validate that `data` has a `name` property.
- code-review-02: If the API returns an unexpected value such as an error object, `.name` could be `undefined` and `.toUpperCase()` would throw.
- code-review-02: The fixed version removes the unused `profile` variable and the unused promise chain.
- code-review-03: A caller passing user-controlled input such as `customer_name = "x' OR '1'='1"` can read, modify, or delete arbitrary data.
- code-review-03: sqlite3 uses `?` as its placeholder.
- code-review-03: psycopg2 uses `%s` as its placeholder.
- code-review-03: MySQLdb uses `%s` as its placeholder.
- code-review-03: If `customer_name` or `status` is not a string (e.g. `None`), the `+` concatenation raises a `TypeError`.
- code-review-03: The resulting `TypeError` produces a confusing stack trace rather than a clear error.
- code-review-03: Whether the lack of error handling is acceptable depends on the application's conventions.
- code-review-03: The lack of pagination is more of a design consideration than a bug.
- code-review-03: The SQL injection issue is the only problem that actually needs fixing.
- code-review-04: The lost-update bug is a classic TOCTOU/lost-update bug.
- code-review-04: The race condition gets worse under load.
- code-review-04: The window between the read and the write is exactly when a context switch is likely.
- code-review-04: The plain assignment `self.value = 0` is atomic in CPython.
- code-review-04: The atomicity of that assignment in CPython is provided by the GIL.
- code-review-04: The assignment `self.value = 0` is a single bytecode-level store.
- code-review-04: The atomicity of that assignment is a CPython implementation detail, not a guarantee of the Python language.
- code-review-04: Relying on CPython's assignment atomicity is fragile and non-portable to other Python implementations.
- code-review-04: PyPy has an STM mode.
- code-review-04: Python 3.13 has a free-threaded (no-GIL) build.
- code-review-05: The suggested rewrite uses `#!/bin/sh` with `set -eu`.
- code-review-05: The suggested rewrite exits with status 1 and a usage message on stderr when `$#` is not 1.
- code-review-05: The suggested rewrite exits with status 1 and an error message on stderr when BACKUP_DIR is not a directory.
- code-review-05: The suggested rewrite uses `rm -f -- *.tmp` instead of `rm -rf *.tmp`.
- code-review-05: The suggested rewrite calls `gzip -- "$f"` with the filename quoted.
- code-review-06: Calling `.items()` on a string raises AttributeError.
- code-review-06: The function resembles the JSON Merge Patch algorithm defined in RFC 7386.
- code-review-06: The JSON Merge Patch spec checks the patch value's type rather than the target's type.
- code-review-06: Recursive merging of a key produces no aliasing.
- code-review-06: Deletion via None only works when merging into a dict that already exists at that key.
- code-review-06: None values inside a newly-introduced nested dict are stored literally instead of being treated as deletions.
- code-review-06: The None sentinel means different things depending on whether the key already existed as a dict.
- code-review-06: JSON Merge Patch uses None (null) as a delete sentinel.
- code-review-06: Custom Mapping subclasses and OrderedDict are examples of types not merged recursively.
- code-review-06: If base is a dict subclass, subclass-specific behavior is lost in the return value.
- code-review-06: Failures surface as generic AttributeError or TypeError deep in the recursion rather than as a clear error at the call site.
- code-review-06: The function has no docstring and no type hints.
- code-review-06: The absence of a documented contract makes the analysis guesswork.
- code-review-06: The shallow-copy sharing and the asymmetric nested None deletion are subtler correctness traps that should at least be documented.
- code-review-07: Any non-retryable error, including 4xx other than 429 and exhausted retries, is converted into a null return rather than propagated.
- code-review-07: A caller that awaits withRetry(fn)() and dereferences the result without a null check will get a confusing downstream error far from the real cause.
- code-review-07: The default value of attempts is 3.
- code-review-07: The lack of cap and jitter likely never mattered because the default attempts is 3.
- code-review-07: The code loses this binding.
- code-review-07: The wrapped function is invoked as fn(...args) and is not bound to any receiver.
- code-review-07: If a hidden caller wrapped an object method expecting this to refer to the object, it will break silently or throw.
- code-review-07: An error thrown from a lost this binding would itself be swallowed by the null-returning and status-assumption behavior.
- code-review-07: The accidental issues resemble logic slips from editing retry logic without re-testing all branches.
- code-review-07: The null-swallowing contract should be confirmed explicitly before relying on it further.
- code-review-07: The code can be rewritten with corrected backoff, consistent failure semantics, and error preservation.
- code-review-07: Changing the return contract should be a deliberate, separate decision rather than a quiet fix.
- code-review-08: os.path.getmtime works on directories.
- code-review-08: An aborted run produces only a traceback, visible if run interactively.
- code-review-08: Because the script runs on a schedule, errors are unlikely to be noticed unless someone checks logs.
- code-review-08: Deleting oldest first would require sorting by mtime.
- code-review-08: os.path.getmtime follows symlinks when stating.
- code-review-08: os.remove unlinks the symlink itself rather than the target.
- code-review-08: A broken symlink causes getmtime to raise FileNotFoundError and crash the run.
- code-review-08: The constants have no comments, no config, and no environment variable override.
- code-review-08: The 45-day and 500 values were previously flagged by the user as magic numbers with no rationale.
- code-review-08: The rationale for the 45-day and 500 values must come from whoever wrote the code or from data-retention/compliance requirements.
- code-review-08: The 45-day value may be tied to a legal retention policy.
- code-review-08: A dry-run mode is standard practice for scheduled deletion scripts.
- code-review-08: The absence of a dry-run mode is a gap rather than a bug.
- code-review-08: The variable 'removed' is computed but is not logged or returned anywhere visible in the snippet.
- code-review-08: If 'removed' is meant to feed monitoring or alerting, that plumbing is missing.
- code-review-08: The 45-day cutoff, the 500-item cap as a safety brake, and deleting tmp-/.part files at all are likely deliberate business logic needing confirmation.
- debugging-01: The fix is to have get_url return f"http://{cfg['host']}:{cfg['port']}/api".
- debugging-02: The NaN value produced is what gets logged to the console.
- debugging-02: The incremented value is assigned onto the global object rather than the Timer instance.
- debugging-02: Calling .bind(this) on a regular function callback is an alternative fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` inside it is an alternative fix.
- debugging-03: The corrected loop produces the output `[3, 5, 7]`.
- debugging-03: `[3, 5, 7]` is the expected output.
- debugging-04: The file contains a non-ASCII byte 0xc3 at byte 512.
- debugging-04: The 0xc3 byte likely represents an accented character.
- debugging-04: UTF-8 is the most common encoding to use for such files.
- debugging-04: Using errors="replace" can mangle unusual characters.
- debugging-04: Mangling characters is acceptable if only line counts matter rather than content.
- debugging-04: The libraries chardet and charset-normalizer can detect a file's encoding.
- debugging-04: Opening a file in binary mode with "rb" avoids decoding entirely.
- debugging-04: Counting b"\n" bytes in binary mode counts lines without decoding.
- debugging-04: Iterating over a file object opened in binary mode yields lines.
- debugging-06: The export job and the analytics service share a database.
- debugging-06: If the combined pool sizes of the export job, the analytics service, and other clients exceed the database's max_connections, requests queue at the database even when each service's own pool appears to have headroom.
- debugging-06: Pool-utilization metrics worth adding include in-use count, wait queue depth, and wait time.
- debugging-06: Setting an alert on pool wait time or queue depth at a threshold below the 30s timeout would page someone with full context during the next occurrence.
- debugging-06: Correlating schedules and adding pool-utilization metrics are cheap steps that will likely distinguish contention from a leak before direct database inspection is needed.
- debugging-07: A read-after-write race on an async pipeline is the most common cause of flakes where a count is short by exactly one.
- debugging-07: Read-after-write races typically only appear when the system is under load.
- debugging-07: Deferred commits can occur when the commit happens in a background hook or when the ORM session flush is deferred.
- debugging-07: GC pauses, container throttling, and noisy neighbors can starve a CI machine.
- debugging-07: If a test does not assert on the response of each seed call, a transient 429 or 500 can silently drop an event and only be noticed at the final assertion.
- debugging-07: Transient 429s or 500s from a shared rate limiter or connection pool exhaustion are more likely when four workers hammer the same DB or API simultaneously.
- debugging-07: pytest includes a custom assertion message in the failure log even without artifact storage.
- debugging-07: If the test only flakes when the full suite runs, shared fixture or account contamination from other tests is the likely cause rather than a bug in the test in isolation.
- debugging-07: `-k test_digest_contains_all_events` filters a pytest run to a single test while still collecting the rest of the suite.
- debugging-07: Per-test isolation can be achieved with `uuid4()` IDs or freezegun-style time control instead of hardcoded constants.
- debugging-07: A race condition and a shared-state isolation bug require different fixes: adding a read-your-writes guarantee versus isolating test fixtures.
- debugging-08: True garbage gets collected regardless of load.
- debugging-08: A canary instance with no webhooks that still grows rules out causes strictly tied to webhook handling.
- debugging-08: Idempotency or dedup maps keyed by request or webhook ID with no TTL are a possible reference leak source.
- debugging-08: `jcmd <pid> GC.class_histogram` produces a heap class histogram on the JVM.
- debugging-08: A metrics or observability cardinality leak is the second-ranked hypothesis.
- debugging-08: A metrics cardinality leak matches growth without webhooks because the canary still emits its own metrics.
- debugging-08: A cache bound bug or entry-size growth is the third-ranked hypothesis.
- debugging-08: Off-heap or native allocation is the fourth-ranked hypothesis.
- debugging-08: Buffers for TLS, compression, and HTTP client connection pools are often native or off-heap.
- debugging-08: More traffic leads to more connections and buffers, matching the campaign correlation.
- debugging-08: Off-heap allocation matches the canary growing slowly from its own baseline connections.
- debugging-08: JVM native memory tracking is enabled with -XX:NativeMemoryTracking.
- debugging-08: pmap or smaps snapshots over time can diagnose native memory growth.
- debugging-08: Allocator fragmentation is the fifth-ranked, lower-priority hypothesis.
- debugging-08: Standard allocators such as glibc malloc do not always return freed memory to the OS.
- debugging-08: RSS can ratchet upward with allocation churn and never return to baseline due to fragmentation.
- debugging-08: More request churn produces more fragmentation.
- debugging-08: Setting MALLOC_ARENA_MAX=1 or swapping in jemalloc or tcmalloc on a test instance tests the fragmentation hypothesis.
- debugging-08: Comparing live-heap size from GC logs against process RSS helps detect fragmentation.
- explanation-01: A hash map stores key-value pairs.
- explanation-01: A hash map typically uses hash modulo array size (hash % array_size) to pick a slot in an underlying array.
- explanation-01: A slot in a hash map's underlying array is called a bucket.
- explanation-01: Collisions are not a bug.
- explanation-01: Collisions are unavoidable.
- explanation-01: There are infinitely many possible keys but only a finite number of buckets.
- explanation-01: Because keys are infinite and buckets are finite, two keys will eventually land in the same bucket.
- explanation-01: The inevitability of collisions is the same idea as the birthday paradox.
- explanation-01: Every hash map needs a strategy for handling collisions.
- explanation-01: The collection in a chaining bucket is usually a linked list, and sometimes a small array or a tree.
- explanation-01: In the worst case, where everything hashes to one bucket, chaining lookup degrades to O(n) list traversal.
- explanation-01: Linear probing tries successive slots at index + 1, index + 2, and so on.
- explanation-01: Quadratic probing jumps by increasing squares, such as index + 1, index + 4, index + 9.
- explanation-01: Quadratic probing reduces clustering.
- explanation-01: Double hashing uses a second hash function to compute the probe step size.
- explanation-01: Open addressing needs resizing sooner than chaining at high load factors.
- explanation-01: Tuning open addressing involves resizing and rehashing proactively.
- explanation-01: Both chaining and open addressing rely on resizing the underlying array and rehashing all entries once the load factor gets too high.
- explanation-01: Resizing and rehashing keep collisions manageable and keep operations close to O(1).
- explanation-02: PostgreSQL and MySQL support pessimistic locking via SELECT ... FOR UPDATE.
- explanation-02: Seat reservations are an example use case for pessimistic locking.
- explanation-02: Pessimistic locking is also good when the work between read and write is short, keeping lock hold time low.
- explanation-02: Most web CRUD operations, where two users rarely edit the same record simultaneously, are a use case for optimistic locking.
- explanation-02: Optimistic locking works well in stateless and distributed systems.
- explanation-02: Holding a database lock across a network round-trip or user think-time would be costly.
- explanation-02: As a rule of thumb, high contention with a short critical section favors pessimistic locking.
- explanation-02: As a rule of thumb, low contention with long user-facing gaps between read and write favors optimistic locking.
- explanation-03: A starting TCP sender does not know how many other connections share the path's bandwidth.
- explanation-03: A starting TCP sender does not know how much buffering exists in routers along the path.
- explanation-03: If a sender transmitted as fast as the receiver's window allowed, it could send more data than the network path can handle.
- explanation-03: A burst of excess data can overwhelm shared routers and harm every connection passing through them.
- explanation-03: Congestion collapse is the scenario where the network is congested and throughput collapses.
- explanation-03: Congestion collapse was a real problem on the early internet in the 1980s.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The receiver's advertised window limits data based on the receiver's buffer space.
- explanation-03: Historically, TCP connections began with a congestion window of 1 segment.
- explanation-03: TCP connections now typically begin with a congestion window of 10 segments.
- explanation-03: RFC 6928 specifies the initial congestion window of 10 segments.
- explanation-03: During slow start, the sender increases cwnd by roughly one segment for each ACK received.
- explanation-03: Each round trip generates ACKs for everything sent during that round.
- explanation-03: Congestion avoidance uses linear growth instead of exponential growth.
- explanation-03: Growing linearly from the start would waste available bandwidth, especially on high-bandwidth, high-latency links.
- explanation-03: Linear growth from the start might take a long time to reach a reasonable sending rate.
- explanation-03: The name 'slow start' is misleading because the mechanism is not sluggish.
- explanation-03: Slow start is slow only relative to sending at full speed immediately.
- explanation-03: If a loss is detected after congestion avoidance begins, TCP reduces its rate, for example by cutting cwnd.
- explanation-03: After a loss, TCP often re-enters a slow-start-like ramp.
- explanation-03: TCP's congestion control philosophy allows millions of independent connections to share the internet's capacity without a central coordinator.
- explanation-04: Sharing memory between threads requires locks or synchronization.
- explanation-04: Process creation overhead includes creating a new address space and copy-on-write page tables.
- explanation-04: Examples of work worth isolating in a process include processing untrusted input, running third-party plugins, and rendering a webpage.
- explanation-04: Gunicorn uses worker processes.
- explanation-04: nginx uses worker processes.
- explanation-04: Process boundaries can be further restricted with seccomp, containers, or chroot.
- explanation-04: With many threads, growing amounts of shared mutable state need locks.
- explanation-04: Lock contention, deadlocks, and race conditions become harder to reason about as thread count grows.
- explanation-04: Explicit message passing is often easier to get correct than shared mutable state, though slower.
- explanation-04: Processes can be distributed across machines more naturally than threads.
- explanation-04: Threads or async are recommended for I/O-bound concurrency within a single logical unit where shared memory is convenient and low overhead matters.
- explanation-05: Root references include global variables and active stack frames.
- explanation-05: Garbage collection prevents leaks caused by forgotten pointers.
- explanation-05: A collection can be reachable by being a static field or a singleton.
- explanation-05: Long-lived objects that listeners attach to include event emitters, DOM elements, and global buses.
- explanation-05: A closure often captures its enclosing scope.
- explanation-06: Lock contention is a possible cause of slowness.
- explanation-06: Slow serialization is a possible cause of slowness.
- explanation-06: A cache requires extra infrastructure to run.
- explanation-06: The user said they do not know the read/write mix of the service.
- explanation-06: If a workload is read-heavy but each read is already cheap, caching saves little.
- explanation-06: An indexed lookup is an example of a cheap read.
- explanation-06: Complex joins, aggregations, and external calls are examples of expensive reads.
- explanation-06: Slow query logs can be checked to diagnose database performance.
- explanation-06: Running EXPLAIN on queries reveals whether they perform full table scans or are missing indexes.
- explanation-06: A slow API is often caused by a missing index or an N+1 query.
- explanation-06: Fixing a missing index or N+1 query is a smaller fix than building a cache layer.
- explanation-07: Sharding solves the problem of a dataset being too large for a single machine.
- explanation-07: Managed Postgres offerings such as RDS, Aurora, and Cloud SQL scale to tens of terabytes.
- explanation-07: Managed Postgres offerings offer very large instance types.
- explanation-07: Team capacity is a factor in the sharding decision.
- explanation-07: A single Postgres instance without replicas is a single point of failure.
- explanation-07: A concrete trigger, such as sustained write saturation or nearing the maximum vertical instance size, should be chosen for revisiting sharding.
- explanation-08: Speedups from switching from JSON to a binary format vary widely, ranging from negligible to 5-10x.
- explanation-08: Two factors determine the payoff of switching to a binary format: the share of latency spent on serialization/parsing, and the payload shape.
- explanation-08: Request latency is composed of serialization/parsing plus network, database queries, and business logic.
- explanation-08: Binary formats mainly win on numeric-heavy or repetitive-schema payloads.
- explanation-08: Text-heavy or highly variable JSON payloads see much smaller gains from binary formats.
- explanation-08: A flamegraph or simple timers around JSON.parse/stringify equivalents can be used to profile serialization time.
- explanation-08: Typical payload sizes can be measured by logging them.
- explanation-08: Profiling the request path and measuring payload sizes takes roughly an hour of work.
- summarization-01: The app now starts up to 40% faster.
- summarization-02: The incident ran from 09:14 to 09:48 UTC.
- summarization-03: The background worker pool would update the record after generating thumbnails.
- summarization-04: The expected PDF export behavior is consistent with the CSV export behavior.
- summarization-04: The issue was reproduced on the latest version of Firefox.
- summarization-04: The issue is likely a backend/server-side problem.
- summarization-05: Ada is assigned to run a migration dry run for the payments database.
- summarization-07: The assistant checked its memory for relevant context on communication preferences before responding.
- summarization-07: No relevant information was found in memory.
- summarization-07: Confirming the tail latency result requires a production-like test.
- summarization-08: The recommendation is to prioritize investigating the link between the progress bar and abandonment.

Added facts (styled only):

- code-review-02: The corrected version awaits `res.json()` before returning `profile.name.toUpperCase()`.
- code-review-03: `SELECT *` obscures what the function actually depends on.
- code-review-03: The caller has no indication of the failure mode.
- code-review-05: If no .log files exist, `ls *.log` fails and its error output is passed into the loop as a literal string.
- code-review-05: If $BACKUP_DIR or a filename starts with `-`, it could be interpreted as an option by `cd`, `rm`, or `gzip`, creating an argument injection risk.
- code-review-05: `echo Cleaned $BACKUP_DIR` is unquoted, which is a minor issue but inconsistent with the rest.
- code-review-05: The suggested fix is to use `cd "$BACKUP_DIR" || exit 1`.
- code-review-05: The suggested fix is to guard against no-match globs using `shopt -s nullglob` in bash, or a `[ -e ... ]` check in POSIX sh.
- code-review-06: The shallow-copy issue and the type-mismatch crash are straightforward correctness bugs that should be fixed regardless of original intent.
- code-review-06: Changing the None-as-delete semantics would break callers.
- code-review-07: A legitimate null return from fn is indistinguishable from a failure.
- code-review-07: The backoff growth is linear rather than exponential, which limits how large the waits become.
- code-review-07: The function has no cancellation or AbortSignal support.
- code-review-07: Callers cannot distinguish 'fn returned null/undefined' from 'call failed after retries'.
- code-review-07: Code that checks the return value for truthiness will silently treat failures as successes.
- code-review-08: The hardcoded `ROOT` path is reasonable for a single-purpose internal script.
- debugging-01: The fix should be applied to line 4.
- debugging-01: The corrected line 4 is: return f"http://{cfg['host']}:{cfg['port']}/api"
- debugging-05: In the fixed code, tags is set to list(tags if tags is not None else DEFAULT_TAGS).
- debugging-06: pgbouncer is a form of connection pool that can be shared between services.
- debugging-06: Locks, table scans, vacuum, and analytics aggregation are examples of long-running or blocking operations.
- debugging-06: Retries add load at the moment the pool is already stressed.
- debugging-06: The failures occur about once a week rather than every night.
- debugging-06: A slowly developing connection leak is consistent with weekly rather than nightly failures.
- debugging-06: Retry attempt 2 also timed out.
- debugging-06: Attempt 2 timing out suggests the underlying contention had not cleared 30 seconds later.
- debugging-06: Pool metrics can be obtained from pgbouncer or from an app pool library that exposes stats.
- debugging-06: Application logs alone do not provide pool metrics.
- debugging-06: Slow query logging and pg_stat_activity snapshots can be enabled during the failure window.
- debugging-06: A cron job dumping pg_stat_activity every 30 seconds overnight would capture the offending long-running query or lock.
- debugging-06: Blocking and blocked sessions can be identified by joining pg_locks with pg_stat_activity.
- debugging-06: Auditing connection release means verifying that all DB access paths return connections in finally blocks.
- debugging-06: Structured logging at DB connection checkout should record timestamp, caller, and pool size at time of request.
- debugging-06: Such structured logging would reveal what is holding the pool without depending on rotated logs.
- debugging-06: Sampling pg_stat_activity continuously overnight is the highest-leverage first step.
- debugging-07: A test isolation leak under parallel workers is the prime suspect because the failure only reproduces in parallel and not serially.
- debugging-07: Async persistence paths that cause this include queue-to-worker-to-DB pipelines and write-to-read-replica lag.
- debugging-07: Clock resolution or skew can cause an event created in the same millisecond to fall outside the digest's time window.
- debugging-07: A fixture assumed to reset (counter, in-memory list, cache) may actually be process- or module-level and bleed across tests when workers reuse processes.
- debugging-07: If parallel workers share a DB or file without per-worker schemas, that is the likely cause of the failure.
- debugging-07: On-failure logging of the digest response, event IDs, and timestamps can be added via a pytest hook.
- debugging-07: Fixtures with `scope="session"` or `scope="module"` combined with pytest-xdist create one instance per worker process.
- debugging-07: The test never fails when run serially.
- debugging-07: The most likely cause is shared state not scoped per xdist worker.
- debugging-07: The second most likely cause is an eventual-consistency race in event ingestion.
- debugging-08: The canary is the cleanest reproduction of the leak because the webhook variable is removed.
- debugging-08: Eclipse MAT and jmap can be used to take and analyze heap dumps and diff dominator trees.
- explanation-01: Open addressing has no extra memory overhead.
- explanation-03: A burst of packet loss wastes bandwidth.
- explanation-03: When packet loss is detected, the sender backs off and switches to a slower growth mode.
- explanation-04: Process context switching is more expensive because it requires swapping the memory map.
- explanation-04: Independent restartability is useful for supervisor patterns such as systemd and Erlang-style "let it crash".
- explanation-04: A game engine's render and physics loops are an example where threads are preferable.
- explanation-06: If data changes constantly, a cache adds complexity without much payoff.
- explanation-07: Hardware suitable for large single-instance Postgres includes NVMe storage and enough RAM for the working set.
- explanation-07: Sharding requires application-level routing logic.
- explanation-07: If the primary is not saturated, sharding provides no benefit.
- explanation-07: Uncertainty about growth rate is itself informative for the decision.
- explanation-07: Decisions made under uncertainty should be reversible and cheap.
- explanation-07: Sharding is hard to reverse.
- explanation-07: Metrics worth tracking are disk growth rate, primary CPU/IOPS, replication lag, and connection saturation.
- explanation-07: Postgres has native table partitioning.
- explanation-07: Table partitioning and read replicas solve most scaling problems up to several terabytes and high read load.
- explanation-07: Table partitioning and read replicas avoid the distributed-systems cost of sharding.
- explanation-07: Sharding now would entangle application code with shard-routing logic.
- explanation-07: Cross-shard transactions become eventual-consistency problems.
- explanation-07: Sharding under pressure leaves less time to pick a good shard key.
- explanation-07: A poorly chosen shard key leads to hot shards.
- explanation-07: A middle-ground option is to pick a shard key such as tenant_id now without sharding.
- explanation-07: Picking a shard key early is cheap insurance against the risk of waiting.
- explanation-08: Profiling a representative endpoint yields payload sizes at p50 and p95 for typical requests and responses.
- summarization-01: Cold start time was reduced by approximately 40%.
- summarization-02: The problem went undetected until it caused user-facing impact.
- summarization-02: Engineers were paged 7 minutes after the incident onset.
- summarization-02: The rollback was completed in 34 minutes.
- summarization-02: No process change is needed for detection and response.
- summarization-02: The recommendation is to add pool size and other capacity-sensitive values to the config review checklist.
- summarization-04: PDF export fails silently on the Reports page.
- summarization-05: Ada is to confirm that the dry run happens before Thursday.
- summarization-06: A restart restored the checkout service.
- summarization-07: Everything other than the median latency result is uncertain.
- summarization-07: The recommendation is to profile memory before drawing conclusions on tail latency and stability.
- summarization-07: The recommendation is to investigate the crash before drawing conclusions on tail latency and stability.
- summarization-08: The abandonment outcome is concrete enough to warrant a fix.
- summarization-08: Non-use of the template gallery is not counted as a finding.

### developer-docs

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 31 | 23 | 0.742 | 19 | 3 |
| code-review-02 | 18 | 14 | 0.778 | 16 | 2 |
| code-review-03 | 28 | 14 | 0.5 | 19 | 5 |
| code-review-04 | 24 | 15 | 0.625 | 20 | 6 |
| code-review-05 | 32 | 25 | 0.781 | 33 | 4 |
| code-review-06 | 43 | 24 | 0.558 | 35 | 4 |
| code-review-07 | 56 | 42 | 0.75 | 35 | 5 |
| code-review-08 | 54 | 41 | 0.759 | 34 | 6 |
| debugging-01 | 6 | 6 | 1.0 | 9 | 0 |
| debugging-02 | 14 | 8 | 0.571 | 8 | 0 |
| debugging-03 | 12 | 12 | 1.0 | 9 | 2 |
| debugging-04 | 15 | 9 | 0.6 | 16 | 2 |
| debugging-05 | 15 | 14 | 0.933 | 17 | 0 |
| debugging-06 | 24 | 15 | 0.625 | 33 | 15 |
| debugging-07 | 30 | 14 | 0.467 | 21 | 2 |
| debugging-08 | 50 | 18 | 0.36 | 29 | 11 |
| explanation-01 | 43 | 32 | 0.744 | 26 | 0 |
| explanation-02 | 28 | 20 | 0.714 | 30 | 4 |
| explanation-03 | 38 | 25 | 0.658 | 26 | 4 |
| explanation-04 | 41 | 29 | 0.707 | 32 | 3 |
| explanation-05 | 19 | 13 | 0.684 | 13 | 0 |
| explanation-06 | 32 | 19 | 0.594 | 22 | 4 |
| explanation-07 | 28 | 19 | 0.679 | 19 | 5 |
| explanation-08 | 15 | 8 | 0.533 | 21 | 13 |
| summarization-01 | 5 | 4 | 0.8 | 5 | 2 |
| summarization-02 | 14 | 14 | 1.0 | 9 | 0 |
| summarization-03 | 13 | 13 | 1.0 | 12 | 0 |
| summarization-04 | 16 | 13 | 0.812 | 11 | 0 |
| summarization-05 | 8 | 7 | 0.875 | 11 | 1 |
| summarization-06 | 12 | 12 | 1.0 | 12 | 1 |
| summarization-07 | 18 | 15 | 0.833 | 11 | 0 |
| summarization-08 | 19 | 16 | 0.842 | 20 | 1 |

Median fraction: 0.743 over 32 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python pitfall.
- code-review-01: The function does not check whether `"member"` is already in `roles`.
- code-review-01: If `roles` already contains `"member"`, it gets added a second time.
- code-review-01: The fixed version raises `ValueError("name is required")` when `name` is falsy.
- code-review-01: The fixed version uses `roles = list(roles) if roles else []`.
- code-review-01: The fixed version appends `"member"` only if it is not already in `roles`.
- code-review-01: The fixed version avoids silently swallowing exceptions, leaving handling to the caller.
- code-review-01: The fixed version prevents duplicate roles.
- code-review-02: The `async` keyword makes `loadProfile` return a `Promise`.
- code-review-02: The promise returned by `loadProfile` rejects synchronously due to the `TypeError` rather than because of awaited async work.
- code-review-02: The code does not validate that `data` has a `name` property.
- code-review-02: If the API returns an unexpected value such as an error object, `.name` could be `undefined` and `.toUpperCase()` would throw.
- code-review-03: The SQL injection vulnerability is critical.
- code-review-03: sqlite3 uses `?` as its placeholder.
- code-review-03: psycopg2 uses `%s` as its placeholder.
- code-review-03: MySQLdb uses `%s` as its placeholder.
- code-review-03: `SELECT *` breaks silently if columns are added, reordered, or removed.
- code-review-03: If `customer_name` or `status` is not a string (e.g. `None`), the `+` concatenation raises a `TypeError`.
- code-review-03: The resulting `TypeError` produces a confusing stack trace rather than a clear error.
- code-review-03: Whether the lack of error handling is acceptable depends on the application's conventions.
- code-review-03: It is worth considering whether callers expect a wrapped or logged exception.
- code-review-03: The function has no pagination or limit.
- code-review-03: The function could return unbounded result sets on a wildcard-like match.
- code-review-03: The lack of pagination is more of a design consideration than a bug.
- code-review-03: The SQL injection issue is the only problem that actually needs fixing.
- code-review-03: All the other issues identified are secondary.
- code-review-04: The race condition gets worse under load.
- code-review-04: The window between the read and the write is exactly when a context switch is likely.
- code-review-04: The plain assignment `self.value = 0` is atomic in CPython.
- code-review-04: The atomicity of that assignment in CPython is provided by the GIL.
- code-review-04: The assignment `self.value = 0` is a single bytecode-level store.
- code-review-04: The atomicity of that assignment is a CPython implementation detail, not a guarantee of the Python language.
- code-review-04: Relying on CPython's assignment atomicity is fragile and non-portable to other Python implementations.
- code-review-04: PyPy has an STM mode.
- code-review-04: Python 3.13 has a free-threaded (no-GIL) build.
- code-review-05: If no .log files exist, `*.log` will not expand unless `nullglob` is set.
- code-review-05: `nullglob` is not available in POSIX sh.
- code-review-05: If no .log files exist, `ls *.log` prints an error to stderr.
- code-review-05: The script has no argument count check and should verify `$#` before proceeding.
- code-review-05: The suggested rewrite exits with status 1 and a usage message on stderr when `$#` is not 1.
- code-review-05: The suggested rewrite exits with status 1 and an error message on stderr when BACKUP_DIR is not a directory.
- code-review-05: The key fixes are argument and directory validation before destructive actions, `set -eu`, quoted variables, removal of the `ls` parsing anti-pattern, and a glob-no-match guard.
- code-review-06: The function resembles the JSON Merge Patch algorithm defined in RFC 7386.
- code-review-06: The JSON Merge Patch spec checks the patch value's type rather than the target's type.
- code-review-06: Recursive merging of a key produces no aliasing.
- code-review-06: When the override introduces a new key whose value is a dict, the code takes the `else` branch.
- code-review-06: The `else` branch assigns `merged[key] = value`, storing the value by reference.
- code-review-06: Storing the override value by reference makes the merged dict share the nested dict object with the override.
- code-review-06: The aliasing of newly-introduced nested dicts is an unintentional bug.
- code-review-06: Deletion via None only works when merging into a dict that already exists at that key.
- code-review-06: If the override introduces a brand-new nested dict, the whole dict is assigned as-is.
- code-review-06: None values inside a newly-introduced nested dict are stored literally instead of being treated as deletions.
- code-review-06: The None sentinel means different things depending on whether the key already existed as a dict.
- code-review-06: JSON Merge Patch uses None (null) as a delete sentinel.
- code-review-06: Recursive merging applies only to `dict`, not to other mapping types.
- code-review-06: Custom Mapping subclasses and OrderedDict are examples of types not merged recursively.
- code-review-06: The `isinstance(..., dict)` check is strict rather than duck-typed.
- code-review-06: The function has no docstring and no type hints.
- code-review-06: The absence of a documented contract makes the analysis guesswork.
- code-review-06: The crash on a dict-to-non-dict override and the aliasing of newly-introduced nested dicts are genuine bugs to fix.
- code-review-06: The shallow-copy sharing and the asymmetric nested None deletion are subtler correctness traps that should at least be documented.
- code-review-07: Collapsing different failure classes is a real risk if unknown callers rely on exceptions propagating for non-HTTP errors.
- code-review-07: Any non-retryable error, including 4xx other than 429 and exhausted retries, is converted into a null return rather than propagated.
- code-review-07: A caller that awaits withRetry(fn)() and dereferences the result without a null check will get a confusing downstream error far from the real cause.
- code-review-07: The attempts semantics are worth confirming with any caller who tuned the value expecting different semantics.
- code-review-07: The backoff has no cap and no jitter.
- code-review-07: The backoff is linear and unbounded.
- code-review-07: Unbounded backoff is fine for small attempts values.
- code-review-07: If a caller passes a large attempts value, delays grow indefinitely.
- code-review-07: The lack of cap and jitter likely never mattered because the default attempts is 3.
- code-review-07: The code loses this binding.
- code-review-07: The wrapped function is invoked as fn(...args) and is not bound to any receiver.
- code-review-07: If a hidden caller wrapped an object method expecting this to refer to the object, it will break silently or throw.
- code-review-07: An error thrown from a lost this binding would itself be swallowed by the null-returning and status-assumption behavior.
- code-review-07: The accidental issues resemble logic slips from editing retry logic without re-testing all branches.
- code-review-08: An aborted run produces only a traceback, visible if run interactively.
- code-review-08: Because the script runs on a schedule, errors are unlikely to be noticed unless someone checks logs.
- code-review-08: os.remove unlinks the symlink itself rather than the target.
- code-review-08: The 45-day and 500 values were previously flagged by the user as magic numbers with no rationale.
- code-review-08: The rationale for the 45-day and 500 values must come from whoever wrote the code or from data-retention/compliance requirements.
- code-review-08: The 45-day value may be tied to a legal retention policy.
- code-review-08: As written, the constants are indistinguishable from arbitrary defaults.
- code-review-08: The script has no --dry-run mode.
- code-review-08: A dry-run mode is standard practice for scheduled deletion scripts.
- code-review-08: The absence of a dry-run mode is a gap rather than a bug.
- code-review-08: Without a dry-run mode, behavior cannot be safely tested in production without risking real deletions.
- code-review-08: The variable 'removed' is computed but is not logged or returned anywhere visible in the snippet.
- code-review-08: If 'removed' is meant to feed monitoring or alerting, that plumbing is missing.
- debugging-02: In non-strict mode, `this` inside such a setInterval callback is the global object (window/globalThis).
- debugging-02: In strict mode or ES modules, `this` inside such a setInterval callback is undefined.
- debugging-02: The NaN value produced is what gets logged to the console.
- debugging-02: The incremented value is assigned onto the global object rather than the Timer instance.
- debugging-02: Calling .bind(this) on a regular function callback is an alternative fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` inside it is an alternative fix.
- debugging-04: The user's code forces encoding="ascii" when opening the file.
- debugging-04: Passing errors="replace" to open() prevents a crash on malformed or unexpected bytes.
- debugging-04: Passing errors="ignore" to open() also prevents a crash on malformed or unexpected bytes.
- debugging-04: Using errors="replace" can mangle unusual characters.
- debugging-04: Mangling characters is acceptable if only line counts matter rather than content.
- debugging-04: Counting b"\n" bytes in binary mode counts lines without decoding.
- debugging-05: Python evaluates default arguments once, at function definition time.
- debugging-06: A connection leak in the export job's retry path is a plausible cause.
- debugging-06: The export job's timeout and exception paths should be audited to confirm they always return the connection.
- debugging-06: An undersized pool relative to the database's max_connections is a plausible cause.
- debugging-06: If the combined pool sizes of the export job, the analytics service, and other clients exceed the database's max_connections, requests queue at the database even when each service's own pool appears to have headroom.
- debugging-06: The export job failures occur around 02:14 UTC.
- debugging-06: Pool-utilization metrics worth adding include in-use count, wait queue depth, and wait time.
- debugging-06: Summing all services' maximum pool sizes and comparing that total against the database's max_connections checks for oversubscription.
- debugging-06: Setting an alert on pool wait time or queue depth at a threshold below the 30s timeout would page someone with full context during the next occurrence.
- debugging-06: Correlating schedules and adding pool-utilization metrics are cheap steps that will likely distinguish contention from a leak before direct database inspection is needed.
- debugging-07: A read-after-write race on an async pipeline is the most common cause of flakes where a count is short by exactly one.
- debugging-07: If an API call returns after the HTTP handler responds but before the DB transaction commits, a fast subsequent read can miss the write.
- debugging-07: Deferred commits can occur when the commit happens in a background hook or when the ORM session flush is deferred.
- debugging-07: A missing await or commit boundary produces intermittent, load-sensitive failures that are exactly one event short.
- debugging-07: GC pauses, container throttling, and noisy neighbors can starve a CI machine.
- debugging-07: If a test does not assert on the response of each seed call, a transient 429 or 500 can silently drop an event and only be noticed at the final assertion.
- debugging-07: Transient 429s or 500s from a shared rate limiter or connection pool exhaustion are more likely when four workers hammer the same DB or API simultaneously.
- debugging-07: pytest includes a custom assertion message in the failure log even without artifact storage.
- debugging-07: If the test never fails locally under `-n 4`, that is evidence the problem is CI-resource-contention-specific timing rather than a pure test-isolation bug.
- debugging-07: If the test only flakes when the full suite runs, shared fixture or account contamination from other tests is the likely cause rather than a bug in the test in isolation.
- debugging-07: `-k test_digest_contains_all_events` filters a pytest run to a single test while still collecting the rest of the suite.
- debugging-07: If adding a short poll/retry loop before reading the digest makes the flake disappear, that strongly indicates an async or eventual-consistency race rather than a data-isolation bug.
- debugging-07: Per-test isolation can be achieved with `uuid4()` IDs or freezegun-style time control instead of hardcoded constants.
- debugging-07: Under READ COMMITTED isolation, when the app writes on a different connection or transaction than the test's setup, stale reads can occur and be worsened by connection pool pressure from four workers.
- debugging-07: Logging seed results and digest contents on failure, combined with testing whether a poll/retry removes the flake, gives the fastest diagnostic signal.
- debugging-07: That combination can distinguish a race condition from a shared-state isolation bug within one or two CI flakes.
- debugging-08: Memory growth that survives quiet nights rules out normal cache/GC churn.
- debugging-08: True garbage gets collected regardless of load.
- debugging-08: Growth that survives quiet nights points to objects still reachable from live roots, indicating an actual leak rather than mere heap pressure.
- debugging-08: A bounded cache with an unchanged bound and no code changes in a year is a less likely root cause.
- debugging-08: Eviction bugs are possible even in code that has not changed in a long time.
- debugging-08: The most likely hypothesis is a reference leak outside the cache.
- debugging-08: Idempotency or dedup maps keyed by request or webhook ID with no TTL are a possible reference leak source.
- debugging-08: ThreadLocal or MDC context leaking on pooled threads is a possible reference leak source.
- debugging-08: A reference leak explains why quiet nights do not recover memory, because the objects are held by real GC roots.
- debugging-08: `jcmd <pid> GC.class_histogram` produces a heap class histogram on the JVM.
- debugging-08: A class whose object count trends upward independent of traffic volume indicates a leak.
- debugging-08: Grepping for ThreadLocal usage in request-handling code that is not cleared on completion is a useful check.
- debugging-08: A metrics or observability cardinality leak is the second-ranked hypothesis.
- debugging-08: Using product or campaign identifiers as metric labels causes each new campaign to introduce new unique label combinations.
- debugging-08: Unique metric label combinations can live forever in the metrics registry.
- debugging-08: A metrics cardinality leak matches the correlation between memory growth and marketing campaigns.
- debugging-08: A metrics cardinality leak matches growth without webhooks because the canary still emits its own metrics.
- debugging-08: Checking the unique series count on the /metrics endpoint over a week tests the metrics cardinality hypothesis.
- debugging-08: A metrics registry size that climbs and never resets indicates the leak.
- debugging-08: The metrics registry check can be done without a heap profiler.
- debugging-08: A cache bound bug or entry-size growth is the third-ranked hypothesis.
- debugging-08: Campaigns can increase average cache entry payload size through larger product descriptions or more variants and images.
- debugging-08: Logging cache item count versus configured limit, eviction rate, and average serialized entry size tests the cache hypothesis.
- debugging-08: Off-heap or native allocation is the fourth-ranked hypothesis.
- debugging-08: Buffers for TLS, compression, and HTTP client connection pools are often native or off-heap.
- debugging-08: Off-heap buffers are not visible to a Java-style heap profiler.
- debugging-08: Off-heap allocation matches the canary growing slowly from its own baseline connections.
- debugging-08: JVM native memory tracking is enabled with -XX:NativeMemoryTracking.
- debugging-08: pmap or smaps snapshots over time can diagnose native memory growth.
- debugging-08: Allocator fragmentation is the fifth-ranked, lower-priority hypothesis.
- debugging-08: Setting MALLOC_ARENA_MAX=1 or swapping in jemalloc or tcmalloc on a test instance tests the fragmentation hypothesis.
- debugging-08: The canary's lower, steadier growth rate makes the responsible class or allocation site easier to isolate from noise.
- explanation-01: A hash map typically uses hash modulo array size (hash % array_size) to pick a slot in an underlying array.
- explanation-01: A slot in a hash map's underlying array is called a bucket.
- explanation-01: There are infinitely many possible keys but only a finite number of buckets.
- explanation-01: The inevitability of collisions is the same idea as the birthday paradox.
- explanation-01: In the worst case, where everything hashes to one bucket, chaining lookup degrades to O(n) list traversal.
- explanation-01: Quadratic probing jumps by increasing squares, such as index + 1, index + 4, index + 9.
- explanation-01: Quadratic probing reduces clustering.
- explanation-01: Open addressing performance degrades sharply as the table fills up because clustering gets worse.
- explanation-01: Tuning open addressing involves resizing and rehashing proactively.
- explanation-01: Both chaining and open addressing rely on resizing the underlying array and rehashing all entries once the load factor gets too high.
- explanation-01: Resizing and rehashing keep collisions manageable and keep operations close to O(1).
- explanation-02: PostgreSQL and MySQL support pessimistic locking via SELECT ... FOR UPDATE.
- explanation-02: Seat reservations are an example use case for pessimistic locking.
- explanation-02: Pessimistic locking is also good when the work between read and write is short, keeping lock hold time low.
- explanation-02: Editing a user profile is an example use case for optimistic locking.
- explanation-02: Editing a document in a CMS is an example use case for optimistic locking.
- explanation-02: Optimistic locking works well in stateless and distributed systems.
- explanation-02: Holding a database lock across a network round-trip or user think-time would be costly.
- explanation-02: As a rule of thumb, low contention with long user-facing gaps between read and write favors optimistic locking.
- explanation-03: A starting TCP sender does not know how many other connections share the path's bandwidth.
- explanation-03: A starting TCP sender does not know how much buffering exists in routers along the path.
- explanation-03: If a sender transmitted as fast as the receiver's window allowed, it could send more data than the network path can handle.
- explanation-03: Congestion collapse was a real problem on the early internet in the 1980s.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The receiver's advertised window limits data based on the receiver's buffer space.
- explanation-03: Historically, TCP connections began with a congestion window of 1 segment.
- explanation-03: TCP connections now typically begin with a congestion window of 10 segments.
- explanation-03: RFC 6928 specifies the initial congestion window of 10 segments.
- explanation-03: Growing linearly from the start would waste available bandwidth, especially on high-bandwidth, high-latency links.
- explanation-03: The name 'slow start' is misleading because the mechanism is not sluggish.
- explanation-03: After a loss, TCP often re-enters a slow-start-like ramp.
- explanation-03: TCP's congestion control philosophy allows millions of independent connections to share the internet's capacity without a central coordinator.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own register state, including the instruction pointer.
- explanation-04: Sharing memory between threads requires locks or synchronization.
- explanation-04: Process creation overhead includes creating a new address space and copy-on-write page tables.
- explanation-04: Older Ruby MRI has a global interpreter lock.
- explanation-04: Gunicorn uses worker processes.
- explanation-04: nginx uses worker processes.
- explanation-04: Process boundaries can be further restricted with seccomp, containers, or chroot.
- explanation-04: With many threads, growing amounts of shared mutable state need locks.
- explanation-04: Lock contention, deadlocks, and race conditions become harder to reason about as thread count grows.
- explanation-04: Explicit message passing is often easier to get correct than shared mutable state, though slower.
- explanation-04: Processes can be distributed across machines more naturally than threads.
- explanation-05: Root references include global variables and active stack frames.
- explanation-05: Garbage collection prevents leaks caused by forgotten pointers.
- explanation-05: A collection can be reachable by being a static field or a singleton.
- explanation-05: Long-lived objects that listeners attach to include event emitters, DOM elements, and global buses.
- explanation-05: Subscriptions to observables or streams that are not disposed can cause memory leaks.
- explanation-05: Timers or intervals holding references that are never cleared can cause memory leaks.
- explanation-06: N+1 queries are a possible cause of slowness.
- explanation-06: CPU-bound work is a possible cause of slowness.
- explanation-06: A cache only helps with expensive, repeated reads that return the same data.
- explanation-06: A cache requires extra infrastructure to run.
- explanation-06: The user said they do not know the read/write mix of the service.
- explanation-06: If a workload is read-heavy but each read is already cheap, caching saves little.
- explanation-06: An indexed lookup is an example of a cheap read.
- explanation-06: Complex joins, aggregations, and external calls are examples of expensive reads.
- explanation-06: Adding basic request timing and logging reveals which endpoints are actually slow.
- explanation-06: An APM tool can be used to measure request timing.
- explanation-06: Running EXPLAIN on queries reveals whether they perform full table scans or are missing indexes.
- explanation-06: A slow API is often caused by a missing index or an N+1 query.
- explanation-06: Fixing a missing index or N+1 query is a smaller fix than building a cache layer.
- explanation-07: Vertical scaling (a bigger instance with more RAM and IOPS) and read replicas will likely suffice well past 1-2 TB of data.
- explanation-07: The decision to shard depends on write load rather than storage size.
- explanation-07: If reads dominate the workload, read replicas are a cheaper solution than sharding.
- explanation-07: Multi-tenant data keyed by customer_id shards cleanly at a later date with low regret.
- explanation-07: Managed Postgres offerings such as RDS, Aurora, and Cloud SQL scale to tens of terabytes.
- explanation-07: Managed Postgres offerings offer very large instance types.
- explanation-07: Waiting risks that no natural shard key is designed into the schema, making eventual sharding a bigger rewrite.
- explanation-07: A single Postgres instance without replicas is a single point of failure.
- explanation-07: A database size number alone is not an appropriate trigger for sharding because size is not the actual constraint.
- explanation-08: Speedups from switching from JSON to a binary format vary widely, ranging from negligible to 5-10x.
- explanation-08: Request latency is composed of serialization/parsing plus network, database queries, and business logic.
- explanation-08: Binary formats mainly win on numeric-heavy or repetitive-schema payloads.
- explanation-08: Text-heavy or highly variable JSON payloads see much smaller gains from binary formats.
- explanation-08: A flamegraph or simple timers around JSON.parse/stringify equivalents can be used to profile serialization time.
- explanation-08: Typical payload sizes can be measured by logging them.
- explanation-08: Profiling the request path and measuring payload sizes takes roughly an hour of work.
- summarization-01: The app now starts up to 40% faster.
- summarization-04: After clicking the PDF export option, nothing happens initially.
- summarization-04: The expected PDF export behavior is consistent with the CSV export behavior.
- summarization-04: The issue is likely a backend/server-side problem.
- summarization-05: Chen is assigned to continue the search indexing work.
- summarization-07: The assistant checked its memory for relevant context on communication preferences before responding.
- summarization-07: No relevant information was found in memory.
- summarization-07: Confirming the tail latency result requires a production-like test.
- summarization-08: The stuck-progress-bar issue is a perception/feedback issue rather than a functional bug.
- summarization-08: The recommendation is to prioritize investigating the link between the progress bar and abandonment.
- summarization-08: The progress-bar/abandonment finding is prioritized because of its behavioral impact despite the small sample size.

Added facts (styled only):

- code-review-01: The function has five problems.
- code-review-01: The function does not validate that `roles` is a list.
- code-review-01: The corrected version logs the specific exception instead of swallowing it silently.
- code-review-02: Declaring a function `async` without using `await` defeats the purpose of the declaration.
- code-review-02: The corrected version checks the response status and throws an `Error` including the user ID and `res.status` when the response is not OK.
- code-review-03: A driver's documentation should be checked to determine its placeholder syntax.
- code-review-03: Missing input validation can produce a query that returns no rows or an unexpected error instead of a clear failure, depending on the schema.
- code-review-03: The function gives no indication of what values the `status` parameter accepts.
- code-review-03: `status` may be intended to be one of a fixed set of values such as `"pending"`, `"shipped"`, or `"cancelled"`.
- code-review-03: An enum or a validated set of constants would prevent typos and invalid values from reaching the database.
- code-review-04: The ordering behavior between `reset` and `increment` is not documented anywhere.
- code-review-04: The class has no getter for the value.
- code-review-04: Without a getter, callers likely access `counter.value` directly.
- code-review-04: Accessing `counter.value` directly bypasses any locking added inside the class.
- code-review-04: The fix includes adding a `value` property (or `get()` method) that also acquires the lock.
- code-review-04: The proposed `value` property gives callers a safe way to read the value without touching an internal attribute directly.
- code-review-05: `rm -rf *.tmp` is dangerous when no files match.
- code-review-05: `echo Cleaned $BACKUP_DIR` is unquoted.
- code-review-05: `echo Cleaned $BACKUP_DIR` carries a word-splitting risk.
- code-review-05: `echo Cleaned $BACKUP_DIR` does not reflect where the script actually ended up if the `cd` failed silently.
- code-review-06: Any type mismatch between base and override triggers a crash instead of a clear error or a defined replace behavior.
- code-review-06: Two questions should be answered by whoever uses the function before changing the logic: whether "None deletes" is required behavior, and what should happen on a type mismatch between base and override.
- code-review-06: The options for type-mismatch behavior are crash, keep base, or replace with override.
- code-review-06: Bugs #1 and #2 should be fixed by making the mismatch behavior explicit and consistent.
- code-review-07: If a 429 occurs on the final iteration, the code still awaits the backoff before checking the loop condition.
- code-review-07: The backoff wait on the final iteration provides no benefit because the loop exits afterward.
- code-review-07: The function returns null for 'gave up' and undefined for 'exhausted 5xx retries'.
- code-review-07: Callers cannot distinguish a genuine falsy result from a failure.
- code-review-07: The author's best guess is that 'fail soft, return null' was a deliberate design decision.
- code-review-08: Deleting in-progress `tmp-`/`.part` files is the most dangerous bug in the script.
- code-review-08: After the cap is reached, the loop keeps iterating and calling `getmtime` on every remaining file.
- code-review-08: The cap saves no work; it only stops deletions.
- code-review-08: There is no check that `ROOT` exists.
- code-review-08: `os.listdir(ROOT)` raises immediately if the directory is missing or unmounted, with no guard.
- code-review-08: The answer about whether `tmp-`/`.part` files represent in-progress work determines whether the biggest identified bug is a bug at all.
- debugging-03: `moving_sum` returns the sum of each window of the given size.
- debugging-03: With the corrected range, `moving_sum([1, 2, 3, 4], 2)` returns `[3, 5, 7]`.
- debugging-04: The ascii codec only supports byte values 0 through 127.
- debugging-04: Counting lines in binary mode is the most robust option when only a line count is needed and the text content does not matter.
- debugging-06: The error points to a connection pool problem rather than a query problem.
- debugging-06: Connection leaks accumulate over time rather than occurring at a fixed point, which explains why the batch number at failure varies.
- debugging-06: When a query blocks on a row or table lock, the connection stays checked out until the lock clears.
- debugging-06: Lock contention drains the pool in the same way a connection leak does.
- debugging-06: Network or database-side slowness is a plausible cause.
- debugging-06: A slow disk, autovacuum, or a burst of replication lag can make every query take longer.
- debugging-06: The pool metrics to log are active connections, idle connections, and wait queue depth, sampled every few seconds.
- debugging-06: A snapshot of database query and lock state can be captured on a timer in production to have data for the next failure.
- debugging-06: Connection checkout/checkin logging should be added in the application, including a stack trace on checkout.
- debugging-06: If connections are leaked, checkout/checkin logging will show checkouts without matching checkins.
- debugging-06: Log retention should be increased for the affected services to capture the full window before and after the failure.
- debugging-06: The issue can be reproduced under load by running the export job against a copy of the database while simulating analytics traffic.
- debugging-06: Reproducing under load reveals whether pool exhaustion is load-triggered.
- debugging-06: Given the shared database and the varying batch number, the recommended starting points are the analytics service's schedule and the database's lock/long-query stats.
- debugging-06: A connection leak would eventually cause failures at low batch numbers as well.
- debugging-07: Three candidate explanations stand out: eventual consistency, shared state across workers, and time-window filtering.
- debugging-07: If a queue or worker sits between the event API and the digest endpoint, the test likely needs a wait-for-condition or polling step instead of an immediate assertion.
- debugging-08: A secondary map that mirrors a cache may itself have no size bound.
- debugging-08: Forcing a full cache eviction cycle and taking heap snapshots immediately before and after can reveal retained references.
- debugging-08: If retained size does not drop proportionally to the number of evicted entries, something outside the cache still holds references to the evicted objects.
- debugging-08: Taking heap snapshots before and after a traffic burst and diffing object counts by type can detect per-request accumulation.
- debugging-08: Disabling all non-webhook background jobs on a test instance and observing whether memory stays flat can isolate the leak to those jobs.
- debugging-08: If memory stays flat after disabling background jobs, the baseline leak lives in one of those jobs rather than in shared request-handling code.
- debugging-08: The fix for allocator fragmentation is allocator tuning rather than code changes.
- debugging-08: RSS stands for resident set size.
- debugging-08: There appear to be at least two separate sources of unbounded retention: one tied to request volume and one present without webhook traffic.
- debugging-08: Taking a heap snapshot on the canary at startup and again after a few hours of growth, then diffing object counts by type, is the recommended first step.
- debugging-08: That heap snapshot diff will likely point directly at either the cache retention cause or the per-request accumulation cause.
- explanation-02: A version column can be used to implement optimistic locking, as in a products table with a version column.
- explanation-02: An optimistic update can be written as: UPDATE products SET stock = stock - 1, version = 6 WHERE id = 42 AND version = 5.
- explanation-02: Optimistic locking fits when conflicts are infrequent and transactions are short-lived.
- explanation-02: Pessimistic locking fits when the workload includes long-running transactions on shared, high-contention data.
- explanation-03: Before congestion control existed, TCP senders had no mechanism to hold back.
- explanation-03: Congestion can cascade because dropped packets trigger retransmissions, which add more traffic to an already congested network.
- explanation-03: During congestion collapse, throughput dropped sharply because the network spent its capacity on retransmissions instead of new data.
- explanation-03: 'ssthresh' stands for slow start threshold.
- explanation-04: Processes get separate memory and, on most systems, separate permissions.
- explanation-04: Independent process restarts suit long-running services that need rolling restarts.
- explanation-04: I/O-bound tasks spend most of their time waiting.
- explanation-06: A cache placed in front of the database does not fix slowness caused by the network, external API calls, unindexed queries, or application code.
- explanation-06: The layers to time include the incoming request, the database query, external calls, and response serialization.
- explanation-06: Databases can be checked for slow queries, missing indexes, and lock contention.
- explanation-06: The read-to-write ratio can be measured by counting query types over a representative time window.
- explanation-07: At 200 GB, a single PostgreSQL instance can still be handled by vertical scaling, indexing, and read replicas.
- explanation-07: A vague statement that data 'will grow' does not indicate when a scaling limit will be reached.
- explanation-07: An order-of-magnitude growth estimate, such as 2x per year versus 20x per year, is more useful to request from the product team than an exact number.
- explanation-07: The recommendation is to scale vertically and optimize first by adding read replicas and tuning indexes.
- explanation-07: Table partitioning within PostgreSQL is an alternative to full sharding that may solve the problem.
- explanation-08: If serialization is 5% of request time, a format 10 times faster to parse saves about 4.5% overall.
- explanation-08: If serialization is 40% of request time, a format 10 times faster to parse saves about 36% overall.
- explanation-08: Payload size affects network performance, not just CPU.
- explanation-08: Binary formats typically shrink payloads by 20-50%.
- explanation-08: The benefit of smaller payloads appears mainly when bandwidth or transfer time dominates, such as on mobile clients or with large responses.
- explanation-08: For small payloads on a fast network, reducing payload size barely changes latency.
- explanation-08: Protocol Buffers, MessagePack, and CBOR have different tradeoffs between parse speed, payload size, and schema flexibility.
- explanation-08: A generic claim about switching to 'binary' hides the differences between specific binary formats.
- explanation-08: Typical and worst-case payload sizes should be measured for both requests and responses.
- explanation-08: Network bottlenecks are especially relevant for high-latency or bandwidth-constrained clients.
- explanation-08: Prototyping the switch on one endpoint allows re-measuring both serialization time and end-to-end request time.
- explanation-08: High-throughput internal services and mobile clients on slow networks are cases where serialization or payload transfer is a large share of request time.
- explanation-08: The profiling step costs about a day or two.
- summarization-01: Cold start time is about 40% faster.
- summarization-01: Each button's tooltip shows that button's keyboard shortcut.
- summarization-05: The action items listed come from a sprint planning meeting.
- summarization-06: A restart resolved the error rates.
- summarization-08: Some customers already had templates.

### plain-language

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 31 | 23 | 0.742 | 31 | 9 |
| code-review-02 | 18 | 13 | 0.722 | 16 | 1 |
| code-review-03 | 28 | 20 | 0.714 | 21 | 3 |
| code-review-04 | 24 | 17 | 0.708 | 22 | 10 |
| code-review-05 | 32 | 24 | 0.75 | 27 | 2 |
| code-review-06 | 43 | 33 | 0.767 | 33 | 6 |
| code-review-07 | 56 | 42 | 0.75 | 28 | 6 |
| code-review-08 | 54 | 36 | 0.667 | 24 | 4 |
| debugging-01 | 6 | 6 | 1.0 | 8 | 0 |
| debugging-02 | 14 | 10 | 0.714 | 15 | 0 |
| debugging-03 | 12 | 12 | 1.0 | 12 | 3 |
| debugging-04 | 15 | 8 | 0.533 | 16 | 2 |
| debugging-05 | 15 | 15 | 1.0 | 13 | 1 |
| debugging-06 | 24 | 18 | 0.75 | 26 | 8 |
| debugging-07 | 30 | 12 | 0.4 | 30 | 11 |
| debugging-08 | 50 | 19 | 0.38 | 32 | 12 |
| explanation-01 | 43 | 29 | 0.674 | 31 | 5 |
| explanation-02 | 28 | 20 | 0.714 | 28 | 2 |
| explanation-03 | 38 | 18 | 0.474 | 20 | 2 |
| explanation-04 | 41 | 24 | 0.585 | 30 | 2 |
| explanation-05 | 19 | 11 | 0.579 | 14 | 0 |
| explanation-06 | 32 | 19 | 0.594 | 22 | 7 |
| explanation-07 | 28 | 19 | 0.679 | 22 | 9 |
| explanation-08 | 15 | 6 | 0.4 | 18 | 10 |
| summarization-01 | 5 | 4 | 0.8 | 5 | 1 |
| summarization-02 | 14 | 13 | 0.929 | 13 | 0 |
| summarization-03 | 13 | 12 | 0.923 | 11 | 0 |
| summarization-04 | 16 | 11 | 0.688 | 11 | 0 |
| summarization-05 | 8 | 7 | 0.875 | 11 | 1 |
| summarization-06 | 12 | 0 | 0.0 | 4 | 4 |
| summarization-07 | 18 | 16 | 0.889 | 12 | 0 |
| summarization-08 | 19 | 18 | 0.947 | 25 | 2 |

Median fraction: 0.714 over 32 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python pitfall.
- code-review-01: The function does not check whether `"member"` is already in `roles`.
- code-review-01: If `roles` already contains `"member"`, it gets added a second time.
- code-review-01: The boolean return tells the caller nothing about what was inserted or why it failed.
- code-review-01: The fixed version uses `roles = list(roles) if roles else []`.
- code-review-01: The fixed version appends `"member"` only if it is not already in `roles`.
- code-review-01: The fixed version avoids silently swallowing exceptions, leaving handling to the caller.
- code-review-01: The fixed version prevents duplicate roles.
- code-review-02: The `async` keyword makes `loadProfile` return a `Promise`.
- code-review-02: The promise returned by `loadProfile` rejects synchronously due to the `TypeError` rather than because of awaited async work.
- code-review-02: Failed requests such as network errors or non-2xx responses are silently swallowed or turned into unhandled rejections.
- code-review-02: The `.then` chain is neither returned nor awaited, so any rejection becomes an unhandled promise rejection.
- code-review-02: The fixed version removes the unused `profile` variable and the unused promise chain.
- code-review-03: psycopg2 uses `%s` as its placeholder.
- code-review-03: MySQLdb uses `%s` as its placeholder.
- code-review-03: If `customer_name` or `status` is not a string (e.g. `None`), the `+` concatenation raises a `TypeError`.
- code-review-03: The resulting `TypeError` produces a confusing stack trace rather than a clear error.
- code-review-03: The function has no pagination or limit.
- code-review-03: The function could return unbounded result sets on a wildcard-like match.
- code-review-03: The lack of pagination is more of a design consideration than a bug.
- code-review-03: The SQL injection issue is the only problem that actually needs fixing.
- code-review-04: The race condition gets worse under load.
- code-review-04: The window between the read and the write is exactly when a context switch is likely.
- code-review-04: The atomicity of that assignment in CPython is provided by the GIL.
- code-review-04: The assignment `self.value = 0` is a single bytecode-level store.
- code-review-04: PyPy has an STM mode.
- code-review-04: Python 3.13 has a free-threaded (no-GIL) build.
- code-review-04: A `reset` can interleave between the read and the write of an `increment`.
- code-review-05: `nullglob` is not available in POSIX sh.
- code-review-05: If no .log files exist, `ls *.log` prints an error to stderr.
- code-review-05: The script does not check that BACKUP_DIR is actually a directory before running `cd`.
- code-review-05: The script lacks `set -u`, which would have caught the empty-$1 problem.
- code-review-05: The suggested rewrite exits with status 1 and a usage message on stderr when `$#` is not 1.
- code-review-05: The suggested rewrite exits with status 1 and an error message on stderr when BACKUP_DIR is not a directory.
- code-review-05: The suggested rewrite calls `gzip -- "$f"` with the filename quoted.
- code-review-05: The key fixes are argument and directory validation before destructive actions, `set -eu`, quoted variables, removal of the `ls` parsing anti-pattern, and a glob-no-match guard.
- code-review-06: The JSON Merge Patch spec checks the patch value's type rather than the target's type.
- code-review-06: Recursive merging of a key produces no aliasing.
- code-review-06: Deletion via None only works when merging into a dict that already exists at that key.
- code-review-06: None values inside a newly-introduced nested dict are stored literally instead of being treated as deletions.
- code-review-06: The None sentinel means different things depending on whether the key already existed as a dict.
- code-review-06: Custom Mapping subclasses and OrderedDict are examples of types not merged recursively.
- code-review-06: The `isinstance(..., dict)` check is strict rather than duck-typed.
- code-review-06: If base is a dict subclass, subclass-specific behavior is lost in the return value.
- code-review-06: The function has no docstring and no type hints.
- code-review-06: The shallow-copy sharing and the asymmetric nested None deletion are subtler correctness traps that should at least be documented.
- code-review-07: Any non-retryable error, including 4xx other than 429 and exhausted retries, is converted into a null return rather than propagated.
- code-review-07: A caller that awaits withRetry(fn)() and dereferences the result without a null check will get a confusing downstream error far from the real cause.
- code-review-07: The attempts parameter counts total tries rather than retries.
- code-review-07: The default value of attempts is 3.
- code-review-07: A default attempts of 3 means fn is called at most 3 times total, not 3 retries after an original attempt.
- code-review-07: The attempts naming ambiguity is not a bug per se.
- code-review-07: The attempts semantics are worth confirming with any caller who tuned the value expecting different semantics.
- code-review-07: The lack of cap and jitter likely never mattered because the default attempts is 3.
- code-review-07: The code loses this binding.
- code-review-07: The wrapped function is invoked as fn(...args) and is not bound to any receiver.
- code-review-07: If a hidden caller wrapped an object method expecting this to refer to the object, it will break silently or throw.
- code-review-07: An error thrown from a lost this binding would itself be swallowed by the null-returning and status-assumption behavior.
- code-review-07: Distinguishing 429 (retry with delay) from other 4xx (don't retry) is likely deliberate.
- code-review-07: The accidental issues resemble logic slips from editing retry logic without re-testing all branches.
- code-review-08: The import-time CUTOFF computation is a latent bug rather than deliberate.
- code-review-08: os.path.getmtime works on directories.
- code-review-08: An aborted run produces only a traceback, visible if run interactively.
- code-review-08: Because the script runs on a schedule, errors are unlikely to be noticed unless someone checks logs.
- code-review-08: os.path.getmtime follows symlinks when stating.
- code-review-08: os.remove unlinks the symlink itself rather than the target.
- code-review-08: Unconditional tmp/part deletion creates a race with the process that produces the exports.
- code-review-08: The unconditional tmp/part deletion is very likely not deliberate.
- code-review-08: The constants have no comments, no config, and no environment variable override.
- code-review-08: The 45-day and 500 values were previously flagged by the user as magic numbers with no rationale.
- code-review-08: The script has no --dry-run mode.
- code-review-08: A dry-run mode is standard practice for scheduled deletion scripts.
- code-review-08: The absence of a dry-run mode is a gap rather than a bug.
- code-review-08: Without a dry-run mode, behavior cannot be safely tested in production without risking real deletions.
- code-review-08: The variable 'removed' is computed but is not logged or returned anywhere visible in the snippet.
- code-review-08: If 'removed' is meant to feed monitoring or alerting, that plumbing is missing.
- code-review-08: The 45-day cutoff, the 500-item cap as a safety brake, and deleting tmp-/.part files at all are likely deliberate business logic needing confirmation.
- code-review-08: The likely genuine bugs are the cap not applying to tmp/part deletions, lack of exception isolation, arbitrary deletion order under the cap, and import-time CUTOFF computation.
- debugging-02: The NaN value produced is what gets logged to the console.
- debugging-02: The incremented value is assigned onto the global object rather than the Timer instance.
- debugging-02: Calling .bind(this) on a regular function callback is an alternative fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` inside it is an alternative fix.
- debugging-04: The file contains a non-ASCII byte 0xc3 at byte 512.
- debugging-04: UTF-8 is the most common encoding to use for such files.
- debugging-04: Passing errors="ignore" to open() also prevents a crash on malformed or unexpected bytes.
- debugging-04: The libraries chardet and charset-normalizer can detect a file's encoding.
- debugging-04: Opening a file in binary mode with "rb" avoids decoding entirely.
- debugging-04: Counting b"\n" bytes in binary mode counts lines without decoding.
- debugging-04: Iterating over a file object opened in binary mode yields lines.
- debugging-06: If the combined pool sizes of the export job, the analytics service, and other clients exceed the database's max_connections, requests queue at the database even when each service's own pool appears to have headroom.
- debugging-06: Another nightly cron job scheduled near 02:14 UTC could be overlapping with the export job.
- debugging-06: The export job failures occur around 02:14 UTC.
- debugging-06: Querying pg_stat_activity or an equivalent view during a live failure window, filtered by application or user, shows who is holding connections and whether any are idle in transaction or long-running.
- debugging-06: Summing all services' maximum pool sizes and comparing that total against the database's max_connections checks for oversubscription.
- debugging-06: The relevant log fragment for the failure was lost to log rotation.
- debugging-07: A read-after-write race on an async pipeline is the most common cause of flakes where a count is short by exactly one.
- debugging-07: Read-after-write races typically only appear when the system is under load.
- debugging-07: Dev machines running tests serially rarely hit read-after-write races.
- debugging-07: If an API call returns after the HTTP handler responds but before the DB transaction commits, a fast subsequent read can miss the write.
- debugging-07: Deferred commits can occur when the commit happens in a background hook or when the ORM session flush is deferred.
- debugging-07: A missing await or commit boundary produces intermittent, load-sensitive failures that are exactly one event short.
- debugging-07: GC pauses, container throttling, and noisy neighbors can starve a CI machine.
- debugging-07: If a test does not assert on the response of each seed call, a transient 429 or 500 can silently drop an event and only be noticed at the final assertion.
- debugging-07: Transient 429s or 500s from a shared rate limiter or connection pool exhaustion are more likely when four workers hammer the same DB or API simultaneously.
- debugging-07: pytest includes a custom assertion message in the failure log even without artifact storage.
- debugging-07: `pytest -n 4 --count 200` combines pytest-xdist with pytest-repeat.
- debugging-07: If the test never fails locally under `-n 4`, that is evidence the problem is CI-resource-contention-specific timing rather than a pure test-isolation bug.
- debugging-07: If the test only flakes when the full suite runs, shared fixture or account contamination from other tests is the likely cause rather than a bug in the test in isolation.
- debugging-07: `-k test_digest_contains_all_events` filters a pytest run to a single test while still collecting the rest of the suite.
- debugging-07: Per-test isolation can be achieved with `uuid4()` IDs or freezegun-style time control instead of hardcoded constants.
- debugging-07: Under READ COMMITTED isolation, when the app writes on a different connection or transaction than the test's setup, stale reads can occur and be worsened by connection pool pressure from four workers.
- debugging-07: Logging seed results and digest contents on failure, combined with testing whether a poll/retry removes the flake, gives the fastest diagnostic signal.
- debugging-07: That combination can distinguish a race condition from a shared-state isolation bug within one or two CI flakes.
- debugging-08: A canary with no webhooks growing does not rule out causes tied to background jobs, scheduled tasks, or the canary's own baseline traffic such as health checks and polling.
- debugging-08: The cache could still be the root cause if the composition of its entries changed.
- debugging-08: A bound on entry count does not protect against growing entry size.
- debugging-08: Idempotency or dedup maps keyed by request or webhook ID with no TTL are a possible reference leak source.
- debugging-08: ThreadLocal or MDC context leaking on pooled threads is a possible reference leak source.
- debugging-08: A reference leak explains why the canary still grows slowly, because its own scheduled or background traffic hits the same code path.
- debugging-08: `jcmd <pid> GC.class_histogram` produces a heap class histogram on the JVM.
- debugging-08: A class whose object count trends upward independent of traffic volume indicates a leak.
- debugging-08: Grepping for ThreadLocal usage in request-handling code that is not cleared on completion is a useful check.
- debugging-08: A metrics or observability cardinality leak is the second-ranked hypothesis.
- debugging-08: Using product or campaign identifiers as metric labels causes each new campaign to introduce new unique label combinations.
- debugging-08: Unique metric label combinations can live forever in the metrics registry.
- debugging-08: A metrics cardinality leak matches the correlation between memory growth and marketing campaigns.
- debugging-08: A metrics cardinality leak matches growth without webhooks because the canary still emits its own metrics.
- debugging-08: Checking the unique series count on the /metrics endpoint over a week tests the metrics cardinality hypothesis.
- debugging-08: A metrics registry size that climbs and never resets indicates the leak.
- debugging-08: The metrics registry check can be done without a heap profiler.
- debugging-08: Campaigns can increase average cache entry payload size through larger product descriptions or more variants and images.
- debugging-08: An eviction path that fails to clear a secondary index or reference to the evicted entry can cause a leak in a bounded cache.
- debugging-08: Logging cache item count versus configured limit, eviction rate, and average serialized entry size tests the cache hypothesis.
- debugging-08: A capped entry count combined with growing average entry size during campaigns confirms the cache hypothesis.
- debugging-08: Buffers for TLS, compression, and HTTP client connection pools are often native or off-heap.
- debugging-08: Off-heap allocation matches the canary growing slowly from its own baseline connections.
- debugging-08: JVM native memory tracking is enabled with -XX:NativeMemoryTracking.
- debugging-08: Allocator fragmentation is the fifth-ranked, lower-priority hypothesis.
- debugging-08: Standard allocators such as glibc malloc do not always return freed memory to the OS.
- debugging-08: RSS can ratchet upward with allocation churn and never return to baseline due to fragmentation.
- debugging-08: More request churn produces more fragmentation.
- debugging-08: Setting MALLOC_ARENA_MAX=1 or swapping in jemalloc or tcmalloc on a test instance tests the fragmentation hypothesis.
- debugging-08: Comparing live-heap size from GC logs against process RSS helps detect fragmentation.
- debugging-08: The canary's lower, steadier growth rate makes the responsible class or allocation site easier to isolate from noise.
- explanation-01: A hash map typically uses hash modulo array size (hash % array_size) to pick a slot in an underlying array.
- explanation-01: There are infinitely many possible keys but only a finite number of buckets.
- explanation-01: Because keys are infinite and buckets are finite, two keys will eventually land in the same bucket.
- explanation-01: The inevitability of collisions is the same idea as the birthday paradox.
- explanation-01: The collection in a chaining bucket is usually a linked list, and sometimes a small array or a tree.
- explanation-01: Deletion under chaining is easy because the entry is just removed from the list.
- explanation-01: Quadratic probing jumps by increasing squares, such as index + 1, index + 4, index + 9.
- explanation-01: Quadratic probing reduces clustering.
- explanation-01: Double hashing uses a second hash function to compute the probe step size.
- explanation-01: Open addressing performance degrades sharply as the table fills up because clustering gets worse.
- explanation-01: Tuning open addressing involves keeping the load factor low, often below about 0.7.
- explanation-01: Tuning open addressing involves resizing and rehashing proactively.
- explanation-01: Both chaining and open addressing rely on resizing the underlying array and rehashing all entries once the load factor gets too high.
- explanation-01: Resizing and rehashing keep collisions manageable and keep operations close to O(1).
- explanation-02: PostgreSQL and MySQL support pessimistic locking via SELECT ... FOR UPDATE.
- explanation-02: Seat reservations are an example use case for pessimistic locking.
- explanation-02: Pessimistic locking is also good when the work between read and write is short, keeping lock hold time low.
- explanation-02: An optimistic update takes the form UPDATE accounts SET balance = balance - 100, version = version + 1 WHERE id = 1 AND version = 5.
- explanation-02: If the optimistic UPDATE affects 0 rows, someone else updated the row first, and the operation should be retried or failed.
- explanation-02: Editing a user profile is an example use case for optimistic locking.
- explanation-02: Optimistic locking works well in stateless and distributed systems.
- explanation-02: As a rule of thumb, high contention with a short critical section favors pessimistic locking.
- explanation-03: A starting TCP sender does not know how many other connections share the path's bandwidth.
- explanation-03: A starting TCP sender does not know how much buffering exists in routers along the path.
- explanation-03: If a sender transmitted as fast as the receiver's window allowed, it could send more data than the network path can handle.
- explanation-03: Routers queue excess packets in their buffers.
- explanation-03: When router buffers fill up, routers start dropping packets.
- explanation-03: A burst of excess data can overwhelm shared routers and harm every connection passing through them.
- explanation-03: Congestion collapse is the scenario where the network is congested and throughput collapses.
- explanation-03: Congestion collapse was a real problem on the early internet in the 1980s.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The receiver's advertised window limits data based on the receiver's buffer space.
- explanation-03: Historically, TCP connections began with a congestion window of 1 segment.
- explanation-03: TCP connections now typically begin with a congestion window of 10 segments.
- explanation-03: RFC 6928 specifies the initial congestion window of 10 segments.
- explanation-03: Each round trip generates ACKs for everything sent during that round.
- explanation-03: Packet loss is interpreted as a sign of congestion, meaning the network's buffers overflowed.
- explanation-03: Congestion avoidance uses linear growth instead of exponential growth.
- explanation-03: Growing linearly from the start would waste available bandwidth, especially on high-bandwidth, high-latency links.
- explanation-03: Linear growth from the start might take a long time to reach a reasonable sending rate.
- explanation-03: If a loss is detected after congestion avoidance begins, TCP reduces its rate, for example by cutting cwnd.
- explanation-03: TCP's congestion control philosophy allows millions of independent connections to share the internet's capacity without a central coordinator.
- explanation-04: A process has its own file descriptors.
- explanation-04: A process has its own OS-managed resources.
- explanation-04: All threads in a process share the same file descriptors.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own register state, including the instruction pointer.
- explanation-04: Sharing memory between threads requires locks or synchronization.
- explanation-04: Spawning and switching processes is more expensive than spawning and switching threads.
- explanation-04: Process creation overhead includes creating a new address space and copy-on-write page tables.
- explanation-04: Older Ruby MRI has a global interpreter lock.
- explanation-04: Examples of work worth isolating in a process include processing untrusted input, running third-party plugins, and rendering a webpage.
- explanation-04: Gunicorn uses worker processes.
- explanation-04: nginx uses worker processes.
- explanation-04: Process boundaries can be further restricted with seccomp, containers, or chroot.
- explanation-04: With many threads, growing amounts of shared mutable state need locks.
- explanation-04: Lock contention, deadlocks, and race conditions become harder to reason about as thread count grows.
- explanation-04: Explicit message passing is often easier to get correct than shared mutable state, though slower.
- explanation-04: Processes can be distributed across machines more naturally than threads.
- explanation-05: Root references include global variables and active stack frames.
- explanation-05: Garbage collection prevents leaks caused by forgotten pointers.
- explanation-05: A collection can be reachable by being a static field or a singleton.
- explanation-05: Long-lived objects that listeners attach to include event emitters, DOM elements, and global buses.
- explanation-05: A closure often captures its enclosing scope.
- explanation-05: A retained listener closure keeps a whole chain of otherwise-unused objects alive.
- explanation-05: Subscriptions to observables or streams that are not disposed can cause memory leaks.
- explanation-05: Timers or intervals holding references that are never cleared can cause memory leaks.
- explanation-06: N+1 queries are a possible cause of slowness.
- explanation-06: CPU-bound work is a possible cause of slowness.
- explanation-06: Slow serialization is a possible cause of slowness.
- explanation-06: Adding a cache introduces new failure modes.
- explanation-06: Cache invalidation bugs are a failure mode introduced by caching.
- explanation-06: A cache requires extra infrastructure to run.
- explanation-06: If a workload is read-heavy but each read is already cheap, caching saves little.
- explanation-06: An indexed lookup is an example of a cheap read.
- explanation-06: Complex joins, aggregations, and external calls are examples of expensive reads.
- explanation-06: Adding basic request timing and logging reveals which endpoints are actually slow.
- explanation-06: Running EXPLAIN on queries reveals whether they perform full table scans or are missing indexes.
- explanation-06: A slow API is often caused by a missing index or an N+1 query.
- explanation-06: Fixing a missing index or N+1 query is a smaller fix than building a cache layer.
- explanation-07: Sharding solves write throughput problems.
- explanation-07: Sharding solves the problem of a dataset being too large for a single machine.
- explanation-07: The decision to shard depends on write load rather than storage size.
- explanation-07: Multi-tenant data keyed by customer_id shards cleanly at a later date with low regret.
- explanation-07: Managed Postgres offerings such as RDS, Aurora, and Cloud SQL scale to tens of terabytes.
- explanation-07: Managed Postgres offerings offer very large instance types.
- explanation-07: Waiting risks that no natural shard key is designed into the schema, making eventual sharding a bigger rewrite.
- explanation-07: A single Postgres instance without replicas is a single point of failure.
- explanation-07: A database size number alone is not an appropriate trigger for sharding because size is not the actual constraint.
- explanation-08: Speedups from switching from JSON to a binary format vary widely, ranging from negligible to 5-10x.
- explanation-08: Two factors determine the payoff of switching to a binary format: the share of latency spent on serialization/parsing, and the payload shape.
- explanation-08: Request latency is composed of serialization/parsing plus network, database queries, and business logic.
- explanation-08: If JSON encoding/decoding is 40% of request time, switching to a binary format is worth doing.
- explanation-08: Binary formats mainly win on numeric-heavy or repetitive-schema payloads.
- explanation-08: Text-heavy or highly variable JSON payloads see much smaller gains from binary formats.
- explanation-08: A flamegraph or simple timers around JSON.parse/stringify equivalents can be used to profile serialization time.
- explanation-08: Typical payload sizes can be measured by logging them.
- explanation-08: Profiling the request path and measuring payload sizes takes roughly an hour of work.
- summarization-01: The app now starts up to 40% faster.
- summarization-02: Adding pool size to the config review checklist is a recommended remediation.
- summarization-03: The background worker pool would update the record after generating thumbnails.
- summarization-04: The bug is reproduced by clicking the "Export" button and then selecting the PDF option.
- summarization-04: After clicking the PDF export option, nothing happens initially.
- summarization-04: The expected PDF export behavior is consistent with the CSV export behavior.
- summarization-04: The issue was reproduced on the latest version of Firefox.
- summarization-04: The issue is likely a backend/server-side problem.
- summarization-05: Ada is assigned to check with the mobile team lead whether the mobile team was informed about the API deprecation.
- summarization-06: On March 3rd, the checkout service errored for about 40 minutes.
- summarization-06: The on-call engineer suspects connection-pool exhaustion in the payments client caused the checkout service errors.
- summarization-06: Pool metrics were not retained.
- summarization-06: The connection-pool exhaustion hypothesis remains unconfirmed.
- summarization-06: A deploy occurred 20 minutes before the checkout service errors began.
- summarization-06: That deploy touched retry settings.
- summarization-06: The deploy may have contributed to the outage.
- summarization-06: Rolling back the deploy alone did not restore service.
- summarization-06: Error rates recovered after a restart.
- summarization-06: The recovery after restart is consistent with several possible causes and does not prove any single cause.
- summarization-06: The team believes a retry storm amplified the outage.
- summarization-06: The team cannot yet demonstrate that a retry storm amplified the outage.
- summarization-07: The assistant checked its memory for relevant context on communication preferences before responding.
- summarization-07: No relevant information was found in memory.
- summarization-08: The recommendation is to prioritize investigating the link between the progress bar and abandonment.

Added facts (styled only):

- code-review-01: The assistant checked its memory for relevant guidance before reviewing.
- code-review-01: The memory check found nothing relevant to code review style.
- code-review-01: The mutable default argument is the most serious bug in the code.
- code-review-01: The bare `except:` should be replaced with a specific exception such as `except Exception as e`, and the error should be logged.
- code-review-01: Building a new list with `roles = [*roles, "member"]` avoids mutating the caller's list.
- code-review-01: The code does not check that `roles` contains valid role names.
- code-review-01: The suggested rewrite builds `all_roles` as `[*(roles or []), "member"]`.
- code-review-01: The suggested rewrite calls `db.insert({"name": name, "roles": all_roles})` and returns `True` on success.
- code-review-01: The suggested rewrite catches `Exception as e`, logs it with `logging.error`, and returns `False`.
- code-review-02: The fixed version throws an error when the profile is missing a name.
- code-review-03: The function has no docstring.
- code-review-03: The function has no type hints.
- code-review-03: Without type hints or documentation, a caller has to read the function body to know what the parameters and return value are.
- code-review-04: The assistant checked its memory directory and found no notes about the project or the user's preferences.
- code-review-04: The `reset` method carries the same thread-safety risk as `increment`.
- code-review-04: Because single assignment is atomic in CPython, `reset` is safe as currently written.
- code-review-04: If `reset` were later changed to depend on the old value, the race condition bug would return.
- code-review-04: Locking `reset` protects against future changes that would reintroduce the bug.
- code-review-04: Reading `counter.value` directly is not protected by the lock.
- code-review-04: An unprotected read of `counter.value` could observe the value mid-update on some Python implementations.
- code-review-04: Adding a `get_value` method that acquires the lock before returning `self.value` provides a safe read.
- code-review-04: The absence of `__repr__` and comparison methods is not a bug.
- code-review-04: Without `__repr__`, printing a `Counter` object displays `<Counter object at 0x...>` rather than the number.
- code-review-05: The line `cd "$BACKUP_DIR" || exit 1` should be added.
- code-review-05: The `-f` flag of `rm` suppresses errors, so failures go unnoticed.
- code-review-06: Replacing lists rather than merging them is standard behavior for merge patch semantics.
- code-review-06: merged.pop(key, None) does not raise an error if the key is missing.
- code-review-06: Deleting a key that does not exist does nothing.
- code-review-06: Because deletion of a missing key is silent, a typo in a key name to delete fails silently.
- code-review-06: The recommendation is to deep-copy nested structures so merged never shares references with base or override.
- code-review-06: The None-means-delete behavior is hidden and surprising to a first-time reader.
- code-review-07: The error-swallowing behavior is not documented anywhere.
- code-review-07: A legitimate null result from fn is indistinguishable from a swallowed error.
- code-review-07: If fn can return null on success, the caller cannot tell success from failure.
- code-review-07: The delay was probably intended to be exponential backoff such as 1000 * 2 ** i, but was written as linear backoff.
- code-review-07: When attempts is less than or equal to 0, the loop never runs and the function returns undefined immediately, producing no error and no result.
- code-review-07: If the null-on-failure behavior is intentional, it should be documented clearly.
- code-review-08: os.listdir raises an error if the target folder does not exist.
- code-review-08: The script has no check or fallback for a missing ROOT directory.
- code-review-08: The script uses a 45-day cutoff, written as 86400 * 45.
- code-review-08: The user said they did not set up the schedule that invokes the script.
- debugging-03: For the input `[1, 2, 3, 4]` with window size 2, `i = 2` gives the window `[3, 4]`.
- debugging-03: `moving_sum` returns the sum of each window of the given size.
- debugging-03: `moving_sum([1, 2, 3, 4], 2)` returns `[3, 5, 7]`.
- debugging-04: ASCII only covers byte values 0 through 127.
- debugging-04: UTF-8 can decode plain ASCII text.
- debugging-05: The failure occurs only when the tests run in an order where another test touches the shared default first.
- debugging-06: A connection leak would explain why the problem is rare and unpredictable.
- debugging-06: Slow or blocking queries can be caused by lock contention or missing indexes.
- debugging-06: There is a retry on attempt 2.
- debugging-06: The retry adds more load while the pool is already stressed, which can worsen the exhaustion.
- debugging-06: Enabling slow query logging on the database shows what ran just before each failure.
- debugging-06: Giving the export job its own dedicated pool separate from analytics is a possible quick mitigation.
- debugging-06: If failures stop after separating the pools, that confirms shared-pool contention as the root cause.
- debugging-06: Adding pool metrics and correlating timing require no code changes.
- debugging-07: A uniqueness or ordering collision is a likely cause of the flaky test.
- debugging-07: If events are keyed by a field that isn't guaranteed unique under concurrent writes, two events could collide and only one survives.
- debugging-07: Events may be keyed by timestamp or sequence number.
- debugging-07: Running only the test file 50 times with 4 workers and separately 50 times with 1 worker reproduces the load rather than just the parallelism.
- debugging-07: Failure only under 4 workers points toward the race cause or the shared-state cause.
- debugging-07: Checking test isolation involves looking at whether all workers point at the same database, cache, or queue.
- debugging-07: Giving each worker its own schema, database, or namespace fixes the shared-state cause if it is present.
- debugging-07: Logging in CI until the test fails again reveals whether an event is missing entirely, duplicated, or filtered out.
- debugging-07: Inspecting the digest's data path means reading the code between event seeded and digest built.
- debugging-07: Logging the digest's query bounds and the events' actual timestamps when the test fails rules out an off-by-a-few-milliseconds issue.
- debugging-07: Step 1, reproducing the load, is cheap.
- debugging-08: Growth tracking campaign weeks indicates something scales with request volume rather than only with product catalog size.
- debugging-08: Comparing bytes grown per day against request count per day is a better check than comparing growth against calendar days alone.
- debugging-08: If growth per request stays about the same across weeks, the leak is traffic-driven.
- debugging-08: The canary growth pattern points to two simultaneous leaks: a small general leak and a larger webhook-specific one.
- debugging-08: Profiling the canary and a normal instance under matched request rates and comparing growth rates is a way to check the two-leak hypothesis.
- debugging-08: A load test sending only webhook traffic to an isolated instance can show whether its growth rate matches production.
- debugging-08: Webhook-specific code for retries, dead-letter queues, or event buffers can grow unbounded.
- debugging-08: If the cache holds steady at its bound, the cache is not the cause.
- debugging-08: Compression, image handling, and database driver libraries are examples of third-party libraries that can leak outside the heap.
- debugging-08: Surviving quiet nights rules out causes tied to a daily cycle, such as a scheduled job that clears itself or a working time-based cache expiry.
- debugging-08: A full heap dump can be analyzed with a tool like Eclipse MAT.
- debugging-08: Taking two heap dumps a few hours apart on the same instance and comparing which object types grew the most should identify which of the four causes is real.
- explanation-01: Chaining never runs out of room because another item can always be added to a list.
- explanation-01: Most general-purpose hash maps use either chaining or open addressing.
- explanation-01: Python's dict uses one of these two approaches.
- explanation-01: Java's HashMap uses one of these two approaches.
- explanation-01: General-purpose hash maps often add tweaks to these approaches to handle edge cases well.
- explanation-02: An editor whose optimistic-locking save is rejected must reload the page and redo the edit.
- explanation-02: Content management systems and shopping carts are examples of good fits for optimistic locking.
- explanation-03: After packet loss, a TCP connection has to recover from the loss.
- explanation-03: ssthresh stands for slow start threshold.
- explanation-04: A thread crash can take down the whole program because all threads share memory.
- explanation-04: Inter-process data passing is slower because the data must cross the memory boundary.
- explanation-06: Profiling can show how much request time is spent in the database, in network calls, or in application code.
- explanation-06: If data changes often, a cache adds overhead for little benefit.
- explanation-06: APM stands for application performance monitoring.
- explanation-06: Timing logs can be added around database calls, external calls, and business logic to find where time goes.
- explanation-06: Databases can be checked for slow queries, missing indexes, and lock contention.
- explanation-06: The read-to-write ratio can be measured from logs or metrics.
- explanation-06: Planning a cache involves deciding what to cache, how long to keep it, and how to invalidate it.
- explanation-07: A well-tuned PostgreSQL instance can often handle tens of thousands of writes per second on strong hardware.
- explanation-07: Candidates for the first single-node limit to break include disk size, write throughput, connection count, and query latency.
- explanation-07: If most growth comes from one entity, such as a single large customer or a single busy table, it may be enough to partition that table or move it to its own instance rather than shard the whole database.
- explanation-07: Bigger disks, more RAM, read replicas, connection pooling, and query and index tuning are all cheaper and simpler than sharding.
- explanation-07: The product team cannot predict growth.
- explanation-07: A bad shard key causes hot shards that overload one node while others sit idle.
- explanation-07: Moving data between shards while the system is live is one of the hardest operations in distributed systems.
- explanation-07: Concrete triggers for sharding can include disk usage above 70%, write latency above a target threshold, or connection saturation.
- explanation-07: Cheaper options to exhaust before sharding include vertical scaling, read replicas, table partitioning, and archiving old data.
- explanation-08: The benefit of switching serialization formats depends on payload size and the network path.
- explanation-08: Smaller payloads help most when requests travel over slow or high-latency networks.
- explanation-08: If clients are close to the service on a fast network, smaller payloads may barely matter.
- explanation-08: Payload sizes for JSON and a candidate binary format should be compared on real data.
- explanation-08: Protocol Buffers is an example of a binary serialization format.
- explanation-08: MessagePack is an example of a binary serialization format.
- explanation-08: Adopting a binary format brings costs including schema management.
- explanation-08: Adopting a binary format makes debugging less human-readable.
- explanation-08: Adopting a binary format requires a migration across every client.
- explanation-08: The measured gain from a binary format needs to be worth the costs it introduces.
- summarization-01: The app now starts about 40% faster.
- summarization-05: The listed action items come from a sprint planning meeting.
- summarization-06: The speaker will check memory for relevant context before responding.
- summarization-06: A read command is issued targeting the path /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-5_ptlss1/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-yp4qod2b/memory/MEMORY.md
- summarization-06: The memory index file is named MEMORY.md.
- summarization-06: The memory directory is located under a project-specific path inside a style-config-pairs temporary directory.
- summarization-08: The observed drop-off makes the progress bar issue worth fixing.
- summarization-08: The template gallery observation is not a main finding.

### technical-simplified

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 31 | 21 | 0.677 | 27 | 7 |
| code-review-02 | 18 | 11 | 0.611 | 19 | 1 |
| code-review-03 | 28 | 0 | 0.0 | 6 | 6 |
| code-review-04 | 24 | 15 | 0.625 | 16 | 5 |
| code-review-05 | 32 | 19 | 0.594 | 27 | 2 |
| code-review-06 | 43 | 27 | 0.628 | 42 | 12 |
| code-review-08 | 54 | 36 | 0.667 | 41 | 9 |
| debugging-01 | 6 | 6 | 1.0 | 6 | 0 |
| debugging-02 | 14 | 10 | 0.714 | 14 | 1 |
| debugging-03 | 12 | 12 | 1.0 | 10 | 0 |
| debugging-04 | 15 | 7 | 0.467 | 12 | 1 |
| debugging-05 | 15 | 14 | 0.933 | 14 | 0 |
| debugging-06 | 24 | 12 | 0.5 | 26 | 12 |
| debugging-08 | 50 | 20 | 0.4 | 29 | 12 |
| explanation-01 | 43 | 21 | 0.488 | 20 | 0 |
| explanation-02 | 28 | 22 | 0.786 | 20 | 4 |
| explanation-03 | 38 | 17 | 0.447 | 22 | 2 |
| explanation-04 | 41 | 22 | 0.537 | 24 | 0 |
| explanation-05 | 19 | 11 | 0.579 | 15 | 0 |
| explanation-06 | 32 | 17 | 0.531 | 26 | 1 |
| explanation-07 | 28 | 18 | 0.643 | 21 | 7 |
| summarization-01 | 5 | 3 | 0.6 | 8 | 3 |
| summarization-02 | 14 | 12 | 0.857 | 12 | 1 |
| summarization-03 | 13 | 13 | 1.0 | 13 | 0 |
| summarization-04 | 16 | 12 | 0.75 | 12 | 1 |
| summarization-05 | 8 | 7 | 0.875 | 6 | 0 |

Median fraction: 0.627 over 26 scored pairs.

Median additions: 1.0 over 26 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python pitfall.
- code-review-01: The function does not check whether `"member"` is already in `roles`.
- code-review-01: If `roles` already contains `"member"`, it gets added a second time.
- code-review-01: The boolean return tells the caller nothing about what was inserted or why it failed.
- code-review-01: The fixed version raises `ValueError("name is required")` when `name` is falsy.
- code-review-01: The fixed version raises `ValueError("db is required")` when `db` is `None`.
- code-review-01: The fixed version uses `roles = list(roles) if roles else []`.
- code-review-01: The fixed version appends `"member"` only if it is not already in `roles`.
- code-review-01: The fixed version avoids silently swallowing exceptions, leaving handling to the caller.
- code-review-01: The fixed version prevents duplicate roles.
- code-review-02: Accessing `.name` on `undefined` throws a `TypeError: Cannot read properties of undefined`.
- code-review-02: The `async` keyword makes `loadProfile` return a `Promise`.
- code-review-02: The promise returned by `loadProfile` rejects synchronously due to the `TypeError` rather than because of awaited async work.
- code-review-02: The `.then` chain is neither returned nor awaited, so any rejection becomes an unhandled promise rejection.
- code-review-02: The code does not validate that `data` has a `name` property.
- code-review-02: If the API returns an unexpected value such as an error object, `.name` could be `undefined` and `.toUpperCase()` would throw.
- code-review-02: The fixed version removes the unused `profile` variable and the unused promise chain.
- code-review-03: The function concatenates `customer_name` and `status` directly into the query string.
- code-review-03: The function is vulnerable to SQL injection.
- code-review-03: The SQL injection vulnerability is critical.
- code-review-03: A caller passing user-controlled input such as `customer_name = "x' OR '1'='1"` can read, modify, or delete arbitrary data.
- code-review-03: The function must use parameterized queries instead of string concatenation.
- code-review-03: A parameterized fix is `cursor.execute("SELECT * FROM orders WHERE customer = %s AND status = %s", (customer_name, status))`.
- code-review-03: The correct placeholder style (`%s`, `?`, or `:name`) depends on the database driver.
- code-review-03: sqlite3 uses `?` as its placeholder.
- code-review-03: psycopg2 uses `%s` as its placeholder.
- code-review-03: MySQLdb uses `%s` as its placeholder.
- code-review-03: The query uses `SELECT *`.
- code-review-03: `SELECT *` is fragile.
- code-review-03: `SELECT *` breaks silently if columns are added, reordered, or removed.
- code-review-03: `SELECT *` pulls more data than is likely needed.
- code-review-03: Explicit column names are preferable to `SELECT *`.
- code-review-03: The function performs no input validation or type checking.
- code-review-03: If `customer_name` or `status` is not a string (e.g. `None`), the `+` concatenation raises a `TypeError`.
- code-review-03: The resulting `TypeError` produces a confusing stack trace rather than a clear error.
- code-review-03: The function has no error handling.
- code-review-03: `cursor.execute` can raise exceptions, such as from a bad connection or a lock timeout.
- code-review-03: Exceptions from `cursor.execute` propagate with no context added.
- code-review-03: Whether the lack of error handling is acceptable depends on the application's conventions.
- code-review-03: It is worth considering whether callers expect a wrapped or logged exception.
- code-review-03: The function has no pagination or limit.
- code-review-03: The function could return unbounded result sets on a wildcard-like match.
- code-review-03: The lack of pagination is more of a design consideration than a bug.
- code-review-03: The SQL injection issue is the only problem that actually needs fixing.
- code-review-03: All the other issues identified are secondary.
- code-review-04: The race condition gets worse under load.
- code-review-04: The window between the read and the write is exactly when a context switch is likely.
- code-review-04: The plain assignment `self.value = 0` is atomic in CPython.
- code-review-04: The atomicity of that assignment in CPython is provided by the GIL.
- code-review-04: The assignment `self.value = 0` is a single bytecode-level store.
- code-review-04: The atomicity of that assignment is a CPython implementation detail, not a guarantee of the Python language.
- code-review-04: Relying on CPython's assignment atomicity is fragile and non-portable to other Python implementations.
- code-review-04: PyPy has an STM mode.
- code-review-04: Python 3.13 has a free-threaded (no-GIL) build.
- code-review-05: With the literal string `*.tmp`, `rm -rf` fails harmlessly in this script.
- code-review-05: If no .log files exist, `*.log` will not expand unless `nullglob` is set.
- code-review-05: `nullglob` is not available in POSIX sh.
- code-review-05: If no .log files exist, `ls *.log` prints an error to stderr.
- code-review-05: If `gzip` fails partway through, the script continues and still prints "Cleaned" as if it succeeded.
- code-review-05: The script has no argument count check and should verify `$#` before proceeding.
- code-review-05: The script lacks `set -u`, which would have caught the empty-$1 problem.
- code-review-05: The suggested rewrite uses `#!/bin/sh` with `set -eu`.
- code-review-05: The suggested rewrite exits with status 1 and a usage message on stderr when `$#` is not 1.
- code-review-05: The suggested rewrite exits with status 1 and an error message on stderr when BACKUP_DIR is not a directory.
- code-review-05: The suggested rewrite uses `rm -f -- *.tmp` instead of `rm -rf *.tmp`.
- code-review-05: The suggested rewrite calls `gzip -- "$f"` with the filename quoted.
- code-review-05: The key fixes are argument and directory validation before destructive actions, `set -eu`, quoted variables, removal of the `ls` parsing anti-pattern, and a glob-no-match guard.
- code-review-06: The function resembles the JSON Merge Patch algorithm defined in RFC 7386.
- code-review-06: The JSON Merge Patch spec checks the patch value's type rather than the target's type.
- code-review-06: Recursive merging of a key produces no aliasing.
- code-review-06: Deletion via None only works when merging into a dict that already exists at that key.
- code-review-06: None values inside a newly-introduced nested dict are stored literally instead of being treated as deletions.
- code-review-06: The None sentinel means different things depending on whether the key already existed as a dict.
- code-review-06: JSON Merge Patch uses None (null) as a delete sentinel.
- code-review-06: Recursive merging applies only to `dict`, not to other mapping types.
- code-review-06: Custom Mapping subclasses and OrderedDict are examples of types not merged recursively.
- code-review-06: The `isinstance(..., dict)` check is strict rather than duck-typed.
- code-review-06: If base is a dict subclass, subclass-specific behavior is lost in the return value.
- code-review-06: The function has no cycle or self-reference protection.
- code-review-06: A self-referential input would cause infinite recursion.
- code-review-06: The function has no docstring and no type hints.
- code-review-06: The absence of a documented contract makes the analysis guesswork.
- code-review-06: The shallow-copy sharing and the asymmetric nested None deletion are subtler correctness traps that should at least be documented.
- code-review-08: os.path.getmtime works on directories.
- code-review-08: os.remove raises IsADirectoryError when called on a directory.
- code-review-08: An aborted run produces only a traceback, visible if run interactively.
- code-review-08: Because the script runs on a schedule, errors are unlikely to be noticed unless someone checks logs.
- code-review-08: os.listdir returns entries in an arbitrary, filesystem-dependent order.
- code-review-08: Because of arbitrary listing order plus the 500-item cap, which files get removed near the cap is essentially random.
- code-review-08: The script does not delete oldest files first.
- code-review-08: Deleting oldest first would require sorting by mtime.
- code-review-08: os.remove unlinks the symlink itself rather than the target.
- code-review-08: The unconditional tmp/part deletion is very likely not deliberate.
- code-review-08: The 45-day and 500 values were previously flagged by the user as magic numbers with no rationale.
- code-review-08: The script has no --dry-run mode.
- code-review-08: A dry-run mode is standard practice for scheduled deletion scripts.
- code-review-08: The absence of a dry-run mode is a gap rather than a bug.
- code-review-08: Without a dry-run mode, behavior cannot be safely tested in production without risking real deletions.
- code-review-08: The variable 'removed' is computed but is not logged or returned anywhere visible in the snippet.
- code-review-08: If 'removed' is meant to feed monitoring or alerting, that plumbing is missing.
- code-review-08: The likely genuine bugs are the cap not applying to tmp/part deletions, lack of exception isolation, arbitrary deletion order under the cap, and import-time CUTOFF computation.
- debugging-02: In strict mode or ES modules, `this` inside such a setInterval callback is undefined.
- debugging-02: The NaN value produced is what gets logged to the console.
- debugging-02: Calling .bind(this) on a regular function callback is an alternative fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` inside it is an alternative fix.
- debugging-04: The file contains a non-ASCII byte 0xc3 at byte 512.
- debugging-04: UTF-8 is the most common encoding to use for such files.
- debugging-04: Passing errors="ignore" to open() also prevents a crash on malformed or unexpected bytes.
- debugging-04: Mangling characters is acceptable if only line counts matter rather than content.
- debugging-04: The libraries chardet and charset-normalizer can detect a file's encoding.
- debugging-04: Opening a file in binary mode with "rb" avoids decoding entirely.
- debugging-04: Counting b"\n" bytes in binary mode counts lines without decoding.
- debugging-04: Iterating over a file object opened in binary mode yields lines.
- debugging-05: The fixed make_post sets tags to list(DEFAULT_TAGS) when tags is None.
- debugging-06: Contention with the analytics service is the most likely cause of the failures.
- debugging-06: The batch number at which the export job fails varies between runs.
- debugging-06: A varying failing batch number indicates the problem is timing-dependent rather than data-size-dependent.
- debugging-06: A connection leak in the export job's retry path is a plausible cause.
- debugging-06: If the combined pool sizes of the export job, the analytics service, and other clients exceed the database's max_connections, requests queue at the database even when each service's own pool appears to have headroom.
- debugging-06: Another nightly cron job scheduled near 02:14 UTC could be overlapping with the export job.
- debugging-06: The export job failures occur around 02:14 UTC.
- debugging-06: Checking whether the analytics service has a nightly job or cron firing around 02:xx UTC is free and may immediately confirm or rule out the leading suspect.
- debugging-06: Querying pg_stat_activity or an equivalent view during a live failure window, filtered by application or user, shows who is holding connections and whether any are idle in transaction or long-running.
- debugging-06: Summing all services' maximum pool sizes and comparing that total against the database's max_connections checks for oversubscription.
- debugging-06: Setting an alert on pool wait time or queue depth at a threshold below the 30s timeout would page someone with full context during the next occurrence.
- debugging-06: The relevant log fragment for the failure was lost to log rotation.
- debugging-08: A bounded cache with an unchanged bound and no code changes in a year is a less likely root cause.
- debugging-08: Eviction bugs are possible even in code that has not changed in a long time.
- debugging-08: The most likely hypothesis is a reference leak outside the cache.
- debugging-08: ThreadLocal or MDC context leaking on pooled threads is a possible reference leak source.
- debugging-08: A reference leak explains why the canary still grows slowly, because its own scheduled or background traffic hits the same code path.
- debugging-08: `jcmd <pid> GC.class_histogram` produces a heap class histogram on the JVM.
- debugging-08: Grepping for ThreadLocal usage in request-handling code that is not cleared on completion is a useful check.
- debugging-08: A metrics or observability cardinality leak is the second-ranked hypothesis.
- debugging-08: Using product or campaign identifiers as metric labels causes each new campaign to introduce new unique label combinations.
- debugging-08: A metrics cardinality leak matches the correlation between memory growth and marketing campaigns.
- debugging-08: Checking the unique series count on the /metrics endpoint over a week tests the metrics cardinality hypothesis.
- debugging-08: The metrics registry check can be done without a heap profiler.
- debugging-08: A cache bound bug or entry-size growth is the third-ranked hypothesis.
- debugging-08: Campaigns can increase average cache entry payload size through larger product descriptions or more variants and images.
- debugging-08: Off-heap or native allocation is the fourth-ranked hypothesis.
- debugging-08: Buffers for TLS, compression, and HTTP client connection pools are often native or off-heap.
- debugging-08: Off-heap buffers are not visible to a Java-style heap profiler.
- debugging-08: More traffic leads to more connections and buffers, matching the campaign correlation.
- debugging-08: Off-heap allocation matches the canary growing slowly from its own baseline connections.
- debugging-08: RSS growing while heap usage stays flat indicates off-heap memory growth.
- debugging-08: JVM native memory tracking is enabled with -XX:NativeMemoryTracking.
- debugging-08: pmap or smaps snapshots over time can diagnose native memory growth.
- debugging-08: Allocator fragmentation is the fifth-ranked, lower-priority hypothesis.
- debugging-08: Standard allocators such as glibc malloc do not always return freed memory to the OS.
- debugging-08: RSS can ratchet upward with allocation churn and never return to baseline due to fragmentation.
- debugging-08: More request churn produces more fragmentation.
- debugging-08: Setting MALLOC_ARENA_MAX=1 or swapping in jemalloc or tcmalloc on a test instance tests the fragmentation hypothesis.
- debugging-08: Comparing live-heap size from GC logs against process RSS helps detect fragmentation.
- debugging-08: The highest-leverage next action is taking a heap dump or histogram from the canary at two points several days apart.
- debugging-08: The canary's lower, steadier growth rate makes the responsible class or allocation site easier to isolate from noise.
- explanation-01: A hash map typically uses hash modulo array size (hash % array_size) to pick a slot in an underlying array.
- explanation-01: A slot in a hash map's underlying array is called a bucket.
- explanation-01: Collisions are not a bug.
- explanation-01: Collisions are unavoidable.
- explanation-01: There are infinitely many possible keys but only a finite number of buckets.
- explanation-01: Because keys are infinite and buckets are finite, two keys will eventually land in the same bucket.
- explanation-01: The inevitability of collisions is the same idea as the birthday paradox.
- explanation-01: Every hash map needs a strategy for handling collisions.
- explanation-01: The collection in a chaining bucket is usually a linked list, and sometimes a small array or a tree.
- explanation-01: Deletion under chaining is easy because the entry is just removed from the list.
- explanation-01: In the worst case, where everything hashes to one bucket, chaining lookup degrades to O(n) list traversal.
- explanation-01: Linear probing tries successive slots at index + 1, index + 2, and so on.
- explanation-01: Quadratic probing jumps by increasing squares, such as index + 1, index + 4, index + 9.
- explanation-01: Quadratic probing reduces clustering.
- explanation-01: Double hashing uses a second hash function to compute the probe step size.
- explanation-01: Open addressing performance degrades sharply as the table fills up because clustering gets worse.
- explanation-01: Deletion under open addressing cannot simply clear a slot, because doing so might break the probe chain for a later key.
- explanation-01: Deletion under open addressing typically requires a special deleted marker called a tombstone.
- explanation-01: Tuning open addressing involves keeping the load factor low, often below about 0.7.
- explanation-01: Tuning open addressing involves resizing and rehashing proactively.
- explanation-01: Both chaining and open addressing rely on resizing the underlying array and rehashing all entries once the load factor gets too high.
- explanation-01: Resizing and rehashing keep collisions manageable and keep operations close to O(1).
- explanation-02: PostgreSQL and MySQL support pessimistic locking via SELECT ... FOR UPDATE.
- explanation-02: Bank account transfers are an example use case for pessimistic locking.
- explanation-02: Seat reservations are an example use case for pessimistic locking.
- explanation-02: Editing a user profile is an example use case for optimistic locking.
- explanation-02: Editing a document in a CMS is an example use case for optimistic locking.
- explanation-02: Optimistic locking works well in stateless and distributed systems.
- explanation-03: A starting TCP sender does not know how many other connections share the path's bandwidth.
- explanation-03: A starting TCP sender does not know how much buffering exists in routers along the path.
- explanation-03: If a sender transmitted as fast as the receiver's window allowed, it could send more data than the network path can handle.
- explanation-03: Routers queue excess packets in their buffers.
- explanation-03: When router buffers fill up, routers start dropping packets.
- explanation-03: A burst of excess data can overwhelm shared routers and harm every connection passing through them.
- explanation-03: Congestion collapse is the scenario where the network is congested and throughput collapses.
- explanation-03: Congestion collapse was a real problem on the early internet in the 1980s.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The receiver's advertised window limits data based on the receiver's buffer space.
- explanation-03: Historically, TCP connections began with a congestion window of 1 segment.
- explanation-03: TCP connections now typically begin with a congestion window of 10 segments.
- explanation-03: RFC 6928 specifies the initial congestion window of 10 segments.
- explanation-03: Congestion avoidance uses linear growth instead of exponential growth.
- explanation-03: Growing linearly from the start would waste available bandwidth, especially on high-bandwidth, high-latency links.
- explanation-03: Linear growth from the start might take a long time to reach a reasonable sending rate.
- explanation-03: The name 'slow start' is misleading because the mechanism is not sluggish.
- explanation-03: Slow start is slow only relative to sending at full speed immediately.
- explanation-03: If a loss is detected after congestion avoidance begins, TCP reduces its rate, for example by cutting cwnd.
- explanation-03: After a loss, TCP often re-enters a slow-start-like ramp.
- explanation-03: TCP's congestion control philosophy allows millions of independent connections to share the internet's capacity without a central coordinator.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own register state, including the instruction pointer.
- explanation-04: A thread crash, such as a segfault, can take down the whole process.
- explanation-04: Sharing memory between threads requires locks or synchronization.
- explanation-04: Processes require IPC to communicate, such as pipes, sockets, or shared memory.
- explanation-04: IPC is slower and more explicit than direct memory sharing between threads.
- explanation-04: Process creation overhead includes creating a new address space and copy-on-write page tables.
- explanation-04: Older Ruby MRI has a global interpreter lock.
- explanation-04: Examples of work worth isolating in a process include processing untrusted input, running third-party plugins, and rendering a webpage.
- explanation-04: Browsers run tabs in separate processes.
- explanation-04: Gunicorn uses worker processes.
- explanation-04: nginx uses worker processes.
- explanation-04: Process boundaries can be further restricted with seccomp, containers, or chroot.
- explanation-04: With many threads, growing amounts of shared mutable state need locks.
- explanation-04: Lock contention, deadlocks, and race conditions become harder to reason about as thread count grows.
- explanation-04: Processes force explicit communication via message passing over IPC.
- explanation-04: Explicit message passing is often easier to get correct than shared mutable state, though slower.
- explanation-04: Processes can be killed and restarted independently without affecting other processes.
- explanation-04: Processes can be distributed across machines more naturally than threads.
- explanation-05: Root references include global variables and active stack frames.
- explanation-05: Garbage collection prevents leaks caused by forgotten pointers.
- explanation-05: A collection can be reachable by being a static field or a singleton.
- explanation-05: Long-lived objects that listeners attach to include event emitters, DOM elements, and global buses.
- explanation-05: A closure often captures its enclosing scope.
- explanation-05: A retained listener closure keeps a whole chain of otherwise-unused objects alive.
- explanation-05: Subscriptions to observables or streams that are not disposed can cause memory leaks.
- explanation-05: Timers or intervals holding references that are never cleared can cause memory leaks.
- explanation-06: N+1 queries are a possible cause of slowness.
- explanation-06: CPU-bound work is a possible cause of slowness.
- explanation-06: Lock contention is a possible cause of slowness.
- explanation-06: External API calls are a possible cause of slowness.
- explanation-06: Slow serialization is a possible cause of slowness.
- explanation-06: A cache requires extra infrastructure to run.
- explanation-06: The user said they do not know the read/write mix of the service.
- explanation-06: An indexed lookup is an example of a cheap read.
- explanation-06: If a workload is read-heavy and the reads are expensive, caching can provide a large benefit.
- explanation-06: Complex joins, aggregations, and external calls are examples of expensive reads.
- explanation-06: Adding basic request timing and logging reveals which endpoints are actually slow.
- explanation-06: An APM tool can be used to measure request timing.
- explanation-06: Running EXPLAIN on queries reveals whether they perform full table scans or are missing indexes.
- explanation-06: A slow API is often caused by a missing index or an N+1 query.
- explanation-06: Fixing a missing index or N+1 query is a smaller fix than building a cache layer.
- explanation-07: Vertical scaling (a bigger instance with more RAM and IOPS) and read replicas will likely suffice well past 1-2 TB of data.
- explanation-07: Sharding solves the problem of a dataset being too large for a single machine.
- explanation-07: Multi-tenant data keyed by customer_id shards cleanly at a later date with low regret.
- explanation-07: Managed Postgres offerings such as RDS, Aurora, and Cloud SQL scale to tens of terabytes.
- explanation-07: Managed Postgres offerings offer very large instance types.
- explanation-07: Sharding before usage patterns are known risks choosing the wrong shard key.
- explanation-07: Choosing the wrong shard key forces a later re-shard.
- explanation-07: Waiting risks that no natural shard key is designed into the schema, making eventual sharding a bigger rewrite.
- explanation-07: A single Postgres instance without replicas is a single point of failure.
- explanation-07: A database size number alone is not an appropriate trigger for sharding because size is not the actual constraint.
- summarization-01: Keyboard shortcuts were added for the ten most-used actions.
- summarization-01: The app now starts up to 40% faster.
- summarization-02: The smaller connection pool exhausted the available database connections.
- summarization-02: The incident ran from 09:14 to 09:48 UTC.
- summarization-04: After clicking the PDF export option, nothing happens initially.
- summarization-04: The expected PDF export behavior is consistent with the CSV export behavior.
- summarization-04: The issue was reproduced on the latest version of Firefox.
- summarization-04: The issue is likely a backend/server-side problem.
- summarization-05: Ada is assigned to check with the mobile team lead whether the mobile team was informed about the API deprecation.

Added facts (styled only):

- code-review-01: Specific errors, such as database errors, should be caught instead of using a bare `except`.
- code-review-01: The function has no type hints.
- code-review-01: Type hints for `name`, `roles`, `db`, and the return value would make the function easier to use correctly.
- code-review-01: The suggested fix annotates `roles` as `list[str] | None` with a default of `None`.
- code-review-01: The suggested fix returns `False` when `name` is falsy or `db` is `None`.
- code-review-01: The suggested fix catches `DatabaseError` instead of using a bare `except`.
- code-review-01: The suggested fix logs an error message with `logger.error` that includes the user name and the exception.
- code-review-02: The corrected version returns `profile.name.toUpperCase()`.
- code-review-03: The speaker is going to check their memory files for relevant context on the project.
- code-review-03: A bash tool is invoked.
- code-review-03: The bash command runs `cat` on the file /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-5_ptlss1/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-yp4qod2b/memory/MEMORY.md
- code-review-03: The command redirects standard error to /dev/null with `2>/dev/null`.
- code-review-03: The command echoes "NO_FILE" if the `cat` command fails.
- code-review-03: The bash tool call has the description "Check memory index".
- code-review-04: When `reset` runs between another thread's read and write in `increment`, the reset value is overwritten by the stale increment.
- code-review-04: Without a lock, the operations cannot be made atomic.
- code-review-04: The class has no method to read `self.value` safely.
- code-review-04: A thread that reads `self.value` directly can get a value in the middle of an update.
- code-review-04: A lock can be used with a `with` statement to guard `self.value` in `increment`, `reset`, and `get`.
- code-review-05: The script does not quote the variable in `rm -rf *.tmp`.
- code-review-05: The script does not check that the user has correct permissions.
- code-review-06: A new user can add None and lose data by mistake.
- code-review-06: The handling of the two type mismatch cases is inconsistent with each other.
- code-review-06: The two type mismatch cases require a decision to either both error or both replace.
- code-review-06: If base is not a dict, dict(base) can raise a TypeError.
- code-review-06: dict(base) can silently succeed if base is a list of key-value pairs.
- code-review-06: A deeply nested settings structure can hit the Python recursion limit and raise a RecursionError.
- code-review-06: The recursion depth issue is an edge case unlikely to matter for typical settings files.
- code-review-06: merged.pop(key, None) succeeds silently even when the key does not exist in merged.
- code-review-06: Silently ignoring a delete request for a missing key can hide a typo in the override data.
- code-review-06: The absence of input validation is classified as a likely bug.
- code-review-06: The silent delete of a missing key needs a decision from the team and could be intentional idempotence or a hidden way to miss typos.
- code-review-06: The recursion depth question needs a decision from the team and only matters if settings data can be deeply nested.
- code-review-08: The script does not check that ROOT exists.
- code-review-08: os.listdir(ROOT) raises an error when the directory is missing.
- code-review-08: The run fails with no clear message when ROOT is missing.
- code-review-08: The missing age check on tmp-/.part files is the highest-risk problem in the script.
- code-review-08: The script uses a hardcoded path.
- code-review-08: A fixed path can be a deliberate safety measure to stop a wrong environment variable from pointing the job at the wrong directory.
- code-review-08: The hardcoded path makes the script hard to test.
- code-review-08: Before changing the script, the schedule owner should be consulted.
- code-review-08: Recommended changes include a directory check using os.path.isfile.
- debugging-02: The value of `this.seconds` remains `NaN` on every tick.
- debugging-04: Passing errors="replace" replaces bad bytes with a placeholder character.
- debugging-06: A connection leak can explain a failure that happens about once a week rather than every night.
- debugging-06: The failure happens about once a week.
- debugging-06: The failure does not happen every night.
- debugging-06: A fixed pool size can become insufficient if traffic grows in both services.
- debugging-06: A brief spike in database response time can cause requests to hold connections longer than normal.
- debugging-06: Pool metrics include active connections, idle connections, and wait time.
- debugging-06: Slow query logging on the database can reveal queries running longer than a few seconds.
- debugging-06: The database can be queried for active locks and blocked sessions.
- debugging-06: Structured logging with a request ID links a failed request to a specific query.
- debugging-06: Structured logging with a request ID helps find the origin of a failed request later.
- debugging-06: The maximum number of connections the export job and analytics service can request together can be calculated and compared against the current pool size.
- debugging-06: Pool metrics and the slow query log show what happened during past failures.
- debugging-08: The four observations show two separate leaks.
- debugging-08: One of the leaks is tied to webhook traffic.
- debugging-08: One of the leaks runs at all times.
- debugging-08: A heap dump taken at the end of the day can be used to compare the count of cache-entry objects in the heap against the count the cache reports.
- debugging-08: Order services often track webhook state using an idempotency-key map, a retry queue, or an in-flight-request set.
- debugging-08: Heap histograms can be taken from the canary and a normal instance at the same time.
- debugging-08: Classes whose count is higher on the normal instance and that correlate with webhook volume indicate the webhook-tied leak.
- debugging-08: A full garbage collection can be forced during a quiet period through JMX or an admin endpoint.
- debugging-08: If memory use does not drop after a forced full garbage collection, the objects are still referenced somewhere.
- debugging-08: The recommended first step is taking a heap histogram from the canary and a normal instance at the same time of day.
- debugging-08: Class counts that differ between the canary and a normal instance point to the webhook-specific leak.
- debugging-08: Classes that grow on both instances point to the baseline leak.
- explanation-02: In the example, when a user reads the row, the app stores `version = 3`.
- explanation-02: When the user saves, the app runs an UPDATE statement that sets `balance = 100` and `version = 4` where `id = 1` and `version = 3`.
- explanation-02: If another process already changed the row, `version` no longer equals 3.
- explanation-02: Optimistic locking should be used when conflicts are rare and read operations are frequent.
- explanation-03: Dropped packets cause delay.
- explanation-03: Dropped packets waste bandwidth.
- explanation-06: Profiling includes checking for repeat reads.
- explanation-07: If write throughput stays under about 5,000 to 10,000 transactions per second, a single PostgreSQL instance is usually sufficient.
- explanation-07: Index maintenance and vacuum can slow down when a single table passes 1 to 2 TB or 1 billion rows.
- explanation-07: Compliance or data residency laws requiring data to stay in a specific region can force sharding regardless of database size.
- explanation-07: Cross-shard queries and reports become slow or require a separate analytics path.
- explanation-07: Vacuum and index rebuild times on very large tables can cause maintenance windows to grow.
- explanation-07: Large tables can be partitioned by date or tenant ID inside the same PostgreSQL instance.
- explanation-07: Partitioning solves most of the pain that sharding solves, without cross-instance complexity.
- summarization-01: The crash fix is listed under the "Fixes" section.
- summarization-01: The remaining three changes are listed under the "Improvements" section.
- summarization-01: Start time is about 40% faster.
- summarization-02: Production requires 50 connections.
- summarization-04: Clicking the PDF export button several times produces four identical "export failed" banners at once.

## Hedging survival

The judge lists the claims that the unstyled answer presents with uncertainty, then judges each claim in the styled answer: hedged (the uncertainty survives in some form), certain (the claim survives but reads as a fact — the failure this check targets), or absent (the claim is gone, a completeness loss). Survival is hedged / (hedged + certain). The claims that became certain appear verbatim below the table.

### actionable-clarity

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-02 | 2 | 1 | 0 | 1 | 1.0 |
| code-review-03 | 3 | 1 | 0 | 2 | 1.0 |
| code-review-04 | 1 | 0 | 0 | 1 | n/a |
| code-review-05 | 0 | 0 | 0 | 0 | n/a |
| code-review-06 | 10 | 6 | 1 | 3 | 0.857 |
| code-review-07 | 13 | 10 | 0 | 3 | 1.0 |
| code-review-08 | 9 | 8 | 1 | 0 | 0.889 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 2 | 0 | 1 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 11 | 11 | 0 | 0 | 1.0 |
| debugging-07 | 13 | 6 | 2 | 5 | 0.75 |
| debugging-08 | 6 | 4 | 0 | 2 | 1.0 |
| explanation-01 | 5 | 2 | 2 | 1 | 0.5 |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 5 | 2 | 3 | 0 | 0.4 |
| explanation-04 | 3 | 0 | 2 | 1 | 0.0 |
| explanation-05 | 1 | 0 | 0 | 1 | n/a |
| explanation-06 | 2 | 2 | 0 | 0 | 1.0 |
| explanation-07 | 3 | 1 | 2 | 0 | 0.333 |
| explanation-08 | 3 | 1 | 0 | 2 | 1.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 1 | 1 | 0 | 0 | 1.0 |
| summarization-04 | 2 | 1 | 0 | 1 | 1.0 |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 4 | 4 | 0 | 0 | 1.0 |

Claims: 108 over 32 judged pairs: 70 hedged, 14 certain, 24 absent.

Median survival: 1.0 over 21 scored pairs.

Claims that became certain:

- code-review-01: If the caller passes their own `roles` list, `.append("member")` mutates it in place, which can surprise the caller (side effect on their data).
- code-review-06: The four issues listed under 'Likely bugs' are likely bugs rather than certain ones.
- code-review-08: Which files get removed once you're near the 500 cap is essentially random/filesystem-order-dependent rather than oldest-first.
- debugging-07: Dev machines running serially rarely hit this race.
- debugging-07: Dumping seed results and the raw digest into the assertion message usually tells you which of the three seeds is missing, or whether the digest call happened too early.
- explanation-01: In open addressing, clearing a slot on deletion might break the probe chain for a later key.
- explanation-01: With open addressing you typically need a special "deleted" marker (a tombstone) to handle deletion.
- explanation-03: Every time the sender receives an ACK, it increases cwnd — roughly by one segment per ACK.
- explanation-03: Growing slowly and linearly from the very start might take a long time to reach a reasonable sending rate.
- explanation-03: If a loss is detected later, TCP reduces its rate and often re-enters a slow-start-like ramp.
- explanation-04: A thread crash (e.g., segfault) can take down the whole process.
- explanation-04: Since threads share everything with no memory-safety wall between them, a bug in one thread can corrupt another thread's data.
- explanation-07: Vertical scaling (bigger instance, more RAM/IOPS) and read replicas will likely carry you well past 1–2 TB.
- explanation-07: It doesn't sound like you have either a write-throughput problem or a dataset-too-large-for-one-box problem yet.

### clarity-flow

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-02 | 2 | 0 | 2 | 0 | 0.0 |
| code-review-03 | 3 | 0 | 2 | 1 | 0.0 |
| code-review-04 | 1 | 0 | 0 | 1 | n/a |
| code-review-05 | 0 | 0 | 0 | 0 | n/a |
| code-review-06 | 10 | 5 | 0 | 5 | 1.0 |
| code-review-07 | 13 | 5 | 1 | 7 | 0.833 |
| code-review-08 | 9 | 4 | 4 | 1 | 0.5 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 2 | 0 | 1 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 11 | 7 | 1 | 3 | 0.875 |
| debugging-07 | 13 | 7 | 2 | 4 | 0.778 |
| debugging-08 | 6 | 4 | 0 | 2 | 1.0 |
| explanation-01 | 5 | 1 | 0 | 4 | 1.0 |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 5 | 2 | 1 | 2 | 0.667 |
| explanation-04 | 3 | 1 | 1 | 1 | 0.5 |
| explanation-05 | 1 | 1 | 0 | 0 | 1.0 |
| explanation-06 | 2 | 1 | 1 | 0 | 0.5 |
| explanation-07 | 3 | 1 | 1 | 1 | 0.5 |
| explanation-08 | 3 | 1 | 0 | 2 | 1.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 1 | 1 | 0 | 0 | 1.0 |
| summarization-04 | 2 | 0 | 1 | 1 | 0.0 |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 4 | 4 | 0 | 0 | 1.0 |

Claims: 108 over 32 judged pairs: 54 hedged, 18 certain, 36 absent.

Median survival: 0.854 over 22 scored pairs.

Claims that became certain:

- code-review-01: If the caller passes their own `roles` list, `.append("member")` mutates it in place, which can surprise the caller (side effect on their data).
- code-review-02: If the response status isn't checked, an error page or empty body could be parsed as JSON and produce confusing downstream failures.
- code-review-02: Even once the timing bug is fixed, if the API returns something unexpected (e.g., an error object), `.name` could be `undefined`, and `.toUpperCase()` would still throw.
- code-review-03: `SELECT *` pulls more data than is likely needed.
- code-review-03: The lack of error handling around `cursor.execute` may be fine depending on the app's conventions, though it's worth considering whether callers expect a wrapped/logged exception.
- code-review-07: With unbounded linear backoff, synchronized retries across many clients could cause thundering-herd effects.
- code-review-08: The tmp/`.part` branch removing unconditionally while the age-based branch checks the 500 cap looks like a bug, not intentional, unless tmp/part files are trusted as always-safe-to-delete-unbounded.
- code-review-08: Because the script runs on a schedule, you likely won't see an aborting error unless someone checks logs.
- code-review-08: The global unbounded deletion of `tmp-`/`*.part` files regardless of age is very likely not deliberate.
- code-review-08: Likely genuine bugs: the cap not being applied to tmp/part deletions, the lack of crash/exception isolation, the arbitrary deletion order under the cap, and `CUTOFF` being computed at import time if the process is long-running.
- debugging-06: Steps #1 and #2 are cheap and will likely tell you whether this is contention or a leak before you need to touch the DB directly.
- debugging-07: Dev machines running serially rarely hit this race.
- debugging-07: If adding a short poll/retry loop before reading the digest makes the flake disappear, that strongly confirms an async/eventual-consistency race rather than a data-isolation bug.
- explanation-03: Every time the sender receives an ACK, it increases cwnd — roughly by one segment per ACK.
- explanation-04: Since threads share everything with no memory-safety wall between them, a bug in one thread can corrupt another thread's data.
- explanation-06: If the workload is read-heavy and those reads are expensive (complex joins, aggregations, external calls), caching could be a big win.
- explanation-07: Vertical scaling (bigger instance, more RAM/IOPS) and read replicas will likely carry you well past 1–2 TB.
- summarization-04: The issue is browser-independent (suggested by reproduction on Firefox and Chrome across two different machines/users)

### classic-concise

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 1 | 0 | 0 | 1.0 |
| code-review-02 | 2 | 0 | 0 | 2 | n/a |
| code-review-03 | 3 | 1 | 1 | 1 | 0.5 |
| code-review-04 | 1 | 0 | 0 | 1 | n/a |
| code-review-05 | 0 | 0 | 0 | 0 | n/a |
| code-review-06 | 10 | 7 | 0 | 3 | 1.0 |
| code-review-07 | 13 | 7 | 1 | 5 | 0.875 |
| code-review-08 | 9 | 5 | 3 | 1 | 0.625 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 2 | 0 | 1 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 11 | 9 | 0 | 2 | 1.0 |
| debugging-07 | 13 | 4 | 3 | 6 | 0.571 |
| debugging-08 | 6 | 1 | 0 | 5 | 1.0 |
| explanation-01 | 5 | 1 | 2 | 2 | 0.333 |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 5 | 1 | 2 | 2 | 0.333 |
| explanation-04 | 3 | 0 | 2 | 1 | 0.0 |
| explanation-05 | 1 | 0 | 0 | 1 | n/a |
| explanation-06 | 2 | 1 | 1 | 0 | 0.5 |
| explanation-07 | 3 | 1 | 2 | 0 | 0.333 |
| explanation-08 | 3 | 1 | 1 | 1 | 0.5 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 1 | 1 | 0 | 0 | 1.0 |
| summarization-04 | 2 | 0 | 0 | 2 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 4 | 3 | 1 | 0 | 0.75 |

Claims: 108 over 32 judged pairs: 53 hedged, 19 certain, 36 absent.

Median survival: 0.75 over 19 scored pairs.

Claims that became certain:

- code-review-03: The lack of error handling around `cursor.execute` may be fine depending on the app's conventions, though it's worth considering whether callers expect a wrapped/logged exception.
- code-review-07: With unbounded linear backoff, synchronized retries across many clients could cause thundering-herd effects.
- code-review-08: Because the script runs on a schedule, you likely won't see an aborting error unless someone checks logs.
- code-review-08: Which files get removed once you're near the 500 cap is essentially random/filesystem-order-dependent rather than oldest-first.
- code-review-08: Likely genuine bugs: the cap not being applied to tmp/part deletions, the lack of crash/exception isolation, the arbitrary deletion order under the cap, and `CUTOFF` being computed at import time if the process is long-running.
- debugging-07: Dev machines running serially rarely hit this race.
- debugging-07: The time-window boundary problem is more likely under load, which again correlates with parallel CI workers competing for CPU.
- debugging-07: If the test only flakes when the full suite runs, the suspected cause is shared fixture/account contamination from other tests rather than a bug in this test in isolation.
- explanation-01: In chaining, each bucket usually holds a linked list, though sometimes a small array or tree.
- explanation-01: With open addressing you typically need a special "deleted" marker (a tombstone) to handle deletion.
- explanation-03: Every time the sender receives an ACK, it increases cwnd — roughly by one segment per ACK.
- explanation-03: This causes cwnd to double approximately every round-trip time (RTT).
- explanation-04: A thread crash (e.g., segfault) can take down the whole process.
- explanation-04: Since threads share everything with no memory-safety wall between them, a bug in one thread can corrupt another thread's data.
- explanation-06: If the workload is read-heavy and those reads are expensive (complex joins, aggregations, external calls), caching could be a big win.
- explanation-07: Vertical scaling (bigger instance, more RAM/IOPS) and read replicas will likely carry you well past 1–2 TB.
- explanation-07: It doesn't sound like you have either a write-throughput problem or a dataset-too-large-for-one-box problem yet.
- explanation-08: Profiling a representative request path and measuring typical payload sizes is maybe an hour of work
- summarization-08: The stuck-progress-bar reports suggest a perception/feedback issue rather than a functional bug.

### concise

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-02 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-03 | 3 | 1 | 2 | 0 | 0.333 |
| code-review-04 | 1 | 0 | 0 | 1 | n/a |
| code-review-05 | 0 | 0 | 0 | 0 | n/a |
| code-review-06 | 10 | 6 | 1 | 3 | 0.857 |
| code-review-07 | 13 | 8 | 0 | 5 | 1.0 |
| code-review-08 | 9 | 5 | 3 | 1 | 0.625 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 2 | 0 | 1 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 11 | 8 | 2 | 1 | 0.8 |
| debugging-07 | 13 | 7 | 3 | 3 | 0.7 |
| debugging-08 | 6 | 4 | 0 | 2 | 1.0 |
| explanation-01 | 5 | 2 | 1 | 2 | 0.667 |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 5 | 1 | 1 | 3 | 0.5 |
| explanation-04 | 3 | 0 | 1 | 2 | 0.0 |
| explanation-05 | 1 | 1 | 0 | 0 | 1.0 |
| explanation-06 | 2 | 2 | 0 | 0 | 1.0 |
| explanation-07 | 3 | 0 | 3 | 0 | 0.0 |
| explanation-08 | 3 | 1 | 1 | 1 | 0.5 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 1 | 1 | 0 | 0 | 1.0 |
| summarization-04 | 2 | 0 | 1 | 1 | 0.0 |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 4 | 3 | 1 | 0 | 0.75 |

Claims: 108 over 32 judged pairs: 59 hedged, 22 certain, 27 absent.

Median survival: 0.725 over 22 scored pairs.

Claims that became certain:

- code-review-01: If the caller passes their own `roles` list, `.append("member")` mutates it in place, which can surprise the caller (side effect on their data).
- code-review-02: If the response status isn't checked, an error page or empty body could be parsed as JSON and produce confusing downstream failures.
- code-review-03: `SELECT *` pulls more data than is likely needed.
- code-review-03: The lack of error handling around `cursor.execute` may be fine depending on the app's conventions, though it's worth considering whether callers expect a wrapped/logged exception.
- code-review-06: The four issues listed under 'Likely bugs' are likely bugs rather than certain ones.
- code-review-08: The tmp/`.part` branch removing unconditionally while the age-based branch checks the 500 cap looks like a bug, not intentional, unless tmp/part files are trusted as always-safe-to-delete-unbounded.
- code-review-08: Which files get removed once you're near the 500 cap is essentially random/filesystem-order-dependent rather than oldest-first.
- code-review-08: Likely genuine bugs: the cap not being applied to tmp/part deletions, the lack of crash/exception isolation, the arbitrary deletion order under the cap, and `CUTOFF` being computed at import time if the process is long-running.
- debugging-06: The varying batch number at failure suggests the problem is timing-dependent rather than data-size-dependent — whichever batch happens to be running when analytics spikes.
- debugging-06: A connection leak would likely show up as pool usage creeping up over the job's runtime even without analytics interference.
- debugging-07: Dumping seed results and the raw digest into the assertion message usually tells you which of the three seeds is missing, or whether the digest call happened too early.
- debugging-07: If adding a short poll/retry loop before reading the digest makes the flake disappear, that strongly confirms an async/eventual-consistency race rather than a data-isolation bug.
- debugging-07: The fastest signal is usually step 1 (logging seed results and digest contents on failure) combined with step 4 (seeing whether a poll/retry makes it go away).
- explanation-01: With open addressing you typically need a special "deleted" marker (a tombstone) to handle deletion.
- explanation-03: This causes cwnd to double approximately every round-trip time (RTT).
- explanation-04: A thread crash (e.g., segfault) can take down the whole process.
- explanation-07: Vertical scaling (bigger instance, more RAM/IOPS) and read replicas will likely carry you well past 1–2 TB.
- explanation-07: It doesn't sound like you have either a write-throughput problem or a dataset-too-large-for-one-box problem yet.
- explanation-07: If you shard now, you likely guess the wrong shard key before usage patterns are known, forcing a re-shard later.
- explanation-08: Profiling a representative request path and measuring typical payload sizes is maybe an hour of work
- summarization-04: The issue is browser-independent (suggested by reproduction on Firefox and Chrome across two different machines/users)
- summarization-08: The stuck-progress-bar reports suggest a perception/feedback issue rather than a functional bug.

### developer-docs

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-02 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-03 | 3 | 0 | 2 | 1 | 0.0 |
| code-review-04 | 1 | 0 | 0 | 1 | n/a |
| code-review-05 | 0 | 0 | 0 | 0 | n/a |
| code-review-06 | 10 | 8 | 0 | 2 | 1.0 |
| code-review-07 | 13 | 11 | 0 | 2 | 1.0 |
| code-review-08 | 9 | 6 | 2 | 1 | 0.75 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 2 | 0 | 1 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 11 | 6 | 1 | 4 | 0.857 |
| debugging-07 | 13 | 6 | 3 | 4 | 0.667 |
| debugging-08 | 6 | 2 | 0 | 4 | 1.0 |
| explanation-01 | 5 | 1 | 3 | 1 | 0.25 |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 5 | 2 | 1 | 2 | 0.667 |
| explanation-04 | 3 | 0 | 2 | 1 | 0.0 |
| explanation-05 | 1 | 0 | 1 | 0 | 0.0 |
| explanation-06 | 2 | 2 | 0 | 0 | 1.0 |
| explanation-07 | 3 | 1 | 0 | 2 | 1.0 |
| explanation-08 | 3 | 0 | 2 | 1 | 0.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 1 | 1 | 0 | 0 | 1.0 |
| summarization-04 | 2 | 0 | 0 | 2 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 4 | 4 | 0 | 0 | 1.0 |

Claims: 108 over 32 judged pairs: 59 hedged, 19 certain, 30 absent.

Median survival: 0.857 over 21 scored pairs.

Claims that became certain:

- code-review-01: If the caller passes their own `roles` list, `.append("member")` mutates it in place, which can surprise the caller (side effect on their data).
- code-review-02: If the response status isn't checked, an error page or empty body could be parsed as JSON and produce confusing downstream failures.
- code-review-03: `SELECT *` pulls more data than is likely needed.
- code-review-03: The lack of error handling around `cursor.execute` may be fine depending on the app's conventions, though it's worth considering whether callers expect a wrapped/logged exception.
- code-review-08: Which files get removed once you're near the 500 cap is essentially random/filesystem-order-dependent rather than oldest-first.
- code-review-08: Likely genuine bugs: the cap not being applied to tmp/part deletions, the lack of crash/exception isolation, the arbitrary deletion order under the cap, and `CUTOFF` being computed at import time if the process is long-running.
- debugging-06: The varying batch number at failure suggests the problem is timing-dependent rather than data-size-dependent — whichever batch happens to be running when analytics spikes.
- debugging-07: Dev machines running serially rarely hit this race.
- debugging-07: Dumping seed results and the raw digest into the assertion message usually tells you which of the three seeds is missing, or whether the digest call happened too early.
- debugging-07: The fastest signal is usually step 1 (logging seed results and digest contents on failure) combined with step 4 (seeing whether a poll/retry makes it go away).
- explanation-01: In chaining, each bucket usually holds a linked list, though sometimes a small array or tree.
- explanation-01: In open addressing, clearing a slot on deletion might break the probe chain for a later key.
- explanation-01: With open addressing you typically need a special "deleted" marker (a tombstone) to handle deletion.
- explanation-03: Growing slowly and linearly from the very start might take a long time to reach a reasonable sending rate.
- explanation-04: A thread crash (e.g., segfault) can take down the whole process.
- explanation-04: Since threads share everything with no memory-safety wall between them, a bug in one thread can corrupt another thread's data.
- explanation-05: The closure created for an event listener often captures its enclosing scope, so the listener keeps a whole chain of otherwise-unused objects alive.
- explanation-08: JSON→binary speedups vary wildly, anywhere from negligible to 5-10x, depending on your actual bottleneck
- explanation-08: Profiling a representative request path and measuring typical payload sizes is maybe an hour of work

### plain-language

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 1 | 0 | 0 | 1.0 |
| code-review-02 | 2 | 0 | 2 | 0 | 0.0 |
| code-review-03 | 3 | 2 | 0 | 1 | 1.0 |
| code-review-04 | 1 | 0 | 0 | 1 | n/a |
| code-review-05 | 0 | 0 | 0 | 0 | n/a |
| code-review-06 | 10 | 6 | 1 | 3 | 0.857 |
| code-review-07 | 13 | 8 | 1 | 4 | 0.889 |
| code-review-08 | 9 | 7 | 1 | 1 | 0.875 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 2 | 1 | 0 | 0.667 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 11 | 7 | 1 | 3 | 0.875 |
| debugging-07 | 13 | 5 | 2 | 6 | 0.714 |
| debugging-08 | 6 | 4 | 0 | 2 | 1.0 |
| explanation-01 | 5 | 0 | 4 | 1 | 0.0 |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 5 | 2 | 2 | 1 | 0.5 |
| explanation-04 | 3 | 0 | 2 | 1 | 0.0 |
| explanation-05 | 1 | 0 | 0 | 1 | n/a |
| explanation-06 | 2 | 2 | 0 | 0 | 1.0 |
| explanation-07 | 3 | 2 | 0 | 1 | 1.0 |
| explanation-08 | 3 | 1 | 0 | 2 | 1.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 1 | 1 | 0 | 0 | 1.0 |
| summarization-04 | 2 | 0 | 1 | 1 | 0.0 |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 0 | 0 | 4 | n/a |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 4 | 3 | 1 | 0 | 0.75 |

Claims: 108 over 32 judged pairs: 56 hedged, 19 certain, 33 absent.

Median survival: 0.875 over 20 scored pairs.

Claims that became certain:

- code-review-02: If the response status isn't checked, an error page or empty body could be parsed as JSON and produce confusing downstream failures.
- code-review-02: Even once the timing bug is fixed, if the API returns something unexpected (e.g., an error object), `.name` could be `undefined`, and `.toUpperCase()` would still throw.
- code-review-06: Infinite recursion from a self-referential input is unlikely in practice for settings.
- code-review-07: With unbounded linear backoff, synchronized retries across many clients could cause thundering-herd effects.
- code-review-08: Which files get removed once you're near the 500 cap is essentially random/filesystem-order-dependent rather than oldest-first.
- debugging-04: Using errors="replace" (or "ignore") comes at the cost of possibly mangling odd characters.
- debugging-06: Steps #1 and #2 are cheap and will likely tell you whether this is contention or a leak before you need to touch the DB directly.
- debugging-07: Dumping seed results and the raw digest into the assertion message usually tells you which of the three seeds is missing, or whether the digest call happened too early.
- debugging-07: If adding a short poll/retry loop before reading the digest makes the flake disappear, that strongly confirms an async/eventual-consistency race rather than a data-isolation bug.
- explanation-01: In chaining, each bucket usually holds a linked list, though sometimes a small array or tree.
- explanation-01: In open addressing, clearing a slot on deletion might break the probe chain for a later key.
- explanation-01: With open addressing you typically need a special "deleted" marker (a tombstone) to handle deletion.
- explanation-01: Open addressing requires keeping the load factor low, often below about 0.7.
- explanation-03: Every time the sender receives an ACK, it increases cwnd — roughly by one segment per ACK.
- explanation-03: If a loss is detected later, TCP reduces its rate and often re-enters a slow-start-like ramp.
- explanation-04: A thread crash (e.g., segfault) can take down the whole process.
- explanation-04: Since threads share everything with no memory-safety wall between them, a bug in one thread can corrupt another thread's data.
- summarization-04: The issue is browser-independent (suggested by reproduction on Firefox and Chrome across two different machines/users)
- summarization-08: The stuck-progress-bar reports suggest a perception/feedback issue rather than a functional bug.

### technical-simplified

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-02 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-03 | 3 | 0 | 0 | 3 | n/a |
| code-review-04 | 1 | 0 | 0 | 1 | n/a |
| code-review-05 | 0 | 0 | 0 | 0 | n/a |
| code-review-06 | 10 | 6 | 0 | 4 | 1.0 |
| code-review-08 | 9 | 5 | 2 | 2 | 0.714 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 1 | 2 | 0 | 0.333 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 11 | 4 | 2 | 5 | 0.667 |
| debugging-08 | 6 | 1 | 0 | 5 | 1.0 |
| explanation-01 | 5 | 0 | 2 | 3 | 0.0 |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 5 | 1 | 3 | 1 | 0.25 |
| explanation-04 | 3 | 0 | 1 | 2 | 0.0 |
| explanation-05 | 1 | 0 | 0 | 1 | n/a |
| explanation-06 | 2 | 1 | 1 | 0 | 0.5 |
| explanation-07 | 3 | 0 | 1 | 2 | 0.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 1 | 1 | 0 | 0 | 1.0 |
| summarization-04 | 2 | 0 | 1 | 1 | 0.0 |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |

Claims: 68 over 26 judged pairs: 20 hedged, 17 certain, 31 absent.

Median survival: 0.291 over 14 scored pairs.

Claims that became certain:

- code-review-01: If the caller passes their own `roles` list, `.append("member")` mutates it in place, which can surprise the caller (side effect on their data).
- code-review-02: If the response status isn't checked, an error page or empty body could be parsed as JSON and produce confusing downstream failures.
- code-review-08: The tmp/`.part` branch removing unconditionally while the age-based branch checks the 500 cap looks like a bug, not intentional, unless tmp/part files are trusted as always-safe-to-delete-unbounded.
- code-review-08: Likely genuine bugs: the cap not being applied to tmp/part deletions, the lack of crash/exception isolation, the arbitrary deletion order under the cap, and `CUTOFF` being computed at import time if the process is long-running.
- debugging-04: The non-ASCII byte 0xc3 at byte 512 is likely part of a UTF-8 multi-byte sequence representing an accented character.
- debugging-04: Using errors="replace" (or "ignore") comes at the cost of possibly mangling odd characters.
- debugging-06: The varying batch number at failure suggests the problem is timing-dependent rather than data-size-dependent — whichever batch happens to be running when analytics spikes.
- debugging-06: Steps #1 and #2 are cheap and will likely tell you whether this is contention or a leak before you need to touch the DB directly.
- explanation-01: In chaining, each bucket usually holds a linked list, though sometimes a small array or tree.
- explanation-01: Open addressing requires keeping the load factor low, often below about 0.7.
- explanation-03: If the sender just blasted out data as fast as the receiver's window allowed, it could easily dump far more data onto the network than the path can handle.
- explanation-03: Every time the sender receives an ACK, it increases cwnd — roughly by one segment per ACK.
- explanation-03: If a loss is detected later, TCP reduces its rate and often re-enters a slow-start-like ramp.
- explanation-04: Since threads share everything with no memory-safety wall between them, a bug in one thread can corrupt another thread's data.
- explanation-06: If the workload is read-heavy and those reads are expensive (complex joins, aggregations, external calls), caching could be a big win.
- explanation-07: It doesn't sound like you have either a write-throughput problem or a dataset-too-large-for-one-box problem yet.
- summarization-04: The issue is browser-independent (suggested by reproduction on Firefox and Chrome across two different machines/users)

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 873, measured: 873.
Mean duration: 14358 ms. Mean wall: 28551 ms. Mean startup: 14193 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 873, measured: 873.
Input tokens: 1746 uncached, 1751616 cache write, 1810272 cache read. Output tokens: 1042085.
Cache-read share: 0.508.
Cache writes by lifetime: 1751616 at 5 minutes, 0 at 1 hour.

## Warnings

- technical-simplified/explanation-08: the pair failed the gate, excluded
- technical-simplified/code-review-07: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/summarization-07: the pair failed the gate, excluded
- technical-simplified/summarization-08: the pair failed the gate, excluded
- technical-simplified/debugging-07: the pair failed the gate, excluded
