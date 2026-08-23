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

Judge: opus. Judged on 2026-08-22T12:09:29+00:00.

## Completeness (fact survival)

The judge lists the facts of the unstyled answer, then checks each fact against the styled answer. The fraction is the share of the facts that survive. The judge also lists the facts of the styled answer and checks each fact against the unstyled answer: a styled fact that the unstyled answer does not state is an addition. The lost facts and the added facts appear verbatim below the table.

### actionable-clarity

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 28 | 18 | 0.643 | 29 | 6 |
| code-review-02 | 19 | 18 | 0.947 | 26 | 3 |
| code-review-03 | 24 | 21 | 0.875 | 21 | 5 |
| code-review-04 | 26 | 19 | 0.731 | 18 | 5 |
| code-review-05 | 27 | 21 | 0.778 | 27 | 4 |
| code-review-06 | 38 | 21 | 0.553 | 31 | 13 |
| code-review-07 | 30 | 21 | 0.7 | 30 | 10 |
| code-review-08 | 34 | 27 | 0.794 | 40 | 11 |
| debugging-01 | 7 | 7 | 1.0 | 8 | 2 |
| debugging-02 | 19 | 11 | 0.579 | 11 | 0 |
| debugging-03 | 10 | 8 | 0.8 | 10 | 0 |
| debugging-04 | 15 | 10 | 0.667 | 13 | 1 |
| debugging-05 | 17 | 16 | 0.941 | 15 | 0 |
| debugging-06 | 4 | 1 | 0.25 | 0 | 0 |
| debugging-07 | 0 | 0 | n/a | 41 | 41 |
| debugging-08 | 28 | 10 | 0.357 | 41 | 23 |
| explanation-01 | 39 | 29 | 0.744 | 30 | 3 |
| explanation-02 | 24 | 21 | 0.875 | 30 | 7 |
| explanation-03 | 35 | 26 | 0.743 | 30 | 4 |
| explanation-04 | 39 | 31 | 0.795 | 36 | 2 |
| explanation-05 | 18 | 17 | 0.944 | 13 | 0 |
| explanation-06 | 21 | 17 | 0.81 | 25 | 6 |
| explanation-07 | 26 | 18 | 0.692 | 24 | 7 |
| explanation-08 | 18 | 15 | 0.833 | 21 | 8 |
| summarization-01 | 5 | 5 | 1.0 | 7 | 1 |
| summarization-02 | 12 | 11 | 0.917 | 17 | 6 |
| summarization-03 | 13 | 12 | 0.923 | 11 | 0 |
| summarization-04 | 13 | 12 | 0.923 | 18 | 3 |
| summarization-05 | 9 | 9 | 1.0 | 14 | 2 |
| summarization-06 | 12 | 12 | 1.0 | 13 | 0 |
| summarization-07 | 14 | 12 | 0.857 | 14 | 3 |
| summarization-08 | 20 | 18 | 0.9 | 22 | 2 |

Median fraction: 0.81 over 31 scored pairs.

Median additions: 3.0 over 32 scored pairs.

Lost facts:

- code-review-01: When `roles` is passed explicitly, `.append("member")` mutates the caller's original list in place.
- code-review-01: Mutating the caller's list is a surprising side effect that can cause bugs elsewhere in the caller's code.
- code-review-01: Duplicate roles aren't prevented.
- code-review-01: Calling the function with `roles=["member"]` explicitly produces `["member", "member"]`.
- code-review-01: The function has no docstring and no type hints.
- code-review-01: Missing type hints is a minor issue.
- code-review-01: Type hints of `name: str`, `roles: list[str] | None`, and a type for `db` would clarify the function's contract.
- code-review-01: A safer rewrite uses `roles=None` as the default and raises `ValueError` when `name` or `db` is missing.
- code-review-01: The safer rewrite copies `roles` with `list(roles)` and appends `"member"` only if it is not already present.
- code-review-01: The rewrite drops the silent failure mode by letting real errors propagate.
- code-review-02: The fixed version awaits `fetch` with an encoded `userId`, throws an Error including `res.status` when `!res.ok`, awaits `res.json()`, throws an Error when the response is missing `name`, and returns `data.name.toUpperCase()`.
- code-review-03: pymysql uses `%s` as its parameter placeholder.
- code-review-03: The function does not check that `status` is one of the expected valid values before querying.
- code-review-03: `fetchall` can raise an exception, for example on a bad connection or a database error.
- code-review-04: Python's GIL guarantees that each individual bytecode operation is atomic.
- code-review-04: Python's GIL does not guarantee atomicity of a multi-step read-modify-write sequence.
- code-review-04: A single assignment is atomic in CPython.
- code-review-04: `reset` by itself will not corrupt the counter's state.
- code-review-04: An example of the reset/increment race is resetting to 0 and then a stale increment writing 1.
- code-review-04: The class has no thread-safety documentation or contract.
- code-review-04: A caller reading the code has no way to know the class is unsafe under concurrent use.
- code-review-05: `cd "$BACKUP_DIR" || exit 1` is the correct form.
- code-review-05: Some shells leave an unmatched glob as the literal string `*.tmp`.
- code-review-05: `rm -rf` given a literal unmatched pattern typically errors out harmlessly in POSIX sh.
- code-review-05: Bash has a `nullglob` option affecting unmatched glob behavior.
- code-review-05: The loop body may run once with the literal string `*.log` as $f, causing gzip to fail with a confusing error.
- code-review-05: `${1:?Usage: ...}` makes the first argument required.
- code-review-06: Resolving the `None`-means-delete ambiguity requires a sentinel such as a `DELETE` marker if both behaviors are needed.
- code-review-06: `merged.pop(key, None)` silently does nothing if the key is not present in `base`.
- code-review-06: Silently no-oping on a missing key can hide a typo, such as a misspelled key intended to delete something.
- code-review-06: If `base[key]` is a dict and `override[key]` is not a dict, the `elif` branch fails and control falls to the `else` branch.
- code-review-06: In that case the entire nested dict is replaced by the scalar value.
- code-review-06: No validation or error is raised for either type-mismatch case.
- code-review-06: The type-mismatch behavior could mask a configuration mistake.
- code-review-06: Recursion depth follows the depth of `override`'s nested dicts.
- code-review-06: Some config systems expect list concatenation or index-wise merging.
- code-review-06: There is no check that keys are hashable or strings.
- code-review-06: `isinstance(merged[key], dict)` also matches dict subclasses.
- code-review-06: Recursing into an `OrderedDict` or custom dict subclass via `merge_settings` returns a plain `dict`, losing the subclass type.
- code-review-06: Ansible and Kubernetes strategic merge patches use conventions similar to `None`-as-delete.
- code-review-06: The shallow-copy aliasing issue and the silent type-mismatch overwrite are almost certainly bugs or oversights.
- code-review-06: Those two issues tend to pass testing and later cause hard-to-trace mutation bugs or config-clobbering incidents in production.
- code-review-06: Issues #1 and #4 are the highest-priority items to write tests around and confirm intent for.
- code-review-06: Issues #1 and #4 are the ones most likely to fail silently.
- code-review-07: The function has three different signals for failure: a thrown error that never happens, null, and undefined.
- code-review-07: The inconsistency in failure signals indicates the retry-exhaustion path was never tested.
- code-review-07: Swallowing non-HTTP errors as null is the most dangerous issue in the code, especially with callers that cannot be audited.
- code-review-07: Retrying server errors with zero delay defeats the purpose of backoff and could contribute to a thundering-herd effect.
- code-review-07: Discarding errors without a trace can cause silent data corruption downstream in a shared library with unknown callers.
- code-review-07: Most retry helpers use exponential backoff to avoid synchronized retry storms across clients.
- code-review-07: With attempts = 3, the code performs 3 total tries rather than 3 retries after an initial call.
- code-review-07: The attempts semantics are not a bug.
- code-review-07: A fail-soft contract is plausible for an old internal helper whose callers expect a fallback value rather than a thrown exception.
- code-review-08: A `PermissionError` would similarly abort the run.
- code-review-08: The script can delete a `foo.part` file while another process is actively writing it.
- code-review-08: The unconditional `tmp-`/`.part` deletion is the most dangerous line in the file.
- code-review-08: `os.listdir()` loads the entire directory listing into memory at once.
- code-review-08: The in-memory listing is acceptable for modest directories and only a concern if `ROOT` grows very large.
- code-review-08: The schedule that invokes this script was not set up by the author of the text.
- code-review-08: The two highest-priority changes are guarding against directories and requiring a minimum age before deleting `.part`/`tmp-` files.
- debugging-02: Class bodies are always in strict mode.
- debugging-02: Strict mode propagates to functions nested inside strict-mode code.
- debugging-02: A regular `function () {...}` passed to `setInterval` from inside a class method has `this === undefined` when called.
- debugging-02: Accessing `this.seconds` when `this` is `undefined` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: Seeing `NaN` instead of a thrown error indicates the code is running in a non-strict/sloppy context.
- debugging-02: Running code directly in a browser `<script>` without `"use strict"` is an example of a non-strict/sloppy context.
- debugging-02: Some transpilation does not preserve strict mode, producing a sloppy-mode context.
- debugging-02: Storing `const self = this;` before `setInterval` and using `self` inside the callback is an alternative fix.
- debugging-03: The corrected `moving_sum` function appends `sum(values[i : i + window])` to a list named `sums` on each iteration.
- debugging-03: The corrected `moving_sum` function returns `sums`.
- debugging-04: The non-ASCII byte occurs at byte offset 512 in the file.
- debugging-04: Encoding can be detected at runtime with libraries such as charset-normalizer or chardet.
- debugging-04: Detecting the encoding is preferable to hardcoding one when the encoding is not known ahead of time.
- debugging-04: For line counting, UTF-8 with errors="replace" is usually the pragmatic fix.
- debugging-04: The errors="surrogateescape" option preserves byte fidelity.
- debugging-05: The same test running twice can also cause the extra `"post"` entries, for example via test discovery, parametrization, or fixtures.
- debugging-06: A tool call was made to list files and directories in a given path.
- debugging-06: The status of that tool call was 'Completed'.
- debugging-06: The tool call's terminal output was 'No files found'.
- debugging-08: Campaign products can have larger payloads, more images and variants, and richer JSON than normal products.
- debugging-08: The count-bounded-cache explanation fits all four reported observations.
- debugging-08: Cache entries persist until they are evicted, so cache-driven memory growth survives quiet nights.
- debugging-08: Any traffic populates the cache, so cache-driven growth occurs even without webhooks.
- debugging-08: Guava and Caffeine caches offer a `maximumSize` setting and a `maximumWeight` setting.
- debugging-08: Long-lived maps used for deduplication, idempotency keys, rate limiting, or session and request tracking are a classic source of leaks when their TTL cleanup is absent, broken, or slow.
- debugging-08: Dynamically generated classes from serialization libraries, proxies, or template engines leak metaspace rather than heap.
- debugging-08: More campaign SKUs and variants can produce more dynamically generated types.
- debugging-08: Classes are not unloaded until their classloader is garbage collected.
- debugging-08: Application classloaders often are never garbage collected.
- debugging-08: `jstat -gc` or an APM memory breakdown can distinguish heap growth from non-heap/metaspace growth.
- debugging-08: Native or off-heap memory, such as Netty direct buffers and native codecs, can leak on specific code paths.
- debugging-08: Off-heap leaks are consistent with growth that survives quiet nights and correlates with traffic volume.
- debugging-08: If RSS grows well beyond JVM-reported heap usage, the growth is native or off-heap.
- debugging-08: NativeMemoryTracking, `pmap`, and `smaps` diffs can be used to investigate native memory growth.
- debugging-08: The cache-bound hypothesis is the only one of the four consistent with all four clues without positing an additional leak.
- debugging-08: Switching the cache to weight-based eviction would be a one-line fix.
- debugging-08: The canary-still-grows observation is the strongest evidence that something grows independently of the cache.
- explanation-01: The collection in a chained slot is usually a linked list, and sometimes a small array or tree.
- explanation-01: The rule for finding another open slot in open addressing is called a probe sequence.
- explanation-01: Linear probing tries the next index, then the next, and so on.
- explanation-01: Quadratic probing tries indices at increasing squared steps.
- explanation-01: Double hashing uses a second hash function to decide the step size.
- explanation-01: Chaining eventually needs resizing, but less urgently than open addressing.
- explanation-01: Chaining tolerates a poor hash function or high load factor more gracefully than open addressing.
- explanation-01: Java converts long chains to trees for performance.
- explanation-01: Python's dict uses open addressing.
- explanation-01: Many high-performance C++ hash maps use open addressing.
- explanation-02: Optimistic locking fits for long-lived transactions or when there is user think time between read and write, such as editing a form in a browser.
- explanation-02: Holding a database lock during user think time would be wasteful.
- explanation-02: As a rule of thumb, use optimistic locking for low-contention scenarios or when there is a gap between read and write that a lock shouldn't span, such as multi-step user edits and web forms.
- explanation-03: Dropped packets cause wasted bandwidth and retransmissions.
- explanation-03: Before congestion control existed, dropped packets could snowball into congestion collapse.
- explanation-03: Congestion collapse is when a congested network becomes even more congested because senders keep retransmitting lost data.
- explanation-03: The initial cwnd is now typically 2-10 segments per RFC 6928.
- explanation-03: Slow start is called 'slow' only relative to the older approach of immediately sending as much as the receiver's window allowed.
- explanation-03: Reaching a reasonable sending rate quickly matters a lot for short connections such as most web requests.
- explanation-03: ssthresh is often set from a previous congestion event.
- explanation-03: This congestion control philosophy is why the internet has remained stable even as usage grew enormously.
- explanation-03: Every TCP connection cooperates to avoid overwhelming shared links rather than assuming its capacity upfront.
- explanation-04: Each thread has its own stack and register/instruction pointer state.
- explanation-04: Switching between threads is cheaper than switching between processes.
- explanation-04: Thread communication requires careful synchronization, such as locks and mutexes, to avoid race conditions.
- explanation-04: Threads provide parallelism with shared state and need synchronization.
- explanation-04: Nginx and Apache use worker processes.
- explanation-04: Separate processes make it straightforward to restart, upgrade, or scale components independently.
- explanation-04: Microservices and worker pools are examples of components with independent lifecycles that can be killed and respawned.
- explanation-04: GIL and shared-state concerns matter less for I/O-bound tasks.
- explanation-05: Caches without a TTL, without a size limit, or using strong keys instead of weak references are unbounded.
- explanation-06: A cache does not help when slowness comes from a missing database index.
- explanation-06: A cache does not help when slowness comes from lock contention caused by writes.
- explanation-06: A cache does not help when slowness comes from an N+1 query problem.
- explanation-06: Slow query logs and DB metrics show whether the database is CPU or IO bound or whether the app is slow elsewhere.
- explanation-07: Routing logic is a source of sharding complexity.
- explanation-07: The product team's inability to estimate growth is the real problem.
- explanation-07: A growth rate of about 10% in GB is fine for years.
- explanation-07: Sharding solves horizontal scaling, not disk cost.
- explanation-07: Cheaper alternatives to sharding include indexing, partitioning within one instance, read replicas, connection pooling, archiving cold data, and vertical scaling.
- explanation-07: Waiting leaves less room to test the shard key choice.
- explanation-07: Partitioning can be time-based or tenant-based and still run on a single instance.
- explanation-07: Partitioning and read replicas are reversible.
- explanation-08: Smaller payload size helps if an application is network-bound.
- explanation-08: JSON has overhead from quotes, keys repeated per record, and text-encoded numbers.
- explanation-08: Most languages allow wrapping JSON encode/decode in a timer or using a profiler to measure it.
- summarization-02: The copied config exhausted the database connection pool.
- summarization-03: A worker pool would generate the thumbnails and update the record.
- summarization-04: The issue was reproduced by a second user on a different machine.
- summarization-07: The comparison confirmed a per-worker memory increase of approximately 60 MB.
- summarization-07: Aside from the median latency drop and the memory increase, the results of the comparison are uncertain.
- summarization-08: The progress bar finding is rated FIRM for the behavior and TENTATIVE for the cause.
- summarization-08: Follow-up with new or template-less users is needed before drawing conclusions about the template gallery.

Added facts (styled only):

- code-review-01: The function has five separate problems.
- code-review-01: `db` should probably be a required argument rather than a keyword argument defaulting to `None`.
- code-review-01: The uninformative return value is not a bug but a design gap.
- code-review-01: The suggested rewrite has the signature `add_user(name, db, roles=None)`.
- code-review-01: The suggested rewrite catches `DatabaseError` and returns `False`.
- code-review-01: `DatabaseError` should be replaced with whatever exception type `db.insert` actually raises.
- code-review-02: Without error handling, a network failure produces an unhandled promise rejection instead of a clear error.
- code-review-02: `fetch` rejects only on network errors.
- code-review-02: The caller should still wrap the call in `try/catch` to handle rejected promises.
- code-review-03: Setting customer_name to "x' OR '1'='1" returns every row in the table.
- code-review-03: psycopg2 and MySQLdb use %s as the query parameter placeholder.
- code-review-03: Pulling every column wastes bandwidth.
- code-review-03: SELECT * breaks silently if the table schema changes column order or names, where other code indexes results positionally.
- code-review-03: The function does not check that customer_name or status are non-empty or of a reasonable length before querying.
- code-review-04: `reset()` has the same concurrency problem as `increment()`, in reverse.
- code-review-04: The `Counter` class currently provides no way to read `self.value` safely from another thread.
- code-review-04: A `get_value()` method, if added, should also acquire the lock.
- code-review-04: Even a plain read can observe a partially-updated value if `value` is later changed to something non-atomic, such as a multi-field object.
- code-review-04: If increments are far more frequent than resets, lock contention can become a bottleneck.
- code-review-05: The script has one critical safety flaw and several correctness bugs.
- code-review-05: `cd` can fail due to a bad path or lack of permissions.
- code-review-05: If no `.log` files exist, the loop silently does nothing.
- code-review-05: The error printed when no `.log` files exist is not fatal but is noisy and easy to miss.
- code-review-06: The function has a crash bug caused by a type mismatch on nested keys.
- code-review-06: The function crashes when a nested dict in the base is overridden with a non-dict value.
- code-review-06: The recursion check only tests merged[key], the base side, and not value, the override side.
- code-review-06: Merging base {"db": {"host": "a", "port": 1}} with override {"db": "disabled"} raises AttributeError: 'str' object has no attribute 'items'.
- code-review-06: Because merged["db"] is a dict, the code recurses with merge_settings({"host": "a", "port": 1}, "disabled").
- code-review-06: The inner recursive call calls .items() on the string.
- code-review-06: The crash occurs if override configs are allowed to replace a whole sub-config with a scalar, such as when disabling a section.
- code-review-06: The type-mismatch crash is likely a bug rather than intended behavior.
- code-review-06: If override introduces a brand-new nested dict for a key, that dict is assigned by reference via merged[key] = value.
- code-review-06: Mutating merged[key] can also mutate the original override dict.
- code-review-06: The recommendation is to confirm the None-deletes-key and list-replacement behaviors with a stakeholder before writing tests.
- code-review-06: The recommendation is to fix the type-mismatch crash and the shallow-copy aliasing.
- code-review-06: The type-mismatch crash and shallow-copy aliasing are correctness bugs regardless of original intent.
- code-review-07: Nothing in the code explains why 429 errors get a delay while 5xx errors do not.
- code-review-07: The zero first delay is an off-by-one error; the intent was probably `1000 * (i + 1)`.
- code-review-07: On the final loop iteration, the 429 path waits `1000 * i` ms and then continues straight into loop exit, so the delay accomplishes nothing.
- code-review-07: Some callers may depend on catching errors, and this function never gives them the chance.
- code-review-07: Linear backoff without jitter is acceptable for low-concurrency internal use.
- code-review-07: When `attempts <= 0`, the function skips calling `fn` entirely and returns undefined.
- code-review-07: The `attempts <= 0` behavior is probably an unhandled edge case rather than designed behavior.
- code-review-07: `fn` is awaited with no timeout, so a hung `fn` blocks the retry logic indefinitely.
- code-review-07: The lack of a timeout on `fn` is outside the function's stated scope.
- code-review-07: If no caller relies on the null return, the safest fix is to rethrow the original error on the non-retryable and exhausted-attempts paths, add backoff to the 5xx branch, and fix the off-by-one in the delay calculation.
- code-review-08: `os.path.getmtime` succeeds on directories.
- code-review-08: An `IsADirectoryError` stops the whole run and the `removed` count is lost.
- code-review-08: When the run crashes, the caller never learns how many files were deleted before the crash.
- code-review-08: The `elif` means the cap never limits the first branch.
- code-review-08: The cap as written does not reliably keep the directory bounded.
- code-review-08: Exempting `tmp-`/`.part` files from the cap is plausibly intentional, treating incomplete or transient files as always safe to delete.
- code-review-08: The 45-day cutoff and 500-file cap are almost certainly tuned business or operations values.
- code-review-08: Because the cutoff and cap values are undocumented, nobody can safely change them.
- code-review-08: The absence of logging may be deliberate for a fire-and-forget cron job.
- code-review-08: The 500 cap can be applied globally by incrementing `removed` before either branch and checking it first.
- code-review-08: Logging each deletion with path, reason, and mtime would allow the cap and cutoff values to be tuned with real data.
- debugging-01: The dictionary only contains the lowercase key `'port'`.
- debugging-01: The faulty lookup is on line 4 of the code.
- debugging-04: errors="replace" substitutes undecodable bytes with the replacement character ï¿½ instead of raising an exception.
- debugging-07: The test passes when run serially.
- debugging-07: The test fails about 10% of the time when run under 4-way parallel load.
- debugging-07: The test creates three events via seed POST calls and then queries a digest endpoint.
- debugging-07: The failure symptom is an undercount: the digest returns 2 of 3 events, not an overcount or wrong content.
- debugging-07: The test is tests/test_notifications.py::test_digest_contains_all_events.
- debugging-07: CI runs the suite with 4 parallel workers.
- debugging-07: CI retains no artifacts from test runs.
- debugging-07: Passing serially while failing only under parallel load indicates a timing race exposed by contention rather than a badly written assertion.
- debugging-07: The most likely cause is that event creation and the digest read are not consistent with each other.
- debugging-07: If event creation is asynchronous, the third event may not be visible yet when the test calls the digest endpoint.
- debugging-07: Asynchronous creation can take the form of a queue, a background worker, an outbox pattern, or eventual index consistency.
- debugging-07: Contention from 4 parallel workers adds CPU and database load that can delay event visibility.
- debugging-07: Serial execution produces no contention, so the event pipeline always keeps up.
- debugging-07: A slow write-then-read race produces a low count.
- debugging-07: A shared-state bug would more often add or duplicate events than cause an undercount.
- debugging-07: The second hypothesis is shared state across parallel workers.
- debugging-07: If the four workers share one database, queue, or in-memory store instead of isolated instances, one worker's setup or teardown can interfere with another worker's data.
- debugging-07: A cleanup step in another test could delete or filter out an event that this test just wrote.
- debugging-07: The shared-state hypothesis also produces an undercount and explains why parallelism triggers the failure.
- debugging-07: One of the three seed POST calls could fail or time out under load without the test checking its response code, so only 2 events get created.
- debugging-07: The digest endpoint may filter by a time window, and under CI load the first event could fall outside that window before the digest is requested.
- debugging-07: Grepping the event-creation and digest code paths for a queue, background task, or eventually consistent read reveals whether creation is asynchronous.
- debugging-07: A search index or cache is an example of an eventually consistent read.
- debugging-07: If creation is synchronous end-to-end, the async-race hypothesis can be dropped in favor of shared state.
- debugging-07: If the 4 CI workers share a database rather than each having its own database or schema, shared state is the prime suspect.
- debugging-07: Isolating the database per worker and observing whether the failure rate drops tests the shared-state hypothesis.
- debugging-07: Adding an assertion on the response status code after each of the three event-creation calls catches a silent failure immediately.
- debugging-07: 201 is a typical success status code for the event-creation POST calls.
- debugging-07: Temporary logging of worker ID, event IDs from each POST, timestamps, and the full digest response body, printed only on assertion failure, would provide failure artifacts.
- debugging-07: Pytest captures stdout per test by default.
- debugging-07: CI configuration must be set to surface captured stdout, for example with -rA or a JUnit/HTML report, rather than showing only the assertion line.
- debugging-07: Running pytest with -n 4 and --count=50 on the single test reproduces the conditions locally.
- debugging-07: The -n flag comes from pytest-xdist and the --count flag comes from pytest-repeat.
- debugging-07: Local repeated runs yield far more attempts per minute than waiting for CI's 1-in-10 failure rate.
- debugging-07: Failing only when run alongside the full suite, but not alone under -n4, points to cross-test shared state.
- debugging-07: Failing even in isolation under -n4 while never failing serially points to a pure contention-induced race, because no other test is present to interfere.
- debugging-07: Replacing the single digest call with a retry loop that polls up to 2 seconds until the count reaches 3 tests the async-race hypothesis.
- debugging-07: If the flake disappears when polling is added, that confirms an eventual-consistency race.
- debugging-07: The real fix for an eventual-consistency race is either making the digest read wait on write confirmation or having the test poll instead of asserting once.
- debugging-07: Success is being able to reproduce the failure on demand locally instead of waiting for CI.
- debugging-07: The isolated-versus-full-suite comparison determines definitively whether the bug is contention timing or shared state.
- debugging-08: The observed memory problem is a real memory leak, meaning objects that never get collected.
- debugging-08: The memory problem is not GC pressure.
- debugging-08: The memory problem is not cache growth.
- debugging-08: The leak has two separate sources.
- debugging-08: One source is a baseline leak that occurs even with zero webhook traffic.
- debugging-08: The second source is a leak that scales with request volume.
- debugging-08: The request-volume-scaled leak worsens during marketing campaigns.
- debugging-08: Normal GC delay recovers or plateaus under low traffic.
- debugging-08: JIT warm-up recovers or plateaus under low traffic.
- debugging-08: A size-bounded cache filling up recovers or plateaus under low traffic.
- debugging-08: The overnight non-recovery observation rules out normal GC delay, JIT warm-up, and a size-bounded cache filling up.
- debugging-08: An off-by-one error in the cache bound could produce the observed memory growth.
- debugging-08: Product objects can gain longer field lists over time.
- debugging-08: If cache entry count stays flat while memory grows, the cache bound is working and the cache is not the cause.
- debugging-08: If cache entry count creeps past the configured max, that identifies the cause.
- debugging-08: Candidate baseline leak sources include metrics buffers, listener/subscriber lists, unclosed connections, and a ThreadLocal not cleared in a pooled thread.
- debugging-08: The class with the largest object count delta is the leak source.
- debugging-08: Webhook request-rate metrics can be correlated against memory growth rate over the same days.
- debugging-08: A tight correlation between webhook request rate and memory growth rate confirms a per-request leak.
- debugging-08: Histogram diffs taken on production during a traffic spike can reveal which class count tracks the webhook rate.
- debugging-08: A correctly bounded cache can still pin large object graphs if evicted entries retain external references.
- debugging-08: A listener or callback capturing a reference to a cached object is an example of an external reference pinning evicted entries.
- debugging-08: Whether an evicted cache object is actually unreachable can be verified by code review or by confirming eviction correlates with count drops in a histogram diff.
- explanation-01: A hash map's underlying array has a fixed number of slots.
- explanation-01: A hash map can hold far more keys than its array has slots.
- explanation-01: Collisions are inevitable in hash maps.
- explanation-02: Under optimistic locking, the application must retry after a failed commit.
- explanation-02: Optimistic locking fits when conflicts are infrequent and transactions are short.
- explanation-02: Editing one's own user profile is an example use case for optimistic locking.
- explanation-02: A shopping cart update is an example use case for optimistic locking.
- explanation-02: Optimistic locking suits short transactions; pessimistic locking can accommodate longer transactions.
- explanation-02: When unsure which to use, start with optimistic locking for its better concurrency.
- explanation-02: Switch from optimistic to pessimistic locking only if retries become frequent enough to hurt performance or correctness.
- explanation-03: A network path might be a fast local link or a slow, congested one.
- explanation-03: Routers can only hold a limited number of packets in their queues.
- explanation-03: Modern TCP systems typically start with an initial congestion window of about 10 segments.
- explanation-03: Every segment in a batch triggers its own ACK.
- explanation-04: Python and Ruby have a GIL.
- explanation-04: Browsers use one process per tab partly for security and resource isolation.
- explanation-06: When the database is slow because of missing indexes or bad queries, a cache may help, but fixing the query is usually cheaper.
- explanation-06: Fixing a query fixes the problem everywhere, not just on cache hits.
- explanation-06: Profiling a service with an APM tool reveals where request time goes: database queries, network calls, serialization, or application code.
- explanation-06: Datadog and New Relic are APM tools.
- explanation-06: Slow queries, missing indexes, and lock contention are often cheaper to fix than adding a cache.
- explanation-06: Profiling will reveal whether a simpler fix, such as an index or a query rewrite, solves the problem.
- explanation-07: Sharding fixes write throughput and data size problems.
- explanation-07: Sharding does not fix a poorly indexed query or connection exhaustion.
- explanation-07: Current headroom can be assessed by checking CPU, memory, IOPS, and replication lag under current load.
- explanation-07: At 20% utilization, a database likely has 12-18 months of runway even at aggressive growth rates.
- explanation-07: Migrating a live system to a sharded architecture without downtime is harder than designing for sharding from the start.
- explanation-07: Migration to sharding is especially hard if the schema has deep foreign-key relationships.
- explanation-07: PgBouncer is a connection pooling tool.
- explanation-08: Two unknowns each swing the estimated answer by an order of magnitude.
- explanation-08: If JSON encoding/decoding is 2% of request latency, a 10x faster format saves about 1.8% end to end.
- explanation-08: A 2% serialization share is typical when network, database, or business logic dominate request time.
- explanation-08: If JSON encoding/decoding is 40% of request latency, a 10x speedup saves close to 36% end to end.
- explanation-08: A 40% serialization share occurs with large payloads, high request rates, and CPU-bound services.
- explanation-08: For small payloads of a few KB or low-traffic endpoints, the difference between formats is often not measurable.
- explanation-08: The third measurement step is benchmarking a candidate binary format against JSON on the same payloads, measuring both size and encode/decode time.
- explanation-08: With those three measurements, a realistic end-to-end speedup can be projected instead of guessed.
- summarization-01: Plugins now initialize after startup rather than before startup.
- summarization-02: A checkout outage occurred on Tuesday.
- summarization-02: The page went out at 09:21.
- summarization-02: The time from page to rollback was 27 minutes.
- summarization-02: The rollback fully resolved the errors.
- summarization-02: The incident response time was good.
- summarization-02: No changes are needed to the incident response process.
- summarization-04: The expected result matches the behavior of the working CSV export.
- summarization-04: One error banner appears per click.
- summarization-04: The bug was reproduced on the latest version of Firefox.
- summarization-05: A sprint planning meeting took place on Monday.
- summarization-05: The sprint planning meeting produced a list of action items.
- summarization-07: A production-like test is needed to confirm the p99 improvement.
- summarization-07: Staging runs a newer kernel.
- summarization-07: The newer kernel in staging may be the cause of the worker crash.
- summarization-08: Confidence in the progress bar finding is limited by the small sample of 3 participants.
- summarization-08: The progress bar finding is rated tentative.

### clarity-flow

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 28 | 18 | 0.643 | 29 | 2 |
| code-review-02 | 19 | 13 | 0.684 | 20 | 2 |
| code-review-03 | 24 | 15 | 0.625 | 16 | 3 |
| code-review-04 | 26 | 22 | 0.846 | 21 | 8 |
| code-review-05 | 27 | 23 | 0.852 | 42 | 3 |
| code-review-06 | 38 | 18 | 0.474 | 25 | 12 |
| code-review-07 | 30 | 23 | 0.767 | 33 | 4 |
| code-review-08 | 34 | 29 | 0.853 | 27 | 2 |
| debugging-01 | 7 | 6 | 0.857 | 8 | 0 |
| debugging-02 | 19 | 9 | 0.474 | 9 | 0 |
| debugging-03 | 10 | 10 | 1.0 | 9 | 1 |
| debugging-04 | 15 | 9 | 0.6 | 11 | 1 |
| debugging-05 | 17 | 16 | 0.941 | 10 | 1 |
| debugging-06 | 4 | 0 | 0.0 | 32 | 32 |
| debugging-07 | 0 | 0 | n/a | 30 | 30 |
| debugging-08 | 28 | 12 | 0.429 | 24 | 12 |
| explanation-01 | 39 | 23 | 0.59 | 22 | 1 |
| explanation-02 | 24 | 22 | 0.917 | 23 | 2 |
| explanation-03 | 35 | 21 | 0.6 | 23 | 2 |
| explanation-04 | 39 | 23 | 0.59 | 27 | 3 |
| explanation-05 | 18 | 15 | 0.833 | 12 | 1 |
| explanation-06 | 21 | 16 | 0.762 | 18 | 3 |
| explanation-07 | 26 | 13 | 0.5 | 23 | 3 |
| explanation-08 | 18 | 13 | 0.722 | 14 | 0 |
| summarization-01 | 5 | 5 | 1.0 | 10 | 4 |
| summarization-02 | 12 | 10 | 0.833 | 16 | 5 |
| summarization-03 | 13 | 12 | 0.923 | 12 | 0 |
| summarization-04 | 13 | 11 | 0.846 | 12 | 1 |
| summarization-05 | 9 | 7 | 0.778 | 8 | 0 |
| summarization-06 | 12 | 10 | 0.833 | 13 | 2 |
| summarization-07 | 14 | 13 | 0.929 | 17 | 4 |
| summarization-08 | 20 | 17 | 0.85 | 21 | 1 |

Median fraction: 0.778 over 31 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python footgun.
- code-review-01: Mutating the caller's list is a surprising side effect that can cause bugs elsewhere in the caller's code.
- code-review-01: Duplicate roles aren't prevented.
- code-review-01: Calling the function with `roles=["member"]` explicitly produces `["member", "member"]`.
- code-review-01: The function has no docstring and no type hints.
- code-review-01: Missing type hints is a minor issue.
- code-review-01: Type hints of `name: str`, `roles: list[str] | None`, and a type for `db` would clarify the function's contract.
- code-review-01: A safer rewrite uses `roles=None` as the default and raises `ValueError` when `name` or `db` is missing.
- code-review-01: The safer rewrite copies `roles` with `list(roles)` and appends `"member"` only if it is not already present.
- code-review-01: An alternative to letting errors propagate is catching a specific DB exception in order to translate it.
- code-review-02: There is no validation that the response `data` has a `name` property.
- code-review-02: If the API returns an error object instead of a profile, `data.name` could be `undefined` and calling `.toUpperCase()` on it would throw.
- code-review-02: There is no input validation on `userId`.
- code-review-02: Unsanitized/unencoded `userId` could allow injection of unexpected path segments such as `../` or query-like content.
- code-review-02: `encodeURIComponent(userId)` can be used to encode `userId` before interpolating it into the URL.
- code-review-02: The fixed version awaits `fetch` with an encoded `userId`, throws an Error including `res.status` when `!res.ok`, awaits `res.json()`, throws an Error when the response is missing `name`, and returns `data.name.toUpperCase()`.
- code-review-03: The SQL injection issue is critical in severity.
- code-review-03: psycopg2 uses `%s` as its parameter placeholder.
- code-review-03: pymysql uses `%s` as its parameter placeholder.
- code-review-03: `fetchall` can raise an exception, for example on a bad connection or a database error.
- code-review-03: These exceptions are handled nowhere, and no context is provided to the caller.
- code-review-03: The function imposes no limit on the number of results returned.
- code-review-03: A broad match could return an unbounded number of rows.
- code-review-03: Pagination or a `LIMIT` clause should be considered to bound the result set.
- code-review-03: The SQL injection issue is the one that must be fixed before the code is used in production.
- code-review-04: Under contention, the counter class will systematically undercount.
- code-review-04: An example of the reset/increment race is resetting to 0 and then a stale increment writing 1.
- code-review-04: The class has no thread-safety documentation or contract.
- code-review-04: A caller reading the code has no way to know the class is unsafe under concurrent use.
- code-review-05: `rm -rf` given a literal unmatched pattern typically errors out harmlessly in POSIX sh.
- code-review-05: Bash has a `nullglob` option affecting unmatched glob behavior.
- code-review-05: `rm -rf *.tmp` is the most dangerous line in the script.
- code-review-05: The `-r` flag is unnecessary for `rm` because the targets are files, not directories.
- code-review-06: Resolving the `None`-means-delete ambiguity requires a sentinel such as a `DELETE` marker if both behaviors are needed.
- code-review-06: `merged.pop(key, None)` silently does nothing if the key is not present in `base`.
- code-review-06: Silently no-oping on a missing key can hide a typo, such as a misspelled key intended to delete something.
- code-review-06: If `base[key]` is a dict and `override[key]` is not a dict, the `elif` branch fails and control falls to the `else` branch.
- code-review-06: In that case the entire nested dict is replaced by the scalar value.
- code-review-06: No validation or error is raised for either type-mismatch case.
- code-review-06: The type-mismatch behavior could mask a configuration mistake.
- code-review-06: Recursion depth follows the depth of `override`'s nested dicts.
- code-review-06: Self-referential structures are unlikely for JSON-like config but possible if `base` or `override` are constructed programmatically.
- code-review-06: List replacement is a common convention in settings-merge functions.
- code-review-06: Some config systems expect list concatenation or index-wise merging.
- code-review-06: There is no check that keys are hashable or strings.
- code-review-06: `isinstance(merged[key], dict)` also matches dict subclasses.
- code-review-06: Recursing into an `OrderedDict` or custom dict subclass via `merge_settings` returns a plain `dict`, losing the subclass type.
- code-review-06: Non-dict values fully overriding reflects typical 'last writer wins' semantics.
- code-review-06: Ansible and Kubernetes strategic merge patches use conventions similar to `None`-as-delete.
- code-review-06: The shallow-copy aliasing issue and the silent type-mismatch overwrite are almost certainly bugs or oversights.
- code-review-06: Those two issues tend to pass testing and later cause hard-to-trace mutation bugs or config-clobbering incidents in production.
- code-review-06: Issues #1 and #4 are the highest-priority items to write tests around and confirm intent for.
- code-review-06: Issues #1 and #4 are the ones most likely to fail silently.
- code-review-07: The inconsistency in failure signals indicates the retry-exhaustion path was never tested.
- code-review-07: Swallowing non-HTTP errors as null is the most dangerous issue in the code, especially with callers that cannot be audited.
- code-review-07: Discarding errors without a trace can cause silent data corruption downstream in a shared library with unknown callers.
- code-review-07: Most retry helpers use exponential backoff to avoid synchronized retry storms across clients.
- code-review-07: With attempts = 3, the code performs 3 total tries rather than 3 retries after an initial call.
- code-review-07: The attempts semantics are not a bug.
- code-review-07: Changing the undefined case or making the function throw would be a breaking change if callers currently check === null to detect failure.
- code-review-08: The script has no dry-run mode.
- code-review-08: `os.listdir()` loads the entire directory listing into memory at once.
- code-review-08: The in-memory listing is acceptable for modest directories and only a concern if `ROOT` grows very large.
- code-review-08: The schedule that invokes this script was not set up by the author of the text.
- code-review-08: Unconditional removal of `tmp-`/`.part` files could be an intentional 'always junk' assumption.
- debugging-01: The corrected get_url function returns an f-string of the form "http://{cfg['host']}:{cfg['port']}/api".
- debugging-02: Class bodies are always in strict mode.
- debugging-02: Strict mode propagates to functions nested inside strict-mode code.
- debugging-02: A regular `function () {...}` passed to `setInterval` from inside a class method has `this === undefined` when called.
- debugging-02: Accessing `this.seconds` when `this` is `undefined` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: Seeing `NaN` instead of a thrown error indicates the code is running in a non-strict/sloppy context.
- debugging-02: Running code directly in a browser `<script>` without `"use strict"` is an example of a non-strict/sloppy context.
- debugging-02: Some transpilation does not preserve strict mode, producing a sloppy-mode context.
- debugging-02: Calling `.bind(this)` on the callback function is an alternative fix.
- debugging-02: Storing `const self = this;` before `setInterval` and using `self` inside the callback is an alternative fix.
- debugging-02: The arrow function is the cleanest modern approach among these fixes.
- debugging-04: The 0xc3 byte likely represents an accented character such as é or ü.
- debugging-04: The ASCII codec rejects any byte greater than or equal to 0x80.
- debugging-04: Encoding can be detected at runtime with libraries such as charset-normalizer or chardet.
- debugging-04: Detecting the encoding is preferable to hardcoding one when the encoding is not known ahead of time.
- debugging-04: For line counting, UTF-8 with errors="replace" is usually the pragmatic fix.
- debugging-04: The errors="surrogateescape" option preserves byte fidelity.
- debugging-05: The same test running twice can also cause the extra `"post"` entries, for example via test discovery, parametrization, or fixtures.
- debugging-06: The speaker intends to check memory for prior context on the system.
- debugging-06: A tool call was made to list files and directories in a given path.
- debugging-06: The status of that tool call was 'Completed'.
- debugging-06: The tool call's terminal output was 'No files found'.
- debugging-08: Campaign products can have larger payloads, more images and variants, and richer JSON than normal products.
- debugging-08: The count-bounded-cache explanation fits all four reported observations.
- debugging-08: Cache entries persist until they are evicted, so cache-driven memory growth survives quiet nights.
- debugging-08: Any traffic populates the cache, so cache-driven growth occurs even without webhooks.
- debugging-08: Guava and Caffeine caches offer a `maximumSize` setting and a `maximumWeight` setting.
- debugging-08: Long-lived maps used for deduplication, idempotency keys, rate limiting, or session and request tracking are a classic source of leaks when their TTL cleanup is absent, broken, or slow.
- debugging-08: Such leaky maps are typically keyed by request ID, order ID, webhook event ID, or correlation ID.
- debugging-08: Dynamically generated classes from serialization libraries, proxies, or template engines leak metaspace rather than heap.
- debugging-08: More campaign SKUs and variants can produce more dynamically generated types.
- debugging-08: Classes are not unloaded until their classloader is garbage collected.
- debugging-08: Application classloaders often are never garbage collected.
- debugging-08: Native or off-heap memory, such as Netty direct buffers and native codecs, can leak on specific code paths.
- debugging-08: Off-heap leaks are consistent with growth that survives quiet nights and correlates with traffic volume.
- debugging-08: NativeMemoryTracking, `pmap`, and `smaps` diffs can be used to investigate native memory growth.
- debugging-08: The cache-bound hypothesis is the only one of the four consistent with all four clues without positing an additional leak.
- debugging-08: Switching the cache to weight-based eviction would be a one-line fix.
- explanation-01: An array slot cannot hold two values at once.
- explanation-01: The collection in a chained slot is usually a linked list, and sometimes a small array or tree.
- explanation-01: Quadratic probing tries indices at increasing squared steps.
- explanation-01: Double hashing uses a second hash function to decide the step size.
- explanation-01: Open addressing can fail entirely if the array is full.
- explanation-01: Deletion in chaining is simple because the node is just removed from the list.
- explanation-01: Deletion in open addressing is trickier because emptying a slot breaks the probe chain for other keys.
- explanation-01: Deletion in open addressing usually needs tombstone markers.
- explanation-01: Chaining eventually needs resizing, but less urgently than open addressing.
- explanation-01: Open addressing needs resizing sooner and must be kept well below full, often under a 70% load factor.
- explanation-01: Chaining is simpler to reason about than open addressing.
- explanation-01: Chaining tolerates a poor hash function or high load factor more gracefully than open addressing.
- explanation-01: Deletion and resizing are more delicate to implement correctly in open addressing.
- explanation-01: Java converts long chains to trees for performance.
- explanation-01: Python's dict uses open addressing.
- explanation-01: Many high-performance C++ hash maps use open addressing.
- explanation-02: Optimistic locking fits for long-lived transactions or when there is user think time between read and write, such as editing a form in a browser.
- explanation-02: Holding a database lock during user think time would be wasteful.
- explanation-03: Dropped packets cause wasted bandwidth and retransmissions.
- explanation-03: Congestion collapse is when a congested network becomes even more congested because senders keep retransmitting lost data.
- explanation-03: Historically the initial cwnd was 1 segment.
- explanation-03: The initial cwnd is now typically 2-10 segments per RFC 6928.
- explanation-03: During slow start, cwnd grows by roughly one segment per ACK.
- explanation-03: The exponential increase is a deliberate trade-off.
- explanation-03: Exponential growth lets a connection reach a reasonable sending rate in a few RTTs, on the order of log base 2 of the target window.
- explanation-03: Reaching a reasonable sending rate quickly matters a lot for short connections such as most web requests.
- explanation-03: After detecting loss, TCP switches to a more cautious, linear growth phase called congestion avoidance.
- explanation-03: Slow start also ends when cwnd reaches a threshold called ssthresh (slow start threshold).
- explanation-03: ssthresh is often set from a previous congestion event.
- explanation-03: When cwnd reaches ssthresh, TCP switches to the linear growth of congestion avoidance.
- explanation-03: This congestion control philosophy is why the internet has remained stable even as usage grew enormously.
- explanation-03: Every TCP connection cooperates to avoid overwhelming shared links rather than assuming its capacity upfront.
- explanation-04: A process is an independent instance of a running program.
- explanation-04: A process has its own memory address space, file descriptors, and OS-level resources.
- explanation-04: Each thread has its own stack and register/instruction pointer state.
- explanation-04: Threads are cheaper to create than processes.
- explanation-04: Switching between threads is cheaper than switching between processes.
- explanation-04: Thread communication requires careful synchronization, such as locks and mutexes, to avoid race conditions.
- explanation-04: Process creation cost is higher than thread creation cost because the OS allocates a new memory space and tables.
- explanation-04: Threads provide parallelism with shared state and need synchronization.
- explanation-04: Multiple processes bypass the GIL because each process has its own interpreter and GIL.
- explanation-04: Nginx and Apache use worker processes.
- explanation-04: The OS lets you set per-process limits on memory, CPU, and file descriptors via cgroups and ulimits.
- explanation-04: Per-process resource limits are hard or impossible to apply to a single thread within a shared process.
- explanation-04: Microservices and worker pools are examples of components with independent lifecycles that can be killed and respawned.
- explanation-04: Threads are preferable for tasks that are lightweight, need to share state efficiently, and are I/O-bound.
- explanation-04: I/O-bound tasks wait on network or disk.
- explanation-04: GIL and shared-state concerns matter less for I/O-bound tasks.
- explanation-05: Global emitters and DOM elements are examples of long-lived objects.
- explanation-05: Listeners often close over additional state.
- explanation-05: Caches without a TTL, without a size limit, or using strong keys instead of weak references are unbounded.
- explanation-06: A cache does not help when slowness comes from lock contention caused by writes.
- explanation-06: Adding a cache means maintaining two systems instead of one.
- explanation-06: Adding a cache introduces a new class of bugs involving stale or inconsistent data.
- explanation-06: For write-heavy or unique-read workloads, cache invalidation overhead may add complexity for little benefit.
- explanation-06: Slow query logs and DB metrics show whether the database is CPU or IO bound or whether the app is slow elsewhere.
- explanation-07: Rebalancing is a source of sharding complexity.
- explanation-07: Routing logic is a source of sharding complexity.
- explanation-07: The product team's inability to estimate growth is the real problem.
- explanation-07: A growth rate of about 10% in GB is fine for years.
- explanation-07: A growth rate of 10x per year changes the calculus.
- explanation-07: Sharding solves horizontal scaling, not disk cost.
- explanation-07: A natural shard key such as tenant ID or region can keep queries within a single shard.
- explanation-07: If most queries need cross-shard joins or aggregations, sharding will hurt more than help.
- explanation-07: Cheaper alternatives to sharding include indexing, partitioning within one instance, read replicas, connection pooling, archiving cold data, and vertical scaling.
- explanation-07: That complexity slows every feature that touches multiple entities.
- explanation-07: Waiting leaves less room to test the shard key choice.
- explanation-07: Partitioning can be time-based or tenant-based and still run on a single instance.
- explanation-07: Partitioning and read replicas are reversible.
- explanation-08: Protobuf and msgpack are examples of binary formats.
- explanation-08: JSON has overhead from quotes, keys repeated per record, and text-encoded numbers.
- explanation-08: JSON's overhead matters most for large arrays of small objects or numeric-heavy data.
- explanation-08: If payloads are already small or mostly free-text strings, binary formats provide little size benefit.
- explanation-08: Most languages allow wrapping JSON encode/decode in a timer or using a profiler to measure it.
- summarization-02: The staging pool size of 5 was intended to be small.
- summarization-02: The incident caused approximately 12% error rates for checkout.
- summarization-03: Thumbnail generation currently ties up web workers.
- summarization-04: After clicking the PDF export option, nothing happens initially.
- summarization-04: The issue was reproduced by a second user on a different machine.
- summarization-05: Ada is assigned to run the payments database migration dry run.
- summarization-05: Chen is assigned to continue the search indexing work.
- summarization-06: The on-call engineer suspects connection-pool exhaustion in the payments client caused the checkout service errors.
- summarization-06: Recovery after a restart is consistent with several possible causes.
- summarization-07: Aside from the median latency drop and the memory increase, the results of the comparison are uncertain.
- summarization-08: The abandonment behavior is a real, actionable problem regardless of its cause.
- summarization-08: The template gallery finding is rated TENTATIVE.
- summarization-08: Follow-up with new or template-less users is needed before drawing conclusions about the template gallery.

Added facts (styled only):

- code-review-01: The function has five problems.
- code-review-01: The corrected version builds a new list with `roles + ["member"]` instead of mutating the argument.
- code-review-02: `fetch` only rejects on network failure.
- code-review-02: A corrected version awaits `fetch(`/api/users/${userId}`)` and assigns the result to `res`.
- code-review-03: `' OR '1'='1` is an example of an SQL injection payload.
- code-review-03: Naming columns explicitly avoids leaking columns that were not intended to be exposed.
- code-review-03: `status` is meant to be one of a fixed set of values, such as "pending" or "shipped".
- code-review-04: The class has one real bug: `increment` is not thread-safe.
- code-review-04: The read-modify-write in `increment` consists of two separate steps.
- code-review-04: Under CPython's GIL, each of the two statements in `increment` is individually atomic.
- code-review-04: The class provides no thread-safe way to read `value` for reporting.
- code-review-04: A `get()` method, if added, should be guarded by the same lock.
- code-review-04: Guarding `get()` with the lock prevents it from observing a half-updated state.
- code-review-04: Observing a half-updated state is not an issue in this exact code because the write is atomic.
- code-review-04: Guarding a `get()` method is worthwhile for correctness under future changes.
- code-review-05: The script's word-splitting logic assumes bash-like array-free globbing.
- code-review-05: Using `$(...)` command substitution is not a bug in POSIX sh.
- code-review-05: It is worth confirming the target shell is truly POSIX-compliant in case other bashisms are added later.
- code-review-06: The code review identifies three real bugs and two behaviors that look intentional but need confirmation.
- code-review-06: The `elif` branch only checks whether `merged[key]`, the base value, is a dict.
- code-review-06: The `elif` branch never checks whether `value`, the override value, is a dict.
- code-review-06: If base holds a dict at a key and override holds a non-dict such as a string, number, or list, the code still recurses into `merge_settings(merged[key], value)`.
- code-review-06: In that recursion, `value.items()` raises `AttributeError` because `value` is not a dict.
- code-review-06: When override introduces a brand-new dict value, `merged[key] = value` stores override's dict by reference rather than copying it.
- code-review-06: Because new dict values are stored by reference, mutating the merged result can mutate `override`.
- code-review-06: Letting override win on type mismatch is a reasonable merge policy in principle.
- code-review-06: The code implements the override-wins policy correctly in only one direction.
- code-review-06: The dict-in-base, scalar-in-override case crashes instead of overwriting, which is bug #1.
- code-review-06: The recommended next step is to write tests pinning down expected behavior for `None` values and type mismatches before changing the code.
- code-review-06: `None` values and type mismatches are the two places where bug and intended design are hard to distinguish from the code alone.
- code-review-07: The loop has no exit path for its final iteration.
- code-review-07: The backoff delay looks like an off-by-one error and probably was meant to be `1000 * (i + 1)`.
- code-review-07: The delay asymmetry between 5xx and 429 retries is undocumented.
- code-review-07: The zero-delay first retry is almost certainly a bug rather than design.
- code-review-08: Skipping the age check for `tmp-`/`.part` files is probably not deliberate.
- code-review-08: The recommended fix before running in production again is to add an age check for `.part`/`tmp-` files and add basic `try/except` around the remove and stat calls.
- debugging-03: The original range dropped the last window `[3, 4]`.
- debugging-04: `open()` accepts an `errors` parameter with values such as `"replace"` and `"ignore"`.
- debugging-05: The fixed make_post uses tags=None as the default and sets tags = list(tags) if tags is not None else list(DEFAULT_TAGS).
- debugging-06: A shared connection pool running out of connections is the most likely cause of the failure.
- debugging-06: The export job and the analytics service compete for the same limited connection pool.
- debugging-06: A 'Pool exhausted' error indicates a connection or thread pool problem rather than a query timing out.
- debugging-06: In a pool exhaustion failure, the request never obtained a connection at all.
- debugging-06: The batch number at which the failure occurs varies between failures.
- debugging-06: A varying batch number rules out a bad row or query in a specific batch.
- debugging-06: The failure is caused by contention rather than by data.
- debugging-06: The database is shared with an independent analytics service.
- debugging-06: A shared database with an independent analytics service is a classic source of unpredictable load spikes.
- debugging-06: A heavy analytics query or scheduled report can saturate the connection pool at any time.
- debugging-06: The export job loses the race for connections unpredictably.
- debugging-06: The failures occur on a weekly frequency.
- debugging-06: Weekly failure frequency suggests a periodic job on the analytics side rather than pure randomness.
- debugging-06: A weekly report, batch refresh, or vacuum/maintenance task could be the periodic analytics-side job.
- debugging-06: A pool size too small for the combined peak load of both services is a plausible cause.
- debugging-06: An undersized pool is a capacity problem rather than a bug.
- debugging-06: A connection leak in either service is a plausible cause.
- debugging-06: A connection leak starves the pool slowly until it clears itself.
- debugging-06: Long-running or blocking queries on the analytics side are a plausible cause.
- debugging-06: Large scans and locks can cause connections to be held rather than released.
- debugging-06: Database-side resource pressure from CPU, I/O, or lock contention is a plausible cause.
- debugging-06: Database-side resource pressure slows query completion and indirectly holds pool connections longer.
- debugging-06: The failure window was 02:14:07 to 02:14:41 on 2026-07-29.
- debugging-06: There were prior failure nights before 2026-07-29.
- debugging-06: Analytics service logs and database slow-query logs can be correlated by timestamp to see what else was running.
- debugging-06: Pool size, active connections, and wait queue length can be tracked as pool metrics over time.
- debugging-06: A saturation pattern originating from the analytics side would confirm contention.
- debugging-06: Connection leaks can be checked via ORM/driver stats.
- debugging-06: `pg_stat_activity` can be used to check for connection leaks if the database is Postgres.
- debugging-06: If max pool size multiplied by concurrent workers from both services can exceed available connections, that is the root cause rather than any single bug.
- debugging-06: Running the export job while replaying typical analytics load can reproduce the pool exhaustion on demand.
- debugging-06: Possible fixes include separating pools per service, increasing pool size, or scheduling analytics jobs away from the export window.
- debugging-07: The most plausible cause of the failure is a race between event creation and digest generation.
- debugging-07: The race only surfaces under CPU contention.
- debugging-07: The failure is not a bug in the test's assertions themselves.
- debugging-07: The test fails approximately 10% of runs.
- debugging-07: The failure occurs only under parallel load.
- debugging-07: There are no artifacts available to confirm the cause.
- debugging-07: Four specific mechanisms fit the observed symptom.
- debugging-07: The test creates three events and then requests a digest.
- debugging-07: If event creation returns before the write is durable or visible, the digest query can run before the third event commits.
- debugging-07: Async queues, eventual-consistency indexes, and read replicas can cause event creation to return before the write is visible.
- debugging-07: A digest reading before the third write lands is the single most common cause of 'N-1 of N' flakes of this shape.
- debugging-07: If the digest scopes events by a wall-clock window, contention slowing an API call can push an event's timestamp to the wrong side of the window boundary.
- debugging-07: Serial runs are fast enough that all three events always land inside the time window.
- debugging-07: Parallel runs occasionally fail to land all three events inside the time window.
- debugging-07: Four workers are hitting a shared database.
- debugging-07: If the test does not scope events to a unique account, tenant, or time range, a concurrently running test could delete, expire, or interfere with one of the three events before the digest reads them.
- debugging-07: If events are deduplicated by a timestamp truncated to the second, two events created in rapid succession under load could collide onto the same dedup key and merge into one.
- debugging-07: Running the test file repeatedly with `pytest -n4 --count=50` locally can reproduce the parallelism dependency.
- debugging-07: If the test fails locally at a similar rate under parallelism, parallelism is confirmed as a factor rather than a CI artifact.
- debugging-07: Reproducing the failure locally rules out the explanation that CI hardware is simply different.
- debugging-07: CI drops the test artifacts.
- debugging-07: Logging worker id, event IDs, and timestamps at creation and at digest read will reveal which event went missing and when on the next CI failure.
- debugging-07: Temporary logging can be landed behind a flag or merged temporarily.
- debugging-07: Hardcoded account IDs, user IDs, or fixed timestamps in the test or fixture can collide across xdist workers.
- debugging-07: Shared identifiers explain a large fraction of bugs that are flaky only in parallel.
- debugging-07: If adding a poll or wait for all three events to be indexed before requesting the digest makes the flake disappear, that confirms the eventual-consistency cause rather than the other three.
- debugging-07: Inspecting the digest window logic in the source is about a five-minute read.
- debugging-07: Reading the source can confirm or rule out the time-boundary and dedup-key causes without a live reproduction.
- debugging-07: Grepping for shared IDs and reading the digest windowing code are both cheap steps.
- debugging-07: Grepping for shared IDs and reading the digest windowing code often surface the answer before reproduction is needed.
- debugging-08: Campaign weeks push more webhook traffic.
- debugging-08: The correlation between traffic volume and growth points to a per-request accumulation bug.
- debugging-08: A per-request accumulation bug can consist of listeners, timers, or promises registered per request and never cleaned up.
- debugging-08: Because the canary grows without webhooks, something runs on a timer or on every process tick regardless of external load.
- debugging-08: Candidates for traffic-independent growth are a scheduled job, a connection pool, or a logger/metrics buffer that grows unbounded.
- debugging-08: A count-bounded cache would not explain the canary's growth if the cache is fed by webhook-triggered writes.
- debugging-08: Failure to return to baseline overnight is normal for a real memory leak.
- debugging-08: Failure to return to baseline overnight also matches memory fragmentation from an allocator that does not return pages to the OS.
- debugging-08: Failure to return to baseline overnight also matches a connection or object pool that grows under load and never shrinks.
- debugging-08: If heap-used stays flat while RSS climbs, the cause is fragmentation rather than a leak.
- debugging-08: Fragmentation requires a different fix than a memory leak.
- debugging-08: A heap snapshot diff would confirm or rule out the first three hypotheses without guesswork.
- explanation-01: The trade-off between chaining and open addressing is memory versus speed under load.
- explanation-02: An editor loading a wiki page reads the page along with its version number.
- explanation-02: An optimistic save runs UPDATE pages SET content=?, version=version+1 WHERE id=? AND version=?.
- explanation-03: A network path may cross a slow home Wi-Fi link or a fast data-center backbone.
- explanation-03: Congestion collapse events occurred in the late 1980s.
- explanation-04: The memory-ownership difference between processes and threads drives almost everything else that distinguishes them.
- explanation-04: Parsing untrusted input, running a plugin, and calling flaky native code are examples of work that might crash or hang.
- explanation-04: A web server handling many connections against the same in-memory cache is a case where threads win.
- explanation-05: Cached results, session data, and log entries are examples of entries that accumulate in unbounded collections.
- explanation-06: Slowness can come from serialization overhead.
- explanation-06: The read-to-write mix can be measured by examining query logs or adding simple counters.
- explanation-06: Profiling and read-to-write data reveal which endpoints or queries should be cached first.
- explanation-07: Sharding only helps with storage and write throughput, not query latency.
- explanation-07: Sharding typically helps with write throughput only once a single node saturates.
- explanation-07: Table partitioning helps with query performance.
- summarization-01: The release includes build tooling changes.
- summarization-01: The release includes an internal module refactor.
- summarization-01: The release includes telemetry batching changes.
- summarization-01: The build tooling, internal module refactor, and telemetry batching changes are internal and do not affect app behavior.
- summarization-02: The change shipped unnoticed until checkout errors appeared more than 12 hours later.
- summarization-02: Detection and recovery were fast.
- summarization-02: The page went out at 09:21.
- summarization-02: The rollback resolved the issue by 09:48.
- summarization-02: The gap to close is prevention rather than response time.
- summarization-04: The bug was reproduced on the latest version of Firefox.
- summarization-06: A restart resolved the checkout service errors.
- summarization-06: The team suspects connection-pool exhaustion in the payments client caused the incident.
- summarization-07: Staging runs a newer kernel.
- summarization-07: The newer kernel on staging offers a possible explanation for the crash.
- summarization-07: The recommendation is to treat the latency win as real.
- summarization-07: The recommendation is to obtain profiling and a production-like traffic test before ruling on memory and crash risk.
- summarization-08: The participants had existing templates.

### classic-concise

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 28 | 20 | 0.714 | 18 | 0 |
| code-review-02 | 19 | 12 | 0.632 | 19 | 7 |
| code-review-03 | 24 | 15 | 0.625 | 14 | 1 |
| code-review-04 | 26 | 19 | 0.731 | 18 | 11 |
| code-review-05 | 27 | 19 | 0.704 | 30 | 2 |
| code-review-06 | 38 | 20 | 0.526 | 21 | 7 |
| code-review-07 | 30 | 22 | 0.733 | 29 | 6 |
| code-review-08 | 34 | 28 | 0.824 | 37 | 8 |
| debugging-01 | 7 | 7 | 1.0 | 6 | 0 |
| debugging-02 | 19 | 9 | 0.474 | 9 | 0 |
| debugging-03 | 10 | 6 | 0.6 | 3 | 0 |
| debugging-04 | 15 | 9 | 0.6 | 7 | 0 |
| debugging-05 | 17 | 15 | 0.882 | 12 | 1 |
| debugging-06 | 4 | 0 | 0.0 | 31 | 31 |
| debugging-07 | 0 | 0 | n/a | 34 | 34 |
| debugging-08 | 28 | 10 | 0.357 | 29 | 11 |
| explanation-01 | 39 | 30 | 0.769 | 28 | 2 |
| explanation-02 | 24 | 19 | 0.792 | 19 | 0 |
| explanation-03 | 35 | 28 | 0.8 | 26 | 6 |
| explanation-04 | 39 | 30 | 0.769 | 26 | 2 |
| explanation-05 | 18 | 16 | 0.889 | 9 | 0 |
| explanation-06 | 21 | 18 | 0.857 | 14 | 2 |
| explanation-07 | 26 | 15 | 0.577 | 25 | 8 |
| explanation-08 | 18 | 11 | 0.611 | 11 | 4 |
| summarization-01 | 5 | 5 | 1.0 | 6 | 1 |
| summarization-02 | 12 | 10 | 0.833 | 10 | 0 |
| summarization-03 | 13 | 10 | 0.769 | 10 | 0 |
| summarization-04 | 13 | 10 | 0.769 | 9 | 1 |
| summarization-05 | 9 | 7 | 0.778 | 10 | 2 |
| summarization-06 | 12 | 10 | 0.833 | 13 | 0 |
| summarization-07 | 14 | 14 | 1.0 | 12 | 2 |
| summarization-08 | 20 | 13 | 0.65 | 18 | 3 |

Median fraction: 0.769 over 31 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python footgun.
- code-review-01: Duplicate roles aren't prevented.
- code-review-01: Calling the function with `roles=["member"]` explicitly produces `["member", "member"]`.
- code-review-01: The function has no docstring and no type hints.
- code-review-01: Missing type hints is a minor issue.
- code-review-01: Type hints of `name: str`, `roles: list[str] | None`, and a type for `db` would clarify the function's contract.
- code-review-01: A safer rewrite uses `roles=None` as the default and raises `ValueError` when `name` or `db` is missing.
- code-review-01: The safer rewrite copies `roles` with `list(roles)` and appends `"member"` only if it is not already present.
- code-review-02: The function always returns a rejected promise almost instantly, due to the TypeError.
- code-review-02: There is no validation that the response `data` has a `name` property.
- code-review-02: If the API returns an error object instead of a profile, `data.name` could be `undefined` and calling `.toUpperCase()` on it would throw.
- code-review-02: There is no input validation on `userId`.
- code-review-02: Unsanitized/unencoded `userId` could allow injection of unexpected path segments such as `../` or query-like content.
- code-review-02: `encodeURIComponent(userId)` can be used to encode `userId` before interpolating it into the URL.
- code-review-02: The fixed version awaits `fetch` with an encoded `userId`, throws an Error including `res.status` when `!res.ok`, awaits `res.json()`, throws an Error when the response is missing `name`, and returns `data.name.toUpperCase()`.
- code-review-03: The correct parameter placeholder depends on the database driver.
- code-review-03: sqlite3 uses `?` as its parameter placeholder.
- code-review-03: psycopg2 uses `%s` as its parameter placeholder.
- code-review-03: pymysql uses `%s` as its parameter placeholder.
- code-review-03: Explicitly listing the needed columns is better than using `SELECT *`.
- code-review-03: `fetchall` can raise an exception, for example on a bad connection or a database error.
- code-review-03: The function imposes no limit on the number of results returned.
- code-review-03: A broad match could return an unbounded number of rows.
- code-review-03: Pagination or a `LIMIT` clause should be considered to bound the result set.
- code-review-04: Python's GIL guarantees that each individual bytecode operation is atomic.
- code-review-04: Under contention, the counter class will systematically undercount.
- code-review-04: A single assignment is atomic in CPython.
- code-review-04: `reset` by itself will not corrupt the counter's state.
- code-review-04: An example of the reset/increment race is resetting to 0 and then a stale increment writing 1.
- code-review-04: The class has no thread-safety documentation or contract.
- code-review-04: A caller reading the code has no way to know the class is unsafe under concurrent use.
- code-review-05: `cd "$BACKUP_DIR" || exit 1` is the correct form.
- code-review-05: `rm -rf` given a literal unmatched pattern typically errors out harmlessly in POSIX sh.
- code-review-05: Bash has a `nullglob` option affecting unmatched glob behavior.
- code-review-05: `rm -rf *.tmp` is the most dangerous line in the script.
- code-review-05: When no .log files exist, `ls *.log` prints an error to stderr and returns nothing usable.
- code-review-05: `echo Cleaned $BACKUP_DIR` uses an unquoted variable and should be `echo "Cleaned $BACKUP_DIR"`.
- code-review-05: Without `set -u`, the missing-argument problem passes silently.
- code-review-05: The `-r` flag is unnecessary for `rm` because the targets are files, not directories.
- code-review-06: Resolving the `None`-means-delete ambiguity requires a sentinel such as a `DELETE` marker if both behaviors are needed.
- code-review-06: Silently no-oping on a missing key can hide a typo, such as a misspelled key intended to delete something.
- code-review-06: If `base[key]` is a dict and `override[key]` is not a dict, the `elif` branch fails and control falls to the `else` branch.
- code-review-06: In that case the entire nested dict is replaced by the scalar value.
- code-review-06: No validation or error is raised for either type-mismatch case.
- code-review-06: The type-mismatch behavior could mask a configuration mistake.
- code-review-06: Recursion depth follows the depth of `override`'s nested dicts.
- code-review-06: There is no depth limit on the recursion.
- code-review-06: Deeply nested or self-referential structures could cause a `RecursionError` or an infinite loop if a dict contains itself.
- code-review-06: Self-referential structures are unlikely for JSON-like config but possible if `base` or `override` are constructed programmatically.
- code-review-06: There is no check that keys are hashable or strings.
- code-review-06: `isinstance(merged[key], dict)` also matches dict subclasses.
- code-review-06: Recursing into an `OrderedDict` or custom dict subclass via `merge_settings` returns a plain `dict`, losing the subclass type.
- code-review-06: Ansible and Kubernetes strategic merge patches use conventions similar to `None`-as-delete.
- code-review-06: The shallow-copy aliasing issue and the silent type-mismatch overwrite are almost certainly bugs or oversights.
- code-review-06: Those two issues tend to pass testing and later cause hard-to-trace mutation bugs or config-clobbering incidents in production.
- code-review-06: Issues #1 and #4 are the highest-priority items to write tests around and confirm intent for.
- code-review-06: Issues #1 and #4 are the ones most likely to fail silently.
- code-review-07: Every other failure path in the function explicitly returns null.
- code-review-07: The function has three different signals for failure: a thrown error that never happens, null, and undefined.
- code-review-07: The inconsistency in failure signals indicates the retry-exhaustion path was never tested.
- code-review-07: Swallowing non-HTTP errors as null is the most dangerous issue in the code, especially with callers that cannot be audited.
- code-review-07: Discarding errors without a trace can cause silent data corruption downstream in a shared library with unknown callers.
- code-review-07: Most retry helpers use exponential backoff to avoid synchronized retry storms across clients.
- code-review-07: The attempts semantics are not a bug.
- code-review-07: Changing the undefined case or making the function throw would be a breaking change if callers currently check === null to detect failure.
- code-review-08: The script has no dry-run mode.
- code-review-08: `os.listdir()` loads the entire directory listing into memory at once.
- code-review-08: The in-memory listing is acceptable for modest directories and only a concern if `ROOT` grows very large.
- code-review-08: Iteration order is filesystem-dependent and not sorted by age.
- code-review-08: Because iteration order is arbitrary, which files survive when the 500 cap is reached is effectively arbitrary rather than oldest-first.
- code-review-08: The two highest-priority changes are guarding against directories and requiring a minimum age before deleting `.part`/`tmp-` files.
- debugging-02: Class bodies are always in strict mode.
- debugging-02: Strict mode propagates to functions nested inside strict-mode code.
- debugging-02: A regular `function () {...}` passed to `setInterval` from inside a class method has `this === undefined` when called.
- debugging-02: Accessing `this.seconds` when `this` is `undefined` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: Seeing `NaN` instead of a thrown error indicates the code is running in a non-strict/sloppy context.
- debugging-02: Running code directly in a browser `<script>` without `"use strict"` is an example of a non-strict/sloppy context.
- debugging-02: Some transpilation does not preserve strict mode, producing a sloppy-mode context.
- debugging-02: Calling `.bind(this)` on the callback function is an alternative fix.
- debugging-02: Storing `const self = this;` before `setInterval` and using `self` inside the callback is an alternative fix.
- debugging-02: The arrow function is the cleanest modern approach among these fixes.
- debugging-03: The corrected `moving_sum` function iterates with `for i in range(len(values) - window + 1)`.
- debugging-03: The corrected `moving_sum` function appends `sum(values[i : i + window])` to a list named `sums` on each iteration.
- debugging-03: The corrected `moving_sum` function returns `sums`.
- debugging-03: `moving_sum` computes the sum of each window of the given size.
- debugging-04: The 0xc3 byte likely represents an accented character such as é or ü.
- debugging-04: The non-ASCII byte occurs at byte offset 512 in the file.
- debugging-04: Encoding can be detected at runtime with libraries such as charset-normalizer or chardet.
- debugging-04: Detecting the encoding is preferable to hardcoding one when the encoding is not known ahead of time.
- debugging-04: For line counting, UTF-8 with errors="replace" is usually the pragmatic fix.
- debugging-04: The errors="surrogateescape" option preserves byte fidelity.
- debugging-05: The same test running twice can also cause the extra `"post"` entries, for example via test discovery, parametrization, or fixtures.
- debugging-05: In the fixed code, `make_post` is defined as `def make_post(title, tags=None)` and sets `tags = list(DEFAULT_TAGS)` when `tags is None`.
- debugging-06: The speaker intends to check memory for prior context on the system.
- debugging-06: A tool call was made to list files and directories in a given path.
- debugging-06: The status of that tool call was 'Completed'.
- debugging-06: The tool call's terminal output was 'No files found'.
- debugging-08: Campaign products can have larger payloads, more images and variants, and richer JSON than normal products.
- debugging-08: The count-bounded-cache explanation fits all four reported observations.
- debugging-08: Cache entries persist until they are evicted, so cache-driven memory growth survives quiet nights.
- debugging-08: Any traffic populates the cache, so cache-driven growth occurs even without webhooks.
- debugging-08: The count-bounded-cache explanation does not require the configured bound to have changed.
- debugging-08: Guava and Caffeine caches offer a `maximumSize` setting and a `maximumWeight` setting.
- debugging-08: Long-lived maps used for deduplication, idempotency keys, rate limiting, or session and request tracking are a classic source of leaks when their TTL cleanup is absent, broken, or slow.
- debugging-08: Such leaky maps are typically keyed by request ID, order ID, webhook event ID, or correlation ID.
- debugging-08: Dynamically generated classes from serialization libraries, proxies, or template engines leak metaspace rather than heap.
- debugging-08: More campaign SKUs and variants can produce more dynamically generated types.
- debugging-08: Classes are not unloaded until their classloader is garbage collected.
- debugging-08: Application classloaders often are never garbage collected.
- debugging-08: `jstat -gc` or an APM memory breakdown can distinguish heap growth from non-heap/metaspace growth.
- debugging-08: Off-heap leaks are consistent with growth that survives quiet nights and correlates with traffic volume.
- debugging-08: If RSS grows well beyond JVM-reported heap usage, the growth is native or off-heap.
- debugging-08: The cache-bound hypothesis is the only one of the four consistent with all four clues without positing an additional leak.
- debugging-08: Switching the cache to weight-based eviction would be a one-line fix.
- debugging-08: The canary-still-grows observation is the strongest evidence that something grows independently of the cache.
- explanation-01: The collection in a chained slot is usually a linked list, and sometimes a small array or tree.
- explanation-01: Quadratic probing tries indices at increasing squared steps.
- explanation-01: Double hashing uses a second hash function to decide the step size.
- explanation-01: Open addressing can fail entirely if the array is full.
- explanation-01: Deletion in open addressing usually needs tombstone markers.
- explanation-01: Chaining eventually needs resizing, but less urgently than open addressing.
- explanation-01: Open addressing needs resizing sooner and must be kept well below full, often under a 70% load factor.
- explanation-01: Java converts long chains to trees for performance.
- explanation-01: Many high-performance C++ hash maps use open addressing.
- explanation-02: The SQL FOR UPDATE clause locks the row until the transaction commits or rolls back.
- explanation-02: In optimistic locking, the WHERE version = N check catches conflicts at commit time.
- explanation-02: Optimistic locking fits for long-lived transactions or when there is user think time between read and write, such as editing a form in a browser.
- explanation-02: Holding a database lock during user think time would be wasteful.
- explanation-02: As a rule of thumb, use optimistic locking for low-contention scenarios or when there is a gap between read and write that a lock shouldn't span, such as multi-step user edits and web forms.
- explanation-03: Before congestion control existed, dropped packets could snowball into congestion collapse.
- explanation-03: Congestion collapse is when a congested network becomes even more congested because senders keep retransmitting lost data.
- explanation-03: The initial cwnd is now typically 2-10 segments per RFC 6928.
- explanation-03: Reaching a reasonable sending rate quickly matters a lot for short connections such as most web requests.
- explanation-03: After detecting loss, TCP switches to a more cautious, linear growth phase called congestion avoidance.
- explanation-03: This congestion control philosophy is why the internet has remained stable even as usage grew enormously.
- explanation-03: Every TCP connection cooperates to avoid overwhelming shared links rather than assuming its capacity upfront.
- explanation-04: Each thread has its own stack and register/instruction pointer state.
- explanation-04: Processes communicate via IPC mechanisms such as pipes, sockets, and shared memory, which is slower than thread communication.
- explanation-04: Nginx and Apache use worker processes.
- explanation-04: The OS lets you set per-process limits on memory, CPU, and file descriptors via cgroups and ulimits.
- explanation-04: Per-process resource limits are hard or impossible to apply to a single thread within a shared process.
- explanation-04: Separate processes make it straightforward to restart, upgrade, or scale components independently.
- explanation-04: Microservices and worker pools are examples of components with independent lifecycles that can be killed and respawned.
- explanation-04: I/O-bound tasks wait on network or disk.
- explanation-04: Processes are preferable when you need true CPU parallelism, fault or security isolation, or independent resource control.
- explanation-05: Global emitters and DOM elements are examples of long-lived objects.
- explanation-05: Caches without a TTL, without a size limit, or using strong keys instead of weak references are unbounded.
- explanation-06: A cache does not help when slowness comes from a slow external API call.
- explanation-06: A cache does not help when slowness comes from lock contention caused by writes.
- explanation-06: Slow query logs and DB metrics show whether the database is CPU or IO bound or whether the app is slow elsewhere.
- explanation-07: The product team's inability to estimate growth is the real problem.
- explanation-07: A growth rate of about 10% in GB is fine for years.
- explanation-07: A growth rate of 10x per year changes the calculus.
- explanation-07: Sharding solves horizontal scaling, not disk cost.
- explanation-07: Cheaper alternatives to sharding include indexing, partitioning within one instance, read replicas, connection pooling, archiving cold data, and vertical scaling.
- explanation-07: Sharding now locks in a shard key before access patterns are understood.
- explanation-07: If the shard key choice is wrong, resharding later is a major migration.
- explanation-07: Partitioning can be time-based or tenant-based and still run on a single instance.
- explanation-07: Partitioning and read replicas are reversible.
- explanation-07: Partitioning and read replicas buy significant headroom.
- explanation-07: Tracking actual growth for a few months makes the shard-key decision evidence-based rather than guessed.
- explanation-08: Protobuf and msgpack are examples of binary formats.
- explanation-08: JSON has overhead from quotes, keys repeated per record, and text-encoded numbers.
- explanation-08: JSON's overhead matters most for large arrays of small objects or numeric-heavy data.
- explanation-08: If payloads are already small or mostly free-text strings, binary formats provide little size benefit.
- explanation-08: If most latency comes from DB queries, business logic, or network round-trips, even a 5-10x faster serializer might reduce total request time by only low single-digit percent.
- explanation-08: Most languages allow wrapping JSON encode/decode in a timer or using a profiler to measure it.
- explanation-08: Switching to a binary format has real costs: schema management, tooling, debuggability, and client compatibility.
- summarization-02: The staging pool size of 5 was intended to be small.
- summarization-02: The incident ran from 09:14 to 09:48 UTC.
- summarization-03: Thumbnail generation currently ties up web workers.
- summarization-03: Under the proposal, uploads would store the original image.
- summarization-03: A worker pool would generate the thumbnails and update the record.
- summarization-04: After clicking the PDF export option, nothing happens initially.
- summarization-04: The error banners provide no further error details.
- summarization-04: The issue was reproduced by a second user on a different machine.
- summarization-05: Ada is assigned to run the payments database migration dry run.
- summarization-05: Ada is assigned to check with the mobile team lead about whether the mobile team has been informed of the API deprecation.
- summarization-06: The on-call engineer suspects connection-pool exhaustion in the payments client caused the checkout service errors.
- summarization-06: Recovery after a restart is consistent with several possible causes.
- summarization-08: The findings are based on 8 customer interviews.
- summarization-08: The progress bar finding is rated FIRM for the behavior and TENTATIVE for the cause.
- summarization-08: 2 of those 3 participants abandoned the import as a result.
- summarization-08: The abandonment behavior is a real, actionable problem regardless of its cause.
- summarization-08: The template gallery finding is rated TENTATIVE.
- summarization-08: The template gallery is a new feature.
- summarization-08: Follow-up with new or template-less users is needed before drawing conclusions about the template gallery.

Added facts (styled only):

- code-review-02: Calling `.toUpperCase()` on the undefined `profile.name` throws `TypeError: Cannot read properties of undefined`.
- code-review-02: A failed fetch can result from a network error or a non-2xx status.
- code-review-02: As written, the promise returned by `loadProfile` resolves to `undefined`.
- code-review-02: The promise resolves to `undefined` because the synchronous `return` fires before the assignment to `profile`.
- code-review-02: The listed problems are ordered by severity, with the race condition being the most severe.
- code-review-02: The fixed version awaits `fetch(`/api/users/${userId}`)` and stores the result in `res`.
- code-review-02: The fixed version awaits `res.json()` to obtain `profile` and returns `profile.name.toUpperCase()`.
- code-review-03: A schema change can silently break callers that index into rows by position.
- code-review-04: A reset can occur between another thread's read and write, silently discarding progress.
- code-review-04: The original code provides no way to read `value` safely.
- code-review-04: Callers likely access `counter.value` directly.
- code-review-04: Directly accessing `counter.value` can observe a torn or stale value while another thread is mid-increment.
- code-review-04: The risk of reading a torn or stale value is less severe under the GIL for a single int.
- code-review-04: Safe reads of a plain attribute are not guaranteed by any contract even under the GIL.
- code-review-04: Future changes, such as using non-atomic types, would break the safety of direct attribute reads.
- code-review-04: In the fix, `increment` acquires the lock before performing `self._value += 1`.
- code-review-04: In the fix, `reset` acquires the lock before setting `self._value` to 0.
- code-review-04: In the fix, `value` is exposed as a property that acquires the lock before returning `self._value`.
- code-review-04: In the fix, the counter's state is stored in a private attribute named `_value` initialized to 0.
- code-review-05: The script prints "Cleaned" even when a step failed.
- code-review-05: The script uses `rm -rf` with no confirmation and no dry-run option.
- code-review-06: If `merged[key]` is a dict but `override[key]` is not, the code recurses into `merge_settings` with a non-dict second argument.
- code-review-06: The recursive call calls `.items()` on the non-dict value and raises `AttributeError`.
- code-review-06: The code never checks that `value` is a dict before recursing.
- code-review-06: New keys and non-dict values are assigned by reference via `merged[key] = value`.
- code-review-06: If `value` is a dict or list from `override`, `merged` holds the same object as `override`.
- code-review-06: Later mutation of the merged result or of the original `override` will silently affect the other.
- code-review-06: Adding an `isinstance(value, dict)` check before recursing fixes the crash.
- code-review-07: The first-backoff bug is an off-by-one; the intended expression was probably `1000 * (i + 1)`.
- code-review-07: There is no cap on backoff growth.
- code-review-07: If `attempts <= 0`, the function never calls `fn` and returns undefined.
- code-review-07: The `attempts <= 0` case is a silent no-op.
- code-review-07: The fail-soft behavior should at minimum be limited to known error shapes.
- code-review-07: The execution of the backoff has an off-by-one, no jitter, and no cap.
- code-review-08: os.path.getmtime and os.remove raise IsADirectoryError if the path is a directory.
- code-review-08: getmtime follows the symlink target rather than the link itself.
- code-review-08: A dangling symlink raises FileNotFoundError and crashes the loop.
- code-review-08: The dangling-symlink crash shares its root cause with the missing exception handling.
- code-review-08: The 500 throttle is presumably meant to avoid hammering the filesystem or triggering a burst of I/O.
- code-review-08: If the backlog consistently exceeds 500 files, the throttle silently caps cleanup below the inflow rate.
- code-review-08: Under a persistent backlog, old files accumulate forever with no alert.
- code-review-08: Before changing anything, one should find out what 'removed' is used for downstream, such as metrics or alerting.
- debugging-05: In the fixed version, tags is set to list(tags) if tags is not None, otherwise ["draft"].
- debugging-06: Connection pool exhaustion is the likely cause of the failures.
- debugging-06: Analytics service contention is the most probable cause.
- debugging-06: The database is shared between the export process and an analytics service.
- debugging-06: The shared database's connection pool fills with analytics queries at the same time the export runs.
- debugging-06: The batch number at which the failure occurs varies between occurrences.
- debugging-06: Because the batch number varies, the trigger is time-based rather than data-based.
- debugging-06: A time-based trigger is consistent with a competing job running on its own schedule, such as an hourly rollup or a cron report.
- debugging-06: That competing job sometimes overlaps with the export window.
- debugging-06: A connection leak in the export worker is a possible cause.
- debugging-06: If a prior batch fails to release its connection, the pool shrinks over the course of the run.
- debugging-06: Exceptions in batch processing can skip a `finally` block or context-manager cleanup.
- debugging-06: The pool may be sized too small for peak concurrency.
- debugging-06: If worker count or batch parallelism grew over time, the pool may be undersized for the combined load.
- debugging-06: A slow query from either service holding connections is a possible cause.
- debugging-06: One long-running analytics query can starve the pool for all other clients, even at modest concurrency.
- debugging-06: Correlating failure timing rather than batch number is a way to narrow down the cause.
- debugging-06: Analytics service logs and database slow-query logs can be pulled for the failure timestamps across several occurrences.
- debugging-06: If failures cluster around a recurring analytics job time, that indicates the analytics contention cause.
- debugging-06: Most connection pool libraries expose active, idle, and waiting connection counts.
- debugging-06: If active connections were pegged at max before the timeout, that confirms pool exhaustion.
- debugging-06: Pool metrics can show whether connections were held by the export worker itself (a leak) or by other clients (contention).
- debugging-06: Temporary logging of connection checkout and checkin with query context can reveal which query holds each connection.
- debugging-06: Such logging would show who is holding connections at the next occurrence.
- debugging-06: A database's own connection view, such as `pg_stat_activity`, can be queried directly.
- debugging-06: A monitoring job can snapshot the connection view every minute overnight.
- debugging-06: Such a snapshot job is cheap to add and provides evidence without waiting on log rotation.
- debugging-06: The export code can be grepped for places where connections are acquired without a guaranteed release.
- debugging-06: Error and retry paths are especially likely places for leak patterns.
- debugging-06: The export retries and fails again on the second attempt.
- debugging-06: The retry-and-fail-again pattern suggests the second attempt may start with a pool already partly consumed.
- debugging-06: Pool metrics and a `pg_stat_activity` snapshot are the cheapest diagnostics to add and the most likely to catch the culprit on the next occurrence.
- debugging-07: The most likely cause of the failure is a race condition.
- debugging-07: The test setup uses four parallel workers.
- debugging-07: The test seeds events and then reads a digest.
- debugging-07: Shared state is a likely cause, where all workers hit the same database or queue.
- debugging-07: With shared state, another worker's cleanup or event can pollute or steal from a test.
- debugging-07: A timing gap is a likely cause, where the digest read fires before the third event's write commits.
- debugging-07: An async write, eventual consistency, or a delayed background job that builds the digest can cause the timing gap.
- debugging-07: A test isolation leak is a plausible cause, where events are keyed by a non-unique field such as user id or time window.
- debugging-07: Non-unique keying lets parallel workers collide so an event gets overwritten or double-counted elsewhere.
- debugging-07: Non-atomic seeding is a plausible cause, where the three seed calls aren't awaited or confirmed before the digest call.
- debugging-07: CI is slower and noisier than a dev box.
- debugging-07: Under load, the third write may not have landed before the digest call.
- debugging-07: The digest logic may contain a real bug that only surfaces under load.
- debugging-07: A dedup step keyed on a timestamp with insufficient resolution can collapse two events created in the same millisecond into one.
- debugging-07: An off-by-one window boundary can cause the third event to be dropped.
- debugging-07: Resource contention can cause a request to silently fail or time out and be treated as success due to an unchecked return value on the seed call.
- debugging-07: Reproducing the parallelism rather than just the test is a way to narrow down the cause.
- debugging-07: The single test file can be run repeatedly under a parallel flag such as -n 4 in a loop until it fails locally.
- debugging-07: A shell loop such as `for i in $(seq 1 50); do pytest ... ; done` can be used to repeat the test.
- debugging-07: If the test never fails locally, the CI box's slower and shared resources matter, not just worker count.
- debugging-07: Running 4 workers with each worker given its own DB or schema distinguishes isolation problems from timing problems.
- debugging-07: Most parallel test runners support giving each worker its own database or schema.
- debugging-07: If failures disappear under per-worker databases, the cause is a data isolation leak rather than timing.
- debugging-07: Adding explicit synchronization means asserting each seed call's response before issuing the next.
- debugging-07: If the API is async, the test can poll or wait for the event to be queryable before requesting the digest.
- debugging-07: If explicit synchronization fixes the failure, the cause is a race between write and read rather than application logic.
- debugging-07: Turning on artifacts means running the flaky test in a tight local retry loop with logging and tracing enabled.
- debugging-07: Useful artifacts include SQL logs, event IDs returned by each seed call, and the digest response body.
- debugging-07: Captured failure artifacts show which event went missing and whether it exists in the store at all.
- debugging-07: Checking for shared fixtures and global counters involves grepping for module-level or session-scoped fixtures the test relies on.
- debugging-07: Examples of shared fixtures include a test user, a time-window clock, and a singleton event bus.
- debugging-07: Shared fixtures and global counters are a classic source of cross-worker interference.
- debugging-07: Steps 1 and 2 should be done first.
- debugging-07: Steps 1 and 2 will reveal within an afternoon whether the race is in the test setup or in the application.
- debugging-08: Scheduled jobs, connection pool churn, metrics/logging buffers, thread-local accumulation, classloader/metaspace growth, and off-heap/direct buffers are candidate sources of a base leak.
- debugging-08: Periodic `jcmd GC.class_histogram` snapshots on the canary can be diffed over several hours to find a class whose instance count climbs without bound.
- debugging-08: A heap histogram will not show off-heap growth.
- debugging-08: Unclosed listeners/callbacks, per-request entries appended to a long-lived collection, and futures/subscriptions never cleaned up are candidate request-proportional leaks.
- debugging-08: If growth tracks requests linearly, heap histograms taken on a loaded production instance before and after a traffic burst can reveal collections whose size scales with request count.
- debugging-08: Evicted cache entries can be kept alive by a stray reference elsewhere, such as a listener, index, or thread-local.
- debugging-08: One can confirm whether evictions actually fire at the configured bound.
- debugging-08: One can check whether evicted keys still appear in a heap histogram or dump after eviction, indicating retention by another reference.
- debugging-08: Delayed GC of an actually-growing live set is a possible non-leak explanation worth ruling out.
- debugging-08: Old-gen occupancy immediately after a full GC is more informative than raw heap usage.
- debugging-08: If post-GC old-gen occupancy trends upward day over day, the problem is a real leak rather than fragmentation or GC laziness.
- explanation-01: Chaining wastes memory on list overhead for mostly-empty buckets.
- explanation-01: Rust's HashMap uses open addressing.
- explanation-03: A network path may cross a fast local link and then a congested backbone, which the sender cannot observe from its end.
- explanation-03: Sending too slow wastes capacity the connection could have used.
- explanation-03: Every segment in the current window can trigger an ACK.
- explanation-03: In congestion avoidance, window growth is linear, roughly +1 segment per RTT.
- explanation-03: On packet loss, the sender cuts ssthresh, often to half the current window.
- explanation-03: After packet loss, the sender either restarts slow start from a small window or moves directly into congestion avoidance, depending on the algorithm.
- explanation-04: Ruby has a global interpreter lock.
- explanation-04: Even without a GIL, running independent processes avoids contention on shared data structures and locks.
- explanation-06: A cache trades write cost for read speed.
- explanation-06: A cache can hide the real bottleneck when the slowness originates elsewhere.
- explanation-07: Write saturation can come from CPU, I/O, or lock contention.
- explanation-07: Current disk, IOPS, and connection usage indicate how much headroom is left.
- explanation-07: Being at 20% utilization means years of runway rather than months.
- explanation-07: After sharding, every query, migration, and analytics job needs shard-awareness.
- explanation-07: Cross-shard transactions and joins become slow or impossible without new tooling.
- explanation-07: Sharding too early can consume months of engineering effort on infrastructure the product did not yet need.
- explanation-07: Sharding too late risks downtime or data-consistency problems during the cutover.
- explanation-07: Picking a shard key early in the schema, even if unused, makes a future split cheaper.
- explanation-08: Any estimate made without measurements would be a guess presented as an answer.
- explanation-08: If parsing JSON takes 2% of a request's time, a binary format that halves parse time saves 1%.
- explanation-08: If parsing JSON takes 40% of a request's time, a binary format that halves parse time saves 20%.
- explanation-08: Profiling production requests, sampling payload sizes, and prototyping the binary format yields an actual expected improvement rather than a guess.
- summarization-01: Cold start time has been reduced by about 40%.
- summarization-04: Clicking Export and choosing PDF causes an "export failed" banner to appear.
- summarization-05: Ada is assigned to confirm that the payments database dry run happens before Thursday.
- summarization-05: There is an API deprecation notice.
- summarization-07: The worker crash may trace to staging's newer kernel rather than a batcher bug.
- summarization-07: Staging runs a newer kernel than production.
- summarization-08: The claim that the progress bar drives abandonment on large files is characterized as tentative.
- summarization-08: The link between the progress bar and abandonment needs more data.
- summarization-08: The non-use of the template gallery is not counted as a finding.

### concise

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 28 | 20 | 0.714 | 22 | 3 |
| code-review-02 | 19 | 12 | 0.632 | 16 | 5 |
| code-review-03 | 24 | 18 | 0.75 | 17 | 3 |
| code-review-04 | 26 | 16 | 0.615 | 21 | 9 |
| code-review-05 | 27 | 20 | 0.741 | 23 | 5 |
| code-review-06 | 38 | 20 | 0.526 | 23 | 7 |
| code-review-07 | 30 | 24 | 0.8 | 44 | 16 |
| code-review-08 | 34 | 30 | 0.882 | 37 | 7 |
| debugging-01 | 7 | 6 | 0.857 | 3 | 0 |
| debugging-02 | 19 | 9 | 0.474 | 8 | 0 |
| debugging-03 | 10 | 7 | 0.7 | 7 | 0 |
| debugging-04 | 15 | 10 | 0.667 | 9 | 0 |
| debugging-05 | 17 | 15 | 0.882 | 14 | 1 |
| debugging-06 | 4 | 0 | 0.0 | 28 | 28 |
| debugging-07 | 0 | 0 | n/a | 29 | 29 |
| debugging-08 | 28 | 8 | 0.286 | 30 | 19 |
| explanation-01 | 39 | 28 | 0.718 | 24 | 2 |
| explanation-02 | 24 | 23 | 0.958 | 18 | 1 |
| explanation-03 | 35 | 28 | 0.8 | 24 | 2 |
| explanation-04 | 39 | 27 | 0.692 | 26 | 3 |
| explanation-05 | 18 | 16 | 0.889 | 11 | 0 |
| explanation-06 | 21 | 14 | 0.667 | 18 | 5 |
| explanation-07 | 26 | 20 | 0.769 | 26 | 5 |
| explanation-08 | 18 | 13 | 0.722 | 12 | 3 |
| summarization-01 | 5 | 5 | 1.0 | 6 | 1 |
| summarization-02 | 12 | 9 | 0.75 | 11 | 0 |
| summarization-03 | 13 | 12 | 0.923 | 12 | 0 |
| summarization-04 | 13 | 12 | 0.923 | 13 | 1 |
| summarization-05 | 9 | 7 | 0.778 | 6 | 0 |
| summarization-06 | 12 | 12 | 1.0 | 13 | 1 |
| summarization-07 | 14 | 13 | 0.929 | 14 | 2 |
| summarization-08 | 20 | 18 | 0.9 | 21 | 0 |

Median fraction: 0.75 over 31 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python footgun.
- code-review-01: Mutating the caller's list is a surprising side effect that can cause bugs elsewhere in the caller's code.
- code-review-01: An uninformative return value makes it hard for callers to distinguish validation errors from DB errors or misuse and react appropriately.
- code-review-01: The function has no docstring and no type hints.
- code-review-01: Missing type hints is a minor issue.
- code-review-01: Type hints of `name: str`, `roles: list[str] | None`, and a type for `db` would clarify the function's contract.
- code-review-01: A safer rewrite uses `roles=None` as the default and raises `ValueError` when `name` or `db` is missing.
- code-review-01: An alternative to letting errors propagate is catching a specific DB exception in order to translate it.
- code-review-02: The function always returns a rejected promise almost instantly, due to the TypeError.
- code-review-02: There is no validation that the response `data` has a `name` property.
- code-review-02: If the API returns an error object instead of a profile, `data.name` could be `undefined` and calling `.toUpperCase()` on it would throw.
- code-review-02: There is no input validation on `userId`.
- code-review-02: Unsanitized/unencoded `userId` could allow injection of unexpected path segments such as `../` or query-like content.
- code-review-02: `encodeURIComponent(userId)` can be used to encode `userId` before interpolating it into the URL.
- code-review-02: The fixed version awaits `fetch` with an encoded `userId`, throws an Error including `res.status` when `!res.ok`, awaits `res.json()`, throws an Error when the response is missing `name`, and returns `data.name.toUpperCase()`.
- code-review-03: The SQL injection issue is critical in severity.
- code-review-03: The correct parameter placeholder depends on the database driver.
- code-review-03: sqlite3 uses `?` as its parameter placeholder.
- code-review-03: psycopg2 uses `%s` as its parameter placeholder.
- code-review-03: pymysql uses `%s` as its parameter placeholder.
- code-review-03: The SQL injection issue is the one that must be fixed before the code is used in production.
- code-review-04: Python's GIL guarantees that each individual bytecode operation is atomic.
- code-review-04: Under contention, the counter class will systematically undercount.
- code-review-04: `reset` consists of a single assignment, `self.value = 0`.
- code-review-04: A single assignment is atomic in CPython.
- code-review-04: `reset` by itself will not corrupt the counter's state.
- code-review-04: If `reset` runs between another thread's read and write in `increment`, the increment's write will clobber the reset with a stale value.
- code-review-04: An example of the reset/increment race is resetting to 0 and then a stale increment writing 1.
- code-review-04: The class uses no atomic primitive such as `itertools.count` or `multiprocessing.Value`.
- code-review-04: The class has no thread-safety documentation or contract.
- code-review-04: A caller reading the code has no way to know the class is unsafe under concurrent use.
- code-review-05: `cd` with no arguments changes to the user's $HOME directory.
- code-review-05: With an empty BACKUP_DIR, `rm -rf *.tmp` would run in the user's home directory instead of failing.
- code-review-05: Bash has a `nullglob` option affecting unmatched glob behavior.
- code-review-05: `echo Cleaned $BACKUP_DIR` uses an unquoted variable and should be `echo "Cleaned $BACKUP_DIR"`.
- code-review-05: `${1:?Usage: ...}` makes the first argument required.
- code-review-05: The `-r` flag is unnecessary for `rm` because the targets are files, not directories.
- code-review-05: `[ -e "$f" ] || continue` guards against a non-matching glob in the loop.
- code-review-06: Resolving the `None`-means-delete ambiguity requires a sentinel such as a `DELETE` marker if both behaviors are needed.
- code-review-06: `merged.pop(key, None)` silently does nothing if the key is not present in `base`.
- code-review-06: Silently no-oping on a missing key can hide a typo, such as a misspelled key intended to delete something.
- code-review-06: If `base[key]` is a dict and `override[key]` is not a dict, the `elif` branch fails and control falls to the `else` branch.
- code-review-06: In that case the entire nested dict is replaced by the scalar value.
- code-review-06: No validation or error is raised for either type-mismatch case.
- code-review-06: The type-mismatch behavior could mask a configuration mistake.
- code-review-06: Self-referential structures are unlikely for JSON-like config but possible if `base` or `override` are constructed programmatically.
- code-review-06: List replacement is a common convention in settings-merge functions.
- code-review-06: Some config systems expect list concatenation or index-wise merging.
- code-review-06: There is no check that keys are hashable or strings.
- code-review-06: `isinstance(merged[key], dict)` also matches dict subclasses.
- code-review-06: Recursing into an `OrderedDict` or custom dict subclass via `merge_settings` returns a plain `dict`, losing the subclass type.
- code-review-06: Ansible and Kubernetes strategic merge patches use conventions similar to `None`-as-delete.
- code-review-06: The shallow-copy aliasing issue and the silent type-mismatch overwrite are almost certainly bugs or oversights.
- code-review-06: Those two issues tend to pass testing and later cause hard-to-trace mutation bugs or config-clobbering incidents in production.
- code-review-06: Issues #1 and #4 are the highest-priority items to write tests around and confirm intent for.
- code-review-06: Issues #1 and #4 are the ones most likely to fail silently.
- code-review-07: The function has three different signals for failure: a thrown error that never happens, null, and undefined.
- code-review-07: The inconsistency in failure signals indicates the retry-exhaustion path was never tested.
- code-review-07: Most retry helpers use exponential backoff to avoid synchronized retry storms across clients.
- code-review-07: The attempts semantics are not a bug.
- code-review-07: The error categorization appears intentional even though the missing 5xx delay looks like an oversight.
- code-review-07: Changing the undefined case or making the function throw would be a breaking change if callers currently check === null to detect failure.
- code-review-08: `os.listdir()` loads the entire directory listing into memory at once.
- code-review-08: The in-memory listing is acceptable for modest directories and only a concern if `ROOT` grows very large.
- code-review-08: The schedule that invokes this script was not set up by the author of the text.
- code-review-08: The two highest-priority changes are guarding against directories and requiring a minimum age before deleting `.part`/`tmp-` files.
- debugging-01: The corrected get_url function returns an f-string of the form "http://{cfg['host']}:{cfg['port']}/api".
- debugging-02: Class bodies are always in strict mode.
- debugging-02: Strict mode propagates to functions nested inside strict-mode code.
- debugging-02: A regular `function () {...}` passed to `setInterval` from inside a class method has `this === undefined` when called.
- debugging-02: Accessing `this.seconds` when `this` is `undefined` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: Seeing `NaN` instead of a thrown error indicates the code is running in a non-strict/sloppy context.
- debugging-02: Running code directly in a browser `<script>` without `"use strict"` is an example of a non-strict/sloppy context.
- debugging-02: Some transpilation does not preserve strict mode, producing a sloppy-mode context.
- debugging-02: Calling `.bind(this)` on the callback function is an alternative fix.
- debugging-02: Storing `const self = this;` before `setInterval` and using `self` inside the callback is an alternative fix.
- debugging-02: The arrow function is the cleanest modern approach among these fixes.
- debugging-03: The corrected `moving_sum` function appends `sum(values[i : i + window])` to a list named `sums` on each iteration.
- debugging-03: The corrected `moving_sum` function returns `sums`.
- debugging-03: `moving_sum` computes the sum of each window of the given size.
- debugging-04: The 0xc3 byte likely represents an accented character such as é or ü.
- debugging-04: The non-ASCII byte occurs at byte offset 512 in the file.
- debugging-04: The ASCII codec rejects any byte greater than or equal to 0x80.
- debugging-04: For line counting, UTF-8 with errors="replace" is usually the pragmatic fix.
- debugging-04: The errors="surrogateescape" option preserves byte fidelity.
- debugging-05: A default argument value in Python is evaluated once, at function definition time.
- debugging-05: The same test running twice can also cause the extra `"post"` entries, for example via test discovery, parametrization, or fixtures.
- debugging-06: The speaker intends to check memory for prior context on the system.
- debugging-06: A tool call was made to list files and directories in a given path.
- debugging-06: The status of that tool call was 'Completed'.
- debugging-06: The tool call's terminal output was 'No files found'.
- debugging-08: Campaign products can have larger payloads, more images and variants, and richer JSON than normal products.
- debugging-08: The count-bounded-cache explanation fits all four reported observations.
- debugging-08: Cache entries persist until they are evicted, so cache-driven memory growth survives quiet nights.
- debugging-08: Any traffic populates the cache, so cache-driven growth occurs even without webhooks.
- debugging-08: Guava and Caffeine caches offer a `maximumSize` setting and a `maximumWeight` setting.
- debugging-08: Long-lived maps used for deduplication, idempotency keys, rate limiting, or session and request tracking are a classic source of leaks when their TTL cleanup is absent, broken, or slow.
- debugging-08: Such leaky maps are typically keyed by request ID, order ID, webhook event ID, or correlation ID.
- debugging-08: Dynamically generated classes from serialization libraries, proxies, or template engines leak metaspace rather than heap.
- debugging-08: More campaign SKUs and variants can produce more dynamically generated types.
- debugging-08: Classes are not unloaded until their classloader is garbage collected.
- debugging-08: Application classloaders often are never garbage collected.
- debugging-08: `jstat -gc` or an APM memory breakdown can distinguish heap growth from non-heap/metaspace growth.
- debugging-08: Native or off-heap memory, such as Netty direct buffers and native codecs, can leak on specific code paths.
- debugging-08: Off-heap leaks are consistent with growth that survives quiet nights and correlates with traffic volume.
- debugging-08: If RSS grows well beyond JVM-reported heap usage, the growth is native or off-heap.
- debugging-08: NativeMemoryTracking, `pmap`, and `smaps` diffs can be used to investigate native memory growth.
- debugging-08: The cache-bound hypothesis is the only one of the four consistent with all four clues without positing an additional leak.
- debugging-08: Logging the cache entry-size distribution is a cheap check.
- debugging-08: Switching the cache to weight-based eviction would be a one-line fix.
- debugging-08: The canary-still-grows observation is the strongest evidence that something grows independently of the cache.
- explanation-01: An array slot cannot hold two values at once.
- explanation-01: Quadratic probing tries indices at increasing squared steps.
- explanation-01: Double hashing uses a second hash function to decide the step size.
- explanation-01: Chaining eventually needs resizing, but less urgently than open addressing.
- explanation-01: Open addressing needs resizing sooner and must be kept well below full, often under a 70% load factor.
- explanation-01: Chaining tolerates a poor hash function or high load factor more gracefully than open addressing.
- explanation-01: Most general-purpose hash maps used day-to-day use chaining.
- explanation-01: Java's HashMap uses chaining.
- explanation-01: Java converts long chains to trees for performance.
- explanation-01: Python's dict uses open addressing.
- explanation-01: Many high-performance C++ hash maps use open addressing.
- explanation-02: Pessimistic locking fits when you need guaranteed consistency and can tolerate transactions waiting.
- explanation-03: Dropped packets cause wasted bandwidth and retransmissions.
- explanation-03: Before congestion control existed, dropped packets could snowball into congestion collapse.
- explanation-03: Congestion collapse is when a congested network becomes even more congested because senders keep retransmitting lost data.
- explanation-03: The initial cwnd is now typically 2-10 segments per RFC 6928.
- explanation-03: Reaching a reasonable sending rate quickly matters a lot for short connections such as most web requests.
- explanation-03: After detecting loss, TCP switches to a more cautious, linear growth phase called congestion avoidance.
- explanation-03: This congestion control philosophy is why the internet has remained stable even as usage grew enormously.
- explanation-04: Each thread has its own stack and register/instruction pointer state.
- explanation-04: Thread communication requires careful synchronization, such as locks and mutexes, to avoid race conditions.
- explanation-04: Process creation cost is higher than thread creation cost because the OS allocates a new memory space and tables.
- explanation-04: Processes communicate via IPC mechanisms such as pipes, sockets, and shared memory, which is slower than thread communication.
- explanation-04: Threads communicate via direct shared memory, which is faster than IPC.
- explanation-04: Threads provide parallelism with shared state and need synchronization.
- explanation-04: Multiple processes bypass the GIL because each process has its own interpreter and GIL.
- explanation-04: Nginx and Apache use worker processes.
- explanation-04: The OS lets you set per-process limits on memory, CPU, and file descriptors via cgroups and ulimits.
- explanation-04: Separate processes make it straightforward to restart, upgrade, or scale components independently.
- explanation-04: Microservices and worker pools are examples of components with independent lifecycles that can be killed and respawned.
- explanation-04: I/O-bound tasks wait on network or disk.
- explanation-05: Global emitters and DOM elements are examples of long-lived objects.
- explanation-05: Caches without a TTL, without a size limit, or using strong keys instead of weak references are unbounded.
- explanation-06: A cache does not help when slowness comes from a slow external API call.
- explanation-06: A cache does not help when slowness comes from a missing database index.
- explanation-06: Adding a cache means maintaining two systems instead of one.
- explanation-06: Caching helps read-heavy workloads because it avoids recomputing or refetching the same data repeatedly.
- explanation-06: In a write-heavy workload or one with unique-per-request reads, a cache will have a low hit rate.
- explanation-06: Slow query logs and DB metrics show whether the database is CPU or IO bound or whether the app is slow elsewhere.
- explanation-06: Profiling should check the read/write ratio and whether reads repeat the same keys/queries or are mostly unique.
- explanation-07: The product team's inability to estimate growth is the real problem.
- explanation-07: A growth rate of about 10% in GB is fine for years.
- explanation-07: A growth rate of 10x per year changes the calculus.
- explanation-07: Waiting leaves less room to test the shard key choice.
- explanation-07: Partitioning can be time-based or tenant-based and still run on a single instance.
- explanation-07: Partitioning and read replicas are reversible.
- explanation-08: Protobuf and msgpack are examples of binary formats.
- explanation-08: JSON has overhead from quotes, keys repeated per record, and text-encoded numbers.
- explanation-08: JSON's overhead matters most for large arrays of small objects or numeric-heavy data.
- explanation-08: If payloads are already small or mostly free-text strings, binary formats provide little size benefit.
- explanation-08: Most languages allow wrapping JSON encode/decode in a timer or using a profiler to measure it.
- summarization-02: The staging pool size of 5 was intended to be small.
- summarization-02: The incident caused approximately 12% error rates for checkout.
- summarization-02: The incident ran from 09:14 to 09:48 UTC.
- summarization-03: Thumbnail generation currently ties up web workers.
- summarization-04: The issue was reproduced by a second user on a different machine.
- summarization-05: Ada is assigned to run the payments database migration dry run.
- summarization-05: Ada is assigned to check with the mobile team lead about whether the mobile team has been informed of the API deprecation.
- summarization-07: Aside from the median latency drop and the memory increase, the results of the comparison are uncertain.
- summarization-08: The template gallery is a new feature.
- summarization-08: Follow-up with new or template-less users is needed before drawing conclusions about the template gallery.

Added facts (styled only):

- code-review-01: There is no duplicate-user check.
- code-review-01: Nothing prevents inserting the same `name` twice.
- code-review-01: The proposed fix calls `db.insert({"name": name, "roles": roles})` and returns `True`.
- code-review-02: Unhandled failure cases include network errors, non-2xx statuses, and malformed JSON.
- code-review-02: Because nothing is awaited, the function effectively returns `undefined` synchronously.
- code-review-02: The `async` signature implies the function returns a `Promise<string>`.
- code-review-02: The corrected function awaits `fetch(`/api/users/${userId}`)`.
- code-review-02: The thrown error message includes the user ID and `res.status`.
- code-review-03: Any input containing a single quote character breaks out of the string literal in the query.
- code-review-03: If non-string arguments such as `None` are passed, the string concatenation raises a `TypeError`.
- code-review-03: The `TypeError` raised is less clear than a purpose-built error message.
- code-review-04: `reset` can clobber a concurrent update.
- code-review-04: A caller cannot perform a safe read-then-act sequence (such as incrementing only if below X) without external locking.
- code-review-04: The class has no `get`/read method with proper synchronization.
- code-review-04: That safety is not guaranteed by the Python language.
- code-review-04: A direct read of `self.value` gives no ordering guarantees relative to other operations.
- code-review-04: In the fixed version, the counter value is stored in a private attribute `_value`.
- code-review-04: In the fixed version, `increment` performs `self._value += 1` while holding the lock.
- code-review-04: In the fixed version, `reset` sets `self._value` to 0 while holding the lock.
- code-review-04: In the fixed version, `value` is a property that returns `self._value` while holding the lock.
- code-review-05: If the argument is empty, `cd $BACKUP_DIR` becomes a no-op.
- code-review-05: With an empty argument, `rm -rf *.tmp` runs in the current directory instead of failing safely.
- code-review-05: If no .tmp files exist, most shells leave the literal string `*.tmp`, and the command fails harmlessly.
- code-review-05: The script prints "Cleaned" at the end even when commands have failed, giving false confidence.
- code-review-05: The script relies only on `sh` semantics, which is acceptable here.
- code-review-06: The function's type check only tests isinstance(merged[key], dict) and does not test isinstance(value, dict).
- code-review-06: If base[key] is a dict but override[key] is a non-dict such as a string, the function recurses as merge_settings(dict, str).
- code-review-06: Values assigned from override, including lists and wholesale-overwritten dicts, are stored by reference rather than copied.
- code-review-06: The None-deletes-key behavior is undocumented.
- code-review-06: The same type mismatch either crashes or silently overwrites depending on which side holds the dict.
- code-review-06: The asymmetric type check is very likely an unintentional bug.
- code-review-06: The asymmetric type check makes the function crash on inputs that look like normal, valid config data.
- code-review-07: The silent null return on non-retryable errors is likely a bug rather than deliberate.
- code-review-07: The zero-delay first retry is inconsistent and probably unintentional, resembling an off-by-one error.
- code-review-07: The intended 429 delay was likely 1000 * (i + 1) or exponential backoff.
- code-review-07: The no-backoff behavior on 5xx could be read as deliberate DoS-adjacent behavior against one's own dependency, but is far more likely an oversight.
- code-review-07: There is no cap on the retry delay.
- code-review-07: With larger attempts values, the delay grows unbounded linearly.
- code-review-07: The unbounded delay is not a large issue at attempts = 3 but could be slow if a caller passes a large attempts value.
- code-review-07: The attempts parameter defaults to 3.
- code-review-07: If 0 or a negative value is passed for attempts, the loop does not execute and the function returns undefined silently.
- code-review-07: There is no validation of the attempts parameter.
- code-review-07: The code makes no distinction between 429 and 5xx backoff strategy.
- code-review-07: Conflating rate-limited and server-error handling logic makes intent unclear.
- code-review-07: The silent undefined return after exhausting retries, the zero-delay first retry, and the no-backoff on 5xx are almost certainly bugs.
- code-review-07: Those three issues look like copy-paste or off-by-one mistakes rather than intent.
- code-review-07: The err.status assumption is ambiguous and needs owner input.
- code-review-07: If the code was written for one specific HTTP client's error shape, the err.status assumption is a reasonable but undocumented constraint.
- code-review-08: Without logging, failures are invisible.
- code-review-08: os.path.getmtime follows symlinks.
- code-review-08: Calling os.path.getmtime on a broken symlink raises FileNotFoundError.
- code-review-08: For a valid symlink, os.path.getmtime returns the target's mtime, not the link's.
- code-review-08: Evaluating a symlink by its target's mtime is likely not intended.
- code-review-08: The asymmetry between temp-file and aged-file handling appears intentional but is undocumented.
- code-review-08: The script does not check that ROOT exists or is a directory before listing it.
- debugging-05: In the fixed version, `tags` is set to `list(DEFAULT_TAGS)` when `tags` is None, and `list(tags)` otherwise.
- debugging-06: worker-3 waits 30 seconds before giving up.
- debugging-06: If the connection pool size is fixed and multiple workers or the analytics service compete for it, pool exhaustion under load is expected rather than a bug.
- debugging-06: The database is shared between the export job and the analytics service.
- debugging-06: A nightly analytics query or job may spike connection usage or hold connections via long-running or locking queries at the same time the export runs.
- debugging-06: Export or analytics code may fail to release connections on error paths, slowly starving the pool.
- debugging-06: The failures do not occur on the same batch number each time.
- debugging-06: A failure pattern tied to timing and load rather than to specific data is consistent with a connection leak.
- debugging-06: A query plan regression on certain data, such as a missing index hit only for some batches, can hold connections longer than normal and intermittently push the pool over the edge.
- debugging-06: The retry logic can create additional pool pressure when the pool is already exhausted, worsening a transient spike into a hard failure.
- debugging-06: Attempt 2 also times out.
- debugging-06: Attempt 2 timing out is consistent with the pool still being saturated rather than a fluke.
- debugging-06: Failures occur around 02:xx.
- debugging-06: If failures cluster around an overlap with nightly analytics jobs, the cause is contention rather than a leak.
- debugging-06: A connection leak shows as a slow upward drift in pool metrics over time.
- debugging-06: Contention shows as spikes in pool metrics.
- debugging-06: Pool metrics worth monitoring include connection pool size, active connections, idle connections, and wait queue length.
- debugging-06: Pool metrics should be monitored over time, not just at the moment of failure.
- debugging-06: pg_stat_activity can be used to check database-side active connections and locks.
- debugging-06: Long-running queries from the analytics service against tables the export touches are worth looking for at or near failure timestamps.
- debugging-06: Increasing log verbosity around pool acquire and release, or adding connection lifecycle logging, would reveal total connections in use, who holds them, and how long on the next occurrence.
- debugging-06: Auditing exception and error paths in export and analytics code for missing finally blocks or context-manager connection release can find connection leaks.
- debugging-06: Slow query logs around failure times can reveal queries with abnormal duration.
- debugging-06: Running the export concurrently with a simulated analytics workload in staging could trigger pool exhaustion on demand.
- debugging-06: Synthetic load reproduction in staging is much faster than waiting for the nightly failure to recur.
- debugging-06: The failure occurs approximately weekly.
- debugging-06: Log rotation destroyed the context needed to diagnose the failure.
- debugging-06: The fastest win is likely extending log retention (or shipping logs to a persistent store) and adding pool/connection instrumentation before the next occurrence.
- debugging-06: There is currently not enough data to distinguish between a connection leak, contention, and a slow query as the cause.
- debugging-07: Storing events in a shared table or queue without per-test scoping can cause test isolation leaks under parallel workers.
- debugging-07: Per-test scoping is absent when events are filtered only by a time window or a global 'latest N' query.
- debugging-07: Concurrently-seeded events from another worker can interleave with or evict one of a test's three events.
- debugging-07: If seeding is asynchronous and the digest query fires before all three writes commit, the test observes 2 of 3 events.
- debugging-07: More parallel workers increase contention and the chance the digest request lands in the write-read race window.
- debugging-07: Digest logic may contain a cap, dedup, or time-window filter that is timing-sensitive.
- debugging-07: A 'last N events' or time-bucket cutoff can shift a seeded event across a boundary on slower or loaded CI workers.
- debugging-07: Shared fixture or DB state that is not reset between tests can surface only under parallel workers.
- debugging-07: Worker-local test ordering differs from serial run ordering.
- debugging-07: Differing test ordering under parallel workers can occasionally cause a cleanup-before-assert race.
- debugging-07: A test may assume events appear in insertion order while the digest dedupes or collapses by a key.
- debugging-07: Key collisions in digest dedup may occur only when other workers' data is interleaved.
- debugging-07: Given that the test never fails serially and runs with 4 workers, the leading suspects are missing per-test/per-worker isolation and a write-then-read race.
- debugging-07: Running the suite locally with 4 parallel workers in a loop of 50 iterations often reproduces the failure locally.
- debugging-07: A local parallel reproduction confirms parallelism rather than CI-machine speed as the cause.
- debugging-07: Test isolation can be checked by whether each test uses a unique tenant, user, or session ID.
- debugging-07: Grepping the digest query or fixture for LIMIT, a global filter, or a missing owner-scoped WHERE clause can reveal isolation problems.
- debugging-07: Inserting a synchronization point means waiting or polling for seed confirmation before requesting the digest.
- debugging-07: Seed confirmation can be done by asserting each seed call returns 201 or polling until the event count equals 3.
- debugging-07: If adding a synchronization point fixes the flake, the cause is a race.
- debugging-07: CI in this setup drops logs.
- debugging-07: A retry-with-diagnostics wrapper can dump the actual DB rows or events for the test's scope before the assertion.
- debugging-07: pytest --pdb or logging the raw digest response can capture failure diagnostics.
- debugging-07: Running the flaky test alone with a single worker and the flags '-p no:cacheprovider --reruns' can capture state once in CI.
- debugging-07: Bisecting worker count means running the CI-equivalent suite locally with 1, 2, and 4 workers in loops.
- debugging-07: If the failure rate scales with worker count, the cause is almost certainly shared-state contention rather than slow-machine timing.
- debugging-07: If digest logic buckets by timestamp, logging the timestamps of the three seed calls and the digest call reveals whether one falls outside the window under load.
- debugging-07: The local loop repro with 4 workers is cheap and confirms or denies the parallelism hypothesis in one step.
- debugging-07: The local loop repro should be done before investing in instrumenting CI.
- debugging-08: One leak is traffic-driven and explains the 2%-per-day growth and the campaign correlation.
- debugging-08: A candidate cause is per-request objects added to a static collection, such as listeners, callbacks, or futures that are never completed.
- debugging-08: A candidate cause is unbounded-cardinality metrics or logging tags, such as per-order-id or per-SKU labels.
- debugging-08: Campaigns add new SKUs and promo codes, which creates more distinct label values and a bigger metrics registry.
- debugging-08: A candidate cause is connection or thread-pool objects created but not released per webhook.
- debugging-08: Diffing heap histograms taken at the start and end of a busy day can reveal object counts that scale with request count rather than merely larger objects.
- debugging-08: Metrics registry size (cardinality) should be checked over the course of a day.
- debugging-08: A growing number of distinct metric series is a very common silent leak.
- debugging-08: Background work such as health checks, scheduled jobs, connection-pool keepalive, log buffering, uncleared timers or intervals, and DNS/TLS session caches can leak regardless of webhook volume.
- debugging-08: Running the canary completely idle, including disabling its internal schedulers, tests whether growth stops.
- debugging-08: Disabling background jobs one at a time bisects the cause of the baseline leak.
- debugging-08: Accumulating threads and timers is a common cause of memory growth in a quiet system.
- debugging-08: Taking thread dumps over time can detect accumulating threads and timers.
- debugging-08: Cache eviction may fail to actually fire when weak or soft references are not being collected.
- debugging-08: Evicted cache entries may still be referenced elsewhere, such as in a listener or a secondary index.
- debugging-08: Memory never returning to baseline overnight rules out anything that is just delayed GC.
- debugging-08: The memory involved is retained, reachable memory.
- debugging-08: The overnight behavior confirms a true leak with references being held, rather than fragmentation or lazy collection.
- debugging-08: The suggested first investigation step is to get a heap dump, even a single one at end-of-week.
- explanation-01: The load factor with chaining can exceed 1.0 because buckets grow.
- explanation-01: In the worst case, open addressing degrades to long probe sequences due to clustering.
- explanation-02: Optimistic locking fits read-heavy workloads where locking would hurt throughput.
- explanation-03: The initial congestion window is now typically 10 segments, about 14KB, per RFC 6928.
- explanation-03: On detecting packet loss, ssthresh is set to about half the current cwnd.
- explanation-04: Running untrusted or plugin code is an example of a workload where a worker might crash or hang.
- explanation-04: Ruby has a global interpreter lock.
- explanation-04: Chrome uses sandboxed renderers.
- explanation-06: Profiling an API can be done with an APM tool or by timing/logging around DB calls versus other code.
- explanation-06: Missing indexes, slow queries, and N+1 patterns are cheap fixes to look for first.
- explanation-06: Missing indexes, slow queries, and N+1 patterns are often the real culprit behind performance problems.
- explanation-06: Fixing missing indexes, slow queries, and N+1 patterns is cheaper than adding a cache.
- explanation-06: Redis and in-memory caches are options for caching.
- explanation-07: Sharding only helps if a workload is write-bound or CPU-bound on a single primary.
- explanation-07: With sharding, every query must be shard-aware.
- explanation-07: Monitoring write latency, replication lag, CPU saturation, and table sizes mitigates the risk of waiting to shard.
- explanation-07: A revisit trigger based on metrics is better than picking a calendar date.
- explanation-07: An example revisit trigger is reassessing at 1-2 TB or when write p99 latency degrades.
- explanation-08: Binary formats can shrink payload byte size by 30-50%.
- explanation-08: Profiling request latency for serialization's share and checking typical payload sizes takes about a couple of hours of instrumentation.
- explanation-08: A couple hours of instrumentation is not a big lift.
- summarization-01: Cold start time was reduced by approximately 40%.
- summarization-04: The issue was reproduced on the latest version of Firefox.
- summarization-06: The on-call engineer suspects the connection-pool exhaustion was amplified by a retry storm.
- summarization-07: p99 tail latency also improved.
- summarization-07: Staging runs a newer kernel.

### developer-docs

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 28 | 18 | 0.643 | 26 | 3 |
| code-review-02 | 19 | 12 | 0.632 | 19 | 1 |
| code-review-03 | 24 | 16 | 0.667 | 19 | 6 |
| code-review-04 | 26 | 20 | 0.769 | 17 | 1 |
| code-review-05 | 27 | 19 | 0.704 | 29 | 2 |
| code-review-06 | 38 | 19 | 0.5 | 26 | 7 |
| code-review-07 | 30 | 22 | 0.733 | 32 | 10 |
| code-review-08 | 34 | 26 | 0.765 | 27 | 6 |
| debugging-01 | 7 | 7 | 1.0 | 7 | 0 |
| debugging-02 | 19 | 9 | 0.474 | 10 | 0 |
| debugging-03 | 10 | 10 | 1.0 | 9 | 0 |
| debugging-04 | 15 | 13 | 0.867 | 13 | 1 |
| debugging-05 | 17 | 15 | 0.882 | 16 | 0 |
| debugging-06 | 4 | 0 | 0.0 | 23 | 23 |
| debugging-07 | 0 | 0 | n/a | 20 | 20 |
| debugging-08 | 28 | 5 | 0.179 | 31 | 18 |
| explanation-01 | 39 | 25 | 0.641 | 26 | 2 |
| explanation-02 | 24 | 22 | 0.917 | 26 | 1 |
| explanation-03 | 35 | 31 | 0.886 | 25 | 3 |
| explanation-04 | 39 | 30 | 0.769 | 32 | 1 |
| explanation-05 | 18 | 15 | 0.833 | 16 | 1 |
| explanation-06 | 21 | 17 | 0.81 | 17 | 4 |
| explanation-07 | 26 | 16 | 0.615 | 32 | 9 |
| explanation-08 | 18 | 10 | 0.556 | 12 | 1 |
| summarization-01 | 5 | 5 | 1.0 | 5 | 0 |
| summarization-02 | 12 | 10 | 0.833 | 17 | 1 |
| summarization-03 | 13 | 11 | 0.846 | 13 | 0 |
| summarization-04 | 13 | 11 | 0.846 | 11 | 0 |
| summarization-05 | 9 | 8 | 0.889 | 11 | 1 |
| summarization-06 | 12 | 12 | 1.0 | 12 | 1 |
| summarization-07 | 14 | 14 | 1.0 | 12 | 1 |
| summarization-08 | 20 | 18 | 0.9 | 23 | 3 |

Median fraction: 0.81 over 31 scored pairs.

Median additions: 1.0 over 32 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python footgun.
- code-review-01: Mutating the caller's list is a surprising side effect that can cause bugs elsewhere in the caller's code.
- code-review-01: Duplicate roles aren't prevented.
- code-review-01: Calling the function with `roles=["member"]` explicitly produces `["member", "member"]`.
- code-review-01: The function has no docstring and no type hints.
- code-review-01: Missing type hints is a minor issue.
- code-review-01: Type hints of `name: str`, `roles: list[str] | None`, and a type for `db` would clarify the function's contract.
- code-review-01: The safer rewrite copies `roles` with `list(roles)` and appends `"member"` only if it is not already present.
- code-review-01: The rewrite drops the silent failure mode by letting real errors propagate.
- code-review-01: An alternative to letting errors propagate is catching a specific DB exception in order to translate it.
- code-review-02: The function always returns a rejected promise almost instantly, due to the TypeError.
- code-review-02: There is no validation that the response `data` has a `name` property.
- code-review-02: If the API returns an error object instead of a profile, `data.name` could be `undefined` and calling `.toUpperCase()` on it would throw.
- code-review-02: There is no input validation on `userId`.
- code-review-02: Unsanitized/unencoded `userId` could allow injection of unexpected path segments such as `../` or query-like content.
- code-review-02: `encodeURIComponent(userId)` can be used to encode `userId` before interpolating it into the URL.
- code-review-02: The fixed version awaits `fetch` with an encoded `userId`, throws an Error including `res.status` when `!res.ok`, awaits `res.json()`, throws an Error when the response is missing `name`, and returns `data.name.toUpperCase()`.
- code-review-03: psycopg2 uses `%s` as its parameter placeholder.
- code-review-03: pymysql uses `%s` as its parameter placeholder.
- code-review-03: The function performs no input validation.
- code-review-03: The function does not check that `status` is one of the expected valid values before querying.
- code-review-03: The function has no error handling.
- code-review-03: `cursor.execute` can raise an exception, for example on a bad connection or a database error.
- code-review-03: `fetchall` can raise an exception, for example on a bad connection or a database error.
- code-review-03: These exceptions are handled nowhere, and no context is provided to the caller.
- code-review-04: Under contention, the counter class will systematically undercount.
- code-review-04: `reset` consists of a single assignment, `self.value = 0`.
- code-review-04: A single assignment is atomic in CPython.
- code-review-04: `reset` by itself will not corrupt the counter's state.
- code-review-04: The class has no thread-safety documentation or contract.
- code-review-04: A caller reading the code has no way to know the class is unsafe under concurrent use.
- code-review-05: `cd "$BACKUP_DIR" || exit 1` is the correct form.
- code-review-05: `rm -rf` given a literal unmatched pattern typically errors out harmlessly in POSIX sh.
- code-review-05: `rm -rf *.tmp` is the most dangerous line in the script.
- code-review-05: When no .log files exist, `ls *.log` prints an error to stderr and returns nothing usable.
- code-review-05: `echo Cleaned $BACKUP_DIR` uses an unquoted variable and should be `echo "Cleaned $BACKUP_DIR"`.
- code-review-05: Without `set -u`, the missing-argument problem passes silently.
- code-review-05: `${1:?Usage: ...}` makes the first argument required.
- code-review-05: The `-r` flag is unnecessary for `rm` because the targets are files, not directories.
- code-review-06: Resolving the `None`-means-delete ambiguity requires a sentinel such as a `DELETE` marker if both behaviors are needed.
- code-review-06: `merged.pop(key, None)` silently does nothing if the key is not present in `base`.
- code-review-06: Silently no-oping on a missing key can hide a typo, such as a misspelled key intended to delete something.
- code-review-06: If `base[key]` is a dict and `override[key]` is not a dict, the `elif` branch fails and control falls to the `else` branch.
- code-review-06: In that case the entire nested dict is replaced by the scalar value.
- code-review-06: No validation or error is raised for either type-mismatch case.
- code-review-06: Recursion depth follows the depth of `override`'s nested dicts.
- code-review-06: List replacement is a common convention in settings-merge functions.
- code-review-06: Some config systems expect list concatenation or index-wise merging.
- code-review-06: There is no check that `base` and `override` are actually dicts.
- code-review-06: There is no check that keys are hashable or strings.
- code-review-06: `isinstance(merged[key], dict)` also matches dict subclasses.
- code-review-06: Recursing into an `OrderedDict` or custom dict subclass via `merge_settings` returns a plain `dict`, losing the subclass type.
- code-review-06: Non-dict values fully overriding reflects typical 'last writer wins' semantics.
- code-review-06: Ansible and Kubernetes strategic merge patches use conventions similar to `None`-as-delete.
- code-review-06: The shallow-copy aliasing issue and the silent type-mismatch overwrite are almost certainly bugs or oversights.
- code-review-06: Those two issues tend to pass testing and later cause hard-to-trace mutation bugs or config-clobbering incidents in production.
- code-review-06: Issues #1 and #4 are the highest-priority items to write tests around and confirm intent for.
- code-review-06: Issues #1 and #4 are the ones most likely to fail silently.
- code-review-07: The function has three different signals for failure: a thrown error that never happens, null, and undefined.
- code-review-07: The inconsistency in failure signals indicates the retry-exhaustion path was never tested.
- code-review-07: Swallowing non-HTTP errors as null is the most dangerous issue in the code, especially with callers that cannot be audited.
- code-review-07: A caller cannot distinguish a legitimate null return value from a failure after retries.
- code-review-07: Discarding errors without a trace can cause silent data corruption downstream in a shared library with unknown callers.
- code-review-07: Most retry helpers use exponential backoff to avoid synchronized retry storms across clients.
- code-review-07: The attempts semantics are not a bug.
- code-review-07: The error categorization appears intentional even though the missing 5xx delay looks like an oversight.
- code-review-08: The unconditional `tmp-`/`.part` deletion is the most dangerous line in the file.
- code-review-08: `os.listdir()` loads the entire directory listing into memory at once.
- code-review-08: The in-memory listing is acceptable for modest directories and only a concern if `ROOT` grows very large.
- code-review-08: `CUTOFF = time.time() - 86400 * 45` is computed once at import time rather than per call.
- code-review-08: If the script is re-invoked as a fresh process each run (e.g. cron or systemd timer), the import-time `CUTOFF` is harmless.
- code-review-08: If the module is imported once into a long-lived scheduler process and `clean()` is called repeatedly, `CUTOFF` goes stale and never advances.
- code-review-08: Unconditional removal of `tmp-`/`.part` files could be an intentional 'always junk' assumption.
- code-review-08: The two highest-priority changes are guarding against directories and requiring a minimum age before deleting `.part`/`tmp-` files.
- debugging-02: Class bodies are always in strict mode.
- debugging-02: Strict mode propagates to functions nested inside strict-mode code.
- debugging-02: A regular `function () {...}` passed to `setInterval` from inside a class method has `this === undefined` when called.
- debugging-02: Accessing `this.seconds` when `this` is `undefined` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: Seeing `NaN` instead of a thrown error indicates the code is running in a non-strict/sloppy context.
- debugging-02: Running code directly in a browser `<script>` without `"use strict"` is an example of a non-strict/sloppy context.
- debugging-02: Some transpilation does not preserve strict mode, producing a sloppy-mode context.
- debugging-02: Calling `.bind(this)` on the callback function is an alternative fix.
- debugging-02: Storing `const self = this;` before `setInterval` and using `self` inside the callback is an alternative fix.
- debugging-02: The arrow function is the cleanest modern approach among these fixes.
- debugging-04: The non-ASCII byte occurs at byte offset 512 in the file.
- debugging-04: The errors="surrogateescape" option preserves byte fidelity.
- debugging-05: The same test running twice can also cause the extra `"post"` entries, for example via test discovery, parametrization, or fixtures.
- debugging-05: In the fixed code, `make_post` is defined as `def make_post(title, tags=None)` and sets `tags = list(DEFAULT_TAGS)` when `tags is None`.
- debugging-06: The speaker intends to check memory for prior context on the system.
- debugging-06: A tool call was made to list files and directories in a given path.
- debugging-06: The status of that tool call was 'Completed'.
- debugging-06: The tool call's terminal output was 'No files found'.
- debugging-08: Campaign products can have larger payloads, more images and variants, and richer JSON than normal products.
- debugging-08: The count-bounded-cache explanation fits all four reported observations.
- debugging-08: Any traffic populates the cache, so cache-driven growth occurs even without webhooks.
- debugging-08: Guava and Caffeine caches offer a `maximumSize` setting and a `maximumWeight` setting.
- debugging-08: The canary instance receives no webhooks and still grows in memory, but more slowly.
- debugging-08: Slower growth on the webhook-free canary implies a baseline leak independent of webhooks plus an additional webhook-driven contributor.
- debugging-08: Long-lived maps used for deduplication, idempotency keys, rate limiting, or session and request tracking are a classic source of leaks when their TTL cleanup is absent, broken, or slow.
- debugging-08: Such leaky maps are typically keyed by request ID, order ID, webhook event ID, or correlation ID.
- debugging-08: Dynamically generated classes from serialization libraries, proxies, or template engines leak metaspace rather than heap.
- debugging-08: More campaign SKUs and variants can produce more dynamically generated types.
- debugging-08: Classes are not unloaded until their classloader is garbage collected.
- debugging-08: Application classloaders often are never garbage collected.
- debugging-08: `jstat -gc` or an APM memory breakdown can distinguish heap growth from non-heap/metaspace growth.
- debugging-08: Native or off-heap memory, such as Netty direct buffers and native codecs, can leak on specific code paths.
- debugging-08: Off-heap leaks are consistent with growth that survives quiet nights and correlates with traffic volume.
- debugging-08: If RSS grows well beyond JVM-reported heap usage, the growth is native or off-heap.
- debugging-08: NativeMemoryTracking, `pmap`, and `smaps` diffs can be used to investigate native memory growth.
- debugging-08: The cache-bound hypothesis is the only one of the four consistent with all four clues without positing an additional leak.
- debugging-08: Logging the cache entry-size distribution is a cheap check.
- debugging-08: Switching the cache to weight-based eviction would be a one-line fix.
- debugging-08: The canary-still-grows observation is the strongest evidence that something grows independently of the cache.
- debugging-08: No heap profile currently exists for the affected system.
- debugging-08: A single `jmap -histo:live` or heap dump from an instance near end-of-week, compared against one taken right after restart, would likely identify the top suspect within minutes.
- explanation-01: The collection in a chained slot is usually a linked list, and sometimes a small array or tree.
- explanation-01: Quadratic probing tries indices at increasing squared steps.
- explanation-01: Double hashing uses a second hash function to decide the step size.
- explanation-01: Open addressing can fail entirely if the array is full.
- explanation-01: Chaining eventually needs resizing, but less urgently than open addressing.
- explanation-01: Open addressing needs resizing sooner and must be kept well below full, often under a 70% load factor.
- explanation-01: Chaining is simpler to reason about than open addressing.
- explanation-01: Chaining tolerates a poor hash function or high load factor more gracefully than open addressing.
- explanation-01: Deletion and resizing are more delicate to implement correctly in open addressing.
- explanation-01: Most general-purpose hash maps used day-to-day use chaining.
- explanation-01: Java's HashMap uses chaining.
- explanation-01: Java converts long chains to trees for performance.
- explanation-01: Python's dict uses open addressing.
- explanation-01: Many high-performance C++ hash maps use open addressing.
- explanation-02: Optimistic locking fits for long-lived transactions or when there is user think time between read and write, such as editing a form in a browser.
- explanation-02: Holding a database lock during user think time would be wasteful.
- explanation-03: The initial cwnd is now typically 2-10 segments per RFC 6928.
- explanation-03: Reaching a reasonable sending rate quickly matters a lot for short connections such as most web requests.
- explanation-03: After detecting loss, TCP switches to a more cautious, linear growth phase called congestion avoidance.
- explanation-03: This congestion control philosophy is why the internet has remained stable even as usage grew enormously.
- explanation-04: Each thread has its own stack and register/instruction pointer state.
- explanation-04: Thread communication requires careful synchronization, such as locks and mutexes, to avoid race conditions.
- explanation-04: Threads provide parallelism with shared state and need synchronization.
- explanation-04: Nginx and Apache use worker processes.
- explanation-04: Separate processes make it straightforward to restart, upgrade, or scale components independently.
- explanation-04: Microservices and worker pools are examples of components with independent lifecycles that can be killed and respawned.
- explanation-04: Threads are preferable for tasks that are lightweight, need to share state efficiently, and are I/O-bound.
- explanation-04: I/O-bound tasks wait on network or disk.
- explanation-04: GIL and shared-state concerns matter less for I/O-bound tasks.
- explanation-05: Global emitters and DOM elements are examples of long-lived objects.
- explanation-05: Listeners often close over additional state.
- explanation-05: Caches without a TTL, without a size limit, or using strong keys instead of weak references are unbounded.
- explanation-06: A cache does not help when slowness comes from a missing database index.
- explanation-06: A cache does not help when slowness comes from lock contention caused by writes.
- explanation-06: A cache does not help when slowness comes from an N+1 query problem.
- explanation-06: Slow query logs and DB metrics show whether the database is CPU or IO bound or whether the app is slow elsewhere.
- explanation-07: Routing logic is a source of sharding complexity.
- explanation-07: The product team's inability to estimate growth is the real problem.
- explanation-07: A growth rate of about 10% in GB is fine for years.
- explanation-07: Sharding solves horizontal scaling, not disk cost.
- explanation-07: A natural shard key such as tenant ID or region can keep queries within a single shard.
- explanation-07: If most queries need cross-shard joins or aggregations, sharding will hurt more than help.
- explanation-07: Cheaper alternatives to sharding include indexing, partitioning within one instance, read replicas, connection pooling, archiving cold data, and vertical scaling.
- explanation-07: That complexity slows every feature that touches multiple entities.
- explanation-07: Partitioning can be time-based or tenant-based and still run on a single instance.
- explanation-07: Partitioning and read replicas are reversible.
- explanation-08: The expected improvement depends entirely on where time is actually spent.
- explanation-08: Binary formats typically help in two ways: smaller payload size and faster parse/serialize.
- explanation-08: Smaller payload size helps if an application is network-bound.
- explanation-08: JSON has overhead from quotes, keys repeated per record, and text-encoded numbers.
- explanation-08: JSON's overhead matters most for large arrays of small objects or numeric-heavy data.
- explanation-08: If payloads are already small or mostly free-text strings, binary formats provide little size benefit.
- explanation-08: Most languages allow wrapping JSON encode/decode in a timer or using a profiler to measure it.
- explanation-08: Switching to a binary format has real costs: schema management, tooling, debuggability, and client compatibility.
- summarization-02: A production deploy copied a staging config template into production.
- summarization-02: The staging pool size of 5 was intended to be small.
- summarization-03: Thumbnail generation currently ties up web workers.
- summarization-03: A worker pool would generate the thumbnails and update the record.
- summarization-04: After clicking the PDF export option, nothing happens initially.
- summarization-04: The issue was reproduced by a second user on a different machine.
- summarization-05: Ada is assigned to check with the mobile team lead about whether the mobile team has been informed of the API deprecation.
- summarization-08: The underlying reason for the 'stuck' perception needs investigation.
- summarization-08: Follow-up with new or template-less users is needed before drawing conclusions about the template gallery.

Added facts (styled only):

- code-review-01: Appending "member" to `roles` and inserting into `db` are two different responsibilities bundled into one function.
- code-review-01: Mixing hardcoded role logic with I/O makes the function harder to test in isolation.
- code-review-01: The corrected version catches `Exception` and logs the error with `logger.error` before returning `False`.
- code-review-02: As written, the function returns whatever the synchronous line produces, not the intended result.
- code-review-03: The query builds its SQL string using `+` string concatenation rather than query parameters.
- code-review-03: A `customer_name` value of `x' OR '1'='1` causes the query to return every row.
- code-review-03: Parameterized queries let the database driver handle escaping.
- code-review-03: A customer name containing an apostrophe, such as `O'Brien`, breaks the string concatenation.
- code-review-03: A customer name containing an apostrophe raises a SQL syntax error.
- code-review-03: Parameterized queries also fix the apostrophe-in-input problem.
- code-review-04: In the fixed version, `value` is a property that acquires `self._lock` before returning `self._value`.
- code-review-05: The script gives no indication of whether it targets POSIX `sh` strictly or assumes Bash features.
- code-review-05: The suggested rewrite validates the argument and exits with status 1 and a usage message on standard error when the argument is empty.
- code-review-06: The recursive branch triggers based only on the type of the existing value `merged[key]`, not on the type of the override `value`.
- code-review-06: The code does not check whether the override value is also a dict.
- code-review-06: If `override[key]` is not a dict, such as a string or an int, `merge_settings` fails when it calls `.items()` on it.
- code-review-06: The code is missing an `isinstance(value, dict)` check.
- code-review-06: "Delete the key" and "don't override with `None`" are different behaviors.
- code-review-06: Writing characterization tests against the function's current behavior before modifying it provides a safety net and a record of current behavior.
- code-review-06: Suggested characterization test cases include nested merge, `None` deletion, type-mismatch cases, and a check for base mutation.
- code-review-07: The backoff schedule is effectively shifted by one step.
- code-review-07: The zero-millisecond first wait appears to be an off-by-one error rather than a deliberate retry-once-immediately policy.
- code-review-07: If `attempts` is less than or equal to 0, the loop body never runs and `fn` is never invoked.
- code-review-07: When `attempts` is 0, the wrapped function returns undefined.
- code-review-07: A caller passing `attempts` of 0 expecting one attempt with no retries gets no call at all.
- code-review-07: The function's failure contract is implicit rather than documented.
- code-review-07: The backoff is a fixed delay of one second per attempt.
- code-review-07: The function does not handle the `Retry-After` header and ignores server-provided retry hints in favor of a fixed backoff.
- code-review-07: There is no way to cancel an in-flight retry sequence because there is no `AbortSignal` support.
- code-review-07: There is no cap on total backoff time when `attempts` is large.
- code-review-08: An unhandled `FileNotFoundError` crashes the whole run and loses the count of files already removed.
- code-review-08: The script's return value is a count named `removed`.
- code-review-08: The `removed` return value is only useful if the caller logs it.
- code-review-08: If `ROOT` does not exist, the script raises an unhandled exception.
- code-review-08: The `ROOT` path is hardcoded in the script.
- code-review-08: The script deletes files in production.
- debugging-04: errors="replace" substitutes invalid byte sequences with the replacement character � instead of raising an exception.
- debugging-06: The most likely cause of the export job failures is connection pool exhaustion from contention with the analytics service.
- debugging-06: The failures are not caused by a code bug in the export job itself.
- debugging-06: The export job and the analytics service share a database.
- debugging-06: The export job failures vary by batch number.
- debugging-06: Failures varying by batch number indicate timing-based contention rather than a specific query.
- debugging-06: A database shared with an unrelated service is a common source of this failure pattern.
- debugging-06: The analytics service may hold database connections during its own nightly run.
- debugging-06: If both services size their connection pools for their own peak rather than the combined peak, the pool exhausts intermittently.
- debugging-06: The export job failures occur once a week.
- debugging-06: The failures occur when the two jobs' schedules overlap.
- debugging-06: A slow or unindexed analytics query can hold a connection far longer than expected and starve the pool for other clients.
- debugging-06: A connection that is not released after use shrinks the effective pool size over time until it fails under load.
- debugging-06: A retry occurred at 02:14:08.
- debugging-06: The retry fired 1 second after the failure.
- debugging-06: The retry hit the same exhausted pool 33 seconds later.
- debugging-06: Retries without backoff or jitter can compound contention rather than relieve it.
- debugging-06: The export job fails at approximately 02:14 UTC.
- debugging-06: The retry policy includes an attempt 2.
- debugging-06: Adding backoff and jitter to the retry policy is not a fix, but removes retries as a compounding cause.
- debugging-06: Without logging pool size, active connections, and wait-queue depth at the moment of timeout, the failure cannot be diagnosed.
- debugging-06: A slow analytics query holding a connection would appear in database slow-query logs covering 02:10-02:15 UTC.
- debugging-06: Separate pools per service, or a reserved minimum pool size for the export job, would prevent analytics from starving the export job entirely.
- debugging-06: The failure can be confirmed by reproducing it on demand by running both jobs concurrently under load, or by confirming via pool metrics and slow-query logs that analytics activity coincides with every failure night.
- debugging-07: The test seeds three events by making three separate 'create event' calls.
- debugging-07: The digest returns two events instead of the three that were seeded.
- debugging-07: CI runs the test suite with four-way parallelism.
- debugging-07: CPU contention under CI's parallelism slows writes.
- debugging-07: The failure does not occur on a serial development machine.
- debugging-07: Logs and artifacts for the failing test are not currently retained by CI.
- debugging-07: The test does not assert on the response of each individual 'create event' call.
- debugging-07: The test only asserts on the final digest count.
- debugging-07: A digest that deduplicates events by a coarse key, such as a millisecond timestamp, can merge two events created back-to-back under load into one.
- debugging-07: If the digest filters by a time window, a slow CI worker can push an event's timestamp outside that window.
- debugging-07: A create-event call can fail or be throttled under load.
- debugging-07: Overlapping cleanup or teardown from another parallel worker can delete an event if fixtures share an account ID, timestamp window, or fixture data.
- debugging-07: The `-n4` flag sets the number of parallel test workers.
- debugging-07: `stress-ng` can generate artificial CPU load on a development machine.
- debugging-07: pytest-xdist assigns each worker a `PYTEST_XDIST_WORKER` ID.
- debugging-07: The `PYTEST_XDIST_WORKER` ID can be used to confirm test isolation between workers.
- debugging-07: If retrying the digest read with a short backoff makes the failure disappear, that indicates an async or eventual-consistency race rather than a data-loss bug.
- debugging-07: Reproducing the failure under artificial load and parallelism would confirm timing/parallelism as the trigger.
- debugging-07: Asserting on each seed call's response distinguishes whether the gap is in seeding or in reading.
- debugging-07: The missing CI artifacts are the main reason the bug is hard to diagnose.
- debugging-08: Because the cache bound is unchanged and the canary still grows, the cache is probably not the main driver of the memory growth.
- debugging-08: Correlation with marketing campaigns points to a leak triggered by request volume.
- debugging-08: Unreleased listeners, timers, or per-request objects are examples of request-volume-triggered leaks.
- debugging-08: Connection or session objects that accumulate under load are examples of request-volume-triggered leaks.
- debugging-08: pprof is a heap profiling tool for Go.
- debugging-08: heapdump is a heap profiling tool for Node.
- debugging-08: JFR is a heap profiling tool for Java.
- debugging-08: Diffing a heap profile taken during business hours against one taken right before restart can identify the leak.
- debugging-08: Object counts that scale with request count rather than with unique products indicate a traffic-correlated leak.
- debugging-08: A metrics registry that creates a new label combination per request is an example of unbounded growth keyed by request or event.
- debugging-08: An in-memory queue with no eviction is an example of unbounded growth.
- debugging-08: If the canary's growth is roughly constant per hour, a time-based accumulator such as metrics, a logs buffer, or a scheduled task is more likely than a request-scoped leak.
- debugging-08: If the baseline never returns but the heap profile shows no growing live-object graph, the cause may be memory fragmentation rather than a leak.
- debugging-08: Memory fragmentation is memory the allocator holds but does not return to the OS.
- debugging-08: Go's runtime reports HeapAlloc and HeapSys.
- debugging-08: The JVM reports used heap and committed heap.
- debugging-08: A gap between RSS and the runtime's reported live-heap size that widens over the week points to fragmentation or a runtime not returning pages, not a leak.
- debugging-08: A single heap profile diff comparing business hours to pre-restart often narrows the list of hypotheses to one.
- explanation-01: The number of possible keys usually exceeds the number of available indexes.
- explanation-01: Collisions are unavoidable in a hash map.
- explanation-02: `SELECT ... FOR UPDATE` locks the selected rows so no other transaction can read or write them until the transaction commits.
- explanation-03: A network path may be a fast local link or a slow, congested route across several routers with limited buffer space.
- explanation-03: Congestion collapse was a real problem on the early internet.
- explanation-03: On detecting packet loss, the sender reduces cwnd and adjusts ssthresh based on the current window size.
- explanation-04: Python and Ruby run only one thread at a time per process for CPU-bound work, even on a multi-core machine.
- explanation-05: A cache keyed by user session that never expires entries is an example of an unbounded collection leak.
- explanation-06: A cache only helps when the system has spare capacity outside the database.
- explanation-06: Without profiling, you cannot confirm that reads repeat or that spare capacity exists.
- explanation-06: Writes still hit the database even when a read cache is in place.
- explanation-06: An index fix is often cheaper and safer than a cache.
- explanation-07: Write throughput justifies sharding when the write capacity of the largest instance the cloud provider offers is reached even after tuning.
- explanation-07: Data size justifies sharding when the working set no longer fits in memory and disk I/O becomes the bottleneck even on the biggest available disk.
- explanation-07: Query latency justifies sharding when read replicas and indexing no longer keep p99 latency acceptable under load.
- explanation-07: Many situations where teams believe they need to shard are actually unindexed queries.
- explanation-07: Partitioning within a single instance is appropriate when specific tables are large or hot.
- explanation-07: Postgres does not natively support cross-shard joins, transactions, and aggregations.
- explanation-07: After sharding, every migration, backup, and schema change runs N times instead of once.
- explanation-07: Vertical scaling has a ceiling that may be reached before sharding is ready.
- explanation-07: Vertical scaling can be used as a stopgap while sharding is designed properly.
- explanation-08: The average and maximum payload sizes for representative requests should be measured.
- summarization-02: A deploy the night before the incident copied a database connection pool size from the staging template into production.
- summarization-05: The listed action items come from a sprint planning meeting.
- summarization-06: The team has not yet shown evidence supporting the retry-storm explanation.
- summarization-07: Staging runs a newer kernel than production.
- summarization-08: The second finding, that the progress bar causes abandonment on large files, is labeled firm.
- summarization-08: The stuck-looking progress bar is a perception issue rather than a functional bug.
- summarization-08: The report recommends that the team update the progress indicator for large files.

### plain-language

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 28 | 15 | 0.536 | 24 | 2 |
| code-review-02 | 19 | 13 | 0.684 | 19 | 1 |
| code-review-03 | 24 | 21 | 0.875 | 19 | 3 |
| code-review-04 | 26 | 20 | 0.769 | 22 | 8 |
| code-review-05 | 27 | 19 | 0.704 | 34 | 3 |
| code-review-06 | 38 | 0 | 0.0 | 2 | 2 |
| code-review-07 | 30 | 19 | 0.633 | 29 | 5 |
| code-review-08 | 34 | 26 | 0.765 | 33 | 0 |
| debugging-01 | 7 | 7 | 1.0 | 8 | 0 |
| debugging-02 | 19 | 9 | 0.474 | 15 | 2 |
| debugging-03 | 10 | 10 | 1.0 | 9 | 0 |
| debugging-04 | 15 | 12 | 0.8 | 15 | 5 |
| debugging-05 | 17 | 15 | 0.882 | 14 | 0 |
| debugging-06 | 4 | 0 | 0.0 | 35 | 35 |
| debugging-07 | 0 | 0 | n/a | 28 | 28 |
| debugging-08 | 28 | 11 | 0.393 | 39 | 22 |
| explanation-01 | 39 | 20 | 0.513 | 20 | 1 |
| explanation-02 | 24 | 14 | 0.583 | 27 | 4 |
| explanation-03 | 35 | 21 | 0.6 | 21 | 1 |
| explanation-04 | 39 | 26 | 0.667 | 33 | 0 |
| explanation-05 | 18 | 16 | 0.889 | 15 | 1 |
| explanation-06 | 21 | 18 | 0.857 | 26 | 3 |
| explanation-07 | 26 | 15 | 0.577 | 27 | 6 |
| explanation-08 | 18 | 14 | 0.778 | 15 | 5 |
| summarization-01 | 5 | 5 | 1.0 | 6 | 0 |
| summarization-02 | 12 | 11 | 0.917 | 11 | 0 |
| summarization-03 | 13 | 12 | 0.923 | 13 | 0 |
| summarization-04 | 13 | 12 | 0.923 | 11 | 1 |
| summarization-05 | 9 | 9 | 1.0 | 13 | 2 |
| summarization-06 | 12 | 12 | 1.0 | 12 | 0 |
| summarization-07 | 14 | 13 | 0.929 | 14 | 1 |
| summarization-08 | 20 | 16 | 0.8 | 27 | 3 |

Median fraction: 0.778 over 31 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python footgun.
- code-review-01: A bare `except:` catches everything, including `KeyboardInterrupt` and `SystemExit`.
- code-review-01: Duplicate roles aren't prevented.
- code-review-01: Calling the function with `roles=["member"]` explicitly produces `["member", "member"]`.
- code-review-01: The function returns a bare `True`/`False`, which gives no indication of why something failed.
- code-review-01: An uninformative return value makes it hard for callers to distinguish validation errors from DB errors or misuse and react appropriately.
- code-review-01: The function has no docstring and no type hints.
- code-review-01: Missing type hints is a minor issue.
- code-review-01: Type hints of `name: str`, `roles: list[str] | None`, and a type for `db` would clarify the function's contract.
- code-review-01: A safer rewrite uses `roles=None` as the default and raises `ValueError` when `name` or `db` is missing.
- code-review-01: The safer rewrite copies `roles` with `list(roles)` and appends `"member"` only if it is not already present.
- code-review-01: The rewrite drops the silent failure mode by letting real errors propagate.
- code-review-01: An alternative to letting errors propagate is catching a specific DB exception in order to translate it.
- code-review-02: There is no validation that the response `data` has a `name` property.
- code-review-02: If the API returns an error object instead of a profile, `data.name` could be `undefined` and calling `.toUpperCase()` on it would throw.
- code-review-02: There is no input validation on `userId`.
- code-review-02: Unsanitized/unencoded `userId` could allow injection of unexpected path segments such as `../` or query-like content.
- code-review-02: `encodeURIComponent(userId)` can be used to encode `userId` before interpolating it into the URL.
- code-review-02: The fixed version awaits `fetch` with an encoded `userId`, throws an Error including `res.status` when `!res.ok`, awaits `res.json()`, throws an Error when the response is missing `name`, and returns `data.name.toUpperCase()`.
- code-review-03: psycopg2 uses `%s` as its parameter placeholder.
- code-review-03: pymysql uses `%s` as its parameter placeholder.
- code-review-03: `fetchall` can raise an exception, for example on a bad connection or a database error.
- code-review-04: Python's GIL guarantees that each individual bytecode operation is atomic.
- code-review-04: A single assignment is atomic in CPython.
- code-review-04: `reset` by itself will not corrupt the counter's state.
- code-review-04: An example of the reset/increment race is resetting to 0 and then a stale increment writing 1.
- code-review-04: The class has no thread-safety documentation or contract.
- code-review-04: A caller reading the code has no way to know the class is unsafe under concurrent use.
- code-review-05: `cd` with no arguments changes to the user's $HOME directory.
- code-review-05: With an empty BACKUP_DIR, `rm -rf *.tmp` would run in the user's home directory instead of failing.
- code-review-05: Bash has a `nullglob` option affecting unmatched glob behavior.
- code-review-05: `rm -rf *.tmp` is the most dangerous line in the script.
- code-review-05: `for f in $(ls *.log)` breaks on filenames containing spaces, newlines, or glob characters.
- code-review-05: When no .log files exist, `ls *.log` prints an error to stderr and returns nothing usable.
- code-review-05: `${1:?Usage: ...}` makes the first argument required.
- code-review-05: The `-r` flag is unnecessary for `rm` because the targets are files, not directories.
- code-review-06: `dict(base)` copies only the top-level dict.
- code-review-06: Nested dicts and lists in `base` are shared by reference with the returned `merged`.
- code-review-06: Mutating a nested value in `merged` for a key untouched by `override` also mutates `base`.
- code-review-06: Only keys that are actually recursed into get rebuilt as new dicts.
- code-review-06: Sibling keys not recursed into remain aliased to the originals in `base`.
- code-review-06: A `None` value in `override` always means delete the key.
- code-review-06: There is no way to explicitly set a key's value to `None` through `override`.
- code-review-06: Given `override = {"timeout": None}`, it is impossible to distinguish deleting `timeout` from setting it to `None`.
- code-review-06: Resolving the `None`-means-delete ambiguity requires a sentinel such as a `DELETE` marker if both behaviors are needed.
- code-review-06: `merged.pop(key, None)` silently does nothing if the key is not present in `base`.
- code-review-06: Silently no-oping on a missing key can hide a typo, such as a misspelled key intended to delete something.
- code-review-06: If `base[key]` is a dict and `override[key]` is not a dict, the `elif` branch fails and control falls to the `else` branch.
- code-review-06: In that case the entire nested dict is replaced by the scalar value.
- code-review-06: If `base[key]` is a scalar and `override[key]` is a dict, no recursion occurs and the override dict replaces the scalar wholesale.
- code-review-06: No validation or error is raised for either type-mismatch case.
- code-review-06: The type-mismatch behavior could mask a configuration mistake.
- code-review-06: Recursion depth follows the depth of `override`'s nested dicts.
- code-review-06: There is no depth limit on the recursion.
- code-review-06: Deeply nested or self-referential structures could cause a `RecursionError` or an infinite loop if a dict contains itself.
- code-review-06: Self-referential structures are unlikely for JSON-like config but possible if `base` or `override` are constructed programmatically.
- code-review-06: Only `dict` receives special handling in the merge.
- code-review-06: Lists, sets, and tuples are always fully replaced rather than merged or concatenated.
- code-review-06: List replacement is a common convention in settings-merge functions.
- code-review-06: Some config systems expect list concatenation or index-wise merging.
- code-review-06: There is no check that `base` and `override` are actually dicts.
- code-review-06: There is no check that keys are hashable or strings.
- code-review-06: Passing a non-dict `override` fails with `AttributeError: 'X' object has no attribute 'items'` rather than a clear error.
- code-review-06: `isinstance(merged[key], dict)` also matches dict subclasses.
- code-review-06: Recursing into an `OrderedDict` or custom dict subclass via `merge_settings` returns a plain `dict`, losing the subclass type.
- code-review-06: Recursive merging of nested dicts is clearly the core purpose of the function.
- code-review-06: Non-dict values fully overriding reflects typical 'last writer wins' semantics.
- code-review-06: Using `None` as a delete sentinel is a common pattern in config-merge libraries.
- code-review-06: Ansible and Kubernetes strategic merge patches use conventions similar to `None`-as-delete.
- code-review-06: The lack of a way to explicitly set `None` is a real gap if a setting legitimately needs to be `None`.
- code-review-06: The shallow-copy aliasing issue and the silent type-mismatch overwrite are almost certainly bugs or oversights.
- code-review-06: Those two issues tend to pass testing and later cause hard-to-trace mutation bugs or config-clobbering incidents in production.
- code-review-06: Issues #1 and #4 are the highest-priority items to write tests around and confirm intent for.
- code-review-06: Issues #1 and #4 are the ones most likely to fail silently.
- code-review-07: The function has three different signals for failure: a thrown error that never happens, null, and undefined.
- code-review-07: The inconsistency in failure signals indicates the retry-exhaustion path was never tested.
- code-review-07: Swallowing non-HTTP errors as null is the most dangerous issue in the code, especially with callers that cannot be audited.
- code-review-07: Retrying server errors with zero delay defeats the purpose of backoff and could contribute to a thundering-herd effect.
- code-review-07: Discarding errors without a trace can cause silent data corruption downstream in a shared library with unknown callers.
- code-review-07: The backoff is linear rather than exponential and includes no jitter.
- code-review-07: Most retry helpers use exponential backoff to avoid synchronized retry storms across clients.
- code-review-07: The attempts semantics are not a bug.
- code-review-07: Only 429 receives backoff and retry, while other 4xx errors fail immediately.
- code-review-07: The error categorization appears intentional even though the missing 5xx delay looks like an oversight.
- code-review-07: The riskiest problem in the code is the error-handling contract rather than a syntax bug.
- code-review-08: The unconditional `tmp-`/`.part` deletion is the most dangerous line in the file.
- code-review-08: The script has no dry-run mode.
- code-review-08: `os.listdir()` loads the entire directory listing into memory at once.
- code-review-08: The in-memory listing is acceptable for modest directories and only a concern if `ROOT` grows very large.
- code-review-08: Iteration order is filesystem-dependent and not sorted by age.
- code-review-08: Because iteration order is arbitrary, which files survive when the 500 cap is reached is effectively arbitrary rather than oldest-first.
- code-review-08: Unconditional removal of `tmp-`/`.part` files could be an intentional 'always junk' assumption.
- code-review-08: The two highest-priority changes are guarding against directories and requiring a minimum age before deleting `.part`/`tmp-` files.
- debugging-02: Class bodies are always in strict mode.
- debugging-02: Strict mode propagates to functions nested inside strict-mode code.
- debugging-02: A regular `function () {...}` passed to `setInterval` from inside a class method has `this === undefined` when called.
- debugging-02: Accessing `this.seconds` when `this` is `undefined` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: Seeing `NaN` instead of a thrown error indicates the code is running in a non-strict/sloppy context.
- debugging-02: Running code directly in a browser `<script>` without `"use strict"` is an example of a non-strict/sloppy context.
- debugging-02: Some transpilation does not preserve strict mode, producing a sloppy-mode context.
- debugging-02: Calling `.bind(this)` on the callback function is an alternative fix.
- debugging-02: Storing `const self = this;` before `setInterval` and using `self` inside the callback is an alternative fix.
- debugging-02: The arrow function is the cleanest modern approach among these fixes.
- debugging-04: The non-ASCII byte occurs at byte offset 512 in the file.
- debugging-04: For line counting, UTF-8 with errors="replace" is usually the pragmatic fix.
- debugging-04: The errors="surrogateescape" option preserves byte fidelity.
- debugging-05: The same test running twice can also cause the extra `"post"` entries, for example via test discovery, parametrization, or fixtures.
- debugging-05: In the fixed code, `make_post` is defined as `def make_post(title, tags=None)` and sets `tags = list(DEFAULT_TAGS)` when `tags is None`.
- debugging-06: The speaker intends to check memory for prior context on the system.
- debugging-06: A tool call was made to list files and directories in a given path.
- debugging-06: The status of that tool call was 'Completed'.
- debugging-06: The tool call's terminal output was 'No files found'.
- debugging-08: The count-bounded-cache explanation fits all four reported observations.
- debugging-08: Cache entries persist until they are evicted, so cache-driven memory growth survives quiet nights.
- debugging-08: Any traffic populates the cache, so cache-driven growth occurs even without webhooks.
- debugging-08: Guava and Caffeine caches offer a `maximumSize` setting and a `maximumWeight` setting.
- debugging-08: Long-lived maps used for deduplication, idempotency keys, rate limiting, or session and request tracking are a classic source of leaks when their TTL cleanup is absent, broken, or slow.
- debugging-08: Dynamically generated classes from serialization libraries, proxies, or template engines leak metaspace rather than heap.
- debugging-08: More campaign SKUs and variants can produce more dynamically generated types.
- debugging-08: Classes are not unloaded until their classloader is garbage collected.
- debugging-08: Application classloaders often are never garbage collected.
- debugging-08: `jstat -gc` or an APM memory breakdown can distinguish heap growth from non-heap/metaspace growth.
- debugging-08: Native or off-heap memory, such as Netty direct buffers and native codecs, can leak on specific code paths.
- debugging-08: Off-heap leaks are consistent with growth that survives quiet nights and correlates with traffic volume.
- debugging-08: If RSS grows well beyond JVM-reported heap usage, the growth is native or off-heap.
- debugging-08: NativeMemoryTracking, `pmap`, and `smaps` diffs can be used to investigate native memory growth.
- debugging-08: The cache-bound hypothesis is the only one of the four consistent with all four clues without positing an additional leak.
- debugging-08: Switching the cache to weight-based eviction would be a one-line fix.
- debugging-08: The canary-still-grows observation is the strongest evidence that something grows independently of the cache.
- explanation-01: A hash map stores the value at the computed index in an underlying array.
- explanation-01: An array slot cannot hold two values at once.
- explanation-01: The collection in a chained slot is usually a linked list, and sometimes a small array or tree.
- explanation-01: The rule for finding another open slot in open addressing is called a probe sequence.
- explanation-01: Linear probing tries the next index, then the next, and so on.
- explanation-01: Quadratic probing tries indices at increasing squared steps.
- explanation-01: Double hashing uses a second hash function to decide the step size.
- explanation-01: Open addressing can fail entirely if the array is full.
- explanation-01: Deletion in chaining is simple because the node is just removed from the list.
- explanation-01: Deletion in open addressing is trickier because emptying a slot breaks the probe chain for other keys.
- explanation-01: Deletion in open addressing usually needs tombstone markers.
- explanation-01: Chaining eventually needs resizing, but less urgently than open addressing.
- explanation-01: Chaining is simpler to reason about than open addressing.
- explanation-01: Deletion and resizing are more delicate to implement correctly in open addressing.
- explanation-01: Most general-purpose hash maps used day-to-day use chaining.
- explanation-01: Java's HashMap uses chaining.
- explanation-01: Java converts long chains to trees for performance.
- explanation-01: Python's dict uses open addressing.
- explanation-01: Many high-performance C++ hash maps use open addressing.
- explanation-02: Pessimistic locking locks data as soon as it is read.
- explanation-02: In SQL, 'SELECT * FROM accounts WHERE id = 1 FOR UPDATE' locks the selected row.
- explanation-02: The SQL FOR UPDATE clause locks the row until the transaction commits or rolls back.
- explanation-02: When a row is locked with FOR UPDATE, other transactions attempting SELECT ... FOR UPDATE or UPDATE on that row will block.
- explanation-02: Pessimistic locking fits when the cost of a failed or retried transaction is high, such as money transfers and seat or ticket reservations.
- explanation-02: In optimistic locking, the read retrieves the row's version, and the update sets new values and increments the version while restricting the WHERE clause to the previously read version.
- explanation-02: In optimistic locking, if the versioned UPDATE affects 0 rows, someone else updated the row first, and the application must retry or fail.
- explanation-02: In optimistic locking, the WHERE version = N check catches conflicts at commit time.
- explanation-02: Optimistic locking fits for long-lived transactions or when there is user think time between read and write, such as editing a form in a browser.
- explanation-02: Holding a database lock during user think time would be wasteful.
- explanation-03: Before congestion control existed, dropped packets could snowball into congestion collapse.
- explanation-03: Congestion collapse is when a congested network becomes even more congested because senders keep retransmitting lost data.
- explanation-03: The congestion window limits how much unacknowledged data the sender may have in flight at once.
- explanation-03: Historically the initial cwnd was 1 segment.
- explanation-03: The initial cwnd is now typically 2-10 segments per RFC 6928.
- explanation-03: For every ACK received confirming successful delivery of a segment, the sender increases cwnd.
- explanation-03: During slow start, cwnd grows by roughly one segment per ACK.
- explanation-03: Slow start is called 'slow' only relative to the older approach of immediately sending as much as the receiver's window allowed.
- explanation-03: Exponential growth lets a connection reach a reasonable sending rate in a few RTTs, on the order of log base 2 of the target window.
- explanation-03: Reaching a reasonable sending rate quickly matters a lot for short connections such as most web requests.
- explanation-03: ssthresh is often set from a previous congestion event.
- explanation-03: When cwnd reaches ssthresh, TCP switches to the linear growth of congestion avoidance.
- explanation-03: This congestion control philosophy is why the internet has remained stable even as usage grew enormously.
- explanation-03: Every TCP connection cooperates to avoid overwhelming shared links rather than assuming its capacity upfront.
- explanation-04: A process has its own memory address space, file descriptors, and OS-level resources.
- explanation-04: Each thread has its own stack and register/instruction pointer state.
- explanation-04: Switching between threads is cheaper than switching between processes.
- explanation-04: Thread communication requires careful synchronization, such as locks and mutexes, to avoid race conditions.
- explanation-04: Threads provide parallelism with shared state and need synchronization.
- explanation-04: Nginx and Apache use worker processes.
- explanation-04: When a server uses worker processes, one worker dying does not kill the server.
- explanation-04: The OS lets you set per-process limits on memory, CPU, and file descriptors via cgroups and ulimits.
- explanation-04: Per-process resource limits are hard or impossible to apply to a single thread within a shared process.
- explanation-04: Microservices and worker pools are examples of components with independent lifecycles that can be killed and respawned.
- explanation-04: Threads are preferable for tasks that are lightweight, need to share state efficiently, and are I/O-bound.
- explanation-04: I/O-bound tasks wait on network or disk.
- explanation-04: GIL and shared-state concerns matter less for I/O-bound tasks.
- explanation-05: Listeners often close over additional state.
- explanation-05: Caches without a TTL, without a size limit, or using strong keys instead of weak references are unbounded.
- explanation-06: A cache does not help when slowness comes from lock contention caused by writes.
- explanation-06: A cache does not help when slowness comes from an N+1 query problem.
- explanation-06: Slow query logs and DB metrics show whether the database is CPU or IO bound or whether the app is slow elsewhere.
- explanation-07: Rebalancing is a source of sharding complexity.
- explanation-07: The product team's inability to estimate growth is the real problem.
- explanation-07: A growth rate of about 10% in GB is fine for years.
- explanation-07: A growth rate of 10x per year changes the calculus.
- explanation-07: Sharding solves horizontal scaling, not disk cost.
- explanation-07: A natural shard key such as tenant ID or region can keep queries within a single shard.
- explanation-07: If most queries need cross-shard joins or aggregations, sharding will hurt more than help.
- explanation-07: Cheaper alternatives to sharding include indexing, partitioning within one instance, read replicas, connection pooling, archiving cold data, and vertical scaling.
- explanation-07: Postgres on modern hardware comfortably handles multi-terabyte databases when those cheaper measures are in place.
- explanation-07: Waiting leaves less room to test the shard key choice.
- explanation-07: Partitioning and read replicas are reversible.
- explanation-08: JSON has overhead from quotes, keys repeated per record, and text-encoded numbers.
- explanation-08: JSON's overhead matters most for large arrays of small objects or numeric-heavy data.
- explanation-08: If payloads are already small or mostly free-text strings, binary formats provide little size benefit.
- explanation-08: Most languages allow wrapping JSON encode/decode in a timer or using a profiler to measure it.
- summarization-02: The incident ran from 09:14 to 09:48 UTC.
- summarization-03: A worker pool would generate the thumbnails and update the record.
- summarization-04: The issue was reproduced by a second user on a different machine.
- summarization-07: Aside from the median latency drop and the memory increase, the results of the comparison are uncertain.
- summarization-08: The progress bar finding is rated FIRM for the behavior and TENTATIVE for the cause.
- summarization-08: 2 of those 3 participants abandoned the import as a result.
- summarization-08: The abandonment behavior is a real, actionable problem regardless of its cause.
- summarization-08: Follow-up with new or template-less users is needed before drawing conclusions about the template gallery.

Added facts (styled only):

- code-review-01: The function contains five problems.
- code-review-01: The suggested rewrite catches only the error expected from `db.insert`.
- code-review-02: The calls should be wrapped in a `try`/`catch` block.
- code-review-03: Passing `' OR '1'='1` as the status value could return every row in the table.
- code-review-03: Selecting every column wastes bandwidth.
- code-review-03: A database driver can enforce input type and format through parameter binding.
- code-review-04: A thread running `reset` can overwrite an increment that happened moments earlier.
- code-review-04: There is no way to read `value` safely.
- code-review-04: Reading `self.value` directly from another thread while `increment` or `reset` is mid-update is not guarded.
- code-review-04: Relying on the atomicity of Python attribute reads is fragile and not guaranteed by the language.
- code-review-04: The suggested fix stores the count in a `_value` attribute and creates a `threading.Lock` as `_lock` in `__init__`.
- code-review-04: In the suggested fix, `increment` performs `self._value += 1` while holding the lock.
- code-review-04: In the suggested fix, `reset` sets `self._value = 0` while holding the lock.
- code-review-04: In the suggested fix, `value` is a property that returns `self._value` while holding the lock.
- code-review-05: A guard using `if [ -z "$1" ]; then echo "Usage: $0 <backup_dir>" >&2; exit 1; fi` adds the missing argument check.
- code-review-05: If there are no .tmp files, most shells leave the literal string `*.tmp` in place.
- code-review-05: Placing `--` before filenames protects against filenames starting with a dash being misread as options.
- code-review-06: A tool call was made to the Glob tool.
- code-review-06: The Glob tool call has a status of Completed.
- code-review-07: The delay expression was probably meant to be `1000 * (i + 1)`.
- code-review-07: There is no input validation on `attempts`.
- code-review-07: Passing `0` or a negative value for `attempts` means the loop never runs and the function returns `undefined` with no explanation.
- code-review-07: The absence of a delay on the first 429 retry is likely an off-by-one typo rather than intentional.
- code-review-07: Whether the absence of delay before 5xx retries is intentional is unclear.
- debugging-02: Inside a regular function called by setInterval, `this` refers to the global object.
- debugging-02: Every tick of the interval prints `NaN` in the failing code.
- debugging-04: Python raises UnicodeDecodeError when it encounters a byte outside the ASCII range while decoding as ASCII.
- debugging-04: UTF-8 is an encoding that supports the full range of characters.
- debugging-04: errors="ignore" is an alternative to errors="replace".
- debugging-04: errors="replace" substitutes a placeholder character for bad bytes instead of crashing.
- debugging-04: If every byte must be preserved, the file's actual encoding should be detected first rather than guessed.
- debugging-06: The nightly export and the analytics service compete for the same limited pool of database connections.
- debugging-06: When both services need connections at once, the export waits, times out after 30 seconds, and fails.
- debugging-06: The export job's timeout is 30 seconds.
- debugging-06: The export failures occur at random batch numbers.
- debugging-06: Any batch can be the one caught when the connection pool is briefly full.
- debugging-06: The export failures happen only sometimes, not on every run.
- debugging-06: The intermittent failures occur only when the analytics service's load lines up with the export's timing.
- debugging-06: The connection pool may be too small for the combined load of both services.
- debugging-06: Each service may have its own pool while both draw from a shared connection limit on the database server.
- debugging-06: A connection leak in one of the services could be a contributing cause.
- debugging-06: A connection that isn't returned to the pool after use shrinks the pool over time.
- debugging-06: Connections can fail to be returned to the pool after an error or a slow query.
- debugging-06: A slow or blocking query from the analytics service could hold connections for a long time and starve the export.
- debugging-06: The retry logic retries a batch immediately when it times out.
- debugging-06: Several batches retrying at once can add more requests to an already-full pool and delay recovery.
- debugging-06: A scheduled job overlap, such as a weekly analytics report or backup, could run on some nights but not others.
- debugging-06: A job that runs on some nights but not others would explain why the failure is not nightly.
- debugging-06: Current logging shows that the pool was exhausted but not why.
- debugging-06: Pool size, active connections, and idle connections can be logged at the moment a request waits or times out.
- debugging-06: The analytics service has logs or a job schedule that can be pulled for the same time window.
- debugging-06: Failures lining up with analytics activity would confirm contention.
- debugging-06: Postgres provides `pg_stat_activity` for connection and lock statistics.
- debugging-06: Other databases have equivalents to `pg_stat_activity`.
- debugging-06: Database connection and lock stats can reveal long-running or blocked queries.
- debugging-06: Checking historical database stats requires having monitoring history.
- debugging-06: The surrounding log context for this job keeps getting rotated away.
- debugging-06: Log retention can be increased, or a dedicated alert can capture more context when the error fires.
- debugging-06: A dedicated alert could capture stack trace, active query, and pool stats.
- debugging-06: Connection or session release failures are especially likely in exception-handling paths.
- debugging-06: Adding jitter to retry logic spaces retries out randomly and can reduce pile-up pressure on the pool.
- debugging-06: The export job can be run together with a simulated or real analytics workload in a test environment.
- debugging-06: Reproducing the failure under load would allow testing fixes without waiting a week.
- debugging-06: The failure currently recurs on roughly a weekly basis.
- debugging-06: Steps 1 and 2 cost the least and are most likely to confirm the contention theory.
- debugging-06: Steps 1 and 2 would capture the missing context for the next failure instead of losing it to rotation.
- debugging-07: A timing race between writing events and reading the digest is a likely cause of the failure.
- debugging-07: If event creation triggers an async step, the test may request the digest before all three events are visible.
- debugging-07: Async steps in event creation can include a queue, a background worker, or a search index that updates after a short delay.
- debugging-07: A timing race fits the described pattern: it requires load to appear, passes when nothing else competes for CPU or database connections, and does not involve code correctness.
- debugging-07: Test data leaking between parallel workers is a likely cause of the failure.
- debugging-07: If two tests share a user ID, account ID, or time window, a test running at the same moment could delete or overwrite the three seeded events.
- debugging-07: Cross-test data leakage only shows up under parallelism.
- debugging-07: A boundary condition in the digest's time window is a likely cause of the failure.
- debugging-07: If the digest query filters by events in the last N minutes, a slow CI machine could push the last-seeded event's timestamp just outside that window.
- debugging-07: Four workers competing for resources make a time-window boundary failure more likely than a serial run.
- debugging-07: A colliding ID is a likely cause of the failure.
- debugging-07: If event IDs come from a timestamp or a counter instead of a guaranteed-unique source, two events created close together under load could collide.
- debugging-07: An ID collision would cause one event to silently overwrite the other.
- debugging-07: Running only this test file alone with `pytest -n 4` in a loop of 100-200 iterations isolates parallelism from cross-test interference.
- debugging-07: If the test fails when run alone, the problem is resource contention or async timing rather than another test's data.
- debugging-07: If the test never fails alone but fails in the full suite, the cause is shared state between tests, such as the same tenant, time window, or fixture.
- debugging-07: CI does not retain logs or artifacts.
- debugging-07: The test can be made to print the seeded event IDs, their timestamps, and the digest's actual contents on failure.
- debugging-07: `pytest --tb=long` with a custom assertion message, or a print statement gated on failure, yields real data on the next flake instead of guesswork.
- debugging-07: Determining whether event creation is synchronous requires inspecting the API code the test calls.
- debugging-07: If a queue, background job, or async index update is involved in event creation, that is the top suspect.
- debugging-07: An explicit wait or poll for consistency should be added to the test rather than assuming the write is complete when the API call returns.
- debugging-07: The digest's time filter should be checked for conditions like 'last N minutes' or 'since timestamp X'.
- debugging-07: If the time-filter boundary is tight, a slow test run could cut off the last event.
- debugging-07: Adding a short random sleep in event creation locally and then running the test is a way to stress-test for the race.
- debugging-07: If an artificial delay reproduces the failure, that confirms a race condition.
- debugging-07: The test seeds three events.
- debugging-07: The test suite runs with four parallel workers.
- debugging-08: There is an additional smaller baseline leak that occurs even without traffic.
- debugging-08: An unbounded structure keyed by request or webhook data is the most likely cause.
- debugging-08: A map, list, event listener, or subscription may add an entry per request but only remove it on the happy path.
- debugging-08: An unbounded request-keyed structure matches all three of the reported clues.
- debugging-08: The canary's growth implies a similar structure is filled by other traffic such as cron jobs, health checks, or internal calls.
- debugging-08: Taking two heap dumps 24 hours apart and comparing object counts can reveal collections that keep growing.
- debugging-08: Global or singleton maps, caches, and listener lists should be checked so that every path that adds an entry also removes it, including error and timeout paths.
- debugging-08: Listeners or timers that are never removed are a possible cause of the leak.
- debugging-08: Each webhook or order may register a callback, timer, or event listener that should be removed when the event finishes but is not.
- debugging-08: Some frameworks silently leave callbacks attached to a long-lived object, causing them to accumulate.
- debugging-08: Searching for addEventListener, on(, subscribe, or setInterval equivalents and confirming each has a matching removal can detect unremoved listeners.
- debugging-08: In a heap dump, a growing instance count for classes named Listener, Callback, or Handler indicates accumulating listeners.
- debugging-08: The user stated the cache is size-bounded and has not changed in a year.
- debugging-08: A cache eviction policy can be broken for some key patterns.
- debugging-08: If cache keys include unbounded values such as session IDs or timestamps, the cache can create unlimited distinct keys while appearing to stay within its entry limit.
- debugging-08: Logging the cache's entry count and estimated memory use hourly can distinguish the two cache failure modes.
- debugging-08: Entry count climbing past the bound indicates a broken eviction policy.
- debugging-08: Background jobs, connection pools, log buffers, metric collectors, and health check handlers run on every instance regardless of webhooks.
- debugging-08: The baseline leak explains why memory growth is not zero when the system is idle.
- debugging-08: Disabling one subsystem at a time on a staging copy of the canary and watching the growth rate can isolate the baseline leak.
- debugging-08: Comparing the canary's growth rate to an instance with no cron jobs can isolate how much growth comes from background work.
- debugging-08: Comparing object counts before and after a quiet night identifies leak candidates as anything that fails to shrink back.
- explanation-01: Chaining performance stays steady as the map fills up.
- explanation-02: A rejected optimistic-locking save produces a 'record was modified' error.
- explanation-02: After an optimistic locking failure, the user reloads the record and tries again.
- explanation-02: Pessimistic locking on an account row prevents the balance from going negative due to a race condition.
- explanation-02: Optimistic locking is best for read-heavy applications.
- explanation-03: The network path may be a fast, uncongested link, or it may already be busy with other traffic.
- explanation-05: In a garbage-collected language, the garbage collector usually prevents memory leaks.
- explanation-06: If the real problem is a slow query or a slow downstream service, a cache can hide the pain temporarily while the root cause remains.
- explanation-06: Cache invalidation is one of the harder problems in software design.
- explanation-06: Each write still has to hit the database even when a cache is in place.
- explanation-07: Query latency degradation caused by indexes or working sets no longer fitting in memory is a signal that sharding may be needed.
- explanation-07: Routine PostgreSQL maintenance jobs such as autovacuum taking so long they interfere with normal operations is a signal that sharding may be needed.
- explanation-07: Approaching the practical storage limits of a single disk or cloud instance type is a signal that sharding may be needed.
- explanation-07: Partitioning can fix vacuum and query performance problems without the complexity of sharding across separate database instances.
- explanation-07: The recommended order of cheaper options is vertical scaling, then read replicas, then partitioning, then sharding.
- explanation-07: Monitoring should be set up now for write throughput, query latency, and vacuum time.
- explanation-08: In many services, the bulk of request time goes to database queries or business logic rather than serialization.
- explanation-08: Binary formats typically parse 2 to 10 times faster than JSON.
- explanation-08: Binary formats typically produce payloads 20% to 50% smaller than JSON.
- explanation-08: The 2-10x parsing and 20-50% size figures are rules of thumb from other projects, not predictions for a specific service.
- explanation-08: If serialization is 30% or more of request time, switching to a binary format could yield a noticeable win.
- summarization-04: Clicking the PDF export button again several times causes four "export failed" error banners to appear at once.
- summarization-05: There was a sprint planning meeting on Monday.
- summarization-05: The text lists action items from Monday's sprint planning.
- summarization-07: Staging runs a newer kernel than production.
- summarization-08: The field-mapping finding is based on strong, consistent results across all participants.
- summarization-08: The progress bar finding is classified as tentative.
- summarization-08: The progress bar issue should be treated as a signal worth testing, not a confirmed cause.

### technical-simplified

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 28 | 17 | 0.607 | 23 | 4 |
| code-review-02 | 19 | 11 | 0.579 | 18 | 4 |
| code-review-03 | 24 | 17 | 0.708 | 21 | 6 |
| code-review-04 | 26 | 20 | 0.769 | 23 | 0 |
| code-review-05 | 27 | 21 | 0.778 | 27 | 5 |
| code-review-06 | 38 | 15 | 0.395 | 28 | 9 |
| code-review-07 | 30 | 0 | 0.0 | 9 | 9 |
| debugging-01 | 7 | 7 | 1.0 | 6 | 1 |
| debugging-02 | 19 | 9 | 0.474 | 14 | 2 |
| debugging-03 | 10 | 10 | 1.0 | 9 | 0 |
| debugging-04 | 15 | 10 | 0.667 | 9 | 2 |
| debugging-05 | 17 | 15 | 0.882 | 14 | 0 |
| debugging-07 | 0 | 0 | n/a | 26 | 26 |
| debugging-08 | 28 | 9 | 0.321 | 17 | 4 |
| explanation-01 | 39 | 21 | 0.538 | 20 | 2 |
| explanation-02 | 24 | 21 | 0.875 | 26 | 4 |
| explanation-03 | 35 | 19 | 0.543 | 19 | 3 |
| explanation-04 | 39 | 22 | 0.564 | 23 | 0 |
| explanation-05 | 18 | 16 | 0.889 | 14 | 2 |
| explanation-06 | 21 | 15 | 0.714 | 20 | 6 |
| explanation-07 | 26 | 0 | 0.0 | 5 | 4 |
| summarization-01 | 5 | 5 | 1.0 | 5 | 0 |
| summarization-02 | 12 | 10 | 0.833 | 13 | 3 |
| summarization-03 | 13 | 13 | 1.0 | 13 | 0 |
| summarization-04 | 13 | 12 | 0.923 | 12 | 1 |
| summarization-05 | 9 | 8 | 0.889 | 6 | 0 |

Median fraction: 0.714 over 25 scored pairs.

Median additions: 2.5 over 26 scored pairs.

Lost facts:

- code-review-01: The mutable default argument is a classic Python footgun.
- code-review-01: Duplicate roles aren't prevented.
- code-review-01: Calling the function with `roles=["member"]` explicitly produces `["member", "member"]`.
- code-review-01: An uninformative return value makes it hard for callers to distinguish validation errors from DB errors or misuse and react appropriately.
- code-review-01: The function has no docstring and no type hints.
- code-review-01: Missing type hints is a minor issue.
- code-review-01: Type hints of `name: str`, `roles: list[str] | None`, and a type for `db` would clarify the function's contract.
- code-review-01: A safer rewrite uses `roles=None` as the default and raises `ValueError` when `name` or `db` is missing.
- code-review-01: The safer rewrite copies `roles` with `list(roles)` and appends `"member"` only if it is not already present.
- code-review-01: The rewrite drops the silent failure mode by letting real errors propagate.
- code-review-01: An alternative to letting errors propagate is catching a specific DB exception in order to translate it.
- code-review-02: A non-2xx HTTP response, such as a 404 for a bad `userId`, still resolves rather than rejecting.
- code-review-02: The code will try to parse JSON even for a non-2xx response, whose body may not match the expected shape.
- code-review-02: There is no validation that the response `data` has a `name` property.
- code-review-02: If the API returns an error object instead of a profile, `data.name` could be `undefined` and calling `.toUpperCase()` on it would throw.
- code-review-02: There is no input validation on `userId`.
- code-review-02: Unsanitized/unencoded `userId` could allow injection of unexpected path segments such as `../` or query-like content.
- code-review-02: `encodeURIComponent(userId)` can be used to encode `userId` before interpolating it into the URL.
- code-review-02: The fixed version awaits `fetch` with an encoded `userId`, throws an Error including `res.status` when `!res.ok`, awaits `res.json()`, throws an Error when the response is missing `name`, and returns `data.name.toUpperCase()`.
- code-review-03: psycopg2 uses `%s` as its parameter placeholder.
- code-review-03: pymysql uses `%s` as its parameter placeholder.
- code-review-03: The function does not check that `status` is one of the expected valid values before querying.
- code-review-03: `fetchall` can raise an exception, for example on a bad connection or a database error.
- code-review-03: The function imposes no limit on the number of results returned.
- code-review-03: A broad match could return an unbounded number of rows.
- code-review-03: Pagination or a `LIMIT` clause should be considered to bound the result set.
- code-review-04: Under contention, the counter class will systematically undercount.
- code-review-04: A single assignment is atomic in CPython.
- code-review-04: `reset` by itself will not corrupt the counter's state.
- code-review-04: An example of the reset/increment race is resetting to 0 and then a stale increment writing 1.
- code-review-04: The class has no thread-safety documentation or contract.
- code-review-04: A caller reading the code has no way to know the class is unsafe under concurrent use.
- code-review-05: With an empty BACKUP_DIR, `rm -rf *.tmp` would run in the user's home directory instead of failing.
- code-review-05: Bash has a `nullglob` option affecting unmatched glob behavior.
- code-review-05: When no .log files exist, `ls *.log` prints an error to stderr and returns nothing usable.
- code-review-05: Without `set -u`, the missing-argument problem passes silently.
- code-review-05: `${1:?Usage: ...}` makes the first argument required.
- code-review-05: The `-r` flag is unnecessary for `rm` because the targets are files, not directories.
- code-review-06: Only keys that are actually recursed into get rebuilt as new dicts.
- code-review-06: Resolving the `None`-means-delete ambiguity requires a sentinel such as a `DELETE` marker if both behaviors are needed.
- code-review-06: `merged.pop(key, None)` silently does nothing if the key is not present in `base`.
- code-review-06: Silently no-oping on a missing key can hide a typo, such as a misspelled key intended to delete something.
- code-review-06: If `base[key]` is a dict and `override[key]` is not a dict, the `elif` branch fails and control falls to the `else` branch.
- code-review-06: In that case the entire nested dict is replaced by the scalar value.
- code-review-06: No validation or error is raised for either type-mismatch case.
- code-review-06: The type-mismatch behavior could mask a configuration mistake.
- code-review-06: Recursion depth follows the depth of `override`'s nested dicts.
- code-review-06: There is no depth limit on the recursion.
- code-review-06: Deeply nested or self-referential structures could cause a `RecursionError` or an infinite loop if a dict contains itself.
- code-review-06: Self-referential structures are unlikely for JSON-like config but possible if `base` or `override` are constructed programmatically.
- code-review-06: Only `dict` receives special handling in the merge.
- code-review-06: Some config systems expect list concatenation or index-wise merging.
- code-review-06: There is no check that keys are hashable or strings.
- code-review-06: `isinstance(merged[key], dict)` also matches dict subclasses.
- code-review-06: Recursing into an `OrderedDict` or custom dict subclass via `merge_settings` returns a plain `dict`, losing the subclass type.
- code-review-06: Using `None` as a delete sentinel is a common pattern in config-merge libraries.
- code-review-06: Ansible and Kubernetes strategic merge patches use conventions similar to `None`-as-delete.
- code-review-06: The shallow-copy aliasing issue and the silent type-mismatch overwrite are almost certainly bugs or oversights.
- code-review-06: Those two issues tend to pass testing and later cause hard-to-trace mutation bugs or config-clobbering incidents in production.
- code-review-06: Issues #1 and #4 are the highest-priority items to write tests around and confirm intent for.
- code-review-06: Issues #1 and #4 are the ones most likely to fail silently.
- code-review-07: If every retry attempt hits a 429 or 5xx and the loop runs out, there is no return statement after the for loop.
- code-review-07: When retries are exhausted, the function returns undefined.
- code-review-07: Every other failure path in the function explicitly returns null.
- code-review-07: The function has three different signals for failure: a thrown error that never happens, null, and undefined.
- code-review-07: The inconsistency in failure signals indicates the retry-exhaustion path was never tested.
- code-review-07: The code accesses err.status, which assumes every thrown error is an HTTP-style error object.
- code-review-07: A TypeError, a network-level exception, or a bug inside fn has no .status property.
- code-review-07: When err.status is undefined, both the comparison to 429 and the check for >= 500 evaluate to false.
- code-review-07: Non-HTTP errors fall through to return null.
- code-review-07: A real programming error is silently converted into a null result.
- code-review-07: Swallowing non-HTTP errors as null is the most dangerous issue in the code, especially with callers that cannot be audited.
- code-review-07: Only the 429 branch sleeps before retrying.
- code-review-07: The err.status >= 500 branch calls continue immediately with no delay.
- code-review-07: Retrying server errors with zero delay defeats the purpose of backoff and could contribute to a thundering-herd effect.
- code-review-07: The original error and stack are never logged or attached anywhere.
- code-review-07: A caller cannot distinguish a legitimate null return value from a failure after retries.
- code-review-07: Discarding errors without a trace can cause silent data corruption downstream in a shared library with unknown callers.
- code-review-07: The delay is computed as 1000 * i with i starting at 0, so the first retry delay is 0.
- code-review-07: After the first retry, delays jump to 1 second, then 2 seconds.
- code-review-07: The backoff is linear rather than exponential and includes no jitter.
- code-review-07: Most retry helpers use exponential backoff to avoid synchronized retry storms across clients.
- code-review-07: With attempts = 3, the code performs 3 total tries rather than 3 retries after an initial call.
- code-review-07: The attempts semantics are not a bug.
- code-review-07: Returning null instead of throwing on non-retryable errors is a fail-soft contract.
- code-review-07: A fail-soft contract is plausible for an old internal helper whose callers expect a fallback value rather than a thrown exception.
- code-review-07: Only 429 receives backoff and retry, while other 4xx errors fail immediately.
- code-review-07: 429 means slow down, other 4xx are client errors that are not retryable, and 5xx may be transient and worth retrying.
- code-review-07: The error categorization appears intentional even though the missing 5xx delay looks like an oversight.
- code-review-07: The riskiest problem in the code is the error-handling contract rather than a syntax bug.
- code-review-07: Changing the undefined case or making the function throw would be a breaking change if callers currently check === null to detect failure.
- debugging-02: Class bodies are always in strict mode.
- debugging-02: Strict mode propagates to functions nested inside strict-mode code.
- debugging-02: A regular `function () {...}` passed to `setInterval` from inside a class method has `this === undefined` when called.
- debugging-02: Accessing `this.seconds` when `this` is `undefined` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: Seeing `NaN` instead of a thrown error indicates the code is running in a non-strict/sloppy context.
- debugging-02: Running code directly in a browser `<script>` without `"use strict"` is an example of a non-strict/sloppy context.
- debugging-02: Some transpilation does not preserve strict mode, producing a sloppy-mode context.
- debugging-02: Calling `.bind(this)` on the callback function is an alternative fix.
- debugging-02: Storing `const self = this;` before `setInterval` and using `self` inside the callback is an alternative fix.
- debugging-02: The arrow function is the cleanest modern approach among these fixes.
- debugging-04: The non-ASCII byte occurs at byte offset 512 in the file.
- debugging-04: The ASCII codec rejects any byte greater than or equal to 0x80.
- debugging-04: Encoding can be detected at runtime with libraries such as charset-normalizer or chardet.
- debugging-04: Detecting the encoding is preferable to hardcoding one when the encoding is not known ahead of time.
- debugging-04: The errors="surrogateescape" option preserves byte fidelity.
- debugging-05: The same test running twice can also cause the extra `"post"` entries, for example via test discovery, parametrization, or fixtures.
- debugging-05: In the fixed code, `make_post` is defined as `def make_post(title, tags=None)` and sets `tags = list(DEFAULT_TAGS)` when `tags is None`.
- debugging-08: Campaign products can have larger payloads, more images and variants, and richer JSON than normal products.
- debugging-08: The count-bounded-cache explanation fits all four reported observations.
- debugging-08: Cache entries persist until they are evicted, so cache-driven memory growth survives quiet nights.
- debugging-08: Any traffic populates the cache, so cache-driven growth occurs even without webhooks.
- debugging-08: Guava and Caffeine caches offer a `maximumSize` setting and a `maximumWeight` setting.
- debugging-08: Long-lived maps used for deduplication, idempotency keys, rate limiting, or session and request tracking are a classic source of leaks when their TTL cleanup is absent, broken, or slow.
- debugging-08: Such leaky maps are typically keyed by request ID, order ID, webhook event ID, or correlation ID.
- debugging-08: Dynamically generated classes from serialization libraries, proxies, or template engines leak metaspace rather than heap.
- debugging-08: More campaign SKUs and variants can produce more dynamically generated types.
- debugging-08: Classes are not unloaded until their classloader is garbage collected.
- debugging-08: Application classloaders often are never garbage collected.
- debugging-08: `jstat -gc` or an APM memory breakdown can distinguish heap growth from non-heap/metaspace growth.
- debugging-08: Off-heap leaks are consistent with growth that survives quiet nights and correlates with traffic volume.
- debugging-08: NativeMemoryTracking, `pmap`, and `smaps` diffs can be used to investigate native memory growth.
- debugging-08: The cache-bound hypothesis is the only one of the four consistent with all four clues without positing an additional leak.
- debugging-08: Logging the cache entry-size distribution is a cheap check.
- debugging-08: Switching the cache to weight-based eviction would be a one-line fix.
- debugging-08: The canary-still-grows observation is the strongest evidence that something grows independently of the cache.
- debugging-08: A single `jmap -histo:live` or heap dump from an instance near end-of-week, compared against one taken right after restart, would likely identify the top suspect within minutes.
- explanation-01: An array slot cannot hold two values at once.
- explanation-01: The collection in a chained slot is usually a linked list, and sometimes a small array or tree.
- explanation-01: The rule for finding another open slot in open addressing is called a probe sequence.
- explanation-01: Linear probing tries the next index, then the next, and so on.
- explanation-01: Quadratic probing tries indices at increasing squared steps.
- explanation-01: Double hashing uses a second hash function to decide the step size.
- explanation-01: Chaining has worse cache performance because linked list nodes are scattered in memory.
- explanation-01: Open addressing has better cache performance because its data is contiguous and cache-friendly.
- explanation-01: Deletion in chaining is simple because the node is just removed from the list.
- explanation-01: Deletion in open addressing is trickier because emptying a slot breaks the probe chain for other keys.
- explanation-01: Deletion in open addressing usually needs tombstone markers.
- explanation-01: Chaining eventually needs resizing, but less urgently than open addressing.
- explanation-01: Open addressing needs resizing sooner and must be kept well below full, often under a 70% load factor.
- explanation-01: Open addressing is faster in practice due to better cache locality when memory is tight and the load factor is kept low.
- explanation-01: Deletion and resizing are more delicate to implement correctly in open addressing.
- explanation-01: Java converts long chains to trees for performance.
- explanation-01: Python's dict uses open addressing.
- explanation-01: Many high-performance C++ hash maps use open addressing.
- explanation-02: Optimistic locking fits for long-lived transactions or when there is user think time between read and write, such as editing a form in a browser.
- explanation-02: Holding a database lock during user think time would be wasteful.
- explanation-02: As a rule of thumb, use optimistic locking for low-contention scenarios or when there is a gap between read and write that a lock shouldn't span, such as multi-step user edits and web forms.
- explanation-03: Dropped packets cause wasted bandwidth and retransmissions.
- explanation-03: Congestion collapse is when a congested network becomes even more congested because senders keep retransmitting lost data.
- explanation-03: Historically the initial cwnd was 1 segment.
- explanation-03: The initial cwnd is now typically 2-10 segments per RFC 6928.
- explanation-03: For every ACK received confirming successful delivery of a segment, the sender increases cwnd.
- explanation-03: During slow start, cwnd grows by roughly one segment per ACK.
- explanation-03: The name 'slow start' is misleading.
- explanation-03: Slow start is called 'slow' only relative to the older approach of immediately sending as much as the receiver's window allowed.
- explanation-03: The exponential increase is a deliberate trade-off.
- explanation-03: Exponential growth lets a connection reach a reasonable sending rate in a few RTTs, on the order of log base 2 of the target window.
- explanation-03: Reaching a reasonable sending rate quickly matters a lot for short connections such as most web requests.
- explanation-03: When packet loss is detected, cwnd is cut back significantly.
- explanation-03: ssthresh is often set from a previous congestion event.
- explanation-03: When cwnd reaches ssthresh, TCP switches to the linear growth of congestion avoidance.
- explanation-03: The philosophy of slow start is to start conservatively, probe for available bandwidth, and back off sharply when trouble is detected.
- explanation-03: This congestion control philosophy is why the internet has remained stable even as usage grew enormously.
- explanation-04: A process has its own memory address space, file descriptors, and OS-level resources.
- explanation-04: Each thread has its own stack and register/instruction pointer state.
- explanation-04: Thread communication requires careful synchronization, such as locks and mutexes, to avoid race conditions.
- explanation-04: Processes communicate via IPC mechanisms such as pipes, sockets, and shared memory, which is slower than thread communication.
- explanation-04: A crash such as a segfault in one thread can take down the whole process.
- explanation-04: Threads provide parallelism with shared state and need synchronization.
- explanation-04: Multiple processes bypass the GIL because each process has its own interpreter and GIL.
- explanation-04: Browsers run tabs as separate processes.
- explanation-04: Nginx and Apache use worker processes.
- explanation-04: When a server uses worker processes, one worker dying does not kill the server.
- explanation-04: The OS lets you set per-process limits on memory, CPU, and file descriptors via cgroups and ulimits.
- explanation-04: Per-process resource limits are hard or impossible to apply to a single thread within a shared process.
- explanation-04: Separate processes make it straightforward to restart, upgrade, or scale components independently.
- explanation-04: Microservices and worker pools are examples of components with independent lifecycles that can be killed and respawned.
- explanation-04: GIL and shared-state concerns matter less for I/O-bound tasks.
- explanation-04: Processes are preferable when you need true CPU parallelism, fault or security isolation, or independent resource control.
- explanation-04: The overhead of separate memory spaces and IPC is worth it for the safety and parallelism guarantees processes provide.
- explanation-05: Global emitters and DOM elements are examples of long-lived objects.
- explanation-05: Caches without a TTL, without a size limit, or using strong keys instead of weak references are unbounded.
- explanation-06: Caching only helps if the problem is repeated reads of the same data hitting a slow database.
- explanation-06: A cache does not help when slowness comes from lock contention caused by writes.
- explanation-06: A cache does not help when slowness comes from an N+1 query problem.
- explanation-06: Adding a cache means maintaining two systems instead of one.
- explanation-06: Timing the API end-to-end and breaking it into phases (network, app logic, DB query) reveals where the time actually goes.
- explanation-06: Slow query logs and DB metrics show whether the database is CPU or IO bound or whether the app is slow elsewhere.
- explanation-07: 200 GB is well within what a single well-tuned Postgres instance can handle.
- explanation-07: Sharding adds operational complexity.
- explanation-07: Cross-shard joins and transactions are a source of sharding complexity.
- explanation-07: Rebalancing is a source of sharding complexity.
- explanation-07: Routing logic is a source of sharding complexity.
- explanation-07: Sharding's complexity is hard to justify without a concrete bottleneck.
- explanation-07: The product team cannot say how much the data will grow.
- explanation-07: The product team's inability to estimate growth is the real problem.
- explanation-07: A growth rate of about 10% in GB is fine for years.
- explanation-07: A growth rate of 10x per year changes the calculus.
- explanation-07: Sharding solves horizontal scaling, not disk cost.
- explanation-07: A bigger disk or read replicas solve storage and read pressure much more cheaply than sharding.
- explanation-07: A natural shard key such as tenant ID or region can keep queries within a single shard.
- explanation-07: If most queries need cross-shard joins or aggregations, sharding will hurt more than help.
- explanation-07: Cheaper alternatives to sharding include indexing, partitioning within one instance, read replicas, connection pooling, archiving cold data, and vertical scaling.
- explanation-07: Postgres on modern hardware comfortably handles multi-terabyte databases when those cheaper measures are in place.
- explanation-07: Sharding now locks in a shard key before access patterns are understood.
- explanation-07: If the shard key choice is wrong, resharding later is a major migration.
- explanation-07: Sharding now immediately introduces distributed-transaction and cross-shard-query complexity.
- explanation-07: That complexity slows every feature that touches multiple entities.
- explanation-07: If growth turns out to be fast and unpredictable, waiting means migrating under pressure rather than on your own timeline.
- explanation-07: Waiting leaves less room to test the shard key choice.
- explanation-07: Partitioning can be time-based or tenant-based and still run on a single instance.
- explanation-07: Partitioning and read replicas are reversible.
- explanation-07: Partitioning and read replicas buy significant headroom.
- explanation-07: Tracking actual growth for a few months makes the shard-key decision evidence-based rather than guessed.
- summarization-02: The staging pool size of 5 was intended to be small.
- summarization-02: The copied config exhausted the database connection pool.
- summarization-04: The issue was reproduced by a second user on a different machine.
- summarization-05: Ada is assigned to check with the mobile team lead about whether the mobile team has been informed of the API deprecation.

Added facts (styled only):

- code-review-01: The function has six problems.
- code-review-01: The function does not check that `roles` is a list.
- code-review-01: The corrected version builds `updated_roles` as `roles + ["member"]` instead of appending to the caller's list.
- code-review-01: The corrected version catches `Exception` and logs the failure with `logging.error` before returning `False`.
- code-review-02: The `async` keyword has no effect on the function.
- code-review-02: The return value is wrong for callers.
- code-review-02: Even after the `await` issue is fixed, a caller must use `await loadProfile(userId)` to get the name.
- code-review-02: The current code hides the need for callers to await the function.
- code-review-03: `SELECT *` returns all columns, including columns the caller does not need.
- code-review-03: `SELECT *` can leak sensitive fields.
- code-review-03: The function does not check whether `customer_name` and `status` are empty or `None`.
- code-review-03: Missing input validation can produce a wrong query or an error.
- code-review-03: The function signature has no type hints for `cursor`, `customer_name`, or `status`.
- code-review-03: The function signature has no return type annotation.
- code-review-05: Unquoted $1 can break with filenames containing spaces or special characters.
- code-review-05: The variables should be written as "$1" and "$BACKUP_DIR".
- code-review-05: The unchecked cd is the script's main safety problem.
- code-review-05: The script does not return to the original directory after the cd.
- code-review-05: The script does not save and restore the starting directory.
- code-review-06: The function has several behaviors that look intentional but are undocumented.
- code-review-06: When merged[key] is a dict but override[key] is not a dict, the code still calls merge_settings(merged[key], value).
- code-review-06: Inside that recursive call, value.items() fails because value is not a dict.
- code-review-06: The function raises an AttributeError in the type-mismatch case.
- code-review-06: merge_settings({"a": {"x": 1}}, {"a": 5}) crashes.
- code-review-06: The type-mismatch crash looks like a bug rather than a deliberate design.
- code-review-06: The None-deletion tradeoff needs a comment.
- code-review-06: The function has no docstring.
- code-review-06: Tests should be added for the None-deletion case and the type-mismatch crash before changing the function.
- code-review-07: The text is a tool invocation of a tool named "bash".
- code-review-07: The tool call has a "command" field and a "description" field.
- code-review-07: The command runs `cat` on the file /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-pi8m0gil/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-dwnsot2k/memory/MEMORY.md
- code-review-07: The command redirects standard error to /dev/null with `2>/dev/null`.
- code-review-07: The command falls back to `echo "NO_MEMORY"` if the `cat` fails, using the `||` operator.
- code-review-07: The description of the command is "Check memory index".
- code-review-07: The targeted file is named MEMORY.md.
- code-review-07: The targeted file resides in a directory named `memory`.
- code-review-07: The memory directory path is under a `projects` directory keyed by an encoded project path.
- debugging-01: The key name that needs fixing is on line 4.
- debugging-02: Inside a normal function, `this` refers to the global object.
- debugging-02: `this.seconds += 1` therefore evaluates as `undefined + 1`.
- debugging-04: The byte `0xc3` is often the first byte of a multi-byte UTF-8 character.
- debugging-04: Passing `errors="replace"` to `open` replaces invalid bytes with a placeholder character.
- debugging-07: A race condition between the event write and the digest read is a plausible cause of the failure.
- debugging-07: The API call that seeds an event can return before the event is fully visible to the digest query.
- debugging-07: An async write can cause an event to not be visible to the digest query immediately.
- debugging-07: A queue can cause an event to not be visible to the digest query immediately.
- debugging-07: Database replication lag can cause an event to not be visible to the digest query immediately.
- debugging-07: The event visibility delay grows under CI load.
- debugging-07: Shared state between parallel workers is a plausible cause of the failure.
- debugging-07: If workers share a database, a test user, or a queue, one worker's event can leak into another test.
- debugging-07: If workers share a database, a test user, or a queue, a row can get overwritten.
- debugging-07: A serial run never exposes the shared-state issue.
- debugging-07: A time-window cutoff in the digest logic is a plausible cause of the failure.
- debugging-07: If the digest filters events by a timestamp boundary, a slow CI run can push an event just outside the window.
- debugging-07: A result limit in the digest API is a plausible cause of the failure.
- debugging-07: A page size or row limit can drop the third event under load even when all three events exist.
- debugging-07: Running tests/test_notifications.py with 4 workers in a loop, for example 100 times, raises the failure rate and gives a faster reproduction.
- debugging-07: A pytest hook can be added to write event IDs, timestamps, and the worker ID to a file when the test fails.
- debugging-07: The file written by the pytest hook can be uploaded as a CI artifact.
- debugging-07: The test can be run many times with the -p no:xdist flag.
- debugging-07: If the failure stops when running with -p no:xdist, the cause is parallelism rather than timing alone.
- debugging-07: A poll with retry can be added before the assertion.
- debugging-07: If adding a retry fixes the failure, the digest reads the data before the write is visible.
- debugging-07: The test setup code can be read for fixtures shared across workers, such as a shared user ID or database session.
- debugging-07: The digest code can be read for a time-based cutoff or a page limit that a slow parallel run can trigger.
- debugging-07: The recommended starting steps are the artifact hook and the parallel-vs-serial comparison.
- debugging-07: The artifact hook and the parallel-vs-serial comparison indicate whether the root cause is a race condition or shared state.
- debugging-07: The artifact hook and the parallel-vs-serial comparison provide data for the next round of investigation.
- debugging-08: A leak tied to request handling, such as webhooks or order creation, is the most likely cause.
- debugging-08: The known cache bound has not changed in a year.
- debugging-08: Because the cache bound has not changed in a year, the known cache is a less likely direct cause.
- debugging-08: Metrics and tracing libraries can accumulate a growing backlog.
- explanation-01: Under chaining, the list can grow without a size limit.
- explanation-01: Chaining works well when the load factor is high and few keys have hashes.
- explanation-02: In optimistic locking, when a write fails the application must retry.
- explanation-02: In the example, a product table has a column named `version`.
- explanation-02: In the example, editing a product produces an update statement that includes `WHERE id = 5 AND version = 3`.
- explanation-02: If the row still has `version = 3`, the update succeeds and the version becomes 4.
- explanation-03: In the 1980s, many senders sent data at full speed at the same time.
- explanation-03: In the 1980s, routers dropped packets as a result of simultaneous full-speed sending.
- explanation-03: Network throughput dropped instead of increasing.
- explanation-05: A memory leak can slow a program down.
- explanation-05: A memory leak can crash a program.
- explanation-06: Slowness can come from too many database connections.
- explanation-06: Adding a cache now can hide the real problem.
- explanation-06: The API can stay slow and you will not know why.
- explanation-06: The second step is to measure the read-to-write mix and find how often the same data is read.
- explanation-06: The third step is to check the database for slow queries and missing indexes.
- explanation-06: A cache helps when the data can be a little old without harm.
- explanation-07: The memory directory should be read first.
- explanation-07: The purpose of reading the memory directory is to check for relevant project context.
- explanation-07: The speaker will check for relevant stored context before proceeding.
- explanation-07: A read operation is being performed.
- summarization-02: The on-call engineer was paged at 09:21.
- summarization-02: The rollback finished at 09:48.
- summarization-02: Error rates returned to normal after the rollback finished.
- summarization-04: The app then shows four identical "export failed" error banners.

## Hedging survival

The judge lists the claims that the unstyled answer presents with uncertainty, then judges each claim in the styled answer: hedged (the uncertainty survives in some form), certain (the claim survives but reads as a fact — the failure this check targets), or absent (the claim is gone, a completeness loss). Survival is hedged / (hedged + certain). The claims that became certain appear verbatim below the table.

### actionable-clarity

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 0 | 2 | n/a |
| code-review-02 | 3 | 3 | 0 | 0 | 1.0 |
| code-review-03 | 1 | 1 | 0 | 0 | 1.0 |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 3 | 0 | 1 | 2 | 0.0 |
| code-review-06 | 11 | 6 | 2 | 3 | 0.75 |
| code-review-07 | 10 | 5 | 0 | 5 | 1.0 |
| code-review-08 | 5 | 3 | 2 | 0 | 0.6 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 2 | 0 | 0 | 2 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 3 | 0 | 0 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 0 | 0 | 0 | 0 | n/a |
| debugging-07 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 10 | 3 | 1 | 6 | 0.75 |
| explanation-01 | 0 | 0 | 0 | 0 | n/a |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 6 | 2 | 2 | 2 | 0.5 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 3 | 1 | 2 | 0 | 0.333 |
| explanation-07 | 0 | 0 | 0 | 0 | n/a |
| explanation-08 | 4 | 2 | 1 | 1 | 0.667 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 1 | 1 | 0 | 0 | 1.0 |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-07 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 75 over 32 judged pairs: 41 hedged, 11 certain, 23 absent.

Median survival: 1.0 over 15 scored pairs.

Claims that became certain:

- code-review-05: If `cd $BACKUP_DIR` fails and the script keeps going, `rm -rf *.tmp` executing in whatever the current directory happens to be could potentially delete unintended files.
- code-review-06: Passing a non-dict `override` will fail with a possibly confusing `AttributeError: 'X' object has no attribute 'items'` rather than a clear error.
- code-review-06: Issues #1 and #4 are the ones most likely to bite silently, so they should be the highest-priority items to write tests around and confirm intent for.
- code-review-08: The listed bugs/risks are likely unintentional.
- code-review-08: Between listdir(), getmtime(), and remove(), another process could delete the file first, raising FileNotFoundError and aborting the run.
- debugging-08: A single `jmap -histo:live` or heap dump from an instance near end-of-week, compared to one right after restart, will likely make the top suspect obvious in minutes.
- explanation-03: If TCP started by blasting out data at full speed, it could easily overwhelm a router or link that's slower than expected, causing packets to be dropped.
- explanation-03: Roughly, cwnd grows by one segment per ACK received.
- explanation-06: In a read-heavy workload (e.g., 90% reads of the same records), caching can help a lot, since you avoid recomputing/refetching the same thing repeatedly.
- explanation-06: In a write-heavy or unique-per-request read workload, cache invalidation overhead may add complexity for little benefit.
- explanation-08: Most languages let you wrap JSON encode/decode in a timer or use a profiler to measure its share of request latency.

### clarity-flow

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 2 | 0 | 0.0 |
| code-review-02 | 3 | 0 | 1 | 2 | 0.0 |
| code-review-03 | 1 | 0 | 0 | 1 | n/a |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 3 | 1 | 2 | 0 | 0.333 |
| code-review-06 | 11 | 3 | 2 | 6 | 0.6 |
| code-review-07 | 10 | 6 | 0 | 4 | 1.0 |
| code-review-08 | 5 | 4 | 1 | 0 | 0.8 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 2 | 0 | 0 | 2 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 2 | 1 | 0 | 0.667 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 0 | 0 | 0 | 0 | n/a |
| debugging-07 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 10 | 3 | 1 | 6 | 0.75 |
| explanation-01 | 0 | 0 | 0 | 0 | n/a |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 6 | 3 | 2 | 1 | 0.6 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 3 | 1 | 2 | 0 | 0.333 |
| explanation-07 | 0 | 0 | 0 | 0 | n/a |
| explanation-08 | 4 | 2 | 1 | 1 | 0.667 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 1 | 0 | 0 | 1 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 3 | 0 | 1 | 1.0 |
| summarization-07 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 75 over 32 judged pairs: 35 hedged, 15 certain, 25 absent.

Median survival: 0.667 over 14 scored pairs.

Claims that became certain:

- code-review-01: The problems are listed roughly in order of severity.
- code-review-01: Mutating the caller's original list as a side effect via `.append("member")` is surprising and can cause bugs elsewhere in the caller's code.
- code-review-02: A non-2xx response will still resolve and be parsed as JSON, potentially with a body that doesn't match the expected shape.
- code-review-05: If `cd $BACKUP_DIR` fails and the script keeps going, `rm -rf *.tmp` executing in whatever the current directory happens to be could potentially delete unintended files.
- code-review-05: With `for f in $(ls *.log)` and no `.log` files present, the loop body may still run once with a literal `*.log` string as `$f`, causing `gzip` to fail with a confusing error.
- code-review-06: Passing a non-dict `override` will fail with a possibly confusing `AttributeError: 'X' object has no attribute 'items'` rather than a clear error.
- code-review-06: The shallow-copy aliasing issue (#1) and the silent type-mismatch overwrite (#4) are almost certainly bugs/oversights.
- code-review-08: Between listdir(), getmtime(), and remove(), another process could delete the file first, raising FileNotFoundError and aborting the run.
- debugging-04: An encoding that actually matches the file's contents is typically UTF-8.
- debugging-08: A single `jmap -histo:live` or heap dump from an instance near end-of-week, compared to one right after restart, will likely make the top suspect obvious in minutes.
- explanation-03: If TCP started by blasting out data at full speed, it could easily overwhelm a router or link that's slower than expected, causing packets to be dropped.
- explanation-03: Before congestion control existed, dropped packets could snowball into "congestion collapse," where a congested network gets even more congested because everyone keeps retransmitting lost data.
- explanation-06: In a read-heavy workload (e.g., 90% reads of the same records), caching can help a lot, since you avoid recomputing/refetching the same thing repeatedly.
- explanation-06: In a write-heavy or unique-per-request read workload, cache invalidation overhead may add complexity for little benefit.
- explanation-08: Binary formats (protobuf, msgpack, etc.) typically help in two ways: smaller payload size and faster parse/serialize.

### classic-concise

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 1 | 0 | 1 | 1.0 |
| code-review-02 | 3 | 0 | 1 | 2 | 0.0 |
| code-review-03 | 1 | 0 | 0 | 1 | n/a |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 3 | 0 | 3 | 0 | 0.0 |
| code-review-06 | 11 | 4 | 2 | 5 | 0.667 |
| code-review-07 | 10 | 4 | 1 | 5 | 0.8 |
| code-review-08 | 5 | 4 | 1 | 0 | 0.8 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 2 | 0 | 0 | 2 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 1 | 1 | 1 | 0.5 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 0 | 0 | 0 | 0 | n/a |
| debugging-07 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 10 | 4 | 1 | 5 | 0.8 |
| explanation-01 | 0 | 0 | 0 | 0 | n/a |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 6 | 3 | 2 | 1 | 0.6 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 3 | 1 | 2 | 0 | 0.333 |
| explanation-07 | 0 | 0 | 0 | 0 | n/a |
| explanation-08 | 4 | 3 | 1 | 0 | 0.75 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 1 | 0 | 0 | 1 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-07 | 4 | 3 | 1 | 0 | 0.75 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 75 over 32 judged pairs: 35 hedged, 16 certain, 24 absent.

Median survival: 0.75 over 14 scored pairs.

Claims that became certain:

- code-review-02: A non-2xx response will still resolve and be parsed as JSON, potentially with a body that doesn't match the expected shape.
- code-review-05: If `cd $BACKUP_DIR` fails and the script keeps going, `rm -rf *.tmp` executing in whatever the current directory happens to be could potentially delete unintended files.
- code-review-05: If no `.tmp` files exist and the shell doesn't glob-expand, `rm -rf` gets a literal `*.tmp` pattern and typically just errors out harmlessly in POSIX sh.
- code-review-05: With `for f in $(ls *.log)` and no `.log` files present, the loop body may still run once with a literal `*.log` string as `$f`, causing `gzip` to fail with a confusing error.
- code-review-06: Passing a non-dict `override` will fail with a possibly confusing `AttributeError: 'X' object has no attribute 'items'` rather than a clear error.
- code-review-06: The shallow-copy aliasing issue (#1) and the silent type-mismatch overwrite (#4) are almost certainly bugs/oversights.
- code-review-07: If the 5xx branch is meant to be 'retry on server errors,' hammering a struggling server with zero delay could contribute to a thundering-herd effect.
- code-review-08: Between listdir(), getmtime(), and remove(), another process could delete the file first, raising FileNotFoundError and aborting the run.
- debugging-04: An encoding that actually matches the file's contents is typically UTF-8.
- debugging-08: A single `jmap -histo:live` or heap dump from an instance near end-of-week, compared to one right after restart, will likely make the top suspect obvious in minutes.
- explanation-03: If TCP started by blasting out data at full speed, it could easily overwhelm a router or link that's slower than expected, causing packets to be dropped.
- explanation-03: Roughly, cwnd grows by one segment per ACK received.
- explanation-06: In a read-heavy workload (e.g., 90% reads of the same records), caching can help a lot, since you avoid recomputing/refetching the same thing repeatedly.
- explanation-06: In a write-heavy or unique-per-request read workload, cache invalidation overhead may add complexity for little benefit.
- explanation-08: Most languages let you wrap JSON encode/decode in a timer or use a profiler to measure its share of request latency.
- summarization-07: A batcher bug can't yet be ruled out as the cause of the worker crash.

### concise

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 0 | 2 | n/a |
| code-review-02 | 3 | 0 | 1 | 2 | 0.0 |
| code-review-03 | 1 | 1 | 0 | 0 | 1.0 |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 3 | 1 | 2 | 0 | 0.333 |
| code-review-06 | 11 | 4 | 3 | 4 | 0.571 |
| code-review-07 | 10 | 6 | 0 | 4 | 1.0 |
| code-review-08 | 5 | 3 | 2 | 0 | 0.6 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 2 | 0 | 0 | 2 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 2 | 0 | 1 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 0 | 0 | 0 | 0 | n/a |
| debugging-07 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 10 | 4 | 0 | 6 | 1.0 |
| explanation-01 | 0 | 0 | 0 | 0 | n/a |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 6 | 3 | 2 | 1 | 0.6 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 3 | 2 | 1 | 0 | 0.667 |
| explanation-07 | 0 | 0 | 0 | 0 | n/a |
| explanation-08 | 4 | 0 | 4 | 0 | 0.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 1 | 0 | 0 | 1 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-07 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 75 over 32 judged pairs: 37 hedged, 15 certain, 23 absent.

Median survival: 0.834 over 14 scored pairs.

Claims that became certain:

- code-review-02: A non-2xx response will still resolve and be parsed as JSON, potentially with a body that doesn't match the expected shape.
- code-review-05: If `cd $BACKUP_DIR` fails and the script keeps going, `rm -rf *.tmp` executing in whatever the current directory happens to be could potentially delete unintended files.
- code-review-05: With `for f in $(ls *.log)` and no `.log` files present, the loop body may still run once with a literal `*.log` string as `$f`, causing `gzip` to fail with a confusing error.
- code-review-06: Deeply nested or self-referential structures — unlikely for JSON-like config, but possible if `base`/`override` are constructed programmatically — could cause a `RecursionError` or infinite loop if a dict contains itself.
- code-review-06: Passing a non-dict `override` will fail with a possibly confusing `AttributeError: 'X' object has no attribute 'items'` rather than a clear error.
- code-review-06: Issues #1 and #4 are the ones most likely to bite silently, so they should be the highest-priority items to write tests around and confirm intent for.
- code-review-08: The listed bugs/risks are likely unintentional.
- code-review-08: Between listdir(), getmtime(), and remove(), another process could delete the file first, raising FileNotFoundError and aborting the run.
- explanation-03: Roughly, cwnd grows by one segment per ACK received.
- explanation-03: ssthresh is often set from a previous congestion event.
- explanation-06: In a write-heavy or unique-per-request read workload, cache invalidation overhead may add complexity for little benefit.
- explanation-08: Binary formats (protobuf, msgpack, etc.) typically help in two ways: smaller payload size and faster parse/serialize.
- explanation-08: If most latency is DB queries, business logic, or network round-trips, even a 5-10x faster serializer might shave off only low single-digit percent of total request time.
- explanation-08: If serialization is a bottleneck (e.g., large payloads, high request rate), switching could be a meaningful win.
- explanation-08: Most languages let you wrap JSON encode/decode in a timer or use a profiler to measure its share of request latency.

### developer-docs

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-02 | 3 | 1 | 0 | 2 | 1.0 |
| code-review-03 | 1 | 1 | 0 | 0 | 1.0 |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 3 | 0 | 3 | 0 | 0.0 |
| code-review-06 | 11 | 7 | 1 | 3 | 0.875 |
| code-review-07 | 10 | 4 | 2 | 4 | 0.667 |
| code-review-08 | 5 | 3 | 1 | 1 | 0.75 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 2 | 0 | 0 | 2 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 2 | 1 | 0 | 0.667 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 0 | 0 | 0 | 0 | n/a |
| debugging-07 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 10 | 4 | 0 | 6 | 1.0 |
| explanation-01 | 0 | 0 | 0 | 0 | n/a |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 6 | 3 | 2 | 1 | 0.6 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 3 | 2 | 1 | 0 | 0.667 |
| explanation-07 | 0 | 0 | 0 | 0 | n/a |
| explanation-08 | 4 | 1 | 1 | 2 | 0.5 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 1 | 1 | 0 | 0 | 1.0 |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-07 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 75 over 32 judged pairs: 40 hedged, 13 certain, 22 absent.

Median survival: 0.812 over 16 scored pairs.

Claims that became certain:

- code-review-01: Mutating the caller's original list as a side effect via `.append("member")` is surprising and can cause bugs elsewhere in the caller's code.
- code-review-05: If `cd $BACKUP_DIR` fails and the script keeps going, `rm -rf *.tmp` executing in whatever the current directory happens to be could potentially delete unintended files.
- code-review-05: If no `.tmp` files exist and the shell doesn't glob-expand, `rm -rf` gets a literal `*.tmp` pattern and typically just errors out harmlessly in POSIX sh.
- code-review-05: With `for f in $(ls *.log)` and no `.log` files present, the loop body may still run once with a literal `*.log` string as `$f`, causing `gzip` to fail with a confusing error.
- code-review-06: Passing a non-dict `override` will fail with a possibly confusing `AttributeError: 'X' object has no attribute 'items'` rather than a clear error.
- code-review-07: The bugs identified (silent undefined on exhausted retries, non-HTTP errors swallowed as null, no backoff on 5xx retries) are almost certainly unintentional.
- code-review-07: If the 5xx branch is meant to be 'retry on server errors,' hammering a struggling server with zero delay could contribute to a thundering-herd effect.
- code-review-08: Between listdir(), getmtime(), and remove(), another process could delete the file first, raising FileNotFoundError and aborting the run.
- debugging-04: For line-counting purposes, UTF-8 with errors="replace" (or "surrogateescape" if byte-fidelity is needed) is usually the pragmatic fix.
- explanation-03: Before congestion control existed, dropped packets could snowball into "congestion collapse," where a congested network gets even more congested because everyone keeps retransmitting lost data.
- explanation-03: Roughly, cwnd grows by one segment per ACK received.
- explanation-06: In a write-heavy or unique-per-request read workload, cache invalidation overhead may add complexity for little benefit.
- explanation-08: If most latency is DB queries, business logic, or network round-trips, even a 5-10x faster serializer might shave off only low single-digit percent of total request time.

### plain-language

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-02 | 3 | 0 | 1 | 2 | 0.0 |
| code-review-03 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 3 | 1 | 1 | 1 | 0.5 |
| code-review-06 | 11 | 0 | 0 | 11 | n/a |
| code-review-07 | 10 | 7 | 0 | 3 | 1.0 |
| code-review-08 | 5 | 4 | 0 | 1 | 1.0 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 2 | 0 | 0 | 2 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 3 | 0 | 0 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 0 | 0 | 0 | 0 | n/a |
| debugging-07 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 10 | 3 | 1 | 6 | 0.75 |
| explanation-01 | 0 | 0 | 0 | 0 | n/a |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 6 | 2 | 1 | 3 | 0.667 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 3 | 1 | 2 | 0 | 0.333 |
| explanation-07 | 0 | 0 | 0 | 0 | n/a |
| explanation-08 | 4 | 2 | 1 | 1 | 0.667 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 1 | 0 | 0 | 1 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-07 | 4 | 4 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 75 over 32 judged pairs: 34 hedged, 9 certain, 32 absent.

Median survival: 0.709 over 14 scored pairs.

Claims that became certain:

- code-review-01: Mutating the caller's original list as a side effect via `.append("member")` is surprising and can cause bugs elsewhere in the caller's code.
- code-review-02: A non-2xx response will still resolve and be parsed as JSON, potentially with a body that doesn't match the expected shape.
- code-review-03: A broad match could return an unbounded number of rows.
- code-review-05: If `cd $BACKUP_DIR` fails and the script keeps going, `rm -rf *.tmp` executing in whatever the current directory happens to be could potentially delete unintended files.
- debugging-08: The fact that the canary still grows without webhooks implies there is probably a baseline leak independent of webhooks, plus an additional webhook-driven contributor.
- explanation-03: cwnd doubles roughly every round-trip time, growing approximately 1 segment, then ~2, then ~4, then ~8, and so on, each RTT.
- explanation-06: In a read-heavy workload (e.g., 90% reads of the same records), caching can help a lot, since you avoid recomputing/refetching the same thing repeatedly.
- explanation-06: In a write-heavy or unique-per-request read workload, cache invalidation overhead may add complexity for little benefit.
- explanation-08: If most latency is DB queries, business logic, or network round-trips, even a 5-10x faster serializer might shave off only low single-digit percent of total request time.

### technical-simplified

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 1 | 0 | 1 | 1.0 |
| code-review-02 | 3 | 0 | 0 | 3 | n/a |
| code-review-03 | 1 | 0 | 0 | 1 | n/a |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 3 | 1 | 2 | 0 | 0.333 |
| code-review-06 | 11 | 4 | 2 | 5 | 0.667 |
| code-review-07 | 10 | 0 | 0 | 10 | n/a |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 2 | 0 | 0 | 2 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 1 | 2 | 0 | 0.333 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-07 | 0 | 0 | 0 | 0 | n/a |
| debugging-08 | 10 | 3 | 1 | 6 | 0.75 |
| explanation-01 | 0 | 0 | 0 | 0 | n/a |
| explanation-02 | 0 | 0 | 0 | 0 | n/a |
| explanation-03 | 6 | 0 | 3 | 3 | 0.0 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 3 | 1 | 2 | 0 | 0.333 |
| explanation-07 | 0 | 0 | 0 | 0 | n/a |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 0 | 0 | 0 | 0 | n/a |
| summarization-04 | 1 | 0 | 0 | 1 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |

Claims: 55 over 26 judged pairs: 11 hedged, 12 certain, 32 absent.

Median survival: 0.333 over 7 scored pairs.

Claims that became certain:

- code-review-05: If no `.tmp` files exist and the shell doesn't glob-expand, `rm -rf` gets a literal `*.tmp` pattern and typically just errors out harmlessly in POSIX sh.
- code-review-05: With `for f in $(ls *.log)` and no `.log` files present, the loop body may still run once with a literal `*.log` string as `$f`, causing `gzip` to fail with a confusing error.
- code-review-06: Passing a non-dict `override` will fail with a possibly confusing `AttributeError: 'X' object has no attribute 'items'` rather than a clear error.
- code-review-06: Issues #1 and #4 are the ones most likely to bite silently, so they should be the highest-priority items to write tests around and confirm intent for.
- debugging-04: An encoding that actually matches the file's contents is typically UTF-8.
- debugging-04: For line-counting purposes, UTF-8 with errors="replace" (or "surrogateescape" if byte-fidelity is needed) is usually the pragmatic fix.
- debugging-08: The fact that the canary still grows without webhooks implies there is probably a baseline leak independent of webhooks, plus an additional webhook-driven contributor.
- explanation-03: If TCP started by blasting out data at full speed, it could easily overwhelm a router or link that's slower than expected, causing packets to be dropped.
- explanation-03: Before congestion control existed, dropped packets could snowball into "congestion collapse," where a congested network gets even more congested because everyone keeps retransmitting lost data.
- explanation-03: cwnd doubles roughly every round-trip time, growing approximately 1 segment, then ~2, then ~4, then ~8, and so on, each RTT.
- explanation-06: In a read-heavy workload (e.g., 90% reads of the same records), caching can help a lot, since you avoid recomputing/refetching the same thing repeatedly.
- explanation-06: In a write-heavy or unique-per-request read workload, cache invalidation overhead may add complexity for little benefit.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 824, measured: 824.
Mean duration: 12234 ms. Mean wall: 28970 ms. Mean startup: 16736 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 824, measured: 824.
Input tokens: 1648 uncached, 1574955 cache write, 1708548 cache read. Output tokens: 823828.
Cache-read share: 0.52.
Cache writes by lifetime: 1574955 at 5 minutes, 0 at 1 hour.

## Warnings

- technical-simplified/explanation-08: the pair failed the gate, excluded
- technical-simplified/code-review-08: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/summarization-07: the pair failed the gate, excluded
- technical-simplified/summarization-08: the pair failed the gate, excluded
- technical-simplified/debugging-06: the pair failed the gate, excluded
