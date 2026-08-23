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

Judge: opus. Judged on 2026-08-22T10:58:54+00:00.

## Completeness (fact survival)

The judge lists the facts of the unstyled answer, then checks each fact against the styled answer. The fraction is the share of the facts that survive. The judge also lists the facts of the styled answer and checks each fact against the unstyled answer: a styled fact that the unstyled answer does not state is an addition. The lost facts and the added facts appear verbatim below the table.

### actionable-clarity

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 26 | 19 | 0.731 | 30 | 7 |
| code-review-02 | 19 | 17 | 0.895 | 26 | 2 |
| code-review-03 | 25 | 15 | 0.6 | 18 | 2 |
| code-review-04 | 14 | 12 | 0.857 | 14 | 2 |
| code-review-05 | 39 | 29 | 0.744 | 41 | 7 |
| code-review-06 | 30 | 22 | 0.733 | 34 | 8 |
| code-review-07 | 23 | 14 | 0.609 | 40 | 13 |
| code-review-08 | 42 | 27 | 0.643 | 21 | 4 |
| debugging-01 | 6 | 6 | 1.0 | 8 | 0 |
| debugging-02 | 14 | 10 | 0.714 | 15 | 0 |
| debugging-03 | 8 | 8 | 1.0 | 11 | 0 |
| debugging-04 | 11 | 8 | 0.727 | 11 | 4 |
| debugging-05 | 16 | 13 | 0.812 | 17 | 3 |
| debugging-06 | 27 | 19 | 0.704 | 28 | 14 |
| debugging-07 | 28 | 14 | 0.5 | 34 | 11 |
| debugging-08 | 40 | 15 | 0.375 | 39 | 26 |
| explanation-01 | 42 | 34 | 0.81 | 26 | 2 |
| explanation-02 | 32 | 25 | 0.781 | 28 | 3 |
| explanation-03 | 30 | 21 | 0.7 | 30 | 6 |
| explanation-04 | 31 | 19 | 0.613 | 31 | 2 |
| explanation-05 | 14 | 13 | 0.929 | 19 | 0 |
| explanation-06 | 17 | 10 | 0.588 | 23 | 2 |
| explanation-07 | 27 | 21 | 0.778 | 31 | 10 |
| explanation-08 | 14 | 8 | 0.571 | 18 | 3 |
| summarization-01 | 6 | 6 | 1.0 | 15 | 9 |
| summarization-02 | 13 | 9 | 0.692 | 13 | 5 |
| summarization-03 | 13 | 13 | 1.0 | 14 | 0 |
| summarization-04 | 13 | 11 | 0.846 | 14 | 2 |
| summarization-05 | 9 | 9 | 1.0 | 14 | 3 |
| summarization-06 | 15 | 15 | 1.0 | 12 | 0 |
| summarization-07 | 16 | 13 | 0.812 | 16 | 3 |
| summarization-08 | 25 | 21 | 0.84 | 22 | 7 |

Median fraction: 0.761 over 32 scored pairs.

Median additions: 3.0 over 32 scored pairs.

Lost facts:

- code-review-01: Swallowing all exceptions makes the mutable-default and missing-`db` bugs invisible.
- code-review-01: The function does not check whether "member" is already present in `roles`, which can produce duplicate entries.
- code-review-01: The suggested fix builds a new list with `[*roles, "member"]` instead of appending in place.
- code-review-01: The suggested fix makes `db` a required positional parameter with no default.
- code-review-01: The suggested fix catches `DatabaseError` rather than using a bare `except:`.
- code-review-01: The suggested fix calls `logger.exception` before returning `False`.
- code-review-01: `DatabaseError` is what is actually expected to be raised from a database call.
- code-review-02: The proposed fixed version throws an Error when `data.name` is missing.
- code-review-02: Callers of the fixed function should wrap calls in `try/catch` to handle thrown errors.
- code-review-03: Any input containing a single quote breaks out of the SQL string literal.
- code-review-03: `SELECT *` forces callers to guess column order and meaning from the return value instead of getting named fields.
- code-review-03: Invalid input types will produce a confusing SQL error or unexpected query behavior.
- code-review-03: `cursor.execute` and `fetchall` can raise exceptions, for example from a bad connection or an invalid status value.
- code-review-03: The code calls `fetchall()` on unbounded results.
- code-review-03: If the `orders` table is large, `fetchall()` loads everything into memory at once.
- code-review-03: There is no pagination or limit on the query results.
- code-review-03: The function has no docstring and no type hints.
- code-review-03: The function signature does not indicate the expected types of `cursor`, `customer_name`, or `status`, nor the return type.
- code-review-03: The missing docstring and type hints make the function harder to use correctly.
- code-review-04: The GIL protects individual bytecode operations, but not multi-step sequences like read-modify-write.
- code-review-04: In CPython, inconsistent reads are not a significant problem for a simple int assignment.
- code-review-05: In some shells the no-match case just errors out silently.
- code-review-05: The `-f` flag to rm suppresses the "no such file" error.
- code-review-05: The script uses $BACKUP_DIR unquoted in the final echo.
- code-review-05: The script's quoting is inconsistent throughout.
- code-review-05: Using `set -eu` at the top would have caught the empty-variable and command-failure issues immediately.
- code-review-05: `set -eu` makes the script fail fast on errors and unset variables.
- code-review-05: `${1:?...}` requires the argument to be provided.
- code-review-05: Quoting cd makes a cd failure abort the script instead of silently falling through.
- code-review-05: A glob will not match directories named `*.tmp` recursively.
- code-review-05: The `-r` flag on rm in the original script was a latent risk.
- code-review-06: Configs built programmatically and merged with themselves make self-references more plausible than they sound.
- code-review-06: Only one of the three base/override type combinations behaves consistently with the rule 'override always wins, but dicts merge when both sides agree.'
- code-review-06: The base=scalar/override=dict behavior suggests the intended rule was 'override always wins, but dicts merge when both sides agree.'
- code-review-06: Overriding a dict-valued key with an empty dict is a no-op rather than a clear.
- code-review-06: merge_settings({"a": {"x": 1}}, {"a": {}}) returns {"a": {"x": 1}} unchanged.
- code-review-06: Merging with an empty override dict has nothing to apply.
- code-review-06: The project has no test suite.
- code-review-06: Characterization tests are cheap to write and pin down what correct behavior means before refactoring.
- code-review-07: withRetry has three distinct outcomes collapsed into two ambiguous return values.
- code-review-07: Nothing in the code documents or uses the distinction between the null and undefined return values.
- code-review-07: If a non-Error value such as null is thrown, reading err.status raises a TypeError.
- code-review-07: In the throw null case, accessing err.status throws inside the catch handler, producing an unhandled rejection instead of the intended fallback.
- code-review-07: On the last allowed iteration, a 429 still triggers the full setTimeout delay before the loop exits and the function returns.
- code-review-07: withRetry never throws and always returns a sentinel value.
- code-review-07: withRetry treats all 5xx responses as retryable and all other errors as fatal.
- code-review-07: HTTP status 501 is a 5xx status that is not actually retryable.
- code-review-07: The attempts parameter means total attempts rather than retries after the first try.
- code-review-08: No relevant memory was found for this project.
- code-review-08: os.path.getmtime works on directories.
- code-review-08: The 'removed < 500' check is evaluated before the deletion it guards, not after.
- code-review-08: Because the check runs before the deletion, the actual cap is 501 rather than 500.
- code-review-08: For an unattended scheduled job, the lack of error handling means silent partial failures.
- code-review-08: The script has no dry-run mode.
- code-review-08: There is no way to safely preview what a run would touch.
- code-review-08: The files the script deletes have unclear provenance and the scheduling is unset.
- code-review-08: The script performs no path validation.
- code-review-08: The code contains the expression 86400 * 45, which corresponds to a 45-day retention window.
- code-review-08: The 45-day window and the unconditional tmp/part deletion are likely deliberate but undocumented.
- code-review-08: The cap applying only to the age branch is inconsistent and has no plausible rationale.
- code-review-08: The off-by-one on the cap is likely accidental.
- code-review-08: The values 45 and 500 may map to a retention policy or a downstream rate limit.
- code-review-08: Issues #1, #3, #4, and #5 have no plausible reason to be intentional.
- debugging-02: Class bodies run in strict mode.
- debugging-02: When `this` is `undefined`, `this.seconds += 1` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: `setInterval(function () {...}.bind(this), 1000)` is an alternative fix that keeps a regular function.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-04: A 0xc3 byte likely indicates an accented character such as é or ü.
- debugging-04: `utf-8-sig` should be used instead if the file may have a BOM.
- debugging-04: `chardet` and `charset-normalizer` can be used to detect a file's encoding.
- debugging-05: A default argument value is created once, when the function is defined.
- debugging-05: After that call, `DEFAULT_TAGS` is permanently `["draft", "post"]`.
- debugging-05: With the sentinel fix, callers who pass their own list will still have that list mutated by `append`.
- debugging-06: A second leading candidate cause is a slow connection leak in the export worker itself.
- debugging-06: Connections may not be released on error paths, causing the pool to gradually shrink over a run.
- debugging-06: A gradual pool shrink would eventually leave a batch unable to obtain a connection.
- debugging-06: A connection leak would explain the non-deterministic failures because it depends on the error rate during a given session.
- debugging-06: Failures caused by a connection leak tend to cluster near the end of long runs.
- debugging-06: Another less likely cause is a periodic DB-side resource spike (backup, autovacuum, or replication lag) that slows all queries at once.
- debugging-06: The relevant window to inspect is roughly 30 seconds before each timeout.
- debugging-06: Logging pool checkout/checkin counts and wait queue depth would show whether the pattern is leak-shaped (gradual decline) or spike-shaped (sudden demand).
- debugging-07: Shared test database or state across pytest-xdist workers is the most likely cause of the flaky failure.
- debugging-07: If the digest endpoint returns 'latest N events' without strict scoping to the test's own user or tenant, a concurrently running test can push one of the 3 seeded events out of the window.
- debugging-07: A read-after-write / eventual consistency race is the second most likely cause.
- debugging-07: Under CI's 4x concurrency, workers compete for CPU and DB connections.
- debugging-07: 4 parallel workers sharing a small DB connection pool could cause a write to queue or retry so that it lands after the digest read.
- debugging-07: Connection pool exhaustion could cause the failure without any explicit error surfacing in the test.
- debugging-07: Checking whether each xdist worker gets its own DB or schema is the cheapest first diagnostic step.
- debugging-07: The digest implementation should be grepped for implicit scoping or limits such as LIMIT, ORDER BY created_at DESC with a cap, or a time window not strictly filtered by the test's user or tenant ID.
- debugging-07: Confirming parallelism as the trigger separates hypothesis 1 from hypotheses 2, 3, and 4.
- debugging-07: Temporary instrumentation should log event IDs and timestamps returned by the API versus those returned by the digest, plus the worker ID that created them.
- debugging-07: Worker count can be bisected by temporarily running -n2 and -n3 in CI.
- debugging-07: If the failure rate scales with worker count rather than staying constant, that points to shared-resource contention rather than pure timing.
- debugging-07: Steps 1 and 2 are static or config checks that need no CI cycles.
- debugging-07: The recommended order is to start with steps 1 and 2, then use step 3 to confirm before spending time on instrumentation.
- debugging-08: Collections keyed by request, session, or correlation IDs that grow without cleanup are a candidate leak source
- debugging-08: Unbounded metrics or histogram label cardinality is a candidate leak source
- debugging-08: If growth-rate per request is roughly constant across canary and normal instances, unbounded per-request growth is the prime suspect
- debugging-08: Bounded caches are a classic false lead in memory investigations
- debugging-08: Product objects can grow over time as more fields, variants, or images are added
- debugging-08: Cache eviction can be broken for certain code paths
- debugging-08: Multiple cache instances (per-thread or per-connection) can each be individually bounded while multiplying without bound
- debugging-08: If logged cache size plateaus at the configured bound, the cache is not the culprit or is only one contributor
- debugging-08: If process memory still grows when a second cache is given a deliberately tiny bound, the cache is not the primary cause
- debugging-08: An LRU eviction policy implemented with a lock that is sometimes bypassed may fail to fire
- debugging-08: Eviction that triggers only on insert leaves expired-but-present entries uncleaned during lookups
- debugging-08: Memory growth that survives quiet nights is also consistent with heap fragmentation from allocator behavior
- debugging-08: Variable-size allocations such as product payloads of differing sizes can fragment the heap
- debugging-08: Heap fragmentation can prevent freed memory from being returned to the OS or reused efficiently
- debugging-08: Fragmentation would explain RSS never dropping even when logical memory usage does
- debugging-08: Go exposes heap_alloc and heap_live statistics that can be compared against RSS
- debugging-08: C and C++ expose malloc_stats and jemalloc statistics for allocator accounting
- debugging-08: JVM and .NET expose GC heap statistics for allocator accounting
- debugging-08: Flat live-object memory combined with climbing RSS indicates fragmentation rather than a leak
- debugging-08: Fragmentation requires a different fix than a leak, such as a compacting GC or a different allocator
- debugging-08: Periodic restart is a reasonable mitigation for fragmentation
- debugging-08: If a forced GC or compaction does not reduce RSS, the retention is OS-level rather than application-level
- debugging-08: Campaigns may trigger specific code paths such as promotions or coupon rules that leak
- debugging-08: Unusually high distinct-entity cardinality during campaigns would implicate cache-key cardinality rather than the cache size bound
- debugging-08: A single pprof or heap dump comparison between start and end of week would settle whether the issue is a leak or fragmentation
- explanation-01: A hash map needs a strategy to handle collisions because it cannot overwrite existing data.
- explanation-01: Quadratic probing reduces clustering.
- explanation-01: Double hashing uses a second hash function to compute the step size.
- explanation-01: Open addressing requires careful resizing (rehashing) well before the table gets full, often at around 70% load.
- explanation-01: Most standard library implementations use chaining.
- explanation-01: Java's HashMap uses chaining.
- explanation-01: Java's HashMap often converts a bucket's list to a balanced tree if it grows too large.
- explanation-01: Converting a bucket's list to a balanced tree is a hybrid approach that protects against worst-case performance from many collisions.
- explanation-02: `SELECT * FROM accounts WHERE id = 1 FOR UPDATE;` is an example of pessimistic locking in Postgres and MySQL.
- explanation-02: Pessimistic locking fits when the cost of retrying a failed operation is high.
- explanation-02: Inventory decrements at checkout for a hot-selling item are an example of a workload suited to pessimistic locking.
- explanation-02: Many ORMs implement optimistic locking.
- explanation-02: Hibernate implements optimistic locking with `@Version`.
- explanation-02: EF Core implements optimistic locking with concurrency tokens.
- explanation-02: Collaborative editing is an example use case for optimistic locking.
- explanation-03: The problem of retransmissions and degraded performance from dropped packets is known as congestion collapse.
- explanation-03: Congestion collapse was a real problem on the early internet in the late 1980s.
- explanation-03: TCP slow start is one of the original congestion control mechanisms.
- explanation-03: Historically the initial cwnd was 1 segment.
- explanation-03: The initial cwnd is now often around 10 segments.
- explanation-03: The initial window of about 10 segments is specified in RFC 6928.
- explanation-03: A larger initial window speeds up short connections.
- explanation-03: In congestion avoidance, the window grows linearly instead of exponentially.
- explanation-03: After detecting packet loss, TCP backs off.
- explanation-04: A process has its own file descriptors and OS resources.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own register state.
- explanation-04: Ruby historically serialized thread execution for CPU-bound code because of a global interpreter lock.
- explanation-04: Separate processes enable privilege separation between a low-privilege worker and a privileged coordinator.
- explanation-04: A separate process can be independently supervised, killed, and restarted without disturbing the rest of the system.
- explanation-04: Independent process restart is useful for workers that leak memory over time or that crash.
- explanation-04: Erlang/OTP-style 'let it crash' supervision is based on independent process lifecycle and restart.
- explanation-04: Gunicorn and Nginx worker processes are based on independent process lifecycle and restart.
- explanation-04: Process-based designs using separate services communicating over IPC or network generalize naturally to distributed systems.
- explanation-04: Threads only work within a single machine's shared memory.
- explanation-04: A web server handling many connections that share an in-memory cache is an example where threads win.
- explanation-05: Event emitters, DOM elements, and global services are examples of long-lived objects that listeners can be registered on.
- explanation-06: With a cache in place, writes still have to hit the database.
- explanation-06: Adding a cache means writes must also update or invalidate the cache.
- explanation-06: Possible non-database bottlenecks include slow application code, network latency, N+1 query problems, missing indexes, and external API calls.
- explanation-06: In a write-heavy workload, a cache adds complexity and can slow things down due to the extra layer to update and invalidate.
- explanation-06: Some databases have a slow query log.
- explanation-06: A database's slow query log often points directly at missing indexes or expensive queries.
- explanation-06: A rough read/write ratio can be obtained from a manual count of logs over an hour.
- explanation-07: A product team being unable to say how much growth to expect indicates the access pattern is not yet well understood.
- explanation-07: If read load can be offloaded to replicas and storage growth handled by bigger disks or instance classes, there are likely years of runway before sharding becomes necessary.
- explanation-07: Write throughput and replication lag serve as leading indicators of approaching a scaling ceiling.
- explanation-07: Tables can be partitioned by date or by tenant.
- explanation-07: Partitioning now makes a later shard split easier because the data is already logically separated.
- explanation-07: Growth across tenants often turns out uneven, with some tenants very large and most very small.
- explanation-08: JSON encode/decode accounting for about 2% of request latency is common when network, database, or business logic dominate.
- explanation-08: If JSON encode/decode is 2% of request latency, a 10x faster serializer yields roughly a 1.8% overall improvement.
- explanation-08: Binary formats such as protobuf and msgpack typically reduce payload size by 30-70% compared to JSON.
- explanation-08: Gzip compression significantly narrows the payload size gap between JSON and binary formats.
- explanation-08: Serialization exceeding 10-15% of request latency counts as a meaningful chunk.
- explanation-08: Prototyping a binary format on one endpoint surfaces migration costs such as schema management, debuggability, and client compatibility.
- summarization-02: The incident took about 7 minutes to page.
- summarization-02: Full rollback and recovery took about 34 minutes.
- summarization-02: The detection and rollback path worked well.
- summarization-02: The fix should focus on prevention rather than response speed.
- summarization-04: After clicking the PDF export option, nothing happens initially.
- summarization-04: The bug was reproduced on different machines.
- summarization-07: All findings other than the median latency and memory measurements are provisional.
- summarization-07: The recommendation is to profile memory before drawing conclusions on tail latency or stability.
- summarization-07: The recommendation is to test under production-like traffic before drawing conclusions on tail latency or stability.
- summarization-08: It is firm that the progress bar behavior is a problem.
- summarization-08: The cause of the progress bar issue is tentative.
- summarization-08: Whether the fix should be visual or technical needs more investigation.
- summarization-08: The template gallery observation is not counted as a core finding.

Added facts (styled only):

- code-review-01: The function contains five real bugs.
- code-review-01: The five bugs are presented in order of severity.
- code-review-01: Whether the lack of `name` validation matters depends on what `db.insert` expects.
- code-review-01: The corrected version raises `ValueError("db is required")` when `db` is `None`.
- code-review-01: The corrected version raises `ValueError("name is required")` when `name` is falsy.
- code-review-01: The corrected version copies the roles list with `list(roles) if roles else []`.
- code-review-01: `SomeDbError` in the corrected version is a placeholder that should be replaced with the exception that `db.insert` actually raises.
- code-review-02: The unused `async` keyword hides the fact that the fetch is not connected to the function's return value.
- code-review-02: The corrected version throws an `Error` with the message `Failed to load user ${userId}: ${res.status}` when `res.ok` is false.
- code-review-03: With parameterized queries, the database driver handles escaping.
- code-review-03: The `%s` placeholder is used by drivers such as `psycopg2` and `mysql-connector`.
- code-review-04: There is no way to read `value` safely.
- code-review-04: Adding a `get()` method that acquires `self._lock` would let outside code read the current count safely.
- code-review-05: If `$1` is empty, `cd $BACKUP_DIR` fails but the script keeps running.
- code-review-05: `$1` and `$BACKUP_DIR` are used unquoted in the script.
- code-review-05: If `BACKUP_DIR` does not exist or is empty, `cd` fails and prints an error.
- code-review-05: With no matching files, `rm -rf *.tmp` fails harmlessly with a file-not-found error.
- code-review-05: Relying on `ls`-parsing and unquoted variables breaks more easily under `sh` (dash) than under bash.
- code-review-05: dash has fewer safety nets than bash.
- code-review-05: The suggested rewrite checks `[ -z "${1:-}" ]` and exits 1 with a usage message on stderr.
- code-review-06: The function has three real bugs.
- code-review-06: The function has two design choices that are probably intentional but should be confirmed with someone who knows the config schema.
- code-review-06: The recursion branch is guarded by `elif key in merged and isinstance(merged[key], dict)`.
- code-review-06: The function performs no input validation on the types of `base` and `override`.
- code-review-06: `dict(base)` raises `TypeError` if `base` is `None`.
- code-review-06: The caller contract for argument types is not documented anywhere in the code.
- code-review-06: The deletion behavior is implemented as `if value is None: merged.pop(key, None)`.
- code-review-06: The recommendation is to add a short docstring or comment documenting the delete-on-`None` and replace-vs-merge behaviors as intentional.
- code-review-07: The `err.status >= 500` branch retries immediately with no delay.
- code-review-07: The 5xx branch is missing an `await` for a delay if the intent was to back off on any retryable error.
- code-review-07: The backoff formula probably should be `1000 * (i + 1)`.
- code-review-07: The untyped-error case is the riskiest issue for callers that cannot be inspected, because it hides failures instead of surfacing them.
- code-review-07: Lack of jitter is fine for low-volume internal use.
- code-review-07: The code alone does not reveal whether the thundering-herd risk was considered.
- code-review-07: There is no separate cap on 5xx retries; 429s and 5xxs draw from the same shared `attempts` budget.
- code-review-07: A mix of 429 and 5xx errors can exhaust retries faster than either type alone.
- code-review-07: The shared retry budget may be intentional simplicity rather than an oversight.
- code-review-07: An explicit `return null;` or `throw` should be added after the loop so exhausted retries do not return `undefined`.
- code-review-07: A delay should be added before retrying 5xx errors, matching the 429 branch.
- code-review-07: The backoff formula should be fixed to `1000 * (i + 1)` so the first retry is not instant.
- code-review-07: Changes beyond the backoff timing fixes should be confirmed with whoever owns the calling code.
- code-review-08: If an export job is still writing a `tmp-`/`.part` file when cleanup runs, the in-progress export will be deleted.
- code-review-08: The 500-file cap on old-file deletion appears to be an intentional safety brake limiting blast radius if `CUTOFF` logic misbehaves.
- code-review-08: Clock skew could place `CUTOFF` far in the future and cause nearly every file to be flagged as old.
- code-review-08: Capping deletions is a common and sensible defensive pattern.
- debugging-04: The decoder fails at byte 512 of the file.
- debugging-04: 0xc3 is a lead byte for a two-byte UTF-8 sequence.
- debugging-04: The errors="replace" and errors="ignore" options substitute or drop bytes rather than reproducing them exactly.
- debugging-04: Detecting the encoding first is the option to use when an exact byte-for-byte match is needed.
- debugging-05: Leftover tags can include a second `"post"` or tags added by another test.
- debugging-05: The full test suite should be run after the fix, not just this one test.
- debugging-05: Running the full suite confirms whether other tests relied on the old shared-list behavior.
- debugging-06: Only worker-3 appears in the log fragment.
- debugging-06: When the combined pool sizes exceed the DB connection limit, whichever service loses the race times out.
- debugging-06: The retry at attempt 2 also failed.
- debugging-06: The failed retry suggests the pool was still exhausted 34 seconds later.
- debugging-06: If the job retries aggressively without backoff, the retries themselves can prolong contention instead of easing it.
- debugging-06: A recent deploy introducing a slow query or lock is worth ruling out only if the failures started after a specific date.
- debugging-06: The failure window was 02:14:07 to 02:14:41 UTC on 2026-07-29.
- debugging-06: Pool wait-time metrics can let the problem be caught before it times out.
- debugging-06: The surrounding log context was rotated away.
- debugging-06: Logs from the minutes before 02:14:07 showing what analytics was doing are missing.
- debugging-06: Extending log retention for at least one week should allow catching the next occurrence with full context.
- debugging-06: Load-testing both services against a shared test DB can confirm whether pool sizing alone explains the exhaustion.
- debugging-06: The export job runs nightly.
- debugging-06: Common fixes are separate connection pools per service with hard caps, a raised max_connections with adjusted pool sizes, or scheduling the analytics job outside the export window.
- debugging-07: The failure requires contention that only four parallel workers under CI's shared, possibly slower hardware reliably produce.
- debugging-07: If the digest reads from a read replica while event creation writes to the primary, replication lag that is usually near-zero can spike under CI's shared infrastructure.
- debugging-07: If the API deduplicates near-identical events within a short time window, tightly clustered event creation under fast parallel execution could cause an unintended dedup.
- debugging-07: Without captured failure data, every other hypothesis is a guess.
- debugging-07: The xdist worker ID is available in the environment variable `PYTEST_XDIST_WORKER`.
- debugging-07: Fixes for a write/read race are making event creation synchronous or having the test poll instead of asserting immediately.
- debugging-07: If the digest windows by timestamp, the window may be computed from a clock read at request time or from a fixed point set during test setup.
- debugging-07: The test has a flake rate of roughly 10%.
- debugging-07: Success means being able to reproduce the failure on demand, locally under parallel load or via a scripted CI rerun loop.
- debugging-07: Success also means artifact capture showing which of the two events is missing and why.
- debugging-07: Once the cause is known, the fix follows directly: make event creation synchronous/awaited, isolate worker state, or fix the digest's time window logic.
- debugging-08: The memory directory was checked and contains no existing notes on this order service or its memory issue.
- debugging-08: The size-bounded cache is the most likely single culprit.
- debugging-08: Marketing campaigns add new or promoted SKUs, which increases cache churn and entry size.
- debugging-08: Webhook traffic drives more cache lookups.
- debugging-08: The canary continues to grow without webhook traffic, just more slowly.
- debugging-08: If evicted cache entries are still referenced elsewhere, the garbage collector or allocator cannot reclaim them.
- debugging-08: Lingering references to evicted entries can come from event listeners, callback closures, secondary indexes, or metrics taggers.
- debugging-08: Taking two heap snapshots hours apart under load and diffing retained objects is a check for the retained-reference hypothesis.
- debugging-08: If counts of the cached type exceed the current cache size, something outside the cache still holds references.
- debugging-08: Webhook handling often opens connections, buffers payloads, or creates short-lived worker objects.
- debugging-08: If webhook-related allocations leak per call, campaign weeks would show faster memory growth due to higher webhook volume.
- debugging-08: Comparing the growth rate curve against the webhook request rate curve is a check for the webhook allocation hypothesis.
- debugging-08: If growth rate and webhook request rate track tightly, the webhook handler's allocation lifecycle should be examined.
- debugging-08: If growth rate and webhook request rate do not track, the webhook cause should be deprioritized.
- debugging-08: Because the canary grows with zero webhook traffic, part of the leak is traffic-independent.
- debugging-08: Traffic-independent leak sources include scheduled jobs, metrics or log buffers, connection pools that grow and never shrink, and slow leaks in shared libraries used on every request path.
- debugging-08: The canary still performs activities such as health checks or database polling.
- debugging-08: Disabling one background subsystem at a time on the canary over several days and watching for a flattened growth curve isolates the traffic-independent portion of the leak.
- debugging-08: The fact that memory does not recover on quiet nights rules out merely delayed cleanup such as late-but-eventual GC or allocator reclamation.
- debugging-08: If the cause were delayed cleanup, a quiet night would show at least partial return toward baseline.
- debugging-08: The lack of recovery means memory is truly retained rather than merely uncollected.
- debugging-08: The lack of overnight recovery strengthens the retained-reference theory over a pure GC-tuning issue.
- debugging-08: Instrumenting cache byte size versus entry count is the cheapest check with the most likely payoff and should be done first.
- debugging-08: If cache byte size is flat, the next step is heap snapshots diffed for retained-but-evicted objects.
- debugging-08: The canary subsystem-disabling experiment is slow, taking multiple days.
- debugging-08: The canary experiment can run in parallel with the cache instrumentation and heap snapshot checks.
- explanation-01: A hash map must handle collisions because the hash function maps a huge space of possible keys onto a small, fixed number of buckets.
- explanation-01: Because the key space is larger than the number of buckets, some keys are bound to land in the same bucket.
- explanation-02: Optimistic locking fits when conflicts are rare and reads vastly outnumber writes.
- explanation-02: Under pessimistic locking, other transactions are sometimes prevented from even reading the locked row.
- explanation-02: Poor lock management can cause deadlocks.
- explanation-03: A network path might cross both a fast local network and a slow overseas link.
- explanation-03: Every packet in a batch gets acknowledged.
- explanation-03: ssthresh stands for slow start threshold.
- explanation-03: Doubling the window each round trip lets the sender find the network's capacity in roughly log₂ of the eventual window size steps.
- explanation-03: Linear growth would take many rounds to creep up to the network's capacity.
- explanation-03: With a small starting window, the sender loses only a few packets before slow start ends, instead of flooding the path.
- explanation-04: The difference in memory sharing drives most practical tradeoffs between processes and threads.
- explanation-04: Some web servers fork a worker process per request or per core.
- explanation-06: Datadog and New Relic are examples of APM software.
- explanation-06: The read-to-write ratio should be measured over a representative time window.
- explanation-07: Sharding complexity cannot be sized correctly without knowing the growth rate.
- explanation-07: Sharding fixes write-throughput and lock-contention limits rather than storage size.
- explanation-07: Operating a sharded distributed system requires sufficient staffing.
- explanation-07: Hitting a write-throughput or connection ceiling causes latency spikes or outages during peak traffic with no fast fix available.
- explanation-07: Maintenance exceeding the maintenance window degrades performance gradually until it becomes an incident.
- explanation-07: The single-node path stays reversible.
- explanation-07: Slow or impossible cross-shard operations can break features the product team has not yet scoped.
- explanation-07: Sharding is hard to reverse; unsharding or reshaping shards is one of the more expensive migrations in a system's life.
- explanation-07: A rough growth range tied to a roadmap milestone changes the scaling plan.
- explanation-07: Sharding should be revisited only when there is evidence of a specific bottleneck and a growth number to size the shard scheme against.
- explanation-08: Binary formats such as protobuf and msgpack typically reduce payload size by 20-60% compared to JSON.
- explanation-08: Payload size reduction helps less for small payloads, where headers and connection overhead dominate.
- explanation-08: Current payload sizes should be measured at the median and p95 for typical requests.
- summarization-01: Each button's tooltip shows that button's keyboard shortcut.
- summarization-01: Plugins now load only when needed.
- summarization-01: Lazy plugin loading is the reason for the faster startup.
- summarization-01: The release includes a build tooling upgrade.
- summarization-01: The release includes a session module refactor.
- summarization-01: The release includes a change to the telemetry interval.
- summarization-01: The build tooling upgrade, session module refactor, and telemetry interval change are internal.
- summarization-01: The build tooling upgrade, session module refactor, and telemetry interval change do not affect how users use the app.
- summarization-01: The build tooling upgrade, session module refactor, and telemetry interval change are omitted from the release notes.
- summarization-02: Staging intentionally uses smaller connection pool sizes than production.
- summarization-02: Nothing distinguished the staging template from the production template.
- summarization-02: The exhausted connection pool caused checkout errors.
- summarization-02: About 12% of requests experienced checkout errors during the incident.
- summarization-02: The incident ran from 09:14 to 09:48 UTC.
- summarization-04: The issue was reproduced by two different users.
- summarization-04: The issue is not browser-specific.
- summarization-05: A sprint planning meeting took place on Monday.
- summarization-05: The listed items are action items from Monday's sprint planning.
- summarization-05: Ada is assigned to run the payments database migration dry run.
- summarization-07: All findings other than the median latency improvement need more data.
- summarization-07: Staging runs a newer kernel.
- summarization-07: The recommendation is to investigate the crash before drawing conclusions on production readiness.
- summarization-08: The field-mapping result is the strongest result in the study.
- summarization-08: The progress bar finding is characterized as tentative but worth acting on.
- summarization-08: The abandonment outcome is concrete enough to justify a UI fix rather than more research first.
- summarization-08: A likely UI fix is a clearer progress indicator for large files.
- summarization-08: The template gallery finding is characterized as tentative with an unclear cause.
- summarization-08: Possible follow-up for the template gallery includes usage analytics or a task specifically prompting template use.
- summarization-08: The differing-default-settings signal is additional signal, not a finding.

### clarity-flow

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 26 | 19 | 0.731 | 24 | 7 |
| code-review-02 | 19 | 13 | 0.684 | 19 | 2 |
| code-review-03 | 25 | 19 | 0.76 | 18 | 3 |
| code-review-04 | 14 | 9 | 0.643 | 17 | 4 |
| code-review-05 | 39 | 30 | 0.769 | 30 | 2 |
| code-review-06 | 30 | 23 | 0.767 | 26 | 4 |
| code-review-07 | 23 | 14 | 0.609 | 33 | 7 |
| code-review-08 | 42 | 27 | 0.643 | 19 | 6 |
| debugging-01 | 6 | 5 | 0.833 | 7 | 0 |
| debugging-02 | 14 | 11 | 0.786 | 12 | 2 |
| debugging-03 | 8 | 6 | 0.75 | 10 | 0 |
| debugging-04 | 11 | 6 | 0.545 | 12 | 3 |
| debugging-05 | 16 | 15 | 0.938 | 12 | 2 |
| debugging-06 | 27 | 16 | 0.593 | 20 | 7 |
| debugging-07 | 28 | 17 | 0.607 | 24 | 6 |
| debugging-08 | 40 | 16 | 0.4 | 41 | 32 |
| explanation-01 | 42 | 35 | 0.833 | 22 | 2 |
| explanation-02 | 32 | 25 | 0.781 | 27 | 8 |
| explanation-03 | 30 | 26 | 0.867 | 26 | 3 |
| explanation-04 | 31 | 16 | 0.516 | 24 | 3 |
| explanation-05 | 14 | 13 | 0.929 | 18 | 3 |
| explanation-06 | 17 | 9 | 0.529 | 22 | 6 |
| explanation-07 | 27 | 18 | 0.667 | 23 | 6 |
| explanation-08 | 14 | 8 | 0.571 | 19 | 7 |
| summarization-01 | 6 | 5 | 0.833 | 9 | 2 |
| summarization-02 | 13 | 12 | 0.923 | 14 | 2 |
| summarization-03 | 13 | 12 | 0.923 | 11 | 0 |
| summarization-04 | 13 | 11 | 0.846 | 13 | 1 |
| summarization-05 | 9 | 8 | 0.889 | 9 | 1 |
| summarization-06 | 15 | 13 | 0.867 | 10 | 1 |
| summarization-07 | 16 | 14 | 0.875 | 14 | 1 |
| summarization-08 | 25 | 23 | 0.92 | 20 | 1 |

Median fraction: 0.768 over 32 scored pairs.

Median additions: 3.0 over 32 scored pairs.

Lost facts:

- code-review-01: Swallowing all exceptions makes the mutable-default and missing-`db` bugs invisible.
- code-review-01: The function does not check whether "member" is already present in `roles`, which can produce duplicate entries.
- code-review-01: The suggested fix builds a new list with `[*roles, "member"]` instead of appending in place.
- code-review-01: The suggested fix makes `db` a required positional parameter with no default.
- code-review-01: The suggested fix catches `DatabaseError` rather than using a bare `except:`.
- code-review-01: The suggested fix calls `logger.exception` before returning `False`.
- code-review-01: `DatabaseError` is what is actually expected to be raised from a database call.
- code-review-02: The TypeError message is "Cannot read properties of undefined (reading 'name')".
- code-review-02: Without error handling, a failed fetch (network error) or a non-OK response causes a silent failure or an unhandled rejection instead of a meaningful error.
- code-review-02: The unnecessary `async` keyword masks the fact that the function is not actually asynchronous in its logic.
- code-review-02: The code does not check that `data` has a `name` property before calling `.toUpperCase()` on it.
- code-review-02: The proposed fixed version throws an Error when `data.name` is missing.
- code-review-02: Callers of the fixed function should wrap calls in `try/catch` to handle thrown errors.
- code-review-03: Any input containing a single quote breaks out of the SQL string literal.
- code-review-03: Passing `customer_name = "x' OR '1'='1"` returns all rows.
- code-review-03: `SELECT *` forces callers to guess column order and meaning from the return value instead of getting named fields.
- code-review-03: Nothing stops `customer_name` or `status` from being `None`, empty, or the wrong type.
- code-review-03: Invalid input types will produce a confusing SQL error or unexpected query behavior.
- code-review-03: If the `orders` table is large, `fetchall()` loads everything into memory at once.
- code-review-04: The class is explicitly used from multiple threads.
- code-review-04: In CPython, inconsistent reads are not a significant problem for a simple int assignment.
- code-review-04: The corrected implementation creates a `threading.Lock` as `self._lock` in `__init__` and initializes `self.value` to 0.
- code-review-04: In the corrected implementation, `increment` executes `self.value += 1` inside a `with self._lock:` block.
- code-review-04: In the corrected implementation, `reset` executes `self.value = 0` inside a `with self._lock:` block.
- code-review-05: Glob-expansion behavior when there are no matches varies across POSIX sh implementations.
- code-review-05: In some shells the no-match case just errors out silently.
- code-review-05: The `-f` flag to rm suppresses the "no such file" error.
- code-review-05: The no-match case for `rm -rf *.tmp` is not catastrophic in this script.
- code-review-05: If `*.log` does not expand, gzip receives a literal `*.log` argument and produces a spurious error.
- code-review-05: The script uses $BACKUP_DIR unquoted in the final echo.
- code-review-05: The script's quoting is inconsistent throughout.
- code-review-05: Quoting cd makes a cd failure abort the script instead of silently falling through.
- code-review-05: A glob will not match directories named `*.tmp` recursively.
- code-review-06: Configs built programmatically and merged with themselves make self-references more plausible than they sound.
- code-review-06: Only one of the three base/override type combinations behaves consistently with the rule 'override always wins, but dicts merge when both sides agree.'
- code-review-06: Overriding a dict-valued key with an empty dict is a no-op rather than a clear.
- code-review-06: merge_settings({"a": {"x": 1}}, {"a": {}}) returns {"a": {"x": 1}} unchanged.
- code-review-06: Merging with an empty override dict has nothing to apply.
- code-review-06: The project has no test suite.
- code-review-06: Characterization tests are cheap to write and pin down what correct behavior means before refactoring.
- code-review-07: withRetry has three distinct outcomes collapsed into two ambiguous return values.
- code-review-07: Nothing in the code documents or uses the distinction between the null and undefined return values.
- code-review-07: On the last allowed iteration, a 429 still triggers the full setTimeout delay before the loop exits and the function returns.
- code-review-07: The retry delays include no jitter.
- code-review-07: Fixed linear delays cause concurrent callers hitting the same rate limit to retry in lockstep, producing a thundering-herd pattern.
- code-review-07: withRetry never throws and always returns a sentinel value.
- code-review-07: withRetry treats all 5xx responses as retryable and all other errors as fatal.
- code-review-07: The attempts parameter means total attempts rather than retries after the first try.
- code-review-07: The history of the withRetry code is unknown and its callers cannot be inspected.
- code-review-08: No relevant memory was found for this project.
- code-review-08: os.path.getmtime works on directories.
- code-review-08: os.path.getmtime raises FileNotFoundError on broken symlinks.
- code-review-08: The 'removed < 500' check is evaluated before the deletion it guards, not after.
- code-review-08: Because the check runs before the deletion, the actual cap is 501 rather than 500.
- code-review-08: When the function aborts, 'removed' is left undefined to the caller and the rest of the directory is unprocessed.
- code-review-08: For an unattended scheduled job, the lack of error handling means silent partial failures.
- code-review-08: The script has no dry-run mode.
- code-review-08: There is no way to safely preview what a run would touch.
- code-review-08: The files the script deletes have unclear provenance and the scheduling is unset.
- code-review-08: The script performs no path validation.
- code-review-08: The code contains the expression 86400 * 45, which corresponds to a 45-day retention window.
- code-review-08: The cap applying only to the age branch is inconsistent and has no plausible rationale.
- code-review-08: The off-by-one on the cap is likely accidental.
- code-review-08: Issues #1, #3, #4, and #5 have no plausible reason to be intentional.
- debugging-01: The corrected get_url function returns f"http://{cfg['host']}:{cfg['port']}/api".
- debugging-02: Class bodies run in strict mode.
- debugging-02: When `this` is `undefined`, `this.seconds += 1` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-03: `moving_sum` returns the sum of each window of the given size.
- debugging-03: `moving_sum([1, 2, 3, 4], 2)` returns `[3, 5, 7]`.
- debugging-04: A 0xc3 byte likely indicates an accented character such as é or ü.
- debugging-04: The `ascii` codec fails on any byte outside the range 0–127.
- debugging-04: `utf-8-sig` should be used instead if the file may have a BOM.
- debugging-04: `chardet` and `charset-normalizer` can be used to detect a file's encoding.
- debugging-04: `errors="replace"` still counts lines correctly in the common case.
- debugging-05: With the sentinel fix, callers who pass their own list will still have that list mutated by `append`.
- debugging-06: The failures occur at variable batch numbers rather than a consistent one.
- debugging-06: Variable batch numbers rule out a specific bad row as the cause.
- debugging-06: The failures recur approximately weekly.
- debugging-06: Because the failures don't always hit the same batch, the problem is about when contention occurs rather than what the batch contains.
- debugging-06: Connections may not be released on error paths, causing the pool to gradually shrink over a run.
- debugging-06: A connection leak would explain the non-deterministic failures because it depends on the error rate during a given session.
- debugging-06: Failures caused by a connection leak tend to cluster near the end of long runs.
- debugging-06: Another less likely cause is a periodic DB-side resource spike (backup, autovacuum, or replication lag) that slows all queries at once.
- debugging-06: A failure occurred on 2026-07-29 at roughly 02:13–02:14.
- debugging-06: Comparing the analytics job schedule to the failure timestamps is the fastest lead to pursue.
- debugging-06: Additional incident logs could show whether all failures land in the same few-minute window.
- debugging-07: Async work that can delay queryability includes background jobs, message queues, and search indexes such as Elasticsearch or OpenSearch.
- debugging-07: Connection pool exhaustion could cause the failure without any explicit error surfacing in the test.
- debugging-07: The digest implementation should be grepped for implicit scoping or limits such as LIMIT, ORDER BY created_at DESC with a cap, or a time window not strictly filtered by the test's user or tenant ID.
- debugging-07: Confirming parallelism as the trigger separates hypothesis 1 from hypotheses 2, 3, and 4.
- debugging-07: Temporary instrumentation should log event IDs and timestamps returned by the API versus those returned by the digest, plus the worker ID that created them.
- debugging-07: Instrumentation output can be redirected to a file uploaded as an explicit CI artifact for just this test, or inspected by running locally in a loop with -n4.
- debugging-07: A poll or retry on the assertion should be tried in a scratch branch rather than committed.
- debugging-07: Worker count can be bisected by temporarily running -n2 and -n3 in CI.
- debugging-07: If the failure rate scales with worker count rather than staying constant, that points to shared-resource contention rather than pure timing.
- debugging-07: Steps 1 and 2 are static or config checks that need no CI cycles.
- debugging-07: The recommended order is to start with steps 1 and 2, then use step 3 to confirm before spending time on instrumentation.
- debugging-08: Traffic-correlated growth plus growth on the no-webhook canary points to something scaling with all request traffic rather than only webhooks
- debugging-08: Accumulating listeners or callbacks are a candidate leak source
- debugging-08: If growth-rate per request is roughly constant across canary and normal instances, unbounded per-request growth is the prime suspect
- debugging-08: Bounded caches are a classic false lead in memory investigations
- debugging-08: Cache eviction can be broken for certain code paths
- debugging-08: Multiple cache instances (per-thread or per-connection) can each be individually bounded while multiplying without bound
- debugging-08: If logged cache size plateaus at the configured bound, the cache is not the culprit or is only one contributor
- debugging-08: If process memory still grows when a second cache is given a deliberately tiny bound, the cache is not the primary cause
- debugging-08: An LRU eviction policy implemented with a lock that is sometimes bypassed may fail to fire
- debugging-08: Eviction that triggers only on insert leaves expired-but-present entries uncleaned during lookups
- debugging-08: Memory growth that survives quiet nights is also consistent with heap fragmentation from allocator behavior
- debugging-08: Variable-size allocations such as product payloads of differing sizes can fragment the heap
- debugging-08: Heap fragmentation can prevent freed memory from being returned to the OS or reused efficiently
- debugging-08: RSS never drops in the observed service
- debugging-08: Fragmentation would explain RSS never dropping even when logical memory usage does
- debugging-08: Go exposes heap_alloc and heap_live statistics that can be compared against RSS
- debugging-08: C and C++ expose malloc_stats and jemalloc statistics for allocator accounting
- debugging-08: JVM and .NET expose GC heap statistics for allocator accounting
- debugging-08: Flat live-object memory combined with climbing RSS indicates fragmentation rather than a leak
- debugging-08: Fragmentation requires a different fix than a leak, such as a compacting GC or a different allocator
- debugging-08: Periodic restart is a reasonable mitigation for fragmentation
- debugging-08: If a forced GC or compaction does not reduce RSS, the retention is OS-level rather than application-level
- debugging-08: Campaigns may trigger specific code paths such as promotions or coupon rules that leak
- debugging-08: A single pprof or heap dump comparison between start and end of week would settle whether the issue is a leak or fragmentation
- explanation-01: A hash map needs a strategy to handle collisions because it cannot overwrite existing data.
- explanation-01: Quadratic probing jumps by increasing steps such as index + 1, index + 4, index + 9.
- explanation-01: Quadratic probing reduces clustering.
- explanation-01: Open addressing requires careful resizing (rehashing) well before the table gets full, often at around 70% load.
- explanation-01: Language runtime implementations such as Python's dict use open addressing.
- explanation-01: Java's HashMap often converts a bucket's list to a balanced tree if it grows too large.
- explanation-01: Converting a bucket's list to a balanced tree is a hybrid approach that protects against worst-case performance from many collisions.
- explanation-02: `SELECT * FROM accounts WHERE id = 1 FOR UPDATE;` is an example of pessimistic locking in Postgres and MySQL.
- explanation-02: `UPDATE documents SET content = ?, version = version + 1 WHERE id = ? AND version = ?;` is an example optimistic locking statement.
- explanation-02: If an optimistic-locking UPDATE affects 0 rows, it means someone else modified the row first.
- explanation-02: Many ORMs implement optimistic locking.
- explanation-02: Hibernate implements optimistic locking with `@Version`.
- explanation-02: EF Core implements optimistic locking with concurrency tokens.
- explanation-02: Collaborative editing is an example use case for optimistic locking.
- explanation-03: A network path may be a fast local link or a congested transatlantic route through many routers.
- explanation-03: Historically the initial cwnd was 1 segment.
- explanation-03: The initial window of about 10 segments is specified in RFC 6928.
- explanation-03: A larger initial window speeds up short connections.
- explanation-04: A process is an independent instance of a running program.
- explanation-04: A process has its own file descriptors and OS resources.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own register state.
- explanation-04: Threads are cheaper than processes because no separate address space must be set up or protected.
- explanation-04: Ruby historically serialized thread execution for CPU-bound code because of a global interpreter lock.
- explanation-04: Separate processes are used for sandboxing untrusted plugin code.
- explanation-04: Separate processes enable privilege separation between a low-privilege worker and a privileged coordinator.
- explanation-04: A separate process can be independently supervised, killed, and restarted without disturbing the rest of the system.
- explanation-04: Independent process restart is useful for workers that leak memory over time or that crash.
- explanation-04: Erlang/OTP-style 'let it crash' supervision is based on independent process lifecycle and restart.
- explanation-04: Gunicorn and Nginx worker processes are based on independent process lifecycle and restart.
- explanation-04: Process-based designs using separate services communicating over IPC or network generalize naturally to distributed systems.
- explanation-04: Threads only work within a single machine's shared memory.
- explanation-04: A web server handling many connections that share an in-memory cache is an example where threads win.
- explanation-05: Event emitters, DOM elements, and global services are examples of long-lived objects that listeners can be registered on.
- explanation-06: With a cache in place, writes still have to hit the database.
- explanation-06: Adding a cache means writes must also update or invalidate the cache.
- explanation-06: A cache does not help when requests are mostly unique reads.
- explanation-06: When data is not reused, a cache mostly misses and adds overhead without benefit.
- explanation-06: Possible non-database bottlenecks include slow application code, network latency, N+1 query problems, missing indexes, and external API calls.
- explanation-06: In a write-heavy workload, a cache adds complexity and can slow things down due to the extra layer to update and invalidate.
- explanation-06: Profiling slow requests can be done with timing logs or an APM tool.
- explanation-06: A rough read/write ratio can be obtained from a manual count of logs over an hour.
- explanation-07: A product team being unable to say how much growth to expect indicates the access pattern is not yet well understood.
- explanation-07: If read load can be offloaded to replicas and storage growth handled by bigger disks or instance classes, there are likely years of runway before sharding becomes necessary.
- explanation-07: Write throughput and replication lag serve as leading indicators of approaching a scaling ceiling.
- explanation-07: Tables can be partitioned by date or by tenant.
- explanation-07: Partitioning now makes a later shard split easier because the data is already logically separated.
- explanation-07: Re-sharding later is far more painful than sharding late.
- explanation-07: Growth across tenants often turns out uneven, with some tenants very large and most very small.
- explanation-07: Rebalancing shards under uneven growth becomes an ongoing operational cost.
- explanation-07: Sharding before there is evidence it is needed means paying the rebalancing cost prematurely.
- explanation-08: JSON encode/decode accounting for about 2% of request latency is common when network, database, or business logic dominate.
- explanation-08: Binary formats such as protobuf and msgpack typically reduce payload size by 30-70% compared to JSON.
- explanation-08: Gzip compression significantly narrows the payload size gap between JSON and binary formats.
- explanation-08: Serialization exceeding 10-15% of request latency counts as a meaningful chunk.
- explanation-08: Prototyping a binary format on one endpoint surfaces migration costs such as schema management, debuggability, and client compatibility.
- explanation-08: Migration costs matter as much as raw serialization speed.
- summarization-01: Cold start time was reduced by approximately 40%.
- summarization-02: Prevention measures should include updating the checklist and separating the templates.
- summarization-03: Under the proposal, uploads would immediately save the original image.
- summarization-04: The Export button offers both a PDF option and a CSV option.
- summarization-04: The "export failed" error banners provide no further details.
- summarization-05: Ada is assigned to check with the mobile team lead on whether the mobile team was informed about the API deprecation.
- summarization-06: Pool metrics were not retained.
- summarization-06: The restart-driven recovery is consistent with multiple possible root causes.
- summarization-07: The recommendation is to profile memory before drawing conclusions on tail latency or stability.
- summarization-07: The recommendation is to test under production-like traffic before drawing conclusions on tail latency or stability.
- summarization-08: It is firm that the progress bar behavior is a problem.
- summarization-08: Role-based defaults are worth probing in a larger or targeted study before prioritizing.

Added facts (styled only):

- code-review-01: The function has five problems.
- code-review-01: The fixed version uses `roles=None` and `db=None` as defaults.
- code-review-01: The fixed version raises `ValueError("name is required")` when `name` is falsy.
- code-review-01: The fixed version raises `ValueError("db is required")` when `db` is `None`.
- code-review-01: The fixed version builds a new list with `list(roles) if roles else []` before appending `"member"`.
- code-review-01: The fixed version catches `Exception` instead of using a bare except.
- code-review-01: The fixed version logs the failure with `logger.error` including the user name and the exception.
- code-review-02: Because the function is `async`, the caller receives a promise.
- code-review-02: The corrected version awaits `res.json()` and returns `profile.name.toUpperCase()`.
- code-review-03: Lines 3-6 of the code contain a SQL injection vulnerability.
- code-review-03: SELECT * wastes bandwidth.
- code-review-03: With parameterized queries, the database driver escapes the values instead of the code.
- code-review-04: The current correctness depends on the CPython GIL making single attribute reads and writes atomic.
- code-review-04: The fix renames the attribute from `value` to `_value`.
- code-review-04: The fix adds a `value` property that acquires the lock before returning `_value`.
- code-review-04: External code reading `counter.value` directly, without going through the lock, would see a torn or stale value.
- code-review-05: The script has one critical bug.
- code-review-05: `cd $BACKUP_DIR` can fail if the argument is missing or the path does not exist.
- code-review-06: Calling the function a 'deep merge' is misleading, since it is only deep along paths that override actually visits.
- code-review-06: Lists and other containers are replaced rather than merged.
- code-review-06: Not merging lists is defensible because list merging is ambiguous (append, replace, or by index).
- code-review-06: The list-replacement behavior should be documented so callers do not expect list merging.
- code-review-07: The zero-delay first retry reads as an off-by-one error rather than intentional throttling.
- code-review-07: 5xx retries have no delay at all.
- code-review-07: The 5xx retry path is asymmetric with the 429 retry path, which does have a delay.
- code-review-07: Immediately hammering a struggling server is the opposite of desired behavior during an outage.
- code-review-07: The 429/5xx delay asymmetry looks unintentional.
- code-review-07: If `fn` rejects with null, undefined, or a string, accessing `err.status` throws inside the catch block.
- code-review-07: It is worth confirming the author's intent on point 5 if the author is available.
- code-review-08: APScheduler and Celery beat are examples of in-process schedulers
- code-review-08: os.listdir, os.path.getmtime, and os.remove all raise on a race
- code-review-08: os.listdir order isn't sorted by age
- code-review-08: Once candidates exceed 500 in a single run, the script deletes an arbitrary 500 files rather than the oldest 500
- code-review-08: If the directory backlog grows faster than 500 files per run, cleanup may never catch up on the true oldest files
- code-review-08: The stale-CUTOFF bug is the issue most likely to silently break the retention policy in production
- debugging-02: The code does not throw an error.
- debugging-02: The code runs and prints NaN.
- debugging-04: Adding `errors="ignore"` to `open` is an alternative to `errors="replace"`.
- debugging-04: Opening a file in binary mode with `open(path, "rb")` avoids decoding and thus encoding errors.
- debugging-04: Iterating over a file opened in binary mode yields lines, allowing a byte-level line count.
- debugging-05: Setting the default to None and building the list inside the function copies DEFAULT_TAGS instead of mutating the shared default.
- debugging-05: With the fix, state never leaks between calls or tests.
- debugging-06: The pool exhaustion is caused by contention for database connections, not by a bug in the export job itself.
- debugging-06: The export job experiences 30-second waits for connections.
- debugging-06: Batch 1148 was retried, adding a second request right after the first timeout.
- debugging-06: The retry of batch 1148 compounds the contention rather than easing it.
- debugging-06: The failure occurred in the window 02:14:07–02:14:41.
- debugging-06: Analytics service logs and DB server logs are available for the failure window.
- debugging-06: The export job can be run alongside a synthetic analytics workload in staging to attempt to reproduce the exhaustion.
- debugging-07: Reusing fixture-scoped IDs across workers can cause events to collide between workers.
- debugging-07: If seeding uses one DB connection or transaction and the digest read uses another, the read may not see uncommitted or recently committed rows.
- debugging-07: Dirty read protection under load can cause a data visibility race rather than a business-logic bug.
- debugging-07: A local reproduction loop is worth far more than CI logs.
- debugging-07: `pytest-xdist` does not isolate external resources by default.
- debugging-07: A single flaky run with diagnostic logging enabled will usually make the cause obvious.
- debugging-08: Two independent memory leaks are the likeliest explanation for the observed behavior.
- debugging-08: One of the two suspected leaks scales with webhook volume.
- debugging-08: The other suspected leak runs even with zero webhook traffic.
- debugging-08: The canary's growth proves a leak exists that is independent of webhook traffic.
- debugging-08: The correlation with marketing campaigns proves a traffic-scaling leak exists.
- debugging-08: The canary shows slower but nonzero memory growth.
- debugging-08: Thread-local state in pooled threads is a classic cause of per-request objects that never release.
- debugging-08: A webhook handler can set a thread-local that a pooled thread later reuses without clearing it.
- debugging-08: MDC context, request-scoped caches, and security principals are examples of thread-local state.
- debugging-08: An uncleared thread-local value chain grows with request count and never shrinks overnight.
- debugging-08: `jmap -histo:live` produces a heap histogram.
- debugging-08: Comparing heap histograms taken a day apart can reveal a ThreadLocal-backed class growing in lockstep with request count.
- debugging-08: Each `ThreadLocal.set(...)` call should have a matching `remove()` in a `finally` block.
- debugging-08: Old metric keys are rarely evicted.
- debugging-08: Most metrics libraries expose their registry size.
- debugging-08: A steadily rising metric label count during a campaign confirms a high-cardinality metrics leak.
- debugging-08: A background or scheduled task leak is independent of webhook traffic.
- debugging-08: Health checks, polling jobs, and connection-pool keep-alives run on the canary as well as production.
- debugging-08: Anything background jobs leak shows up even without webhook traffic.
- debugging-08: Disabling scheduled jobs one at a time and taking heap histograms before and after can isolate which job causes the growth.
- debugging-08: `jstack` can be used to periodically observe thread counts on the canary.
- debugging-08: Evicted cache entries can still leak memory if they retain references elsewhere.
- debugging-08: An eviction listener that fails to close a resource causes a per-entry resource leak.
- debugging-08: If cache entry count is flat but the cache's dominator-tree retained heap grows, the eviction listener is the prime suspect.
- debugging-08: Off-heap or native memory growth is invisible without a heap profile.
- debugging-08: Direct buffers from Netty or HTTP clients can grow independently of the JVM heap.
- debugging-08: Metaspace from dynamically generated classes or lambdas can grow independently of heap and survive GC.
- debugging-08: A large and growing gap between heap-reported usage and RSS points to off-heap memory.
- debugging-08: `-XX:NativeMemoryTracking=summary` enables Native Memory Tracking.
- debugging-08: `jcmd VM.native_memory` snapshots can be diffed across time.
- debugging-08: The fastest next step is a daily `jmap -histo:live` diff on both the canary and a production instance.
- debugging-08: Comparing the accumulating class between canary and production reveals whether there is one leak or two.
- explanation-01: Open addressing is used where cache performance matters most, such as high-performance C++ hash tables.
- explanation-01: absl::flat_hash_map is an example of a high-performance C++ hash table that uses open addressing.
- explanation-02: An e-commerce product table can have a `version` column used for optimistic locking.
- explanation-02: When Employee A saves a price change, the database bumps the row's `version` from 3 to 4.
- explanation-02: Employee B, still holding `version = 3`, fails to save because the row is now at `version = 4`.
- explanation-02: After a failed optimistic-locking write, Employee B reloads and retries.
- explanation-02: Optimistic locking fits systems with many reads and few actual write collisions.
- explanation-02: In a bank transfer, the system locks both account rows with `SELECT ... FOR UPDATE`.
- explanation-02: Locking both account rows prevents a concurrent transfer from reading a stale balance and causing a lost update.
- explanation-02: Financial transactions, inventory decrements, and ticket booking are examples of systems suited to pessimistic locking.
- explanation-03: Early TCP implementations sent data at whatever rate the sender's buffer allowed.
- explanation-03: Slow start was introduced by Van Jacobson in 1988.
- explanation-03: Every segment in a window generates an acknowledgment.
- explanation-04: Threads can clobber each other's state if not synchronized.
- explanation-04: Inter-process communication includes pipes, sockets, and serialization.
- explanation-04: I/O-bound tasks waiting on network or disk are an example of work suited to threads.
- explanation-05: The garbage collector walks the graph of references starting from roots.
- explanation-05: Roots include global variables and active stack frames.
- explanation-05: Data closed over by an unregistered listener often outlives the component or request that created it.
- explanation-06: If the slowdown is lock contention, a cache does not help.
- explanation-06: A cache introduces stale data.
- explanation-06: A cache introduces cache invalidation bugs.
- explanation-06: A cache adds another system to operate and monitor.
- explanation-06: Slow query logs show whether a database bottleneck comes from a few expensive queries or from high read volume.
- explanation-06: Indexing can fix a few expensive queries more simply than caching can.
- explanation-07: It is worth choosing a shard key now even if you don't shard now.
- explanation-07: Retrofitting a shard key later is the expensive part.
- explanation-07: The decision to shard depends on growth rate, not just whether growth exists.
- explanation-07: Current row-count growth per month or expected user growth are rougher proxies that can be used to extrapolate growth.
- explanation-07: Migrating a live system from unsharded to sharded is far harder than starting sharded, especially under write pressure.
- explanation-07: Even an order-of-magnitude growth estimate changes the answer to whether to shard.
- explanation-08: Both unmeasured factors can push the answer anywhere from negligible to dramatic
- explanation-08: Payload size and structure determine the speedup
- explanation-08: If serialization is 40% of the time, a 10x gain is huge
- explanation-08: Guessing either number risks underselling a real win
- explanation-08: Prototyping the binary format on the three or four largest or most frequent payload types allows direct comparison of serialized size and round-trip time
- explanation-08: These measurements usually take a day or two of work
- explanation-08: A day or two of measurement work is far cheaper than committing to the migration blind
- summarization-01: Plugin loading was deferred until it is needed.
- summarization-01: Deferring plugin loading is the cause of the faster app startup.
- summarization-02: Staging deliberately uses smaller configuration values than production.
- summarization-02: The checklist should ideally also check other environment-specific values.
- summarization-04: The bug was reproduced on two different machines.
- summarization-05: Ada is assigned to run the payments database migration dry run.
- summarization-06: There is no evidence yet for the retry storm hypothesis.
- summarization-07: Staging runs a newer kernel.
- summarization-08: The large-file upload finding is tentative but concerning.

### classic-concise

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 26 | 17 | 0.654 | 23 | 4 |
| code-review-02 | 19 | 13 | 0.684 | 14 | 1 |
| code-review-03 | 25 | 21 | 0.84 | 13 | 1 |
| code-review-04 | 14 | 9 | 0.643 | 15 | 0 |
| code-review-05 | 39 | 31 | 0.795 | 36 | 3 |
| code-review-06 | 30 | 17 | 0.567 | 39 | 10 |
| code-review-07 | 23 | 16 | 0.696 | 31 | 9 |
| code-review-08 | 42 | 26 | 0.619 | 31 | 11 |
| debugging-01 | 6 | 5 | 0.833 | 5 | 0 |
| debugging-02 | 14 | 10 | 0.714 | 8 | 0 |
| debugging-03 | 8 | 5 | 0.625 | 5 | 0 |
| debugging-04 | 11 | 8 | 0.727 | 10 | 0 |
| debugging-05 | 16 | 15 | 0.938 | 12 | 0 |
| debugging-06 | 27 | 15 | 0.556 | 24 | 6 |
| debugging-07 | 28 | 15 | 0.536 | 37 | 8 |
| debugging-08 | 40 | 15 | 0.375 | 35 | 19 |
| explanation-01 | 42 | 29 | 0.69 | 25 | 1 |
| explanation-02 | 32 | 23 | 0.719 | 18 | 0 |
| explanation-03 | 30 | 20 | 0.667 | 29 | 7 |
| explanation-04 | 31 | 23 | 0.742 | 30 | 5 |
| explanation-05 | 14 | 11 | 0.786 | 14 | 3 |
| explanation-06 | 17 | 6 | 0.353 | 14 | 3 |
| explanation-07 | 27 | 16 | 0.593 | 26 | 6 |
| explanation-08 | 14 | 7 | 0.5 | 10 | 2 |
| summarization-01 | 6 | 5 | 0.833 | 5 | 0 |
| summarization-02 | 13 | 13 | 1.0 | 13 | 3 |
| summarization-03 | 13 | 13 | 1.0 | 13 | 0 |
| summarization-04 | 13 | 10 | 0.769 | 11 | 0 |
| summarization-05 | 9 | 9 | 1.0 | 8 | 1 |
| summarization-06 | 15 | 15 | 1.0 | 12 | 0 |
| summarization-07 | 16 | 14 | 0.875 | 14 | 2 |
| summarization-08 | 25 | 23 | 0.92 | 19 | 1 |

Median fraction: 0.716 over 32 scored pairs.

Median additions: 1.5 over 32 scored pairs.

Lost facts:

- code-review-01: Swallowing all exceptions makes the mutable-default and missing-`db` bugs invisible.
- code-review-01: `roles.append("member")` mutates the list object the caller passed in, as a side effect.
- code-review-01: If the caller reuses that list elsewhere, it will unexpectedly contain "member".
- code-review-01: The function does not check whether "member" is already present in `roles`, which can produce duplicate entries.
- code-review-01: The suggested fix builds a new list with `[*roles, "member"]` instead of appending in place.
- code-review-01: The suggested fix makes `db` a required positional parameter with no default.
- code-review-01: The suggested fix catches `DatabaseError` rather than using a bare `except:`.
- code-review-01: The suggested fix calls `logger.exception` before returning `False`.
- code-review-01: `DatabaseError` is what is actually expected to be raised from a database call.
- code-review-02: The TypeError message is "Cannot read properties of undefined (reading 'name')".
- code-review-02: The `async` keyword serves no purpose in the original function.
- code-review-02: The unnecessary `async` keyword masks the fact that the function is not actually asynchronous in its logic.
- code-review-02: The code does not check that `data` has a `name` property before calling `.toUpperCase()` on it.
- code-review-02: The proposed fixed version throws an Error when `data.name` is missing.
- code-review-02: Callers of the fixed function should wrap calls in `try/catch` to handle thrown errors.
- code-review-03: `SELECT *` forces callers to guess column order and meaning from the return value instead of getting named fields.
- code-review-03: Invalid input types will produce a confusing SQL error or unexpected query behavior.
- code-review-03: If the `orders` table is large, `fetchall()` loads everything into memory at once.
- code-review-03: The missing docstring and type hints make the function harder to use correctly.
- code-review-04: The GIL protects individual bytecode operations, but not multi-step sequences like read-modify-write.
- code-review-04: The class is explicitly used from multiple threads.
- code-review-04: Reading `self.value` from outside while another thread is mid-increment is not guaranteed to see a consistent value.
- code-review-04: In CPython, inconsistent reads are not a significant problem for a simple int assignment.
- code-review-04: The class provides no defined or documented way to read the value safely.
- code-review-05: The unchecked cd failure combined with rm -rf is the most dangerous bug in the script.
- code-review-05: In some shells the no-match case just errors out silently.
- code-review-05: The `-f` flag to rm suppresses the "no such file" error.
- code-review-05: The script's quoting is inconsistent throughout.
- code-review-05: Using `set -eu` at the top would have caught the empty-variable and command-failure issues immediately.
- code-review-05: Quoting cd makes a cd failure abort the script instead of silently falling through.
- code-review-05: A glob will not match directories named `*.tmp` recursively.
- code-review-05: The `-r` flag on rm in the original script was a latent risk.
- code-review-06: When base[key] is a dict and override[key] is a non-dict, non-None value, merge_settings recurses into merge_settings(merged[key], value).
- code-review-06: That recursive call raises AttributeError when value.items() is called because value is not a mapping.
- code-review-06: merge_settings({"db": {"host": "x"}}, {"db": "disabled"}) crashes instead of replacing the dict.
- code-review-06: Values taken from override are assigned by reference via merged[key] = value rather than copied.
- code-review-06: Configs built programmatically and merged with themselves make self-references more plausible than they sound.
- code-review-06: When the base value is a dict and the override value is a scalar, merge_settings crashes.
- code-review-06: Only one of the three base/override type combinations behaves consistently with the rule 'override always wins, but dicts merge when both sides agree.'
- code-review-06: The base=scalar/override=dict behavior suggests the intended rule was 'override always wins, but dicts merge when both sides agree.'
- code-review-06: The code likely intended to fall through to a plain replace when value is not a dict, but omitted an isinstance(value, dict) check alongside isinstance(merged[key], dict).
- code-review-06: Overriding a dict-valued key with an empty dict is a no-op rather than a clear.
- code-review-06: merge_settings({"a": {"x": 1}}, {"a": {}}) returns {"a": {"x": 1}} unchanged.
- code-review-06: The project has no test suite.
- code-review-06: The dict-override crash and the shared mutable state issue are the problems most likely to cause production failures.
- code-review-07: withRetry has three distinct outcomes collapsed into two ambiguous return values.
- code-review-07: If a non-Error value such as null is thrown, reading err.status raises a TypeError.
- code-review-07: In the throw null case, accessing err.status throws inside the catch handler, producing an unhandled rejection instead of the intended fallback.
- code-review-07: On the last allowed iteration, a 429 still triggers the full setTimeout delay before the loop exits and the function returns.
- code-review-07: withRetry never throws and always returns a sentinel value.
- code-review-07: withRetry treats all 5xx responses as retryable and all other errors as fatal.
- code-review-07: The attempts parameter means total attempts rather than retries after the first try.
- code-review-08: No relevant memory was found for this project.
- code-review-08: os.path.getmtime raises FileNotFoundError on broken symlinks.
- code-review-08: The 'removed < 500' check is evaluated before the deletion it guards, not after.
- code-review-08: Because the check runs before the deletion, the actual cap is 501 rather than 500.
- code-review-08: When the function aborts, 'removed' is left undefined to the caller and the rest of the directory is unprocessed.
- code-review-08: The files the script deletes have unclear provenance and the scheduling is unset.
- code-review-08: The script performs no path validation.
- code-review-08: There is no comment explaining the assumption that tmp/part files are always disposable.
- code-review-08: CUTOFF is computed once at import time rather than per call.
- code-review-08: Computing CUTOFF at import time is fine for a single-shot scheduled invocation.
- code-review-08: If the module is imported into a long-running process and clean() is called repeatedly, the cutoff goes stale.
- code-review-08: The code contains the expression 86400 * 45, which corresponds to a 45-day retention window.
- code-review-08: 45 is a clean round number and plausibly reflects a real retention policy.
- code-review-08: Deleting tmp-/.part files unconditionally regardless of age makes sense if those files are always safe to remove immediately.
- code-review-08: The off-by-one on the cap is likely accidental.
- code-review-08: Issues #1, #3, #4, and #5 have no plausible reason to be intentional.
- debugging-01: The corrected get_url function returns f"http://{cfg['host']}:{cfg['port']}/api".
- debugging-02: Class bodies run in strict mode.
- debugging-02: When `this` is `undefined`, `this.seconds += 1` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: `setInterval(function () {...}.bind(this), 1000)` is an alternative fix that keeps a regular function.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-03: `i=2` would produce the last window `[3, 4]`.
- debugging-03: `moving_sum` returns the sum of each window of the given size.
- debugging-03: `moving_sum([1, 2, 3, 4], 2)` returns `[3, 5, 7]`.
- debugging-04: The code forces the `ascii` codec.
- debugging-04: `utf-8-sig` should be used instead if the file may have a BOM.
- debugging-04: `chardet` and `charset-normalizer` can be used to detect a file's encoding.
- debugging-05: With the sentinel fix, callers who pass their own list will still have that list mutated by `append`.
- debugging-06: The reported failure symptom is a "pool exhausted" error.
- debugging-06: Variable batch numbers rule out a specific bad row as the cause.
- debugging-06: The failures recur approximately weekly.
- debugging-06: A second leading candidate cause is a slow connection leak in the export worker itself.
- debugging-06: A connection leak would explain the non-deterministic failures because it depends on the error rate during a given session.
- debugging-06: Failures caused by a connection leak tend to cluster near the end of long runs.
- debugging-06: A less likely cause is a pool size configured too small for the combined peak concurrency of both services.
- debugging-06: Another less likely cause is a periodic DB-side resource spike (backup, autovacuum, or replication lag) that slows all queries at once.
- debugging-06: The problem cannot currently be reproduced on demand.
- debugging-06: A failure occurred on 2026-07-29 at roughly 02:13–02:14.
- debugging-06: The relevant window to inspect is roughly 30 seconds before each timeout.
- debugging-06: Additional incident logs could show whether all failures land in the same few-minute window.
- debugging-07: Async work that can delay queryability includes background jobs, message queues, and search indexes such as Elasticsearch or OpenSearch.
- debugging-07: Under CI's 4x concurrency, workers compete for CPU and DB connections.
- debugging-07: The digest implementation should be grepped for implicit scoping or limits such as LIMIT, ORDER BY created_at DESC with a cap, or a time window not strictly filtered by the test's user or tenant ID.
- debugging-07: If the test fails locally under -n4 but not -n1, that confirms parallelism rather than CI machine slowness is the trigger.
- debugging-07: Confirming parallelism as the trigger separates hypothesis 1 from hypotheses 2, 3, and 4.
- debugging-07: Temporary instrumentation should log event IDs and timestamps returned by the API versus those returned by the digest, plus the worker ID that created them.
- debugging-07: The CI setup keeps no artifacts.
- debugging-07: Instrumentation output can be redirected to a file uploaded as an explicit CI artifact for just this test, or inspected by running locally in a loop with -n4.
- debugging-07: A poll or retry on the assertion should be tried in a scratch branch rather than committed.
- debugging-07: Worker count can be bisected by temporarily running -n2 and -n3 in CI.
- debugging-07: If the failure rate scales with worker count rather than staying constant, that points to shared-resource contention rather than pure timing.
- debugging-07: Steps 1 and 2 are static or config checks that need no CI cycles.
- debugging-07: The recommended order is to start with steps 1 and 2, then use step 3 to confirm before spending time on instrumentation.
- debugging-08: Traffic-correlated growth plus growth on the no-webhook canary points to something scaling with all request traffic rather than only webhooks
- debugging-08: If growth-rate per request is roughly constant across canary and normal instances, unbounded per-request growth is the prime suspect
- debugging-08: In-memory structures keyed by unbounded cardinality such as customer ID, order ID, request ID, or campaign ID can cause unbounded growth
- debugging-08: Product objects can grow over time as more fields, variants, or images are added
- debugging-08: Multiple cache instances (per-thread or per-connection) can each be individually bounded while multiplying without bound
- debugging-08: If process memory still grows when a second cache is given a deliberately tiny bound, the cache is not the primary cause
- debugging-08: An LRU eviction policy implemented with a lock that is sometimes bypassed may fail to fire
- debugging-08: Eviction that triggers only on insert leaves expired-but-present entries uncleaned during lookups
- debugging-08: Memory growth that survives quiet nights is also consistent with heap fragmentation from allocator behavior
- debugging-08: Variable-size allocations such as product payloads of differing sizes can fragment the heap
- debugging-08: Heap fragmentation can prevent freed memory from being returned to the OS or reused efficiently
- debugging-08: RSS never drops in the observed service
- debugging-08: Fragmentation would explain RSS never dropping even when logical memory usage does
- debugging-08: Go exposes heap_alloc and heap_live statistics that can be compared against RSS
- debugging-08: C and C++ expose malloc_stats and jemalloc statistics for allocator accounting
- debugging-08: JVM and .NET expose GC heap statistics for allocator accounting
- debugging-08: Flat live-object memory combined with climbing RSS indicates fragmentation rather than a leak
- debugging-08: Fragmentation requires a different fix than a leak, such as a compacting GC or a different allocator
- debugging-08: Periodic restart is a reasonable mitigation for fragmentation
- debugging-08: If a forced GC or compaction does not reduce RSS, the retention is OS-level rather than application-level
- debugging-08: Campaign flows may pull in a wider or rarer product catalog, producing more distinct product IDs
- debugging-08: More distinct product IDs would produce more distinct cache entries or one-off allocations
- debugging-08: Campaigns may trigger specific code paths such as promotions or coupon rules that leak
- debugging-08: Unusually high distinct-entity cardinality during campaigns would implicate cache-key cardinality rather than the cache size bound
- debugging-08: A single pprof or heap dump comparison between start and end of week would settle whether the issue is a leak or fragmentation
- explanation-01: The data structure in a separate chaining bucket is usually a linked list, and sometimes a tree.
- explanation-01: Deletion in separate chaining is straightforward because it just removes the node from the list.
- explanation-01: Linear probing tries successive slots at index + 1, index + 2, and so on.
- explanation-01: Quadratic probing jumps by increasing steps such as index + 1, index + 4, index + 9.
- explanation-01: Quadratic probing reduces clustering.
- explanation-01: Double hashing uses a second hash function to compute the step size.
- explanation-01: Deletion in open addressing is trickier because emptying a slot might break the probe chain for other keys.
- explanation-01: Open addressing implementations typically use a special tombstone marker for deleted entries.
- explanation-01: Open addressing requires careful resizing (rehashing) well before the table gets full, often at around 70% load.
- explanation-01: Deletion is easy in chaining and needs tombstones in open addressing.
- explanation-01: Most standard library implementations use chaining.
- explanation-01: Java's HashMap often converts a bucket's list to a balanced tree if it grows too large.
- explanation-01: Converting a bucket's list to a balanced tree is a hybrid approach that protects against worst-case performance from many collisions.
- explanation-02: `SELECT * FROM accounts WHERE id = 1 FOR UPDATE;` is an example of pessimistic locking in Postgres and MySQL.
- explanation-02: Pessimistic locking fits when the cost of retrying a failed operation is high.
- explanation-02: Inventory decrements at checkout for a hot-selling item are an example of a workload suited to pessimistic locking.
- explanation-02: `UPDATE documents SET content = ?, version = version + 1 WHERE id = ? AND version = ?;` is an example optimistic locking statement.
- explanation-02: Many ORMs implement optimistic locking.
- explanation-02: Hibernate implements optimistic locking with `@Version`.
- explanation-02: EF Core implements optimistic locking with concurrency tokens.
- explanation-02: Collaborative editing is an example use case for optimistic locking.
- explanation-02: Most CRUD web apps are an example use case for optimistic locking, because two users editing the same record simultaneously is uncommon.
- explanation-03: A network path may be a fast local link or a congested transatlantic route through many routers.
- explanation-03: Dropped packets cause retransmissions, wasted bandwidth, and worse performance for everyone sharing the link.
- explanation-03: The problem of retransmissions and degraded performance from dropped packets is known as congestion collapse.
- explanation-03: Congestion collapse was a real problem on the early internet in the late 1980s.
- explanation-03: TCP slow start is one of the original congestion control mechanisms.
- explanation-03: Historically the initial cwnd was 1 segment.
- explanation-03: The initial cwnd is now often around 10 segments.
- explanation-03: The initial window of about 10 segments is specified in RFC 6928.
- explanation-03: A larger initial window speeds up short connections.
- explanation-03: In congestion avoidance, the window grows linearly instead of exponentially.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own register state.
- explanation-04: Independent process restart is useful for workers that leak memory over time or that crash.
- explanation-04: Erlang/OTP-style 'let it crash' supervision is based on independent process lifecycle and restart.
- explanation-04: Gunicorn and Nginx worker processes are based on independent process lifecycle and restart.
- explanation-04: Process-based designs using separate services communicating over IPC or network generalize naturally to distributed systems.
- explanation-04: Threads only work within a single machine's shared memory.
- explanation-04: A web server handling many connections that share an in-memory cache is an example where threads win.
- explanation-05: Event emitters, DOM elements, and global services are examples of long-lived objects that listeners can be registered on.
- explanation-05: A listener holds a reference to its enclosing scope, including large objects it captured.
- explanation-05: A listener keeps its enclosing scope reachable for as long as the emitter lives.
- explanation-06: With a cache in place, writes still have to hit the database.
- explanation-06: Adding a cache means writes must also update or invalidate the cache.
- explanation-06: A cache does not help when requests are mostly unique reads.
- explanation-06: When data is not reused, a cache mostly misses and adds overhead without benefit.
- explanation-06: Possible non-database bottlenecks include slow application code, network latency, N+1 query problems, missing indexes, and external API calls.
- explanation-06: Request time could be spent in the database, in serialization, or in a slow downstream call.
- explanation-06: In a write-heavy workload, a cache adds complexity and can slow things down due to the extra layer to update and invalidate.
- explanation-06: Profiling slow requests can be done with timing logs or an APM tool.
- explanation-06: Some databases have a slow query log.
- explanation-06: A database's slow query log often points directly at missing indexes or expensive queries.
- explanation-06: A rough read/write ratio can be obtained from a manual count of logs over an hour.
- explanation-07: A product team being unable to say how much growth to expect indicates the access pattern is not yet well understood.
- explanation-07: Write throughput and replication lag serve as leading indicators of approaching a scaling ceiling.
- explanation-07: Postgres supports native declarative partitioning.
- explanation-07: Tables can be partitioned by date or by tenant.
- explanation-07: Native declarative partitioning costs little to adopt.
- explanation-07: Partitioning now makes a later shard split easier because the data is already logically separated.
- explanation-07: Re-sharding later is far more painful than sharding late.
- explanation-07: Growth across tenants often turns out uneven, with some tenants very large and most very small.
- explanation-07: Rebalancing shards under uneven growth becomes an ongoing operational cost.
- explanation-07: Sharding before there is evidence it is needed means paying the rebalancing cost prematurely.
- explanation-07: The recommended investment now is partitioning, read replicas, and monitoring the real bottleneck rather than disk size.
- explanation-08: JSON encode/decode accounting for about 2% of request latency is common when network, database, or business logic dominate.
- explanation-08: If JSON encode/decode is 2% of request latency, a 10x faster serializer yields roughly a 1.8% overall improvement.
- explanation-08: Binary formats such as protobuf and msgpack typically reduce payload size by 30-70% compared to JSON.
- explanation-08: Payload size reduction helps less when payloads are small or already compressed.
- explanation-08: Gzip compression significantly narrows the payload size gap between JSON and binary formats.
- explanation-08: Serialization exceeding 10-15% of request latency counts as a meaningful chunk.
- explanation-08: Prototyping a binary format on one endpoint surfaces migration costs such as schema management, debuggability, and client compatibility.
- summarization-01: Cold start time was reduced by approximately 40%.
- summarization-04: The Export button offers both a PDF option and a CSV option.
- summarization-04: After clicking the PDF export option, nothing happens initially.
- summarization-04: The bug was reproduced on the latest version of Firefox.
- summarization-07: The recommendation is to profile memory before drawing conclusions on tail latency or stability.
- summarization-07: The recommendation is to test under production-like traffic before drawing conclusions on tail latency or stability.
- summarization-08: It is firm that the progress bar behavior is a problem.
- summarization-08: Whether the fix should be visual or technical needs more investigation.

Added facts (styled only):

- code-review-01: The proposed fix uses `roles=None` as the default and builds the list inside the function with `list(roles) if roles else []`.
- code-review-01: The proposed fix raises `ValueError("name is required")` when `name` is falsy.
- code-review-01: The proposed fix raises `ValueError("db is required")` when `db` is `None`.
- code-review-01: The caller should handle exceptions rather than the function masking them.
- code-review-02: Because the fetch chain is not awaited, the promise result is discarded.
- code-review-03: `SELECT *` retrieves data that is not needed.
- code-review-05: If no `.tmp` files exist, most shells leave the `*.tmp` glob unexpanded.
- code-review-05: `echo` with unquoted user input can misbehave if the value starts with `-`.
- code-review-05: Using `--` before a filename argument prevents the value from being interpreted as an option.
- code-review-06: The shallow copy is not a bug in the current code because the recursive call does not mutate its input.
- code-review-06: If `base[key]` is a dict but `override[key]` is not, `merge_settings` is never called, which is correct.
- code-review-06: The list-replacement behavior is probably intentional and probably fine, but undocumented.
- code-review-06: Keys deleted via `None` never reappear.
- code-review-06: `merged`'s key order depends on `base`'s order plus new keys from `override`.
- code-review-06: Unpredictable key ordering is not a bug.
- code-review-06: Key ordering is fine for dicts but could matter if the result feeds something order-sensitive.
- code-review-06: Passing a non-dict `base` or `override` throws an `AttributeError` on `.items()`.
- code-review-06: `dict(base)` fails with a less obvious error if `base` is not iterable as key-value pairs.
- code-review-06: The recommendation is to add a docstring capturing the `None`-deletes convention and the merge-versus-overwrite rule.
- code-review-07: A plain network error has no `.status` field.
- code-review-07: The original error is discarded — it is not logged or attached anywhere.
- code-review-07: Returning `null` without documentation is dangerous because every caller must remember to check for `null`.
- code-review-07: TypeScript/JSDoc give no hint that the function can return `null`.
- code-review-07: 5xx failures are retried with zero delay.
- code-review-07: The retry logic has no maximum delay cap.
- code-review-07: The lack of jitter and delay cap is acceptable for a small `attempts` count.
- code-review-07: A high `attempts` value set by an unseen caller creates thundering-herd or multi-second-hang risk.
- code-review-07: The most likely real defect is that errors with no `.status` are treated the same as a definitive non-retryable failure.
- code-review-08: A file being written that matches the `tmp-*` or `.part` pattern can be deleted while another process still has it open.
- code-review-08: The unconditional deletion of in-flight temp files is a race condition and the script's biggest bug.
- code-review-08: The script is destructive, scheduled, and runs in production.
- code-review-08: The script's `removed` return value goes nowhere unless the caller logs it.
- code-review-08: `ROOT` is not verified to exist or be mounted.
- code-review-08: If the export volume is not mounted at cron time, `os.listdir` throws.
- code-review-08: That `os.listdir` failure is silent unless something wraps the call.
- code-review-08: `os.listdir` iteration order is not guaranteed.
- code-review-08: Which files survive when near the 500-file cap is arbitrary rather than oldest-first.
- code-review-08: Temp-file deletion should also check an age threshold, such as only deleting files older than an hour.
- code-review-08: The recommended fix order is: gate temp-file deletion on age, add per-file try/except, skip non-regular files, and log every removal.
- debugging-06: If a pool is sized for the export alone, any overlap with another service exhausts it.
- debugging-06: The WARN log shows a retry on attempt 2.
- debugging-06: If many batches retry simultaneously after a timeout, they compound the contention that caused the first failure.
- debugging-06: pg_stat_activity includes a wait_event field.
- debugging-06: Separating the pools or setting per-service max connections is a low-risk experiment.
- debugging-06: If failures stop after separating the pools, contention is confirmed as the cause.
- debugging-07: Without isolation, another test's cleanup or setup can delete or overwrite one of the three events.
- debugging-07: A shared clock or ID sequence is a possible cause.
- debugging-07: Two workers' events can collide under a shared clock or ID sequence.
- debugging-07: A truncated or second-resolution clock can put the third event just outside the digest window.
- debugging-07: Under contention, one event drops out due to clock or ID sequence issues.
- debugging-07: The suite should be run serially in CI 50-100 times to confirm the issue is parallelism-related.
- debugging-07: The serial run should use the same CI environment rather than a dev machine.
- debugging-07: 'CI parallel / dev serial' is the only known variable.
- debugging-08: There are two leaks, not one.
- debugging-08: The traffic-correlated growth and the baseline growth point to different causes.
- debugging-08: One leak is traffic-driven and follows the webhook path.
- debugging-08: The canary grows slower than webhook-serving instances.
- debugging-08: Possible causes of the traffic-driven leak include a listener, timer, or connection not cleaned up during webhook handling.
- debugging-08: Diffing live heap histograms between a webhook-heavy instance and the canary at the same uptime is a way to check the traffic-driven leak.
- debugging-08: In that histogram diff, one should look for a class whose instance count scales with request count rather than with cache size.
- debugging-08: The second leak is a baseline leak present even on the canary.
- debugging-08: Possible causes of the baseline leak include background jobs, scheduled tasks, connection pools, or metrics/logging buffers that never trim.
- debugging-08: Watching the canary heap overnight with GC forced is a way to check the baseline leak.
- debugging-08: If RSS or heap still climbs with zero webhook traffic, heap snapshots taken 12 hours apart on the canary should be diffed to find the growing class.
- debugging-08: The cache bound has been unchanged for a year.
- debugging-08: An unchanged bound for a year is weak evidence that the cache is not the cause.
- debugging-08: One such bug is a key that never matches on eviction.
- debugging-08: Another such bug is a memory leak in the values the cache references even after eviction.
- debugging-08: The suggestion is to take two heap dumps on the canary, at start of day and end of day, with forced GC before each.
- debugging-08: The suggestion is to diff the dominator tree of the two heap dumps.
- debugging-08: Diffing the dominator tree will directly show the actual growing type.
- debugging-08: Diffing the dominator tree will turn steps 1 through 3 from guesses into a confirmed root cause in one pass.
- explanation-01: Rust's HashMap uses open addressing.
- explanation-03: A new TCP connection does not know the queue depths of routers on the path.
- explanation-03: Every packet in the window gets acknowledged.
- explanation-03: On packet loss, TCP cuts the congestion window drastically.
- explanation-03: On packet loss, TCP switches to congestion avoidance, a slower and more careful growth phase.
- explanation-03: ssthresh is a threshold set from a past congestion event.
- explanation-03: Slow start is the mechanism that lets millions of independent connections share the internet's bandwidth.
- explanation-03: Sharing of internet bandwidth across connections happens without any central coordinator.
- explanation-04: Threads in the same process run independently.
- explanation-04: Processes communicate through explicit channels such as pipes, sockets, shared memory segments, or files.
- explanation-04: Concurrent access to shared variables without synchronization causes race conditions.
- explanation-04: Kubernetes pods and Unix daemons are examples of independently scaled and restarted processes.
- explanation-04: Go, Rust, Java, and C++ are languages without a GIL bottleneck.
- explanation-05: A leak grows as long as the stray reference persists.
- explanation-05: A subscribed handler holds a reference to its target object.
- explanation-05: Failing to unsubscribe a handler keeps its target object reachable for the listener's lifetime.
- explanation-06: A cache brings new risks: stale data, invalidation bugs, and another system to operate.
- explanation-06: The read/write ratio should be measured on the endpoints that feel slow.
- explanation-06: Adding a missing index is a smaller change with less risk than adding a cache.
- explanation-07: Scaling vertically is a configuration change rather than an architecture change.
- explanation-07: Sharding prematurely can consume months of team time on infrastructure the product does not yet need, delaying feature work.
- explanation-07: Concrete triggers to revisit sharding are sustained write latency degradation despite tuning, or storage approaching what a single reasonably-sized instance can hold.
- explanation-07: A rough growth curve should be requested from the product team.
- explanation-07: 10x growth in a year is a different conversation than 10x growth in five years.
- explanation-07: A product team being unable to say how much growth to expect is itself information indicating the threshold is not near.
- explanation-08: Payload size matters more than parse speed when an application is bandwidth-bound or latency-bound.
- explanation-08: Per-request savings multiplied by request volume indicates whether a migration is worth its cost.
- summarization-02: The connection pool became exhausted.
- summarization-02: The connection pool exhaustion caused checkout errors.
- summarization-02: 12% of requests experienced checkout errors.
- summarization-05: Ada is assigned to run the payments database migration dry run.
- summarization-07: The worker crash may be attributable to staging's newer kernel.
- summarization-07: Staging runs a newer kernel.
- summarization-08: The claim that the progress bar causes abandonment on large files is tentative.

### concise

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 26 | 20 | 0.769 | 21 | 2 |
| code-review-02 | 19 | 13 | 0.684 | 10 | 0 |
| code-review-03 | 25 | 15 | 0.6 | 14 | 1 |
| code-review-04 | 14 | 10 | 0.714 | 20 | 0 |
| code-review-05 | 39 | 31 | 0.795 | 38 | 4 |
| code-review-06 | 30 | 21 | 0.7 | 32 | 6 |
| code-review-07 | 23 | 15 | 0.652 | 36 | 13 |
| code-review-08 | 42 | 35 | 0.833 | 31 | 7 |
| debugging-01 | 6 | 5 | 0.833 | 5 | 0 |
| debugging-02 | 14 | 10 | 0.714 | 8 | 0 |
| debugging-03 | 8 | 5 | 0.625 | 6 | 0 |
| debugging-04 | 11 | 8 | 0.727 | 11 | 0 |
| debugging-05 | 16 | 13 | 0.812 | 13 | 1 |
| debugging-06 | 27 | 19 | 0.704 | 32 | 6 |
| debugging-07 | 28 | 15 | 0.536 | 29 | 9 |
| debugging-08 | 40 | 16 | 0.4 | 39 | 17 |
| explanation-01 | 42 | 34 | 0.81 | 33 | 4 |
| explanation-02 | 32 | 26 | 0.812 | 20 | 4 |
| explanation-03 | 30 | 23 | 0.767 | 27 | 2 |
| explanation-04 | 31 | 22 | 0.71 | 37 | 7 |
| explanation-05 | 14 | 13 | 0.929 | 9 | 0 |
| explanation-06 | 17 | 8 | 0.471 | 15 | 6 |
| explanation-07 | 27 | 20 | 0.741 | 22 | 5 |
| explanation-08 | 14 | 4 | 0.286 | 10 | 0 |
| summarization-01 | 6 | 4 | 0.667 | 5 | 0 |
| summarization-02 | 13 | 8 | 0.615 | 11 | 3 |
| summarization-03 | 13 | 12 | 0.923 | 12 | 0 |
| summarization-04 | 13 | 13 | 1.0 | 13 | 1 |
| summarization-05 | 9 | 9 | 1.0 | 8 | 0 |
| summarization-06 | 15 | 14 | 0.933 | 12 | 0 |
| summarization-07 | 16 | 14 | 0.875 | 15 | 3 |
| summarization-08 | 25 | 22 | 0.88 | 19 | 1 |

Median fraction: 0.734 over 32 scored pairs.

Median additions: 1.5 over 32 scored pairs.

Lost facts:

- code-review-01: Swallowing all exceptions makes the mutable-default and missing-`db` bugs invisible.
- code-review-01: The suggested fix builds a new list with `[*roles, "member"]` instead of appending in place.
- code-review-01: The suggested fix makes `db` a required positional parameter with no default.
- code-review-01: The suggested fix catches `DatabaseError` rather than using a bare `except:`.
- code-review-01: The suggested fix calls `logger.exception` before returning `False`.
- code-review-01: `DatabaseError` is what is actually expected to be raised from a database call.
- code-review-02: The TypeError message is "Cannot read properties of undefined (reading 'name')".
- code-review-02: A 404 or 500 response with a JSON error body would be parsed as if it were valid profile data.
- code-review-02: The unnecessary `async` keyword masks the fact that the function is not actually asynchronous in its logic.
- code-review-02: The code does not check that `data` has a `name` property before calling `.toUpperCase()` on it.
- code-review-02: The proposed fixed version throws an Error when `data.name` is missing.
- code-review-02: Callers of the fixed function should wrap calls in `try/catch` to handle thrown errors.
- code-review-03: The sqlite3 driver uses `?` placeholders instead of `%s`.
- code-review-03: `SELECT *` forces callers to guess column order and meaning from the return value instead of getting named fields.
- code-review-03: Invalid input types will produce a confusing SQL error or unexpected query behavior.
- code-review-03: `cursor.execute` and `fetchall` can raise exceptions, for example from a bad connection or an invalid status value.
- code-review-03: The code calls `fetchall()` on unbounded results.
- code-review-03: If the `orders` table is large, `fetchall()` loads everything into memory at once.
- code-review-03: There is no pagination or limit on the query results.
- code-review-03: The function has no docstring and no type hints.
- code-review-03: The function signature does not indicate the expected types of `cursor`, `customer_name`, or `status`, nor the return type.
- code-review-03: The missing docstring and type hints make the function harder to use correctly.
- code-review-04: The class is explicitly used from multiple threads.
- code-review-04: Reading `self.value` from outside while another thread is mid-increment is not guaranteed to see a consistent value.
- code-review-04: In CPython, inconsistent reads are not a significant problem for a simple int assignment.
- code-review-04: The class provides no defined or documented way to read the value safely.
- code-review-05: The unchecked cd failure combined with rm -rf is the most dangerous bug in the script.
- code-review-05: In some shells the no-match case just errors out silently.
- code-review-05: The `-f` flag to rm suppresses the "no such file" error.
- code-review-05: The script's quoting is inconsistent throughout.
- code-review-05: Using `set -eu` at the top would have caught the empty-variable and command-failure issues immediately.
- code-review-05: Quoting cd makes a cd failure abort the script instead of silently falling through.
- code-review-05: A glob will not match directories named `*.tmp` recursively.
- code-review-05: The `-r` flag on rm in the original script was a latent risk.
- code-review-06: Values taken from override are assigned by reference via merged[key] = value rather than copied.
- code-review-06: Configs built programmatically and merged with themselves make self-references more plausible than they sound.
- code-review-06: Only one of the three base/override type combinations behaves consistently with the rule 'override always wins, but dicts merge when both sides agree.'
- code-review-06: The base=scalar/override=dict behavior suggests the intended rule was 'override always wins, but dicts merge when both sides agree.'
- code-review-06: Overriding a dict-valued key with an empty dict is a no-op rather than a clear.
- code-review-06: merge_settings({"a": {"x": 1}}, {"a": {}}) returns {"a": {"x": 1}} unchanged.
- code-review-06: Merging with an empty override dict has nothing to apply.
- code-review-06: The project has no test suite.
- code-review-06: Characterization tests are cheap to write and pin down what correct behavior means before refactoring.
- code-review-07: withRetry has three distinct outcomes collapsed into two ambiguous return values.
- code-review-07: Nothing in the code documents or uses the distinction between the null and undefined return values.
- code-review-07: If a non-Error value such as null is thrown, reading err.status raises a TypeError.
- code-review-07: In the throw null case, accessing err.status throws inside the catch handler, producing an unhandled rejection instead of the intended fallback.
- code-review-07: On the last allowed iteration, a 429 still triggers the full setTimeout delay before the loop exits and the function returns.
- code-review-07: withRetry never throws and always returns a sentinel value.
- code-review-07: withRetry treats all 5xx responses as retryable and all other errors as fatal.
- code-review-07: HTTP status 501 is a 5xx status that is not actually retryable.
- code-review-08: No relevant memory was found for this project.
- code-review-08: os.path.getmtime works on directories.
- code-review-08: os.path.getmtime raises FileNotFoundError on broken symlinks.
- code-review-08: The files the script deletes have unclear provenance and the scheduling is unset.
- code-review-08: The script performs no path validation.
- code-review-08: The code contains the expression 86400 * 45, which corresponds to a 45-day retention window.
- code-review-08: Issues #1, #3, #4, and #5 have no plausible reason to be intentional.
- debugging-01: The corrected get_url function returns f"http://{cfg['host']}:{cfg['port']}/api".
- debugging-02: Class bodies run in strict mode.
- debugging-02: When `this` is `undefined`, `this.seconds += 1` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: `setInterval(function () {...}.bind(this), 1000)` is an alternative fix that keeps a regular function.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-03: `i=2` would produce the last window `[3, 4]`.
- debugging-03: `moving_sum` returns the sum of each window of the given size.
- debugging-03: `moving_sum([1, 2, 3, 4], 2)` returns `[3, 5, 7]`.
- debugging-04: `utf-8-sig` should be used instead if the file may have a BOM.
- debugging-04: `chardet` and `charset-normalizer` can be used to detect a file's encoding.
- debugging-04: `errors="replace"` still counts lines correctly in the common case.
- debugging-05: A default argument value is created once, when the function is defined.
- debugging-05: After that call, `DEFAULT_TAGS` is permanently `["draft", "post"]`.
- debugging-05: With the sentinel fix, callers who pass their own list will still have that list mutated by `append`.
- debugging-06: The reported failure symptom is a "pool exhausted" error.
- debugging-06: A second leading candidate cause is a slow connection leak in the export worker itself.
- debugging-06: Connections may not be released on error paths, causing the pool to gradually shrink over a run.
- debugging-06: A connection leak would explain the non-deterministic failures because it depends on the error rate during a given session.
- debugging-06: Failures caused by a connection leak tend to cluster near the end of long runs.
- debugging-06: pg_stat_activity (or an equivalent) can provide DB-side connection and lock telemetry.
- debugging-06: Connection telemetry can reveal long-lived or idle-in-transaction connections at failure time.
- debugging-06: Additional incident logs could show whether all failures land in the same few-minute window.
- debugging-07: Async work that can delay queryability includes background jobs, message queues, and search indexes such as Elasticsearch or OpenSearch.
- debugging-07: Connection pool exhaustion could cause the failure without any explicit error surfacing in the test.
- debugging-07: Checking whether each xdist worker gets its own DB or schema is the cheapest first diagnostic step.
- debugging-07: The digest implementation should be grepped for implicit scoping or limits such as LIMIT, ORDER BY created_at DESC with a cap, or a time window not strictly filtered by the test's user or tenant ID.
- debugging-07: Confirming parallelism as the trigger separates hypothesis 1 from hypotheses 2, 3, and 4.
- debugging-07: Temporary instrumentation should log event IDs and timestamps returned by the API versus those returned by the digest, plus the worker ID that created them.
- debugging-07: Instrumentation output can be redirected to a file uploaded as an explicit CI artifact for just this test, or inspected by running locally in a loop with -n4.
- debugging-07: A poll or retry on the assertion should be tried in a scratch branch rather than committed.
- debugging-07: If adding a short retry or backoff before reading the digest fixes the failure, that strongly implicates eventual consistency (hypotheses 2 or 3) rather than cross-test contamination (hypothesis 1).
- debugging-07: Retries would not fix a genuine data leak from another test.
- debugging-07: If the failure rate scales with worker count rather than staying constant, that points to shared-resource contention rather than pure timing.
- debugging-07: Steps 1 and 2 are static or config checks that need no CI cycles.
- debugging-07: The recommended order is to start with steps 1 and 2, then use step 3 to confirm before spending time on instrumentation.
- debugging-08: Traffic-correlated growth plus growth on the no-webhook canary points to something scaling with all request traffic rather than only webhooks
- debugging-08: If growth-rate per request is roughly constant across canary and normal instances, unbounded per-request growth is the prime suspect
- debugging-08: Bounded caches are a classic false lead in memory investigations
- debugging-08: Multiple cache instances (per-thread or per-connection) can each be individually bounded while multiplying without bound
- debugging-08: If logged cache size plateaus at the configured bound, the cache is not the culprit or is only one contributor
- debugging-08: If process memory still grows when a second cache is given a deliberately tiny bound, the cache is not the primary cause
- debugging-08: An LRU eviction policy implemented with a lock that is sometimes bypassed may fail to fire
- debugging-08: Eviction that triggers only on insert leaves expired-but-present entries uncleaned during lookups
- debugging-08: Memory growth that survives quiet nights is also consistent with heap fragmentation from allocator behavior
- debugging-08: Variable-size allocations such as product payloads of differing sizes can fragment the heap
- debugging-08: Heap fragmentation can prevent freed memory from being returned to the OS or reused efficiently
- debugging-08: RSS never drops in the observed service
- debugging-08: Fragmentation would explain RSS never dropping even when logical memory usage does
- debugging-08: Go exposes heap_alloc and heap_live statistics that can be compared against RSS
- debugging-08: C and C++ expose malloc_stats and jemalloc statistics for allocator accounting
- debugging-08: JVM and .NET expose GC heap statistics for allocator accounting
- debugging-08: Flat live-object memory combined with climbing RSS indicates fragmentation rather than a leak
- debugging-08: Fragmentation requires a different fix than a leak, such as a compacting GC or a different allocator
- debugging-08: Periodic restart is a reasonable mitigation for fragmentation
- debugging-08: If a forced GC or compaction does not reduce RSS, the retention is OS-level rather than application-level
- debugging-08: Campaign flows may pull in a wider or rarer product catalog, producing more distinct product IDs
- debugging-08: More distinct product IDs would produce more distinct cache entries or one-off allocations
- debugging-08: Unusually high distinct-entity cardinality during campaigns would implicate cache-key cardinality rather than the cache size bound
- debugging-08: A single pprof or heap dump comparison between start and end of week would settle whether the issue is a leak or fragmentation
- explanation-01: A hash map needs a strategy to handle collisions because it cannot overwrite existing data.
- explanation-01: Each linked list node can live anywhere in memory.
- explanation-01: Quadratic probing jumps by increasing steps such as index + 1, index + 4, index + 9.
- explanation-01: Quadratic probing reduces clustering.
- explanation-01: Double hashing uses a second hash function to compute the step size.
- explanation-01: Open addressing requires careful resizing (rehashing) well before the table gets full, often at around 70% load.
- explanation-01: Java's HashMap often converts a bucket's list to a balanced tree if it grows too large.
- explanation-01: Converting a bucket's list to a balanced tree is a hybrid approach that protects against worst-case performance from many collisions.
- explanation-02: `SELECT * FROM accounts WHERE id = 1 FOR UPDATE;` is an example of pessimistic locking in Postgres and MySQL.
- explanation-02: Inventory decrements at checkout for a hot-selling item are an example of a workload suited to pessimistic locking.
- explanation-02: Many ORMs implement optimistic locking.
- explanation-02: Hibernate implements optimistic locking with `@Version`.
- explanation-02: EF Core implements optimistic locking with concurrency tokens.
- explanation-02: Collaborative editing is an example use case for optimistic locking.
- explanation-03: A network path may be a fast local link or a congested transatlantic route through many routers.
- explanation-03: If a sender transmits at whatever rate the receiver's window allows, it can overwhelm a router buffer along the path.
- explanation-03: The problem of retransmissions and degraded performance from dropped packets is known as congestion collapse.
- explanation-03: Congestion collapse was a real problem on the early internet in the late 1980s.
- explanation-03: TCP slow start is one of the original congestion control mechanisms.
- explanation-03: A larger initial window speeds up short connections.
- explanation-03: After detecting packet loss, TCP backs off.
- explanation-04: Threads are cheaper than processes because no separate address space must be set up or protected.
- explanation-04: Browsers put each tab in a separate process so that one tab crashing doesn't kill the whole browser.
- explanation-04: Multiple processes each get their own interpreter and GIL.
- explanation-04: Independent process restart is useful for workers that leak memory over time or that crash.
- explanation-04: Erlang/OTP-style 'let it crash' supervision is based on independent process lifecycle and restart.
- explanation-04: Gunicorn and Nginx worker processes are based on independent process lifecycle and restart.
- explanation-04: Process-based designs using separate services communicating over IPC or network generalize naturally to distributed systems.
- explanation-04: Threads only work within a single machine's shared memory.
- explanation-04: A web server handling many connections that share an in-memory cache is an example where threads win.
- explanation-05: Event emitters, DOM elements, and global services are examples of long-lived objects that listeners can be registered on.
- explanation-06: With a cache in place, writes still have to hit the database.
- explanation-06: Adding a cache means writes must also update or invalidate the cache.
- explanation-06: When data is not reused, a cache mostly misses and adds overhead without benefit.
- explanation-06: Request time could be spent in the database, in serialization, or in a slow downstream call.
- explanation-06: In a write-heavy workload, a cache adds complexity and can slow things down due to the extra layer to update and invalidate.
- explanation-06: Profiling slow requests can be done with timing logs or an APM tool.
- explanation-06: Some databases have a slow query log.
- explanation-06: A database's slow query log often points directly at missing indexes or expensive queries.
- explanation-06: A rough read/write ratio can be obtained from a manual count of logs over an hour.
- explanation-07: A product team being unable to say how much growth to expect indicates the access pattern is not yet well understood.
- explanation-07: If read load can be offloaded to replicas and storage growth handled by bigger disks or instance classes, there are likely years of runway before sharding becomes necessary.
- explanation-07: Tables can be partitioned by date or by tenant.
- explanation-07: Partitioning now makes a later shard split easier because the data is already logically separated.
- explanation-07: Re-sharding later is far more painful than sharding late.
- explanation-07: Growth across tenants often turns out uneven, with some tenants very large and most very small.
- explanation-07: Rebalancing shards under uneven growth becomes an ongoing operational cost.
- explanation-08: JSON encode/decode accounting for about 2% of request latency is common when network, database, or business logic dominate.
- explanation-08: If JSON encode/decode is 2% of request latency, a 10x faster serializer yields roughly a 1.8% overall improvement.
- explanation-08: A roughly 1.8% overall improvement is likely not worth the cost of migrating serialization formats.
- explanation-08: Binary formats such as protobuf and msgpack typically reduce payload size by 30-70% compared to JSON.
- explanation-08: Payload size reduction helps more when payloads are large or bandwidth is constrained.
- explanation-08: Payload size reduction helps less when payloads are small or already compressed.
- explanation-08: Gzip compression significantly narrows the payload size gap between JSON and binary formats.
- explanation-08: Serialization exceeding 10-15% of request latency counts as a meaningful chunk.
- explanation-08: Prototyping a binary format on one endpoint surfaces migration costs such as schema management, debuggability, and client compatibility.
- explanation-08: Migration costs matter as much as raw serialization speed.
- summarization-01: Keyboard shortcuts were added for the 10 most-used actions.
- summarization-01: Cold start time was reduced by approximately 40%.
- summarization-02: The config value swap was not caught before deploy despite review.
- summarization-02: The incident took about 7 minutes to page.
- summarization-02: Full rollback and recovery took about 34 minutes.
- summarization-02: The detection and rollback path worked well.
- summarization-02: The fix should focus on prevention rather than response speed.
- summarization-03: The worker pool would update the record when thumbnail processing is done.
- summarization-06: The restart-driven recovery is consistent with multiple possible root causes.
- summarization-07: The recommendation is to profile memory before drawing conclusions on tail latency or stability.
- summarization-07: The recommendation is to test under production-like traffic before drawing conclusions on tail latency or stability.
- summarization-08: It is firm that the progress bar behavior is a problem.
- summarization-08: Whether the fix should be visual or technical needs more investigation.
- summarization-08: Role-based defaults are worth probing in a larger or targeted study before prioritizing.

Added facts (styled only):

- code-review-01: The suggested fix raises `ValueError("db is required")` when `db` is None.
- code-review-01: The suggested fix appends `"member"` only if it is not already in `roles`.
- code-review-03: `SELECT *` pulls unneeded data.
- code-review-05: If `$1` is empty, `cd ""` changes to `$HOME`.
- code-review-05: If no `.tmp` files exist and the glob does not match, most shells leave the literal string `*.tmp`.
- code-review-05: The script performs destructive `rm -rf` operations with no confirmation, dry-run, or logging of what was deleted.
- code-review-05: The fixed version uses `cd -- "$BACKUP_DIR" || exit 1`.
- code-review-06: Non-dict collections such as lists, sets, and tuples are replaced wholesale and never merged.
- code-review-06: Overriding a list appends nothing; it just swaps the list.
- code-review-06: Replacing non-dict collections wholesale is likely intentional, since only dicts get recursive treatment.
- code-review-06: It is worth confirming that lists are not meant to be concatenated or merged.
- code-review-06: Cycles and self-references are unlikely in practice for config data and are low priority.
- code-review-06: The lack of input validation is fine for a trusted internal function but less acceptable for a public API.
- code-review-07: The 0ms first delay is likely an off-by-one error.
- code-review-07: The backoff should probably be 1000 * (i + 1), or i should start at 1.
- code-review-07: 500 errors get no backoff and are retried immediately in a tight loop.
- code-review-07: The lack of backoff on 500s is inconsistent with the 429 handling.
- code-review-07: Retrying 500s immediately could hammer a struggling server.
- code-review-07: Linear delay without jitter is worse than exponential backoff with jitter under real contention.
- code-review-07: The missing jitter is more a missed improvement than a bug.
- code-review-07: The backoff growth is unbounded-looking but acceptable because attempts is small.
- code-review-07: There is no maximum delay cap.
- code-review-07: The lack of backoff on 500s might be deliberate under the assumption that 500s are rare and transient and immediate retry is acceptable.
- code-review-07: The justification for immediate retry is weaker for 500s than for 429s.
- code-review-07: Falling through unknown errors to return null is the most suspicious behavior of those examined.
- code-review-07: The 1000 * i off-by-one is a straightforward bug rather than intentional behavior.
- code-review-08: Deleting mid-write temp files creates a race with the process writing them.
- code-review-08: `os.listdir` provides no ordering guarantee.
- code-review-08: Because of the lack of ordering, which files survive when the 500 cap is reached is arbitrary, neither oldest-first nor deterministic.
- code-review-08: Permission errors and a missing directory propagate as an unhandled crash with no diagnostic output.
- code-review-08: Deletions are irreversible and unlogged, reporting no filenames and no count anywhere visible.
- code-review-08: The 500-per-run cap is probably a deliberate throttle to avoid heavy filesystem/disk I/O in a single run.
- code-review-08: The cutoff-computed-at-import issue is the most dangerous one to verify first.
- debugging-05: In the fixed code, `tags` is set to `list(tags)` when `tags` is not `None`, and `list(DEFAULT_TAGS)` otherwise.
- debugging-06: An undersized pool that only tips over under specific overlapping load would explain failures occurring about once a week rather than every night.
- debugging-06: An analytics query without a timeout, or a lock wait on a shared table that the export writes to, could hold connections too long.
- debugging-06: The export job writes to a table that may be shared with the analytics service.
- debugging-06: A leaking pool would only exhaust when it coincides with a busy night.
- debugging-06: Queries still running past 30 seconds are the ones to look for in the slow query log.
- debugging-06: DB CPU, I/O, and connection-count metrics can be compared at 02:14 UTC on failure nights versus good nights.
- debugging-07: Examples of missing test isolation include no per-worker schema, shared sequence IDs, or a global 'latest N events' query.
- debugging-07: Seeding writes may become delayed if they go through an async queue, an outbox pattern, or a read replica with replication lag.
- debugging-07: A session-scoped or module-scoped fixture such as a test user, tenant, or digest cursor may be reused across workers or tests in a way that works serially but fails under interleaving.
- debugging-07: An autouse fixture that resets or truncates a table while another worker is mid-write is an example of shared fixture/state ordering problems.
- debugging-07: Under load with 4x concurrent database connections, a transaction isolation issue (read committed versus snapshot) can cause one insert to not yet be visible to the digest's read.
- debugging-07: A common gap is using one shared database and relying on per-test transaction rollback.
- debugging-07: Per-test transaction rollback does not protect against cross-worker reads if the isolation level is lenient.
- debugging-07: Because CI keeps no artifacts, diagnostics should print to stdout so they appear in the log.
- debugging-07: The recommended starting point is checking whether the test DB is shared across xdist workers and whether the digest read has any retry or wait logic.
- debugging-08: There are almost certainly two problems stacked together, not one.
- debugging-08: A baseline leak explains why memory usage never drops overnight.
- debugging-08: Memory usage not dropping overnight indicates real object retention rather than merely uncollected garbage.
- debugging-08: Likely causes of the baseline leak include background or scheduled jobs such as cache refresh, health checks, and metrics flush.
- debugging-08: The second problem is a traffic-proportional leak triggered by webhook processing.
- debugging-08: The cache bound has been unchanged for a year.
- debugging-08: An unchanged cache bound rules out the explanation that someone raised the limit.
- debugging-08: The cache is unlikely by itself to explain campaign-driven acceleration in memory growth.
- debugging-08: The heap dump procedure is to take two heap dumps some hours apart during growth and diff the dominator trees.
- debugging-08: Heap dump diffing can be done without a live profiler by using jmap -dump plus Eclipse MAT after the fact.
- debugging-08: If usage does not drop after a forced full GC, the growth is genuine retention.
- debugging-08: If RSS grows but runtime heap-used does not, the cause is native or off-heap growth.
- debugging-08: Direct buffers, native library allocations, and thread stacks are sources of native or off-heap growth.
- debugging-08: Disabling background jobs one at a time on the canary and seeing which reproduces growth alone pinpoints the baseline leak.
- debugging-08: Scheduled refresh, health checks, and metrics export are background jobs to disable individually.
- debugging-08: Dedup sets, rate limiters, and idempotency caches are examples of unbounded structures to grep for.
- debugging-08: High label cardinality is a very common silent leak.
- explanation-01: The lists in a chained hash map are usually short.
- explanation-01: A chained hash map never runs out of space.
- explanation-01: Chaining's worst-case lookup degrades to O(n) when many keys collide.
- explanation-01: Rust's HashMap uses open addressing.
- explanation-02: Optimistic locking fits read-heavy workloads.
- explanation-02: Optimistic locking fits long-lived transactions.
- explanation-02: Web form edits are an example of a long-lived transaction.
- explanation-02: In long-lived transactions, holding a database lock would be wasteful or cause deadlocks.
- explanation-03: A network path could be a fast datacenter link or a congested Wi-Fi connection.
- explanation-03: Every segment in the current window can trigger an ACK.
- explanation-04: Sharing memory between threads requires locking.
- explanation-04: Processes communicate via IPC mechanisms such as pipes, sockets, and shared memory.
- explanation-04: Workers handling flaky third-party code are an example of work that benefits from a process boundary.
- explanation-04: Python's multiprocessing module contrasts with its threading module for CPU-bound parallelism.
- explanation-04: Browsers sandbox tabs and renderers using separate processes.
- explanation-04: Using processes instead of threads eliminates an entire class of race conditions and deadlocks by construction when work doesn't need shared memory.
- explanation-04: Real-time data sharing is an example of a workload suited to threads.
- explanation-06: Slowness can be caused by slow queries, N+1 calls, network latency, CPU-bound code, or lock contention.
- explanation-06: Caches introduce cache invalidation bugs.
- explanation-06: Caches introduce stale data.
- explanation-06: A cache is another system to operate.
- explanation-06: Missing indexes, N+1 queries, and oversized payloads are often the real cause of slowness.
- explanation-06: Missing indexes, N+1 queries, and oversized payloads are cheaper to fix than adding a cache layer.
- explanation-07: Database capacity is a real but bounded problem.
- explanation-07: Under sharding, cross-shard joins, transactions, and unique constraints become expensive or impossible.
- explanation-07: Cheaper mitigations than sharding include a bigger instance, read replicas, table-level partitioning, archiving cold data, and improved indexes or query tuning.
- explanation-07: Retrofitting sharding later is work that would have to be done either way.
- explanation-07: Instrumentation for this decision includes tracking growth rate, hot tables, write QPS, and replication lag.
- summarization-02: The incorrect pool configuration exhausted the connection pool.
- summarization-02: The incident caused an error rate of approximately 12%.
- summarization-02: The incident ran from 09:14 to 09:48.
- summarization-04: The bug is not browser-specific.
- summarization-07: The worker crash could have been caused by the newer staging kernel.
- summarization-07: The worker crash could have been caused by an unrelated batcher bug.
- summarization-07: Staging runs a newer kernel.
- summarization-08: The progress bar finding is tentative.

### developer-docs

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 26 | 18 | 0.692 | 23 | 6 |
| code-review-02 | 19 | 15 | 0.789 | 19 | 0 |
| code-review-03 | 25 | 16 | 0.64 | 29 | 8 |
| code-review-04 | 14 | 9 | 0.643 | 13 | 1 |
| code-review-05 | 39 | 29 | 0.744 | 32 | 2 |
| code-review-06 | 30 | 19 | 0.633 | 28 | 7 |
| code-review-07 | 23 | 13 | 0.565 | 30 | 10 |
| code-review-08 | 42 | 29 | 0.69 | 41 | 19 |
| debugging-01 | 6 | 6 | 1.0 | 8 | 0 |
| debugging-02 | 14 | 10 | 0.714 | 9 | 1 |
| debugging-03 | 8 | 8 | 1.0 | 9 | 0 |
| debugging-04 | 11 | 7 | 0.636 | 15 | 5 |
| debugging-05 | 16 | 14 | 0.875 | 15 | 0 |
| debugging-06 | 27 | 19 | 0.704 | 36 | 15 |
| debugging-07 | 28 | 12 | 0.429 | 28 | 8 |
| debugging-08 | 40 | 20 | 0.5 | 40 | 20 |
| explanation-01 | 42 | 33 | 0.786 | 31 | 2 |
| explanation-02 | 32 | 25 | 0.781 | 24 | 3 |
| explanation-03 | 30 | 22 | 0.733 | 25 | 4 |
| explanation-04 | 31 | 21 | 0.677 | 39 | 4 |
| explanation-05 | 14 | 13 | 0.929 | 18 | 6 |
| explanation-06 | 17 | 13 | 0.765 | 18 | 5 |
| explanation-07 | 27 | 13 | 0.481 | 32 | 11 |
| explanation-08 | 14 | 7 | 0.5 | 16 | 2 |
| summarization-01 | 6 | 6 | 1.0 | 9 | 4 |
| summarization-02 | 13 | 11 | 0.846 | 15 | 5 |
| summarization-03 | 13 | 13 | 1.0 | 15 | 0 |
| summarization-04 | 13 | 12 | 0.923 | 13 | 1 |
| summarization-05 | 9 | 7 | 0.778 | 11 | 1 |
| summarization-06 | 15 | 15 | 1.0 | 13 | 0 |
| summarization-07 | 16 | 15 | 0.938 | 17 | 2 |
| summarization-08 | 25 | 22 | 0.88 | 22 | 3 |

Median fraction: 0.754 over 32 scored pairs.

Median additions: 3.5 over 32 scored pairs.

Lost facts:

- code-review-01: Swallowing all exceptions makes the mutable-default and missing-`db` bugs invisible.
- code-review-01: `roles.append("member")` mutates the list object the caller passed in, as a side effect.
- code-review-01: If the caller reuses that list elsewhere, it will unexpectedly contain "member".
- code-review-01: The suggested fix builds a new list with `[*roles, "member"]` instead of appending in place.
- code-review-01: The suggested fix makes `db` a required positional parameter with no default.
- code-review-01: The suggested fix catches `DatabaseError` rather than using a bare `except:`.
- code-review-01: The suggested fix calls `logger.exception` before returning `False`.
- code-review-01: `DatabaseError` is what is actually expected to be raised from a database call.
- code-review-02: The TypeError message is "Cannot read properties of undefined (reading 'name')".
- code-review-02: The unnecessary `async` keyword masks the fact that the function is not actually asynchronous in its logic.
- code-review-02: The proposed fixed version throws an Error when `data.name` is missing.
- code-review-02: Callers of the fixed function should wrap calls in `try/catch` to handle thrown errors.
- code-review-03: Passing `customer_name = "x' OR '1'='1"` returns all rows.
- code-review-03: `SELECT *` forces callers to guess column order and meaning from the return value instead of getting named fields.
- code-review-03: Invalid input types will produce a confusing SQL error or unexpected query behavior.
- code-review-03: The code calls `fetchall()` on unbounded results.
- code-review-03: If the `orders` table is large, `fetchall()` loads everything into memory at once.
- code-review-03: There is no pagination or limit on the query results.
- code-review-03: The function has no docstring and no type hints.
- code-review-03: The function signature does not indicate the expected types of `cursor`, `customer_name`, or `status`, nor the return type.
- code-review-03: The missing docstring and type hints make the function harder to use correctly.
- code-review-04: The GIL protects individual bytecode operations, but not multi-step sequences like read-modify-write.
- code-review-04: The class is explicitly used from multiple threads.
- code-review-04: Reading `self.value` from outside while another thread is mid-increment is not guaranteed to see a consistent value.
- code-review-04: In CPython, inconsistent reads are not a significant problem for a simple int assignment.
- code-review-04: The class provides no defined or documented way to read the value safely.
- code-review-05: Glob-expansion behavior when there are no matches varies across POSIX sh implementations.
- code-review-05: In some shells the no-match case just errors out silently.
- code-review-05: The `-f` flag to rm suppresses the "no such file" error.
- code-review-05: The script's quoting is inconsistent throughout.
- code-review-05: Using `set -eu` at the top would have caught the empty-variable and command-failure issues immediately.
- code-review-05: `set -eu` makes the script fail fast on errors and unset variables.
- code-review-05: `${1:?...}` requires the argument to be provided.
- code-review-05: Quoting cd makes a cd failure abort the script instead of silently falling through.
- code-review-05: A glob will not match directories named `*.tmp` recursively.
- code-review-05: The `-r` flag on rm in the original script was a latent risk.
- code-review-06: Values taken from override are assigned by reference via merged[key] = value rather than copied.
- code-review-06: merge_settings has no cycle or depth protection.
- code-review-06: A self-reference in either input structure causes unbounded recursion and a RecursionError.
- code-review-06: Configs built programmatically and merged with themselves make self-references more plausible than they sound.
- code-review-06: Only one of the three base/override type combinations behaves consistently with the rule 'override always wins, but dicts merge when both sides agree.'
- code-review-06: The base=scalar/override=dict behavior suggests the intended rule was 'override always wins, but dicts merge when both sides agree.'
- code-review-06: Overriding a dict-valued key with an empty dict is a no-op rather than a clear.
- code-review-06: merge_settings({"a": {"x": 1}}, {"a": {}}) returns {"a": {"x": 1}} unchanged.
- code-review-06: Merging with an empty override dict has nothing to apply.
- code-review-06: The project has no test suite.
- code-review-06: Characterization tests are cheap to write and pin down what correct behavior means before refactoring.
- code-review-07: On success, withRetry returns whatever fn returns.
- code-review-07: withRetry has three distinct outcomes collapsed into two ambiguous return values.
- code-review-07: If fn can itself legitimately return null or undefined, callers cannot distinguish success from silent failure.
- code-review-07: Nothing in the code documents or uses the distinction between the null and undefined return values.
- code-review-07: If a non-Error value such as null is thrown, reading err.status raises a TypeError.
- code-review-07: In the throw null case, accessing err.status throws inside the catch handler, producing an unhandled rejection instead of the intended fallback.
- code-review-07: On the last allowed iteration, a 429 still triggers the full setTimeout delay before the loop exits and the function returns.
- code-review-07: withRetry never throws and always returns a sentinel value.
- code-review-07: withRetry treats all 5xx responses as retryable and all other errors as fatal.
- code-review-07: HTTP status 501 is a 5xx status that is not actually retryable.
- code-review-08: No relevant memory was found for this project.
- code-review-08: The 'removed < 500' check is evaluated before the deletion it guards, not after.
- code-review-08: Because the check runs before the deletion, the actual cap is 501 rather than 500.
- code-review-08: When the function aborts, 'removed' is left undefined to the caller and the rest of the directory is unprocessed.
- code-review-08: The script has no dry-run mode.
- code-review-08: There is no way to safely preview what a run would touch.
- code-review-08: The files the script deletes have unclear provenance and the scheduling is unset.
- code-review-08: The script performs no path validation.
- code-review-08: CUTOFF is computed once at import time rather than per call.
- code-review-08: Computing CUTOFF at import time is fine for a single-shot scheduled invocation.
- code-review-08: If the module is imported into a long-running process and clean() is called repeatedly, the cutoff goes stale.
- code-review-08: The off-by-one on the cap is likely accidental.
- code-review-08: Issues #1, #3, #4, and #5 have no plausible reason to be intentional.
- debugging-02: Class bodies run in strict mode.
- debugging-02: When `this` is `undefined`, `this.seconds += 1` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: `setInterval(function () {...}.bind(this), 1000)` is an alternative fix that keeps a regular function.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-04: `utf-8-sig` should be used instead if the file may have a BOM.
- debugging-04: `chardet` and `charset-normalizer` can be used to detect a file's encoding.
- debugging-04: Passing `errors="replace"` to `open` prevents crashes on malformed or mixed-encoding files.
- debugging-04: `errors="replace"` still counts lines correctly in the common case.
- debugging-05: After that call, `DEFAULT_TAGS` is permanently `["draft", "post"]`.
- debugging-05: Copying the passed-in list with `list(tags)` prevents mutation of the caller's list.
- debugging-06: Variable batch numbers rule out a specific bad row as the cause.
- debugging-06: A connection leak would explain the non-deterministic failures because it depends on the error rate during a given session.
- debugging-06: Failures caused by a connection leak tend to cluster near the end of long runs.
- debugging-06: A less likely cause is a pool size configured too small for the combined peak concurrency of both services.
- debugging-06: Another less likely cause is a periodic DB-side resource spike (backup, autovacuum, or replication lag) that slows all queries at once.
- debugging-06: A failure occurred on 2026-07-29 at roughly 02:13–02:14.
- debugging-06: Slow query logging can be enabled on the shared database.
- debugging-06: The relevant window to inspect is roughly 30 seconds before each timeout.
- debugging-07: Shared test database or state across pytest-xdist workers is the most likely cause of the flaky failure.
- debugging-07: If the digest endpoint returns 'latest N events' without strict scoping to the test's own user or tenant, a concurrently running test can push one of the 3 seeded events out of the window.
- debugging-07: A read-after-write / eventual consistency race is the second most likely cause.
- debugging-07: Connection pool exhaustion could cause the failure without any explicit error surfacing in the test.
- debugging-07: Checking whether each xdist worker gets its own DB or schema is the cheapest first diagnostic step.
- debugging-07: Test/DB isolation setup alone often explains failures that occur only under parallelism and never serially.
- debugging-07: The digest implementation should be grepped for implicit scoping or limits such as LIMIT, ORDER BY created_at DESC with a cap, or a time window not strictly filtered by the test's user or tenant ID.
- debugging-07: Confirming parallelism as the trigger separates hypothesis 1 from hypotheses 2, 3, and 4.
- debugging-07: Temporary instrumentation should log event IDs and timestamps returned by the API versus those returned by the digest, plus the worker ID that created them.
- debugging-07: The CI setup keeps no artifacts.
- debugging-07: Instrumentation output can be redirected to a file uploaded as an explicit CI artifact for just this test, or inspected by running locally in a loop with -n4.
- debugging-07: A poll or retry on the assertion should be tried in a scratch branch rather than committed.
- debugging-07: Worker count can be bisected by temporarily running -n2 and -n3 in CI.
- debugging-07: If the failure rate scales with worker count rather than staying constant, that points to shared-resource contention rather than pure timing.
- debugging-07: Steps 1 and 2 are static or config checks that need no CI cycles.
- debugging-07: The recommended order is to start with steps 1 and 2, then use step 3 to confirm before spending time on instrumentation.
- debugging-08: Unbounded metrics or histogram label cardinality is a candidate leak source
- debugging-08: If growth-rate per request is roughly constant across canary and normal instances, unbounded per-request growth is the prime suspect
- debugging-08: A cache bound may limit entry count without limiting entry size
- debugging-08: Product objects can grow over time as more fields, variants, or images are added
- debugging-08: Multiple cache instances (per-thread or per-connection) can each be individually bounded while multiplying without bound
- debugging-08: If process memory still grows when a second cache is given a deliberately tiny bound, the cache is not the primary cause
- debugging-08: An LRU eviction policy implemented with a lock that is sometimes bypassed may fail to fire
- debugging-08: Eviction that triggers only on insert leaves expired-but-present entries uncleaned during lookups
- debugging-08: Variable-size allocations such as product payloads of differing sizes can fragment the heap
- debugging-08: Go exposes heap_alloc and heap_live statistics that can be compared against RSS
- debugging-08: C and C++ expose malloc_stats and jemalloc statistics for allocator accounting
- debugging-08: JVM and .NET expose GC heap statistics for allocator accounting
- debugging-08: Fragmentation requires a different fix than a leak, such as a compacting GC or a different allocator
- debugging-08: Periodic restart is a reasonable mitigation for fragmentation
- debugging-08: If a forced GC or compaction does not reduce RSS, the retention is OS-level rather than application-level
- debugging-08: Campaign flows may pull in a wider or rarer product catalog, producing more distinct product IDs
- debugging-08: More distinct product IDs would produce more distinct cache entries or one-off allocations
- debugging-08: Campaigns may trigger specific code paths such as promotions or coupon rules that leak
- debugging-08: Unusually high distinct-entity cardinality during campaigns would implicate cache-key cardinality rather than the cache size bound
- debugging-08: A single pprof or heap dump comparison between start and end of week would settle whether the issue is a leak or fragmentation
- explanation-01: A hash map needs a strategy to handle collisions because it cannot overwrite existing data.
- explanation-01: Separate chaining is simple to implement and reason about.
- explanation-01: Quadratic probing jumps by increasing steps such as index + 1, index + 4, index + 9.
- explanation-01: Quadratic probing reduces clustering.
- explanation-01: A high load factor in open addressing causes long probe chains.
- explanation-01: Chaining is favored when simplicity and worst-case robustness matter more, or when load factors are unpredictable.
- explanation-01: Most standard library implementations use chaining.
- explanation-01: Java's HashMap often converts a bucket's list to a balanced tree if it grows too large.
- explanation-01: Converting a bucket's list to a balanced tree is a hybrid approach that protects against worst-case performance from many collisions.
- explanation-02: `SELECT * FROM accounts WHERE id = 1 FOR UPDATE;` is an example of pessimistic locking in Postgres and MySQL.
- explanation-02: Inventory decrements at checkout for a hot-selling item are an example of a workload suited to pessimistic locking.
- explanation-02: `UPDATE documents SET content = ?, version = version + 1 WHERE id = ? AND version = ?;` is an example optimistic locking statement.
- explanation-02: Many ORMs implement optimistic locking.
- explanation-02: Hibernate implements optimistic locking with `@Version`.
- explanation-02: EF Core implements optimistic locking with concurrency tokens.
- explanation-02: Collaborative editing is an example use case for optimistic locking.
- explanation-03: A network path may be a fast local link or a congested transatlantic route through many routers.
- explanation-03: The problem of retransmissions and degraded performance from dropped packets is known as congestion collapse.
- explanation-03: Congestion collapse was a real problem on the early internet in the late 1980s.
- explanation-03: TCP slow start is one of the original congestion control mechanisms.
- explanation-03: Historically the initial cwnd was 1 segment.
- explanation-03: The initial cwnd is now often around 10 segments.
- explanation-03: The initial window of about 10 segments is specified in RFC 6928.
- explanation-03: A larger initial window speeds up short connections.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own register state.
- explanation-04: Threads are cheaper than processes because no separate address space must be set up or protected.
- explanation-04: Separate processes are used for sandboxing untrusted plugin code.
- explanation-04: Separate processes enable privilege separation between a low-privilege worker and a privileged coordinator.
- explanation-04: Erlang/OTP-style 'let it crash' supervision is based on independent process lifecycle and restart.
- explanation-04: Gunicorn and Nginx worker processes are based on independent process lifecycle and restart.
- explanation-04: Process-based designs using separate services communicating over IPC or network generalize naturally to distributed systems.
- explanation-04: Threads only work within a single machine's shared memory.
- explanation-04: A web server handling many connections that share an in-memory cache is an example where threads win.
- explanation-05: Event emitters, DOM elements, and global services are examples of long-lived objects that listeners can be registered on.
- explanation-06: With a cache in place, writes still have to hit the database.
- explanation-06: Profiling slow requests can be done with timing logs or an APM tool.
- explanation-06: A database's slow query log often points directly at missing indexes or expensive queries.
- explanation-06: A rough read/write ratio can be obtained from a manual count of logs over an hour.
- explanation-07: Sharding addresses write-throughput or single-machine-ceiling problems rather than storage-size problems.
- explanation-07: Whether the constraint is storage size versus write IOPS, CPU, or connection count hitting a single primary's limits determines which fix is appropriate, and those two situations require very different fixes.
- explanation-07: A product team being unable to say how much growth to expect indicates the access pattern is not yet well understood.
- explanation-07: If read load can be offloaded to replicas and storage growth handled by bigger disks or instance classes, there are likely years of runway before sharding becomes necessary.
- explanation-07: Write throughput and replication lag serve as leading indicators of approaching a scaling ceiling.
- explanation-07: Postgres supports native declarative partitioning.
- explanation-07: Tables can be partitioned by date or by tenant.
- explanation-07: Native declarative partitioning costs little to adopt.
- explanation-07: Partitioning now makes a later shard split easier because the data is already logically separated.
- explanation-07: Re-sharding later is far more painful than sharding late.
- explanation-07: Sharding makes every query, migration, and backup process N times more complex.
- explanation-07: Growth across tenants often turns out uneven, with some tenants very large and most very small.
- explanation-07: The recommended investment now is partitioning, read replicas, and monitoring the real bottleneck rather than disk size.
- explanation-07: Sharding should be revisited only when a specific metric — write throughput to the primary, replication lag, or vacuum time — shows a ceiling that vertical scaling cannot fix.
- explanation-08: JSON encode/decode accounting for about 2% of request latency is common when network, database, or business logic dominate.
- explanation-08: If JSON encode/decode is 2% of request latency, a 10x faster serializer yields roughly a 1.8% overall improvement.
- explanation-08: A roughly 1.8% overall improvement is likely not worth the cost of migrating serialization formats.
- explanation-08: Binary formats such as protobuf and msgpack typically reduce payload size by 30-70% compared to JSON.
- explanation-08: Gzip compression significantly narrows the payload size gap between JSON and binary formats.
- explanation-08: Serialization exceeding 10-15% of request latency counts as a meaningful chunk.
- explanation-08: Prototyping a binary format on one endpoint surfaces migration costs such as schema management, debuggability, and client compatibility.
- summarization-02: The detection and rollback path worked well.
- summarization-02: The fix should focus on prevention rather than response speed.
- summarization-04: After clicking the PDF export option, nothing happens initially.
- summarization-05: Ada is assigned to check with the mobile team lead on whether the mobile team was informed about the API deprecation.
- summarization-05: Chen is assigned to deliver a demo.
- summarization-07: The recommendation is to profile memory before drawing conclusions on tail latency or stability.
- summarization-08: It is firm that the progress bar behavior is a problem.
- summarization-08: Whether the fix should be visual or technical needs more investigation.
- summarization-08: Role-based defaults are worth probing in a larger or targeted study before prioritizing.

Added facts (styled only):

- code-review-01: A caller can pass `None`, a number, or a string as `roles`, and the function tries to append to it.
- code-review-01: The corrected version raises errors instead of hiding them.
- code-review-01: Raising errors lets the caller catch specific exceptions and decide how to handle them.
- code-review-01: In the corrected version, a falsy `name` raises `ValueError("name is required")`.
- code-review-01: In the corrected version, a `db` of `None` raises `ValueError("db is required")`.
- code-review-01: In the corrected version, `"member"` is appended only if it is not already in `roles`.
- code-review-03: `SELECT *` returns every column, including columns the caller might not need.
- code-review-03: If the caller passes `None` or another non-string type, the `+` concatenation raises a `TypeError`.
- code-review-03: The `TypeError` raised by the `+` concatenation has a confusing message.
- code-review-03: A malformed query is an example of a condition that causes the database call to raise an exception.
- code-review-03: The function neither catches nor documents the exceptions from the database call.
- code-review-03: Without a docstring, a caller has to read the implementation to learn what the function does.
- code-review-03: The problems are listed in order from most severe to least severe.
- code-review-03: The missing docstring is the least severe of the listed problems.
- code-review-04: The bytecode for `+=` involves separate load, add, and store steps.
- code-review-05: `cd` can fail if `$BACKUP_DIR` does not exist or was not provided.
- code-review-05: If no .tmp files exist, `rm -rf` receives the literal string `*.tmp` and fails with "no such file".
- code-review-06: The function has one clearly intentional behavior.
- code-review-06: The deletion is implemented via `merged.pop(key, None)`.
- code-review-06: Under the delete-by-`None` convention, only two states exist: "leave alone" (key absent) and "delete" (key set to `None`).
- code-review-06: If the intent is a full deep merge, the list-replacement behavior is a gap.
- code-review-06: If the intent is "merge dicts, replace everything else", the list-replacement behavior is correct and consistent with the `None` rule.
- code-review-06: Equality-based tests will not catch the shared-reference problem.
- code-review-06: Only identity checks or later mutation will reveal the shared-reference problem.
- code-review-07: Callers must handle three different 'not a real result' values: undefined, null, and thrown errors.
- code-review-07: The zero-delay first retry is an off-by-one error, and the intent was probably `1000 * (i + 1)`.
- code-review-07: The `err.status >= 500` branch calls `continue` with no delay.
- code-review-07: The 5xx branch retries as fast as possible, with no backoff.
- code-review-07: The lack of backoff on 5xx is inconsistent with the 429 branch.
- code-review-07: Retrying 5xx errors without delay can hammer a struggling server.
- code-review-07: With `attempts = 0`, the loop body never runs and the function returns undefined without ever calling `fn`.
- code-review-07: Converting errors to null destroys the original error's message and stack trace.
- code-review-07: Losing the message and stack trace makes debugging any masked failure impossible.
- code-review-07: To keep backward compatibility for unknown callers, the off-by-one delay and the fall-through undefined should be fixed first.
- code-review-08: os.remove runs on every listed entry, including subdirectories.
- code-review-08: Two overlapping cron runs make it a real risk that a file is deleted by another process between listdir and remove.
- code-review-08: A file matching the tmp- or .part pattern could be mid-write by another process.
- code-review-08: Deleting a mid-write tmp- or .part file can corrupt or lose in-progress work.
- code-review-08: The unconditional removal of tmp-/.part files is the most serious bug in the script.
- code-review-08: The 500-item cap does not select the oldest files.
- code-review-08: os.listdir returns entries in filesystem order, not by age.
- code-review-08: The first 500 files removed are effectively arbitrary.
- code-review-08: Sorting by mtime and removing the oldest first would make the cap bound blast radius as intended.
- code-review-08: Without sorting by mtime, a run can leave very old files behind while removing newer ones.
- code-review-08: The script has no concurrency guard.
- code-review-08: If a run takes longer than the schedule interval, two instances can run at once.
- code-review-08: Two concurrent instances each compute their own cap and race on the same files.
- code-review-08: The variable `removed` is returned but nothing shown in the reviewed code consumes it.
- code-review-08: If the caller does not log or alert on `removed`, the safety cap is silent.
- code-review-08: A silent safety cap gives no signal that the job hit the limit and is falling behind.
- code-review-08: Immediate unconditional removal of tmp-/.part files might be intentional if those files come from a fully synchronous write process with no partial-write window.
- code-review-08: The unconditional tmp-/.part removal is the highest-risk line in the script as written.
- code-review-08: The recommended fixes before the script runs unsupervised again are: add logging, sort by mtime for capped deletions, skip directories, and add an age threshold to the tmp-/.part branch or confirm no partial-write window exists.
- debugging-02: `setInterval` calls the callback with `this` set to the global object.
- debugging-04: UTF-8 is the safe default encoding for most modern text files.
- debugging-04: An alternative to detecting the encoding is to open the file in binary mode and count newline bytes directly.
- debugging-04: Opening a file with mode "rb" opens it in binary mode.
- debugging-04: Binary mode avoids decoding entirely.
- debugging-04: Counting lines in binary mode works regardless of the file's text encoding.
- debugging-06: A connection pool that is too small for peak load is the most likely cause.
- debugging-06: The connection leak hypothesis can originate in either service.
- debugging-06: The failure only appears under sustained load.
- debugging-06: Reaching a database-side connection limit is a possible cause.
- debugging-06: If the database caps total connections, both services' pools might request more connections than the database allows.
- debugging-06: Pool metrics should be watched in both services during a normal run and, if possible, during a failure.
- debugging-06: Connection pool configuration to review includes pool size, timeout, and max lifetime.
- debugging-06: Both services' pool configurations should be compared against the database's max connection limit.
- debugging-06: It is worth checking whether the sum of both services' pool sizes exceeds the database's connection limit.
- debugging-06: Both codebases should be audited for connections acquired without a corresponding release in error paths.
- debugging-06: Distributed tracing or connection-acquisition logging can record connection checkout and checkin events with a timestamp and caller identifier.
- debugging-06: Instrumentation needs to remain in place for at least two to three weeks to capture enough occurrences to find a pattern.
- debugging-06: Increasing the pool size or adding a circuit breaker with backoff is a temporary mitigation.
- debugging-06: Increasing the pool size or adding a circuit breaker is a stopgap, not a fix.
- debugging-06: Connection-acquisition instrumentation is the more reliable path to a root cause for a failure that isn't directly reproducible.
- debugging-07: The most likely cause of the failure is a race between event creation and digest generation that only appears under load.
- debugging-07: The test fails at a rate of 10%.
- debugging-07: The 10% failure rate and the CI-versus-local divide both point to timing rather than logic as the cause.
- debugging-07: If the database is shared across CI workers, that should be fixed first regardless of the root cause.
- debugging-07: The seeding and digest code can be grepped for async calls without `await`, or for background task dispatch such as queue publish, `Thread`, or `asyncio.create_task` that the test does not wait on.
- debugging-07: If the digest uses a time window, logging the cutoff timestamp and each event's stored timestamp checks for a boundary miss.
- debugging-07: Temporarily raising the connection pool size in CI and observing whether the failure rate drops tests the pool exhaustion hypothesis.
- debugging-07: A drop in failure rate after raising the pool size points to contention rather than a genuine logic bug.
- debugging-08: This explanation fits all four observations.
- debugging-08: The canary still runs cron jobs, health checks, and internal order processing.
- debugging-08: The canary skips only the webhook-triggered inserts.
- debugging-08: The canary's memory grows too, just more slowly than the other instances.
- debugging-08: The known cache is size-bounded and unchanged.
- debugging-08: Taking two heap dumps hours apart during a quiet period and diffing object counts by type and retained size can check for an unbounded collection.
- debugging-08: Adding metrics that report the size of every long-lived collection and graphing them against day-of-week and request volume can check for an unbounded collection.
- debugging-08: A comparator bug, TTL bug, or exception swallowed during eviction can leave a cache growing past its bound.
- debugging-08: A comparator bug, TTL bug, or exception swallowed during eviction can leave evicted entries still referenced elsewhere.
- debugging-08: Evicted objects may still be reachable from other structures such as closures, secondary indexes, or listener callbacks.
- debugging-08: Auditing each `on`/`subscribe`/`addEventListener` call for a matching removal can check for a listener leak.
- debugging-08: Tracking listener counts as a metric can check for a listener leak.
- debugging-08: Runtime warnings about excessive listeners or growing handle/thread counts can indicate a listener leak.
- debugging-08: Connections opened by internal jobs on the canary would still leak.
- debugging-08: Comparing heap size to process RSS can check for leaked native resources.
- debugging-08: If RSS grows faster than the managed heap, connection pool and socket counts over time should be examined.
- debugging-08: The suggested next step is to capture two heap dumps a few hours apart during a quiet night on the canary.
- debugging-08: A quiet-night diff isolates growth from webhook traffic.
- debugging-08: A quiet-night diff should point directly at the collection responsible.
- debugging-08: The quiet-night diff approach does not require marketing-week data.
- explanation-01: In chaining, if no matching key exists, the map appends the new entry to the list.
- explanation-01: In chaining, lookup, insert, and delete all require scanning the list in the worst case.
- explanation-02: Optimistic locking fits when conflicts are rare and transactions are short-lived.
- explanation-02: Pessimistic locking is best for high-conflict, long transactions.
- explanation-02: Optimistic locking is best for low-conflict, short transactions.
- explanation-03: A TCP connection often crosses several network links with different capacities.
- explanation-03: Every packet in a round trip generates its own ACK.
- explanation-03: On detecting loss, TCP resets or lowers `ssthresh`, depending on the algorithm variant.
- explanation-03: Slow start succeeds when the connection reaches a sending rate matching the path's available bandwidth without triggering a burst of loss.
- explanation-04: Shared thread resources include open files and network connections.
- explanation-04: Processes should be preferred when the work is CPU-bound and multiple cores are available.
- explanation-04: Threads are a better fit for I/O-bound work.
- explanation-04: I/O-bound tasks spend most of their time waiting rather than competing for the CPU.
- explanation-05: In a garbage-collected language, the garbage collector runs, finds unused memory, and frees it.
- explanation-05: Memory leaks can be found by watching for objects that live as long as a long-lived owner instead of as long as the task that created them.
- explanation-05: Caches, singletons, and global emitters are examples of long-lived owners.
- explanation-05: When an object's lifetime should be short but its owner's lifetime is long, the reference should be removed explicitly.
- explanation-05: Ways to remove such references explicitly include expiring cache entries, unregistering listeners, and using weak references.
- explanation-05: Weak references are available only in languages that support them.
- explanation-06: A cache does not fix database connection pool exhaustion.
- explanation-06: A database's slow-query log, an application profiler, and distributed tracing are all tools that can be used to profile a service.
- explanation-06: A cache is a strong fit when reads vastly outnumber writes.
- explanation-06: A cache is a strong fit when the underlying query or computation is expensive and its result does not change often.
- explanation-06: Adding a cache introduces cache invalidation bugs, a new failure mode, and extra operational cost.
- explanation-07: Sharding solves storage limits on a single node.
- explanation-07: Sharding does not fix query latency, index design, or connection handling problems.
- explanation-07: Sharding can make query latency, index design, or connection handling problems worse.
- explanation-07: The statement 'growth is expected' is not a number.
- explanation-07: A growth rate range as wide as 10% versus 300% per year changes whether sharding is the right decision.
- explanation-07: Sharding requires someone who owns the operational work permanently, not just at rollout.
- explanation-07: Sharding now spends engineering time on infrastructure instead of features.
- explanation-07: Monitoring database size, write throughput, and query latency provides data instead of a vague growth expectation.
- explanation-07: Vertical scaling and tuning options include a bigger instance, better indexes, connection pooling, and read replicas for read-heavy load.
- explanation-07: A product team response of 'cannot say how much' is a signal to get a rough estimate rather than to skip the estimate.
- explanation-07: A rough growth estimate can be derived from current user growth rate or contract pipeline.
- explanation-08: Headers and connection overhead often dominate network transfer time for small payloads.
- explanation-08: Binary formats tend to pay off most when throughput at high request volume is the goal, because they use less CPU per request across many machines.
- summarization-01: The release notes are based on the changes that affect end users.
- summarization-01: The remaining changes are build tooling, internal module refactoring, and telemetry batching.
- summarization-01: The build tooling, internal module refactoring, and telemetry batching changes do not affect app behavior.
- summarization-01: The changes that do not affect app behavior were left out of the release notes.
- summarization-02: The incorrect pool setting caused connection pool exhaustion.
- summarization-02: The pool exhaustion caused errors for about 12% of checkout requests.
- summarization-02: Errors started at 09:14 UTC.
- summarization-02: The on-call engineer was paged at 09:21.
- summarization-02: The rollback completed at 09:48.
- summarization-04: The failure was reproduced on two different machines.
- summarization-05: The action items listed come from a sprint planning meeting.
- summarization-07: The newer staging kernel might explain the worker crash.
- summarization-07: Apart from the median latency result, everything else in the results is uncertain.
- summarization-08: The study included eight interviews with eight participants.
- summarization-08: Of the three findings, one is firm and two are tentative.
- summarization-08: The finding that the progress bar might cause abandonment on large files is tentative.

### plain-language

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 26 | 18 | 0.692 | 23 | 4 |
| code-review-02 | 19 | 13 | 0.684 | 16 | 1 |
| code-review-03 | 25 | 17 | 0.68 | 20 | 1 |
| code-review-04 | 14 | 10 | 0.714 | 18 | 1 |
| code-review-05 | 39 | 28 | 0.718 | 23 | 2 |
| code-review-06 | 30 | 20 | 0.667 | 24 | 4 |
| code-review-07 | 23 | 11 | 0.478 | 37 | 14 |
| code-review-08 | 42 | 29 | 0.69 | 26 | 6 |
| debugging-01 | 6 | 6 | 1.0 | 9 | 0 |
| debugging-02 | 14 | 10 | 0.714 | 12 | 0 |
| debugging-03 | 8 | 8 | 1.0 | 10 | 0 |
| debugging-04 | 11 | 8 | 0.727 | 15 | 5 |
| debugging-05 | 16 | 14 | 0.875 | 15 | 0 |
| debugging-06 | 27 | 18 | 0.667 | 30 | 5 |
| debugging-07 | 28 | 15 | 0.536 | 30 | 8 |
| debugging-08 | 40 | 14 | 0.35 | 24 | 17 |
| explanation-01 | 42 | 27 | 0.643 | 20 | 2 |
| explanation-02 | 32 | 23 | 0.719 | 20 | 1 |
| explanation-03 | 30 | 18 | 0.6 | 23 | 1 |
| explanation-04 | 31 | 20 | 0.645 | 31 | 1 |
| explanation-05 | 14 | 11 | 0.786 | 15 | 1 |
| explanation-06 | 17 | 9 | 0.529 | 29 | 2 |
| explanation-07 | 27 | 11 | 0.407 | 32 | 11 |
| explanation-08 | 14 | 8 | 0.571 | 10 | 2 |
| summarization-01 | 6 | 5 | 0.833 | 5 | 0 |
| summarization-02 | 13 | 9 | 0.692 | 18 | 4 |
| summarization-03 | 13 | 12 | 0.923 | 12 | 0 |
| summarization-04 | 13 | 9 | 0.692 | 14 | 3 |
| summarization-05 | 9 | 8 | 0.889 | 11 | 2 |
| summarization-06 | 15 | 15 | 1.0 | 13 | 1 |
| summarization-07 | 16 | 14 | 0.875 | 17 | 2 |
| summarization-08 | 25 | 25 | 1.0 | 24 | 0 |

Median fraction: 0.692 over 32 scored pairs.

Median additions: 2.0 over 32 scored pairs.

Lost facts:

- code-review-01: Swallowing all exceptions makes the mutable-default and missing-`db` bugs invisible.
- code-review-01: The function performs no input validation.
- code-review-01: The function does not check that `name` is non-empty or valid.
- code-review-01: The suggested fix builds a new list with `[*roles, "member"]` instead of appending in place.
- code-review-01: The suggested fix makes `db` a required positional parameter with no default.
- code-review-01: The suggested fix calls `logger.exception` before returning `False`.
- code-review-01: The suggested fix returns `True` after a successful `db.insert(...)` call.
- code-review-01: `DatabaseError` is what is actually expected to be raised from a database call.
- code-review-02: The TypeError message is "Cannot read properties of undefined (reading 'name')".
- code-review-02: A 404 or 500 response with a JSON error body would be parsed as if it were valid profile data.
- code-review-02: The unnecessary `async` keyword masks the fact that the function is not actually asynchronous in its logic.
- code-review-02: The code does not check that `data` has a `name` property before calling `.toUpperCase()` on it.
- code-review-02: The proposed fixed version throws an Error when `data.name` is missing.
- code-review-02: Callers of the fixed function should wrap calls in `try/catch` to handle thrown errors.
- code-review-03: Any input containing a single quote breaks out of the SQL string literal.
- code-review-03: Passing `customer_name = "x' OR '1'='1"` returns all rows.
- code-review-03: `SELECT *` forces callers to guess column order and meaning from the return value instead of getting named fields.
- code-review-03: Nothing stops `customer_name` or `status` from being `None`, empty, or the wrong type.
- code-review-03: Invalid input types will produce a confusing SQL error or unexpected query behavior.
- code-review-03: The function has no docstring and no type hints.
- code-review-03: The function signature does not indicate the expected types of `cursor`, `customer_name`, or `status`, nor the return type.
- code-review-03: The missing docstring and type hints make the function harder to use correctly.
- code-review-04: The GIL protects individual bytecode operations, but not multi-step sequences like read-modify-write.
- code-review-04: The class is explicitly used from multiple threads.
- code-review-04: In CPython, inconsistent reads are not a significant problem for a simple int assignment.
- code-review-04: The class provides no defined or documented way to read the value safely.
- code-review-05: If BACKUP_DIR is empty, `cd $BACKUP_DIR` runs cd with no arguments.
- code-review-05: If cd goes to $HOME, the subsequent `rm -rf *.tmp` deletes .tmp files in the user's home directory.
- code-review-05: Glob-expansion behavior when there are no matches varies across POSIX sh implementations.
- code-review-05: In some shells the no-match case just errors out silently.
- code-review-05: The `-f` flag to rm suppresses the "no such file" error.
- code-review-05: The script's quoting is inconsistent throughout.
- code-review-05: `${1:?...}` requires the argument to be provided.
- code-review-05: Quoting cd makes a cd failure abort the script instead of silently falling through.
- code-review-05: The rewrite drops the `-r` flag from rm as unnecessary.
- code-review-05: A glob will not match directories named `*.tmp` recursively.
- code-review-05: The `-r` flag on rm in the original script was a latent risk.
- code-review-06: A call where override or a nested recursively passed value lacks .items() raises a raw AttributeError with no context about which key or config caused it.
- code-review-06: merge_settings has no cycle or depth protection.
- code-review-06: A self-reference in either input structure causes unbounded recursion and a RecursionError.
- code-review-06: Configs built programmatically and merged with themselves make self-references more plausible than they sound.
- code-review-06: Only one of the three base/override type combinations behaves consistently with the rule 'override always wins, but dicts merge when both sides agree.'
- code-review-06: The base=scalar/override=dict behavior suggests the intended rule was 'override always wins, but dicts merge when both sides agree.'
- code-review-06: The code likely intended to fall through to a plain replace when value is not a dict, but omitted an isinstance(value, dict) check alongside isinstance(merged[key], dict).
- code-review-06: The project has no test suite.
- code-review-06: Characterization tests are cheap to write and pin down what correct behavior means before refactoring.
- code-review-06: The dict-override crash and the shared mutable state issue are the problems most likely to cause production failures.
- code-review-07: On success, withRetry returns whatever fn returns.
- code-review-07: withRetry has three distinct outcomes collapsed into two ambiguous return values.
- code-review-07: If fn can itself legitimately return null or undefined, callers cannot distinguish success from silent failure.
- code-review-07: If a non-Error value such as null is thrown, reading err.status raises a TypeError.
- code-review-07: If a plain object without a .status property is thrown, err.status evaluates to undefined.
- code-review-07: The comparison undefined === 429 evaluates to false.
- code-review-07: The comparison undefined >= 500 evaluates to false.
- code-review-07: In the throw null case, accessing err.status throws inside the catch handler, producing an unhandled rejection instead of the intended fallback.
- code-review-07: On the last allowed iteration, a 429 still triggers the full setTimeout delay before the loop exits and the function returns.
- code-review-07: withRetry treats all 5xx responses as retryable and all other errors as fatal.
- code-review-07: HTTP status 501 is a 5xx status that is not actually retryable.
- code-review-07: The attempts parameter means total attempts rather than retries after the first try.
- code-review-08: No relevant memory was found for this project.
- code-review-08: The code uses os.listdir, which snapshots filenames.
- code-review-08: The 'removed < 500' check is evaluated before the deletion it guards, not after.
- code-review-08: Because the check runs before the deletion, the actual cap is 501 rather than 500.
- code-review-08: The script has no dry-run mode.
- code-review-08: There is no way to safely preview what a run would touch.
- code-review-08: The files the script deletes have unclear provenance and the scheduling is unset.
- code-review-08: There is no comment explaining the assumption that tmp/part files are always disposable.
- code-review-08: Deleting tmp-/.part files unconditionally regardless of age makes sense if those files are always safe to remove immediately.
- code-review-08: The 45-day window and the unconditional tmp/part deletion are likely deliberate but undocumented.
- code-review-08: The cap applying only to the age branch is inconsistent and has no plausible rationale.
- code-review-08: The off-by-one on the cap is likely accidental.
- code-review-08: Issues #1, #3, #4, and #5 have no plausible reason to be intentional.
- debugging-02: Class bodies run in strict mode.
- debugging-02: When `this` is `undefined`, `this.seconds += 1` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: `setInterval(function () {...}.bind(this), 1000)` is an alternative fix that keeps a regular function.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-04: `utf-8-sig` should be used instead if the file may have a BOM.
- debugging-04: `chardet` and `charset-normalizer` can be used to detect a file's encoding.
- debugging-04: `errors="replace"` still counts lines correctly in the common case.
- debugging-05: With the sentinel fix, callers who pass their own list will still have that list mutated by `append`.
- debugging-05: Copying the passed-in list with `list(tags)` prevents mutation of the caller's list.
- debugging-06: The reported failure symptom is a "pool exhausted" error.
- debugging-06: The failures recur approximately weekly.
- debugging-06: Failures caused by a connection leak tend to cluster near the end of long runs.
- debugging-06: The problem cannot currently be reproduced on demand.
- debugging-06: A failure occurred on 2026-07-29 at roughly 02:13–02:14.
- debugging-06: Slow query logging can be enabled on the shared database.
- debugging-06: The relevant window to inspect is roughly 30 seconds before each timeout.
- debugging-06: Comparing the analytics job schedule to the failure timestamps is the fastest lead to pursue.
- debugging-06: Additional incident logs could show whether all failures land in the same few-minute window.
- debugging-07: If the digest endpoint returns 'latest N events' without strict scoping to the test's own user or tenant, a concurrently running test can push one of the 3 seeded events out of the window.
- debugging-07: Async work that can delay queryability includes background jobs, message queues, and search indexes such as Elasticsearch or OpenSearch.
- debugging-07: Connection pool exhaustion could cause the failure without any explicit error surfacing in the test.
- debugging-07: Checking whether each xdist worker gets its own DB or schema is the cheapest first diagnostic step.
- debugging-07: The digest implementation should be grepped for implicit scoping or limits such as LIMIT, ORDER BY created_at DESC with a cap, or a time window not strictly filtered by the test's user or tenant ID.
- debugging-07: Confirming parallelism as the trigger separates hypothesis 1 from hypotheses 2, 3, and 4.
- debugging-07: Temporary instrumentation should log event IDs and timestamps returned by the API versus those returned by the digest, plus the worker ID that created them.
- debugging-07: A poll or retry on the assertion should be tried in a scratch branch rather than committed.
- debugging-07: Retries would not fix a genuine data leak from another test.
- debugging-07: Worker count can be bisected by temporarily running -n2 and -n3 in CI.
- debugging-07: If the failure rate scales with worker count rather than staying constant, that points to shared-resource contention rather than pure timing.
- debugging-07: Steps 1 and 2 are static or config checks that need no CI cycles.
- debugging-07: The recommended order is to start with steps 1 and 2, then use step 3 to confirm before spending time on instrumentation.
- debugging-08: Traffic-correlated growth plus growth on the no-webhook canary points to something scaling with all request traffic rather than only webhooks
- debugging-08: Unbounded metrics or histogram label cardinality is a candidate leak source
- debugging-08: If growth-rate per request is roughly constant across canary and normal instances, unbounded per-request growth is the prime suspect
- debugging-08: Bounded caches are a classic false lead in memory investigations
- debugging-08: Cache eviction can be broken for certain code paths
- debugging-08: Multiple cache instances (per-thread or per-connection) can each be individually bounded while multiplying without bound
- debugging-08: If logged cache size plateaus at the configured bound, the cache is not the culprit or is only one contributor
- debugging-08: If process memory still grows when a second cache is given a deliberately tiny bound, the cache is not the primary cause
- debugging-08: An LRU eviction policy implemented with a lock that is sometimes bypassed may fail to fire
- debugging-08: Eviction that triggers only on insert leaves expired-but-present entries uncleaned during lookups
- debugging-08: Memory growth that survives quiet nights is also consistent with heap fragmentation from allocator behavior
- debugging-08: Variable-size allocations such as product payloads of differing sizes can fragment the heap
- debugging-08: Heap fragmentation can prevent freed memory from being returned to the OS or reused efficiently
- debugging-08: Fragmentation would explain RSS never dropping even when logical memory usage does
- debugging-08: Go exposes heap_alloc and heap_live statistics that can be compared against RSS
- debugging-08: C and C++ expose malloc_stats and jemalloc statistics for allocator accounting
- debugging-08: JVM and .NET expose GC heap statistics for allocator accounting
- debugging-08: Flat live-object memory combined with climbing RSS indicates fragmentation rather than a leak
- debugging-08: Fragmentation requires a different fix than a leak, such as a compacting GC or a different allocator
- debugging-08: Periodic restart is a reasonable mitigation for fragmentation
- debugging-08: If a forced GC or compaction does not reduce RSS, the retention is OS-level rather than application-level
- debugging-08: Campaign flows may pull in a wider or rarer product catalog, producing more distinct product IDs
- debugging-08: More distinct product IDs would produce more distinct cache entries or one-off allocations
- debugging-08: Campaigns may trigger specific code paths such as promotions or coupon rules that leak
- debugging-08: Unusually high distinct-entity cardinality during campaigns would implicate cache-key cardinality rather than the cache size bound
- debugging-08: A single pprof or heap dump comparison between start and end of week would settle whether the issue is a leak or fragmentation
- explanation-01: A hash map needs a strategy to handle collisions because it cannot overwrite existing data.
- explanation-01: The data structure in a separate chaining bucket is usually a linked list, and sometimes a tree.
- explanation-01: Deletion in separate chaining is straightforward because it just removes the node from the list.
- explanation-01: Quadratic probing jumps by increasing steps such as index + 1, index + 4, index + 9.
- explanation-01: Quadratic probing reduces clustering.
- explanation-01: Double hashing uses a second hash function to compute the step size.
- explanation-01: Deletion in open addressing is trickier because emptying a slot might break the probe chain for other keys.
- explanation-01: Open addressing implementations typically use a special tombstone marker for deleted entries.
- explanation-01: Open addressing requires careful resizing (rehashing) well before the table gets full, often at around 70% load.
- explanation-01: Deletion is easy in chaining and needs tombstones in open addressing.
- explanation-01: Language runtime implementations such as Python's dict use open addressing.
- explanation-01: Most standard library implementations use chaining.
- explanation-01: Java's HashMap uses chaining.
- explanation-01: Java's HashMap often converts a bucket's list to a balanced tree if it grows too large.
- explanation-01: Converting a bucket's list to a balanced tree is a hybrid approach that protects against worst-case performance from many collisions.
- explanation-02: `SELECT * FROM accounts WHERE id = 1 FOR UPDATE;` is an example of pessimistic locking in Postgres and MySQL.
- explanation-02: A `SELECT ... FOR UPDATE` statement locks the row so no other transaction can update or lock it until the current transaction commits or rolls back.
- explanation-02: Inventory decrements at checkout for a hot-selling item are an example of a workload suited to pessimistic locking.
- explanation-02: `UPDATE documents SET content = ?, version = version + 1 WHERE id = ? AND version = ?;` is an example optimistic locking statement.
- explanation-02: If an optimistic-locking UPDATE affects 0 rows, it means someone else modified the row first.
- explanation-02: When an optimistic-locking UPDATE affects 0 rows, the application catches that and retries or shows a conflict error.
- explanation-02: Many ORMs implement optimistic locking.
- explanation-02: Hibernate implements optimistic locking with `@Version`.
- explanation-02: EF Core implements optimistic locking with concurrency tokens.
- explanation-03: A network path may be a fast local link or a congested transatlantic route through many routers.
- explanation-03: If a sender transmits at whatever rate the receiver's window allows, it can overwhelm a router buffer along the path.
- explanation-03: Dropped packets cause retransmissions, wasted bandwidth, and worse performance for everyone sharing the link.
- explanation-03: The problem of retransmissions and degraded performance from dropped packets is known as congestion collapse.
- explanation-03: Congestion collapse was a real problem on the early internet in the late 1980s.
- explanation-03: TCP slow start is one of the original congestion control mechanisms.
- explanation-03: Historically the initial cwnd was 1 segment.
- explanation-03: The initial cwnd is now often around 10 segments.
- explanation-03: The initial window of about 10 segments is specified in RFC 6928.
- explanation-03: A larger initial window speeds up short connections.
- explanation-03: cwnd increases roughly by one segment per ACK.
- explanation-03: In congestion avoidance, the window grows linearly instead of exponentially.
- explanation-04: A process has its own file descriptors and OS resources.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own register state.
- explanation-04: Threads are cheaper than processes because no separate address space must be set up or protected.
- explanation-04: Multiple processes each get their own interpreter and GIL.
- explanation-04: Separate processes enable privilege separation between a low-privilege worker and a privileged coordinator.
- explanation-04: Independent process restart is useful for workers that leak memory over time or that crash.
- explanation-04: Erlang/OTP-style 'let it crash' supervision is based on independent process lifecycle and restart.
- explanation-04: Gunicorn and Nginx worker processes are based on independent process lifecycle and restart.
- explanation-04: Process-based designs using separate services communicating over IPC or network generalize naturally to distributed systems.
- explanation-04: Threads only work within a single machine's shared memory.
- explanation-05: Event emitters, DOM elements, and global services are examples of long-lived objects that listeners can be registered on.
- explanation-05: A listener holds a reference to its enclosing scope, including large objects it captured.
- explanation-05: A listener keeps its enclosing scope reachable for as long as the emitter lives.
- explanation-06: With a cache in place, writes still have to hit the database.
- explanation-06: Adding a cache means writes must also update or invalidate the cache.
- explanation-06: Possible non-database bottlenecks include slow application code, network latency, N+1 query problems, missing indexes, and external API calls.
- explanation-06: Request time could be spent in the database, in serialization, or in a slow downstream call.
- explanation-06: In a write-heavy workload, a cache adds complexity and can slow things down due to the extra layer to update and invalidate.
- explanation-06: Some databases have a slow query log.
- explanation-06: A database's slow query log often points directly at missing indexes or expensive queries.
- explanation-06: A rough read/write ratio can be obtained from a manual count of logs over an hour.
- explanation-07: Whether the constraint is storage size versus write IOPS, CPU, or connection count hitting a single primary's limits determines which fix is appropriate, and those two situations require very different fixes.
- explanation-07: A product team being unable to say how much growth to expect indicates the access pattern is not yet well understood.
- explanation-07: Storage growth can be handled by provisioning bigger disks or a better instance class.
- explanation-07: If read load can be offloaded to replicas and storage growth handled by bigger disks or instance classes, there are likely years of runway before sharding becomes necessary.
- explanation-07: Write throughput and replication lag serve as leading indicators of approaching a scaling ceiling.
- explanation-07: Postgres supports native declarative partitioning.
- explanation-07: Tables can be partitioned by date or by tenant.
- explanation-07: Native declarative partitioning costs little to adopt.
- explanation-07: Partitioning now makes a later shard split easier because the data is already logically separated.
- explanation-07: Re-sharding later is far more painful than sharding late.
- explanation-07: Sharding makes every query, migration, and backup process N times more complex.
- explanation-07: Growth across tenants often turns out uneven, with some tenants very large and most very small.
- explanation-07: Rebalancing shards under uneven growth becomes an ongoing operational cost.
- explanation-07: Sharding before there is evidence it is needed means paying the rebalancing cost prematurely.
- explanation-07: The recommended investment now is partitioning, read replicas, and monitoring the real bottleneck rather than disk size.
- explanation-07: Sharding should be revisited only when a specific metric — write throughput to the primary, replication lag, or vacuum time — shows a ceiling that vertical scaling cannot fix.
- explanation-08: JSON encode/decode accounting for about 2% of request latency is common when network, database, or business logic dominate.
- explanation-08: If JSON encode/decode is 2% of request latency, a 10x faster serializer yields roughly a 1.8% overall improvement.
- explanation-08: Binary formats such as protobuf and msgpack typically reduce payload size by 30-70% compared to JSON.
- explanation-08: Payload size reduction helps less when payloads are small or already compressed.
- explanation-08: Gzip compression significantly narrows the payload size gap between JSON and binary formats.
- explanation-08: Prototyping a binary format on one endpoint surfaces migration costs such as schema management, debuggability, and client compatibility.
- summarization-01: Cold start time was reduced by approximately 40%.
- summarization-02: The incident took about 7 minutes to page.
- summarization-02: Full rollback and recovery took about 34 minutes.
- summarization-02: The detection and rollback path worked well.
- summarization-02: The fix should focus on prevention rather than response speed.
- summarization-03: The worker pool would update the record when thumbnail processing is done.
- summarization-04: The Reports page has an "Export" button.
- summarization-04: The Export button offers both a PDF option and a CSV option.
- summarization-04: After clicking the PDF export option, nothing happens initially.
- summarization-04: The bug was reproduced on the latest version of Firefox.
- summarization-05: Ada is assigned to check with the mobile team lead on whether the mobile team was informed about the API deprecation.
- summarization-07: The recommendation is to profile memory before drawing conclusions on tail latency or stability.
- summarization-07: The recommendation is to test under production-like traffic before drawing conclusions on tail latency or stability.

Added facts (styled only):

- code-review-01: The assistant checked its memory for relevant context before reviewing.
- code-review-01: The memory contained nothing relevant to this review.
- code-review-01: The review is based on the code alone.
- code-review-01: The recommendation is to raise the exception or return an error message along with the status.
- code-review-02: The missing `await` is likely why the developer expected `profile` to be ready when `return` runs.
- code-review-03: Example allowed status values are "pending", "shipped", and "cancelled".
- code-review-04: With the lock, no thread can observe a half-updated value.
- code-review-05: If the backup directory does not exist or `$1` is empty, `cd` fails but the script keeps running.
- code-review-05: `cd` with an empty argument does nothing in some shells and changes to `$HOME` in others.
- code-review-06: Storing new nested dicts by reference is inconsistent with the recursive branch, which builds a fresh dict.
- code-review-06: Deleting a key that doesn't exist is a silent no-op.
- code-review-06: `merged.pop(key, None)` won't raise an error if the key was never present.
- code-review-06: The crash bug is the one that should be fixed first regardless of intent, because a crash is never a reasonable feature.
- code-review-07: 5xx errors in `withRetry` get no backoff at all.
- code-review-07: The line `if (err.status >= 500) continue;` retries immediately with no delay.
- code-review-07: Retrying 5xx errors with no delay hammers a server that is already struggling.
- code-review-07: Immediate retry for 500-range errors is the opposite of what a retry helper should do.
- code-review-07: The zero-delay first retry looks like an off-by-one mistake.
- code-review-07: The delay expression probably should be `1000 * (i + 1)`.
- code-review-07: The backoff in `withRetry` has no cap and no jitter.
- code-review-07: The delay grows without limit as `attempts` increases.
- code-review-07: Having two silent-failure signals suggests the null-returning behavior isn't fully intentional.
- code-review-07: `withRetry` treats 429 errors with backoff-and-retry and 5xx errors with immediate retry.
- code-review-07: The differing treatment of 429 and 5xx could reflect a real distinction between rate limits and transient server errors that the original author cared about.
- code-review-07: Nothing in the code documents the distinction between 429 and 5xx handling.
- code-review-07: The asymmetry where one error class waits and the other does not looks more like an unfinished thought than a deliberate choice.
- code-review-07: The safest first fix is the loop-exhaustion bug of returning `undefined` instead of `null`.
- code-review-08: Deleting `.part`/`tmp-` files without an age check can delete an export file while it is still being written.
- code-review-08: The lack of an age check on `.part`/`tmp-` deletion is a real bug rather than a design choice.
- code-review-08: `ROOT` is hardcoded rather than read from config or environment.
- code-review-08: There is no check that the path is a real, expected export directory before deleting from it.
- code-review-08: Cron typically invokes a script as a fresh process each run.
- code-review-08: Deleting `tmp-`/`.part` files outright is probably intended to clean up crashed or abandoned exports.
- debugging-04: UTF-8 can represent plain ASCII text.
- debugging-04: UTF-8 can represent most characters beyond ASCII.
- debugging-04: UTF-8 is a safer default encoding than ASCII.
- debugging-04: errors="replace" substitutes invalid bytes with a placeholder character instead of raising an error.
- debugging-04: errors="replace" should only be used if the exact original bytes are not needed.
- debugging-06: Checking database host metrics such as CPU, disk I/O, and memory for the failure windows is a diagnostic step.
- debugging-06: Spikes in database host metrics point to database resource pressure as the cause.
- debugging-06: Reviewing error-handling code paths for the export job's database calls is a diagnostic step.
- debugging-06: The log context surrounding the failure is currently rotated away before it can be examined.
- debugging-06: Extending log retention or triggering a fuller dump when the error occurs will make the next occurrence easier to diagnose.
- debugging-07: The test fails about 10% of the time in CI.
- debugging-07: A cleanup step from another test can delete an event before the test reads it.
- debugging-07: If the test uses a fixed ID, timestamp, or user instead of a unique one per run, a parallel worker running the same or similar test can overwrite or filter out one of the three events.
- debugging-07: If the app uses a shared connection pool and workers reuse connections, one worker's uncommitted transaction can be invisible to another.
- debugging-07: Assigning every event a unique identifier per test run, such as a UUID, can eliminate the flake if shared test data is the cause.
- debugging-07: `pytest-xdist` combined with `pytest-django`'s `--create-db` per worker removes cross-worker interference.
- debugging-07: If the flake goes away after isolating the database per worker, shared state was the cause.
- debugging-07: Mocking the clock or widening the digest's time window prevents timing jitter from excluding a valid event.
- debugging-08: The growth pattern points to a real memory leak — objects that are never freed — rather than normal cache churn.
- debugging-08: Webhook traffic likely worsens an existing leak rather than creating it.
- debugging-08: Richer product data during a marketing campaign is an example of cached objects growing in size.
- debugging-08: The entry-count-bounded cache hypothesis fits the observed faster growth during campaign weeks.
- debugging-08: The entry-count-bounded cache hypothesis fits the clue that the cache bound has been static for a year.
- debugging-08: Comparing average cache entry size on a normal day against a campaign day can check the entry-count-bounded cache hypothesis.
- debugging-08: If a cache key includes a value such as a user ID, session ID, or campaign ID instead of just a product ID, the bounded cache is effectively many small caches whose total can grow without limit.
- debugging-08: Sampling the actual keys in the cache and looking for patterns that should not vary by product can detect unbounded cache key values.
- debugging-08: Because the canary grows with no webhook traffic, something outside the cache and unrelated to webhooks is leaking.
- debugging-08: Webhook traffic probably adds volume to the same non-webhook leak, which would explain the faster growth on the main instances.
- debugging-08: Taking two heap dumps on the canary hours apart with no traffic and diffing them shows which object counts increase.
- debugging-08: If each webhook creates a listener, promise, or connection that is not cleaned up, that would explain why webhook-receiving instances grow faster than the canary.
- debugging-08: Sending a batch of synthetic webhook requests to the canary and diffing heap dumps taken before and after can check for per-request webhook leaks.
- debugging-08: Memory growth that never shrinks overnight can come from native memory outside the heap, which a heap profiler will not show.
- debugging-08: HTTP connection pools, TLS session caches, and buffer allocations are examples of native memory outside the heap.
- debugging-08: If heap-used memory looks stable but the process's total memory (RSS) still grows, the cause may be a native buffer or connection leak.
- debugging-08: All five proposed checks are faster and more conclusive with an actual heap profile.
- explanation-01: Chaining handles many collisions without extra work.
- explanation-01: Chaining's performance stays steady even if the map fills up.
- explanation-02: Pessimistic locking fits when the work between reading and writing takes a long time, to avoid risking wasted effort.
- explanation-03: When congestion is detected, TCP shifts to congestion avoidance.
- explanation-04: If one process crashes, the operating system cleans it up and the other processes keep running.
- explanation-05: Leaks from unremoved listeners are especially common in long-running applications such as web pages or servers, where listeners accumulate over time.
- explanation-06: A cache stores a copy of data in fast memory so a slow step can be skipped.
- explanation-06: Issuing too many small queries per request is called the N+1 problem.
- explanation-07: Write latency that climbs after indexes and queries have been tuned is a sign that a single primary cannot keep up with writes.
- explanation-07: Storage growth rate is a signal to watch when deciding whether to shard.
- explanation-07: Projecting when the database will reach multiple terabytes reveals the real timeline for sharding.
- explanation-07: Many teams that think they need sharding actually just need read replicas or better caching.
- explanation-07: A rough growth estimate from the product team affects the sharding timeline more than the current 200 GB size does.
- explanation-07: Sharding now diverts engineering time from product features to infrastructure.
- explanation-07: The anticipated bottleneck that motivates sharding may never materialize.
- explanation-07: IDs or foreign keys that do not align well with a future shard key are an example of a schema that complicates a later split.
- explanation-07: Adding monitoring for write throughput, storage growth, query patterns, and read load is low-cost work that keeps sharding options open.
- explanation-07: Including a tenant or customer ID on every table, even if unused today, is an example of a shard-key-ready schema design.
- explanation-07: Setting a recurring review date, such as quarterly, to re-check the numbers keeps sharding options open.
- explanation-08: For small payloads, fixed overhead such as connection setup and parsing overhead may matter more than the encoding format.
- explanation-08: For large payloads, bandwidth and serialization speed matter more than fixed overhead.
- summarization-02: A deployment took place the evening before the incident.
- summarization-02: The wrong pool size exhausted the database connection pool.
- summarization-02: The pool exhaustion caused errors for about 12% of checkout requests.
- summarization-02: The incident ran from 09:14 to 09:48 UTC.
- summarization-04: The expected behavior is that the PDF exports the same way CSV export does for the same report.
- summarization-04: The reporter observed the issue in Firefox.
- summarization-04: A colleague observed the issue in Chrome.
- summarization-05: The text lists action items from a meeting.
- summarization-05: Ada is to run the payments database migration dry run.
- summarization-06: The summary is five sentences long and intended for the newsletter.
- summarization-07: Staging uses a newer kernel than production.
- summarization-07: The newer staging kernel could be the cause of the crash.

### technical-simplified

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 26 | 20 | 0.769 | 24 | 6 |
| code-review-02 | 19 | 15 | 0.789 | 21 | 1 |
| code-review-03 | 25 | 14 | 0.56 | 17 | 4 |
| code-review-04 | 14 | 9 | 0.643 | 17 | 0 |
| code-review-05 | 39 | 21 | 0.538 | 32 | 3 |
| code-review-06 | 30 | 19 | 0.633 | 33 | 8 |
| code-review-07 | 23 | 14 | 0.609 | 34 | 9 |
| code-review-08 | 42 | 0 | 0.0 | 0 | 0 |
| debugging-01 | 6 | 6 | 1.0 | 6 | 0 |
| debugging-02 | 14 | 9 | 0.643 | 10 | 0 |
| debugging-03 | 8 | 8 | 1.0 | 8 | 0 |
| debugging-04 | 11 | 9 | 0.818 | 11 | 0 |
| debugging-05 | 16 | 13 | 0.812 | 15 | 1 |
| debugging-07 | 28 | 14 | 0.5 | 24 | 5 |
| explanation-01 | 42 | 20 | 0.476 | 22 | 0 |
| explanation-02 | 32 | 26 | 0.812 | 27 | 1 |
| explanation-03 | 30 | 17 | 0.567 | 24 | 1 |
| explanation-04 | 31 | 14 | 0.452 | 21 | 1 |
| explanation-05 | 14 | 12 | 0.857 | 13 | 1 |
| explanation-06 | 17 | 9 | 0.529 | 17 | 3 |
| explanation-07 | 27 | 15 | 0.556 | 21 | 9 |
| explanation-08 | 14 | 4 | 0.286 | 18 | 3 |
| summarization-01 | 6 | 6 | 1.0 | 6 | 1 |
| summarization-03 | 13 | 13 | 1.0 | 12 | 0 |
| summarization-04 | 13 | 10 | 0.769 | 10 | 1 |
| summarization-05 | 9 | 8 | 0.889 | 6 | 1 |
| summarization-07 | 16 | 12 | 0.75 | 13 | 2 |
| summarization-08 | 25 | 24 | 0.96 | 22 | 2 |

Median fraction: 0.697 over 28 scored pairs.

Median additions: 1.0 over 28 scored pairs.

Lost facts:

- code-review-01: Swallowing all exceptions makes the mutable-default and missing-`db` bugs invisible.
- code-review-01: The suggested fix builds a new list with `[*roles, "member"]` instead of appending in place.
- code-review-01: The suggested fix makes `db` a required positional parameter with no default.
- code-review-01: The suggested fix catches `DatabaseError` rather than using a bare `except:`.
- code-review-01: The suggested fix calls `logger.exception` before returning `False`.
- code-review-01: `DatabaseError` is what is actually expected to be raised from a database call.
- code-review-02: The TypeError message is "Cannot read properties of undefined (reading 'name')".
- code-review-02: The unnecessary `async` keyword masks the fact that the function is not actually asynchronous in its logic.
- code-review-02: The proposed fixed version throws an Error when `data.name` is missing.
- code-review-02: Callers of the fixed function should wrap calls in `try/catch` to handle thrown errors.
- code-review-03: Passing `customer_name = "x' OR '1'='1"` returns all rows.
- code-review-03: A malicious input value such as `'; DROP TABLE orders; --` could run arbitrary SQL.
- code-review-03: `SELECT *` forces callers to guess column order and meaning from the return value instead of getting named fields.
- code-review-03: Nothing stops `customer_name` or `status` from being `None`, empty, or the wrong type.
- code-review-03: Invalid input types will produce a confusing SQL error or unexpected query behavior.
- code-review-03: The code calls `fetchall()` on unbounded results.
- code-review-03: If the `orders` table is large, `fetchall()` loads everything into memory at once.
- code-review-03: There is no pagination or limit on the query results.
- code-review-03: The function has no docstring and no type hints.
- code-review-03: The function signature does not indicate the expected types of `cursor`, `customer_name`, or `status`, nor the return type.
- code-review-03: The missing docstring and type hints make the function harder to use correctly.
- code-review-04: The GIL protects individual bytecode operations, but not multi-step sequences like read-modify-write.
- code-review-04: The class is explicitly used from multiple threads.
- code-review-04: Reading `self.value` from outside while another thread is mid-increment is not guaranteed to see a consistent value.
- code-review-04: In CPython, inconsistent reads are not a significant problem for a simple int assignment.
- code-review-04: The class provides no defined or documented way to read the value safely.
- code-review-05: If BACKUP_DIR is empty, `cd $BACKUP_DIR` runs cd with no arguments.
- code-review-05: Running cd with no arguments changes to $HOME rather than failing.
- code-review-05: If cd goes to $HOME, the subsequent `rm -rf *.tmp` deletes .tmp files in the user's home directory.
- code-review-05: An unquoted $BACKUP_DIR behaves incorrectly and unsafely if the value contains spaces or glob characters.
- code-review-05: The unchecked cd failure combined with rm -rf is the most dangerous bug in the script.
- code-review-05: Glob-expansion behavior when there are no matches varies across POSIX sh implementations.
- code-review-05: In some shells the no-match case just errors out silently.
- code-review-05: The `-f` flag to rm suppresses the "no such file" error.
- code-review-05: The no-match case for `rm -rf *.tmp` is not catastrophic in this script.
- code-review-05: Parsing ls output breaks on filenames containing spaces, newlines, or glob characters.
- code-review-05: Unquoted $f causes word-splitting and globbing problems and breaks on filenames with spaces.
- code-review-05: The script's quoting is inconsistent throughout.
- code-review-05: Using `set -eu` at the top would have caught the empty-variable and command-failure issues immediately.
- code-review-05: `set -eu` makes the script fail fast on errors and unset variables.
- code-review-05: `${1:?...}` requires the argument to be provided.
- code-review-05: Quoting cd makes a cd failure abort the script instead of silently falling through.
- code-review-05: A glob will not match directories named `*.tmp` recursively.
- code-review-05: The `-r` flag on rm in the original script was a latent risk.
- code-review-06: Values taken from override are assigned by reference via merged[key] = value rather than copied.
- code-review-06: Configs built programmatically and merged with themselves make self-references more plausible than they sound.
- code-review-06: Using None as an 'unset' marker is a common convention in layered-config systems.
- code-review-06: When the base value is a scalar and the override value is a dict, the override dict replaces the scalar wholesale because isinstance(merged[key], dict) is false.
- code-review-06: Only one of the three base/override type combinations behaves consistently with the rule 'override always wins, but dicts merge when both sides agree.'
- code-review-06: The base=scalar/override=dict behavior suggests the intended rule was 'override always wins, but dicts merge when both sides agree.'
- code-review-06: The code likely intended to fall through to a plain replace when value is not a dict, but omitted an isinstance(value, dict) check alongside isinstance(merged[key], dict).
- code-review-06: Overriding a dict-valued key with an empty dict is a no-op rather than a clear.
- code-review-06: merge_settings({"a": {"x": 1}}, {"a": {}}) returns {"a": {"x": 1}} unchanged.
- code-review-06: Merging with an empty override dict has nothing to apply.
- code-review-06: The project has no test suite.
- code-review-07: withRetry has three distinct outcomes collapsed into two ambiguous return values.
- code-review-07: Nothing in the code documents or uses the distinction between the null and undefined return values.
- code-review-07: If a non-Error value such as null is thrown, reading err.status raises a TypeError.
- code-review-07: In the throw null case, accessing err.status throws inside the catch handler, producing an unhandled rejection instead of the intended fallback.
- code-review-07: On the last allowed iteration, a 429 still triggers the full setTimeout delay before the loop exits and the function returns.
- code-review-07: withRetry never throws and always returns a sentinel value.
- code-review-07: withRetry treats all 5xx responses as retryable and all other errors as fatal.
- code-review-07: HTTP status 501 is a 5xx status that is not actually retryable.
- code-review-07: The history of the withRetry code is unknown and its callers cannot be inspected.
- code-review-08: No relevant memory was found for this project.
- code-review-08: The code calls os.path.getmtime(path) without any os.path.isfile or os.path.isdir check.
- code-review-08: os.path.getmtime works on directories.
- code-review-08: os.remove raises IsADirectoryError when called on a directory.
- code-review-08: If ROOT contains subdirectories, os.remove will crash the run partway through.
- code-review-08: os.path.getmtime raises FileNotFoundError on broken symlinks.
- code-review-08: The code uses os.listdir, which snapshots filenames.
- code-review-08: If another process deletes a file between the listing and os.path.getmtime or os.remove, an unhandled FileNotFoundError occurs.
- code-review-08: The script is described as a cleanup script running on a schedule.
- code-review-08: Concurrent writers or other cleanup jobs are plausible for this script.
- code-review-08: The 'removed < 500' check is evaluated before the deletion it guards, not after.
- code-review-08: Because the check runs before the deletion, the actual cap is 501 rather than 500.
- code-review-08: The 500-item cap applies only to the age-based branch and not to the tmp-/.part branch.
- code-review-08: tmp- and .part files are deleted unconditionally with no limit.
- code-review-08: Old files stop being cleaned once the cap is hit for a given run.
- code-review-08: Nothing in the code suggests tmp files should be exempt from a safety cap while regular exports are subject to one.
- code-review-08: The code has no error handling.
- code-review-08: A permission error, a race-condition-deleted file, or a subdirectory in ROOT aborts the whole function.
- code-review-08: When the function aborts, 'removed' is left undefined to the caller and the rest of the directory is unprocessed.
- code-review-08: For an unattended scheduled job, the lack of error handling means silent partial failures.
- code-review-08: The script does not log what was deleted.
- code-review-08: The script has no audit trail, so there is no record to diagnose an incorrect deletion after the fact.
- code-review-08: The script has no dry-run mode.
- code-review-08: There is no way to safely preview what a run would touch.
- code-review-08: The files the script deletes have unclear provenance and the scheduling is unset.
- code-review-08: The script matches tmp- and .part files by filename prefix and suffix.
- code-review-08: The script performs no path validation.
- code-review-08: A legitimately named file starting with 'tmp-', such as a customer export named tmp-report.csv, would be deleted regardless of age.
- code-review-08: There is no comment explaining the assumption that tmp/part files are always disposable.
- code-review-08: CUTOFF is computed once at import time rather than per call.
- code-review-08: Computing CUTOFF at import time is fine for a single-shot scheduled invocation.
- code-review-08: If the module is imported into a long-running process and clean() is called repeatedly, the cutoff goes stale.
- code-review-08: The code contains the expression 86400 * 45, which corresponds to a 45-day retention window.
- code-review-08: 45 is a clean round number and plausibly reflects a real retention policy.
- code-review-08: Deleting tmp-/.part files unconditionally regardless of age makes sense if those files are always safe to remove immediately.
- code-review-08: The 45-day window and the unconditional tmp/part deletion are likely deliberate but undocumented.
- code-review-08: The cap applying only to the age branch is inconsistent and has no plausible rationale.
- code-review-08: The off-by-one on the cap is likely accidental.
- code-review-08: The missing directory and error handling will eventually cause a crash.
- code-review-08: The absence of logging is a gap rather than a design choice.
- code-review-08: The values 45 and 500 may map to a retention policy or a downstream rate limit.
- code-review-08: Issues #1, #3, #4, and #5 have no plausible reason to be intentional.
- debugging-02: Class bodies run in strict mode.
- debugging-02: In strict mode, `this` inside a plain-called regular function is `undefined`.
- debugging-02: When `this` is `undefined`, `this.seconds += 1` throws `TypeError: Cannot read properties of undefined (reading 'seconds')`.
- debugging-02: `setInterval(function () {...}.bind(this), 1000)` is an alternative fix that keeps a regular function.
- debugging-02: Capturing `const self = this;` before the callback and using `self.seconds` is an alternative fix.
- debugging-04: `utf-8-sig` should be used instead if the file may have a BOM.
- debugging-04: `chardet` and `charset-normalizer` can be used to detect a file's encoding.
- debugging-05: After that call, `DEFAULT_TAGS` is permanently `["draft", "post"]`.
- debugging-05: With the sentinel fix, callers who pass their own list will still have that list mutated by `append`.
- debugging-05: Copying the passed-in list with `list(tags)` prevents mutation of the caller's list.
- debugging-07: Shared test database or state across pytest-xdist workers is the most likely cause of the flaky failure.
- debugging-07: If the digest endpoint returns 'latest N events' without strict scoping to the test's own user or tenant, a concurrently running test can push one of the 3 seeded events out of the window.
- debugging-07: A read-after-write / eventual consistency race is the second most likely cause.
- debugging-07: Async work that can delay queryability includes background jobs, message queues, and search indexes such as Elasticsearch or OpenSearch.
- debugging-07: Under CI's 4x concurrency, workers compete for CPU and DB connections.
- debugging-07: 4 parallel workers sharing a small DB connection pool could cause a write to queue or retry so that it lands after the digest read.
- debugging-07: Connection pool exhaustion could cause the failure without any explicit error surfacing in the test.
- debugging-07: Checking whether each xdist worker gets its own DB or schema is the cheapest first diagnostic step.
- debugging-07: The digest implementation should be grepped for implicit scoping or limits such as LIMIT, ORDER BY created_at DESC with a cap, or a time window not strictly filtered by the test's user or tenant ID.
- debugging-07: Confirming parallelism as the trigger separates hypothesis 1 from hypotheses 2, 3, and 4.
- debugging-07: Temporary instrumentation should log event IDs and timestamps returned by the API versus those returned by the digest, plus the worker ID that created them.
- debugging-07: Instrumentation output can be redirected to a file uploaded as an explicit CI artifact for just this test, or inspected by running locally in a loop with -n4.
- debugging-07: A poll or retry on the assertion should be tried in a scratch branch rather than committed.
- debugging-07: Steps 1 and 2 are static or config checks that need no CI cycles.
- explanation-01: A hash map needs a strategy to handle collisions because it cannot overwrite existing data.
- explanation-01: The data structure in a separate chaining bucket is usually a linked list, and sometimes a tree.
- explanation-01: Separate chaining is simple to implement and reason about.
- explanation-01: Separate chaining handles high load factors gracefully, degrading slowly as the map fills up.
- explanation-01: Deletion in separate chaining is straightforward because it just removes the node from the list.
- explanation-01: Separate chaining has poor cache locality.
- explanation-01: Chasing pointers around memory is slower than scanning a contiguous block.
- explanation-01: Each linked list node can live anywhere in memory.
- explanation-01: Linear probing tries successive slots at index + 1, index + 2, and so on.
- explanation-01: Quadratic probing jumps by increasing steps such as index + 1, index + 4, index + 9.
- explanation-01: Quadratic probing reduces clustering.
- explanation-01: Double hashing uses a second hash function to compute the step size.
- explanation-01: Open addressing has better cache performance because everything lives in one contiguous array.
- explanation-01: Probing nearby slots in a contiguous array is fast.
- explanation-01: A high load factor in open addressing causes long probe chains.
- explanation-01: Open addressing requires careful resizing (rehashing) well before the table gets full, often at around 70% load.
- explanation-01: Chaining has worse cache locality than open addressing.
- explanation-01: Chaining degrades gracefully at high load while open addressing degrades sharply.
- explanation-01: Deletion is easy in chaining and needs tombstones in open addressing.
- explanation-01: Chaining is favored when simplicity and worst-case robustness matter more, or when load factors are unpredictable.
- explanation-01: Java's HashMap often converts a bucket's list to a balanced tree if it grows too large.
- explanation-01: Converting a bucket's list to a balanced tree is a hybrid approach that protects against worst-case performance from many collisions.
- explanation-02: `SELECT * FROM accounts WHERE id = 1 FOR UPDATE;` is an example of pessimistic locking in Postgres and MySQL.
- explanation-02: Pessimistic locking fits when the cost of retrying a failed operation is high.
- explanation-02: Many ORMs implement optimistic locking.
- explanation-02: Hibernate implements optimistic locking with `@Version`.
- explanation-02: EF Core implements optimistic locking with concurrency tokens.
- explanation-02: Collaborative editing is an example use case for optimistic locking.
- explanation-03: A network path may be a fast local link or a congested transatlantic route through many routers.
- explanation-03: If a sender transmits at whatever rate the receiver's window allows, it can overwhelm a router buffer along the path.
- explanation-03: Dropped packets cause retransmissions, wasted bandwidth, and worse performance for everyone sharing the link.
- explanation-03: The problem of retransmissions and degraded performance from dropped packets is known as congestion collapse.
- explanation-03: Congestion collapse was a real problem on the early internet in the late 1980s.
- explanation-03: TCP slow start is one of the original congestion control mechanisms.
- explanation-03: Historically the initial cwnd was 1 segment.
- explanation-03: The initial cwnd is now often around 10 segments.
- explanation-03: The initial window of about 10 segments is specified in RFC 6928.
- explanation-03: A larger initial window speeds up short connections.
- explanation-03: The threshold at which slow start ends is called ssthresh.
- explanation-03: In congestion avoidance, the window grows linearly instead of exponentially.
- explanation-03: The name 'slow start' is misleading because its exponential growth is fast relative to later phases.
- explanation-04: Each thread has its own stack.
- explanation-04: Each thread has its own register state.
- explanation-04: Creating and switching threads is cheaper than creating and switching processes.
- explanation-04: Threads are cheaper than processes because no separate address space must be set up or protected.
- explanation-04: Browsers put each tab in a separate process so that one tab crashing doesn't kill the whole browser.
- explanation-04: Ruby historically serialized thread execution for CPU-bound code because of a global interpreter lock.
- explanation-04: Multiple processes each get their own interpreter and GIL.
- explanation-04: Separate processes are used for sandboxing untrusted plugin code.
- explanation-04: Separate processes enable privilege separation between a low-privilege worker and a privileged coordinator.
- explanation-04: A separate process can be independently supervised, killed, and restarted without disturbing the rest of the system.
- explanation-04: Independent process restart is useful for workers that leak memory over time or that crash.
- explanation-04: Erlang/OTP-style 'let it crash' supervision is based on independent process lifecycle and restart.
- explanation-04: Gunicorn and Nginx worker processes are based on independent process lifecycle and restart.
- explanation-04: Process-based designs using separate services communicating over IPC or network generalize naturally to distributed systems.
- explanation-04: Threads only work within a single machine's shared memory.
- explanation-04: A web server handling many connections that share an in-memory cache is an example where threads win.
- explanation-04: Using processes incurs IPC cost and duplicated memory.
- explanation-05: Event emitters, DOM elements, and global services are examples of long-lived objects that listeners can be registered on.
- explanation-05: A listener holds a reference to its enclosing scope, including large objects it captured.
- explanation-06: A cache does not help when requests are mostly unique reads.
- explanation-06: When data is not reused, a cache mostly misses and adds overhead without benefit.
- explanation-06: Possible non-database bottlenecks include slow application code, network latency, N+1 query problems, missing indexes, and external API calls.
- explanation-06: Request time could be spent in the database, in serialization, or in a slow downstream call.
- explanation-06: Profiling slow requests can be done with timing logs or an APM tool.
- explanation-06: Some databases have a slow query log.
- explanation-06: A database's slow query log often points directly at missing indexes or expensive queries.
- explanation-06: A rough read/write ratio can be obtained from a manual count of logs over an hour.
- explanation-07: Whether the constraint is storage size versus write IOPS, CPU, or connection count hitting a single primary's limits determines which fix is appropriate, and those two situations require very different fixes.
- explanation-07: A stable, well-understood access pattern (such as queries almost always scoped to a single tenant or user) is a prerequisite for choosing a shard key.
- explanation-07: A product team being unable to say how much growth to expect indicates the access pattern is not yet well understood.
- explanation-07: Storage growth can be handled by provisioning bigger disks or a better instance class.
- explanation-07: If read load can be offloaded to replicas and storage growth handled by bigger disks or instance classes, there are likely years of runway before sharding becomes necessary.
- explanation-07: Write throughput and replication lag serve as leading indicators of approaching a scaling ceiling.
- explanation-07: Tables can be partitioned by date or by tenant.
- explanation-07: Native declarative partitioning costs little to adopt.
- explanation-07: Partitioning now makes a later shard split easier because the data is already logically separated.
- explanation-07: Re-sharding later is far more painful than sharding late.
- explanation-07: Growth across tenants often turns out uneven, with some tenants very large and most very small.
- explanation-07: The recommended investment now is partitioning, read replicas, and monitoring the real bottleneck rather than disk size.
- explanation-08: JSON encode/decode accounting for about 2% of request latency is common when network, database, or business logic dominate.
- explanation-08: If JSON encode/decode is 2% of request latency, a 10x faster serializer yields roughly a 1.8% overall improvement.
- explanation-08: A roughly 1.8% overall improvement is likely not worth the cost of migrating serialization formats.
- explanation-08: Binary formats such as protobuf and msgpack typically reduce payload size by 30-70% compared to JSON.
- explanation-08: Payload size reduction helps more when payloads are large or bandwidth is constrained.
- explanation-08: Payload size reduction helps less when payloads are small or already compressed.
- explanation-08: Gzip compression significantly narrows the payload size gap between JSON and binary formats.
- explanation-08: Serialization exceeding 10-15% of request latency counts as a meaningful chunk.
- explanation-08: Prototyping a binary format on one endpoint surfaces migration costs such as schema management, debuggability, and client compatibility.
- explanation-08: Migration costs matter as much as raw serialization speed.
- summarization-04: After clicking the PDF export option, nothing happens initially.
- summarization-04: The "export failed" error banners provide no further details.
- summarization-04: The bug was reproduced on the latest version of Firefox.
- summarization-05: Ada is assigned to check with the mobile team lead on whether the mobile team was informed about the API deprecation.
- summarization-07: The staging comparison ran for six hours.
- summarization-07: All findings other than the median latency and memory measurements are provisional.
- summarization-07: The recommendation is to profile memory before drawing conclusions on tail latency or stability.
- summarization-07: The recommendation is to test under production-like traffic before drawing conclusions on tail latency or stability.
- summarization-08: It is firm that the progress bar behavior is a problem.

Added facts (styled only):

- code-review-01: The function contains six problems.
- code-review-01: The corrected version uses `roles=None` and `db=None` as defaults.
- code-review-01: The corrected version raises `ValueError` when `name` is empty.
- code-review-01: The corrected version raises `ValueError` when `db` is None.
- code-review-01: The corrected version appends `"member"` only if it is not already present in roles.
- code-review-01: The corrected version catches `Exception as e` and logs the error with `logging.error`.
- code-review-02: To return the fetched data, the function must return a value from inside the `.then()` chain or use `await`.
- code-review-03: Selecting all columns wastes bandwidth.
- code-review-03: If customer_name contains a single quote, the query becomes invalid SQL.
- code-review-03: A single quote in the data can cause a crash, not just a security risk.
- code-review-03: The database driver handles escaping in a parameterized query.
- code-review-05: Adding || exit 1 after cd handles cd failure.
- code-review-05: rm prints an error when it receives the literal string *.tmp.
- code-review-05: The corrected script exits with status 1 and prints a usage message to stderr when $1 is empty.
- code-review-06: No memory relevant to this task was found.
- code-review-06: The result places `override` keys in the order that `merged` already has them, plus new keys at the end.
- code-review-06: Python dicts preserve insertion order.
- code-review-06: The key order behavior is not documented.
- code-review-06: The function has no docstring.
- code-review-06: Recursive merging of nested dicts is a common pattern for merging settings or config files.
- code-review-06: A test should cover a nested dict in `base` overridden by a non-dict value.
- code-review-06: A test should cover changing a nested dict in the merge result and checking that `base` did not change.
- code-review-07: Returning `null` instead of the error is a bad design choice for a shared library.
- code-review-07: The 5xx branch retries with no delay at all.
- code-review-07: Retrying 5xx errors without delay can send too many requests to a server that already has problems.
- code-review-07: The backoff time has no cap.
- code-review-07: The wait time grows without limit as `attempts` grows.
- code-review-07: Setting `attempts` to 0 or a negative number skips `fn` entirely.
- code-review-07: With `attempts` of 0 or negative, the loop body never runs and the function returns `undefined` with no error.
- code-review-07: The function has no check for the `attempts = 0` or negative edge case.
- code-review-07: The missing delay for 5xx, the inconsistent return value, and the off-by-one delay look like unintended bugs.
- debugging-05: The test calls `tags.append("post")`.
- debugging-07: Another test running at the same time can delete or modify shared data such as a shared user or a shared digest queue.
- debugging-07: Order-dependent test pollution is consistent with low, random failure rates.
- debugging-07: `pytest-randomly` is a plugin that randomizes test order.
- debugging-07: If the failure rate changes when test order randomization is disabled, that points to test pollution.
- debugging-07: Steps 4 through 7 will identify the exact mechanism.
- explanation-02: Two transfers on the same bank account must not overlap.
- explanation-03: Slow start finds the correct sending speed without causing network congestion.
- explanation-04: Using separate processes avoids locks and race conditions.
- explanation-05: Global or static collections that grow are a common cause of memory leaks.
- explanation-06: The recommended second step is to measure the read-to-write mix.
- explanation-06: A cache should be added if reads dominate and the database is the bottleneck.
- explanation-06: Stale data becomes a new risk once a cache is added.
- explanation-07: The sharding decision depends on growth rate, write throughput, query patterns, the availability of a natural shard key, and team operational skill.
- explanation-07: A clear shard key, such as tenant ID or customer ID, makes sharding simple.
- explanation-07: Without a natural shard key, a team must invent one and can pick the wrong one.
- explanation-07: On a single instance, disk space can run out before the team notices, and the database then stops writes.
- explanation-07: Backup and restore time grows with the size of the data set.
- explanation-07: Growing backup and restore time can break the recovery time target.
- explanation-07: A single database instance is a single point of failure that removes the whole database during an outage.
- explanation-07: Migration to a sharded system gets harder as the data set grows.
- explanation-07: More data means a longer cutover to a sharded system.
- explanation-08: Binary formats often save 20% to 60% of size.
- explanation-08: The 20% to 60% savings range is wide.
- explanation-08: The next step is to run a short profiling test on production-like traffic for one day.
- summarization-01: Each button tooltip shows its keyboard shortcut.
- summarization-04: After choosing PDF export, the export fails and an "export failed" banner appears.
- summarization-05: Ada is to run the dry run for the payments database migration before Thursday.
- summarization-07: The crash could be caused by the newer staging kernel.
- summarization-07: Staging runs a newer kernel.
- summarization-08: The finding that the progress bar can cause abandonment on large files is tentative.
- summarization-08: The progress bar finding should be treated as tentative because of the small sample.

## Hedging survival

The judge lists the claims that the unstyled answer presents with uncertainty, then judges each claim in the styled answer: hedged (the uncertainty survives in some form), certain (the claim survives but reads as a fact — the failure this check targets), or absent (the claim is gone, a completeness loss). Survival is hedged / (hedged + certain). The claims that became certain appear verbatim below the table.

### actionable-clarity

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-02 | 3 | 1 | 1 | 1 | 0.5 |
| code-review-03 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 1 | 1 | 0 | 0 | 1.0 |
| code-review-06 | 9 | 7 | 0 | 2 | 1.0 |
| code-review-07 | 7 | 6 | 0 | 1 | 1.0 |
| code-review-08 | 10 | 7 | 2 | 1 | 0.778 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 1 | 1 | 1 | 0.5 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 7 | 4 | 0 | 3 | 1.0 |
| debugging-07 | 10 | 6 | 1 | 3 | 0.857 |
| debugging-08 | 16 | 5 | 2 | 9 | 0.714 |
| explanation-01 | 5 | 2 | 1 | 2 | 0.667 |
| explanation-02 | 2 | 0 | 2 | 0 | 0.0 |
| explanation-03 | 5 | 2 | 2 | 1 | 0.5 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 6 | 4 | 0 | 2 | 1.0 |
| explanation-07 | 2 | 2 | 0 | 0 | 1.0 |
| explanation-08 | 2 | 2 | 0 | 0 | 1.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 1 | 0 | 1 | 0 | 0.0 |
| summarization-04 | 1 | 1 | 0 | 0 | 1.0 |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 2 | 1 | 0 | 0.667 |

Claims: 102 over 32 judged pairs: 59 hedged, 16 certain, 27 absent.

Median survival: 0.818 over 22 scored pairs.

Claims that became certain:

- code-review-01: Collapsing all outcomes to `True`/`False` loses information a caller might need (e.g., "user already exists" vs "DB unreachable").
- code-review-02: The function will essentially always crash rather than return a value.
- code-review-03: A malicious value could run arbitrary SQL, e.g. `'; DROP TABLE orders; --`.
- code-review-08: The missing directory/error handling is likely accidental.
- code-review-08: The absence of logging is likely accidental rather than a design choice.
- debugging-04: The 0xc3 byte is the start of a UTF-8 multi-byte sequence, likely an accented character like é, ü, etc.
- debugging-07: If adding a short retry/backoff before reading the digest fixes it, that strongly implicates eventual consistency rather than cross-test contamination.
- debugging-08: Even one pprof/heap dump comparison (start vs. end of week) would immediately settle leak-vs-fragmentation and show what object types are accumulating.
- debugging-08: Getting a heap profile, even a single before/after snapshot, would answer most of these questions directly and is the highest-leverage next step if it's feasible to capture.
- explanation-01: Each bucket in separate chaining usually holds a linked list, and sometimes a tree.
- explanation-02: Pessimistic locking assumes conflicts are likely, so it prevents them upfront.
- explanation-02: The check for whether data changed since it was read is usually done via a version number or timestamp.
- explanation-03: On each ACK, the sender increases cwnd roughly by one segment per ACK.
- explanation-03: The name "slow start" is a bit misleading, since the growth is actually fast (exponential) relative to later phases.
- summarization-03: The main risk is that thumbnails may appear noticeably delayed during high-traffic periods.
- summarization-08: The cause of the progress-bar problem is tentative — it could be a UI/perception issue rather than a real performance problem.

### clarity-flow

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-02 | 3 | 0 | 2 | 1 | 0.0 |
| code-review-03 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 1 | 1 | 0 | 0 | 1.0 |
| code-review-06 | 9 | 6 | 1 | 2 | 0.857 |
| code-review-07 | 7 | 6 | 1 | 0 | 0.857 |
| code-review-08 | 10 | 6 | 3 | 1 | 0.667 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 2 | 0 | 1 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 7 | 4 | 0 | 3 | 1.0 |
| debugging-07 | 10 | 7 | 0 | 3 | 1.0 |
| debugging-08 | 16 | 4 | 3 | 9 | 0.571 |
| explanation-01 | 5 | 2 | 2 | 1 | 0.5 |
| explanation-02 | 2 | 0 | 2 | 0 | 0.0 |
| explanation-03 | 5 | 1 | 3 | 1 | 0.25 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 6 | 6 | 0 | 0 | 1.0 |
| explanation-07 | 2 | 2 | 0 | 0 | 1.0 |
| explanation-08 | 2 | 0 | 1 | 1 | 0.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 1 | 0 | 1 | 0 | 0.0 |
| summarization-04 | 1 | 1 | 0 | 0 | 1.0 |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 102 over 32 judged pairs: 57 hedged, 21 certain, 24 absent.

Median survival: 0.857 over 22 scored pairs.

Claims that became certain:

- code-review-01: Collapsing all outcomes to `True`/`False` loses information a caller might need (e.g., "user already exists" vs "DB unreachable").
- code-review-02: The function will essentially always crash rather than return a value.
- code-review-02: If the fetch fails or the response isn't OK, the code either fails silently or throws an unhandled rejection.
- code-review-03: A malicious value could run arbitrary SQL, e.g. `'; DROP TABLE orders; --`.
- code-review-06: Bugs #1 and #2 are the ones most likely to bite someone in production.
- code-review-07: Making the function throw properly is the change most likely to silently break something, given there are callers you can't see.
- code-review-08: In a cleanup script running on a schedule, concurrent writers or other cleanup jobs are plausible, so a file could be deleted between listing and getmtime/os.remove.
- code-review-08: The missing directory/error handling is likely accidental.
- code-review-08: The absence of logging is likely accidental rather than a design choice.
- debugging-08: Unusually high distinct-entity cardinality during a campaign week would implicate the cache-key-cardinality variant of cause #2 rather than the cache size bound itself.
- debugging-08: Even one pprof/heap dump comparison (start vs. end of week) would immediately settle leak-vs-fragmentation and show what object types are accumulating.
- debugging-08: Getting a heap profile, even a single before/after snapshot, would answer most of these questions directly and is the highest-leverage next step if it's feasible to capture.
- explanation-01: Each bucket in separate chaining usually holds a linked list, and sometimes a tree.
- explanation-01: Most standard library implementations use chaining, often converting a bucket's list to a balanced tree if it grows too large.
- explanation-02: Pessimistic locking assumes conflicts are likely, so it prevents them upfront.
- explanation-02: The check for whether data changed since it was read is usually done via a version number or timestamp.
- explanation-03: If the sender just started blasting data at whatever rate the receiver's window allows, it could easily overwhelm a router buffer somewhere in the middle.
- explanation-03: On each ACK, the sender increases cwnd roughly by one segment per ACK.
- explanation-03: The name "slow start" is a bit misleading, since the growth is actually fast (exponential) relative to later phases.
- explanation-08: If JSON encode/decode is only ~2% of request latency, even a 10x faster serializer nets ~1.8% overall improvement, which is likely not worth the migration cost.
- summarization-03: The main risk is that thumbnails may appear noticeably delayed during high-traffic periods.

### classic-concise

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-02 | 3 | 0 | 3 | 0 | 0.0 |
| code-review-03 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 1 | 1 | 0 | 0 | 1.0 |
| code-review-06 | 9 | 4 | 0 | 5 | 1.0 |
| code-review-07 | 7 | 6 | 0 | 1 | 1.0 |
| code-review-08 | 10 | 5 | 4 | 1 | 0.556 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 2 | 0 | 1 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 7 | 4 | 1 | 2 | 0.8 |
| debugging-07 | 10 | 5 | 3 | 2 | 0.625 |
| debugging-08 | 16 | 3 | 3 | 10 | 0.5 |
| explanation-01 | 5 | 0 | 2 | 3 | 0.0 |
| explanation-02 | 2 | 0 | 2 | 0 | 0.0 |
| explanation-03 | 5 | 1 | 2 | 2 | 0.333 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 6 | 4 | 0 | 2 | 1.0 |
| explanation-07 | 2 | 1 | 1 | 0 | 0.5 |
| explanation-08 | 2 | 2 | 0 | 0 | 1.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 1 | 1 | 0 | 0 | 1.0 |
| summarization-04 | 1 | 0 | 0 | 1 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 102 over 32 judged pairs: 48 hedged, 23 certain, 31 absent.

Median survival: 0.8 over 21 scored pairs.

Claims that became certain:

- code-review-01: Collapsing all outcomes to `True`/`False` loses information a caller might need (e.g., "user already exists" vs "DB unreachable").
- code-review-02: The problems are listed roughly in order of severity.
- code-review-02: The function will essentially always crash rather than return a value.
- code-review-02: If the fetch fails or the response isn't OK, the code either fails silently or throws an unhandled rejection.
- code-review-03: A malicious value could run arbitrary SQL, e.g. `'; DROP TABLE orders; --`.
- code-review-08: The asymmetry where the 500-item cap applies only to the age-based branch and not the tmp-/.part branch looks unintentional.
- code-review-08: The 500-cap applying only to the age branch and not the tmp/part branch is likely accidental.
- code-review-08: The missing directory/error handling is likely accidental.
- code-review-08: The absence of logging is likely accidental rather than a design choice.
- debugging-06: The fastest lead is probably comparing the analytics job schedule to the failure timestamps.
- debugging-07: Under CI's 4x concurrency, the write path is likely slower and more variable than on a quiet dev machine — enough to occasionally lose the race.
- debugging-07: Whether each xdist worker gets its own DB/schema or shares an instance alone often explains "only under parallelism, never serial."
- debugging-07: If adding a short retry/backoff before reading the digest fixes it, that strongly implicates eventual consistency rather than cross-test contamination.
- debugging-08: If cache size plateaus at the configured bound, the cache is not the culprit, or is just one contributor.
- debugging-08: Even one pprof/heap dump comparison (start vs. end of week) would immediately settle leak-vs-fragmentation and show what object types are accumulating.
- debugging-08: Getting a heap profile, even a single before/after snapshot, would answer most of these questions directly and is the highest-leverage next step if it's feasible to capture.
- explanation-01: Each bucket in separate chaining usually holds a linked list, and sometimes a tree.
- explanation-01: Open addressing requires resizing (rehashing) well before the table gets full, often at around 70% load.
- explanation-02: Pessimistic locking assumes conflicts are likely, so it prevents them upfront.
- explanation-02: The check for whether data changed since it was read is usually done via a version number or timestamp.
- explanation-03: On each ACK, the sender increases cwnd roughly by one segment per ACK.
- explanation-03: The name "slow start" is a bit misleading, since the growth is actually fast (exponential) relative to later phases.
- explanation-07: Risk of not sharding now: you eventually hit a real ceiling (single-writer throughput, vacuum/maintenance windows too long, connection limits) and have to shard under production pressure.

### concise

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 2 | 0 | 0.0 |
| code-review-02 | 3 | 0 | 1 | 2 | 0.0 |
| code-review-03 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 1 | 1 | 0 | 0 | 1.0 |
| code-review-06 | 9 | 5 | 0 | 4 | 1.0 |
| code-review-07 | 7 | 4 | 0 | 3 | 1.0 |
| code-review-08 | 10 | 3 | 6 | 1 | 0.333 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 2 | 0 | 1 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 7 | 4 | 2 | 1 | 0.667 |
| debugging-07 | 10 | 9 | 0 | 1 | 1.0 |
| debugging-08 | 16 | 3 | 2 | 11 | 0.6 |
| explanation-01 | 5 | 0 | 4 | 1 | 0.0 |
| explanation-02 | 2 | 1 | 1 | 0 | 0.5 |
| explanation-03 | 5 | 3 | 2 | 0 | 0.6 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 6 | 5 | 0 | 1 | 1.0 |
| explanation-07 | 2 | 1 | 0 | 1 | 1.0 |
| explanation-08 | 2 | 0 | 1 | 1 | 0.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 1 | 0 | 1 | 0 | 0.0 |
| summarization-04 | 1 | 0 | 1 | 0 | 0.0 |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 102 over 32 judged pairs: 50 hedged, 24 certain, 28 absent.

Median survival: 0.633 over 22 scored pairs.

Claims that became certain:

- code-review-01: Not checking whether "member" is already in `roles` could end up with duplicates.
- code-review-01: Collapsing all outcomes to `True`/`False` loses information a caller might need (e.g., "user already exists" vs "DB unreachable").
- code-review-02: The function will essentially always crash rather than return a value.
- code-review-03: A malicious value could run arbitrary SQL, e.g. `'; DROP TABLE orders; --`.
- code-review-08: The asymmetry where the 500-item cap applies only to the age-based branch and not the tmp-/.part branch looks unintentional.
- code-review-08: Deleting tmp-/.part files by filename prefix/suffix regardless of age may be deliberate, on the assumption that tmp/part files are always disposable.
- code-review-08: The 500-cap applying only to the age branch and not the tmp/part branch is likely accidental.
- code-review-08: The off-by-one on the 500 cap is likely accidental.
- code-review-08: The missing directory/error handling is likely accidental.
- code-review-08: The absence of logging is likely accidental rather than a design choice.
- debugging-06: Given the symptoms, this looks like connection contention rather than a query bug.
- debugging-06: The fastest lead is probably comparing the analytics job schedule to the failure timestamps.
- debugging-08: Even one pprof/heap dump comparison (start vs. end of week) would immediately settle leak-vs-fragmentation and show what object types are accumulating.
- debugging-08: Getting a heap profile, even a single before/after snapshot, would answer most of these questions directly and is the highest-leverage next step if it's feasible to capture.
- explanation-01: Each bucket in separate chaining usually holds a linked list, and sometimes a tree.
- explanation-01: Implementations of open addressing typically use a special "tombstone" marker instead of emptying a slot.
- explanation-01: Open addressing requires resizing (rehashing) well before the table gets full, often at around 70% load.
- explanation-01: Most standard library implementations use chaining, often converting a bucket's list to a balanced tree if it grows too large.
- explanation-02: Pessimistic locking assumes conflicts are likely, so it prevents them upfront.
- explanation-03: On each ACK, the sender increases cwnd roughly by one segment per ACK.
- explanation-03: The name "slow start" is a bit misleading, since the growth is actually fast (exponential) relative to later phases.
- explanation-08: If JSON encode/decode is only ~2% of request latency, even a 10x faster serializer nets ~1.8% overall improvement, which is likely not worth the migration cost.
- summarization-03: The main risk is that thumbnails may appear noticeably delayed during high-traffic periods.
- summarization-04: The issue is likely not browser-specific, since it reproduced on Firefox (latest) and Chrome on different machines.

### developer-docs

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 2 | 0 | 0.0 |
| code-review-02 | 3 | 0 | 1 | 2 | 0.0 |
| code-review-03 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-06 | 9 | 5 | 0 | 4 | 1.0 |
| code-review-07 | 7 | 5 | 2 | 0 | 0.714 |
| code-review-08 | 10 | 7 | 2 | 1 | 0.778 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 1 | 1 | 1 | 0.5 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 7 | 3 | 3 | 1 | 0.5 |
| debugging-07 | 10 | 5 | 2 | 3 | 0.714 |
| debugging-08 | 16 | 5 | 3 | 8 | 0.625 |
| explanation-01 | 5 | 1 | 3 | 1 | 0.25 |
| explanation-02 | 2 | 1 | 1 | 0 | 0.5 |
| explanation-03 | 5 | 1 | 2 | 2 | 0.333 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 6 | 4 | 2 | 0 | 0.667 |
| explanation-07 | 2 | 1 | 1 | 0 | 0.5 |
| explanation-08 | 2 | 1 | 0 | 1 | 1.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 1 | 0 | 1 | 0 | 0.0 |
| summarization-04 | 1 | 0 | 0 | 1 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 2 | 0 | 1 | 1.0 |

Claims: 102 over 32 judged pairs: 48 hedged, 28 certain, 26 absent.

Median survival: 0.5 over 21 scored pairs.

Claims that became certain:

- code-review-01: Not checking whether "member" is already in `roles` could end up with duplicates.
- code-review-01: Collapsing all outcomes to `True`/`False` loses information a caller might need (e.g., "user already exists" vs "DB unreachable").
- code-review-02: The function will essentially always crash rather than return a value.
- code-review-03: A malicious value could run arbitrary SQL, e.g. `'; DROP TABLE orders; --`.
- code-review-05: If no `.tmp` files exist and the shell doesn't glob-expand, `rm -rf` may literally try to remove a file named `*.tmp`, or in some shells just error out silently
- code-review-07: The `null` vs `undefined` split for two different failure modes looks like an oversight rather than a design choice.
- code-review-07: The zero-delay first retry (`1000 * i` with `i` starting at 0) may or may not be intended.
- code-review-08: The missing directory/error handling is likely accidental.
- code-review-08: The absence of logging is likely accidental rather than a design choice.
- debugging-04: The 0xc3 byte is the start of a UTF-8 multi-byte sequence, likely an accented character like é, ü, etc.
- debugging-06: Given the symptoms, this looks like connection contention rather than a query bug.
- debugging-06: A connection leak would explain why the failure isn't deterministic, and such failures tend to cluster near the end of long runs.
- debugging-06: The fastest lead is probably comparing the analytics job schedule to the failure timestamps.
- debugging-07: Under CI's 4x concurrency, the write path is likely slower and more variable than on a quiet dev machine — enough to occasionally lose the race.
- debugging-07: If adding a short retry/backoff before reading the digest fixes it, that strongly implicates eventual consistency rather than cross-test contamination.
- debugging-08: The traffic-correlated growth rate plus continued growth on the no-webhook canary points to something scaling with all request traffic, not just webhooks.
- debugging-08: Heap fragmentation would explain why RSS never drops even if logical memory usage does.
- debugging-08: If live-object memory is flat but RSS climbs, it's fragmentation rather than a leak.
- explanation-01: Each bucket in separate chaining usually holds a linked list, and sometimes a tree.
- explanation-01: In open addressing, emptying a slot on deletion might break the probe chain for other keys.
- explanation-01: Implementations of open addressing typically use a special "tombstone" marker instead of emptying a slot.
- explanation-02: Pessimistic locking assumes conflicts are likely, so it prevents them upfront.
- explanation-03: On each ACK, the sender increases cwnd roughly by one segment per ACK.
- explanation-03: The name "slow start" is a bit misleading, since the growth is actually fast (exponential) relative to later phases.
- explanation-06: If the workload is write-heavy, a cache adds complexity and can even slow things down.
- explanation-06: The database's slow query log, if it has one, often points straight at missing indexes or expensive queries.
- explanation-07: If read load can be offloaded with replicas and storage growth handled by bigger disks/better instance class, you likely have years of runway before sharding is forced.
- summarization-03: The main risk is that thumbnails may appear noticeably delayed during high-traffic periods.

### plain-language

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 2 | 0 | 0.0 |
| code-review-02 | 3 | 1 | 2 | 0 | 0.333 |
| code-review-03 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-06 | 9 | 6 | 0 | 3 | 1.0 |
| code-review-07 | 7 | 6 | 0 | 1 | 1.0 |
| code-review-08 | 10 | 6 | 3 | 1 | 0.667 |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 2 | 0 | 1 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-06 | 7 | 6 | 0 | 1 | 1.0 |
| debugging-07 | 10 | 7 | 1 | 2 | 0.875 |
| debugging-08 | 16 | 3 | 1 | 12 | 0.75 |
| explanation-01 | 5 | 1 | 0 | 4 | 1.0 |
| explanation-02 | 2 | 0 | 2 | 0 | 0.0 |
| explanation-03 | 5 | 2 | 1 | 2 | 0.667 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 6 | 4 | 1 | 1 | 0.8 |
| explanation-07 | 2 | 1 | 0 | 1 | 1.0 |
| explanation-08 | 2 | 1 | 0 | 1 | 1.0 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-02 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 1 | 1 | 0 | 0 | 1.0 |
| summarization-04 | 1 | 0 | 0 | 1 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-06 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 102 over 32 judged pairs: 56 hedged, 15 certain, 31 absent.

Median survival: 1.0 over 21 scored pairs.

Claims that became certain:

- code-review-01: Not checking whether "member" is already in `roles` could end up with duplicates.
- code-review-01: Collapsing all outcomes to `True`/`False` loses information a caller might need (e.g., "user already exists" vs "DB unreachable").
- code-review-02: The problems are listed roughly in order of severity.
- code-review-02: The function will essentially always crash rather than return a value.
- code-review-03: A malicious value could run arbitrary SQL, e.g. `'; DROP TABLE orders; --`.
- code-review-05: If no `.tmp` files exist and the shell doesn't glob-expand, `rm -rf` may literally try to remove a file named `*.tmp`, or in some shells just error out silently
- code-review-08: In a cleanup script running on a schedule, concurrent writers or other cleanup jobs are plausible, so a file could be deleted between listing and getmtime/os.remove.
- code-review-08: The missing directory/error handling is likely accidental.
- code-review-08: The absence of logging is likely accidental rather than a design choice.
- debugging-07: Under CI's 4x concurrency, the write path is likely slower and more variable than on a quiet dev machine — enough to occasionally lose the race.
- debugging-08: Getting a heap profile, even a single before/after snapshot, would answer most of these questions directly and is the highest-leverage next step if it's feasible to capture.
- explanation-02: Pessimistic locking assumes conflicts are likely, so it prevents them upfront.
- explanation-02: The check for whether data changed since it was read is usually done via a version number or timestamp.
- explanation-03: The name "slow start" is a bit misleading, since the growth is actually fast (exponential) relative to later phases.
- explanation-06: If the workload is write-heavy, a cache adds complexity and can even slow things down.

### technical-simplified

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 1 | 1 | 0 | 0.5 |
| code-review-02 | 3 | 0 | 2 | 1 | 0.0 |
| code-review-03 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-04 | 0 | 0 | 0 | 0 | n/a |
| code-review-05 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-06 | 9 | 3 | 0 | 6 | 1.0 |
| code-review-07 | 7 | 5 | 0 | 2 | 1.0 |
| code-review-08 | 10 | 0 | 0 | 10 | n/a |
| debugging-01 | 0 | 0 | 0 | 0 | n/a |
| debugging-02 | 0 | 0 | 0 | 0 | n/a |
| debugging-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 3 | 2 | 0 | 1 | 1.0 |
| debugging-05 | 0 | 0 | 0 | 0 | n/a |
| debugging-07 | 10 | 7 | 2 | 1 | 0.778 |
| explanation-01 | 5 | 0 | 4 | 1 | 0.0 |
| explanation-02 | 2 | 0 | 2 | 0 | 0.0 |
| explanation-03 | 5 | 0 | 2 | 3 | 0.0 |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| explanation-05 | 0 | 0 | 0 | 0 | n/a |
| explanation-06 | 6 | 5 | 0 | 1 | 1.0 |
| explanation-07 | 2 | 0 | 2 | 0 | 0.0 |
| explanation-08 | 2 | 1 | 1 | 0 | 0.5 |
| summarization-01 | 0 | 0 | 0 | 0 | n/a |
| summarization-03 | 1 | 0 | 1 | 0 | 0.0 |
| summarization-04 | 1 | 0 | 1 | 0 | 0.0 |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-07 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 76 over 28 judged pairs: 30 hedged, 20 certain, 26 absent.

Median survival: 0.25 over 18 scored pairs.

Claims that became certain:

- code-review-01: Collapsing all outcomes to `True`/`False` loses information a caller might need (e.g., "user already exists" vs "DB unreachable").
- code-review-02: The function will essentially always crash rather than return a value.
- code-review-02: If the fetch fails or the response isn't OK, the code either fails silently or throws an unhandled rejection.
- code-review-03: A malicious value could run arbitrary SQL, e.g. `'; DROP TABLE orders; --`.
- code-review-05: If no `.tmp` files exist and the shell doesn't glob-expand, `rm -rf` may literally try to remove a file named `*.tmp`, or in some shells just error out silently
- debugging-07: Whether each xdist worker gets its own DB/schema or shares an instance alone often explains "only under parallelism, never serial."
- debugging-07: If adding a short retry/backoff before reading the digest fixes it, that strongly implicates eventual consistency rather than cross-test contamination.
- explanation-01: Each bucket in separate chaining usually holds a linked list, and sometimes a tree.
- explanation-01: In open addressing, emptying a slot on deletion might break the probe chain for other keys.
- explanation-01: Implementations of open addressing typically use a special "tombstone" marker instead of emptying a slot.
- explanation-01: Most standard library implementations use chaining, often converting a bucket's list to a balanced tree if it grows too large.
- explanation-02: Pessimistic locking assumes conflicts are likely, so it prevents them upfront.
- explanation-02: The check for whether data changed since it was read is usually done via a version number or timestamp.
- explanation-03: If the sender just started blasting data at whatever rate the receiver's window allows, it could easily overwhelm a router buffer somewhere in the middle.
- explanation-03: On each ACK, the sender increases cwnd roughly by one segment per ACK.
- explanation-07: If read load can be offloaded with replicas and storage growth handled by bigger disks/better instance class, you likely have years of runway before sharding is forced.
- explanation-07: Risk of not sharding now: you eventually hit a real ceiling (single-writer throughput, vacuum/maintenance windows too long, connection limits) and have to shard under production pressure.
- explanation-08: If JSON encode/decode is only ~2% of request latency, even a 10x faster serializer nets ~1.8% overall improvement, which is likely not worth the migration cost.
- summarization-03: The main risk is that thumbnails may appear noticeably delayed during high-traffic periods.
- summarization-04: The issue is likely not browser-specific, since it reproduced on Firefox (latest) and Chrome on different machines.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 874, measured: 874.
Mean duration: 13398 ms. Mean wall: 33980 ms. Mean startup: 20582 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 874, measured: 874.
Input tokens: 1748 uncached, 1708316 cache write, 1814424 cache read. Output tokens: 965388.
Cache-read share: 0.515.
Cache writes by lifetime: 1708316 at 5 minutes, 0 at 1 hour.

## Warnings

- technical-simplified/summarization-02: the pair failed the gate, excluded
- technical-simplified/summarization-06: the pair failed the gate, excluded
- technical-simplified/debugging-06: the pair failed the gate, excluded
- technical-simplified/debugging-08: the pair failed the gate, excluded
