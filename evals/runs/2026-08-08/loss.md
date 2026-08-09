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

Judge: opus. Judged on 2026-08-08T08:00:46+00:00.

## Completeness (fact survival)

The judge lists the facts of the unstyled answer, then checks each fact against the styled answer. The fraction is the share of the facts that survive. The judge also lists the facts of the styled answer and checks each fact against the unstyled answer: a styled fact that the unstyled answer does not state is an addition. The lost facts and the added facts appear verbatim below the table.

### clarity-flow

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 27 | 20 | 0.741 | 27 | 2 |
| code-review-02 | 21 | 19 | 0.905 | 18 | 3 |
| code-review-03 | 15 | 13 | 0.867 | 16 | 2 |
| code-review-04 | 25 | 19 | 0.76 | 17 | 3 |
| code-review-05 | 37 | 28 | 0.757 | 24 | 3 |
| code-review-06 | 26 | 17 | 0.654 | 30 | 7 |
| code-review-07 | 39 | 35 | 0.897 | 32 | 7 |
| code-review-08 | 37 | 27 | 0.73 | 38 | 6 |
| debugging-01 | 6 | 6 | 1.0 | 6 | 0 |
| debugging-02 | 16 | 12 | 0.75 | 11 | 1 |
| debugging-03 | 9 | 9 | 1.0 | 8 | 0 |
| debugging-04 | 16 | 11 | 0.688 | 16 | 5 |
| debugging-05 | 20 | 16 | 0.8 | 11 | 0 |
| debugging-06 | 6 | 1 | 0.167 | 28 | 28 |
| debugging-07 | 35 | 14 | 0.4 | 27 | 13 |
| debugging-08 | 36 | 15 | 0.417 | 26 | 14 |
| explanation-01 | 33 | 25 | 0.758 | 24 | 2 |
| explanation-02 | 28 | 21 | 0.75 | 22 | 4 |
| explanation-03 | 31 | 18 | 0.581 | 20 | 5 |
| explanation-04 | 45 | 27 | 0.6 | 27 | 4 |
| explanation-05 | 21 | 18 | 0.857 | 12 | 1 |
| explanation-06 | 15 | 13 | 0.867 | 16 | 0 |
| explanation-07 | 28 | 18 | 0.643 | 24 | 9 |
| explanation-08 | 11 | 10 | 0.909 | 16 | 6 |
| summarization-01 | 10 | 4 | 0.4 | 7 | 2 |
| summarization-02 | 15 | 10 | 0.667 | 13 | 1 |
| summarization-03 | 14 | 14 | 1.0 | 11 | 0 |
| summarization-04 | 13 | 13 | 1.0 | 15 | 2 |
| summarization-05 | 12 | 10 | 0.833 | 10 | 0 |
| summarization-06 | 13 | 13 | 1.0 | 16 | 2 |
| summarization-07 | 16 | 15 | 0.938 | 17 | 1 |
| summarization-08 | 26 | 23 | 0.885 | 19 | 3 |

Median fraction: 0.759 over 32 scored pairs.

Median additions: 2.5 over 32 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python gotcha.
- code-review-01: If a caller passes in their own `roles` list, `add_user` mutates it in place by appending `"member"`.
- code-review-01: Mutating the caller's list is a surprising side effect that is not signaled by the function's interface.
- code-review-01: The function has no duplicate-role handling.
- code-review-01: If `"member"` is already in `roles`, it gets appended again, creating duplicates.
- code-review-01: The proposed version appends `"member"` only if it is not already in `roles`.
- code-review-01: The proposed version avoids duplicate roles.
- code-review-02: The code unnecessarily mixes `async`/`await` with `.then()` chains.
- code-review-02: The fixed version throws an `Error` with message `Failed to load profile: ${res.status}` when `res.ok` is false.
- code-review-03: The parameterization fix also sidesteps quoting bugs.
- code-review-03: In the current code, a name containing an apostrophe would break the query.
- code-review-04: Over many concurrent calls, the final `value` will be less than the number of increments performed.
- code-review-04: If a reset happens after the read but before the write in `increment`, the increment silently undoes the reset by writing `1`.
- code-review-04: If callers read `counter.value` directly from another thread while an increment is in progress, they may observe a stale or inconsistent value.
- code-review-04: In CPython, the GIL protects the single attribute read, making the unsafe direct read less severe.
- code-review-04: Safety of the direct attribute read is not guaranteed by the Python language.
- code-review-04: Reading between the `current = self.value` and `self.value = ...` steps in `increment` can return an intermediate value.
- code-review-05: The missing `cd` success check is the most dangerous bug in the script.
- code-review-05: The variables `$1`, `$BACKUP_DIR`, and `$f` are unquoted in the script.
- code-review-05: The unquoted variables should be written as `"$1"`, `"$BACKUP_DIR"`, and `"$f"`.
- code-review-05: With default shell globbing, if no `.tmp` files exist, `rm` receives the literal string `*.tmp` and errors out.
- code-review-05: The `rm -rf *.tmp` no-match error is harmless in this script but sloppy and confusing.
- code-review-05: The script contains the line `echo Cleaned $BACKUP_DIR`, which is unquoted.
- code-review-05: The `echo Cleaned $BACKUP_DIR` message is misleading if `cd` never actually happened.
- code-review-05: The script does not restore the original working directory when it finishes.
- code-review-05: Failing to restore the original working directory matters if the script is sourced or chained with other commands.
- code-review-06: The recursion condition checks only that the existing value is a dict, not that the override value is a dict.
- code-review-06: Merging base={'a': {'x': 1}} with override={'a': 'oops'} raises AttributeError: 'str' object has no attribute 'items' inside the recursive call.
- code-review-06: The missing type check on the override value is a real crash bug for malformed or unexpected input.
- code-review-06: Values not touched by the override, or assigned directly via the `else` branch, are shared by reference with `base` or `override` rather than copied.
- code-review-06: A dict value in `override` under a key not already in `merged` is aliased directly instead of being merged or copied.
- code-review-06: The aliasing behavior for new nested dicts is asymmetric with the recurse-into-dicts path.
- code-review-06: Using `None` as a deletion marker is a common config-merging convention known as a tombstone value.
- code-review-06: Using `is None` instead of a falsiness check means `0`, `False`, and `""` are treated as real values.
- code-review-06: `dict(base)` always returns a plain `dict`, so a subclass type such as `OrderedDict` or a custom Mapping is lost.
- code-review-07: The helper has three distinct signals for failure: null, undefined, and a thrown error.
- code-review-07: There is no consistent contract across the three failure signals.
- code-review-07: The asymmetry between 429 and 5xx backoff is more likely an oversight than a considered choice.
- code-review-07: Swallowing non-HTTP errors into null is probably accidental.
- code-review-08: The script contains no `if __name__ == "__main__":` block.
- code-review-08: The function `clean()` is never called anywhere in the script.
- code-review-08: If the scheduler runs the script via `python script.py`, the script does nothing.
- code-review-08: If the cleanup runs while another job is writing `tmp-export-123.part`, the file is deleted and the writer either errors or produces a truncated file.
- code-review-08: The script's own tmp-file deletion branch can race with a concurrent run of the same script.
- code-review-08: `os.path.getmtime` works on a directory.
- code-review-08: The script uses the constant `86400 * 45`, corresponding to a 45-day retention period.
- code-review-08: The rationale for the `86400 * 45` and `500` constants is undocumented and nobody can recall it.
- code-review-08: The script's current behavior falls into one of three cases: inert, silently corrupting data, or working as intended.
- code-review-08: Determining how `clean()` is invoked and whether anything creates `tmp-*`/`*.part` files as working files decides which of those three cases applies.
- debugging-02: `this.seconds += 1` where `this` is `undefined` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: Outside a class or strict-mode context, `this` in a plain function call defaults to the global object.
- debugging-02: With `this` as the global object, `this.seconds` would be `undefined`, and `undefined + 1` evaluates to `NaN`.
- debugging-02: In the non-strict case, `NaN` would be printed each tick.
- debugging-04: A file's encoding may not be under the caller's control.
- debugging-04: Opening a file in binary mode with "rb" avoids decoding text.
- debugging-04: Binary mode can be used when only a line count is needed.
- debugging-04: Iterating a file object in binary mode splits on \n bytes.
- debugging-04: The binary-mode approach sidesteps encoding issues entirely.
- debugging-05: A function's default value is stored on the function object itself.
- debugging-05: The failure looks flaky but is deterministic given the call order.
- debugging-05: The fix also protects callers who pass their own `tags` list from having it mutated as a side effect.
- debugging-05: Copying a caller-supplied `tags` list, e.g. `tags = list(tags) if tags is not None else list(DEFAULT_TAGS)`, avoids mutating the caller's list.
- debugging-06: The speaker will check whether the directory contains relevant code before answering.
- debugging-06: The Bash tool was invoked.
- debugging-06: The command issued was `ls -la`.
- debugging-06: The command's stated purpose was to list files in the working directory.
- debugging-06: The working directory should be checked for relevant code before the question is answered.
- debugging-07: The parallelism is almost certainly relevant to the failure rather than incidental.
- debugging-07: If the digest query is scoped by a time window rather than a unique test/user/session ID, a concurrently running test in another worker can insert or delete rows that the test sees.
- debugging-07: Serial runs never share concurrent state, so cross-test leakage only appears under parallelism.
- debugging-07: Cross-test data leakage from shared state is the single most common cause of this exact symptom.
- debugging-07: If cleanup uses TRUNCATE, shared sequence resets, or a global counter instead of per-worker or per-test transactions, one worker's teardown can wipe or renumber rows another worker just wrote.
- debugging-07: An autoincrement ID or pagination boundary issue is a plausible cause.
- debugging-07: If the digest endpoint has an implicit LIMIT and orders by an insufficiently unique ID or timestamp, concurrent inserts from other workers can push one of the test's events outside the page or limit boundary.
- debugging-07: Connection pool or DB isolation level behavior is a plausible cause.
- debugging-07: READ COMMITTED with async replication, or a connection pool reusing a stale snapshot, can cause a worker to read a stale view missing the third insert.
- debugging-07: The cheapest first diagnostic step is to reproduce locally under contention by running the whole suite with `pytest -n 4` repeatedly.
- debugging-07: pytest-repeat provides a `--count` option, e.g. `--count=50`.
- debugging-07: If the failure reproduces locally under parallelism, that confirms it is parallelism-driven rather than CI-infrastructure-specific.
- debugging-07: Reproducing locally allows debugging with full tooling.
- debugging-07: The second step is to run only this test file or test repeatedly under `-n 4` to distinguish cross-test pollution from an internal race.
- debugging-07: If the test never fails alone under `-n 4` but fails with the full suite, that strongly implicates shared state or fixtures rather than an internal race.
- debugging-07: Diagnostics added to the test should be temporary rather than permanent.
- debugging-07: If the digest contains an unexpected event ID belonging to another test, that directly confirms cross-test data leakage.
- debugging-07: A diagnostic step is to grep whether the API seeding path involves a queue, Celery task, outbox pattern, or cache layer.
- debugging-07: pytest-django's `--reuse-db` can interact badly with `-n`.
- debugging-07: The recommended first move is reproducing under `-n 4` locally, because it turns an unreproducible CI-only flake into something iterable.
- debugging-07: The recommended second move is bisecting isolation problems versus an internal race.
- debugging-08: The observed pattern consists of steady percentage growth, no overnight recovery, presence without webhooks but faster growth with them, and a cache that has not changed.
- debugging-08: The pattern points away from a single 'leaky cache' explanation.
- debugging-08: The pattern points toward something unbounded that is driven by order volume.
- debugging-08: An unbounded per-order or per-webhook tracking structure is the explanation most consistent with all four observations.
- debugging-08: Examples of such tracking structures include idempotency keys, dedup sets, in-flight/retry state, and in-memory audit logs.
- debugging-08: An unbounded per-order tracking structure grows with every order, which explains growth on the canary.
- debugging-08: An unbounded tracking structure shows unbounded object count growth over time even when the request rate is flat.
- debugging-08: High-cardinality metrics or logging labels, such as per-order-id, per-webhook-id, or per-campaign-id tags, are a possible cause.
- debugging-08: Metrics clients often retain one time series per unique label combination forever.
- debugging-08: High-cardinality labels match the campaign correlation because campaigns produce more unique IDs and campaign tags.
- debugging-08: High-cardinality labels match canary growth because the canary still emits per-order metrics.
- debugging-08: One check is to query the metrics backend for active series or cardinality count over the same window as the memory graph.
- debugging-08: If metric cardinality climbs monotonically alongside RSS, high-cardinality labels are the cause.
- debugging-08: One check is to pick evicted product IDs in a heap dump and trace their GC roots to see if anything outside the cache still retains them.
- debugging-08: Allocator or runtime fragmentation, rather than a true leak, is a possible cause.
- debugging-08: Fragmentation would explain gradual RSS growth that does not return to baseline, independent of application logic.
- debugging-08: One check is to compare process RSS to the runtime's reported live heap size over the same period.
- debugging-08: If live heap is flat while RSS climbs, the cause is fragmentation rather than retained objects.
- debugging-08: Fragmentation requires a different fix than retained objects.
- debugging-08: Diffing object counts by type will immediately reveal which of the first four causes is real.
- debugging-08: The exact diagnostic tool to use differs by runtime, such as JVM, Node, or Go.
- explanation-01: An example of computing an index is hash("apple") % array_size.
- explanation-01: Deletion under separate chaining is easy because the entry is just removed from the list.
- explanation-01: In the worst case, with many collisions in one slot, separate chaining degrades to O(n) list traversal.
- explanation-01: Quadratic probing tries index+1², then index+2², and so on.
- explanation-01: Deletion under open addressing usually needs a "tombstone" marker.
- explanation-01: Open addressing requires resizing/rehashing earlier, typically once the load factor exceeds about 0.7.
- explanation-01: Deletion is simple with chaining, whereas open addressing needs tombstones or shifting.
- explanation-01: Rust's HashMap uses an open addressing variant.
- explanation-02: An optimistic-locking stock update can be written as: UPDATE products SET stock = stock - 1, version = version + 1 WHERE id = 42 AND version = 7.
- explanation-02: A CMS article edit is an example workload suited to optimistic locking.
- explanation-02: A shopping cart is an example workload suited to optimistic locking.
- explanation-02: Postgres and MySQL support pessimistic locking via SELECT ... FOR UPDATE.
- explanation-02: A pessimistic locking example is: BEGIN; SELECT stock FROM products WHERE id = 42 FOR UPDATE; UPDATE products SET stock = stock - 1 WHERE id = 42; COMMIT;
- explanation-02: Seat and inventory reservation systems are examples of workloads suited to pessimistic locking.
- explanation-02: In reservation systems, two users grabbing the last item is unacceptable.
- explanation-03: If a sender sends data as fast as the receiver's advertised window allows, it can overwhelm a router queue.
- explanation-03: Dropped packets cause retransmissions.
- explanation-03: Dropped packets cause wasted bandwidth.
- explanation-03: Slow start is also used after certain recovery events.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The sender's actual sending rate is limited by the smaller of the congestion window and the receiver's advertised window.
- explanation-03: The initial cwnd was historically 1 segment.
- explanation-03: The initial cwnd is now typically 2-10 segments.
- explanation-03: RFC 6928 raised the initial congestion window value to improve performance for short flows.
- explanation-03: The congestion avoidance phase is more conservative than slow start and uses linear growth.
- explanation-03: When packet loss is detected, ssthresh is lowered and cwnd is reset or cut back.
- explanation-03: The name 'slow start' is slightly misleading because the growth is exponential and ramps up quickly.
- explanation-03: The name 'slow start' refers to starting from a small window rather than assuming the full receiver-advertised window can be used immediately.
- explanation-04: A process is an independent instance of a running program.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own instruction pointer.
- explanation-04: Threads are cheaper to create than processes.
- explanation-04: A crashed process can be restarted independently.
- explanation-04: nginx uses multiple processes.
- explanation-04: Chrome uses a per-tab process model.
- explanation-04: Threads release the GIL while waiting on I/O.
- explanation-04: Processes can run under different privilege levels.
- explanation-04: Multiple processes are preferable when components need independent lifecycle management.
- explanation-04: Separate processes allow components to be started, stopped, restarted, or scaled independently using OS-level tools.
- explanation-04: OS-level tools for managing processes include kill, restart, and resource limits via cgroups.
- explanation-04: Using separate processes avoids coordinating shutdown logic inside one program.
- explanation-04: Threads have lower creation cost than processes.
- explanation-04: Threads have faster context switches than processes.
- explanation-04: Processes win when isolation is needed: fault tolerance, true CPU parallelism around language-level locks, security boundaries, or independent lifecycle.
- explanation-04: Processes have higher memory overhead than threads.
- explanation-04: Inter-process communication mechanisms include pipes, sockets, and shared memory segments.
- explanation-05: A garbage collector walks references starting from roots.
- explanation-05: Roots include global variables, stack frames, and active closures.
- explanation-05: Eviction mechanisms include TTL, LRU, and a size cap.
- explanation-06: Possible alternative causes of the performance problem include slow queries, network latency, N+1 calls, and serialization.
- explanation-06: A cache is another system that must be operated.
- explanation-07: Sharding is a one-way architectural decision.
- explanation-07: Sharding only helps when the constraint is write throughput, storage, or single-node CPU/IO that vertical scaling cannot fix.
- explanation-07: If the bottleneck is bad queries, missing indexes, or lock contention, sharding will not fix it.
- explanation-07: Sharding replicates query, index, and lock-contention problems across all nodes.
- explanation-07: At 20% utilization on a mid-size instance, there is likely 5-10x runway before sharding is urgent.
- explanation-07: Building routing and rebalancing infrastructure can take months.
- explanation-07: Premature sharding causes a permanent drop in team velocity.
- explanation-07: Waiting too long is usually still cheaper than premature sharding.
- explanation-07: Postgres native partitioning by date or tenant addresses table size and vacuum/index bloat concerns.
- explanation-07: Sharding should be revisited only when utilization numbers show vertical scaling, partitioning, and read replicas will not suffice for the next 12-18 months.
- explanation-08: The performance win from changing serialization could range from negligible to significant.
- summarization-01: The app now starts up to 40% faster.
- summarization-01: Hovering over any toolbar button displays that button's keyboard shortcut.
- summarization-01: Internal build tooling changes were omitted from these release notes.
- summarization-01: Module refactoring changes were omitted from these release notes.
- summarization-01: Telemetry batching changes were omitted from these release notes.
- summarization-01: The omitted changes have no user-facing effect.
- summarization-02: The small pool size of 5 was intentional for staging.
- summarization-02: The incident caused an approximately 12% error rate for checkout.
- summarization-02: The incident was detected at 09:14.
- summarization-02: An on-call engineer was paged at 09:21.
- summarization-02: The change was rolled back at 09:48.
- summarization-05: Ada is assigned to check with the mobile team's lead about whether the mobile team was informed of the API deprecation.
- summarization-05: The mobile team has a lead.
- summarization-07: Memory impact, production tail latency, and the crash's cause all need further investigation before rollout.
- summarization-08: The progress bar finding is rated FIRM, with the cause tentative.
- summarization-08: No action is recommended yet on the template gallery.
- summarization-08: Template gallery usage data is worth tracking at scale.

Added facts (styled only):

- code-review-01: The function has five real problems.
- code-review-01: The proposed fix raises `ValueError("name is required")` when `name` is falsy.
- code-review-02: The code throws a `TypeError` on every call.
- code-review-02: A network error or non-2xx status produces an unhandled promise rejection instead of a meaningful error to the caller.
- code-review-02: The fixed version throws an `Error` with the user ID and response status when `res.ok` is false.
- code-review-03: The function has no error handling.
- code-review-03: A malformed query or database error propagates as a raw exception with no context for the caller.
- code-review-04: A thread in the middle of an increment can have its write overwritten by a concurrent `reset`.
- code-review-04: CPython's GIL makes each bytecode operation atomic.
- code-review-04: A read-modify-write in Python compiles to three separate bytecode ops: `LOAD`, `ADD`, and `STORE`.
- code-review-05: If the directory doesn't exist or `$BACKUP_DIR` is empty, `cd` fails silently.
- code-review-05: `rm -rf *.tmp` deletes files with no confirmation.
- code-review-05: Using `--` before filenames protects against filenames starting with `-`.
- code-review-06: If `merged[key]` is a dict and `value` is not (or vice versa), the code overwrites instead of raising an error.
- code-review-06: A type mismatch on merge can hide a config-schema mismatch, such as a string shadowing a nested config section.
- code-review-06: `isinstance(merged[key], dict)` fails for `OrderedDict`, custom `Mapping` types, and similar mapping types.
- code-review-06: Some config systems expect list concatenation or deduplication.
- code-review-06: Deeply nested structures could hit Python's recursion limit.
- code-review-06: If `base` or `override` is not a dict or is `None`, the function throws a generic `AttributeError` internally without indicating which argument was bad.
- code-review-06: `None`-as-delete is common in Kubernetes-style overlay configs.
- code-review-07: Preventing lockstep retries under load is the purpose of backoff.
- code-review-07: The default `attempts = 3` is small and cannot be configured per call.
- code-review-07: Calling with `attempts = 0` silently returns undefined without ever invoking `fn`.
- code-review-07: Treating 4xx client errors other than 429 as non-retryable is sound practice.
- code-review-07: Returning null on non-retryable errors is almost certainly deliberate.
- code-review-07: Checking a returned value for falsiness instead of catching is a callback-era pattern.
- code-review-07: The undefined-on-exhaustion path and the missing initial delay are clear bugs worth fixing regardless.
- code-review-08: os.path.getmtime(path) and os.remove(path) do not handle directories.
- code-review-08: The aborted run fails silently unless something upstream catches the error.
- code-review-08: If the mount is briefly unavailable, the script dies with no context in the error.
- code-review-08: Without a dry-run mode, the script cannot be safely tested against a real ROOT before being trusted.
- code-review-08: The 45-day cutoff needs a comment citing the actual policy or ticket.
- code-review-08: The tmp-/.part branch is the only branch that can delete something still in use.
- debugging-02: `this.seconds` reads as `undefined` in the callback.
- debugging-04: The file contains a non-ASCII byte at position 512.
- debugging-04: A file's encoding can be detected at runtime when it is not known in advance.
- debugging-04: `charset-normalizer` is a library for detecting character encodings.
- debugging-04: `chardet` is a library for detecting character encodings.
- debugging-04: `errors="replace"` keeps the line count accurate even if a few bytes are malformed.
- debugging-06: The export service and the analytics service compete for a shared connection pool.
- debugging-06: The shared connection pool is undersized.
- debugging-06: The export's requests have a 30-second timeout.
- debugging-06: Something occasionally holds connections long enough that the export's requests queue past the 30s timeout.
- debugging-06: The likely connection holders are a long-running analytics query, a lock, or a connection leak.
- debugging-06: The batch number varies across the failures.
- debugging-06: The varying batch number indicates a timing/contention issue rather than bad data in a specific batch.
- debugging-06: A periodic analytics query, such as report generation or a weekly rollup, may hold connections or lock tables the export touches.
- debugging-06: Failures may cluster around a weekly analytics schedule.
- debugging-06: A connection leak occurs when a code path checks out a connection and never returns it.
- debugging-06: A connection leak causes the pool to slowly fill until nightly load hits the ceiling.
- debugging-06: A connection leak would explain why the failures are intermittent rather than constant.
- debugging-06: The export runs nightly.
- debugging-06: The pool size may have been set assuming isolated usage by one service.
- debugging-06: Concurrent demand from both services can exceed the pool size under load.
- debugging-06: A slow query or lock wait on the database side can make connections unavailable even when the pool configuration is fine.
- debugging-06: Correlating failure timestamps is more informative than correlating batch numbers.
- debugging-06: Analytics service logs and DB slow-query/lock logs can be pulled for the exact failure windows.
- debugging-06: One failure window was 02:14:07 to 02:14:41.
- debugging-06: Active, idle, and waiting connection counts can be logged on a timer to capture pool metrics.
- debugging-06: A pool near capacity before failures begin points to a connection leak or undersizing.
- debugging-06: A sudden spike in pool usage points to a single long-running query.
- debugging-06: pg_stat_activity, or its equivalent, shows long-running and idle-in-transaction connections and lock wait events.
- debugging-06: Checked-out connections trending upward across the week and resetting only on service restart indicates a leak rather than contention.
- debugging-06: Increasing pool and timeout logging retention prevents the next occurrence from being lost to log rotation.
- debugging-06: The provided log fragment alone cannot distinguish a leak from contention or undersizing.
- debugging-06: The database type and pool library have not been provided.
- debugging-06: Knowing the database type and pool library would allow pointing to specific metrics and queries to check.
- debugging-07: The most likely cause of the failure is a race between seeding and reading.
- debugging-07: If the digest is scoped to a time window and the three seed calls straddle a boundary, the slowest seed call can fall outside the window and be excluded.
- debugging-07: The time-window bucketing failure requires no parallelism, only enough latency variance.
- debugging-07: Examples of poor worker isolation include a shared schema, a shared in-memory store, and non-worker-scoped keys.
- debugging-07: If the test does not check the response status or body of each of the three creation calls, a timeout or 5xx under CI load would leave only two events persisted.
- debugging-07: A silently failing seed call produces no exception, just a smaller digest.
- debugging-07: Dumping the three seed responses (status, returned IDs) and the raw digest payload to stdout on assertion failure usually reveals which of the four causes applies on the next flake.
- debugging-07: Asserting on each seed call's status converts the mystery into a clear failure such as "event 3 returned 503".
- debugging-07: Reproducing the failure locally is more likely under artificial CPU/IO load.
- debugging-07: If the failure reproduces locally under load, the cause is timing rather than worker isolation.
- debugging-07: freezegun is a tool for freezing the clock.
- debugging-07: If freezing the clock and rerunning under load makes the flake vanish, the time-window cause is confirmed.
- debugging-07: Global or module-level state in the notification code that is not keyed per test or per worker can cause the failure.
- debugging-08: Two causes best explain the data: an unbounded or leaky allocation tied to request/webhook volume, and a cache bounded by count or logical size but not by actual bytes.
- debugging-08: The most plausible cause is that the cache's bound measures the wrong thing.
- debugging-08: A "size-bounded" cache is usually bounded by entry count rather than memory bytes.
- debugging-08: Campaigns push larger or more variant-heavy products.
- debugging-08: The cache-bound-measures-the-wrong-thing explanation fits all four observations.
- debugging-08: Baseline growth is explained by normal churn evicting by count while retaining larger objects.
- debugging-08: Overnight survival is explained by evicted-but-still-referenced entries, or by the cache holding more bytes at a steady entry count.
- debugging-08: Slower-but-nonzero growth on the canary is explained by background refresh or scheduled jobs populating the cache without webhook traffic.
- debugging-08: The baseline leak likely comes from scheduled jobs, connection pools, timers, or metrics/logging buffers that accumulate regardless of traffic.
- debugging-08: A possible webhook-driven leak mechanism is a listener registered per webhook and never removed.
- debugging-08: Because the canary has no webhook traffic, diffing two heap dumps taken a day apart on it isolates the non-webhook leak.
- debugging-08: Memory surviving quiet nights rules out anything that is merely slow to release under GC pressure.
- debugging-08: The overnight survival points at retained references such as caches, registered listeners, or growing collections, rather than GC tuning or fragmentation.
- debugging-08: If a forced full GC during a quiet period does not reduce memory usage, the memory is live and referenced, confirming a retention leak rather than a collection issue.
- explanation-01: Most language standard libraries use chaining.
- explanation-01: High-performance C++ hash maps use open addressing.
- explanation-02: A bank transfer can use SELECT ... FOR UPDATE on both accounts before debiting and crediting.
- explanation-02: With SELECT ... FOR UPDATE, any concurrent transfer touching the same accounts blocks until the first transfer commits.
- explanation-02: An e-commerce admin panel can load a product row with version = 5, edit the price, then update WHERE id = ? AND version = 5.
- explanation-02: On an optimistic locking conflict, the app can tell the user to reload and retry.
- explanation-03: The sender sends an amount of data equal to the congestion window and waits for acknowledgments.
- explanation-03: When packet loss occurs, TCP backs off and switches to congestion avoidance.
- explanation-03: Slow start exists because networks are shared and their capacity is unknown in advance.
- explanation-03: Many connections starting at once without slow start could overwhelm routers.
- explanation-03: Overwhelmed routers would cause cascading packet loss and collapse throughput for everyone.
- explanation-04: A runaway thread can hang the whole address space.
- explanation-04: Flaky plugins and request handlers processing untrusted input are examples of work that might crash or hang.
- explanation-04: Older versions of Ruby have a global interpreter lock.
- explanation-04: The cost of copying data between isolated processes would dominate for high-frequency, low-latency communication.
- explanation-05: Event buses, DOM nodes, and global singletons are examples of long-lived objects.
- explanation-07: Growth rate can be forecast from current trends such as rows per month and GB per month.
- explanation-07: Sharding decisions should be revisited at concrete checkpoints such as reaching 500 GB or hitting a write throughput ceiling, rather than on a calendar schedule.
- explanation-07: Vertical scaling, read replicas, partitioning, and archiving solve most database scaling constraints without sharding.
- explanation-07: Sharding early locks in a shard key before access patterns are understood.
- explanation-07: Choosing the wrong shard key forces a resharding migration later.
- explanation-07: A resharding migration is far more painful than migrating a single instance.
- explanation-07: Waiting too long to shard can let a single write-heavy table saturate I/O or hit a single-writer bottleneck before sharding infrastructure exists.
- explanation-07: Vacuum and index maintenance windows can grow long enough to threaten availability.
- explanation-07: PgBouncer is a connection pooling tool.
- explanation-08: Switching to a binary format should be expected to produce a modest performance win rather than a transformative one.
- explanation-08: Without measurements, the size of the performance gain cannot be estimated before trying it.
- explanation-08: Binary formats typically reduce serialization and deserialization time by 2-10x compared to JSON.
- explanation-08: Binary formats typically reduce payload size by 20-50% compared to JSON.
- explanation-08: If serialization is 5% of request time, a 5x speedup in serialization saves about 4% of overall request time.
- explanation-08: Binary formats add real costs including schema management, tooling, debuggability, and cross-language friction.
- summarization-01: The app now launches roughly 40% faster.
- summarization-01: Each button's tooltip displays that action's keyboard shortcut.
- summarization-02: The outage ran from 09:14 to 09:48 UTC.
- summarization-04: The issue is not browser-specific.
- summarization-04: Only PDF export fails.
- summarization-06: The deploy is not the sole cause of the incident.
- summarization-06: Confirming the root cause is pending better instrumentation.
- summarization-07: Everything other than the median latency result is a guess.
- summarization-08: The finding that the progress bar drives abandonment on large files is tentative.
- summarization-08: Some customers already had templates.
- summarization-08: A fourth interview round aimed at template gallery discoverability is recommended.

### classic-concise

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 27 | 25 | 0.926 | 19 | 2 |
| code-review-02 | 21 | 15 | 0.714 | 17 | 5 |
| code-review-03 | 15 | 13 | 0.867 | 19 | 2 |
| code-review-04 | 25 | 21 | 0.84 | 17 | 3 |
| code-review-05 | 37 | 28 | 0.757 | 36 | 8 |
| code-review-06 | 26 | 16 | 0.615 | 26 | 5 |
| code-review-07 | 39 | 35 | 0.897 | 34 | 8 |
| code-review-08 | 37 | 28 | 0.757 | 31 | 3 |
| debugging-01 | 6 | 6 | 1.0 | 6 | 1 |
| debugging-02 | 16 | 14 | 0.875 | 12 | 1 |
| debugging-03 | 9 | 9 | 1.0 | 10 | 0 |
| debugging-04 | 16 | 11 | 0.688 | 9 | 1 |
| debugging-05 | 20 | 17 | 0.85 | 11 | 0 |
| debugging-06 | 6 | 1 | 0.167 | 29 | 29 |
| debugging-07 | 35 | 17 | 0.486 | 35 | 15 |
| debugging-08 | 36 | 17 | 0.472 | 30 | 15 |
| explanation-01 | 33 | 29 | 0.879 | 25 | 3 |
| explanation-02 | 28 | 25 | 0.893 | 24 | 4 |
| explanation-03 | 31 | 25 | 0.806 | 31 | 5 |
| explanation-04 | 45 | 33 | 0.733 | 21 | 2 |
| explanation-05 | 21 | 16 | 0.762 | 12 | 0 |
| explanation-06 | 15 | 15 | 1.0 | 19 | 1 |
| explanation-07 | 28 | 16 | 0.571 | 27 | 3 |
| explanation-08 | 11 | 9 | 0.818 | 9 | 4 |
| summarization-01 | 10 | 4 | 0.4 | 6 | 1 |
| summarization-02 | 15 | 11 | 0.733 | 12 | 3 |
| summarization-03 | 14 | 14 | 1.0 | 13 | 0 |
| summarization-04 | 13 | 11 | 0.846 | 9 | 0 |
| summarization-05 | 12 | 11 | 0.917 | 8 | 0 |
| summarization-06 | 13 | 13 | 1.0 | 12 | 0 |
| summarization-07 | 16 | 14 | 0.875 | 14 | 1 |
| summarization-08 | 26 | 24 | 0.923 | 24 | 0 |

Median fraction: 0.843 over 32 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python gotcha.
- code-review-01: The proposed version lets real exceptions propagate instead of hiding them.
- code-review-02: Unchecked bad responses get parsed as if they were valid data.
- code-review-02: Parsing bad responses as valid data can produce more confusing downstream errors.
- code-review-02: The code unnecessarily mixes `async`/`await` with `.then()` chains.
- code-review-02: The code does not validate `data.name`.
- code-review-02: If the API response does not include a `name` field, `.toUpperCase()` will throw, even when the fetch succeeds.
- code-review-02: The fixed version throws an `Error` with message `Failed to load profile: ${res.status}` when `res.ok` is false.
- code-review-03: The parameterization fix also sidesteps quoting bugs.
- code-review-03: In the current code, a name containing an apostrophe would break the query.
- code-review-04: Safety of the direct attribute read is not guaranteed by the Python language.
- code-review-04: The fixed `Counter.__init__` creates `self._lock = threading.Lock()` and sets `self.value = 0`.
- code-review-04: The fixed `increment` executes `self.value += 1` inside a `with self._lock:` block.
- code-review-04: The fixed `reset` executes `self.value = 0` inside a `with self._lock:` block.
- code-review-05: The missing `cd` success check is the most dangerous bug in the script.
- code-review-05: The variables `$1`, `$BACKUP_DIR`, and `$f` are unquoted in the script.
- code-review-05: The unquoted variables should be written as `"$1"`, `"$BACKUP_DIR"`, and `"$f"`.
- code-review-05: The script contains the line `echo Cleaned $BACKUP_DIR`, which is unquoted.
- code-review-05: The `echo Cleaned $BACKUP_DIR` message is misleading if `cd` never actually happened.
- code-review-05: `set -u` would have caught the missing-argument problem immediately.
- code-review-05: The script does not restore the original working directory when it finishes.
- code-review-05: Failing to restore the original working directory matters if the script is sourced or chained with other commands.
- code-review-05: The suggested fix checks `[ -z "$BACKUP_DIR" ] || [ ! -d "$BACKUP_DIR" ]` and prints a usage message to stderr before exiting with status 1.
- code-review-06: A dict value in `override` under a key not already in `merged` is aliased directly instead of being merged or copied.
- code-review-06: The aliasing behavior for new nested dicts is asymmetric with the recurse-into-dicts path.
- code-review-06: Using `is None` instead of a falsiness check means `0`, `False`, and `""` are treated as real values.
- code-review-06: `merged.pop(key, None)` swallows the KeyError, so deleting a non-existent key is a silent no-op.
- code-review-06: A typo'd key in an override config intended to delete something fails silently instead of raising.
- code-review-06: If `base` is not dict-like, `dict(base)` may raise unhelpful errors.
- code-review-06: `isinstance(merged[key], dict)` does not match dict-like types that do not subclass `dict`, such as a custom Mapping.
- code-review-06: Dict-like values that are not `dict` subclasses get overwritten instead of merged, inconsistently with regular dicts.
- code-review-06: The function has no recursion guard, so self-referential structures would cause infinite recursion.
- code-review-06: Self-referential structures are unlikely in typical settings data.
- code-review-07: The asymmetry between 429 and 5xx backoff is more likely an oversight than a considered choice.
- code-review-07: Treating all other errors as non-retryable is likely deliberate.
- code-review-07: Whether existing callers rely on null as a sentinel should be determined before changing the helper.
- code-review-07: The null sentinel behavior is the part most likely to break silently if 'fixed'.
- code-review-08: The script contains no `if __name__ == "__main__":` block.
- code-review-08: The function `clean()` is never called anywhere in the script.
- code-review-08: If the scheduler runs the script via `python script.py`, the script does nothing.
- code-review-08: Whether another module imports the script and calls `clean()` is not visible in the code shown.
- code-review-08: The script's own tmp-file deletion branch can race with a concurrent run of the same script.
- code-review-08: A broken or dangling symlink in `ROOT` causes `getmtime` to raise `FileNotFoundError`.
- code-review-08: Treating `tmp-`/`.part` files as always safe to delete immediately, with no age check and no cap, may be an intentional design assumption that they are orphaned artifacts of failed runs.
- code-review-08: The script's current behavior falls into one of three cases: inert, silently corrupting data, or working as intended.
- code-review-08: Determining how `clean()` is invoked and whether anything creates `tmp-*`/`*.part` files as working files decides which of those three cases applies.
- debugging-02: Class bodies execute in strict mode.
- debugging-02: `this.seconds += 1` where `this` is `undefined` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-04: The actual encoding is usually UTF-8.
- debugging-04: Opening a file in binary mode with "rb" avoids decoding text.
- debugging-04: Binary mode can be used when only a line count is needed.
- debugging-04: Iterating a file object in binary mode splits on \n bytes.
- debugging-04: The binary-mode approach sidesteps encoding issues entirely.
- debugging-05: A function's default value is stored on the function object itself.
- debugging-05: The failure looks flaky but is deterministic given the call order.
- debugging-05: The fix is to never use a mutable object as a default argument.
- debugging-06: The speaker will check whether the directory contains relevant code before answering.
- debugging-06: The Bash tool was invoked.
- debugging-06: The command issued was `ls -la`.
- debugging-06: The command's stated purpose was to list files in the working directory.
- debugging-06: The working directory should be checked for relevant code before the question is answered.
- debugging-07: The parallelism is almost certainly relevant to the failure rather than incidental.
- debugging-07: If the digest query is scoped by a time window rather than a unique test/user/session ID, a concurrently running test in another worker can insert or delete rows that the test sees.
- debugging-07: Cross-test data leakage from shared state is the single most common cause of this exact symptom.
- debugging-07: Load from 3 other workers increases latency variance enough to expose a race that does not manifest without resource contention.
- debugging-07: Test isolation implemented via truncation or transaction rollback racing across workers is a plausible cause.
- debugging-07: If cleanup uses TRUNCATE, shared sequence resets, or a global counter instead of per-worker or per-test transactions, one worker's teardown can wipe or renumber rows another worker just wrote.
- debugging-07: An autoincrement ID or pagination boundary issue is a plausible cause.
- debugging-07: If the digest endpoint has an implicit LIMIT and orders by an insufficiently unique ID or timestamp, concurrent inserts from other workers can push one of the test's events outside the page or limit boundary.
- debugging-07: Connection pool or DB isolation level behavior is a plausible cause.
- debugging-07: READ COMMITTED with async replication, or a connection pool reusing a stale snapshot, can cause a worker to read a stale view missing the third insert.
- debugging-07: The cheapest first diagnostic step is to reproduce locally under contention by running the whole suite with `pytest -n 4` repeatedly.
- debugging-07: pytest-repeat provides a `--count` option, e.g. `--count=50`.
- debugging-07: Reproducing locally allows debugging with full tooling.
- debugging-07: If the seeding path is asynchronous, one should check whether the test waits on a task-completion signal or assumes synchronous completion.
- debugging-07: If adding a short explicit wait or poll-until-visible makes the failure disappear under parallel runs, the eventual consistency race is confirmed.
- debugging-07: pytest-django's `--reuse-db` can interact badly with `-n`.
- debugging-07: The recommended first move is reproducing under `-n 4` locally, because it turns an unreproducible CI-only flake into something iterable.
- debugging-07: The recommended second move is bisecting isolation problems versus an internal race.
- debugging-08: The observed pattern consists of steady percentage growth, no overnight recovery, presence without webhooks but faster growth with them, and a cache that has not changed.
- debugging-08: The pattern points toward something unbounded that is driven by order volume.
- debugging-08: An unbounded per-order or per-webhook tracking structure is the explanation most consistent with all four observations.
- debugging-08: Examples of such tracking structures include idempotency keys, dedup sets, in-flight/retry state, and in-memory audit logs.
- debugging-08: An unbounded per-order tracking structure grows with every order, which explains growth on the canary.
- debugging-08: Such a structure grows faster with higher webhook volume because of extra entries per event.
- debugging-08: Such a structure never shrinks overnight because nothing evicts it.
- debugging-08: Such a structure scales with traffic during campaigns.
- debugging-08: One check is to grep for maps or sets keyed by order ID, webhook ID, or idempotency key that lack a TTL or an explicit .remove() call.
- debugging-08: An unbounded tracking structure shows unbounded object count growth over time even when the request rate is flat.
- debugging-08: High-cardinality metrics or logging labels, such as per-order-id, per-webhook-id, or per-campaign-id tags, are a possible cause.
- debugging-08: Metrics clients often retain one time series per unique label combination forever.
- debugging-08: High-cardinality labels match the campaign correlation because campaigns produce more unique IDs and campaign tags.
- debugging-08: High-cardinality labels match canary growth because the canary still emits per-order metrics.
- debugging-08: One check is to query the metrics backend for active series or cardinality count over the same window as the memory graph.
- debugging-08: If metric cardinality climbs monotonically alongside RSS, high-cardinality labels are the cause.
- debugging-08: One check is to pick evicted product IDs in a heap dump and trace their GC roots to see if anything outside the cache still retains them.
- debugging-08: No profile has been taken yet.
- debugging-08: Diffing object counts by type will immediately reveal which of the first four causes is real.
- explanation-01: An example of computing an index is hash("apple") % array_size.
- explanation-01: A hash map array has only one slot per index, so a strategy is needed to store both colliding entries.
- explanation-01: Lookup under open addressing hashes to the slot, then follows the same probing sequence until the key is found or an empty slot is hit.
- explanation-01: Rust's HashMap uses an open addressing variant.
- explanation-02: A CMS article edit is an example workload suited to optimistic locking.
- explanation-02: A shopping cart is an example workload suited to optimistic locking.
- explanation-02: Postgres and MySQL support pessimistic locking via SELECT ... FOR UPDATE.
- explanation-03: If a sender sends data as fast as the receiver's advertised window allows, it can overwhelm a router queue.
- explanation-03: Slow start is also used after certain recovery events.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The sender's actual sending rate is limited by the smaller of the congestion window and the receiver's advertised window.
- explanation-03: RFC 6928 raised the initial congestion window value to improve performance for short flows.
- explanation-03: The name 'slow start' refers to starting from a small window rather than assuming the full receiver-advertised window can be used immediately.
- explanation-04: All threads in a process share the same resources.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own instruction pointer.
- explanation-04: nginx uses multiple processes.
- explanation-04: Chrome uses a per-tab process model.
- explanation-04: Each process gets its own interpreter and GIL.
- explanation-04: For I/O-bound work, threads or async are fine.
- explanation-04: Threads release the GIL while waiting on I/O.
- explanation-04: Processes can run under different privilege levels.
- explanation-04: OS-level tools for managing processes include kill, restart, and resource limits via cgroups.
- explanation-04: Using separate processes avoids coordinating shutdown logic inside one program.
- explanation-04: Threads have faster context switches than processes.
- explanation-05: A garbage collector walks references starting from roots.
- explanation-05: Roots include global variables, stack frames, and active closures.
- explanation-05: A garbage collector cannot know the programmer's intent.
- explanation-05: Eviction mechanisms include TTL, LRU, and a size cap.
- explanation-05: Closures capturing large outer scopes longer than needed is a frequent cause of memory leaks.
- explanation-07: Sharding only helps when the constraint is write throughput, storage, or single-node CPU/IO that vertical scaling cannot fix.
- explanation-07: If the bottleneck is bad queries, missing indexes, or lock contention, sharding will not fix it.
- explanation-07: Sharding replicates query, index, and lock-contention problems across all nodes.
- explanation-07: Current CPU, IO, and connection utilization determine how much headroom remains on existing hardware.
- explanation-07: At 20% utilization on a mid-size instance, there is likely 5-10x runway before sharding is urgent.
- explanation-07: Building routing and rebalancing infrastructure can take months.
- explanation-07: Waiting too long to shard risks an emergency migration under load with less room to test and roll back safely.
- explanation-07: Waiting too long is usually still cheaper than premature sharding.
- explanation-07: Read replicas, table partitioning, connection pooling, and vertical scaling can mitigate the interim before sharding.
- explanation-07: Read replicas, partitioning, connection pooling, and vertical scaling are reversible, incremental steps.
- explanation-07: Postgres native partitioning by date or tenant addresses table size and vacuum/index bloat concerns.
- explanation-07: Sharding should be revisited only when utilization numbers show vertical scaling, partitioning, and read replicas will not suffice for the next 12-18 months.
- explanation-08: Network, database, and business logic usually dominate request time.
- explanation-08: The migration cost includes client compatibility, debuggability, and tooling.
- summarization-01: The app now starts up to 40% faster.
- summarization-01: Hovering over any toolbar button displays that button's keyboard shortcut.
- summarization-01: Internal build tooling changes were omitted from these release notes.
- summarization-01: Module refactoring changes were omitted from these release notes.
- summarization-01: Telemetry batching changes were omitted from these release notes.
- summarization-01: The omitted changes have no user-facing effect.
- summarization-02: The small pool size of 5 was intentional for staging.
- summarization-02: The reduced pool size exhausted database connections under load.
- summarization-02: The incident caused an approximately 12% error rate for checkout.
- summarization-02: The change was rolled back at 09:48.
- summarization-04: A report named "March" can be selected on the Reports page.
- summarization-04: The bug was reproduced on two different machines.
- summarization-05: Ada is assigned to check with the mobile team's lead about whether the mobile team was informed of the API deprecation.
- summarization-07: A staging comparison was run between a new request batcher and the current request batcher.
- summarization-07: Memory impact, production tail latency, and the crash's cause all need further investigation before rollout.
- summarization-08: No action is recommended yet on the template gallery.
- summarization-08: Template gallery usage data is worth tracking at scale.

Added facts (styled only):

- code-review-01: The code should catch a specific exception, such as the database's exception type, and log it.
- code-review-01: The fix catches `DBError` and logs the error with `logger.error` before returning `False`.
- code-review-02: The code has four problems.
- code-review-02: Most of the four problems are fatal.
- code-review-02: A `try/catch` should be added to handle errors.
- code-review-02: Marking a function `async` wraps its return value in a promise.
- code-review-02: The thrown error message includes the user ID and `res.status`.
- code-review-03: The code has no error handling.
- code-review-03: A database error propagates raw to the caller with no added context.
- code-review-04: The class is documented as safe for concurrent use.
- code-review-04: The proposed fix stores the count in a private attribute `_value` and creates a `threading.Lock` in `__init__`.
- code-review-04: In the proposed fix, `value` is a property that acquires the lock before returning `_value`.
- code-review-05: The `nullglob` option prevents unmatched globs from being passed literally.
- code-review-05: POSIX `sh` does not have `nullglob`.
- code-review-05: When no `*.log` files exist, the loop body still runs once with the literal string `*.log`.
- code-review-05: When no `*.log` files exist, `gzip` fails with a "no such file" error.
- code-review-05: `set -euo pipefail` is the bash equivalent option set.
- code-review-05: The script relies on `$()`, which is POSIX-compliant.
- code-review-05: Because the script is plain POSIX sh, bashisms should not be used elsewhere in it.
- code-review-05: The suggested fix uses `BACKUP_DIR=${1:?usage: $0 <backup_dir>}` to enforce the argument.
- code-review-06: If `base` is not dict-like, `dict(base)` may still succeed on unexpected input such as a list of 2-tuples.
- code-review-06: `dict(base)` on a list of 2-tuples produces a dict silently instead of failing loudly.
- code-review-06: Replacing non-dict values outright is a reasonable default for settings merging.
- code-review-06: Using `dict(base)` instead of `deepcopy` is likely a performance choice.
- code-review-06: Both recommended fixes are one-line changes.
- code-review-07: Passing `attempts = 0` calls `fn` zero times.
- code-review-07: Passing `attempts = 0` returns `undefined` immediately.
- code-review-07: Fail-soft patterns are sometimes used in UI code that wants a fallback value.
- code-review-07: Three different failure modes (`null`, `undefined`, thrown) collapse into two ambiguous sentinels.
- code-review-07: The retry logic has no delay cap.
- code-review-07: The lack of jitter and delay cap is acceptable at `attempts=3`.
- code-review-07: Increasing `attempts` creates a thundering-herd risk.
- code-review-07: Without logging, the only visible symptom is a `null` value downstream.
- code-review-08: The temp-file deletion behavior is almost certainly not intended as written.
- code-review-08: The age check on the second branch suggests temp files were meant to be swept only once stale, not on sight.
- code-review-08: The non-recursive behavior is undocumented.
- debugging-01: Line 4 looks up the key `cfg['Port']`.
- debugging-02: Because `this` is not the `Timer` instance, `this.seconds` is `undefined`.
- debugging-04: `chardet` is a library that can detect a file's actual encoding.
- debugging-06: The export job and the analytics service compete for a shared, fixed-size connection pool.
- debugging-06: Something occasionally holds connections longer than usual.
- debugging-06: A slow analytics query can cause connections to be held longer than usual.
- debugging-06: A lock wait can cause connections to be held longer than usual.
- debugging-06: A leaked connection that isn't returned to the pool can cause connections to be held longer than usual.
- debugging-06: The batch number at which the failure occurs varies.
- debugging-06: A varying batch number points away from bad data as the cause.
- debugging-06: A varying batch number points toward timing or contention as the cause.
- debugging-06: A data-triggered bug would tend to cluster on the same batch.
- debugging-06: One hypothesis is contention with analytics, in which analytics runs a heavy query or its own batch job around the same time and saturates the shared pool.
- debugging-06: One hypothesis is a connection leak, in which a code path such as an error branch or an exception in a `finally` fails to release a connection.
- debugging-06: A connection leak causes the pool to slowly drain until a random request stalls.
- debugging-06: One hypothesis is that the pool's max size is too small for the peak concurrent load from both services combined.
- debugging-06: One hypothesis is DB-side slowness, in which a lock, autovacuum, or slow query on the database makes connections take longer to free up.
- debugging-06: DB-side slowness is a cause distinct from the pool configuration itself.
- debugging-06: Pool stats can be logged on every failure, capturing active, idle, and waiting counts at the moment of the timeout.
- debugging-06: Currently only the symptom is visible in logs, not the pool state.
- debugging-06: Analytics' own logs or `pg_stat_activity` (or an equivalent) can be pulled for 02:14 on the night of the failure.
- debugging-06: The failure occurred at 02:14.
- debugging-06: Long-running or blocked queries can be checked for in the analytics activity data.
- debugging-06: Pool utilization can be graphed over the full night rather than just the failure window.
- debugging-06: A connection leak shows as a rising baseline in pool utilization.
- debugging-06: Contention shows as a spike in pool utilization.
- debugging-06: DB-side connection totals can be checked to confirm that the sum of pool sizes across services is less than or equal to `max_connections`.
- debugging-06: Lock waits can be looked for in the database logs.
- debugging-06: A canary log line can be added on connection checkout and checkin with duration.
- debugging-06: A canary log line with duration would give the next failure enough context instead of another orphaned fragment.
- debugging-06: Pool-stats logging is the cheapest of these diagnostics to add.
- debugging-06: Pool-stats logging would reveal in a single occurrence whether the problem is contention or a leak.
- debugging-07: One event loses the race roughly 10% of the time.
- debugging-07: A shared in-memory store, cache, or singleton that is not reset between tests leaks state across workers.
- debugging-07: Time-based flakiness is a likely cause.
- debugging-07: If the digest filters by a time window, a slow CI worker could push one event's timestamp just outside the window.
- debugging-07: The failing test is named `test_digest_contains_all_events`.
- debugging-07: Running only `test_digest_contains_all_events` many times with 4 workers alongside the rest of the suite tests parallelism in isolation.
- debugging-07: Running the same test 4-at-a-time by duplicating it is a separate isolation experiment.
- debugging-07: Diagnostics should log seeded event IDs, digest query timestamp bounds, and returned event IDs on failure.
- debugging-07: Diagnostic output should be captured to a file CI retains or printed to stdout.
- debugging-07: Shared state under 4-way parallelism is the classic 10%-flake pattern.
- debugging-07: Running CI with `-n 1` for a week or a large repeated batch bisects the problem by disabling workers.
- debugging-07: If the failure disappears under `-n 1`, that confirms concurrency as the root cause and rules out pure timing or CI-hardware flakiness.
- debugging-07: Step 3 (diagnostics) and step 5 (shared-state check) should be started first, in parallel.
- debugging-07: The diagnostics and shared-state checks are cheap.
- debugging-07: The diagnostics and shared-state checks will most likely reveal whether the problem is a race in the app or a test-isolation bug in the suite.
- debugging-08: Memory growth comes from two layered sources: a baseline leak and a traffic-driven leak.
- debugging-08: The idle canary instance proves a baseline leak exists independent of webhook traffic.
- debugging-08: The campaign correlation proves a second, traffic-driven leak sits on top of the baseline leak.
- debugging-08: The baseline leak is a slow, traffic-independent accumulation.
- debugging-08: Likely causes of the baseline leak include scheduled jobs, connection/thread pools, metrics/logging buffers, and listener/callback registries that never shrink.
- debugging-08: Heap histograms can be captured with jmap -histo or a language equivalent.
- debugging-08: If memory usage does not drop after forcing a full GC, the memory is held by retained references rather than uncollected garbage.
- debugging-08: Possible causes of the traffic-driven leak include per-webhook objects not released, unbounded async queues, and listeners registered per request and never removed.
- debugging-08: Replaying synthetic webhook load against the canary tests whether its growth rate rises to match production.
- debugging-08: If synthetic webhook load raises the canary's growth rate to production levels, the leak is in webhook handling rather than the cache.
- debugging-08: Eviction events can be logged to confirm eviction actually fires as expected.
- debugging-08: An eviction policy can evict by weight rather than only by count.
- debugging-08: The fragmentation/RSS explanation would not explain the campaign correlation well.
- debugging-08: A heap histogram diff is cheap and requires no code change.
- debugging-08: Cache bounded by count rather than bytes is the most likely explanation for the campaign-correlated growth, given that the bound hasn't changed but the content has.
- explanation-01: Load factor is the number of entries divided by the number of buckets.
- explanation-01: Most general-purpose hash maps use chaining.
- explanation-01: Performance-critical hash maps use open addressing.
- explanation-02: In the example, a row is read with `version = 5`, edited, then updated with `WHERE id = ? AND version = 5`.
- explanation-02: Web apps, APIs, and collaborative editing where most edits touch different records are examples of workloads suited to optimistic locking.
- explanation-02: Pessimistic locking is simpler to reason about.
- explanation-02: Pessimistic locking risks blocking, deadlocks, and lower throughput under load.
- explanation-03: Excessive retransmission can cascade into congestion collapse.
- explanation-03: Congestion collapse is a state where the network does more retransmitting than useful work.
- explanation-03: Every segment sent in a round trip generates an ACK.
- explanation-03: An example progression of cwnd doubling is 10, 20, 40, 80.
- explanation-03: On packet loss, TCP cuts its sending rate and transitions to congestion avoidance.
- explanation-04: Threads must guard against race conditions using locks.
- explanation-04: Ruby serializes thread execution for CPU-bound work.
- explanation-06: Possible sources of slowness include slow queries, missing indexes, N+1 calls, network latency, slow serialization, and causes outside the database.
- explanation-07: A single primary can bottleneck on writes long before disk capacity fills.
- explanation-07: Guessing the wrong shard key forces a costly re-shard later.
- explanation-07: Defining the trigger metric in advance mitigates the risk of a panicked decision.
- explanation-08: Serialization typically costs 1–10% of request time in JSON-heavy services.
- explanation-08: A codec that is 10x faster often yields a barely-noticeable end-to-end gain.
- explanation-08: If serialization accounts for under 5% of request time, a binary format is not worth the migration cost.
- explanation-08: Migrating to a binary format incurs costs in schema management, debugging opacity, and client compatibility.
- summarization-01: Cold start time has been reduced by about 40%.
- summarization-02: The config review process did not check other environment-specific values.
- summarization-02: Errors began at 09:14.
- summarization-02: There was a 7-minute gap between the start of errors and the page firing.
- summarization-07: All findings other than the median latency result are guesses.

### developer-docs

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 27 | 25 | 0.926 | 23 | 1 |
| code-review-02 | 21 | 19 | 0.905 | 20 | 2 |
| code-review-03 | 15 | 0 | 0.0 | 5 | 5 |
| code-review-04 | 25 | 19 | 0.76 | 22 | 3 |
| code-review-05 | 37 | 27 | 0.73 | 31 | 4 |
| code-review-06 | 26 | 15 | 0.577 | 31 | 8 |
| code-review-07 | 39 | 33 | 0.846 | 50 | 20 |
| code-review-08 | 37 | 20 | 0.541 | 29 | 2 |
| debugging-01 | 6 | 6 | 1.0 | 11 | 5 |
| debugging-02 | 16 | 11 | 0.688 | 10 | 2 |
| debugging-03 | 9 | 9 | 1.0 | 11 | 0 |
| debugging-04 | 16 | 12 | 0.75 | 12 | 3 |
| debugging-05 | 20 | 15 | 0.75 | 15 | 0 |
| debugging-06 | 6 | 1 | 0.167 | 35 | 35 |
| debugging-07 | 35 | 22 | 0.629 | 34 | 8 |
| debugging-08 | 36 | 20 | 0.556 | 33 | 15 |
| explanation-01 | 33 | 24 | 0.727 | 31 | 2 |
| explanation-02 | 28 | 24 | 0.857 | 30 | 3 |
| explanation-03 | 31 | 20 | 0.645 | 27 | 0 |
| explanation-04 | 45 | 37 | 0.822 | 30 | 0 |
| explanation-05 | 21 | 17 | 0.81 | 15 | 0 |
| explanation-06 | 15 | 11 | 0.733 | 25 | 6 |
| explanation-07 | 28 | 13 | 0.464 | 19 | 5 |
| explanation-08 | 11 | 7 | 0.636 | 22 | 16 |
| summarization-01 | 10 | 4 | 0.4 | 6 | 2 |
| summarization-02 | 15 | 11 | 0.733 | 15 | 3 |
| summarization-03 | 14 | 14 | 1.0 | 13 | 1 |
| summarization-04 | 13 | 13 | 1.0 | 10 | 1 |
| summarization-05 | 12 | 12 | 1.0 | 10 | 0 |
| summarization-06 | 13 | 12 | 0.923 | 12 | 0 |
| summarization-07 | 16 | 16 | 1.0 | 16 | 2 |
| summarization-08 | 26 | 25 | 0.962 | 22 | 0 |

Median fraction: 0.75 over 32 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python gotcha.
- code-review-01: The code should at minimum catch a specific exception type and probably log it.
- code-review-02: The code unnecessarily mixes `async`/`await` with `.then()` chains.
- code-review-02: The fixed version awaits `res.json()` to obtain `profile` and returns `profile.name.toUpperCase()`.
- code-review-03: The code has a SQL injection vulnerability, which is its critical issue.
- code-review-03: The `customer_name` value is concatenated directly into the query string.
- code-review-03: The `status` value is concatenated directly into the query string.
- code-review-03: An attacker can pass a value like `' OR '1'='1` to alter the query logic.
- code-review-03: An attacker can pass a value like `'; DROP TABLE orders; --` to run arbitrary SQL.
- code-review-03: Parameterized queries fix the SQL injection issue.
- code-review-03: A parameterized version passes the query with `%s` placeholders and a tuple of values to `cursor.execute`.
- code-review-03: The `?` placeholder should be used instead of `%s` when using sqlite3.
- code-review-03: Using `SELECT *` is fragile if the table schema changes.
- code-review-03: It is better to name only the columns the caller needs instead of using `SELECT *`.
- code-review-03: The code performs no input validation.
- code-review-03: Nothing stops `status` from being an unexpected or invalid value before it reaches the database.
- code-review-03: The parameterization fix alone resolves the injection risk.
- code-review-03: The parameterization fix also sidesteps quoting bugs.
- code-review-03: In the current code, a name containing an apostrophe would break the query.
- code-review-04: If a reset happens after the read but before the write in `increment`, the increment silently undoes the reset by writing `1`.
- code-review-04: In CPython, the GIL protects the single attribute read, making the unsafe direct read less severe.
- code-review-04: Safety of the direct attribute read is not guaranteed by the Python language.
- code-review-04: The fixed `Counter.__init__` creates `self._lock = threading.Lock()` and sets `self.value = 0`.
- code-review-04: The fixed `increment` executes `self.value += 1` inside a `with self._lock:` block.
- code-review-04: The fixed `reset` executes `self.value = 0` inside a `with self._lock:` block.
- code-review-05: The script does not check the exit codes of `gzip` or `rm`.
- code-review-05: The script contains the line `echo Cleaned $BACKUP_DIR`, which is unquoted.
- code-review-05: The `echo Cleaned $BACKUP_DIR` message is misleading if `cd` never actually happened.
- code-review-05: `set -u` would have caught the missing-argument problem immediately.
- code-review-05: The script does not restore the original working directory when it finishes.
- code-review-05: Failing to restore the original working directory matters if the script is sourced or chained with other commands.
- code-review-05: The suggested fix checks `[ -z "$BACKUP_DIR" ] || [ ! -d "$BACKUP_DIR" ]` and prints a usage message to stderr before exiting with status 1.
- code-review-05: The suggested fix uses `cd "$BACKUP_DIR" || exit 1`.
- code-review-05: The suggested fix uses `rm -f -- *.tmp`.
- code-review-05: The suggested fix calls `gzip -- "$f"`.
- code-review-06: Merging base={'a': {'x': 1}} with override={'a': 'oops'} raises AttributeError: 'str' object has no attribute 'items' inside the recursive call.
- code-review-06: The missing type check on the override value is a real crash bug for malformed or unexpected input.
- code-review-06: The aliasing behavior for new nested dicts is asymmetric with the recurse-into-dicts path.
- code-review-06: Using `None` as a deletion marker is a common config-merging convention known as a tombstone value.
- code-review-06: Using `is None` instead of a falsiness check means `0`, `False`, and `""` are treated as real values.
- code-review-06: If `base` is not dict-like, `dict(base)` may raise unhelpful errors.
- code-review-06: If `override` is not dict-like, the `.items()` call fails immediately.
- code-review-06: `dict(base)` always returns a plain `dict`, so a subclass type such as `OrderedDict` or a custom Mapping is lost.
- code-review-06: `isinstance(merged[key], dict)` does not match dict-like types that do not subclass `dict`, such as a custom Mapping.
- code-review-06: Dict-like values that are not `dict` subclasses get overwritten instead of merged, inconsistently with regular dicts.
- code-review-06: The intended behavior for `None`, for list merging, and for shallow aliasing cannot be inferred from the code alone.
- code-review-07: The helper has three distinct signals for failure: null, undefined, and a thrown error.
- code-review-07: There is no consistent contract across the three failure signals.
- code-review-07: 5xx retries have no backoff at all, unlike 429 retries.
- code-review-07: Only rate-limit errors are delayed; server errors are retried in a tight loop with no wait.
- code-review-07: The asymmetry between 429 and 5xx backoff is more likely an oversight than a considered choice.
- code-review-07: Treating all other errors as non-retryable is likely deliberate.
- code-review-08: The script contains no `if __name__ == "__main__":` block.
- code-review-08: The function `clean()` is never called anywhere in the script.
- code-review-08: If the scheduler runs the script via `python script.py`, the script does nothing.
- code-review-08: Whether another module imports the script and calls `clean()` is not visible in the code shown.
- code-review-08: If `ROOT` contains a subdirectory, the script dies partway through the loop.
- code-review-08: Because `os.listdir` ordering is unspecified, a crash mid-loop leaves an arbitrary subset of eligible files uncleaned for that run.
- code-review-08: A broken or dangling symlink in `ROOT` causes `getmtime` to raise `FileNotFoundError`.
- code-review-08: The 500 cap does not select the 500 oldest files.
- code-review-08: `os.listdir` returns entries in filesystem-dependent order, not sorted by mtime.
- code-review-08: When more than 500 files are eligible, which files survive is arbitrary rather than age-based.
- code-review-08: The script does not check that `ROOT` exists before calling `listdir`.
- code-review-08: The rationale for the `86400 * 45` and `500` constants is undocumented and nobody can recall it.
- code-review-08: `CUTOFF` is computed once at import time rather than on each call to `clean()`.
- code-review-08: If the process is short-lived and invoked fresh each schedule tick, computing `CUTOFF` at import time is harmless.
- code-review-08: In a long-running process that calls `clean()` repeatedly, `CUTOFF` never advances and the effective retention window grows beyond 45 days over time.
- code-review-08: The script's current behavior falls into one of three cases: inert, silently corrupting data, or working as intended.
- code-review-08: Determining how `clean()` is invoked and whether anything creates `tmp-*`/`*.part` files as working files decides which of those three cases applies.
- debugging-02: A regular function's `this` binding is determined by how the function is called, not by the surrounding class.
- debugging-02: `setInterval` invokes its callback as a plain function call.
- debugging-02: Class bodies execute in strict mode.
- debugging-02: `this.seconds += 1` where `this` is `undefined` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: In the non-strict case, `NaN` would be printed each tick.
- debugging-04: Opening a file in binary mode with "rb" avoids decoding text.
- debugging-04: Binary mode can be used when only a line count is needed.
- debugging-04: Iterating a file object in binary mode splits on \n bytes.
- debugging-04: The binary-mode approach sidesteps encoding issues entirely.
- debugging-05: A function's default value is stored on the function object itself.
- debugging-05: The failure looks flaky but is deterministic given the call order.
- debugging-05: The fix is to never use a mutable object as a default argument.
- debugging-05: The fix also protects callers who pass their own `tags` list from having it mutated as a side effect.
- debugging-05: Copying a caller-supplied `tags` list, e.g. `tags = list(tags) if tags is not None else list(DEFAULT_TAGS)`, avoids mutating the caller's list.
- debugging-06: The speaker will check whether the directory contains relevant code before answering.
- debugging-06: The Bash tool was invoked.
- debugging-06: The command issued was `ls -la`.
- debugging-06: The command's stated purpose was to list files in the working directory.
- debugging-06: The working directory should be checked for relevant code before the question is answered.
- debugging-07: Serial runs never share concurrent state, so cross-test leakage only appears under parallelism.
- debugging-07: An autoincrement ID or pagination boundary issue is a plausible cause.
- debugging-07: If the digest endpoint has an implicit LIMIT and orders by an insufficiently unique ID or timestamp, concurrent inserts from other workers can push one of the test's events outside the page or limit boundary.
- debugging-07: Connection pool or DB isolation level behavior is a plausible cause.
- debugging-07: READ COMMITTED with async replication, or a connection pool reusing a stale snapshot, can cause a worker to read a stale view missing the third insert.
- debugging-07: The cheapest first diagnostic step is to reproduce locally under contention by running the whole suite with `pytest -n 4` repeatedly.
- debugging-07: pytest-repeat provides a `--count` option, e.g. `--count=50`.
- debugging-07: If the failure reproduces locally under parallelism, that confirms it is parallelism-driven rather than CI-infrastructure-specific.
- debugging-07: Reproducing locally allows debugging with full tooling.
- debugging-07: The second step is to run only this test file or test repeatedly under `-n 4` to distinguish cross-test pollution from an internal race.
- debugging-07: pytest-django's `--reuse-db` can interact badly with `-n`.
- debugging-07: The recommended first move is reproducing under `-n 4` locally, because it turns an unreproducible CI-only flake into something iterable.
- debugging-07: The recommended second move is bisecting isolation problems versus an internal race.
- debugging-08: An unbounded per-order or per-webhook tracking structure is the explanation most consistent with all four observations.
- debugging-08: Examples of such tracking structures include idempotency keys, dedup sets, in-flight/retry state, and in-memory audit logs.
- debugging-08: An unbounded per-order tracking structure grows with every order, which explains growth on the canary.
- debugging-08: Such a structure grows faster with higher webhook volume because of extra entries per event.
- debugging-08: Such a structure never shrinks overnight because nothing evicts it.
- debugging-08: Such a structure scales with traffic during campaigns.
- debugging-08: One check is to grep for maps or sets keyed by order ID, webhook ID, or idempotency key that lack a TTL or an explicit .remove() call.
- debugging-08: Taking two heap dumps a few hours apart and diffing dominator sizes can confirm an unbounded tracking structure.
- debugging-08: An unbounded tracking structure shows unbounded object count growth over time even when the request rate is flat.
- debugging-08: High-cardinality labels match canary growth because the canary still emits per-order metrics.
- debugging-08: A cache eviction leak, where evicted entries are kept alive elsewhere, is a possible cause.
- debugging-08: A secondary index, listener, or closure can still reference an object after the cache evicts it.
- debugging-08: A steady cache bound caps only cache-visible memory, not total retained memory.
- debugging-08: One check is to pick evicted product IDs in a heap dump and trace their GC roots to see if anything outside the cache still retains them.
- debugging-08: Fragmentation requires a different fix than retained objects.
- debugging-08: The fastest confirmation method is taking a heap dump or allocation profile at start-of-week and again after a day or two of growth and diffing object counts by type.
- explanation-01: An example of computing an index is hash("apple") % array_size.
- explanation-01: A hash map array has only one slot per index, so a strategy is needed to store both colliding entries.
- explanation-01: Separate chaining is simple to implement.
- explanation-01: In the worst case, with many collisions in one slot, separate chaining degrades to O(n) list traversal.
- explanation-01: Quadratic probing tries index+1², then index+2², and so on.
- explanation-01: Double hashing uses a second hash function to compute the step size.
- explanation-01: Open addressing performance degrades sharply as the table fills up due to clustering.
- explanation-01: Open addressing requires resizing/rehashing earlier, typically once the load factor exceeds about 0.7.
- explanation-01: Chaining is easier to reason about and more forgiving if the load factor is not tuned carefully.
- explanation-02: An optimistic-locking stock update can be written as: UPDATE products SET stock = stock - 1, version = version + 1 WHERE id = 42 AND version = 7.
- explanation-02: Optimistic locking fits when throughput matters more than avoiding retries.
- explanation-02: A shopping cart is an example workload suited to optimistic locking.
- explanation-02: Postgres and MySQL support pessimistic locking via SELECT ... FOR UPDATE.
- explanation-03: If a sender sends data as fast as the receiver's advertised window allows, it can overwhelm a router queue.
- explanation-03: Slow start is also used after certain recovery events.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The sender's actual sending rate is limited by the smaller of the congestion window and the receiver's advertised window.
- explanation-03: The initial cwnd was historically 1 segment.
- explanation-03: The initial cwnd is now typically 2-10 segments.
- explanation-03: RFC 6928 raised the initial congestion window value to improve performance for short flows.
- explanation-03: When packet loss is detected, ssthresh is lowered and cwnd is reset or cut back.
- explanation-03: The name 'slow start' is slightly misleading because the growth is exponential and ramps up quickly.
- explanation-03: The name 'slow start' refers to starting from a small window rather than assuming the full receiver-advertised window can be used immediately.
- explanation-03: Slow start is slow relative to sending everything at once but fast relative to linear growth.
- explanation-04: A process has its own file descriptors.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own instruction pointer.
- explanation-04: nginx uses multiple processes.
- explanation-04: For I/O-bound work, threads or async are fine.
- explanation-04: Threads release the GIL while waiting on I/O.
- explanation-04: OS-level tools for managing processes include kill, restart, and resource limits via cgroups.
- explanation-04: Using separate processes avoids coordinating shutdown logic inside one program.
- explanation-05: A garbage-collected runtime automatically frees memory it detects as unused.
- explanation-05: A garbage collector walks references starting from roots.
- explanation-05: Roots include global variables, stack frames, and active closures.
- explanation-05: Eviction mechanisms include TTL, LRU, and a size cap.
- explanation-06: Possible alternative causes of the performance problem include slow queries, network latency, N+1 calls, and serialization.
- explanation-06: Staleness is a complexity introduced by adding a cache.
- explanation-06: A cache is another system that must be operated.
- explanation-06: Cache invalidation is a classic source of subtle bugs.
- explanation-07: Single Postgres instances can comfortably run into multi-TB territory with the right hardware and indexing.
- explanation-07: Sharding only helps when the constraint is write throughput, storage, or single-node CPU/IO that vertical scaling cannot fix.
- explanation-07: If the bottleneck is bad queries, missing indexes, or lock contention, sharding will not fix it.
- explanation-07: Sharding replicates query, index, and lock-contention problems across all nodes.
- explanation-07: Current CPU, IO, and connection utilization determine how much headroom remains on existing hardware.
- explanation-07: At 20% utilization on a mid-size instance, there is likely 5-10x runway before sharding is urgent.
- explanation-07: After sharding, every schema change, migration, and query must be shard-aware.
- explanation-07: Building routing and rebalancing infrastructure can take months.
- explanation-07: Waiting too long is usually still cheaper than premature sharding.
- explanation-07: Read replicas, table partitioning, connection pooling, and vertical scaling can mitigate the interim before sharding.
- explanation-07: Postgres native table partitioning operates within a single instance and is not the same as sharding.
- explanation-07: Read replicas, partitioning, connection pooling, and vertical scaling are reversible, incremental steps.
- explanation-07: Postgres native partitioning by date or tenant addresses table size and vacuum/index bloat concerns.
- explanation-07: Native partitioning provides much of the operational benefit of sharding without cross-node complexity.
- explanation-07: Sharding should be revisited only when utilization numbers show vertical scaling, partitioning, and read replicas will not suffice for the next 12-18 months.
- explanation-08: JSON parsing and serialization is often not the performance bottleneck.
- explanation-08: Network, database, and business logic usually dominate request time.
- explanation-08: Profiling results indicate whether the migration is worth its cost.
- explanation-08: The migration cost includes client compatibility, debuggability, and tooling.
- summarization-01: The app now starts up to 40% faster.
- summarization-01: Hovering over any toolbar button displays that button's keyboard shortcut.
- summarization-01: Internal build tooling changes were omitted from these release notes.
- summarization-01: Module refactoring changes were omitted from these release notes.
- summarization-01: Telemetry batching changes were omitted from these release notes.
- summarization-01: The omitted changes have no user-facing effect.
- summarization-02: The reduced pool size exhausted database connections under load.
- summarization-02: The incident caused an approximately 12% error rate for checkout.
- summarization-02: The incident was detected at 09:14.
- summarization-02: An on-call engineer was paged at 09:21.
- summarization-06: A restart restored the checkout service.
- summarization-08: Template gallery usage data is worth tracking at scale.

Added facts (styled only):

- code-review-01: The original code does not check that `roles` contains only valid role values before inserting into the database.
- code-review-02: The `async` keyword only wraps the return value in a promise.
- code-review-02: If the fetch or JSON parsing fails, the rejection is unhandled and surfaces as an unhandled promise rejection.
- code-review-03: The speaker will check memory for relevant prior guidance before reviewing.
- code-review-03: A PowerShell Get-Content command is invoked.
- code-review-03: The file read is at /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-weclp6d3/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-121asz23/memory/MEMORY.md
- code-review-03: The memory index file is named MEMORY.md.
- code-review-03: The Get-Content command uses -ErrorAction SilentlyContinue to suppress errors.
- code-review-04: The fix uses `threading.Lock` created in `__init__` and acquired with a `with` statement in `increment()`, `reset()`, and `get()`.
- code-review-04: In the fixed version, `get()` returns `self._value` while holding the lock.
- code-review-04: The leading underscore in `_value` signals that callers should not touch the attribute directly and should use `get()` instead.
- code-review-05: Adding `set -e` at the top fixes the unchecked `cd` failure.
- code-review-05: In some shells, the `ls` stderr error still gets captured as loop input.
- code-review-05: The unhandled-glob pattern is riskier in cases such as `rm -rf $DIR/*` rather than a suffix match.
- code-review-05: The absence of `set -e` is what makes the `cd` failure dangerous.
- code-review-06: Two of the function's behaviors are risky.
- code-review-06: Recursive merging of nested dicts is a common 'deep merge' pattern for config layering.
- code-review-06: The function does not raise an error on a dict-vs-non-dict type mismatch.
- code-review-06: The overwrite-on-type-mismatch behavior could mask type mismatches between config layers.
- code-review-06: The function performs no type validation at all.
- code-review-06: A caller could overwrite an entire config section with a plain string and receive no warning.
- code-review-06: The original author of the code is gone.
- code-review-06: A two-line docstring would spare the next person from reverse-engineering the behavior.
- code-review-07: The function returns three different things on failure, and none of them is an error.
- code-review-07: A caller cannot distinguish 'the operation returned null' from 'the operation failed after 3 attempts'.
- code-review-07: A suggested fix is to return null consistently on both failure paths, or better, rethrow the last error so callers keep the status code and message.
- code-review-07: Duck-typing on .status without a guard is a classic gap.
- code-review-07: Callers might need error context to distinguish 'not found' from 'unauthorized' from 'validation failed'.
- code-review-07: The backoff should probably be '1000 * (i + 1)'.
- code-review-07: There is no comment or other signal indicating intent for the backoff timing.
- code-review-07: The function ignores the Retry-After header.
- code-review-07: A 429 response commonly carries a header telling the client how long to wait.
- code-review-07: The function guesses the wait time instead of using Retry-After.
- code-review-07: The 'attempts' parameter name is ambiguous.
- code-review-07: 'attempts' is the total number of tries, not the number of retries after the first failure.
- code-review-07: A caller passing attempts: 1 gets no retries at all.
- code-review-07: The attempts semantics are easy to get wrong without reading the source.
- code-review-07: The backoff for 5xx errors is linear rather than exponential.
- code-review-07: Linear backoff might be intentional given the small default of 3 attempts.
- code-review-07: Linear backoff is worth flagging if the helper is reused with a higher attempts value.
- code-review-07: The default number of attempts is 3.
- code-review-07: The absence of jitter and Retry-After handling is a plausible omission rather than clearly a bug.
- code-review-07: The two issues to fix first are the undefined/null inconsistency and the swallowing of non-HTTP exceptions.
- code-review-08: `tmp-`/`.part` files are deleted with no limit and can push `removed` past 500 before any age-based cleanup runs.
- code-review-08: `removed` is returned but never logged or persisted in the snippet, so past runs cannot be audited after the fact.
- debugging-01: The expression cfg['Port'] appears on line 4 of the code.
- debugging-01: The dictionary defines "port" with the value 8080.
- debugging-01: The dictionary defines "host" with the value "localhost".
- debugging-01: The function get_url returns the f-string "http://{cfg['host']}:{cfg['port']}/api".
- debugging-01: The corrected code prints http://localhost:8080/api.
- debugging-02: Inside a `function` passed to `setInterval`, `this` points to the global object.
- debugging-02: Because `this` is not the `Timer` instance, `this.seconds` evaluates to `undefined`.
- debugging-04: A file's encoding can be detected at runtime using the `chardet` library.
- debugging-04: A file's encoding can be detected at runtime using the `charset-normalizer` library.
- debugging-04: Silently replacing characters may not be acceptable for every use case.
- debugging-06: The error means the export job's database connection pool ran out of free connections.
- debugging-06: A request waited the full 30-second timeout.
- debugging-06: The export job shares a database with an analytics service.
- debugging-06: Pool contention with the analytics service is the most likely cause of the error.
- debugging-06: A scheduled analytics query or long-running report can hold connections during the export window and starve the export job's pool.
- debugging-06: Pool contention is timing-based rather than data-based, which fits the pattern of failures not always occurring at the same batch number.
- debugging-06: The failures do not always occur at the same batch number.
- debugging-06: A pool size too small for peak concurrency is a possible cause.
- debugging-06: If the export job's configured pool size doesn't match its worker count or number of parallel batches, a transient spike in concurrent requests can exhaust the pool without an external actor.
- debugging-06: Slow or blocked queries holding connections is a possible cause.
- debugging-06: A lock wait, a missing index, or a long transaction on either service can hold a connection open well past normal duration.
- debugging-06: A connection held open past normal duration reduces the effective pool size for other consumers.
- debugging-06: Connection leaks are a possible cause.
- debugging-06: If a code path fails to release a connection back to the pool, such as on an unhandled exception, the pool shrinks over time until it saturates.
- debugging-06: A weekly failure cadence could indicate a slow leak that accumulates until a threshold is tripped.
- debugging-06: The failures occur on a weekly cadence.
- debugging-06: Autovacuum or maintenance jobs are a possible cause.
- debugging-06: A nightly database cron job such as vacuum, backup, or index rebuild can spike I/O and hold connections.
- debugging-06: The failures occurred at 02:14 on the failure nights.
- debugging-06: Failures clustering around a recurring analytics job time would make that job the primary suspect.
- debugging-06: Most connection pool libraries expose active, idle, and waiting connection counts.
- debugging-06: SQLAlchemy, HikariCP, and pgbouncer are examples of pool libraries that expose connection metrics.
- debugging-06: Logging or graphing pool metrics over time shows the pool exhausting in context rather than after the fact.
- debugging-06: `SHOW PROCESSLIST` is a MySQL command for seeing what is holding connections and for how long.
- debugging-06: `pg_stat_activity` is a Postgres view that can be queried to see what is holding connections and for how long.
- debugging-06: Slow-query logging and lock-wait logging can be enabled to identify whether a specific query is the bottleneck.
- debugging-06: A missing `finally` block or missing context manager can cause a connection to be acquired without a guaranteed release.
- debugging-06: Cron jobs, backups, or vacuum operations near 02:00 might coincide with the export window.
- debugging-06: Increasing pool size or adding a circuit breaker is a mitigation rather than a fix.
- debugging-06: Raising the pool size can mask the issue but buys time for investigation.
- debugging-06: The export job already has retry logic in place.
- debugging-06: The retry logic is working, as evidenced by attempt 2 also failing.
- debugging-06: Attempt 2 of the retry also fails.
- debugging-06: The strongest first step is to overlay the export job's timestamps with the analytics service's schedule.
- debugging-06: If two systems share a database and only the export job errors, an external consumer competing for connections is the most probable explanation.
- debugging-07: The digest counts events from a shared table.
- debugging-07: An example of missing isolation is pytest-xdist without a --dist scheme that partitions data.
- debugging-07: Another example of missing isolation is a Redis or cache key not namespaced by worker ID.
- debugging-07: If the digest filters by events in the last N minutes and the test runs near a boundary, added latency from parallel load can push the third event's timestamp out of the window.
- debugging-07: Testing isolation in isolation often still passes.
- debugging-07: Checking test isolation is the fastest check and the most common root cause.
- debugging-07: The full suite should be run serially in CI a handful of times.
- debugging-07: A missing seeded event indicates a race or window issue.
- debugging-08: The combination of these three patterns points away from a single leaking object and toward two or three compounding causes.
- debugging-08: A listener, subscription, or timer leak in the webhook handler is a plausible cause.
- debugging-08: Webhook processing adds its own leak on top of a baseline leak.
- debugging-08: A baseline leak independent of webhooks (thread-local accumulation, connection pool growth, scheduled job state, or dynamic class/proxy generation) is a plausible cause.
- debugging-08: A baseline leak accounts for the canary's residual growth with zero webhook traffic.
- debugging-08: Fragmentation and off-heap buffers do not shrink on idle GC cycles the way live-object heap does.
- debugging-08: In Node, `process._getActiveHandles().length` can be sampled over time as a quick check of live handles.
- debugging-08: In the JVM, active threads and scheduled tasks can be counted to detect handle leaks.
- debugging-08: A steady climb in thread count, open file descriptors, or connection pool size on the canary points to a leak in the base request path or a scheduled background job.
- debugging-08: `-XX:NativeMemoryTracking=summary` enables Native Memory Tracking in the JVM.
- debugging-08: For Node or Go, `pmap` output can be checked for growing anonymous mappings.
- debugging-08: Class or object-type histograms are far cheaper and lower-risk to capture in production than a full heap dump.
- debugging-08: `jmap -histo <pid>` captures a class histogram on the JVM.
- debugging-08: `v8.getHeapStatistics()` provides heap statistics in Node.
- debugging-08: Diffing histograms from morning to night on both the canary and a normal instance reveals which object type grows without bound.
- explanation-01: In chaining, insertion is fast because the map computes the hash and appends to the list.
- explanation-01: Most general-purpose hash maps use chaining.
- explanation-02: In the example, a transaction reads a product row with `version = 5` and then issues an UPDATE with `WHERE id = 42 AND version = 5` that sets `stock = stock - 1` and `version = version + 1`.
- explanation-02: In the example, if a concurrent transaction already updated the row so that `version` is now 6, the UPDATE statement affects zero rows.
- explanation-02: A pessimistic locking example is a banking transaction that reads an account row with a lock using `SELECT balance FROM accounts WHERE id = 42 FOR UPDATE;`.
- explanation-06: A slowdown can be caused by a slow external API call.
- explanation-06: A slowdown can be caused by unindexed queries.
- explanation-06: A cache does nothing for slowdowns caused by the network, external API calls, unindexed queries, or inefficient application code.
- explanation-06: In read-heavy traffic, such as 90% reads, a cache is likely to help because many requests can be served from the cache instead of the database.
- explanation-06: The read-to-write ratio can be measured by checking logs or adding metrics that count reads compared with writes over a representative period.
- explanation-06: Adding a database index and optimizing a slow API call are alternatives when the database is not the bottleneck.
- explanation-07: Whether to shard depends on operational maturity, specifically whether the team has experience running a distributed data layer.
- explanation-07: Sharding too early locks in a shard key before real access patterns are understood.
- explanation-07: A wrong shard key forces a costly re-shard later.
- explanation-07: Vacuum, index maintenance, and backup/restore times grow as a database grows and can eventually block operations.
- explanation-07: A concrete trigger for revisiting sharding could be reaching 1-2 TB or writes saturating the primary.
- explanation-08: The other factor is payload size and the network path.
- explanation-08: If JSON encoding and decoding are 2% of total request time, a 10x serialization speedup barely changes total request time.
- explanation-08: If JSON encoding and decoding are 40% of total request time, a 10x serialization speedup matters a lot.
- explanation-08: Binary formats often reduce payload size.
- explanation-08: Payload size reduction helps most when bandwidth or latency is the bottleneck.
- explanation-08: Payload size reduction helps less when payloads are small or requests are local.
- explanation-08: Published comparisons between JSON and formats like Protocol Buffers or MessagePack vary widely.
- explanation-08: Published comparisons often report 2x to 10x improvements in serialization speed.
- explanation-08: Published comparisons often report 20% to 50% reductions in payload size.
- explanation-08: Published benchmark numbers come from other people's workloads.
- explanation-08: Data shapes, field types, and payload sizes can push results in either direction.
- explanation-08: Citing someone else's benchmark would mislead the user.
- explanation-08: Typical and worst-case payload sizes for the actual data should be measured.
- explanation-08: Where payloads travel — same host, same data center, or the public internet — determines whether size reduction helps.
- explanation-08: Prototyping the binary format on real data and re-measuring with the same method yields comparable numbers.
- explanation-08: Expected end-to-end improvement can be calculated from the serialization-time percentage and prototype numbers using Amdahl's law.
- summarization-01: Each keyboard shortcut appears in the tooltip of its corresponding button.
- summarization-01: App startup time was reduced by about 40%.
- summarization-02: The rollback ran from 09:14 to 09:48.
- summarization-02: The detection and recovery process worked as intended.
- summarization-02: Two process gaps enabled the mistake.
- summarization-03: No existing stored memory is relevant to this task.
- summarization-04: Clicking PDF export three additional times results in four "export failed" error banners.
- summarization-07: The text is a one-paragraph summary written for a team lead.
- summarization-07: Two findings need more investigation before being treated as conclusions.

### plain-language

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 27 | 0 | 0.0 | 5 | 5 |
| code-review-02 | 21 | 16 | 0.762 | 22 | 3 |
| code-review-03 | 15 | 0 | 0.0 | 9 | 9 |
| code-review-04 | 25 | 0 | 0.0 | 10 | 10 |
| code-review-05 | 37 | 27 | 0.73 | 31 | 4 |
| code-review-06 | 26 | 14 | 0.538 | 29 | 9 |
| code-review-07 | 39 | 29 | 0.744 | 33 | 8 |
| code-review-08 | 37 | 26 | 0.703 | 49 | 9 |
| debugging-01 | 6 | 6 | 1.0 | 8 | 3 |
| debugging-02 | 16 | 10 | 0.625 | 12 | 3 |
| debugging-03 | 9 | 9 | 1.0 | 9 | 0 |
| debugging-04 | 16 | 12 | 0.75 | 16 | 5 |
| debugging-05 | 20 | 16 | 0.8 | 18 | 0 |
| debugging-06 | 6 | 2 | 0.333 | 23 | 23 |
| debugging-07 | 35 | 0 | 0.0 | 8 | 7 |
| debugging-08 | 36 | 22 | 0.611 | 37 | 24 |
| explanation-01 | 33 | 23 | 0.697 | 25 | 2 |
| explanation-02 | 28 | 22 | 0.786 | 24 | 2 |
| explanation-03 | 31 | 20 | 0.645 | 25 | 2 |
| explanation-04 | 45 | 25 | 0.556 | 30 | 5 |
| explanation-05 | 21 | 17 | 0.81 | 15 | 3 |
| explanation-06 | 15 | 12 | 0.8 | 14 | 5 |
| explanation-07 | 28 | 0 | 0.0 | 0 | 0 |
| explanation-08 | 11 | 8 | 0.727 | 12 | 7 |
| summarization-01 | 10 | 7 | 0.7 | 12 | 3 |
| summarization-02 | 15 | 14 | 0.933 | 13 | 3 |
| summarization-03 | 14 | 14 | 1.0 | 12 | 0 |
| summarization-04 | 13 | 11 | 0.846 | 14 | 3 |
| summarization-05 | 12 | 11 | 0.917 | 11 | 0 |
| summarization-06 | 13 | 13 | 1.0 | 12 | 0 |
| summarization-07 | 16 | 15 | 0.938 | 16 | 1 |
| summarization-08 | 26 | 24 | 0.923 | 20 | 2 |

Median fraction: 0.737 over 32 scored pairs.

Median additions: 3.0 over 32 scored pairs.

Lost facts:

- code-review-01: A mutable default argument such as `roles=[]` causes the same list object to be reused across calls.
- code-review-01: Because the default list is mutated with `.append`, every call without an explicit `roles` accumulates `"member"` entries from previous calls.
- code-review-01: The mutable default argument is a classic Python gotcha.
- code-review-01: A bare `except:` catches everything, including `KeyboardInterrupt` and `SystemExit`.
- code-review-01: A bare `except:` silently swallows the real error.
- code-review-01: Swallowing the error loses all information about why the insert failed, making debugging painful.
- code-review-01: The code should at minimum catch a specific exception type and probably log it.
- code-review-01: The `db` parameter defaults to `None` with no guard against that case.
- code-review-01: If `db` isn't passed, calling `db.insert(...)` raises `AttributeError`.
- code-review-01: That `AttributeError` gets silently swallowed by the bare except and the function returns `False`.
- code-review-01: The returned `False` gives no indication of whether it was a misuse error or a real DB failure.
- code-review-01: If a caller passes in their own `roles` list, `add_user` mutates it in place by appending `"member"`.
- code-review-01: Mutating the caller's list is a surprising side effect that is not signaled by the function's interface.
- code-review-01: The `True`/`False` return value conflates "user added" with "any exception occurred".
- code-review-01: Because of the conflated return value, callers can't distinguish configuration errors (no `db`) from actual insert failures.
- code-review-01: The function has no duplicate-role handling.
- code-review-01: If `"member"` is already in `roles`, it gets appended again, creating duplicates.
- code-review-01: The function performs no input validation.
- code-review-01: `name` isn't checked for type or emptiness before insertion.
- code-review-01: The proposed cleaner version raises `ValueError("db is required")` when `db` is `None`.
- code-review-01: The proposed version copies `roles` with `list(roles) if roles else []`.
- code-review-01: The proposed version appends `"member"` only if it is not already in `roles`.
- code-review-01: The proposed version calls `db.insert({"name": name, "roles": roles})`.
- code-review-01: The proposed version fixes the mutable default argument problem.
- code-review-01: The proposed version avoids mutating caller data.
- code-review-01: The proposed version avoids duplicate roles.
- code-review-01: The proposed version lets real exceptions propagate instead of hiding them.
- code-review-02: The most critical bug is a race condition.
- code-review-02: Parsing bad responses as valid data can produce more confusing downstream errors.
- code-review-02: The code unnecessarily mixes `async`/`await` with `.then()` chains.
- code-review-02: Declaring a function `async` without using `await` defeats the purpose of `async` and signals confused intent.
- code-review-02: The fixed version awaits `res.json()` to obtain `profile` and returns `profile.name.toUpperCase()`.
- code-review-03: The code has a SQL injection vulnerability, which is its critical issue.
- code-review-03: The `customer_name` value is concatenated directly into the query string.
- code-review-03: The `status` value is concatenated directly into the query string.
- code-review-03: An attacker can pass a value like `' OR '1'='1` to alter the query logic.
- code-review-03: An attacker can pass a value like `'; DROP TABLE orders; --` to run arbitrary SQL.
- code-review-03: Parameterized queries fix the SQL injection issue.
- code-review-03: A parameterized version passes the query with `%s` placeholders and a tuple of values to `cursor.execute`.
- code-review-03: The `?` placeholder should be used instead of `%s` when using sqlite3.
- code-review-03: Using `SELECT *` is fragile if the table schema changes.
- code-review-03: It is better to name only the columns the caller needs instead of using `SELECT *`.
- code-review-03: The code performs no input validation.
- code-review-03: Nothing stops `status` from being an unexpected or invalid value before it reaches the database.
- code-review-03: The parameterization fix alone resolves the injection risk.
- code-review-03: The parameterization fix also sidesteps quoting bugs.
- code-review-03: In the current code, a name containing an apostrophe would break the query.
- code-review-04: The `increment` method performs a read-modify-write consisting of `current = self.value` followed by `self.value = current + 1`.
- code-review-04: The `increment` method's read-modify-write is performed without synchronization.
- code-review-04: The unsynchronized read-modify-write in `increment` is a race condition.
- code-review-04: When multiple threads call `increment()` concurrently, two threads can read the same `current` value before either writes back.
- code-review-04: When two threads read the same value before either writes back, an increment is lost.
- code-review-04: Over many concurrent calls, the final `value` will be less than the number of increments performed.
- code-review-04: There is no locking between `reset` and `increment`.
- code-review-04: A call to `reset()` can interleave with an in-flight `increment()`.
- code-review-04: A `reset()` interleaving with an in-flight `increment()` can produce a surprising result.
- code-review-04: If a reset happens after the read but before the write in `increment`, the increment silently undoes the reset by writing `1`.
- code-review-04: Neither `increment` nor `reset` uses a `threading.Lock` or other synchronization primitive.
- code-review-04: Nothing in the class is thread-safe, despite the class being used from multiple threads.
- code-review-04: The class provides no correctness guarantee under concurrency.
- code-review-04: The code shown contains no synchronized `get()` or `value` accessor.
- code-review-04: If callers read `counter.value` directly from another thread while an increment is in progress, they may observe a stale or inconsistent value.
- code-review-04: In CPython, the GIL protects the single attribute read, making the unsafe direct read less severe.
- code-review-04: Safety of the direct attribute read is not guaranteed by the Python language.
- code-review-04: Reading between the `current = self.value` and `self.value = ...` steps in `increment` can return an intermediate value.
- code-review-04: The fix is to guard the critical sections with a `threading.Lock`.
- code-review-04: The fixed `Counter.__init__` creates `self._lock = threading.Lock()` and sets `self.value = 0`.
- code-review-04: The fixed `increment` executes `self.value += 1` inside a `with self._lock:` block.
- code-review-04: The fixed `reset` executes `self.value = 0` inside a `with self._lock:` block.
- code-review-04: Using the lock makes `increment` and `reset` mutually exclusive.
- code-review-04: With the lock, no updates are lost.
- code-review-04: With the lock, resets cannot be silently overwritten by an in-flight increment.
- code-review-05: The missing `cd` success check is the most dangerous bug in the script.
- code-review-05: The variables `$1`, `$BACKUP_DIR`, and `$f` are unquoted in the script.
- code-review-05: The unquoted variables should be written as `"$1"`, `"$BACKUP_DIR"`, and `"$f"`.
- code-review-05: The `rm -rf *.tmp` no-match error is harmless in this script but sloppy and confusing.
- code-review-05: The `echo Cleaned $BACKUP_DIR` message is misleading if `cd` never actually happened.
- code-review-05: `set -u` would have caught the missing-argument problem immediately.
- code-review-05: The script does not restore the original working directory when it finishes.
- code-review-05: Failing to restore the original working directory matters if the script is sourced or chained with other commands.
- code-review-05: The suggested fix checks `[ -z "$BACKUP_DIR" ] || [ ! -d "$BACKUP_DIR" ]` and prints a usage message to stderr before exiting with status 1.
- code-review-05: The suggested fix calls `gzip -- "$f"`.
- code-review-06: Merging base={'a': {'x': 1}} with override={'a': 'oops'} raises AttributeError: 'str' object has no attribute 'items' inside the recursive call.
- code-review-06: The missing type check on the override value is a real crash bug for malformed or unexpected input.
- code-review-06: A dict value in `override` under a key not already in `merged` is aliased directly instead of being merged or copied.
- code-review-06: The aliasing behavior for new nested dicts is asymmetric with the recurse-into-dicts path.
- code-review-06: Using `None` as a deletion marker is a common config-merging convention known as a tombstone value.
- code-review-06: Using `is None` instead of a falsiness check means `0`, `False`, and `""` are treated as real values.
- code-review-06: `merged.pop(key, None)` swallows the KeyError, so deleting a non-existent key is a silent no-op.
- code-review-06: A typo'd key in an override config intended to delete something fails silently instead of raising.
- code-review-06: `dict(base)` always returns a plain `dict`, so a subclass type such as `OrderedDict` or a custom Mapping is lost.
- code-review-06: `isinstance(merged[key], dict)` does not match dict-like types that do not subclass `dict`, such as a custom Mapping.
- code-review-06: Dict-like values that are not `dict` subclasses get overwritten instead of merged, inconsistently with regular dicts.
- code-review-06: The intended behavior for `None`, for list merging, and for shallow aliasing cannot be inferred from the code alone.
- code-review-07: An immediate first retry defeats the purpose of backing off on a rate-limit response.
- code-review-07: The zero-delay first retry appears to be an off-by-one error rather than a design choice.
- code-review-07: If `fn` can legitimately resolve to null on success, callers cannot distinguish success from failure.
- code-review-07: Callers of this helper exist that cannot be seen.
- code-review-07: Treating 429 and 5xx as retryable is likely deliberate.
- code-review-07: Treating all other errors as non-retryable is likely deliberate.
- code-review-07: The zero-delay first retry is probably accidental.
- code-review-07: Swallowing non-HTTP errors into null is probably accidental.
- code-review-07: Whether existing callers rely on null as a sentinel should be determined before changing the helper.
- code-review-07: The null sentinel behavior is the part most likely to break silently if 'fixed'.
- code-review-08: The script contains no `if __name__ == "__main__":` block.
- code-review-08: The function `clean()` is never called anywhere in the script.
- code-review-08: If the scheduler runs the script via `python script.py`, the script does nothing.
- code-review-08: `os.listdir` snapshots filenames, and `getmtime`/`os.remove` run later on those names, creating a TOCTOU race.
- code-review-08: If another process deletes a file between `os.listdir` and `getmtime`/`os.remove`, an unhandled `FileNotFoundError` is raised.
- code-review-08: The script's own tmp-file deletion branch can race with a concurrent run of the same script.
- code-review-08: `os.path.getmtime` works on a directory.
- code-review-08: The script does not check that `ROOT` exists before calling `listdir`.
- code-review-08: The rationale for the `86400 * 45` and `500` constants is undocumented and nobody can recall it.
- code-review-08: The script's current behavior falls into one of three cases: inert, silently corrupting data, or working as intended.
- code-review-08: Determining how `clean()` is invoked and whether anything creates `tmp-*`/`*.part` files as working files decides which of those three cases applies.
- debugging-02: Class bodies execute in strict mode.
- debugging-02: In strict mode, a plain function call does not fall back to the global object for `this`.
- debugging-02: In strict mode, `this` in a plain function call stays `undefined`.
- debugging-02: `this.seconds += 1` where `this` is `undefined` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: `setInterval(function () { ... }.bind(this), 1000)` is a valid fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is a valid fix.
- debugging-04: Opening a file in binary mode with "rb" avoids decoding text.
- debugging-04: Binary mode can be used when only a line count is needed.
- debugging-04: Iterating a file object in binary mode splits on \n bytes.
- debugging-04: The binary-mode approach sidesteps encoding issues entirely.
- debugging-05: A function's default value is stored on the function object itself.
- debugging-05: The failure looks flaky but is deterministic given the call order.
- debugging-05: The fix also protects callers who pass their own `tags` list from having it mutated as a side effect.
- debugging-05: Copying a caller-supplied `tags` list, e.g. `tags = list(tags) if tags is not None else list(DEFAULT_TAGS)`, avoids mutating the caller's list.
- debugging-06: The speaker will check whether the directory contains relevant code before answering.
- debugging-06: The command issued was `ls -la`.
- debugging-06: The command's stated purpose was to list files in the working directory.
- debugging-06: The working directory should be checked for relevant code before the question is answered.
- debugging-07: The test failure is intermittent and occurs only under `-n 4` parallel CI runs, never in serial runs.
- debugging-07: The parallelism is almost certainly relevant to the failure rather than incidental.
- debugging-07: Cross-test data leakage from shared state is a plausible cause of the failure.
- debugging-07: If the digest query is scoped by a time window rather than a unique test/user/session ID, a concurrently running test in another worker can insert or delete rows that the test sees.
- debugging-07: Reusing a shared fixture user or tenant across tests allows concurrent workers to interfere with each other's data.
- debugging-07: Serial runs never share concurrent state, so cross-test leakage only appears under parallelism.
- debugging-07: Cross-test data leakage from shared state is the single most common cause of this exact symptom.
- debugging-07: A digest read-your-writes / eventual consistency race is a plausible cause of the failure.
- debugging-07: If seeding the 3 events goes through an asynchronous API path (queue, background job, message bus, cache invalidation), the digest read can happen before all 3 writes are durably visible, yielding N-1 events.
- debugging-07: Load from 3 other workers increases latency variance enough to expose a race that does not manifest without resource contention.
- debugging-07: Test isolation implemented via truncation or transaction rollback racing across workers is a plausible cause.
- debugging-07: If cleanup uses TRUNCATE, shared sequence resets, or a global counter instead of per-worker or per-test transactions, one worker's teardown can wipe or renumber rows another worker just wrote.
- debugging-07: An autoincrement ID or pagination boundary issue is a plausible cause.
- debugging-07: If the digest endpoint has an implicit LIMIT and orders by an insufficiently unique ID or timestamp, concurrent inserts from other workers can push one of the test's events outside the page or limit boundary.
- debugging-07: Connection pool or DB isolation level behavior is a plausible cause.
- debugging-07: READ COMMITTED with async replication, or a connection pool reusing a stale snapshot, can cause a worker to read a stale view missing the third insert.
- debugging-07: The cheapest first diagnostic step is to reproduce locally under contention by running the whole suite with `pytest -n 4` repeatedly.
- debugging-07: pytest-repeat provides a `--count` option, e.g. `--count=50`.
- debugging-07: If the failure reproduces locally under parallelism, that confirms it is parallelism-driven rather than CI-infrastructure-specific.
- debugging-07: Reproducing locally allows debugging with full tooling.
- debugging-07: The second step is to run only this test file or test repeatedly under `-n 4` to distinguish cross-test pollution from an internal race.
- debugging-07: If the test never fails alone under `-n 4` but fails with the full suite, that strongly implicates shared state or fixtures rather than an internal race.
- debugging-07: CI keeps no artifacts.
- debugging-07: Diagnostics added to the test should be temporary rather than permanent.
- debugging-07: A diagnostic step is to patch the test to log the actual event IDs and any owner/tenant/session identifiers returned in the digest on failure, then run it repeatedly until it reproduces.
- debugging-07: If the digest contains an unexpected event ID belonging to another test, that directly confirms cross-test data leakage.
- debugging-07: A diagnostic step is to grep whether the API seeding path involves a queue, Celery task, outbox pattern, or cache layer.
- debugging-07: If the seeding path is asynchronous, one should check whether the test waits on a task-completion signal or assumes synchronous completion.
- debugging-07: If adding a short explicit wait or poll-until-visible makes the failure disappear under parallel runs, the eventual consistency race is confirmed.
- debugging-07: A diagnostic step is to grep the fixtures for hardcoded user IDs, tenant IDs, or 'test@example.com', or for a shared DB rather than one per worker.
- debugging-07: pytest-xdist should typically get its own DB or schema per worker.
- debugging-07: pytest-django's `--reuse-db` can interact badly with `-n`.
- debugging-07: A shared SQLite file can cause shared-state problems across parallel workers.
- debugging-07: The recommended first move is reproducing under `-n 4` locally, because it turns an unreproducible CI-only flake into something iterable.
- debugging-07: The recommended second move is bisecting isolation problems versus an internal race.
- debugging-08: An unbounded per-order or per-webhook tracking structure is the explanation most consistent with all four observations.
- debugging-08: Examples of such tracking structures include idempotency keys, dedup sets, in-flight/retry state, and in-memory audit logs.
- debugging-08: An unbounded per-order tracking structure grows with every order, which explains growth on the canary.
- debugging-08: High-cardinality labels match canary growth because the canary still emits per-order metrics.
- debugging-08: A cache eviction leak, where evicted entries are kept alive elsewhere, is a possible cause.
- debugging-08: A secondary index, listener, or closure can still reference an object after the cache evicts it.
- debugging-08: A steady cache bound caps only cache-visible memory, not total retained memory.
- debugging-08: One check is to pick evicted product IDs in a heap dump and trace their GC roots to see if anything outside the cache still retains them.
- debugging-08: Allocator or runtime fragmentation, rather than a true leak, is a possible cause.
- debugging-08: Fragmentation would explain gradual RSS growth that does not return to baseline, independent of application logic.
- debugging-08: If live heap is flat while RSS climbs, the cause is fragmentation rather than retained objects.
- debugging-08: Fragmentation requires a different fix than retained objects.
- debugging-08: Diffing object counts by type will immediately reveal which of the first four causes is real.
- debugging-08: The exact diagnostic tool to use differs by runtime, such as JVM, Node, or Go.
- explanation-01: An example of computing an index is hash("apple") % array_size.
- explanation-01: Separate chaining is simple to implement.
- explanation-01: In the worst case, with many collisions in one slot, separate chaining degrades to O(n) list traversal.
- explanation-01: Quadratic probing tries index+1², then index+2², and so on.
- explanation-01: Double hashing uses a second hash function to compute the step size.
- explanation-01: Open addressing performance degrades sharply as the table fills up due to clustering.
- explanation-01: Open addressing requires resizing/rehashing earlier, typically once the load factor exceeds about 0.7.
- explanation-01: Chaining is easier to reason about and more forgiving if the load factor is not tuned carefully.
- explanation-01: Python's dict uses an open addressing variant.
- explanation-01: Rust's HashMap uses an open addressing variant.
- explanation-02: Optimistic locking fits read-heavy workloads.
- explanation-02: A CMS article edit is an example workload suited to optimistic locking.
- explanation-02: A shopping cart is an example workload suited to optimistic locking.
- explanation-02: Postgres and MySQL support pessimistic locking via SELECT ... FOR UPDATE.
- explanation-02: Seat and inventory reservation systems are examples of workloads suited to pessimistic locking.
- explanation-02: In reservation systems, two users grabbing the last item is unacceptable.
- explanation-03: If a sender sends data as fast as the receiver's advertised window allows, it can overwhelm a router queue.
- explanation-03: Slow start is also used after certain recovery events.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The sender's actual sending rate is limited by the smaller of the congestion window and the receiver's advertised window.
- explanation-03: The initial cwnd was historically 1 segment.
- explanation-03: The initial cwnd is now typically 2-10 segments.
- explanation-03: RFC 6928 raised the initial congestion window value to improve performance for short flows.
- explanation-03: Each time the sender receives an ACK confirming a segment was delivered, it increases cwnd by roughly one segment.
- explanation-03: Because every segment acked in a round trip triggers a cwnd increase, cwnd effectively doubles every round-trip time.
- explanation-03: The congestion avoidance phase is more conservative than slow start and uses linear growth.
- explanation-03: When packet loss is detected, ssthresh is lowered and cwnd is reset or cut back.
- explanation-04: A process has its own file descriptors.
- explanation-04: A process has its own OS-level resources.
- explanation-04: All threads in a process share the same resources.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own instruction pointer.
- explanation-04: A crashed process can be restarted independently.
- explanation-04: nginx uses multiple processes.
- explanation-04: Chrome uses a per-tab process model.
- explanation-04: Threads release the GIL while waiting on I/O.
- explanation-04: Multiple processes are preferable when stronger security or permission boundaries are needed.
- explanation-04: Processes can run under different privilege levels.
- explanation-04: Processes are the right tool for sandboxing untrusted code, such as a plugin system or a browser renderer process.
- explanation-04: Processes are the right tool for limiting what a component can access.
- explanation-04: Multiple processes are preferable when components need independent lifecycle management.
- explanation-04: Separate processes allow components to be started, stopped, restarted, or scaled independently using OS-level tools.
- explanation-04: OS-level tools for managing processes include kill, restart, and resource limits via cgroups.
- explanation-04: Using separate processes avoids coordinating shutdown logic inside one program.
- explanation-04: Processes win when isolation is needed: fault tolerance, true CPU parallelism around language-level locks, security boundaries, or independent lifecycle.
- explanation-04: Inter-process communication is slower and more explicit than thread communication.
- explanation-04: Inter-process communication mechanisms include pipes, sockets, and shared memory segments.
- explanation-05: A garbage collector walks references starting from roots.
- explanation-05: Roots include global variables, stack frames, and active closures.
- explanation-05: A subscribed object and anything it closes over stay reachable indefinitely.
- explanation-05: Closures capturing large outer scopes longer than needed is a frequent cause of memory leaks.
- explanation-06: Possible alternative causes of the performance problem include slow queries, network latency, N+1 calls, and serialization.
- explanation-06: A cache is another system that must be operated.
- explanation-06: Cache invalidation is a classic source of subtle bugs.
- explanation-07: 200 GB is well within what a single well-tuned Postgres instance can handle.
- explanation-07: Single Postgres instances can comfortably run into multi-TB territory with the right hardware and indexing.
- explanation-07: Sharding is a one-way architectural decision.
- explanation-07: Sharding adds significant operational complexity.
- explanation-07: Sharding should be justified by concrete pressure rather than vague expected growth.
- explanation-07: Sharding only helps when the constraint is write throughput, storage, or single-node CPU/IO that vertical scaling cannot fix.
- explanation-07: If the bottleneck is bad queries, missing indexes, or lock contention, sharding will not fix it.
- explanation-07: Sharding replicates query, index, and lock-contention problems across all nodes.
- explanation-07: For read-heavy workloads, read replicas are a far cheaper solution than sharding.
- explanation-07: Not knowing the expected growth rate means lacking the input needed to size the decision.
- explanation-07: A rough growth number such as 2x in a year versus 50x in a year completely changes the answer.
- explanation-07: Sharding only works cleanly when there is an obvious partition dimension such as tenant/customer ID or region.
- explanation-07: A good shard key requires mostly-independent access patterns across partitions.
- explanation-07: If queries routinely join or aggregate across the shard key, sharding creates constant cross-shard query pain.
- explanation-07: Current CPU, IO, and connection utilization determine how much headroom remains on existing hardware.
- explanation-07: At 20% utilization on a mid-size instance, there is likely 5-10x runway before sharding is urgent.
- explanation-07: After sharding, every schema change, migration, and query must be shard-aware.
- explanation-07: Cross-shard transactions, joins, and unique constraints become hard or impossible.
- explanation-07: Building routing and rebalancing infrastructure can take months.
- explanation-07: Premature sharding causes a permanent drop in team velocity.
- explanation-07: Waiting too long to shard risks an emergency migration under load with less room to test and roll back safely.
- explanation-07: Waiting too long is usually still cheaper than premature sharding.
- explanation-07: Read replicas, table partitioning, connection pooling, and vertical scaling can mitigate the interim before sharding.
- explanation-07: Postgres native table partitioning operates within a single instance and is not the same as sharding.
- explanation-07: Read replicas, partitioning, connection pooling, and vertical scaling are reversible, incremental steps.
- explanation-07: Postgres native partitioning by date or tenant addresses table size and vacuum/index bloat concerns.
- explanation-07: Native partitioning provides much of the operational benefit of sharding without cross-node complexity.
- explanation-07: Sharding should be revisited only when utilization numbers show vertical scaling, partitioning, and read replicas will not suffice for the next 12-18 months.
- explanation-08: JSON parsing and serialization is often not the performance bottleneck.
- explanation-08: Network, database, and business logic usually dominate request time.
- explanation-08: The migration cost includes client compatibility, debuggability, and tooling.
- summarization-01: The app now starts up to 40% faster.
- summarization-01: Hovering over any toolbar button displays that button's keyboard shortcut.
- summarization-01: Telemetry batching changes were omitted from these release notes.
- summarization-02: The small pool size of 5 was intentional for staging.
- summarization-04: Clicking the PDF export button multiple times produces multiple "export failed" error banners, one per click.
- summarization-04: The bug was reproduced on the latest version of Firefox.
- summarization-05: Ada is assigned to check with the mobile team's lead about whether the mobile team was informed of the API deprecation.
- summarization-07: Memory impact, production tail latency, and the crash's cause all need further investigation before rollout.
- summarization-08: The progress bar finding is rated FIRM, with the cause tentative.
- summarization-08: The template gallery observation is not a top-3 finding but should be flagged.

Added facts (styled only):

- code-review-01: A read operation was performed on a file named MEMORY.md.
- code-review-01: The file read is located at /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-weclp6d3/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-121asz23/memory/MEMORY.md.
- code-review-01: MEMORY.md resides in a directory named 'memory'.
- code-review-01: That memory directory belongs to a project entry named '-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-121asz23'.
- code-review-01: The project entry is stored under a 'projects' directory inside /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-weclp6d3.
- code-review-02: The assistant checked the memory directory.
- code-review-02: No stored context applies to this task.
- code-review-02: A network failure in the function would produce an unhandled promise rejection.
- code-review-03: The tool being invoked is named "bash".
- code-review-03: The request specifies a "command" field and a "description" field.
- code-review-03: The command runs `cat` on the file "/var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-weclp6d3/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-121asz23/memory/MEMORY.md".
- code-review-03: The `cat` command's standard error is redirected to /dev/null via `2>/dev/null`.
- code-review-03: The command falls back to `echo "NO MEMORY FILE"` if the `cat` command fails, using the `||` operator.
- code-review-03: The command's description is "Check memory index for relevant context".
- code-review-03: The targeted file is named MEMORY.md and resides in a directory named "memory".
- code-review-03: The memory directory path is under a temporary folder named "style-config-pairs-weclp6d3".
- code-review-03: The project directory in the path is named "-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-121asz23".
- code-review-04: The speaker will check memory for saved preferences before reviewing the item in question.
- code-review-04: Checking memory precedes the review in the speaker's stated order of operations.
- code-review-04: The speaker invokes the Read tool.
- code-review-04: The Read tool is called with a file_path parameter.
- code-review-04: The file being read is named MEMORY.md.
- code-review-04: The path of the file read is /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-weclp6d3/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-121asz23/memory/MEMORY.md
- code-review-04: The MEMORY.md file resides in a directory named 'memory'.
- code-review-04: The memory directory is located under a project directory named '-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-121asz23'.
- code-review-04: That project directory is inside a 'projects' directory under /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-weclp6d3/.
- code-review-04: Saved preferences are stored in the speaker's memory.
- code-review-05: An unmatched glob combined with the missing-argument or failed-cd problems adds risk of deleting in the wrong directory.
- code-review-05: gzip fails if a file is unreadable or is already gzipped.
- code-review-05: In the rewrite, all variable uses are quoted.
- code-review-05: `rm -f` is preferable to `rm -rf` here because only files, not directories, are being removed in the current folder.
- code-review-06: Recursive merging of nested dicts appears to be the main purpose of the function.
- code-review-06: If `base[key]` is a dict but `override[key]` is not, the code overwrites the dict wholesale.
- code-review-06: The function raises no error or warning on a type mismatch between `base[key]` and `override[key]`.
- code-review-06: If `value` is not a dict, the function overwrites instead of recursing.
- code-review-06: If `value` is a list while `merged[key]` is a dict, the list silently replaces the dict.
- code-review-06: If `base` or `override` is `None` or another non-dict type, the code raises an unclear `AttributeError`.
- code-review-06: The function has no docstring.
- code-review-06: The function has no type hints.
- code-review-06: Returning a new dict instead of mutating `base` is good practice.
- code-review-07: If fn throws null or undefined, accessing err.status throws a new error.
- code-review-07: A thrown null or undefined produces an unrelated crash that can escape uncaught.
- code-review-07: Immediate repeat requests are the opposite of the appropriate response to a 500-range 'server is overloaded' error.
- code-review-07: The delay 1000 * i grows without bound as attempts grows.
- code-review-07: The delay has no upper limit.
- code-review-07: Skipping the delay on the first 429 retry might be intentional or might be an off-by-one mistake.
- code-review-07: There is no reason to treat 5xx and 429 differently on backoff.
- code-review-07: There is no documentation or history for this function.
- code-review-08: Many programs use names like `tmp-*` or `*.part` to mark a file that is still being written.
- code-review-08: Such programs rename the file once the write finishes.
- code-review-08: Both branches share the same `removed` counter.
- code-review-08: If enough `tmp-`/`.part` files are deleted first, `removed` can pass 500 before the loop reaches an old file.
- code-review-08: That silently blocks all age-based cleanup for the rest of the run.
- code-review-08: The function returns a count.
- code-review-08: A minimum age, for example a few hours, should be added before deleting `tmp-`/`.part` files so in-progress writes are safe.
- code-review-08: Directories and broken symlinks should be skipped explicitly.
- code-review-08: Files should be sorted by modification time before applying the 500-file cap.
- debugging-01: The config dictionary is {"host": "localhost", "port": 8080}.
- debugging-01: The function get_url(cfg) returns the f-string "http://{cfg['host']}:{cfg['port']}/api".
- debugging-01: The corrected code calls print(get_url(config)).
- debugging-02: In that call, `this` points to the global object rather than the `Timer` instance.
- debugging-02: Because of this, `this.seconds` evaluates to `undefined`.
- debugging-02: That is why `NaN` is printed each second.
- debugging-04: UTF-8 supports all ASCII text plus a much wider range of characters.
- debugging-04: Reading a file as UTF-8 works just as well as ASCII for plain English files.
- debugging-04: Latin-1 is an encoding commonly used in older Windows files.
- debugging-04: The chardet library can detect a file's encoding.
- debugging-04: chardet.detect() returns a result whose "encoding" key holds the detected encoding.
- debugging-06: The memory directory listing and MEMORY.md read returned no output.
- debugging-06: No memory has been stored for this project yet.
- debugging-06: The connection pool runs out of connections because the export job and the analytics service compete for the same pool.
- debugging-06: The failure is a shared-resource contention problem, not a bug in the export job itself.
- debugging-06: The failures happen at different batch numbers each time.
- debugging-06: Failures occurring at different batch numbers indicate the trigger is timing rather than a specific row or query.
- debugging-06: A 'pool exhausted' error is a capacity error, not a query error.
- debugging-06: The export job waited the full 30 seconds and received no connection.
- debugging-06: No connection was free when the export job waited.
- debugging-06: Waiting the full timeout without getting a connection points to too many active connections rather than a single slow query.
- debugging-06: If one batch contained a poison row or a lock, the same batch number would fail each time.
- debugging-06: The failures occur weekly rather than nightly.
- debugging-06: Weekly rather than nightly failures suggest a periodic competing process.
- debugging-06: The analytics service is the most likely process spiking connection use at the same time as the export job.
- debugging-06: A weekly cron job, a weekly report, and a backup process are common suspects for periodic connection spikes.
- debugging-06: If the combined maximum connections of the export job and the analytics service can exceed the pool's limit, that explains the exhaustion.
- debugging-06: Logging active connections, checked-out connections, and wait queue depth at a fixed interval reveals the pool filling up before the timeout occurs.
- debugging-06: A connection that is not returned to the pool after use shrinks the available pool over time.
- debugging-06: Code paths that skip a connection's close or release call are especially common in error-handling branches.
- debugging-06: A single slow query or a transaction left open can hold a connection for a long time.
- debugging-06: A database's slow-query log or active-connections view can reveal connections open longer than a minute.
- debugging-06: If several worker instances each maintain their own pool, the total connections could exceed what the database allows.
- debugging-06: Multiple worker instances each holding their own pool is a common cause of pool exhaustion failures.
- debugging-07: It is not yet known whether the test in question exists in this directory.
- debugging-07: It is not yet known whether code related to the test exists in this directory.
- debugging-07: Checking the directory contents can determine whether the test and related code exist.
- debugging-07: Grounding the analysis in the real implementation is preferable to guessing.
- debugging-07: The command `ls -la` lists the contents of the current directory, including hidden entries, in long format.
- debugging-07: The `find` command searches for files whose names match '*notification*' or '*digest*', case-insensitively.
- debugging-07: The relevant files are expected to have names containing 'notification' or 'digest'.
- debugging-08: Two of the observed facts point away from a single cause.
- debugging-08: The lack of an overnight reset indicates a genuine leak rather than daytime cache warm-up.
- debugging-08: The canary's continued growth indicates a baseline leak plus a traffic-driven leak on top of it.
- debugging-08: Unbounded collections in this scenario would be keyed by request ID, order ID, or webhook ID.
- debugging-08: Candidate unbounded structures include idempotency/dedup maps, "pending" or "in-flight" trackers, retry queues, and per-request listener registrations.
- debugging-08: `jmap -histo:live` produces a heap histogram.
- debugging-08: If a heap dump is unavailable, logging the size of a suspected collection once a minute is an alternative check.
- debugging-08: A straight upward line in a collection's logged size during business hours confirms an unbounded collection.
- debugging-08: Growth with zero webhook traffic means something runs regardless of request volume.
- debugging-08: Possible request-volume-independent causes include a scheduled job, a metrics collector, a connection pool, and accumulating timers or threads.
- debugging-08: Thread count, open file descriptors, and RSS minus JVM heap size can be tracked on the canary over a day.
- debugging-08: RSS is total process memory.
- debugging-08: If RSS grows faster than the heap, the leak is off-heap rather than in Java objects.
- debugging-08: Off-heap leaks can come from buffer pools or native library allocations.
- debugging-08: Scheduled health checks and internal calls would produce a small baseline metric cost.
- debugging-08: Webhook traffic carries varying source IDs, order IDs, and campaign tags.
- debugging-08: Many metrics libraries expose their registered series count directly.
- debugging-08: Micrometer exposes its meter registry size.
- debugging-08: During campaigns, product payloads may grow larger due to more images and more promo data.
- debugging-08: Some cache libraries provide a built-in weight or size metric.
- debugging-08: If cache entry count stays flat while memory keeps rising, the cache is bounded by entry count rather than bytes.
- debugging-08: The heap histogram diff directly explains the campaign correlation.
- debugging-08: Metric cardinality problems are a common and easy-to-fix culprit.
- debugging-08: Native and off-heap leaks require different tools than a Java heap dump.
- explanation-01: Most general-purpose hash maps use chaining.
- explanation-01: Performance-focused maps that fit in a fixed memory budget often use open addressing.
- explanation-02: Any other transaction that tries to touch the locked account row must wait until the locking transaction commits or rolls back.
- explanation-02: Under low contention, optimistic locking is fast while pessimistic locking is slower due to lock overhead.
- explanation-03: Retransmissions can make congestion worse instead of better.
- explanation-03: Slow start avoids congestion collapse by testing the network first.
- explanation-04: Process creation and switching are costly because the operating system must set up or swap a full separate memory space.
- explanation-04: Threads are cheaper because they don't need a separate memory space.
- explanation-04: Locks are one mechanism for coordinating thread access to shared data.
- explanation-04: Threads can share data directly but need locks to stay safe.
- explanation-04: A GUI app juggling background work is an example where threads are preferable.
- explanation-05: During a memory leak, a program's memory usage grows over time even though its workload has not grown.
- explanation-05: Memory leaks can slow a program down.
- explanation-05: Memory leaks can crash a program.
- explanation-06: A cache stores copies of data so future requests can skip the slow step.
- explanation-06: If an application writes as often as it reads, or more often, the cache spends most of its time being refreshed.
- explanation-06: Constant cache refreshing erases the benefit of the cache and adds the risk of serving stale data.
- explanation-06: The read-to-write mix can be determined from logs or by adding simple counters.
- explanation-06: Fixing missing indexes, inefficient queries, or excessive round trips is often simpler and safer than adding a cache.
- explanation-08: A binary format only improves performance in proportion to the portion of time it replaces.
- explanation-08: If serialization is 5% of request time, a format three times faster saves about 3% of total time.
- explanation-08: If serialization is 40% of request time, the same format could save considerably more.
- explanation-08: Payload size can be measured by sampling real request and response bodies and noting their size in bytes.
- explanation-08: JSON payloads contain repeated keys and structure that a binary format could compress away.
- explanation-08: Protocol Buffers is a binary serialization format.
- explanation-08: MessagePack is a binary serialization format.
- summarization-01: There are no prior notes for this project.
- summarization-01: The release notes were written directly, without prior notes.
- summarization-01: The app starts up about 40% faster.
- summarization-02: The incident began at 09:14.
- summarization-02: The team paged on-call at 09:21, within 7 minutes of the incident start.
- summarization-02: Fast detection and recovery limited the impact of the incident.
- summarization-04: Clicking PDF export several times produces four identical "export failed" error banners.
- summarization-04: The issue was observed in Chrome by a colleague.
- summarization-04: The issue is not browser-specific.
- summarization-07: Two of the results are still guesses rather than confirmed findings.
- summarization-08: The progress bar issue appears to be a display problem rather than a real failure.
- summarization-08: The progress bar finding is tentative because only three people mentioned it.

### technical-simplified

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 27 | 20 | 0.741 | 23 | 3 |
| code-review-02 | 21 | 15 | 0.714 | 18 | 2 |
| code-review-03 | 15 | 10 | 0.667 | 18 | 6 |
| code-review-04 | 25 | 17 | 0.68 | 18 | 5 |
| code-review-05 | 37 | 28 | 0.757 | 25 | 2 |
| code-review-06 | 26 | 18 | 0.692 | 31 | 3 |
| code-review-07 | 39 | 29 | 0.744 | 28 | 8 |
| code-review-08 | 37 | 26 | 0.703 | 41 | 6 |
| debugging-01 | 6 | 6 | 1.0 | 7 | 0 |
| debugging-02 | 16 | 9 | 0.562 | 12 | 0 |
| debugging-03 | 9 | 9 | 1.0 | 10 | 0 |
| debugging-04 | 16 | 15 | 0.938 | 12 | 2 |
| debugging-05 | 20 | 16 | 0.8 | 13 | 0 |
| debugging-06 | 6 | 2 | 0.333 | 6 | 6 |
| debugging-08 | 36 | 20 | 0.556 | 26 | 11 |
| explanation-01 | 33 | 22 | 0.667 | 30 | 2 |
| explanation-02 | 28 | 21 | 0.75 | 24 | 2 |
| explanation-03 | 31 | 19 | 0.613 | 25 | 0 |
| explanation-04 | 45 | 22 | 0.489 | 21 | 0 |
| explanation-05 | 21 | 14 | 0.667 | 12 | 0 |
| explanation-06 | 15 | 11 | 0.733 | 20 | 2 |
| explanation-07 | 28 | 12 | 0.429 | 30 | 9 |
| explanation-08 | 11 | 8 | 0.727 | 18 | 10 |
| summarization-01 | 10 | 4 | 0.4 | 5 | 1 |
| summarization-02 | 15 | 7 | 0.467 | 8 | 0 |
| summarization-03 | 14 | 14 | 1.0 | 14 | 0 |
| summarization-04 | 13 | 11 | 0.846 | 12 | 2 |
| summarization-05 | 12 | 10 | 0.833 | 6 | 0 |
| summarization-06 | 13 | 13 | 1.0 | 12 | 0 |
| summarization-08 | 26 | 25 | 0.962 | 22 | 2 |

Median fraction: 0.72 over 30 scored pairs.

Median additions: 2.0 over 30 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python gotcha.
- code-review-01: The function has no duplicate-role handling.
- code-review-01: If `"member"` is already in `roles`, it gets appended again, creating duplicates.
- code-review-01: The proposed version copies `roles` with `list(roles) if roles else []`.
- code-review-01: The proposed version appends `"member"` only if it is not already in `roles`.
- code-review-01: The proposed version calls `db.insert({"name": name, "roles": roles})`.
- code-review-01: The proposed version avoids duplicate roles.
- code-review-02: The most critical bug is a race condition.
- code-review-02: Parsing bad responses as valid data can produce more confusing downstream errors.
- code-review-02: The code unnecessarily mixes `async`/`await` with `.then()` chains.
- code-review-02: Declaring a function `async` without using `await` defeats the purpose of `async` and signals confused intent.
- code-review-02: The code does not validate `data.name`.
- code-review-02: If the API response does not include a `name` field, `.toUpperCase()` will throw, even when the fetch succeeds.
- code-review-03: An attacker can pass a value like `'; DROP TABLE orders; --` to run arbitrary SQL.
- code-review-03: The `?` placeholder should be used instead of `%s` when using sqlite3.
- code-review-03: Using `SELECT *` is fragile if the table schema changes.
- code-review-03: The parameterization fix also sidesteps quoting bugs.
- code-review-03: In the current code, a name containing an apostrophe would break the query.
- code-review-04: A call to `reset()` can interleave with an in-flight `increment()`.
- code-review-04: A `reset()` interleaving with an in-flight `increment()` can produce a surprising result.
- code-review-04: If a reset happens after the read but before the write in `increment`, the increment silently undoes the reset by writing `1`.
- code-review-04: Nothing in the class is thread-safe, despite the class being used from multiple threads.
- code-review-04: If callers read `counter.value` directly from another thread while an increment is in progress, they may observe a stale or inconsistent value.
- code-review-04: In CPython, the GIL protects the single attribute read, making the unsafe direct read less severe.
- code-review-04: Safety of the direct attribute read is not guaranteed by the Python language.
- code-review-04: Reading between the `current = self.value` and `self.value = ...` steps in `increment` can return an intermediate value.
- code-review-05: The missing `cd` success check is the most dangerous bug in the script.
- code-review-05: If no `.log` files exist, the glob `*.log` expands to the literal string `*.log`, which is then treated as a filename.
- code-review-05: With default shell globbing, if no `.tmp` files exist, `rm` receives the literal string `*.tmp` and errors out.
- code-review-05: The `rm -rf *.tmp` no-match error is harmless in this script but sloppy and confusing.
- code-review-05: `set -u` would have caught the missing-argument problem immediately.
- code-review-05: The script does not restore the original working directory when it finishes.
- code-review-05: Failing to restore the original working directory matters if the script is sourced or chained with other commands.
- code-review-05: The suggested fix checks `[ -z "$BACKUP_DIR" ] || [ ! -d "$BACKUP_DIR" ]` and prints a usage message to stderr before exiting with status 1.
- code-review-05: The suggested fix uses `cd "$BACKUP_DIR" || exit 1`.
- code-review-06: The aliasing behavior for new nested dicts is asymmetric with the recurse-into-dicts path.
- code-review-06: Using `is None` instead of a falsiness check means `0`, `False`, and `""` are treated as real values.
- code-review-06: `dict(base)` always returns a plain `dict`, so a subclass type such as `OrderedDict` or a custom Mapping is lost.
- code-review-06: `isinstance(merged[key], dict)` does not match dict-like types that do not subclass `dict`, such as a custom Mapping.
- code-review-06: Dict-like values that are not `dict` subclasses get overwritten instead of merged, inconsistently with regular dicts.
- code-review-06: The function has no recursion guard, so self-referential structures would cause infinite recursion.
- code-review-06: Self-referential structures are unlikely in typical settings data.
- code-review-06: The intended behavior for `None`, for list merging, and for shallow aliasing cannot be inferred from the code alone.
- code-review-07: Errors lacking a `.status` property fail both the `=== 429` and `>= 500` checks.
- code-review-07: Errors without a `.status` property fall through to `return null`.
- code-review-07: TypeErrors and network failures are examples of errors that get swallowed into a null return.
- code-review-07: Bugs in `fn` itself, not just HTTP failures, are converted into a silent null.
- code-review-07: Swallowing non-HTTP errors is a debugging and observability hazard for callers.
- code-review-07: Errors are never logged or re-thrown by the helper.
- code-review-07: Failures in the helper are invisible to any monitoring around it.
- code-review-07: Swallowing non-HTTP errors into null is probably accidental.
- code-review-07: Whether existing callers rely on null as a sentinel should be determined before changing the helper.
- code-review-07: The null sentinel behavior is the part most likely to break silently if 'fixed'.
- code-review-08: The script contains no `if __name__ == "__main__":` block.
- code-review-08: The function `clean()` is never called anywhere in the script.
- code-review-08: If the scheduler runs the script via `python script.py`, the script does nothing.
- code-review-08: Whether another module imports the script and calls `clean()` is not visible in the code shown.
- code-review-08: The unconditional deletion of `tmp-`/`.part` files is the most dangerous line in the script.
- code-review-08: The script's own tmp-file deletion branch can race with a concurrent run of the same script.
- code-review-08: `os.path.getmtime` works on a directory.
- code-review-08: A broken or dangling symlink in `ROOT` causes `getmtime` to raise `FileNotFoundError`.
- code-review-08: The rationale for the `86400 * 45` and `500` constants is undocumented and nobody can recall it.
- code-review-08: The script's current behavior falls into one of three cases: inert, silently corrupting data, or working as intended.
- code-review-08: Determining how `clean()` is invoked and whether anything creates `tmp-*`/`*.part` files as working files decides which of those three cases applies.
- debugging-02: Class bodies execute in strict mode.
- debugging-02: In strict mode, a plain function call does not fall back to the global object for `this`.
- debugging-02: In strict mode, `this` in a plain function call stays `undefined`.
- debugging-02: `this.seconds += 1` where `this` is `undefined` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: In the non-strict case, `NaN` would be printed each tick.
- debugging-02: `setInterval(function () { ... }.bind(this), 1000)` is a valid fix.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is a valid fix.
- debugging-04: The actual encoding is usually UTF-8.
- debugging-05: A function's default value is stored on the function object itself.
- debugging-05: The failure looks flaky but is deterministic given the call order.
- debugging-05: The fix also protects callers who pass their own `tags` list from having it mutated as a side effect.
- debugging-05: Copying a caller-supplied `tags` list, e.g. `tags = list(tags) if tags is not None else list(DEFAULT_TAGS)`, avoids mutating the caller's list.
- debugging-06: The speaker will check whether the directory contains relevant code before answering.
- debugging-06: The command issued was `ls -la`.
- debugging-06: The command's stated purpose was to list files in the working directory.
- debugging-06: The working directory should be checked for relevant code before the question is answered.
- debugging-08: The observed pattern consists of steady percentage growth, no overnight recovery, presence without webhooks but faster growth with them, and a cache that has not changed.
- debugging-08: An unbounded per-order or per-webhook tracking structure is the explanation most consistent with all four observations.
- debugging-08: Examples of such tracking structures include idempotency keys, dedup sets, in-flight/retry state, and in-memory audit logs.
- debugging-08: An unbounded tracking structure shows unbounded object count growth over time even when the request rate is flat.
- debugging-08: Metrics clients often retain one time series per unique label combination forever.
- debugging-08: High-cardinality labels match the campaign correlation because campaigns produce more unique IDs and campaign tags.
- debugging-08: One check is to query the metrics backend for active series or cardinality count over the same window as the memory graph.
- debugging-08: If metric cardinality climbs monotonically alongside RSS, high-cardinality labels are the cause.
- debugging-08: A cache eviction leak, where evicted entries are kept alive elsewhere, is a possible cause.
- debugging-08: A secondary index, listener, or closure can still reference an object after the cache evicts it.
- debugging-08: A steady cache bound caps only cache-visible memory, not total retained memory.
- debugging-08: One check is to pick evicted product IDs in a heap dump and trace their GC roots to see if anything outside the cache still retains them.
- debugging-08: Allocator or runtime fragmentation, rather than a true leak, is a possible cause.
- debugging-08: Fragmentation would explain gradual RSS growth that does not return to baseline, independent of application logic.
- debugging-08: If live heap is flat while RSS climbs, the cause is fragmentation rather than retained objects.
- debugging-08: Fragmentation requires a different fix than retained objects.
- explanation-01: An example of computing an index is hash("apple") % array_size.
- explanation-01: Separate chaining handles unlimited collisions gracefully.
- explanation-01: Deletion under separate chaining is easy because the entry is just removed from the list.
- explanation-01: In the worst case, with many collisions in one slot, separate chaining degrades to O(n) list traversal.
- explanation-01: Linear probing tries index+1, then index+2, and so on.
- explanation-01: Quadratic probing tries index+1², then index+2², and so on.
- explanation-01: Double hashing uses a second hash function to compute the step size.
- explanation-01: Open addressing performance degrades sharply as the table fills up due to clustering.
- explanation-01: Open addressing requires resizing/rehashing earlier, typically once the load factor exceeds about 0.7.
- explanation-01: Python's dict uses an open addressing variant.
- explanation-01: Rust's HashMap uses an open addressing variant.
- explanation-02: An optimistic-locking stock update can be written as: UPDATE products SET stock = stock - 1, version = version + 1 WHERE id = 42 AND version = 7.
- explanation-02: A CMS article edit is an example workload suited to optimistic locking.
- explanation-02: A shopping cart is an example workload suited to optimistic locking.
- explanation-02: Postgres and MySQL support pessimistic locking via SELECT ... FOR UPDATE.
- explanation-02: A pessimistic locking example is: BEGIN; SELECT stock FROM products WHERE id = 42 FOR UPDATE; UPDATE products SET stock = stock - 1 WHERE id = 42; COMMIT;
- explanation-02: Seat and inventory reservation systems are examples of workloads suited to pessimistic locking.
- explanation-02: In reservation systems, two users grabbing the last item is unacceptable.
- explanation-03: If a sender sends data as fast as the receiver's advertised window allows, it can overwhelm a router queue.
- explanation-03: Dropped packets cause wasted bandwidth.
- explanation-03: Slow start is also used after certain recovery events.
- explanation-03: The congestion window is separate from the receiver's advertised window.
- explanation-03: The sender's actual sending rate is limited by the smaller of the congestion window and the receiver's advertised window.
- explanation-03: The initial cwnd was historically 1 segment.
- explanation-03: The initial cwnd is now typically 2-10 segments.
- explanation-03: RFC 6928 raised the initial congestion window value to improve performance for short flows.
- explanation-03: The congestion avoidance phase is more conservative than slow start and uses linear growth.
- explanation-03: When packet loss is detected, ssthresh is lowered and cwnd is reset or cut back.
- explanation-03: The name 'slow start' is slightly misleading because the growth is exponential and ramps up quickly.
- explanation-03: The name 'slow start' refers to starting from a small window rather than assuming the full receiver-advertised window can be used immediately.
- explanation-04: A process has its own file descriptors.
- explanation-04: A process has its own OS-level resources.
- explanation-04: All threads in a process share the same resources.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own instruction pointer.
- explanation-04: Threads are cheaper to create than processes.
- explanation-04: A crashed process can be restarted independently.
- explanation-04: nginx uses multiple processes.
- explanation-04: Chrome uses a per-tab process model.
- explanation-04: In a multi-process browser model, a bad tab does not kill the whole application.
- explanation-04: For I/O-bound work, threads or async are fine.
- explanation-04: Threads release the GIL while waiting on I/O.
- explanation-04: Processes can run under different privilege levels.
- explanation-04: Multiple processes are preferable when components need independent lifecycle management.
- explanation-04: Separate processes allow components to be started, stopped, restarted, or scaled independently using OS-level tools.
- explanation-04: OS-level tools for managing processes include kill, restart, and resource limits via cgroups.
- explanation-04: Using separate processes avoids coordinating shutdown logic inside one program.
- explanation-04: Threads have lower creation cost than processes.
- explanation-04: Threads have faster context switches than processes.
- explanation-04: Processes win when isolation is needed: fault tolerance, true CPU parallelism around language-level locks, security boundaries, or independent lifecycle.
- explanation-04: Processes have higher memory overhead than threads.
- explanation-04: Inter-process communication is slower and more explicit than thread communication.
- explanation-04: Inter-process communication mechanisms include pipes, sockets, and shared memory segments.
- explanation-05: A garbage collector walks references starting from roots.
- explanation-05: Roots include global variables, stack frames, and active closures.
- explanation-05: A garbage collector cannot know the programmer's intent.
- explanation-05: A subscribed object and anything it closes over stay reachable indefinitely.
- explanation-05: Eviction mechanisms include TTL, LRU, and a size cap.
- explanation-05: Closures capturing large outer scopes longer than needed is a frequent cause of memory leaks.
- explanation-05: Static or global collections that outlive the logical lifetime of the objects placed in them are a frequent cause of memory leaks.
- explanation-06: A cache only helps if the same data is requested repeatedly.
- explanation-06: Possible alternative causes of the performance problem include slow queries, network latency, N+1 calls, and serialization.
- explanation-06: If every read requests different data, a cache provides little benefit.
- explanation-06: A cache is another system that must be operated.
- explanation-07: Sharding is a one-way architectural decision.
- explanation-07: Sharding only helps when the constraint is write throughput, storage, or single-node CPU/IO that vertical scaling cannot fix.
- explanation-07: If the bottleneck is bad queries, missing indexes, or lock contention, sharding will not fix it.
- explanation-07: Sharding replicates query, index, and lock-contention problems across all nodes.
- explanation-07: Current CPU, IO, and connection utilization determine how much headroom remains on existing hardware.
- explanation-07: At 20% utilization on a mid-size instance, there is likely 5-10x runway before sharding is urgent.
- explanation-07: After sharding, every schema change, migration, and query must be shard-aware.
- explanation-07: Building routing and rebalancing infrastructure can take months.
- explanation-07: Premature sharding causes a permanent drop in team velocity.
- explanation-07: Waiting too long is usually still cheaper than premature sharding.
- explanation-07: Read replicas, table partitioning, connection pooling, and vertical scaling can mitigate the interim before sharding.
- explanation-07: Postgres native table partitioning operates within a single instance and is not the same as sharding.
- explanation-07: Read replicas, partitioning, connection pooling, and vertical scaling are reversible, incremental steps.
- explanation-07: Postgres native partitioning by date or tenant addresses table size and vacuum/index bloat concerns.
- explanation-07: Native partitioning provides much of the operational benefit of sharding without cross-node complexity.
- explanation-07: Sharding should be revisited only when utilization numbers show vertical scaling, partitioning, and read replicas will not suffice for the next 12-18 months.
- explanation-08: Network, database, and business logic usually dominate request time.
- explanation-08: Profiling results indicate whether the migration is worth its cost.
- explanation-08: The migration cost includes client compatibility, debuggability, and tooling.
- summarization-01: The app now starts up to 40% faster.
- summarization-01: Hovering over any toolbar button displays that button's keyboard shortcut.
- summarization-01: Internal build tooling changes were omitted from these release notes.
- summarization-01: Module refactoring changes were omitted from these release notes.
- summarization-01: Telemetry batching changes were omitted from these release notes.
- summarization-01: The omitted changes have no user-facing effect.
- summarization-02: A production deploy copied a staging config template into production.
- summarization-02: The small pool size of 5 was intentional for staging.
- summarization-02: The reduced pool size exhausted database connections under load.
- summarization-02: The incident caused an approximately 12% error rate for checkout.
- summarization-02: The incident was detected at 09:14.
- summarization-02: An on-call engineer was paged at 09:21.
- summarization-02: The change was rolled back at 09:48.
- summarization-02: The impact lasted approximately 34 minutes.
- summarization-04: Clicking the PDF export button multiple times produces multiple "export failed" error banners, one per click.
- summarization-04: The bug was reproduced on the latest version of Firefox.
- summarization-05: Ada is assigned to run the payments database migration dry run.
- summarization-05: Ada is assigned to check with the mobile team's lead about whether the mobile team was informed of the API deprecation.
- summarization-08: The progress bar finding is rated FIRM, with the cause tentative.

Added facts (styled only):

- code-review-01: The listed problems are given in order of importance.
- code-review-01: The mutable default argument is the most important problem in the code.
- code-review-01: The suggested fix builds `new_roles = roles + ["member"]` instead of appending to the caller's list.
- code-review-02: The `async` keyword has no effect on this function.
- code-review-02: A failed network request results in an unhandled promise rejection.
- code-review-03: `%s`, `?`, and `:name` are placeholder syntaxes used by different database drivers.
- code-review-03: The query has no result limit.
- code-review-03: A broad match on customer_name and status can return many rows.
- code-review-03: A LIMIT clause or pagination would address the unbounded result set.
- code-review-03: Example allowed status values are "open", "shipped", and "cancelled".
- code-review-03: An invalid status value causes the function to return an empty result with no error message.
- code-review-04: In the two-thread example, Thread A reads `value = 0`.
- code-review-04: In the two-thread example, Thread B also reads `value = 0`.
- code-review-04: In the two-thread example, Thread A writes `value = 1`.
- code-review-04: In the two-thread example, Thread B writes `value = 1`.
- code-review-04: In that example the resulting count is 1 even though two increments occurred.
- code-review-05: Without `--`, a filename beginning with a dash (such as `-rf`) can be treated as an option instead of a filename.
- code-review-05: The suggested rewrite quotes variable expansions and passes `--` to cd, rm, and gzip.
- code-review-06: The reviewer found seven problems in the function.
- code-review-06: Two of the seven problems look like deliberate design choices.
- code-review-06: The remaining five problems are likely bugs that need a fix.
- code-review-07: When retries are exhausted, the caller receives no signal of failure.
- code-review-07: If fn throws a value with no status field, such as null or a plain Error, the expression err.status === 429 can throw a TypeError.
- code-review-07: A TypeError thrown by err.status === 429 escapes the try/catch block and the retry loop.
- code-review-07: Such an escaping TypeError turns a controlled retry into an unhandled rejection.
- code-review-07: The backoff delay has no upper limit.
- code-review-07: The default value of the attempts parameter is 3.
- code-review-07: With the default attempts value of 3, the backoff delays stay small.
- code-review-07: With a large attempts value passed by a caller, the final wait can grow very long.
- code-review-08: removed is a single counter shared by both branches.
- code-review-08: A run can remove 500 tmp-/.part files first and then skip every old file, even if only a few old files exist.
- code-review-08: The same directory can give different results on different runs.
- code-review-08: The script has no limit on directory traversal depth.
- code-review-08: A symlink pointing outside ROOT still gets its target's mtime checked, and the link itself gets removed.
- code-review-08: The symlink issue is a minor edge case but worth noting because the script deletes data.
- debugging-04: The byte 0xc3 occurs at position 512 in the file.
- debugging-04: chardet is a library that can detect a file's encoding.
- debugging-06: The speaker is going to check memory for prior context before answering.
- debugging-06: There may be prior context stored about this export job.
- debugging-06: The memory index file is named MEMORY.md.
- debugging-06: The memory index is located at /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-weclp6d3/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-121asz23/memory/MEMORY.md.
- debugging-06: A bash command is being run to read that memory index file.
- debugging-06: The command prints NONE if the memory index file cannot be read.
- debugging-08: The four observations point to four separate but related causes.
- debugging-08: The four causes should be checked in order from cheapest to most direct.
- debugging-08: One possible cause is an off-heap or native memory leak.
- debugging-08: Both a true heap leak and an off-heap leak produce the pattern of memory not returning to baseline.
- debugging-08: A native memory tracker for the runtime can be used to investigate off-heap memory.
- debugging-08: On Linux, /proc/[pid]/smaps can be read to investigate native memory.
- debugging-08: The cache entry count and estimated byte size should be logged as two separate metrics, once per hour.
- debugging-08: A size metric should be added for each candidate structure and compared against the daily order count.
- debugging-08: The growth rate per order, not per day, should be compared between the canary and a normal instance.
- debugging-08: If the normal instance grows faster per order than the canary, the webhook path is the added cause.
- debugging-08: A heap dump taken before and after a quiet night shows directly which structure retains memory.
- explanation-01: Most general-purpose hash maps use chaining.
- explanation-01: Some C++ hash map implementations use open addressing.
- explanation-02: If the save fails under optimistic locking, the application must retry.
- explanation-02: A product catalog is an example of a system with many reads and few write conflicts.
- explanation-06: A cache stores data in fast memory.
- explanation-06: A cache can add extra work on each write to keep the cache correct.
- explanation-07: If indexes and caching cannot keep queries fast, sharding is required.
- explanation-07: Growth rate can be measured over the next few months and projected forward.
- explanation-07: Sharding adds new failure points.
- explanation-07: Simpler alternatives to sharding include adding read replicas, using connection pooling, adding indexes, and archiving old data.
- explanation-07: Added complexity slows down the team and adds bugs.
- explanation-07: Sharding requires choosing a shard key early.
- explanation-07: A wrong shard key choice is hard to fix later.
- explanation-07: A late shard key choice can still be wrong, and fixing it puts more data at risk.
- explanation-07: Waiting too long makes migration take longer because more data must be moved.
- explanation-08: If serialization uses ten percent of a request, a fifty percent gain in serialization cuts total request time by about five percent rather than fifty percent.
- explanation-08: Average and maximum payload size in bytes should be measured first.
- explanation-08: CPU use during encoding and decoding should be measured.
- explanation-08: Network time compared to processing time should be measured.
- explanation-08: The suggested method starts with picking five to ten real requests that span a range of payload sizes.
- explanation-08: Encode time, decode time, and payload size should be measured for each request using the current JSON format.
- explanation-08: A small prototype using the proposed binary format should be built.
- explanation-08: Protocol Buffers and MessagePack are examples of binary formats.
- explanation-08: The same three measurements should be taken with the prototype.
- explanation-08: Total request time, not only serialization time, should be compared.
- summarization-01: The app now starts about 40% faster.
- summarization-04: Clicking the PDF export option for the March report starts no export.
- summarization-04: Clicking the PDF export button several more times causes four "export failed" error banners to appear at once.
- summarization-08: The finding that the progress bar causes users to abandon large-file imports is labeled tentative but needing action.
- summarization-08: The sample is small, so the exact cause of the abandonment should be treated as tentative.

## Hedging survival

The judge lists the claims that the unstyled answer presents with uncertainty, then judges each claim in the styled answer: hedged (the uncertainty survives in some form), certain (the claim survives but reads as a fact — the failure this check targets), or absent (the claim is gone, a completeness loss). Survival is hedged / (hedged + certain). The claims that became certain appear verbatim below the table.

### clarity-flow

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 0 | 0 | 1 | n/a |
| code-review-02 | 2 | 0 | 2 | 0 | 0.0 |
| code-review-03 | 0 | 0 | 0 | 0 | n/a |
| code-review-04 | 1 | 0 | 0 | 1 | n/a |
| code-review-05 | 0 | 0 | 0 | 0 | n/a |
| code-review-06 | 8 | 6 | 1 | 1 | 0.857 |
| code-review-07 | 11 | 6 | 3 | 2 | 0.667 |
| code-review-08 | 6 | 3 | 0 | 3 | 1.0 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 1 | 0 | 1 | 0 | 0.0 |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 3 | 0 | 0 | 1.0 |
| debugging-05 | 1 | 0 | 1 | 0 | 0.0 |
| debugging-06 | 0 | 0 | 0 | 0 | n/a |
| debugging-07 | 9 | 5 | 1 | 3 | 0.833 |
| debugging-08 | 8 | 3 | 0 | 5 | 1.0 |
| explanation-01 | 2 | 0 | 2 | 0 | 0.0 |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 0 | 0 | 0 | 0 | n/a |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 2 | 2 | 0 | 0 | 1.0 |
| explanation-07 | 5 | 0 | 2 | 3 | 0.0 |
| explanation-08 | 4 | 3 | 1 | 0 | 0.75 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 1 | 0 | 1 | 0 | 0.0 |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 5 | 5 | 0 | 0 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 76 over 32 judged pairs: 42 hedged, 15 certain, 19 absent.

Median survival: 0.833 over 17 scored pairs.

Claims that became certain:

- code-review-02: Because of the missing await, `profile.name` will throw `TypeError: Cannot read properties of undefined (reading 'name')` on virtually every call.
- code-review-02: Bad responses parsed as if they were valid data may potentially produce more confusing downstream errors.
- code-review-06: If `base` isn't dict-like, `dict(base)` may raise unhelpful errors.
- code-review-07: The lack of jitter is a known best-practice gap, not something the author would assume is deliberate.
- code-review-07: Probably deliberate: treating 429 and 5xx as retryable, treating everything else as non-retryable, and backing off on 429.
- code-review-07: Whether existing callers rely on `null` as a sentinel is the part most likely to break silently if "fixed."
- debugging-02: The behavior of `undefined + 1 = NaN` being printed each tick (in a non-strict-mode context) is likely the behavior you're recalling.
- debugging-05: When running the full suite, by the time this test runs, DEFAULT_TAGS might already be ["draft", "post"] (if any earlier test also called make_post without tags and appended "post" to the same list first), so appending again would give ["draft", "post", "post"] and the assertion would fail.
- debugging-07: pytest-xdist should typically get its own DB/schema per worker.
- explanation-01: Deletion in open addressing usually needs a "tombstone" marker (since you can't just clear a slot without breaking the probe chain).
- explanation-01: You typically need to resize/rehash an open-addressed table once the load factor exceeds roughly 0.7.
- explanation-07: Waiting too long risks an emergency migration under load, with less room to test/rollback safely.
- explanation-07: Postgres native partitioning (by date/tenant) may get much of the operational benefit without cross-node complexity, if table size or vacuum/index bloat is the concern.
- explanation-08: Profiling will likely tell you whether this is worth the migration cost (client compatibility, debuggability, tooling) or a solution in search of a problem
- summarization-04: Likely not browser-specific (the PDF export failure was reproduced on Firefox latest and Chrome, on two different machines)

### classic-concise

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-02 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-03 | 0 | 0 | 0 | 0 | n/a |
| code-review-04 | 1 | 1 | 0 | 0 | 1.0 |
| code-review-05 | 0 | 0 | 0 | 0 | n/a |
| code-review-06 | 8 | 2 | 2 | 4 | 0.5 |
| code-review-07 | 11 | 7 | 1 | 3 | 0.875 |
| code-review-08 | 6 | 3 | 0 | 3 | 1.0 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 1 | 0 | 1 | 0 | 0.0 |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 2 | 1 | 0 | 0.667 |
| debugging-05 | 1 | 0 | 1 | 0 | 0.0 |
| debugging-06 | 0 | 0 | 0 | 0 | n/a |
| debugging-07 | 9 | 4 | 1 | 4 | 0.8 |
| debugging-08 | 8 | 5 | 2 | 1 | 0.714 |
| explanation-01 | 2 | 2 | 0 | 0 | 1.0 |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 0 | 0 | 0 | 0 | n/a |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 2 | 1 | 1 | 0 | 0.5 |
| explanation-07 | 5 | 1 | 1 | 3 | 0.5 |
| explanation-08 | 4 | 2 | 1 | 1 | 0.667 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 1 | 0 | 0 | 1 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 5 | 4 | 0 | 1 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 76 over 32 judged pairs: 40 hedged, 14 certain, 22 absent.

Median survival: 0.691 over 18 scored pairs.

Claims that became certain:

- code-review-01: Bare `except:` should at minimum catch a specific exception type and probably log it.
- code-review-02: Because of the missing await, `profile.name` will throw `TypeError: Cannot read properties of undefined (reading 'name')` on virtually every call.
- code-review-06: The issues listed in the first section (the type-mismatch crash and the shallow-copy aliasing) are unlikely to be deliberate.
- code-review-06: Bugs #1 and #2 are almost certainly unintended and should be fixed.
- code-review-07: Probably deliberate: treating 429 and 5xx as retryable, treating everything else as non-retryable, and backing off on 429.
- debugging-02: The behavior of `undefined + 1 = NaN` being printed each tick (in a non-strict-mode context) is likely the behavior you're recalling.
- debugging-04: The non-ASCII byte 0xc3 in the file is likely part of a UTF-8 multi-byte sequence, such as an accented character.
- debugging-05: When running the full suite, by the time this test runs, DEFAULT_TAGS might already be ["draft", "post"] (if any earlier test also called make_post without tags and appended "post" to the same list first), so appending again would give ["draft", "post", "post"] and the assertion would fail.
- debugging-07: If the test never fails alone under `-n 4` but fails when run with the full suite, that strongly implicates shared state/fixtures rather than an internal race.
- debugging-08: The pattern of evidence probably points away from a single "leaky cache" explanation and toward something unbounded driven by order volume, with webhooks likely acting as an accelerant rather than the sole cause.
- debugging-08: If live heap is flat while RSS climbs, the problem is probably fragmentation rather than retained objects.
- explanation-06: Adding a cache before profiling risks solving the wrong problem while introducing new ones
- explanation-07: Postgres native partitioning (by date/tenant) may get much of the operational benefit without cross-node complexity, if table size or vacuum/index bloat is the concern.
- explanation-08: Profiling will likely tell you whether this is worth the migration cost (client compatibility, debuggability, tooling) or a solution in search of a problem

### developer-docs

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 0 | 0 | 1 | n/a |
| code-review-02 | 2 | 1 | 1 | 0 | 0.5 |
| code-review-03 | 0 | 0 | 0 | 0 | n/a |
| code-review-04 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-05 | 0 | 0 | 0 | 0 | n/a |
| code-review-06 | 8 | 3 | 0 | 5 | 1.0 |
| code-review-07 | 11 | 8 | 0 | 3 | 1.0 |
| code-review-08 | 6 | 3 | 0 | 3 | 1.0 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 1 | 0 | 1 | 0 | 0.0 |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 2 | 1 | 0 | 0.667 |
| debugging-05 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-06 | 0 | 0 | 0 | 0 | n/a |
| debugging-07 | 9 | 4 | 1 | 4 | 0.8 |
| debugging-08 | 8 | 4 | 2 | 2 | 0.667 |
| explanation-01 | 2 | 0 | 1 | 1 | 0.0 |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 0 | 0 | 0 | 0 | n/a |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 2 | 2 | 0 | 0 | 1.0 |
| explanation-07 | 5 | 2 | 0 | 3 | 1.0 |
| explanation-08 | 4 | 1 | 1 | 2 | 0.5 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 1 | 0 | 0 | 1 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 5 | 4 | 0 | 1 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 76 over 32 judged pairs: 41 hedged, 9 certain, 26 absent.

Median survival: 1.0 over 17 scored pairs.

Claims that became certain:

- code-review-02: Because of the missing await, `profile.name` will throw `TypeError: Cannot read properties of undefined (reading 'name')` on virtually every call.
- code-review-04: If callers read `counter.value` directly from another thread while an increment is in progress, they may observe a stale or inconsistent value.
- debugging-02: The behavior of `undefined + 1 = NaN` being printed each tick (in a non-strict-mode context) is likely the behavior you're recalling.
- debugging-04: A codec that can handle the file's actual encoding is usually UTF-8.
- debugging-07: The listed causes are the most plausible ones, roughly ordered by likelihood.
- debugging-08: The pattern of evidence probably points away from a single "leaky cache" explanation and toward something unbounded driven by order volume, with webhooks likely acting as an accelerant rather than the sole cause.
- debugging-08: If live heap is flat while RSS climbs, the problem is probably fragmentation rather than retained objects.
- explanation-01: Deletion in open addressing usually needs a "tombstone" marker (since you can't just clear a slot without breaking the probe chain).
- explanation-08: Profiling will likely tell you whether this is worth the migration cost (client compatibility, debuggability, tooling) or a solution in search of a problem

### plain-language

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 0 | 0 | 1 | n/a |
| code-review-02 | 2 | 1 | 1 | 0 | 0.5 |
| code-review-03 | 0 | 0 | 0 | 0 | n/a |
| code-review-04 | 1 | 0 | 0 | 1 | n/a |
| code-review-05 | 0 | 0 | 0 | 0 | n/a |
| code-review-06 | 8 | 4 | 1 | 3 | 0.8 |
| code-review-07 | 11 | 5 | 1 | 5 | 0.833 |
| code-review-08 | 6 | 5 | 0 | 1 | 1.0 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 1 | 0 | 1 | 0 | 0.0 |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 3 | 0 | 0 | 1.0 |
| debugging-05 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-06 | 0 | 0 | 0 | 0 | n/a |
| debugging-07 | 9 | 0 | 0 | 9 | n/a |
| debugging-08 | 8 | 3 | 2 | 3 | 0.6 |
| explanation-01 | 2 | 0 | 1 | 1 | 0.0 |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 0 | 0 | 0 | 0 | n/a |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 2 | 2 | 0 | 0 | 1.0 |
| explanation-07 | 5 | 0 | 0 | 5 | n/a |
| explanation-08 | 4 | 2 | 1 | 1 | 0.667 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 1 | 0 | 1 | 0 | 0.0 |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 5 | 4 | 0 | 1 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 76 over 32 judged pairs: 36 hedged, 9 certain, 31 absent.

Median survival: 0.833 over 15 scored pairs.

Claims that became certain:

- code-review-02: Because of the missing await, `profile.name` will throw `TypeError: Cannot read properties of undefined (reading 'name')` on virtually every call.
- code-review-06: If `base` isn't dict-like, `dict(base)` may raise unhelpful errors.
- code-review-07: The lack of jitter is a known best-practice gap, not something the author would assume is deliberate.
- debugging-02: The behavior of `undefined + 1 = NaN` being printed each tick (in a non-strict-mode context) is likely the behavior you're recalling.
- debugging-08: The pattern of evidence probably points away from a single "leaky cache" explanation and toward something unbounded driven by order volume, with webhooks likely acting as an accelerant rather than the sole cause.
- debugging-08: If active series/cardinality count climbs monotonically alongside RSS over the same window, that is likely the cause.
- explanation-01: Deletion in open addressing usually needs a "tombstone" marker (since you can't just clear a slot without breaking the probe chain).
- explanation-08: Profiling will likely tell you whether this is worth the migration cost (client compatibility, debuggability, tooling) or a solution in search of a problem
- summarization-04: Likely not browser-specific (the PDF export failure was reproduced on Firefox latest and Chrome, on two different machines)

### technical-simplified

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-02 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-03 | 0 | 0 | 0 | 0 | n/a |
| code-review-04 | 1 | 0 | 0 | 1 | n/a |
| code-review-05 | 0 | 0 | 0 | 0 | n/a |
| code-review-06 | 8 | 4 | 1 | 3 | 0.8 |
| code-review-07 | 11 | 7 | 1 | 3 | 0.875 |
| code-review-08 | 6 | 4 | 0 | 2 | 1.0 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 1 | 0 | 1 | 0 | 0.0 |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 2 | 1 | 0 | 0.667 |
| debugging-05 | 1 | 0 | 1 | 0 | 0.0 |
| debugging-06 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 8 | 1 | 3 | 4 | 0.25 |
| explanation-01 | 2 | 0 | 1 | 1 | 0.0 |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 0 | 0 | 0 | 0 | n/a |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 2 | 2 | 0 | 0 | 1.0 |
| explanation-07 | 5 | 0 | 1 | 4 | 0.0 |
| explanation-08 | 4 | 2 | 1 | 1 | 0.667 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 1 | 1 | 0 | 0 | 1.0 |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 5 | 4 | 0 | 1 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 64 over 30 judged pairs: 30 hedged, 13 certain, 21 absent.

Median survival: 0.667 over 16 scored pairs.

Claims that became certain:

- code-review-01: Bare `except:` should at minimum catch a specific exception type and probably log it.
- code-review-02: Because of the missing await, `profile.name` will throw `TypeError: Cannot read properties of undefined (reading 'name')` on virtually every call.
- code-review-06: Swallowing the KeyError via `merged.pop(key, None)` could hide bugs in caller code, since a typo'd key meant to delete something would fail silently.
- code-review-07: Probably deliberate: treating 429 and 5xx as retryable, treating everything else as non-retryable, and backing off on 429.
- debugging-02: The behavior of `undefined + 1 = NaN` being printed each tick (in a non-strict-mode context) is likely the behavior you're recalling.
- debugging-04: A codec that can handle the file's actual encoding is usually UTF-8.
- debugging-05: When running the full suite, by the time this test runs, DEFAULT_TAGS might already be ["draft", "post"] (if any earlier test also called make_post without tags and appended "post" to the same list first), so appending again would give ["draft", "post", "post"] and the assertion would fail.
- debugging-08: The pattern of evidence probably points away from a single "leaky cache" explanation and toward something unbounded driven by order volume, with webhooks likely acting as an accelerant rather than the sole cause.
- debugging-08: An unbounded per-order/per-webhook tracking structure (idempotency keys, dedup set, in-flight/retry state, in-memory audit log) is the most likely cause, as it appears most consistent with all four observations.
- debugging-08: A cache bounded by entry count rather than bytes may be the cause — if campaigns increase average product payload size, a fixed-count cache could hold more bytes without violating its bound, so the unchanged bound doesn't rule this out.
- explanation-01: Deletion in open addressing usually needs a "tombstone" marker (since you can't just clear a slot without breaking the probe chain).
- explanation-07: Waiting too long risks an emergency migration under load, with less room to test/rollback safely.
- explanation-08: Profiling will likely tell you whether this is worth the migration cost (client compatibility, debuggability, tooling) or a solution in search of a problem

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 630, measured: 630.
Mean duration: 13358 ms. Mean wall: 26158 ms. Mean startup: 12799 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 630, measured: 630.
Input tokens: 1260 uncached, 1191889 cache write, 1291337 cache read. Output tokens: 668130.
Cache-read share: 0.52.

## Warnings

- technical-simplified/summarization-07: the pair failed the gate, excluded
- technical-simplified/debugging-07: the pair failed the gate, excluded
