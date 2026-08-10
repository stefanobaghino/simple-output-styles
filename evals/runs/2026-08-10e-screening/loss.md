# Content-loss report

**Screening run.** This run covers 8 of 32 prompts, as one
run instead of 3. By design, the generation calls are about
8% of a full campaign, and the judge calls are about 25%
of one full run.
The subset holds 2 hedge-rich prompts, mirroring the
hedge-rich share of the full set.
Measured against the baseline campaign
(runs/2026-08-08 and runs/2026-08-08b), a screening run holds about
25% of the calls and about 25% of the
weighted input tokens of one full run, plus the full cost
probe, which is per style and does not shrink.
The error bars are wider than in a full run,
because fewer contests feed the bootstrap intervals.
`style-compare` rejects a comparison of this run with a full run.

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

Judge: opus. Judged on 2026-08-10T11:35:56+00:00.

## Completeness (fact survival)

The judge lists the facts of the unstyled answer, then checks each fact against the styled answer. The fraction is the share of the facts that survive. The judge also lists the facts of the styled answer and checks each fact against the unstyled answer: a styled fact that the unstyled answer does not state is an addition. The lost facts and the added facts appear verbatim below the table.

### actionable-clarity

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 28 | 17 | 0.607 | 30 | 6 |
| code-review-03 | 30 | 20 | 0.667 | 22 | 7 |
| debugging-04 | 11 | 10 | 0.909 | 16 | 5 |
| debugging-08 | 43 | 17 | 0.395 | 33 | 17 |
| explanation-03 | 29 | 23 | 0.793 | 26 | 6 |
| explanation-04 | 27 | 19 | 0.704 | 40 | 8 |
| summarization-05 | 9 | 7 | 0.778 | 10 | 0 |
| summarization-08 | 21 | 20 | 0.952 | 23 | 4 |

Median fraction: 0.741 over 8 scored pairs.

Median additions: 6.0 over 8 scored pairs.

Lost facts:

- code-review-01: The function does not check whether `"member"` is already in `roles` before appending it.
- code-review-01: If `roles` already contains `"member"`, it gets appended again, producing duplicates.
- code-review-01: The function has no type hints and no docstring.
- code-review-01: The missing type hints and docstring are a minor issue.
- code-review-01: Without type hints or a docstring, the expected shape of `roles` (list of str) and the interface required of `db` (a `.insert` method) are unclear to callers.
- code-review-01: The cleaner version raises `ValueError("name is required")` when `name` is falsy.
- code-review-01: The cleaner version raises `ValueError("db is required")` when `db` is `None`.
- code-review-01: The cleaner version copies `roles` with `list(roles)` rather than mutating the caller's list.
- code-review-01: The cleaner version appends `"member"` only if it is not already in `roles`.
- code-review-01: The cleaner version calls `db.insert({"name": name, "roles": roles})` and returns `True`.
- code-review-01: Specific exceptions, such as `db`-related errors, can be caught at the call site instead.
- code-review-03: Any value containing a single quote character breaks out of the string literal in the query.
- code-review-03: The unhandled exception provides no context for the caller.
- code-review-03: The function has no type hints.
- code-review-03: The function has no docstring.
- code-review-03: Without type hints or a docstring, the expected shape of `cursor` is not documented.
- code-review-03: Without type hints or a docstring, the expected shape of the return value is not documented.
- code-review-03: The missing type hints and docstring are a minor issue.
- code-review-03: Missing type hints and docstrings are worth noting for a public or reusable function.
- code-review-03: The SQL injection is the only issue that actually matters in this code.
- code-review-03: All the other issues identified are secondary polish.
- debugging-04: Passing errors="surrogateescape" to open enables a byte-for-byte round trip.
- debugging-08: One contributor is baseline/time-driven, such as background jobs, scheduled tasks, connection pools, or internal timers.
- debugging-08: Failure to return to baseline overnight rules out normal cache eviction and GC working as intended.
- debugging-08: If a bounded cache were behaving correctly, quiet periods with no new unique products would let old entries evict.
- debugging-08: If GC were working as intended, it would reclaim short-lived garbage and the RSS/heap floor would flatten.
- debugging-08: A rising memory floor indicates something unbounded or a bound that is not actually enforced.
- debugging-08: A common failure mode is cache keys including unbounded fields such as request ID, locale, or webhook payload variant.
- debugging-08: If key cardinality is effectively infinite, eviction never catches up.
- debugging-08: A common failure mode is a bug in the eviction policy, such as uncleaned wrappers/decorators or soft/weak reference configs that do not reclaim.
- debugging-08: Cache key cardinality explosion is the most likely cause given the described profile.
- debugging-08: Campaigns produce more distinct products and promotions, and therefore more unique cache keys.
- debugging-08: If entry count is not flat at the configured bound, keys are being evicted improperly or the bound is not wired to the intended value.
- debugging-08: Sampling cache keys during a campaign versus a quiet week can reveal high-cardinality fields such as campaign ID, variant ID, or session ID in the key.
- debugging-08: Each webhook or background poll may register a callback, subscription, or timer that is never deregistered.
- debugging-08: Listener/handler leaks survive quiet periods.
- debugging-08: A listener leak would explain why the canary grows slowly from other event sources while normal instances grow faster.
- debugging-08: `jcmd GC.class_histogram` can count live objects on the JVM.
- debugging-08: `/debug/pprof/heap` can be used to count live objects in Go.
- debugging-08: `objgraph` can count live objects in Python.
- debugging-08: Daily class histograms can reveal which class counts climb monotonically.
- debugging-08: Allocator fragmentation is a red herring rather than a real leak.
- debugging-08: If used heap drops back near baseline after a forced GC, the behavior is allocator fragmentation and lower priority.
- debugging-08: No profiling tool currently exists for the service.
- debugging-08: `jmap -histo` produces object-count dumps on the JVM.
- debugging-08: Go supports `runtime.ReadMemStats` and pprof for object-count dumps.
- debugging-08: Node supports heap snapshots via `--inspect`.
- debugging-08: Python supports `tracemalloc` for memory tracking.
- explanation-03: Routers along a network path have limited buffer space.
- explanation-03: Packet drops from buffer overflow degrade throughput for all users sharing the path.
- explanation-03: Historically, the initial cwnd was 1 segment.
- explanation-03: RFC 6928 specifies the initial congestion window of 10 segments.
- explanation-03: Growing cwnd by one segment per RTT would be painfully slow for high-bandwidth links.
- explanation-03: On detecting loss, the sender backs off significantly and switches to congestion avoidance.
- explanation-04: Threads can corrupt each other's data without careful synchronization such as locks and mutexes.
- explanation-04: Separate processes allow use of OS-level protections such as memory isolation, separate permissions, and seccomp/capabilities.
- explanation-04: Threads cannot provide OS-level security protections because threads share everything.
- explanation-04: Separate processes make independent starting, stopping, and resource limiting (memory caps, CPU quotas via cgroups) natural.
- explanation-04: The OS manages resource accounting per-process.
- explanation-04: Processes eliminate categories of concurrency bugs such as race conditions and deadlocks from shared mutable state, because each process's memory is isolated by default.
- explanation-04: Threads are preferred when work is I/O-bound.
- explanation-04: A web server handling many concurrent connections whose handlers share a cache is an example where threads are preferred.
- summarization-05: The payments database migration dry run is due before Thursday.
- summarization-05: Chen is assigned to continue search indexing work.
- summarization-08: The template gallery non-use is an additional observation rather than a core finding.

Added facts (styled only):

- code-review-01: The function has five distinct problems.
- code-review-01: The recommended fix is to catch a specific exception, such as whatever `db.insert` raises, and log it or re-raise it with context.
- code-review-01: Whether the lack of `name` validation matters depends on what `db.insert` and downstream code expect.
- code-review-01: It is worth checking whether the caller can guarantee a valid `name`.
- code-review-01: The mutable-default bug is the most serious of the five problems.
- code-review-01: The mutable-default bug is the one to fix first.
- code-review-03: The input `customer_name = "x' OR '1'='1"` causes the query to return every row.
- code-review-03: A value containing `'; DROP TABLE orders; --` can run arbitrary statements.
- code-review-03: Whether injected multiple statements run depends on the database driver's support for multiple statements.
- code-review-03: `%s` is the placeholder style for drivers such as `psycopg2` and `mysql-connector`.
- code-review-03: The function does not validate that `customer_name` and `status` are non-empty before use.
- code-review-03: A malformed query is an example of an exception source from `cursor.execute`.
- code-review-03: Whether the missing validation and error handling matters depends on what the caller already guarantees.
- debugging-04: 0xc3 is a common lead byte for UTF-8 multi-byte sequences.
- debugging-04: The character é encodes in UTF-8 as the bytes 0xc3 0xa9.
- debugging-04: The ascii codec only accepts bytes in the range 0 to 127.
- debugging-04: The ascii codec raises UnicodeDecodeError as soon as it encounters a byte outside 0-127.
- debugging-04: chardet is a library that can detect a file's encoding.
- debugging-08: The observed memory pattern indicates a true retention leak rather than simple cache growth.
- debugging-08: The most likely cause is evicted cache entries whose objects remain reachable through some other structure.
- debugging-08: If evicted entries are still referenced elsewhere, the object graph survives eviction.
- debugging-08: Structures that can retain evicted entries include per-entry listeners, subscriptions, a secondary index keyed by product ID, and metrics or 'recently viewed' maps.
- debugging-08: Comparing heap size before and after a manual cache flush or forced eviction tests whether evicted objects are still retained.
- debugging-08: If memory does not drop proportionally to what was evicted, something else still holds references to those objects.
- debugging-08: A heap dump taken at a memory peak can reveal the retained-size path from GC roots to evicted product objects.
- debugging-08: During marketing campaigns, product records likely carry more data such as extra images, variant lists, and promotional metadata.
- debugging-08: Baseline leak candidates include per-request objects, session state, and connection or thread-local buffers not released after a request completes.
- debugging-08: If growth per request is roughly the same on canary and production, the leak is tied to normal request handling rather than webhooks.
- debugging-08: Failure to return to baseline is consistent with a leak, an allocator that does not return freed memory to the OS, or native/off-heap allocations.
- debugging-08: Native or off-heap allocations, such as image processing and compression buffers, do not appear in normal heap statistics.
- debugging-08: If heap-used stays flat while RSS keeps climbing, the problem lies in native memory.
- debugging-08: Separating heap-used-after-GC from RSS should be done first because every other check depends on that distinction.
- debugging-08: Forcing cache eviction and checking whether memory drops is the check most likely to directly confirm or rule out the top suspect.
- debugging-08: Behavioral checks alone can only narrow the list of candidates.
- debugging-08: Only a heap dump can show the exact retaining structure.
- explanation-03: A network path might cross a fast data-center link or a slow, congested one.
- explanation-03: The initial congestion window value is typically 10 TCP segments, around 14KB.
- explanation-03: On packet loss, TCP cuts ssthresh, often to half the current cwnd.
- explanation-03: The name 'slow start' is misleading because its growth is exponential and fast relative to congestion avoidance.
- explanation-03: In the name 'slow start', 'slow' refers to the small starting point rather than the growth rate.
- explanation-03: Slow start is slow only compared to sending everything at once.
- explanation-04: Process creation cost is high because the OS allocates a new memory space.
- explanation-04: Thread creation cost is low because a thread reuses the parent's resources.
- explanation-04: Process context switch cost is high.
- explanation-04: Thread context switch cost is low.
- explanation-04: Some web servers fork a process per request.
- explanation-04: Multiple processes provide true CPU parallelism because each process gets its own interpreter and its own GIL.
- explanation-04: In most systems, threads cannot be killed independently.
- explanation-04: Killing a thread's process kills every thread in that process.
- summarization-08: The abandonment behavior is confirmed and costly.
- summarization-08: A sample of 8 users is too small to rule out other causes of the abandonment.
- summarization-08: The recommendation is to prioritize finding 2, the progress bar issue.
- summarization-08: A clearer progress indicator on large-file uploads is given as an example follow-up test.

### clarity-flow

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 28 | 19 | 0.679 | 29 | 3 |
| code-review-03 | 30 | 20 | 0.667 | 14 | 1 |
| debugging-04 | 11 | 8 | 0.727 | 11 | 2 |
| debugging-08 | 43 | 10 | 0.233 | 24 | 8 |
| explanation-03 | 29 | 19 | 0.655 | 17 | 2 |
| explanation-04 | 27 | 22 | 0.815 | 23 | 0 |
| summarization-05 | 9 | 9 | 1.0 | 6 | 0 |
| summarization-08 | 21 | 18 | 0.857 | 21 | 3 |

Median fraction: 0.703 over 8 scored pairs.

Median additions: 2.0 over 8 scored pairs.

Lost facts:

- code-review-01: `roles.append("member")` mutates the caller's list object in place.
- code-review-01: Mutating the caller's list is a surprising side effect if the caller reuses that list elsewhere.
- code-review-01: The function does not check whether `"member"` is already in `roles` before appending it.
- code-review-01: If `roles` already contains `"member"`, it gets appended again, producing duplicates.
- code-review-01: The function has no type hints and no docstring.
- code-review-01: The missing type hints and docstring are a minor issue.
- code-review-01: Without type hints or a docstring, the expected shape of `roles` (list of str) and the interface required of `db` (a `.insert` method) are unclear to callers.
- code-review-01: The cleaner version appends `"member"` only if it is not already in `roles`.
- code-review-01: Specific exceptions, such as `db`-related errors, can be caught at the call site instead.
- code-review-03: Any value containing a single quote character breaks out of the string literal in the query.
- code-review-03: The unhandled exception provides no context for the caller.
- code-review-03: The function has no type hints.
- code-review-03: The function has no docstring.
- code-review-03: Without type hints or a docstring, the expected shape of `cursor` is not documented.
- code-review-03: Without type hints or a docstring, the expected shape of the return value is not documented.
- code-review-03: The missing type hints and docstring are a minor issue.
- code-review-03: Missing type hints and docstrings are worth noting for a public or reusable function.
- code-review-03: The SQL injection is the only issue that actually matters in this code.
- code-review-03: All the other issues identified are secondary polish.
- debugging-04: The byte 0xc3 is likely part of a UTF-8 multi-byte sequence, such as an accented character.
- debugging-04: Passing errors="surrogateescape" to open enables a byte-for-byte round trip.
- debugging-04: charset-normalizer is a detection library that can determine a file's encoding before opening it.
- debugging-08: Failure to return to baseline overnight rules out normal cache eviction and GC working as intended.
- debugging-08: If a bounded cache were behaving correctly, quiet periods with no new unique products would let old entries evict.
- debugging-08: If GC were working as intended, it would reclaim short-lived garbage and the RSS/heap floor would flatten.
- debugging-08: The bounded cache has not changed in a year.
- debugging-08: A common failure mode of size-bounded caches is that the bound counts entries rather than bytes.
- debugging-08: If product payloads grow larger, the same entry count holds more memory.
- debugging-08: A common failure mode is cache keys including unbounded fields such as request ID, locale, or webhook payload variant.
- debugging-08: If key cardinality is effectively infinite, eviction never catches up.
- debugging-08: Cache key cardinality explosion is the most likely cause given the described profile.
- debugging-08: Campaigns produce more distinct products and promotions, and therefore more unique cache keys.
- debugging-08: The canary still serves some baseline product lookups.
- debugging-08: Comparing cache entry count against cache memory bytes over the day distinguishes key-cardinality growth from entry-size growth.
- debugging-08: If entry count is flat at the bound but memory climbs, the cause is unbounded entry size.
- debugging-08: If entry count is not flat at the configured bound, keys are being evicted improperly or the bound is not wired to the intended value.
- debugging-08: Sampling cache keys during a campaign versus a quiet week can reveal high-cardinality fields such as campaign ID, variant ID, or session ID in the key.
- debugging-08: Products may now carry additional data such as reviews, embeddings, and related-item lists, increasing entry size.
- debugging-08: Listener/handler leaks survive quiet periods.
- debugging-08: A listener leak would explain why the canary grows slowly from other event sources while normal instances grow faster.
- debugging-08: `jcmd GC.class_histogram` can count live objects on the JVM.
- debugging-08: `/debug/pprof/heap` can be used to count live objects in Go.
- debugging-08: `objgraph` can count live objects in Python.
- debugging-08: Daily class histograms can reveal which class counts climb monotonically.
- debugging-08: Connection pool metadata, open sockets, per-host retry/backoff state, and in-memory session/idempotency-key tracking can accumulate in memory.
- debugging-08: Webhook idempotency keys often use a TTL cache that does not actually expire entries.
- debugging-08: Memory that grows and does not return can be the allocator failing to return pages to the OS while live heap is fine.
- debugging-08: Allocator fragmentation is a red herring rather than a real leak.
- debugging-08: If live heap after a forced full GC stays elevated, the problem is a real leak.
- debugging-08: If used heap drops back near baseline after a forced GC, the behavior is allocator fragmentation and lower priority.
- debugging-08: No profiling tool currently exists for the service.
- debugging-08: `jmap -histo` produces object-count dumps on the JVM.
- debugging-08: Go supports `runtime.ReadMemStats` and pprof for object-count dumps.
- debugging-08: Node supports heap snapshots via `--inspect`.
- debugging-08: Python supports `tracemalloc` for memory tracking.
- explanation-03: Packet drops from buffer overflow degrade throughput for all users sharing the path.
- explanation-03: Historically, the initial cwnd was 1 segment.
- explanation-03: The initial cwnd is now typically 10 segments.
- explanation-03: RFC 6928 specifies the initial congestion window of 10 segments.
- explanation-03: Each time the sender receives an ACK confirming successful delivery, it increases cwnd by roughly one segment's worth.
- explanation-03: The slow start send pattern is approximately: send 10 segments, receive ACKs, send about 20, receive ACKs, send about 40, and so on.
- explanation-03: Congestion avoidance grows cwnd linearly rather than exponentially.
- explanation-03: Slow start is one piece of a broader system called congestion control.
- explanation-03: Congestion control continuously adjusts the sending rate to match available network capacity.
- explanation-03: Slow start handles the initial ramp-up and the re-ramp-up after a loss.
- explanation-04: Communication between processes requires explicit mechanisms such as pipes, sockets, shared memory, and message queues.
- explanation-04: Threads can corrupt each other's data without careful synchronization such as locks and mutexes.
- explanation-04: Processes eliminate categories of concurrency bugs such as race conditions and deadlocks from shared mutable state, because each process's memory is isolated by default.
- explanation-04: Threads are preferred when work is I/O-bound.
- explanation-04: A web server handling many concurrent connections whose handlers share a cache is an example where threads are preferred.
- summarization-08: The abandonment of imports is a firm, observed outcome.
- summarization-08: Whether the progress bar issue is purely a perception/UI issue or something deeper is tentative.
- summarization-08: The cause of the progress-bar-related abandonment needs more investigation.

Added facts (styled only):

- code-review-01: The function has four real bugs.
- code-review-01: The four bugs are listed in order of severity.
- code-review-01: The corrected version builds roles as `(roles or []) + ["member"]`.
- code-review-03: `SELECT *` breaks silently if columns are added or reordered.
- debugging-04: Adding errors="replace" or errors="ignore" to open() avoids crashing on malformed bytes.
- debugging-04: errors="replace" and errors="ignore" are useful when the file is not guaranteed to be valid UTF-8.
- debugging-08: If the memory slope tracks webhook request volume, the webhook handler can be instrumented with allocation tracking to find what is retained.
- debugging-08: Diffing heap snapshots before and after a burst of synthetic webhook calls can identify retained objects.
- debugging-08: Disabling background timers and cron jobs one at a time on the canary can reveal which one causes the growth.
- debugging-08: The bounded cache is probably not the main culprit.
- debugging-08: A bound enforced by nominal byte size can undercount when values are large.
- debugging-08: If RSS keeps climbing while reported cache size stays flat, the cache is not the source of the leak.
- debugging-08: A heap snapshot is the fastest way to disambiguate all three hypotheses.
- debugging-08: Disabling background jobs on the canary isolates the baseline leak from the webhook-triggered leak.
- explanation-03: Each acknowledgment received roughly doubles the congestion window for the next round.
- explanation-03: Each slow start round only doubles the risk rather than gambling everything at once.
- summarization-08: The field-mapping redesign result is the strongest result of the study.
- summarization-08: The finding that the progress bar stalls users on large files is rated as tentative.
- summarization-08: The abandonment behavior, not just the perception, makes the progress bar issue worth prioritizing.

### classic-concise

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 28 | 19 | 0.679 | 20 | 1 |
| code-review-03 | 30 | 22 | 0.733 | 26 | 5 |
| debugging-04 | 11 | 9 | 0.818 | 10 | 1 |
| debugging-08 | 43 | 22 | 0.512 | 43 | 18 |
| explanation-03 | 29 | 17 | 0.586 | 16 | 2 |
| explanation-04 | 27 | 20 | 0.741 | 26 | 3 |
| summarization-05 | 9 | 8 | 0.889 | 9 | 0 |
| summarization-08 | 21 | 19 | 0.905 | 20 | 2 |

Median fraction: 0.737 over 8 scored pairs.

Median additions: 2.0 over 8 scored pairs.

Lost facts:

- code-review-01: The function has no type hints and no docstring.
- code-review-01: The missing type hints and docstring are a minor issue.
- code-review-01: Without type hints or a docstring, the expected shape of `roles` (list of str) and the interface required of `db` (a `.insert` method) are unclear to callers.
- code-review-01: The cleaner version raises `ValueError("name is required")` when `name` is falsy.
- code-review-01: The cleaner version raises `ValueError("db is required")` when `db` is `None`.
- code-review-01: The cleaner version copies `roles` with `list(roles)` rather than mutating the caller's list.
- code-review-01: The cleaner version appends `"member"` only if it is not already in `roles`.
- code-review-01: The cleaner version calls `db.insert({"name": name, "roles": roles})` and returns `True`.
- code-review-01: Specific exceptions, such as `db`-related errors, can be caught at the call site instead.
- code-review-03: Any value containing a single quote character breaks out of the string literal in the query.
- code-review-03: `SELECT *` pulls unneeded columns.
- code-review-03: Nothing prevents `customer_name` or `status` from being `None` before reaching the database.
- code-review-03: Nothing prevents `customer_name` or `status` from being the wrong type before reaching the database.
- code-review-03: The missing type hints and docstring are a minor issue.
- code-review-03: Missing type hints and docstrings are worth noting for a public or reusable function.
- code-review-03: The SQL injection is the only issue that actually matters in this code.
- code-review-03: All the other issues identified are secondary polish.
- debugging-04: Passing errors="replace" to open allows decoding errors to be handled explicitly.
- debugging-04: Passing errors="surrogateescape" to open enables a byte-for-byte round trip.
- debugging-08: If a bounded cache were behaving correctly, quiet periods with no new unique products would let old entries evict.
- debugging-08: If GC were working as intended, it would reclaim short-lived garbage and the RSS/heap floor would flatten.
- debugging-08: A common failure mode is cache keys including unbounded fields such as request ID, locale, or webhook payload variant.
- debugging-08: If key cardinality is effectively infinite, eviction never catches up.
- debugging-08: A common failure mode is a bug in the eviction policy, such as uncleaned wrappers/decorators or soft/weak reference configs that do not reclaim.
- debugging-08: Cache key cardinality explosion is the most likely cause given the described profile.
- debugging-08: Campaigns produce more distinct products and promotions, and therefore more unique cache keys.
- debugging-08: The canary still serves some baseline product lookups.
- debugging-08: Comparing cache entry count against cache memory bytes over the day distinguishes key-cardinality growth from entry-size growth.
- debugging-08: If entry count is flat at the bound but memory climbs, the cause is unbounded entry size.
- debugging-08: If entry count is not flat at the configured bound, keys are being evicted improperly or the bound is not wired to the intended value.
- debugging-08: Sampling cache keys during a campaign versus a quiet week can reveal high-cardinality fields such as campaign ID, variant ID, or session ID in the key.
- debugging-08: `jcmd GC.class_histogram` can count live objects on the JVM.
- debugging-08: `objgraph` can count live objects in Python.
- debugging-08: Webhook idempotency keys often use a TTL cache that does not actually expire entries.
- debugging-08: Memory that grows and does not return can be the allocator failing to return pages to the OS while live heap is fine.
- debugging-08: Allocator fragmentation is a red herring rather than a real leak.
- debugging-08: If live heap after a forced full GC stays elevated, the problem is a real leak.
- debugging-08: If used heap drops back near baseline after a forced GC, the behavior is allocator fragmentation and lower priority.
- debugging-08: No profiling tool currently exists for the service.
- debugging-08: Python supports `tracemalloc` for memory tracking.
- explanation-03: Packet drops from buffer overflow degrade throughput for all users sharing the path.
- explanation-03: The congestion window is the amount of unacknowledged data the sender is allowed to have in flight.
- explanation-03: Historically, the initial cwnd was 1 segment.
- explanation-03: The initial cwnd is now typically 10 segments.
- explanation-03: RFC 6928 specifies the initial congestion window of 10 segments.
- explanation-03: The slow start send pattern is approximately: send 10 segments, receive ACKs, send about 20, receive ACKs, send about 40, and so on.
- explanation-03: Growing cwnd by one segment per RTT would be painfully slow for high-bandwidth links.
- explanation-03: On detecting loss, the sender backs off significantly and switches to congestion avoidance.
- explanation-03: Congestion avoidance grows cwnd linearly rather than exponentially.
- explanation-03: ssthresh is often set based on a previous congestion event.
- explanation-03: Congestion control continuously adjusts the sending rate to match available network capacity.
- explanation-03: Slow start handles the initial ramp-up and the re-ramp-up after a loss.
- explanation-04: Each thread has its own stack and register state.
- explanation-04: Threads can corrupt each other's data without careful synchronization such as locks and mutexes.
- explanation-04: Chrome runs each tab or worker as a separate process so one bad renderer doesn't kill the whole browser.
- explanation-04: Processes eliminate categories of concurrency bugs such as race conditions and deadlocks from shared mutable state, because each process's memory is isolated by default.
- explanation-04: Threads are preferred when work is I/O-bound.
- explanation-04: A web server handling many concurrent connections whose handlers share a cache is an example where threads are preferred.
- explanation-04: Parallel algorithms operating on the same large in-memory dataset are an example where threads are preferred.
- summarization-05: Chen is assigned to continue search indexing work.
- summarization-08: The abandonment of imports is a firm, observed outcome.
- summarization-08: The cause of the progress-bar-related abandonment needs more investigation.

Added facts (styled only):

- code-review-01: Using `roles = roles + ["member"]` builds a new list instead of mutating the caller's list.
- code-review-03: An attacker could drop tables through the injection.
- code-review-03: `SELECT *` breaks silently when columns are added, reordered, or renamed.
- code-review-03: `status` presumably comes from a fixed set of values, such as "pending" or "shipped".
- code-review-03: Nothing checks `status` against its allowed set of values before it reaches the query.
- code-review-03: Causes of a raised exception include a bad connection, a lock timeout, or a syntax error.
- debugging-04: A file's encoding can be detected with the chardet library.
- debugging-08: The bounded cache is a secondary suspect.
- debugging-08: Candidate causes of the baseline leak include thread-local accumulation.
- debugging-08: Candidate causes of the baseline leak include metrics-library internal state.
- debugging-08: jmap and JFR are heap dump tools for the JVM.
- debugging-08: Candidate causes of the traffic-proportional leak include growing metric label cardinality.
- debugging-08: Adding a campaign-ID label to a counter or histogram causes each new campaign to add permanent entries to the metrics registry.
- debugging-08: A linear relationship between memory growth rate and webhook request rate would confirm the traffic-proportional leak.
- debugging-08: The bounded cache is unlikely to be the primary driver of the leak.
- debugging-08: Evicted cache entries can remain referenced elsewhere, such as by a longer-lived object or captured in a closure or callback.
- debugging-08: Product payloads have grown over the year.
- debugging-08: Logging cache eviction events allows confirming that the eviction rate matches the insertion rate.
- debugging-08: Retained size, not shallow size, is the relevant measure when checking cached objects in a heap dump.
- debugging-08: If evicted objects still appear reachable in a heap dump, another reference holder exists.
- debugging-08: High webhook volume often means more HTTP client connections, TLS buffers, or compression buffers.
- debugging-08: HTTP client connections, TLS buffers, and compression buffers can leak in native memory even when the managed heap looks fine.
- debugging-08: Comparing process RSS to reported heap size can detect off-heap or native memory leaks.
- debugging-08: If RSS grows faster than heap, the cause is likely direct or native allocations such as HTTP client libraries or JSON/gzip codecs.
- debugging-08: Taking a heap dump is the fastest way to confirm which of the four hypotheses is correct.
- explanation-03: The name "slow start" is a misnomer because the window grows exponentially fast, though it starts small.
- explanation-03: Bandwidth, buffer sizes, and competing traffic on shared links are unknown to the sender.
- explanation-04: Python and Ruby have a global interpreter lock.
- explanation-04: Threads are preferable when the language runtime supports true parallel execution.
- explanation-04: Go, Java, C++, and Rust support true parallel execution in threads.
- summarization-08: The progress bar issue is a matter of perception rather than actual failure.
- summarization-08: The progress bar finding is rated as tentative but risky.

### developer-docs

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 28 | 20 | 0.714 | 29 | 3 |
| code-review-03 | 30 | 20 | 0.667 | 21 | 5 |
| debugging-04 | 11 | 8 | 0.727 | 13 | 2 |
| debugging-08 | 43 | 0 | 0.0 | 4 | 4 |
| explanation-03 | 29 | 24 | 0.828 | 26 | 5 |
| explanation-04 | 27 | 22 | 0.815 | 35 | 3 |
| summarization-05 | 9 | 9 | 1.0 | 11 | 1 |
| summarization-08 | 21 | 21 | 1.0 | 21 | 1 |

Median fraction: 0.771 over 8 scored pairs.

Median additions: 3.0 over 8 scored pairs.

Lost facts:

- code-review-01: The function does not check whether `"member"` is already in `roles` before appending it.
- code-review-01: If `roles` already contains `"member"`, it gets appended again, producing duplicates.
- code-review-01: The function has no type hints and no docstring.
- code-review-01: The missing type hints and docstring are a minor issue.
- code-review-01: The cleaner version raises `ValueError("name is required")` when `name` is falsy.
- code-review-01: The cleaner version appends `"member"` only if it is not already in `roles`.
- code-review-01: The cleaner version lets exceptions propagate instead of masking failures as a plain `False`.
- code-review-01: Specific exceptions, such as `db`-related errors, can be caught at the call site instead.
- code-review-03: Any value containing a single quote character breaks out of the string literal in the query.
- code-review-03: Breaking out of the string literal lets an attacker read arbitrary data.
- code-review-03: Breaking out of the string literal lets an attacker modify arbitrary data.
- code-review-03: The unhandled exception provides no context for the caller.
- code-review-03: The function has no type hints.
- code-review-03: The function has no docstring.
- code-review-03: Without type hints or a docstring, the expected shape of `cursor` is not documented.
- code-review-03: The missing type hints and docstring are a minor issue.
- code-review-03: Missing type hints and docstrings are worth noting for a public or reusable function.
- code-review-03: The SQL injection is the only issue that actually matters in this code.
- debugging-04: The code opens the file with encoding forced to "ascii".
- debugging-04: Passing errors="surrogateescape" to open enables a byte-for-byte round trip.
- debugging-04: charset-normalizer is a detection library that can determine a file's encoding before opening it.
- debugging-08: The canary instance's memory still grows without webhooks, but more slowly than normal instances.
- debugging-08: Memory growth that is traffic-correlated but not traffic-exclusive implies at least two contributors.
- debugging-08: One contributor is baseline/time-driven, such as background jobs, scheduled tasks, connection pools, or internal timers.
- debugging-08: One contributor is traffic-driven and amplified by campaigns.
- debugging-08: Memory never returns to baseline overnight.
- debugging-08: Failure to return to baseline overnight rules out normal cache eviction and GC working as intended.
- debugging-08: If a bounded cache were behaving correctly, quiet periods with no new unique products would let old entries evict.
- debugging-08: If GC were working as intended, it would reclaim short-lived garbage and the RSS/heap floor would flatten.
- debugging-08: A rising memory floor indicates something unbounded or a bound that is not actually enforced.
- debugging-08: The bounded cache has not changed in a year.
- debugging-08: A cache being stable and trusted does not exclude it as a suspect.
- debugging-08: A common failure mode of size-bounded caches is that the bound counts entries rather than bytes.
- debugging-08: If product payloads grow larger, the same entry count holds more memory.
- debugging-08: A common failure mode is cache keys including unbounded fields such as request ID, locale, or webhook payload variant.
- debugging-08: If key cardinality is effectively infinite, eviction never catches up.
- debugging-08: A common failure mode is a bug in the eviction policy, such as uncleaned wrappers/decorators or soft/weak reference configs that do not reclaim.
- debugging-08: Cache key cardinality explosion is the most likely cause given the described profile.
- debugging-08: Campaigns produce more distinct products and promotions, and therefore more unique cache keys.
- debugging-08: The canary still serves some baseline product lookups.
- debugging-08: Comparing cache entry count against cache memory bytes over the day distinguishes key-cardinality growth from entry-size growth.
- debugging-08: If entry count is flat at the bound but memory climbs, the cause is unbounded entry size.
- debugging-08: If entry count is not flat at the configured bound, keys are being evicted improperly or the bound is not wired to the intended value.
- debugging-08: Sampling cache keys during a campaign versus a quiet week can reveal high-cardinality fields such as campaign ID, variant ID, or session ID in the key.
- debugging-08: Products may now carry additional data such as reviews, embeddings, and related-item lists, increasing entry size.
- debugging-08: Each webhook or background poll may register a callback, subscription, or timer that is never deregistered.
- debugging-08: Listener/handler leaks survive quiet periods.
- debugging-08: A listener leak would explain why the canary grows slowly from other event sources while normal instances grow faster.
- debugging-08: `jcmd GC.class_histogram` can count live objects on the JVM.
- debugging-08: `/debug/pprof/heap` can be used to count live objects in Go.
- debugging-08: `objgraph` can count live objects in Python.
- debugging-08: Daily class histograms can reveal which class counts climb monotonically.
- debugging-08: Connection pool metadata, open sockets, per-host retry/backoff state, and in-memory session/idempotency-key tracking can accumulate in memory.
- debugging-08: Webhook idempotency keys often use a TTL cache that does not actually expire entries.
- debugging-08: Memory that grows and does not return can be the allocator failing to return pages to the OS while live heap is fine.
- debugging-08: Allocator fragmentation is a red herring rather than a real leak.
- debugging-08: If live heap after a forced full GC stays elevated, the problem is a real leak.
- debugging-08: If used heap drops back near baseline after a forced GC, the behavior is allocator fragmentation and lower priority.
- debugging-08: No profiling tool currently exists for the service.
- debugging-08: `jmap -histo` produces object-count dumps on the JVM.
- debugging-08: Go supports `runtime.ReadMemStats` and pprof for object-count dumps.
- debugging-08: Node supports heap snapshots via `--inspect`.
- debugging-08: Python supports `tracemalloc` for memory tracking.
- debugging-08: Running instrumentation on both a normal instance and the canary across a campaign isolates traffic-driven from baseline-driven contributors.
- explanation-03: RFC 6928 specifies the initial congestion window of 10 segments.
- explanation-03: Growing cwnd by one segment per RTT would be painfully slow for high-bandwidth links.
- explanation-03: On detecting loss, the sender backs off significantly and switches to congestion avoidance.
- explanation-03: ssthresh is often set based on a previous congestion event.
- explanation-03: Slow start handles the initial ramp-up and the re-ramp-up after a loss.
- explanation-04: Each thread has its own stack and register state.
- explanation-04: Threads can corrupt each other's data without careful synchronization such as locks and mutexes.
- explanation-04: Processes eliminate categories of concurrency bugs such as race conditions and deadlocks from shared mutable state, because each process's memory is isolated by default.
- explanation-04: A web server handling many concurrent connections whose handlers share a cache is an example where threads are preferred.
- explanation-04: Parallel algorithms operating on the same large in-memory dataset are an example where threads are preferred.

Added facts (styled only):

- code-review-01: The corrected version has the signature `def add_user(name: str, roles: list[str] | None = None, db=None) -> bool`.
- code-review-01: The corrected version calls `db.insert({"name": name, "roles": roles})` inside a `try` block and returns `True` on success.
- code-review-01: The corrected version catches `Exception as e`, logs it with `logging.error("Failed to insert user %s: %s", name, e)`, and returns `False`.
- code-review-03: An attacker can pass a value containing a semicolon to chain additional SQL statements.
- code-review-03: psycopg2 and MySQLdb use `%s` as the parameter placeholder.
- code-review-03: Naming the columns you need makes the query's intent clear.
- code-review-03: The output of `cursor.fetchall()` varies by driver, and can be a list of tuples, dicts, or driver-specific row objects.
- code-review-03: A caller cannot determine the function's return type without reading the driver's documentation.
- debugging-04: The `ascii` codec only supports the first 128 Unicode code points.
- debugging-04: `chardet` is a library that can detect a file's encoding.
- debugging-08: The assistant is checking its memory for prior context about the service in question.
- debugging-08: The assistant issues a file_glob tool call to search a memory directory.
- debugging-08: The memory directory searched is /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-m13ks_z4/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-s98z926i/memory/.
- debugging-08: The glob pattern used in the search is "*", matching all files.
- explanation-03: A network path may be a fast local link or a congested connection shared by thousands of other flows.
- explanation-03: Filling router queues and dropping packets causes congestion collapse.
- explanation-03: In congestion collapse, throughput drops for everyone even though the network carries plenty of traffic.
- explanation-03: Slow start growth continues until the sender detects a sign of congestion, such as a packet loss or an explicit congestion signal.
- explanation-03: Slow start trades a small amount of initial delay for protection against congestion collapse.
- explanation-04: Python and Ruby use a global interpreter lock.
- explanation-04: Multiple processes bypass the global interpreter lock because each process gets its own interpreter and its own lock.
- explanation-04: Supervisor patterns include systemd and Kubernetes pods.
- summarization-05: The speaker will check their memory directory for relevant context before responding.
- summarization-08: The finding about progress bar confusion is tentative.

### plain-language

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 28 | 20 | 0.714 | 20 | 3 |
| code-review-03 | 30 | 20 | 0.667 | 19 | 4 |
| debugging-04 | 11 | 7 | 0.636 | 17 | 7 |
| debugging-08 | 43 | 20 | 0.465 | 28 | 8 |
| explanation-03 | 29 | 14 | 0.483 | 24 | 3 |
| explanation-04 | 27 | 16 | 0.593 | 30 | 3 |
| summarization-05 | 9 | 7 | 0.778 | 10 | 0 |
| summarization-08 | 21 | 21 | 1.0 | 23 | 1 |

Median fraction: 0.651 over 8 scored pairs.

Median additions: 3.0 over 8 scored pairs.

Lost facts:

- code-review-01: `roles.append("member")` mutates the caller's list object in place.
- code-review-01: Mutating the caller's list is a surprising side effect if the caller reuses that list elsewhere.
- code-review-01: The function does not check whether `"member"` is already in `roles` before appending it.
- code-review-01: If `roles` already contains `"member"`, it gets appended again, producing duplicates.
- code-review-01: The function has no type hints and no docstring.
- code-review-01: The missing type hints and docstring are a minor issue.
- code-review-01: Without type hints or a docstring, the expected shape of `roles` (list of str) and the interface required of `db` (a `.insert` method) are unclear to callers.
- code-review-01: The cleaner version appends `"member"` only if it is not already in `roles`.
- code-review-03: The SQL injection vulnerability is critical in severity.
- code-review-03: Any value containing a single quote character breaks out of the string literal in the query.
- code-review-03: The function has no type hints.
- code-review-03: The function has no docstring.
- code-review-03: Without type hints or a docstring, the expected shape of `cursor` is not documented.
- code-review-03: Without type hints or a docstring, the expected shape of the return value is not documented.
- code-review-03: The missing type hints and docstring are a minor issue.
- code-review-03: Missing type hints and docstrings are worth noting for a public or reusable function.
- code-review-03: The SQL injection is the only issue that actually matters in this code.
- code-review-03: All the other issues identified are secondary polish.
- debugging-04: Decoding fails as soon as it reaches the non-ASCII byte.
- debugging-04: Passing errors="surrogateescape" to open enables a byte-for-byte round trip.
- debugging-04: Opening a file in binary mode ("rb") avoids decoding altogether.
- debugging-04: Counting lines in binary mode sidesteps encoding issues because only line boundaries are needed, not the text content.
- debugging-08: Memory never returns to baseline overnight.
- debugging-08: Failure to return to baseline overnight rules out normal cache eviction and GC working as intended.
- debugging-08: If a bounded cache were behaving correctly, quiet periods with no new unique products would let old entries evict.
- debugging-08: If GC were working as intended, it would reclaim short-lived garbage and the RSS/heap floor would flatten.
- debugging-08: A rising memory floor indicates something unbounded or a bound that is not actually enforced.
- debugging-08: A common failure mode is cache keys including unbounded fields such as request ID, locale, or webhook payload variant.
- debugging-08: If key cardinality is effectively infinite, eviction never catches up.
- debugging-08: A common failure mode is a bug in the eviction policy, such as uncleaned wrappers/decorators or soft/weak reference configs that do not reclaim.
- debugging-08: Cache key cardinality explosion is the most likely cause given the described profile.
- debugging-08: The canary still serves some baseline product lookups.
- debugging-08: If entry count is not flat at the configured bound, keys are being evicted improperly or the bound is not wired to the intended value.
- debugging-08: Sampling cache keys during a campaign versus a quiet week can reveal high-cardinality fields such as campaign ID, variant ID, or session ID in the key.
- debugging-08: A listener leak would explain why the canary grows slowly from other event sources while normal instances grow faster.
- debugging-08: `jcmd GC.class_histogram` can count live objects on the JVM.
- debugging-08: `/debug/pprof/heap` can be used to count live objects in Go.
- debugging-08: `objgraph` can count live objects in Python.
- debugging-08: Connection pool metadata, open sockets, per-host retry/backoff state, and in-memory session/idempotency-key tracking can accumulate in memory.
- debugging-08: Webhook idempotency keys often use a TTL cache that does not actually expire entries.
- debugging-08: No profiling tool currently exists for the service.
- debugging-08: `jmap -histo` produces object-count dumps on the JVM.
- debugging-08: Go supports `runtime.ReadMemStats` and pprof for object-count dumps.
- debugging-08: Node supports heap snapshots via `--inspect`.
- debugging-08: Python supports `tracemalloc` for memory tracking.
- explanation-03: Routers along a network path have limited buffer space.
- explanation-03: Packet drops from buffer overflow degrade throughput for all users sharing the path.
- explanation-03: The congestion window is the amount of unacknowledged data the sender is allowed to have in flight.
- explanation-03: Historically, the initial cwnd was 1 segment.
- explanation-03: The initial cwnd is now typically 10 segments.
- explanation-03: RFC 6928 specifies the initial congestion window of 10 segments.
- explanation-03: Each time the sender receives an ACK confirming successful delivery, it increases cwnd by roughly one segment's worth.
- explanation-03: The slow start send pattern is approximately: send 10 segments, receive ACKs, send about 20, receive ACKs, send about 40, and so on.
- explanation-03: Growing cwnd by one segment per RTT would be painfully slow for high-bandwidth links.
- explanation-03: On detecting loss, the sender backs off significantly and switches to congestion avoidance.
- explanation-03: Congestion avoidance grows cwnd linearly rather than exponentially.
- explanation-03: ssthresh is often set based on a previous congestion event.
- explanation-03: Slow start is one piece of a broader system called congestion control.
- explanation-03: Congestion control continuously adjusts the sending rate to match available network capacity.
- explanation-03: Slow start handles the initial ramp-up and the re-ramp-up after a loss.
- explanation-04: A process is an independent execution unit with its own memory address space, file descriptors, and OS resources.
- explanation-04: All threads in a process share the same address space, heap, and file descriptors.
- explanation-04: Each thread has its own stack and register state.
- explanation-04: Threads can corrupt each other's data without careful synchronization such as locks and mutexes.
- explanation-04: Chrome runs each tab or worker as a separate process so one bad renderer doesn't kill the whole browser.
- explanation-04: Separate processes make independent starting, stopping, and resource limiting (memory caps, CPU quotas via cgroups) natural.
- explanation-04: The OS manages resource accounting per-process.
- explanation-04: Processes eliminate categories of concurrency bugs such as race conditions and deadlocks from shared mutable state, because each process's memory is isolated by default.
- explanation-04: Threads are preferred when work is I/O-bound.
- explanation-04: A web server handling many concurrent connections whose handlers share a cache is an example where threads are preferred.
- explanation-04: Parallel algorithms operating on the same large in-memory dataset are an example where threads are preferred.
- summarization-05: The payments database migration dry run is due before Thursday.
- summarization-05: Ada is assigned to check with the mobile team's lead about whether the mobile team was informed about the API deprecation.

Added facts (styled only):

- code-review-01: The function contains five problems.
- code-review-01: The corrected version raises `ValueError` with the message "name must not be empty" when `name` is falsy.
- code-review-01: The corrected version raises `ValueError` with the message "db must be provided" when `db` is `None`.
- code-review-03: Libraries such as psycopg2 and MySQLdb use `%s` as the parameter placeholder.
- code-review-03: The function imposes no limit on the number of results returned.
- code-review-03: Returning all orders for a customer at once can consume a lot of memory.
- code-review-03: A `LIMIT` clause or pagination is advisable for large result sets.
- debugging-04: ASCII only covers characters 0-127.
- debugging-04: The byte 0xc3 at position 512 is part of a non-ASCII character.
- debugging-04: UTF-8 can read plain ASCII text.
- debugging-04: Switching to UTF-8 will not break files that were already ASCII-only.
- debugging-04: open() accepts an errors argument with values "replace" or "ignore".
- debugging-04: Using errors="replace" or errors="ignore" lets the function keep running despite bad bytes.
- debugging-04: Skipping bad bytes may miscount lines if the bad bytes include a line break.
- debugging-08: Candidate sources of a request-independent leak include a scheduled job, a metrics collector, a connection pool, or a logger that buffers without limit.
- debugging-08: If heap size climbs by roughly one unit per event and never comes back down after the instance goes idle, a per-webhook leak is confirmed.
- debugging-08: Campaigns often add promotional fields or seasonal variants to product data.
- debugging-08: A collection keyed by product ID that is not covered by the cache's size bound can grow with the number of unique products touched rather than with request count.
- debugging-08: Examples of hidden per-product structures include a dedup set, a per-product counter, and a 'recently viewed' list.
- debugging-08: A synthetic webhook burst test isolates the per-webhook leak cause.
- debugging-08: Given that no heap profile exists, taking a heap dump on the canary is the highest-value first investigative step.
- debugging-08: A heap dump will likely reveal whether the baseline leak consists of a few large objects or many small ones, narrowing the search.
- explanation-03: Dropped packets force the sender to resend data, which slows everything down.
- explanation-03: The name 'slow start' is misleading because the growth is actually fast.
- explanation-03: The name 'slow start' comes from the fact that the connection starts small compared to sending everything at once.
- explanation-04: The standard implementations of Python and Ruby let only one thread run interpreted code at a time, even on a multi-core machine.
- explanation-04: Both processes and threads can use multiple cores.
- explanation-04: Running several worker processes behind a load balancer is common in server setups.
- summarization-08: The customers already had templates.

### technical-simplified

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-01 | 28 | 19 | 0.679 | 17 | 1 |
| code-review-03 | 30 | 0 | 0.0 | 7 | 7 |
| debugging-04 | 11 | 7 | 0.636 | 14 | 4 |
| debugging-08 | 43 | 0 | 0.0 | 8 | 8 |
| explanation-04 | 27 | 13 | 0.481 | 28 | 2 |
| summarization-05 | 9 | 8 | 0.889 | 9 | 1 |

Median fraction: 0.558 over 6 scored pairs.

Median additions: 3.0 over 6 scored pairs.

Lost facts:

- code-review-01: The function does not check whether `"member"` is already in `roles` before appending it.
- code-review-01: If `roles` already contains `"member"`, it gets appended again, producing duplicates.
- code-review-01: The function has no type hints and no docstring.
- code-review-01: The missing type hints and docstring are a minor issue.
- code-review-01: Without type hints or a docstring, the expected shape of `roles` (list of str) and the interface required of `db` (a `.insert` method) are unclear to callers.
- code-review-01: The cleaner version raises `ValueError("name is required")` when `name` is falsy.
- code-review-01: The cleaner version copies `roles` with `list(roles)` rather than mutating the caller's list.
- code-review-01: The cleaner version appends `"member"` only if it is not already in `roles`.
- code-review-01: Specific exceptions, such as `db`-related errors, can be caught at the call site instead.
- code-review-03: The `customer_name` and `status` values are concatenated directly into the query string.
- code-review-03: The code contains a SQL injection vulnerability.
- code-review-03: The SQL injection vulnerability is critical in severity.
- code-review-03: Any value containing a single quote character breaks out of the string literal in the query.
- code-review-03: Breaking out of the string literal lets an attacker read arbitrary data.
- code-review-03: Breaking out of the string literal lets an attacker modify arbitrary data.
- code-review-03: Passing `status` the value `' OR '1'='1` is an example of an injection payload.
- code-review-03: The fix for the SQL injection is to use parameterized queries.
- code-review-03: In the parameterized version, the query string uses `%s` placeholders for the customer and status values.
- code-review-03: In the parameterized version, the parameters are passed to `cursor.execute` as a tuple.
- code-review-03: The `?` placeholder style should be used instead of `%s` for sqlite3.
- code-review-03: Some DB-API drivers expect qmark placeholder style.
- code-review-03: The query uses `SELECT *`.
- code-review-03: `SELECT *` is fragile against schema changes.
- code-review-03: `SELECT *` pulls unneeded columns.
- code-review-03: Explicit column names are preferable to `SELECT *`.
- code-review-03: The function has no input validation.
- code-review-03: Nothing prevents `customer_name` or `status` from being `None` before reaching the database.
- code-review-03: Nothing prevents `customer_name` or `status` from being the wrong type before reaching the database.
- code-review-03: The function has no error handling.
- code-review-03: A database error such as a bad connection will propagate as an unhandled exception.
- code-review-03: The unhandled exception provides no context for the caller.
- code-review-03: The function has no type hints.
- code-review-03: The function has no docstring.
- code-review-03: Without type hints or a docstring, the expected shape of `cursor` is not documented.
- code-review-03: Without type hints or a docstring, the expected shape of the return value is not documented.
- code-review-03: The missing type hints and docstring are a minor issue.
- code-review-03: Missing type hints and docstrings are worth noting for a public or reusable function.
- code-review-03: The SQL injection is the only issue that actually matters in this code.
- code-review-03: All the other issues identified are secondary polish.
- debugging-04: Passing errors="surrogateescape" to open enables a byte-for-byte round trip.
- debugging-04: charset-normalizer is a detection library that can determine a file's encoding before opening it.
- debugging-04: Opening a file in binary mode ("rb") avoids decoding altogether.
- debugging-04: Counting lines in binary mode sidesteps encoding issues because only line boundaries are needed, not the text content.
- debugging-08: The canary instance's memory still grows without webhooks, but more slowly than normal instances.
- debugging-08: Memory growth that is traffic-correlated but not traffic-exclusive implies at least two contributors.
- debugging-08: One contributor is baseline/time-driven, such as background jobs, scheduled tasks, connection pools, or internal timers.
- debugging-08: One contributor is traffic-driven and amplified by campaigns.
- debugging-08: Memory never returns to baseline overnight.
- debugging-08: Failure to return to baseline overnight rules out normal cache eviction and GC working as intended.
- debugging-08: If a bounded cache were behaving correctly, quiet periods with no new unique products would let old entries evict.
- debugging-08: If GC were working as intended, it would reclaim short-lived garbage and the RSS/heap floor would flatten.
- debugging-08: A rising memory floor indicates something unbounded or a bound that is not actually enforced.
- debugging-08: The bounded cache has not changed in a year.
- debugging-08: A cache being stable and trusted does not exclude it as a suspect.
- debugging-08: A common failure mode of size-bounded caches is that the bound counts entries rather than bytes.
- debugging-08: If product payloads grow larger, the same entry count holds more memory.
- debugging-08: A common failure mode is cache keys including unbounded fields such as request ID, locale, or webhook payload variant.
- debugging-08: If key cardinality is effectively infinite, eviction never catches up.
- debugging-08: A common failure mode is a bug in the eviction policy, such as uncleaned wrappers/decorators or soft/weak reference configs that do not reclaim.
- debugging-08: Cache key cardinality explosion is the most likely cause given the described profile.
- debugging-08: Campaigns produce more distinct products and promotions, and therefore more unique cache keys.
- debugging-08: The canary still serves some baseline product lookups.
- debugging-08: Comparing cache entry count against cache memory bytes over the day distinguishes key-cardinality growth from entry-size growth.
- debugging-08: If entry count is flat at the bound but memory climbs, the cause is unbounded entry size.
- debugging-08: If entry count is not flat at the configured bound, keys are being evicted improperly or the bound is not wired to the intended value.
- debugging-08: Sampling cache keys during a campaign versus a quiet week can reveal high-cardinality fields such as campaign ID, variant ID, or session ID in the key.
- debugging-08: Products may now carry additional data such as reviews, embeddings, and related-item lists, increasing entry size.
- debugging-08: Each webhook or background poll may register a callback, subscription, or timer that is never deregistered.
- debugging-08: Listener/handler leaks survive quiet periods.
- debugging-08: A listener leak would explain why the canary grows slowly from other event sources while normal instances grow faster.
- debugging-08: `jcmd GC.class_histogram` can count live objects on the JVM.
- debugging-08: `/debug/pprof/heap` can be used to count live objects in Go.
- debugging-08: `objgraph` can count live objects in Python.
- debugging-08: Daily class histograms can reveal which class counts climb monotonically.
- debugging-08: Connection pool metadata, open sockets, per-host retry/backoff state, and in-memory session/idempotency-key tracking can accumulate in memory.
- debugging-08: Webhook idempotency keys often use a TTL cache that does not actually expire entries.
- debugging-08: Memory that grows and does not return can be the allocator failing to return pages to the OS while live heap is fine.
- debugging-08: Allocator fragmentation is a red herring rather than a real leak.
- debugging-08: If live heap after a forced full GC stays elevated, the problem is a real leak.
- debugging-08: If used heap drops back near baseline after a forced GC, the behavior is allocator fragmentation and lower priority.
- debugging-08: No profiling tool currently exists for the service.
- debugging-08: `jmap -histo` produces object-count dumps on the JVM.
- debugging-08: Go supports `runtime.ReadMemStats` and pprof for object-count dumps.
- debugging-08: Node supports heap snapshots via `--inspect`.
- debugging-08: Python supports `tracemalloc` for memory tracking.
- debugging-08: Running instrumentation on both a normal instance and the canary across a campaign isolates traffic-driven from baseline-driven contributors.
- explanation-04: A process is an independent execution unit with its own memory address space, file descriptors, and OS resources.
- explanation-04: Communication between processes requires explicit mechanisms such as pipes, sockets, shared memory, and message queues.
- explanation-04: All threads in a process share the same address space, heap, and file descriptors.
- explanation-04: Each thread has its own stack and register state.
- explanation-04: Threads can corrupt each other's data without careful synchronization such as locks and mutexes.
- explanation-04: Chrome runs each tab or worker as a separate process so one bad renderer doesn't kill the whole browser.
- explanation-04: Separate processes allow use of OS-level protections such as memory isolation, separate permissions, and seccomp/capabilities.
- explanation-04: Threads cannot provide OS-level security protections because threads share everything.
- explanation-04: Separate processes make independent starting, stopping, and resource limiting (memory caps, CPU quotas via cgroups) natural.
- explanation-04: The OS manages resource accounting per-process.
- explanation-04: Processes eliminate categories of concurrency bugs such as race conditions and deadlocks from shared mutable state, because each process's memory is isolated by default.
- explanation-04: Threads are preferred when work is I/O-bound.
- explanation-04: A web server handling many concurrent connections whose handlers share a cache is an example where threads are preferred.
- explanation-04: Parallel algorithms operating on the same large in-memory dataset are an example where threads are preferred.
- summarization-05: Ada is assigned to check with the mobile team's lead about whether the mobile team was informed about the API deprecation.

Added facts (styled only):

- code-review-01: The expression `roles = roles + ["member"]` creates a copy of `roles` instead of mutating the list the caller passed in.
- code-review-03: The speaker checks memory for relevant context before doing anything else.
- code-review-03: The speaker invokes the bash tool.
- code-review-03: The bash command runs `cat` on the file /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-m13ks_z4/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-s98z926i/memory/MEMORY.md
- code-review-03: The memory index file is named MEMORY.md.
- code-review-03: The command redirects stderr to /dev/null to suppress errors.
- code-review-03: The command echoes 'No memory file' if the cat command fails.
- code-review-03: The bash command's description is 'Check memory index'.
- debugging-04: Python raises UnicodeDecodeError when decoding a byte above 127 as ascii.
- debugging-04: errors="replace" keeps the line count correct.
- debugging-04: errors="replace" does not remove line breaks.
- debugging-04: errors="replace" replaces bad bytes with a placeholder character.
- debugging-08: The assistant will check memory for prior context before answering.
- debugging-08: The prior context being sought concerns an order service.
- debugging-08: A bash tool call is issued.
- debugging-08: The command runs `cat` on a MEMORY.md file.
- debugging-08: The MEMORY.md file is located at /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-m13ks_z4/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-s98z926i/memory/MEMORY.md
- debugging-08: The command suppresses error output by redirecting stderr to /dev/null.
- debugging-08: The command echoes "NO_MEMORY_FILE" if the cat command fails.
- debugging-08: The stated description of the command is to check the memory index for prior context.
- explanation-04: A crashed thread can bring down the whole process because threads share memory.
- explanation-04: In old versions of Ruby, only one thread runs code at a time, even on many cores.
- summarization-05: The text lists action items from a meeting.

## Hedging survival

The judge lists the claims that the unstyled answer presents with uncertainty, then judges each claim in the styled answer: hedged (the uncertainty survives in some form), certain (the claim survives but reads as a fact — the failure this check targets), or absent (the claim is gone, a completeness loss). Survival is hedged / (hedged + certain). The claims that became certain appear verbatim below the table.

### actionable-clarity

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 2 | 0 | 0.0 |
| code-review-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 2 | 2 | 0 | 0 | 1.0 |
| debugging-08 | 9 | 2 | 1 | 6 | 0.667 |
| explanation-03 | 0 | 0 | 0 | 0 | n/a |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 16 over 8 judged pairs: 7 hedged, 3 certain, 6 absent.

Median survival: 0.834 over 4 scored pairs.

Claims that became certain:

- code-review-01: The expected shape of `roles` is unclear — possibly a list of str.
- code-review-01: The interface expected of `db` is unclear — possibly something providing `.insert`.
- debugging-08: The five listed items are plausible causes of the memory growth.

### clarity-flow

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 2 | 0 | 0.0 |
| code-review-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 2 | 2 | 0 | 0 | 1.0 |
| debugging-08 | 9 | 2 | 0 | 7 | 1.0 |
| explanation-03 | 0 | 0 | 0 | 0 | n/a |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-08 | 3 | 2 | 0 | 1 | 1.0 |

Claims: 16 over 8 judged pairs: 6 hedged, 2 certain, 8 absent.

Median survival: 1.0 over 4 scored pairs.

Claims that became certain:

- code-review-01: The expected shape of `roles` is unclear — possibly a list of str.
- code-review-01: The interface expected of `db` is unclear — possibly something providing `.insert`.

### classic-concise

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 0 | 2 | n/a |
| code-review-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 2 | 2 | 0 | 0 | 1.0 |
| debugging-08 | 9 | 2 | 1 | 6 | 0.667 |
| explanation-03 | 0 | 0 | 0 | 0 | n/a |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 16 over 8 judged pairs: 7 hedged, 1 certain, 8 absent.

Median survival: 1.0 over 3 scored pairs.

Claims that became certain:

- debugging-08: A rising memory floor points to something unbounded, or to a bound that isn't actually being enforced.

### developer-docs

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 2 | 0 | 0.0 |
| code-review-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 2 | 2 | 0 | 0 | 1.0 |
| debugging-08 | 9 | 0 | 0 | 9 | n/a |
| explanation-03 | 0 | 0 | 0 | 0 | n/a |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 16 over 8 judged pairs: 5 hedged, 2 certain, 9 absent.

Median survival: 1.0 over 3 scored pairs.

Claims that became certain:

- code-review-01: The expected shape of `roles` is unclear — possibly a list of str.
- code-review-01: The interface expected of `db` is unclear — possibly something providing `.insert`.

### plain-language

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 0 | 2 | n/a |
| code-review-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 2 | 2 | 0 | 0 | 1.0 |
| debugging-08 | 9 | 2 | 1 | 6 | 0.667 |
| explanation-03 | 0 | 0 | 0 | 0 | n/a |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |
| summarization-08 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 16 over 8 judged pairs: 7 hedged, 1 certain, 8 absent.

Median survival: 1.0 over 3 scored pairs.

Claims that became certain:

- debugging-08: The five listed items are plausible causes of the memory growth.

### technical-simplified

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-01 | 2 | 0 | 0 | 2 | n/a |
| code-review-03 | 0 | 0 | 0 | 0 | n/a |
| debugging-04 | 2 | 1 | 1 | 0 | 0.5 |
| debugging-08 | 9 | 0 | 0 | 9 | n/a |
| explanation-04 | 0 | 0 | 0 | 0 | n/a |
| summarization-05 | 0 | 0 | 0 | 0 | n/a |

Claims: 13 over 6 judged pairs: 1 hedged, 1 certain, 11 absent.

Median survival: 0.5 over 1 scored pairs.

Claims that became certain:

- debugging-04: The non-ASCII byte 0xc3 is likely part of a UTF-8 multi-byte sequence, e.g. an accented character.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 34, measured: 34.
Mean duration: 17861 ms. Mean wall: 31428 ms. Mean startup: 13567 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 34, measured: 34.
Input tokens: 68 uncached, 71657 cache write, 69802 cache read. Output tokens: 44854.
Cache-read share: 0.493.
Cache writes by lifetime: 71657 at 5 minutes, 0 at 1 hour.

## Reuse

Reused rows: 143, imported from 2026-08-10d-screening.
Live calls of this run: 34.

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

- technical-simplified/explanation-03: the pair failed the gate, excluded
- technical-simplified/summarization-08: the pair failed the gate, excluded
