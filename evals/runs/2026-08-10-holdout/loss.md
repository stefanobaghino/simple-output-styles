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

Judge: opus. Judged on 2026-08-10T14:32:55+00:00.

## Completeness (fact survival)

The judge lists the facts of the unstyled answer, then checks each fact against the styled answer. The fraction is the share of the facts that survive. The judge also lists the facts of the styled answer and checks each fact against the unstyled answer: a styled fact that the unstyled answer does not state is an addition. The lost facts and the added facts appear verbatim below the table.

### actionable-clarity

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-h01 | 27 | 0 | 0.0 | 0 | 0 |
| code-review-h02 | 23 | 20 | 0.87 | 27 | 2 |
| code-review-h03 | 25 | 18 | 0.72 | 27 | 5 |
| code-review-h04 | 2 | 0 | 0.0 | 25 | 25 |
| code-review-h05 | 44 | 29 | 0.659 | 43 | 17 |
| debugging-h01 | 10 | 9 | 0.9 | 12 | 3 |
| debugging-h02 | 11 | 9 | 0.818 | 16 | 4 |
| debugging-h03 | 13 | 13 | 1.0 | 13 | 3 |
| debugging-h04 | 11 | 8 | 0.727 | 11 | 1 |
| debugging-h05 | 1 | 0 | 0.0 | 4 | 3 |
| debugging-h06 | 19 | 13 | 0.684 | 45 | 26 |
| explanation-h01 | 31 | 25 | 0.806 | 37 | 10 |
| explanation-h02 | 24 | 17 | 0.708 | 22 | 2 |
| explanation-h03 | 28 | 27 | 0.964 | 28 | 3 |
| explanation-h04 | 25 | 16 | 0.64 | 23 | 7 |
| explanation-h05 | 11 | 6 | 0.545 | 32 | 12 |
| explanation-h06 | 18 | 11 | 0.611 | 28 | 8 |
| summarization-h01 | 16 | 15 | 0.938 | 17 | 0 |
| summarization-h02 | 18 | 12 | 0.667 | 18 | 3 |
| summarization-h03 | 15 | 15 | 1.0 | 15 | 1 |
| summarization-h04 | 7 | 0 | 0.0 | 29 | 29 |
| summarization-h05 | 16 | 16 | 1.0 | 16 | 1 |
| summarization-h06 | 14 | 14 | 1.0 | 15 | 0 |

Median fraction: 0.72 over 23 scored pairs.

Median additions: 3 over 23 scored pairs.

Lost facts:

- code-review-h01: The expression `share * (people - 1)` uses the rounded per-person share instead of `total`.
- code-review-h01: Using the rounded share in that expression can compound floating-point error for larger `people` counts.
- code-review-h01: The last person's amount may drift by more than a cent instead of the intended ±0.01 correction.
- code-review-h01: With `total=100` and `people=7`, the last share comes out odd.
- code-review-h01: The corrected `amounts[-1]` is not re-rounded.
- code-review-h01: Because `amounts[-1]` is not re-rounded, it can end up with more than 2 decimal places due to float imprecision.
- code-review-h01: An example of that imprecision is a value of `33.33999999999999` instead of `33.34`.
- code-review-h01: `sum(amounts) != total` is a direct float equality check.
- code-review-h01: Floats are unreliable for direct equality comparisons.
- code-review-h01: The float equality check mostly works here because it only decides whether to apply a correction.
- code-review-h01: The float equality check is still fragile.
- code-review-h01: Passing `people == 0` raises an uncaught `ZeroDivisionError`.
- code-review-h01: Passing `people` as a float such as `2.5` makes `[share] * people` raise a `TypeError`.
- code-review-h01: A list cannot be multiplied by a non-integer.
- code-review-h01: Negative or zero `total` is not rejected.
- code-review-h01: Negative `people` is not rejected.
- code-review-h01: Unrejected invalid inputs silently produce nonsense output.
- code-review-h01: Using `float` for currency is the root problem in this code.
- code-review-h01: Using `float` for currency carries a risk of float representation error.
- code-review-h01: Currency should be handled with `Decimal` (using `ROUND_HALF_UP` or similar) or with integer cents.
- code-review-h01: Python's `round()` uses banker's rounding, also called round-half-to-even.
- code-review-h01: Banker's rounding can surprise people who expect standard round-half-up behavior for money.
- code-review-h01: Only the last person absorbs the rounding remainder.
- code-review-h01: If the discrepancy exceeds one cent, the last person's share becomes visibly unfair rather than off by just a cent.
- code-review-h01: The code has no type hints and no docstring.
- code-review-h01: Without type hints or a docstring, the types and units of `total` and `people` are unclear to callers.
- code-review-h01: The code should raise a `ValueError` for `people <= 0`.
- code-review-h02: Decrementing `i` after a splice fixes the skipping bug.
- code-review-h02: The term "expired" often implies a `<=` comparison.
- code-review-h02: `var` is loose scoping style that makes bugs easy to introduce as a function grows.
- code-review-h03: Without closing, the file descriptor stays open indefinitely.
- code-review-h03: The unclosed file is opened inside a generator expression, whose lifetime and closure are not obvious.
- code-review-h03: `int()` tolerates surrounding whitespace.
- code-review-h03: The function signature does not document that it requires a reusable sequence such as a list or tuple rather than a one-shot iterator.
- code-review-h03: The code lacks input validation against negative counts, non-numeric types, and `None` values.
- code-review-h03: The proposed minimal fix guards against empty input by raising `ValueError("numbers must not be empty")`.
- code-review-h03: The proposed minimal fix uses a `with` block so the file is properly closed.
- code-review-h04: The speaker will check for relevant memory before reviewing.
- code-review-h04: A skill named auto-memory-check is being invoked.
- code-review-h05: The append-before-check behavior turns a burst or DoS attempt into a self-inflicted CPU and memory DoS on the limiter.
- code-review-h05: The unbounded burst growth is almost certainly not deliberate.
- code-review-h05: Truncating to whole seconds makes the 60-second window fuzzy, ranging from about 59 to about 61 seconds.
- code-review-h05: `time.time()` can jump due to NTP correction or manual clock changes.
- code-review-h05: A backward clock jump makes `now - 60` smaller, which can make already-expired entries look valid again and stretch the effective window.
- code-review-h05: `time.monotonic()` would avoid the clock-jump problem.
- code-review-h05: Using `time.monotonic()` would require consistent use across all callers because monotonic time is not epoch-based.
- code-review-h05: A `collections.deque` with `popleft()` while entries are stale would be both correct and cheaper.
- code-review-h05: A deque would compose better with a fix that stops appending once over a hard cap.
- code-review-h05: The append-then-check ordering gives correct semantics: it allows exactly `limit` requests per window and blocks the (limit+1)th.
- code-review-h05: The append-then-check ordering is not an off-by-one error and looks intentional.
- code-review-h05: The magic numbers with no rationale is a problem the user previously flagged.
- code-review-h05: The concurrency race and the unbounded burst growth are the two issues to fix before production traffic.
- code-review-h05: The concurrency race and unbounded burst growth are real correctness and availability issues, not style nits.
- code-review-h05: The multi-process issue is the one most likely to bite silently in deployment even though the code looks correct in isolation.
- debugging-h01: An alternative fix is a factory function that takes `name` and returns a lambda.
- debugging-h02: If filenames always follow the exact snap-<N>.db pattern, the key can be simplified to int(s.split('-')[1].split('.')[0]).
- debugging-h02: int(s.split('-')[1].split('.')[0]) avoids using a regular expression.
- debugging-h04: When input strings sometimes include an offset and sometimes do not, validating or normalizing at the boundary is preferable to guessing the zone.
- debugging-h04: Boundary handling options include rejecting naive timestamps or requiring input to always include an offset.
- debugging-h04: `2026-08-01T10:00:00+00:00` is an example of an ISO timestamp that includes an offset.
- debugging-h05: The problem under discussion is a classic idempotency/duplicate-delivery problem.
- debugging-h06: A rollback deploys new code but does not necessarily recycle running processes or pods.
- debugging-h06: A connection, thread, or memory leak on running instances clears only when instances restart or connections time out.
- debugging-h06: A roughly one-hour capacity stabilization time matches typical ASG cooldown and stabilization windows.
- debugging-h06: Cache poisoning or a cold cache self-heals as TTLs expire or entries get overwritten.
- debugging-h06: Aggressive retries and open circuit breakers can take time to settle even after the triggering code is removed.
- debugging-h06: Region-specific configuration differences can cause only one region to exercise a bad code path.
- explanation-h01: Idempotency is treated as a prerequisite for automatic retry logic in HTTP clients, load balancers, and API gateways.
- explanation-h01: Idempotent is not the same as safe.
- explanation-h01: Safe means the method has no side effects at all.
- explanation-h01: Idempotency keys usually expire after some window, such as 24 hours, so storage does not grow forever.
- explanation-h01: Servers typically need to handle a duplicate request arriving while the first request is still processing, by returning a conflict/try-later response or blocking until done.
- explanation-h01: The idempotency key pattern is common in payment APIs such as Stripe and PayPal because double-charging is the worst-case failure mode.
- explanation-h02: B-trees typically have high fan-out, so the tree is shallow.
- explanation-h02: Because index keys are sorted, a B-tree index supports range scans and ordered retrieval without a separate sort step.
- explanation-h02: B-tree indexes help range queries such as filtering order_date BETWEEN two dates.
- explanation-h02: B-tree indexes help queries that sort by the indexed column.
- explanation-h02: Each index causes extra disk I/O and WAL/log writes beyond the table's own row change.
- explanation-h02: An insert gets no query-side benefit from indexes because an insert is not a lookup.
- explanation-h02: You should index columns that are frequently filtered, sorted, or joined on.
- explanation-h03: Offset pagination is stateless and easy to reason about.
- explanation-h04: If the connection is encrypted, establishing it requires TLS negotiation, which adds several more round-trips and cryptographic operations.
- explanation-h04: Establishing a database connection requires session setup, in which the database allocates memory, spawns a backend process or thread, and initializes session state.
- explanation-h04: Postgres forks a process per connection.
- explanation-h04: A request that could be served in 5ms might take 50-100ms because of connection setup for a single query.
- explanation-h04: Postgres defaults to a limit of 100 concurrent connections.
- explanation-h04: Each open database connection consumes real memory and CPU on the server even when idle.
- explanation-h04: When all pooled connections are busy, new requests wait for one to free up rather than opening additional connections.
- explanation-h04: Making requests wait instead of opening extra connections protects the database from being overwhelmed.
- explanation-h04: Requests queuing or timing out under load is the signal that it is time to look at pool size.
- explanation-h05: Adding a queue introduces new complexity: retries, dead-letter handling, and idempotency.
- explanation-h05: Queues typically deliver messages at-least-once.
- explanation-h05: At-least-once delivery is why idempotency is needed.
- explanation-h05: Without traffic or downtime numbers, it is hard to determine whether a queue is worth it.
- explanation-h05: Running a queue carries operational overhead that retry-with-backoff avoids.
- explanation-h06: Splitting is likely to make deploys slower and riskier in the short term unless the actual bottleneck is something microservices specifically fix.
- explanation-h06: Microservices can help when the problem is a slow test suite, unclear ownership causing merge conflicts, or a monolith where any change requires a full redeploy of unrelated code.
- explanation-h06: Microservices help in those cases by letting teams deploy independently.
- explanation-h06: Staying monolithic means deploys stay coupled and the blast radius stays large.
- explanation-h06: Premature service boundaries are expensive to redraw later.
- explanation-h06: A few days of pipeline and incident data will reveal which failure mode the team actually has.
- explanation-h06: For a six-person team, the failure mode is very likely process or tooling rather than something a service split fixes.
- summarization-h01: All other v2 endpoint calls must be migrated to their /v3/ equivalents before November 30.
- summarization-h02: As of Wednesday, 1 of the 3 reports had arrived.
- summarization-h02: Sender reputation was ruled out as a cause.
- summarization-h02: Once the provider responds, their trace should be correlated against internal delivery logs for the 2 missing report IDs.
- summarization-h02: No action is needed from the customer right now.
- summarization-h02: The customer should be followed up with once RLY-4812 resolves.
- summarization-h02: The customer should be contacted proactively if the provider has not responded within the 2-business-day window.
- summarization-h04: A tool named "bash" is being invoked.
- summarization-h04: The tool invocation includes a "command" parameter.
- summarization-h04: The command runs `cat` on the file /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-9pi3l86u/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-dgijk4db/memory/MEMORY.md
- summarization-h04: The command redirects standard error to /dev/null with `2>/dev/null`.
- summarization-h04: The command echoes "NONE" if the `cat` command fails.
- summarization-h04: The tool invocation includes a "description" parameter with the value "Check memory index".
- summarization-h04: The parameters are given in JSON format.

Added facts (styled only):

- code-review-h02: `let` is the current convention.
- code-review-h02: `let` avoids leaking i into the enclosing scope.
- code-review-h03: All of the function's bugs stem from one root cause: it consumes a generator multiple times.
- code-review-h03: The `ValueError` message from `int(line)` won't say which line failed.
- code-review-h03: Lines should be stripped and the failing line number caught and reported.
- code-review-h03: The hardcoded filename makes `stats` harder to test or reuse with different inputs.
- code-review-h03: The hardcoded filename is not a bug.
- code-review-h04: The function has six problems.
- code-review-h04: The most serious problems are a credential leak and a broken auth check.
- code-review-h04: The call `logging.info("login attempt: %s", request)` logs the entire `request` dict.
- code-review-h04: The `request` dict contains the plaintext password.
- code-review-h04: Anyone with log access can obtain user credentials from these logs.
- code-review-h04: Logging only the username, as in `logging.info("login attempt for user: %s", request.get("username"))`, fixes the credential leak.
- code-review-h04: The comparison `user["password"] == request["password"]` assumes `users` stores raw passwords.
- code-review-h04: Passwords must be hashed, for example with `bcrypt` or `argon2`.
- code-review-h04: Password comparison must run against the hash rather than plaintext.
- code-review-h04: The `==` operator on strings short-circuits on the first mismatched character.
- code-review-h04: String short-circuiting leaks timing information that an attacker can use to guess the password.
- code-review-h04: A constant-time comparison such as `hmac.compare_digest` should be used.
- code-review-h04: Most password-hashing libraries' verify functions already handle constant-time comparison.
- code-review-h04: `assert` is the wrong tool for input validation.
- code-review-h04: Python strips `assert` statements when run with the `-O` optimization flag.
- code-review-h04: If the `assert` check vanishes, `request["username"]` can raise an unhandled `KeyError`.
- code-review-h04: Validation should be explicit and return a proper error response, such as returning `{"ok": False, "error": "bad username or password"}` when `username` or `password` is missing from `request`.
- code-review-h04: The function performs no type or emptiness checks on `request`.
- code-review-h04: If `request` isn't a dict, or `username`/`password` are `None` or empty strings, the function may raise or behave unexpectedly instead of failing cleanly.
- code-review-h04: The function has no rate limiting or lockout.
- code-review-h04: The function has no defense against brute-force login attempts.
- code-review-h04: Rate limiting is not something to fix inside `login` itself; the caller or framework should enforce rate limiting or account lockout after repeated failures.
- code-review-h04: The generic error message `"bad username or password"` is good practice because it avoids revealing which field was wrong.
- code-review-h04: The most urgent fix is to stop logging the password.
- code-review-h04: Plaintext password storage and an `assert`-based check that can disappear under `-O` are both production-breaking risks.
- code-review-h05: No memory files exist yet for this project.
- code-review-h05: The memory leak is the most serious problem in the code.
- code-review-h05: The filter `t > now - 60` excludes a hit made exactly 60 seconds ago.
- code-review-h05: Using `<=` after appending allows `limit + 1` total requests.
- code-review-h05: With `limit=20`, the code actually permits 21 hits per window.
- code-review-h05: To allow at most 20, the check should be `< limit`, or `<= limit` checked before the append.
- code-review-h05: Truncating timestamps to whole seconds can let a burst at a second boundary slip through with a slightly wider effective window.
- code-review-h05: There is no input validation on `key` or `limit`.
- code-review-h05: Nothing prevents a caller from passing `limit=0` or a negative limit.
- code-review-h05: With `limit=0`, the first hit passes due to the off-by-one and everything after is blocked.
- code-review-h05: The O(n) per-call cost is acceptable at `limit=20` but does not scale if the limit is raised significantly.
- code-review-h05: The 60-second fixed window is likely deliberate because it is a round number and sliding-window-by-list is a known simple pattern.
- code-review-h05: The `limit=20` default was probably picked empirically and needs documentation.
- code-review-h05: The off-by-one allowing `limit+1` is inconsistent with the `limit` parameter name and looks like a check-order mistake.
- code-review-h05: There are no tests for the rate limiter.
- code-review-h05: Fixing the code in place would involve adding a lock, fixing the off-by-one, and adding eviction.
- code-review-h05: An alternative to fixing in place is replacing it with a battle-tested rate-limiting library or a Redis-backed sliding-window implementation for multi-instance correctness.
- debugging-h01: functools.partial binds the argument at creation time.
- debugging-h01: functools.partial reads more clearly for non-lambda cases.
- debugging-h01: functools.partial is imported from the functools module.
- debugging-h02: Sorting by file modification time via `os.path.getmtime` is an alternative approach.
- debugging-h02: Parsing an embedded timestamp in the filename is an alternative approach.
- debugging-h02: Sorting by modification time or an embedded timestamp avoids relying on the number in the filename.
- debugging-h02: The alternative approaches apply when filenames always use a fixed-width or consistent format.
- debugging-h03: The cart total is correct for practical purposes despite the failed comparison.
- debugging-h03: big.js is a decimal library.
- debugging-h03: Using integer cents or a decimal library prevents rounding errors from accumulating across many transactions.
- debugging-h04: Every datetime being compared must be aware rather than naive.
- debugging-h05: The working directory is being checked for webhook sender/receiver code.
- debugging-h05: Checking the code could ground the analysis rather than leaving it as pure speculation.
- debugging-h05: An `ls` command is run on the path /private/var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-pairs-dgijk4db.
- debugging-h06: A targeted read of stored memory was run to check for related project context.
- debugging-h06: Three explanations fit the evidence best.
- debugging-h06: Cache or connection pool invalidation in one region is the most plausible cause.
- debugging-h06: If the deploy restarted service instances or rotated a cache layer, that region's cache may have gone cold.
- debugging-h06: With a cold cache, downstream lookups to the search index and database would run at full cost until the cache repopulated.
- debugging-h06: Cache warm-up would take longer than the rollback.
- debugging-h06: Uneven traffic or shard rebalancing after restart is the second most plausible cause.
- debugging-h06: A rolling restart of search index nodes could cause one region's cluster to absorb shard reassignment or leader election.
- debugging-h06: Query latency would stay elevated until rebalancing finished, independent of whether the new code was still running.
- debugging-h06: A regional dependency such as an index shard, database replica, or DNS/routing layer getting into a bad state is the third most plausible cause.
- debugging-h06: The dependency explanation fits if the deploy changed connection behavior, such as connection pool size or retry logic, enough to overload one region's dependency.
- debugging-h06: Jaeger and Honeycomb are examples of tracing backends.
- debugging-h06: If Tuesday's data still exists anywhere, it is the best source of ground truth.
- debugging-h06: The incident occurred on Tuesday.
- debugging-h06: Cache hit-rate metrics for the affected region may be stored separately from the main dashboard.
- debugging-h06: A cache hit-rate dip that recovers over roughly an hour would confirm the cache-invalidation theory.
- debugging-h06: The search index's cluster events log records shard moves, leader elections, and node restarts.
- debugging-h06: Most search infrastructure, such as Elasticsearch or OpenSearch, keeps cluster event data separately from latency dashboards.
- debugging-h06: Cluster event data often retains longer than 24 hours.
- debugging-h06: A deploy could restart instances in only one region due to an uneven rollout strategy or an autoscaling difference between regions.
- debugging-h06: The deploy should be re-run in a single low-traffic region first, with cache hit-rate and shard-event monitoring in place beforehand.
- debugging-h06: If the same region shows a hit-rate dip or shard churn, the mechanism is confirmed.
- debugging-h06: A cache warm-up or gradual traffic ramp step can be added to the deploy process before rolling out further.
- debugging-h06: Success means pointing to a specific metric that both dipped at the deploy and recovered around the one-hour mark, in the affected region only.
- debugging-h06: Candidate confirming metrics include cache hit rate, shard events, and connection pool saturation.
- debugging-h06: Identifying such a metric gives a concrete before/after for the controlled retry.
- explanation-h01: When a client doesn't know if a request succeeded, its only safe move is to resend the request.
- explanation-h01: The HTTP specification RFC 7231 classifies which standard methods are idempotent.
- explanation-h01: OPTIONS only queries supported methods and doesn't change state.
- explanation-h01: PATCH is not idempotent by definition.
- explanation-h01: A specific PATCH operation can be idempotent if it sets an absolute value, such as 'set status to shipped', rather than applying a relative change.
- explanation-h01: Services use two main techniques to make POST safe to retry: idempotency keys and client-supplied resource IDs with PUT.
- explanation-h01: With client-supplied resource IDs, the client uses `PUT /orders/{client-generated-id}` with the order data instead of `POST /orders`.
- explanation-h01: With `POST /orders`, the server assigns the resource ID.
- explanation-h01: Retries of a PUT with the same client-supplied ID and body re-apply the same state, which is naturally idempotent.
- explanation-h01: Both techniques shift duplicate detection from 'did the network round-trip succeed' to 'have I already seen this exact operation', which is what makes the retry safe.
- explanation-h02: Some databases support function-based or expression indexes built on an expression such as UPPER(customer_name).
- explanation-h02: A function-based or expression index on UPPER(customer_name) handles the case that a plain index on customer_name does not.
- explanation-h03: Orders data keeps changing, since new orders arrive and older ones may be canceled or reordered by status.
- explanation-h03: Offset pagination needs a stable `ORDER BY` on a unique column, otherwise row order can vary between requests.
- explanation-h03: A cursor is usually an opaque token encoding the last row's sort key.
- explanation-h04: Each step of opening a database connection often takes tens of milliseconds.
- explanation-h04: An app handling 100 requests per second at a 20ms connection cost each spends 2 seconds of connection setup per second of traffic, on top of the actual query work.
- explanation-h04: Exhausting the connection limit causes new requests to fail even when the database itself is not overloaded.
- explanation-h04: A pool opens a fixed number of connections once, at startup.
- explanation-h04: Pooling turns a 20ms setup cost into a near-instant handoff.
- explanation-h04: Node's `pg-pool`, Python's `SQLAlchemy`, and Go's `database/sql` are examples of tools that provide a default connection pool.
- explanation-h04: The key thing to check is that the code uses the shared pool rather than manually opening a new connection in each request handler.
- explanation-h05: The qualitative case for a queue holds regardless of traffic volume.
- explanation-h05: A queue enables retries without extra work in the order service.
- explanation-h05: Today, retry logic likely lives in the order service's HTTP client code, tangled with order logic.
- explanation-h05: A queue absorbs traffic spikes.
- explanation-h05: If email sending is slower than order creation at peak times, a queue buffers the backlog instead of causing timeouts or dropped requests.
- explanation-h05: A queue does not make the email service itself more reliable.
- explanation-h05: If the email service has a bug that fails on certain payloads, a queue delays the failure and may retry it repeatedly.
- explanation-h05: A queue does not guarantee delivery on its own.
- explanation-h05: Guaranteed delivery depends on message persistence, acknowledgment semantics, and dead-letter handling being configured correctly.
- explanation-h05: If queue configuration is incorrect, messages can still be lost silently.
- explanation-h05: At low enough volume, HTTP with retries may be sufficient.
- explanation-h05: The queue is a reasonable architectural improvement independent of the numbers.
- explanation-h06: A typical deploy's time can be broken down into build time, test suite time, CI queue time, manual approval steps, and rollout/rollback time.
- explanation-h06: If most deploy time is spent in a slow test suite or a manual gate, splitting services will not shrink that time.
- explanation-h06: Deploy risk can come from unrelated teams' changes colliding in one deploy, from a lack of automated tests, from no staged rollout, or from unclear ownership of what broke.
- explanation-h06: Lack of automated tests, absence of staged rollout, and unclear ownership are process gaps that a split will not close.
- explanation-h06: If everyone on the team touches every part of the codebase, splitting into services will not create independent deploys.
- explanation-h06: If the root cause is not fixed, the team may blame the architecture instead of the actual bottleneck, causing the same debate to resurface later.
- explanation-h06: If the real problem is a slow test suite or manual gates, those problems will keep compounding as the codebase grows even without a split.
- explanation-h06: If the bottleneck is genuine team coupling, where unrelated changes routinely block or break each other, a split on the specific boundary causing the pain is worth considering rather than splitting the whole system.
- summarization-h02: The customer checked their spam folder and found nothing.
- summarization-h02: The follow-up includes checking whether the two-business-day window has passed and escalating if unanswered.
- summarization-h02: Once the trace returns, the delivery path for the working report should be compared against the two failing ones to find where they diverge.
- summarization-h03: Adding more writers makes the database bottleneck worse.
- summarization-h04: The invoice numbering system is being reworked.
- summarization-h04: The QA test plan orders tests highest risk first.
- summarization-h04: The public API `invoice_number` field is now nullable for draft invoices.
- summarization-h04: The nullable `invoice_number` field is a breaking behavior change for existing API consumers.
- summarization-h04: The shape of the `invoice_number` field is unchanged.
- summarization-h04: GET requests for draft invoices return `invoice_number: null`.
- summarization-h04: Some API consumers and internal integrations assume `invoice_number` is always a string.
- summarization-h04: A migration backfills entity prefixes onto existing invoices.
- summarization-h04: The migration runs once against production data.
- summarization-h04: The migration is hard to reverse if done wrong.
- summarization-h04: Each invoice's prefix is determined by its legal entity.
- summarization-h04: The numbering sequence changed from global to per-entity.
- summarization-h04: Number collisions and gaps are the main risk of the per-entity sequence change.
- summarization-h04: Each entity's number sequence increments independently.
- summarization-h04: Concurrent finalization within the same entity carries a race condition risk of duplicate numbers.
- summarization-h04: Each entity's sequence continues from a migrated starting point.
- summarization-h04: Number allocation timing moved from invoice creation to invoice finalization.
- summarization-h04: Number allocation behavior differs for new drafts versus existing drafts.
- summarization-h04: Drafts created after this release have no number until they are finalized.
- summarization-h04: Finalizing a new draft allocates its number at that point.
- summarization-h04: Drafts created before this release keep their already-allocated number and are not re-numbered on finalization.
- summarization-h04: Drafts can be deleted or voided.
- summarization-h04: PDF template rendering is a lower risk area but is user-visible.
- summarization-h04: PDFs display the new prefixed number for finalized invoices.
- summarization-h04: PDFs can be rendered for draft invoices that have no number yet.
- summarization-h04: The search index is being rebuilt as part of this change.
- summarization-h04: The search index rebuild is the lowest risk area but affects findability.
- summarization-h04: Invoices can be searched by their prefixed number.
- summarization-h04: Support for searching by the old pre-migration number format is uncertain.
- summarization-h05: Marketing expects a large customer campaign next quarter.

### clarity-flow

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-h01 | 27 | 13 | 0.481 | 28 | 13 |
| code-review-h02 | 23 | 19 | 0.826 | 20 | 2 |
| code-review-h03 | 25 | 21 | 0.84 | 15 | 2 |
| code-review-h04 | 2 | 0 | 0.0 | 22 | 22 |
| code-review-h05 | 44 | 30 | 0.682 | 40 | 15 |
| code-review-h06 | 38 | 34 | 0.895 | 36 | 4 |
| debugging-h01 | 10 | 8 | 0.8 | 12 | 3 |
| debugging-h02 | 11 | 9 | 0.818 | 9 | 1 |
| debugging-h03 | 13 | 10 | 0.769 | 10 | 1 |
| debugging-h04 | 11 | 9 | 0.818 | 9 | 1 |
| debugging-h05 | 1 | 1 | 1.0 | 22 | 22 |
| debugging-h06 | 19 | 14 | 0.737 | 27 | 19 |
| explanation-h01 | 31 | 24 | 0.774 | 38 | 5 |
| explanation-h02 | 24 | 16 | 0.667 | 16 | 2 |
| explanation-h03 | 28 | 22 | 0.786 | 26 | 2 |
| explanation-h04 | 25 | 15 | 0.6 | 19 | 1 |
| explanation-h05 | 11 | 6 | 0.545 | 20 | 10 |
| explanation-h06 | 18 | 10 | 0.556 | 23 | 10 |
| summarization-h01 | 16 | 15 | 0.938 | 16 | 0 |
| summarization-h02 | 18 | 14 | 0.778 | 17 | 1 |
| summarization-h03 | 15 | 14 | 0.933 | 17 | 0 |
| summarization-h04 | 7 | 0 | 0.0 | 18 | 18 |
| summarization-h05 | 16 | 15 | 0.938 | 17 | 0 |
| summarization-h06 | 14 | 14 | 1.0 | 14 | 0 |

Median fraction: 0.782 over 24 scored pairs.

Median additions: 2.0 over 24 scored pairs.

Lost facts:

- code-review-h01: The expression `share * (people - 1)` uses the rounded per-person share instead of `total`.
- code-review-h01: Using the rounded share in that expression can compound floating-point error for larger `people` counts.
- code-review-h01: With `total=100` and `people=7`, the last share comes out odd.
- code-review-h01: The corrected `amounts[-1]` is not re-rounded.
- code-review-h01: Because `amounts[-1]` is not re-rounded, it can end up with more than 2 decimal places due to float imprecision.
- code-review-h01: An example of that imprecision is a value of `33.33999999999999` instead of `33.34`.
- code-review-h01: The float equality check mostly works here because it only decides whether to apply a correction.
- code-review-h01: Passing `people` as a float such as `2.5` makes `[share] * people` raise a `TypeError`.
- code-review-h01: A list cannot be multiplied by a non-integer.
- code-review-h01: Using `float` for currency is the root problem in this code.
- code-review-h01: Python's `round()` uses banker's rounding, also called round-half-to-even.
- code-review-h01: Banker's rounding can surprise people who expect standard round-half-up behavior for money.
- code-review-h01: The code has no type hints and no docstring.
- code-review-h01: Without type hints or a docstring, the types and units of `total` and `people` are unclear to callers.
- code-review-h02: Decrementing `i` after a splice fixes the skipping bug.
- code-review-h02: The function uses `var` instead of `let`.
- code-review-h02: Using `var` is not a functional bug in this function because no closure captures `i`.
- code-review-h02: `var` is loose scoping style that makes bugs easy to introduce as a function grows.
- code-review-h03: Without closing, the file descriptor stays open indefinitely.
- code-review-h03: The unclosed file is opened inside a generator expression, whose lifetime and closure are not obvious.
- code-review-h03: The function signature does not document that it requires a reusable sequence such as a list or tuple rather than a one-shot iterator.
- code-review-h03: The code lacks input validation against negative counts, non-numeric types, and `None` values.
- code-review-h04: The speaker will check for relevant memory before reviewing.
- code-review-h04: A skill named auto-memory-check is being invoked.
- code-review-h05: Every call appends to the bucket before checking the limit, including calls that are denied.
- code-review-h05: A client sending high-QPS requests keeps adding entries to `_hits[key]` for the full 60-second window.
- code-review-h05: The size of the hits list is bounded by request volume, not by `limit`.
- code-review-h05: The append-before-check behavior turns a burst or DoS attempt into a self-inflicted CPU and memory DoS on the limiter.
- code-review-h05: The unbounded burst growth is almost certainly not deliberate.
- code-review-h05: Truncating to whole seconds makes the 60-second window fuzzy, ranging from about 59 to about 61 seconds.
- code-review-h05: Using `time.monotonic()` would require consistent use across all callers because monotonic time is not epoch-based.
- code-review-h05: A `collections.deque` with `popleft()` while entries are stale would be both correct and cheaper.
- code-review-h05: A deque would compose better with a fix that stops appending once over a hard cap.
- code-review-h05: The append-then-check ordering gives correct semantics: it allows exactly `limit` requests per window and blocks the (limit+1)th.
- code-review-h05: The append-then-check ordering is not an off-by-one error and looks intentional.
- code-review-h05: The concurrency race and the unbounded burst growth are the two issues to fix before production traffic.
- code-review-h05: The concurrency race and unbounded burst growth are real correctness and availability issues, not style nits.
- code-review-h05: The multi-process issue is the one most likely to bite silently in deployment even though the code looks correct in isolation.
- code-review-h06: The override loop applies even when the existing value is a dict or a list.
- code-review-h06: If a config file contains a nested value like {"database": {...}}, setting DATABASE in the environment replaces the whole nested structure with a single string.
- code-review-h06: The precedence order is likely deliberate and fine to keep, but needs documenting.
- code-review-h06: Whether the relative path is deliberate or accidental cannot be determined without seeing the calling services.
- debugging-h01: An alternative fix is a factory function that takes `name` and returns a lambda.
- debugging-h01: Both fixes work because they create a new variable scoped to each iteration or call.
- debugging-h02: If filenames always follow the exact snap-<N>.db pattern, the key can be simplified to int(s.split('-')[1].split('.')[0]).
- debugging-h02: int(s.split('-')[1].split('.')[0]) avoids using a regular expression.
- debugging-h03: Floating-point numbers in JavaScript use IEEE 754 double precision.
- debugging-h03: IEEE 754 double precision cannot represent most decimal fractions exactly.
- debugging-h03: decimal.js is a decimal library.
- debugging-h04: When input strings sometimes include an offset and sometimes do not, validating or normalizing at the boundary is preferable to guessing the zone.
- debugging-h04: Boundary handling options include rejecting naive timestamps or requiring input to always include an offset.
- debugging-h06: A rollback deploys new code but does not necessarily recycle running processes or pods.
- debugging-h06: A connection, thread, or memory leak on running instances clears only when instances restart or connections time out.
- debugging-h06: A deploy can trigger a scale-down or instance churn in a region.
- debugging-h06: A roughly one-hour capacity stabilization time matches typical ASG cooldown and stabilization windows.
- debugging-h06: Regional infrastructure problems such as noisy neighbors, network path issues, or partial outages can correlate with a deploy by timing alone.
- explanation-h01: Idempotency is treated as a prerequisite for automatic retry logic in HTTP clients, load balancers, and API gateways.
- explanation-h01: Per the HTTP spec, HEAD is idempotent and is the same as GET but without a body.
- explanation-h01: Idempotent is not the same as safe.
- explanation-h01: Safe means the method has no side effects at all.
- explanation-h01: Idempotency keys usually expire after some window, such as 24 hours, so storage does not grow forever.
- explanation-h01: Servers typically need to handle a duplicate request arriving while the first request is still processing, by returning a conflict/try-later response or blocking until done.
- explanation-h01: The idempotency key pattern is common in payment APIs such as Stripe and PayPal because double-charging is the worst-case failure mode.
- explanation-h02: Because index keys are sorted, a B-tree index supports range scans and ordered retrieval without a separate sort step.
- explanation-h02: B-tree indexes help queries that sort by the indexed column.
- explanation-h02: Node splits can cascade up the tree and require rebalancing.
- explanation-h02: Deletes can trigger node merges and rebalancing.
- explanation-h02: Each index causes extra disk I/O and WAL/log writes beyond the table's own row change.
- explanation-h02: An insert gets no query-side benefit from indexes because an insert is not a lookup.
- explanation-h02: You should index columns that are frequently filtered, sorted, or joined on.
- explanation-h02: You should avoid over-indexing tables with heavy write traffic.
- explanation-h03: Offset pagination is stateless and easy to reason about.
- explanation-h03: If rows are inserted or deleted while paginating with offsets, rows can be skipped or duplicated across pages.
- explanation-h03: The cursor pointer is usually an indexed, unique, monotonic column such as id or created_at plus id.
- explanation-h03: Cursor pagination is stable under concurrent inserts and deletes, producing no skipped or duplicated rows.
- explanation-h03: Cursor pagination requires slightly more implementation work than offset pagination.
- explanation-h03: Offset pagination should be chosen only when arbitrary page jumping is specifically needed and its staleness and performance issues are acceptable.
- explanation-h04: Postgres forks a process per connection.
- explanation-h04: Each step of establishing a database connection takes milliseconds.
- explanation-h04: A request that could be served in 5ms might take 50-100ms because of connection setup for a single query.
- explanation-h04: Postgres defaults to a limit of 100 concurrent connections.
- explanation-h04: Opening hundreds of new connections simultaneously during a traffic burst can exhaust the database's connection limit.
- explanation-h04: Exhausting the database's connection limit produces outright errors, not just slowness.
- explanation-h04: A connection pool has a maximum size.
- explanation-h04: When all pooled connections are busy, new requests wait for one to free up rather than opening additional connections.
- explanation-h04: Making requests wait instead of opening extra connections protects the database from being overwhelmed.
- explanation-h04: Requests queuing or timing out under load is the signal that it is time to look at pool size.
- explanation-h05: Adding a queue introduces new complexity: retries, dead-letter handling, and idempotency.
- explanation-h05: Queues typically deliver messages at-least-once.
- explanation-h05: At-least-once delivery is why idempotency is needed.
- explanation-h05: If email service outages are rare and brief, a simple retry-with-backoff on the existing HTTP call could capture most of the reliability gain.
- explanation-h05: Running a queue carries operational overhead that retry-with-backoff avoids.
- explanation-h06: Splitting is likely to make deploys slower and riskier in the short term unless the actual bottleneck is something microservices specifically fix.
- explanation-h06: Microservices can help when the problem is a slow test suite, unclear ownership causing merge conflicts, or a monolith where any change requires a full redeploy of unrelated code.
- explanation-h06: Microservices help in those cases by letting teams deploy independently.
- explanation-h06: After splitting, a single logical change can require coordinated deploys across multiple repositories.
- explanation-h06: Premature service boundaries are expensive to redraw later.
- explanation-h06: The last 10-20 incidents should be reviewed to determine whether they are coupling-related or process-related.
- explanation-h06: A few days of pipeline and incident data will reveal which failure mode the team actually has.
- explanation-h06: For a six-person team, the failure mode is very likely process or tooling rather than something a service split fixes.
- summarization-h01: All other v2 endpoint calls must be migrated to their /v3/ equivalents before November 30.
- summarization-h02: As of Wednesday, 1 of the 3 reports had arrived.
- summarization-h02: Sender reputation was ruled out as a cause.
- summarization-h02: The customer should be followed up with once RLY-4812 resolves.
- summarization-h02: The customer should be contacted proactively if the provider has not responded within the 2-business-day window.
- summarization-h03: Adding workers when the database is the bottleneck makes the problem worse.
- summarization-h04: A tool named "bash" is being invoked.
- summarization-h04: The tool invocation includes a "command" parameter.
- summarization-h04: The command runs `cat` on the file /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-9pi3l86u/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-dgijk4db/memory/MEMORY.md
- summarization-h04: The command redirects standard error to /dev/null with `2>/dev/null`.
- summarization-h04: The command echoes "NONE" if the `cat` command fails.
- summarization-h04: The tool invocation includes a "description" parameter with the value "Check memory index".
- summarization-h04: The parameters are given in JSON format.
- summarization-h05: A large customer campaign is expected next quarter.

Added facts (styled only):

- code-review-h01: The code has four problems.
- code-review-h01: Floating-point comparison breaks the correction logic.
- code-review-h01: `0.1 + 0.2 != 0.3` in floating-point arithmetic.
- code-review-h01: Rounding drift can make the `sum(amounts) != total` check fail or pass unpredictably.
- code-review-h01: The unpredictable comparison can leave the last share wrong whether or not the fix branch runs.
- code-review-h01: Splitting $10 three ways gives `[3.33, 3.33, 3.34]`.
- code-review-h01: The result `[3.33, 3.33, 3.34]` is acceptable for that case.
- code-review-h01: Non-numeric input such as a string passes through without any error.
- code-review-h01: The suggested implementation raises `ValueError` with the message "people must be positive" when `people <= 0`.
- code-review-h01: The suggested implementation computes cents as `round(total * 100)`.
- code-review-h01: The suggested implementation uses `divmod(cents, people)` to obtain a base amount and a remainder.
- code-review-h01: The suggested implementation adds one cent to each of the first `remainder` shares.
- code-review-h01: The suggested implementation returns each amount divided by 100.
- code-review-h02: A function should either mutate its input or return a new array, not do both implicitly.
- code-review-h02: If in-place mutation is required so that other references observe the change, the loop should iterate backwards.
- code-review-h03: A trailing newline at the end of a file is common and will break `int(line)`.
- code-review-h03: Even after converting to a list up front, calling `sum()`, `len()`, and `max()` separately makes three passes instead of one.
- code-review-h04: The code logs the raw request via `logging.info("login attempt: %s", request)`.
- code-review-h04: Logging the raw request dumps the whole dict, so the plaintext password lands in log files.
- code-review-h04: The code compares passwords with `==` instead of a constant-time function.
- code-review-h04: Comparing passwords with `==` leaks timing information.
- code-review-h04: An attacker can use password comparison timing information to guess passwords character by character.
- code-review-h04: `hmac.compare_digest` should be used for password comparison.
- code-review-h04: The code stores and compares plaintext passwords.
- code-review-h04: The expression `user["password"]` implies passwords are not hashed at rest.
- code-review-h04: Passwords should be hashed with bcrypt, argon2, or scrypt.
- code-review-h04: Login should verify the supplied password against the stored hash.
- code-review-h04: The code uses `assert` to validate input.
- code-review-h04: Assertions are removed when Python runs under the `-O` flag.
- code-review-h04: Active assertions raise `AssertionError` rather than producing a proper 4xx response.
- code-review-h04: An attacker sending a malformed request gets a 500 response instead of a clean validation error.
- code-review-h04: The code has no rate limiting or lockout.
- code-review-h04: Nothing in the code stops brute-force attempts against `users`.
- code-review-h04: The code is missing type and emptiness checks on input.
- code-review-h04: `request["username"]` and `request["password"]` could be empty strings or non-strings.
- code-review-h04: The `assert` only checks key presence, not value validity.
- code-review-h04: There is no timeout or normalization on the `username` lookup, such as case sensitivity or leading/trailing whitespace handling.
- code-review-h04: The lack of username normalization is not a security bug.
- code-review-h04: The text identifies six problems plus one minor issue, listed roughly in order of severity.
- code-review-h05: The code has six real problems, one design question, and one clear leak.
- code-review-h05: The memory leak is the most serious issue in the code.
- code-review-h05: Under a single-threaded asyncio loop the function never yields mid-execution, so it is safe there.
- code-review-h05: A forward clock jump can flush the whole bucket early, granting free requests.
- code-review-h05: `time.monotonic()` would not help with the cross-process problem.
- code-review-h05: At `limit=20` the O(n) rebuild cost is trivial.
- code-review-h05: If a caller passes a much larger `limit`, the per-call cost grows with it.
- code-review-h05: The filter uses a strict `>` comparison.
- code-review-h05: Because of second truncation and the strict comparison, the actual window is between 59 and 60 seconds rather than exactly 60.
- code-review-h05: There is no key namespacing, which is a design question rather than obviously a bug.
- code-review-h05: Nothing prevents two unrelated call sites from reusing the same `key` and sharing a budget.
- code-review-h05: Shared keys may be intentional, with the caller expected to build composite keys like `"user:endpoint"`.
- code-review-h05: The function gives no signal about whether callers should build composite keys.
- code-review-h05: The append-then-filter sliding-window approach is a standard, reasonable technique for a simple in-memory limiter.
- code-review-h05: The shape of the algorithm is not the problem; the missing cleanup, locking, and clock choice are.
- code-review-h06: The environment-variable override assigns string values directly over `timeout`, `retries`, and `debug`.
- code-review-h06: `timeout` and `retries` have integer defaults.
- code-review-h06: The type-coercion bug stays hidden until someone tries to disable debug in production.
- code-review-h06: The same type-coercion risk applies if `config.json` contains `"timeout": "30"` as a string.
- debugging-h01: `functools.partial` is another way to capture the value at creation time.
- debugging-h01: `partial` is imported from the `functools` module.
- debugging-h01: The default-argument version is the simplest of the two fixes.
- debugging-h02: Passing `int(re.search(r"\d+", s).group())` as the `key` to `max()` selects the filename with the largest number.
- debugging-h03: The summed value 0.6000000000000001 is correct for practical purposes despite the strict comparison failing.
- debugging-h04: Adding a `Z` or a UTC offset to the ISO string makes the parsed datetime timezone-aware.
- debugging-h05: The most likely cause of the duplicate deliveries is that the receiver occasionally takes close to or over 30 seconds to respond, causing the sender to time out and retry a request that had already succeeded server-side.
- debugging-h05: A steady duplicate rate of about 0.5% is what you would expect when a small percentage of requests cross a fixed timeout threshold.
- debugging-h05: The observed duplicate rate is approximately 0.5%.
- debugging-h05: The duplicate pattern is caused by tail latency rather than random failure.
- debugging-h05: A receiver can process a webhook and return 2xx while the response is dropped before the sender sees it, due to a proxy reset, load balancer restart, or network blip.
- debugging-h05: When a success response is lost, the sender treats the delivery as a failure and retries.
- debugging-h05: A gateway or proxy in front of the receiver with a timeout shorter than the sender's 30 seconds can return an error to the sender while the receiver continues processing and completes successfully.
- debugging-h05: If the sender pulls webhooks from a queue such as SQS or Kafka, an acknowledgment slower than the visibility timeout can cause a second worker to redeliver the same event independently of HTTP-level retry logic.
- debugging-h05: Two sender processes can pick up the same event if a distributed lock is missing or broken.
- debugging-h05: The sender retries on any non-2xx response and uses a 30-second timeout.
- debugging-h05: Response-lost-after-success and receiver slowness past the timeout account for the vast majority of duplicate-delivery bugs in practice.
- debugging-h05: One customer has receiver-side delivery counts available.
- debugging-h05: If the gap between duplicate deliveries clusters around 30 seconds, that strongly confirms the timeout explanation.
- debugging-h05: A duplicate gap much shorter than 30 seconds or with no consistent pattern points toward queue redelivery or proxy issues.
- debugging-h05: The sender logs for the affected window have been deleted.
- debugging-h05: Root cause cannot be reconstructed retroactively with certainty because the sender logs for that window are gone.
- debugging-h05: Adding a delivery ID to every webhook attempt, logging send time, response time, and status code on the sender side, and having the receiver log the same delivery ID and its processing duration would enable diagnosis going forward.
- debugging-h05: If the sender's current p99/p999 latency to the affected endpoint sits near 25 to 30 seconds, that identifies the cause without needing to reproduce the issue.
- debugging-h05: Any gateway, load balancer, or reverse proxy between sender and receiver may time out before 30 seconds.
- debugging-h05: Synchronous downstream work during webhook processing, such as database writes or calls to other services, is the usual source of occasional slow responses.
- debugging-h05: Adding an idempotency key to the webhook payload and having the receiver dedupe on it is the standard fix for at-least-once delivery.
- debugging-h05: Deduplicating on an idempotency key makes pinning down the root cause less urgent.
- debugging-h06: The cold cache explanation fits the reported timeline best.
- debugging-h06: Connection or thread pool churn to a regional dependency is a plausible cause.
- debugging-h06: A deploy can cycle connections to a search index or database, and a rollback triggers another cycle.
- debugging-h06: Connection pools take time to re-establish a healthy steady state.
- debugging-h06: A hot shard or GC pressure on the search backend is a plausible cause.
- debugging-h06: A changed query pattern can hit one region's index harder, triggering segment merges or GC pauses.
- debugging-h06: Segment merges or GC pauses can outlive the code that caused them.
- debugging-h06: An incomplete or staggered rollback in that region is a plausible cause.
- debugging-h06: If some instances kept serving the new code after the rollback started, the effect would be prolonged.
- debugging-h06: If a deploy changes timeout or retry behavior asymmetrically by region, a backlog can keep queues hot even after rollback.
- debugging-h06: Most metrics backends, including Prometheus, Datadog, and CloudWatch, retain data far longer than the 24 hours the dashboard displays by default.
- debugging-h06: Raw metrics can be obtained by querying the underlying metrics store directly for the incident window.
- debugging-h06: The search backend has its own internal stats for the region, including cache hit rate, GC logs, per-shard latency, and connection counts.
- debugging-h06: Search backend internal stats often have separate, longer retention than service dashboards.
- debugging-h06: Load balancer and proxy access logs contain upstream latency and retry counts.
- debugging-h06: Load balancer and proxy access logs usually persist longer than dashboard data.
- debugging-h06: Config differences to check include canary percentage, feature flags, and region-specific overrides.
- debugging-h06: There are three regions in total, one of which was affected.
- debugging-h06: Instrumenting cache hit rate, pool saturation, and per-shard latency would provide live data during a recurrence instead of a data gap.
- explanation-h01: With client-supplied resource IDs, the client supplies the ID upfront instead of POST /orders generating a new ID.
- explanation-h01: PUT /orders/{client-generated-id} turns creation into an idempotent PUT.
- explanation-h01: Conditional writes use If-Match with an ETag.
- explanation-h01: If-Match with an ETag ensures a retry only applies if the resource is still in the state the client last saw.
- explanation-h01: Conditional writes prevent double application of a change.
- explanation-h02: Every index on a table needs the same maintenance on every write.
- explanation-h02: Wrapping a column in a function forces the database to compute the function for every row before it can compare.
- explanation-h03: Slow deep pages are especially painful for a table that accumulates orders indefinitely.
- explanation-h03: The cursor format becomes an implicit contract that must be kept stable.
- explanation-h04: Under light load, the cost of opening a new connection per request is not noticeable.
- explanation-h05: Traffic volume determines whether the queue itself becomes a new bottleneck or single point of failure.
- explanation-h05: At low traffic volume, an unbuffered queue is low-risk.
- explanation-h05: At high traffic volume, throughput requirements are needed to size the queue and to decide on partitioning, consumer scaling, and backpressure handling.
- explanation-h05: If the email service is down for only seconds at a time, a queue plus simple retries closes most of the gap.
- explanation-h05: If the email service is down for hours, message retention limits and dead-letter handling need consideration.
- explanation-h05: If the email service is down for hours, whether eventual email delivery is acceptable for the use case needs consideration.
- explanation-h05: A password-reset email delivered three hours late may be worse than a synchronous failure the caller can react to.
- explanation-h05: The recommended next step is to pull request volume per second on the order-to-email path.
- explanation-h05: The recommended next step is to pull email-service uptime over the last 1-3 months, or check its incident history.
- explanation-h05: If the data isn't available, a rough estimate or a week of monitoring is better than deciding without data.
- explanation-h06: A profiler or timestamped CI logs can reveal where deploy time goes within a day.
- explanation-h06: If the real cause is a slow test suite or CI queue, splitting produces five slow test suites and five CI queues instead of one.
- explanation-h06: Replacing function calls with network calls introduces latency and partial-failure bugs that did not exist before.
- explanation-h06: Staying monolithic and doing nothing causes coupling debt to compound.
- explanation-h06: A 40-minute test suite is an example of an actual cause that can be mistaken for a monolith problem.
- explanation-h06: The recommendation is to measure deploy time by stage for two weeks before deciding.
- explanation-h06: If most deploy time sits in test/build, fixing that is cheaper than splitting and is needed either way.
- explanation-h06: A modular monolith has clear internal boundaries and a single deploy.
- explanation-h06: A modular monolith provides decoupling without the operational cost of microservices.
- explanation-h06: A modular monolith should be considered before full microservices.
- summarization-h02: The customer checked their spam folder and found nothing.
- summarization-h04: The QA test list is ordered by risk.
- summarization-h04: The entity-prefix backfill migration is the highest-risk item on the list.
- summarization-h04: The entity-prefix backfill migration is irreversible.
- summarization-h04: The entity-prefix backfill migration touches historical records.
- summarization-h04: The backfill assigns an entity prefix to every existing invoice.
- summarization-h04: The API returns null for `invoice_number` on draft invoices.
- summarization-h04: Returning null for draft invoice numbers is a breaking behavior change for existing API consumers.
- summarization-h04: The shape of the `invoice_number` field is unchanged.
- summarization-h04: Consumers of the invoice API include billing dashboards, integrations, and webhooks.
- summarization-h04: Each legal entity has its own independent invoice number sequence.
- summarization-h04: Invoice numbers from one entity's sequence never collide with another entity's numbers.
- summarization-h04: Invoice numbers are allocated at finalize time rather than at creation time.
- summarization-h04: Deleting a draft invoice without finalizing it does not consume an invoice number.
- summarization-h04: Drafts that had numbers allocated before the release keep those numbers through finalization instead of being renumbered.
- summarization-h04: Finalized invoice PDFs display the prefixed invoice number.
- summarization-h04: Draft invoices may be rendered as PDFs without an invoice number.
- summarization-h04: The release includes a search index rebuild.
- summarization-h04: Search supports lookup by both old-style invoice numbers and new prefixed invoice numbers.

### classic-concise

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-h01 | 27 | 12 | 0.444 | 19 | 9 |
| code-review-h02 | 23 | 18 | 0.783 | 22 | 1 |
| code-review-h03 | 25 | 19 | 0.76 | 26 | 3 |
| code-review-h04 | 2 | 0 | 0.0 | 36 | 36 |
| code-review-h05 | 44 | 33 | 0.75 | 36 | 8 |
| code-review-h06 | 38 | 30 | 0.789 | 27 | 6 |
| debugging-h01 | 10 | 9 | 0.9 | 8 | 0 |
| debugging-h02 | 11 | 9 | 0.818 | 12 | 2 |
| debugging-h03 | 13 | 10 | 0.769 | 12 | 0 |
| debugging-h04 | 11 | 9 | 0.818 | 8 | 3 |
| debugging-h05 | 1 | 1 | 1.0 | 25 | 25 |
| debugging-h06 | 19 | 16 | 0.842 | 24 | 11 |
| explanation-h01 | 31 | 23 | 0.742 | 26 | 0 |
| explanation-h02 | 24 | 17 | 0.708 | 21 | 3 |
| explanation-h03 | 28 | 25 | 0.893 | 27 | 0 |
| explanation-h04 | 25 | 16 | 0.64 | 27 | 6 |
| explanation-h05 | 11 | 11 | 1.0 | 23 | 7 |
| explanation-h06 | 18 | 13 | 0.722 | 24 | 4 |
| summarization-h01 | 16 | 16 | 1.0 | 14 | 0 |
| summarization-h02 | 18 | 13 | 0.722 | 16 | 1 |
| summarization-h03 | 15 | 13 | 0.867 | 15 | 0 |
| summarization-h04 | 7 | 0 | 0.0 | 24 | 24 |
| summarization-h05 | 16 | 15 | 0.938 | 15 | 0 |
| summarization-h06 | 14 | 14 | 1.0 | 13 | 1 |

Median fraction: 0.786 over 24 scored pairs.

Median additions: 3.0 over 24 scored pairs.

Lost facts:

- code-review-h01: The expression `share * (people - 1)` uses the rounded per-person share instead of `total`.
- code-review-h01: Using the rounded share in that expression can compound floating-point error for larger `people` counts.
- code-review-h01: The last person's amount may drift by more than a cent instead of the intended ±0.01 correction.
- code-review-h01: With `total=100` and `people=7`, the last share comes out odd.
- code-review-h01: The corrected `amounts[-1]` is not re-rounded.
- code-review-h01: Because `amounts[-1]` is not re-rounded, it can end up with more than 2 decimal places due to float imprecision.
- code-review-h01: An example of that imprecision is a value of `33.33999999999999` instead of `33.34`.
- code-review-h01: The float equality check mostly works here because it only decides whether to apply a correction.
- code-review-h01: Passing `people` as a float such as `2.5` makes `[share] * people` raise a `TypeError`.
- code-review-h01: A list cannot be multiplied by a non-integer.
- code-review-h01: Python's `round()` uses banker's rounding, also called round-half-to-even.
- code-review-h01: Banker's rounding can surprise people who expect standard round-half-up behavior for money.
- code-review-h01: If the discrepancy exceeds one cent, the last person's share becomes visibly unfair rather than off by just a cent.
- code-review-h01: The code has no type hints and no docstring.
- code-review-h01: Without type hints or a docstring, the types and units of `total` and `people` are unclear to callers.
- code-review-h02: Iterating backwards with `for (let i = items.length - 1; i >= 0; i--)` fixes the skipping bug.
- code-review-h02: Decrementing `i` after a splice fixes the skipping bug.
- code-review-h02: The function also returns the same array it mutated.
- code-review-h02: The term "expired" often implies a `<=` comparison.
- code-review-h02: Using `var` is not a functional bug in this function because no closure captures `i`.
- code-review-h03: Without closing, the file descriptor stays open indefinitely.
- code-review-h03: The unclosed file is opened inside a generator expression, whose lifetime and closure are not obvious.
- code-review-h03: The code does not call `.strip()` on lines.
- code-review-h03: Not stripping lines means trailing whitespace-only lines could cause avoidable failures.
- code-review-h03: `int()` tolerates surrounding whitespace.
- code-review-h03: The code lacks input validation against negative counts, non-numeric types, and `None` values.
- code-review-h04: The speaker will check for relevant memory before reviewing.
- code-review-h04: A skill named auto-memory-check is being invoked.
- code-review-h05: `bucket = _hits.setdefault(key, [])` gets a shared reference to the list.
- code-review-h05: `bucket.append(now)` mutates the list in place.
- code-review-h05: Truncating to whole seconds makes the 60-second window fuzzy, ranging from about 59 to about 61 seconds.
- code-review-h05: `time.time()` can jump due to NTP correction or manual clock changes.
- code-review-h05: A backward clock jump makes `now - 60` smaller, which can make already-expired entries look valid again and stretch the effective window.
- code-review-h05: `time.monotonic()` would avoid the clock-jump problem.
- code-review-h05: Using `time.monotonic()` would require consistent use across all callers because monotonic time is not epoch-based.
- code-review-h05: A `collections.deque` with `popleft()` while entries are stale would be both correct and cheaper.
- code-review-h05: A deque would compose better with a fix that stops appending once over a hard cap.
- code-review-h05: The append-then-check ordering gives correct semantics: it allows exactly `limit` requests per window and blocks the (limit+1)th.
- code-review-h05: The multi-process issue is the one most likely to bite silently in deployment even though the code looks correct in isolation.
- code-review-h06: Values loaded from the JSON file can have real types such as int.
- code-review-h06: The debug boolean-string bug can appear to work in testing and silently misbehave in production.
- code-review-h06: The override loop applies even when the existing value is a dict or a list.
- code-review-h06: If a config file contains a nested value like {"database": {...}}, setting DATABASE in the environment replaces the whole nested structure with a single string.
- code-review-h06: The precedence order is likely deliberate and fine to keep, but needs documenting.
- code-review-h06: Whether the relative path is deliberate or accidental cannot be determined without seeing the calling services.
- code-review-h06: There is no schema validation on the JSON file, so arbitrary keys merge in unchecked.
- code-review-h06: The string-typing and blanket exception swallowing are the issues to fix first, especially the boolean footgun.
- debugging-h01: Both fixes work because they create a new variable scoped to each iteration or call.
- debugging-h02: If filenames always follow the exact snap-<N>.db pattern, the key can be simplified to int(s.split('-')[1].split('.')[0]).
- debugging-h02: int(s.split('-')[1].split('.')[0]) avoids using a regular expression.
- debugging-h03: Floating-point numbers in JavaScript use IEEE 754 double precision.
- debugging-h03: IEEE 754 double precision cannot represent most decimal fractions exactly.
- debugging-h03: Summing the integer cent values 10, 20, and 30 yields exactly 60.
- debugging-h04: Boundary handling options include rejecting naive timestamps or requiring input to always include an offset.
- debugging-h04: `2026-08-01T10:00:00+00:00` is an example of an ISO timestamp that includes an offset.
- debugging-h06: A rollback deploys new code but does not necessarily recycle running processes or pods.
- debugging-h06: Cache poisoning or a cold cache self-heals as TTLs expire or entries get overwritten.
- debugging-h06: Aggressive retries and open circuit breakers can take time to settle even after the triggering code is removed.
- explanation-h01: Not retrying a failed request risks leaving the operation undone.
- explanation-h01: Idempotency is treated as a prerequisite for automatic retry logic in HTTP clients, load balancers, and API gateways.
- explanation-h01: Per the HTTP spec, HEAD is idempotent and is the same as GET but without a body.
- explanation-h01: Idempotent is not the same as safe.
- explanation-h01: Safe means the method has no side effects at all.
- explanation-h01: Idempotency keys usually expire after some window, such as 24 hours, so storage does not grow forever.
- explanation-h01: Servers typically need to handle a duplicate request arriving while the first request is still processing, by returning a conflict/try-later response or blocking until done.
- explanation-h01: The idempotency key pattern is common in payment APIs such as Stripe and PayPal because double-charging is the worst-case failure mode.
- explanation-h02: B-trees typically have high fan-out, so the tree is shallow.
- explanation-h02: Because index keys are sorted, a B-tree index supports range scans and ordered retrieval without a separate sort step.
- explanation-h02: B-tree indexes help queries that sort by the indexed column.
- explanation-h02: Deletes can trigger node merges and rebalancing.
- explanation-h02: Each index causes extra disk I/O and WAL/log writes beyond the table's own row change.
- explanation-h02: An insert gets no query-side benefit from indexes because an insert is not a lookup.
- explanation-h02: You should index columns that are frequently filtered, sorted, or joined on.
- explanation-h03: Offset pagination is simple to implement using LIMIT/OFFSET in SQL.
- explanation-h03: Offset pagination is stateless and easy to reason about.
- explanation-h03: Cursor pagination requires a stable sort key and encoding/decoding of the cursor.
- explanation-h04: If the connection is encrypted, establishing it requires TLS negotiation, which adds several more round-trips and cryptographic operations.
- explanation-h04: Establishing a database connection requires session setup, in which the database allocates memory, spawns a backend process or thread, and initializes session state.
- explanation-h04: Postgres forks a process per connection.
- explanation-h04: Each step of establishing a database connection takes milliseconds.
- explanation-h04: A request that could be served in 5ms might take 50-100ms because of connection setup for a single query.
- explanation-h04: Postgres defaults to a limit of 100 concurrent connections.
- explanation-h04: Each open database connection consumes real memory and CPU on the server even when idle.
- explanation-h04: Requests queuing or timing out under load is the signal that it is time to look at pool size.
- explanation-h04: For a small app, the default pool settings are usually fine.
- explanation-h06: Microservices can help when the problem is a slow test suite, unclear ownership causing merge conflicts, or a monolith where any change requires a full redeploy of unrelated code.
- explanation-h06: Microservices help in those cases by letting teams deploy independently.
- explanation-h06: Splitting trades slow deploys for operational complexity.
- explanation-h06: After splitting, a single logical change can require coordinated deploys across multiple repositories.
- explanation-h06: For a six-person team, the failure mode is very likely process or tooling rather than something a service split fixes.
- summarization-h02: As of Wednesday, 1 of the 3 reports had arrived.
- summarization-h02: Sender reputation was ruled out as a cause.
- summarization-h02: No action is needed from the customer right now.
- summarization-h02: The customer should be followed up with once RLY-4812 resolves.
- summarization-h02: The customer should be contacted proactively if the provider has not responded within the 2-business-day window.
- summarization-h03: The third check applies if queue depth still grows while workers are alive.
- summarization-h03: Adding workers when the database is the bottleneck makes the problem worse.
- summarization-h04: A tool named "bash" is being invoked.
- summarization-h04: The tool invocation includes a "command" parameter.
- summarization-h04: The command runs `cat` on the file /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-9pi3l86u/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-dgijk4db/memory/MEMORY.md
- summarization-h04: The command redirects standard error to /dev/null with `2>/dev/null`.
- summarization-h04: The command echoes "NONE" if the `cat` command fails.
- summarization-h04: The tool invocation includes a "description" parameter with the value "Check memory index".
- summarization-h04: The parameters are given in JSON format.
- summarization-h05: A large customer campaign is expected next quarter.

Added facts (styled only):

- code-review-h01: Floating-point rounding errors make that equality comparison unreliable in both directions: it can trigger when it should not, and miss cases it should catch.
- code-review-h01: Passing a float or negative value for `people` silently corrupts the result.
- code-review-h01: Rounding to two decimal places assumes a currency with two decimal places.
- code-review-h01: The hardcoded two-decimal rounding breaks for other units.
- code-review-h01: The proposed `split_bill` raises ValueError with the message "people must be a positive integer" when `people` is not a positive integer.
- code-review-h01: The proposed implementation computes cents as `round(total * 100)`.
- code-review-h01: The proposed implementation uses `divmod(cents, people)` to get a base amount and a remainder.
- code-review-h01: The proposed implementation adds one cent to each of the first `remainder` amounts.
- code-review-h01: The proposed implementation returns amounts converted back to currency by dividing each by 100.
- code-review-h02: The name `removeExpired` suggests it should return a new array or warn about mutation.
- code-review-h03: The three passes are wasteful even when `numbers` is a list.
- code-review-h03: A single pass accumulating total, count, and maximum can replace the three passes.
- code-review-h03: An alternative fix is to accept only a list and iterate or slice once.
- code-review-h04: The code calls `logging.info("login attempt: %s", request)`, which logs the raw request.
- code-review-h04: The raw request logged includes the plaintext password.
- code-review-h04: Only the username should be logged instead of the full request.
- code-review-h04: Passwords in the code are compared using the `==` operator.
- code-review-h04: Passwords in the code are stored and compared in plaintext.
- code-review-h04: `hmac.compare_digest` is a constant-time comparison function.
- code-review-h04: Password comparison should use a constant-time comparison such as `hmac.compare_digest`.
- code-review-h04: Passwords should be hashed with an algorithm such as bcrypt or argon2 rather than stored or compared as raw text.
- code-review-h04: The code uses `assert` to enforce input validation.
- code-review-h04: Assert statements are removed when Python runs with the `-O` flag.
- code-review-h04: Because asserts vanish under `python -O`, a missing key would raise `KeyError` or `TypeError` in production instead of failing cleanly.
- code-review-h04: Input validation should use an explicit check that raises or returns an error rather than `assert`.
- code-review-h04: The code performs no type or presence check on `request["username"]` and `request["password"]` beyond checking key existence.
- code-review-h04: Empty strings or values of the wrong type, such as a list, pass through the code's validation.
- code-review-h04: The expression `user["token"]` assumes every user record has a `token` key.
- code-review-h04: A malformed user record without a `token` key would throw `KeyError` instead of producing a handled error.
- code-review-h04: The code has no rate limiting or lockout.
- code-review-h04: Without rate limiting or lockout, the function permits unlimited brute-force attempts.
- code-review-h04: Rate limiting is arguably outside the scope of this function.
- code-review-h04: The error message "bad username or password" is good practice because it avoids user enumeration.
- code-review-h04: The generic error message should be kept.
- code-review-h04: Exceptions from malformed input could leak more specific errors elsewhere.
- code-review-h04: The function takes `users` as a raw dict.
- code-review-h04: The code provides no abstraction for a real datastore.
- code-review-h04: The lack of a datastore abstraction may be intentional for this snippet.
- code-review-h04: The suggested fix uses `request.get("username")` and `request.get("password")` to retrieve credentials.
- code-review-h04: The suggested fix returns `{"ok": False, "error": "bad username or password"}` when username or password is missing or empty.
- code-review-h04: The suggested fix logs only the username via `logging.info("login attempt: %s", username)`.
- code-review-h04: The suggested fix looks up the user with `users.get(username)`.
- code-review-h04: The suggested fix compares passwords with `hmac.compare_digest(user["password"], password)`.
- code-review-h04: The suggested fix returns `{"ok": True, "token": user["token"]}` on successful authentication.
- code-review-h04: The suggested fix imports `hmac` and `logging`.
- code-review-h04: The suggested fix still assumes `user["password"]` is a stored plaintext or hash comparable via `compare_digest`.
- code-review-h04: In a real system, a password should be verified against a hashed password using something like `bcrypt.checkpw`.
- code-review-h04: The listed problems are ordered by severity.
- code-review-h04: The problems are grouped into the categories Security, Correctness, and Style/robustness.
- code-review-h05: The thread-safety bug only shows up under load and won't appear in casual testing.
- code-review-h05: Second-granularity timing lets a burst land on both sides of a window boundary and effectively double the allowed rate for short bursts.
- code-review-h05: The per-process design could be an intentional 'good enough for now' simplification, but it is not documented anywhere.
- code-review-h05: Counting rejected requests is standard practice for abuse prevention because it stops attackers from resetting their budget by spamming past the limit.
- code-review-h05: Counting rejected requests is probably deliberate.
- code-review-h05: Counting rejected requests is what drives the unbounded-burst memory issue, so the two issues should be fixed together rather than separately.
- code-review-h05: `limit` is exposed as a parameter while the `60`-second window is buried in a list comprehension, making their exposure inconsistent.
- code-review-h05: The third recommended fix is evicting idle keys or switching to a Redis-backed counter with TTL, which solves both the leak and the multi-process problem at once.
- code-review-h06: The default config contains the keys `timeout`, `retries`, and `debug`.
- code-review-h06: The default parameter is `path="config.json"`.
- code-review-h06: Environment variables overriding file config is a common intentional pattern associated with 12-factor style.
- code-review-h06: Restricting environment overrides to pre-defined keys may be intentional or may be an oversight of the `for key in config` implementation.
- code-review-h06: Changing the exception handling or type coercion could break callers relying on the current behavior.
- code-review-h06: A caller might already stringify `timeout` itself.
- debugging-h02: `max()` accepts a `key` function to determine which element is largest.
- debugging-h02: Using the extracted-number key, `max()` over ["snap-9.db", "snap-10.db", "snap-11.db"] returns "snap-11.db".
- debugging-h04: A datetime's `tzinfo` attribute is `None` when the datetime is offset-naive.
- debugging-h04: Checking `created.tzinfo is None` before calling `replace` handles source strings that sometimes carry an offset.
- debugging-h04: Attaching UTC to a timestamp that is not actually UTC is incorrect; the correct offset should be used instead.
- debugging-h05: A receiver can commit an event while the 2xx response never reaches the sender.
- debugging-h05: A lost response can be caused by a network drop, a receiver crash after the write, or slow serialization.
- debugging-h05: When a response is lost before the sender's 30-second timeout, the sender retries a delivery that already succeeded.
- debugging-h05: Retrying an already-succeeded delivery is the classic at-least-once failure mode.
- debugging-h05: A lost-response failure fits a rare, timeout-shaped duplicate rate such as 1 in 200.
- debugging-h05: Receiver latency spikes near 30 seconds can cause duplicate deliveries.
- debugging-h05: GC pauses, lock contention, cold starts, and downstream dependency slowness can push processing past 30 seconds.
- debugging-h05: Processing that exceeds 30 seconds can still eventually succeed.
- debugging-h05: A load balancer or reverse proxy in front of the receiver can retry independently of application logic.
- debugging-h05: A load balancer or reverse proxy has its own idle or read timeout.
- debugging-h05: Proxy-level retries can occur even when the application would have returned 2xx in time.
- debugging-h05: A receiver can return a transient 500 or 429 after the event was already persisted.
- debugging-h05: An error after commit can originate in a post-commit hook or a response-building step.
- debugging-h05: A sender-side worker crash or restart after dispatch but before marking a delivery as 'delivered' causes redelivery.
- debugging-h05: Sender-side redelivery from a worker crash is independent of any timeout.
- debugging-h05: The time gap between duplicate deliveries can be measured for an affected customer.
- debugging-h05: Duplicate deliveries roughly 30 seconds apart implicate the sender's timeout.
- debugging-h05: Near-instant or random gaps between duplicates point to proxy retries or sender-side redispatch.
- debugging-h05: Receiver-side access logs and APM show what status was returned and how long the request took, even without sender logs.
- debugging-h05: p99 latency at the time of duplication can be checked against the 30-second threshold.
- debugging-h05: Many default idle timeouts sit close to common sender timeouts of 30 and 60 seconds.
- debugging-h05: Duplicate timestamps can be correlated with deploys, GC logs, or infrastructure incidents on the receiver side.
- debugging-h05: Adding an idempotency key based on event ID and deduping on the receiver neutralizes customer impact immediately.
- debugging-h05: Deduping on the receiver works regardless of the root cause.
- debugging-h05: Retaining sender-side delivery attempt logs with attempt number, status, and latency makes future occurrences diagnosable rather than inferred.
- debugging-h06: The latency doubled after a deploy.
- debugging-h06: The problem affected one region out of three.
- debugging-h06: A config or feature flag can remain flipped after a rollback.
- debugging-h06: A canary or rollout system can fail to revert on all hosts.
- debugging-h06: New code can ship with a different query pattern or index usage.
- debugging-h06: A deploy that changes pod counts or restarts instances can leave stale long-lived connections routed to draining or unhealthy nodes.
- debugging-h06: Prometheus remote-write, Datadog, and CloudWatch are examples of long-term metric stores.
- debugging-h06: Infrastructure provider billing and monitoring data often retains 15 or more days.
- debugging-h06: Regions can differ in instance types, pool sizes, index versions, and traffic volume.
- debugging-h06: Some database migrations do not reverse cleanly.
- debugging-h06: Connection pool max-idle time, DNS cache TTL, autoscaler cooldown, and index/cache warm-up are stack components with characteristic timeouts or TTLs.
- explanation-h02: A table with a million rows needs only 3-4 comparisons to find a row via a B-tree index.
- explanation-h02: Leaf nodes in a B-tree are linked to each other.
- explanation-h02: Because leaf nodes are linked, range scans read a contiguous slice of the index instead of the whole table.
- explanation-h04: Constantly creating and tearing down connections burns CPU on both the client and the database side.
- explanation-h04: A typical connection pool size is 5 to 20 connections.
- explanation-h04: SQLAlchemy includes connection pooling.
- explanation-h04: HikariCP includes connection pooling.
- explanation-h04: The `pg` driver in Node includes connection pooling.
- explanation-h04: Go's `database/sql` includes connection pooling.
- explanation-h05: A failed HTTP call to the email service results in the email being lost.
- explanation-h05: With a queue, a worker retries against the email service until it succeeds.
- explanation-h05: Using a queue introduces concerns about queue durability.
- explanation-h05: Using a queue introduces concerns about consumer lag.
- explanation-h05: The recommended first step is to obtain the error rate from the email service and the current request volume.
- explanation-h05: If numbers cannot be obtained quickly, a simpler fix such as retry with exponential backoff or a circuit breaker may deliver most of the reliability gain.
- explanation-h05: Retry with exponential backoff and circuit breakers do not require adding infrastructure.
- explanation-h06: Splitting a monolith only helps the coordination-between-engineers case.
- explanation-h06: If a team stays monolithic, coordination pain returns as the team grows past roughly 8-10 engineers.
- explanation-h06: Velocity often drops for 6-12 months after a split before any gain appears.
- explanation-h06: Modularizing the monolith with clear internal boundaries is a smaller step than splitting into services.
- summarization-h02: After the whitelisting, one report started arriving.
- summarization-h04: The invoice numbering rework is undergoing QA testing.
- summarization-h04: Migration correctness is the highest-risk area of the invoice numbering rework.
- summarization-h04: The migration is hard to reverse.
- summarization-h04: The rework includes a backfill process for existing invoices.
- summarization-h04: The backfill can be run against a full copy of production data.
- summarization-h04: Existing invoices are assigned an entity prefix by the migration.
- summarization-h04: Existing invoice numbers are not supposed to change during migration.
- summarization-h04: Invoices can belong to multiple different legal entities.
- summarization-h04: The `invoice_number` field returns null for draft invoices.
- summarization-h04: Existing integrations, webhooks, and reports may assume `invoice_number` is non-null.
- summarization-h04: Invoice number sequences are maintained per legal entity.
- summarization-h04: Invoices can be created concurrently across different legal entities.
- summarization-h04: Cross-entity number collisions are a possible failure mode.
- summarization-h04: Concurrent finalization within the same entity can cause race conditions.
- summarization-h04: An invoice number is allocated when a draft is finalized, not when it is created.
- summarization-h04: Drafts can be finalized out of the order in which they were created.
- summarization-h04: Unfinalized drafts do not reserve invoice numbers under the new scheme.
- summarization-h04: Drafts created before this release have pre-allocated invoice numbers.
- summarization-h04: Legacy drafts should finalize without being renumbered.
- summarization-h04: Invoice PDFs display the invoice number.
- summarization-h04: PDFs may be generated for draft invoices.
- summarization-h04: The search index is rebuilt as part of the rework.
- summarization-h04: Invoices are searchable by invoice number.
- summarization-h04: Both an old and a new invoice number format exist.
- summarization-h06: The same IP range then produced two successful logins.

### developer-docs

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-h01 | 27 | 15 | 0.556 | 21 | 4 |
| code-review-h02 | 23 | 17 | 0.739 | 29 | 4 |
| code-review-h03 | 25 | 19 | 0.76 | 24 | 5 |
| code-review-h04 | 2 | 1 | 0.5 | 7 | 5 |
| code-review-h05 | 44 | 33 | 0.75 | 28 | 5 |
| code-review-h06 | 38 | 0 | 0.0 | 1 | 1 |
| debugging-h01 | 10 | 8 | 0.8 | 11 | 3 |
| debugging-h02 | 11 | 9 | 0.818 | 9 | 0 |
| debugging-h03 | 13 | 12 | 0.923 | 14 | 2 |
| debugging-h04 | 11 | 10 | 0.909 | 14 | 4 |
| debugging-h05 | 1 | 1 | 1.0 | 26 | 26 |
| debugging-h06 | 19 | 13 | 0.684 | 30 | 10 |
| explanation-h01 | 31 | 24 | 0.774 | 36 | 7 |
| explanation-h02 | 24 | 15 | 0.625 | 20 | 0 |
| explanation-h03 | 28 | 25 | 0.893 | 20 | 0 |
| explanation-h04 | 25 | 17 | 0.68 | 23 | 4 |
| explanation-h05 | 11 | 7 | 0.636 | 28 | 14 |
| explanation-h06 | 18 | 11 | 0.611 | 32 | 18 |
| summarization-h01 | 16 | 15 | 0.938 | 15 | 0 |
| summarization-h02 | 18 | 14 | 0.778 | 16 | 4 |
| summarization-h03 | 15 | 13 | 0.867 | 15 | 0 |
| summarization-h04 | 7 | 0 | 0.0 | 24 | 23 |
| summarization-h05 | 16 | 14 | 0.875 | 16 | 2 |
| summarization-h06 | 14 | 14 | 1.0 | 12 | 0 |

Median fraction: 0.767 over 24 scored pairs.

Median additions: 4.0 over 24 scored pairs.

Lost facts:

- code-review-h01: The expression `share * (people - 1)` uses the rounded per-person share instead of `total`.
- code-review-h01: Using the rounded share in that expression can compound floating-point error for larger `people` counts.
- code-review-h01: With `total=100` and `people=7`, the last share comes out odd.
- code-review-h01: An example of that imprecision is a value of `33.33999999999999` instead of `33.34`.
- code-review-h01: The float equality check mostly works here because it only decides whether to apply a correction.
- code-review-h01: Passing `people` as a float such as `2.5` makes `[share] * people` raise a `TypeError`.
- code-review-h01: A list cannot be multiplied by a non-integer.
- code-review-h01: Using `float` for currency is the root problem in this code.
- code-review-h01: Python's `round()` uses banker's rounding, also called round-half-to-even.
- code-review-h01: Banker's rounding can surprise people who expect standard round-half-up behavior for money.
- code-review-h01: The code has no type hints and no docstring.
- code-review-h01: Without type hints or a docstring, the types and units of `total` and `people` are unclear to callers.
- code-review-h02: Iterating backwards with `for (let i = items.length - 1; i >= 0; i--)` fixes the skipping bug.
- code-review-h02: Decrementing `i` after a splice fixes the skipping bug.
- code-review-h02: With the condition `expires < now`, items expiring exactly at `now` are kept rather than removed.
- code-review-h02: The term "expired" often implies a `<=` comparison.
- code-review-h02: If an item lacks an `expires` property, `undefined < now` evaluates to `false`.
- code-review-h02: An item missing `expires` is silently kept rather than flagged or erroring.
- code-review-h03: Without closing, the file descriptor stays open indefinitely.
- code-review-h03: The unclosed file is opened inside a generator expression, whose lifetime and closure are not obvious.
- code-review-h03: Not stripping lines means trailing whitespace-only lines could cause avoidable failures.
- code-review-h03: `int()` tolerates surrounding whitespace.
- code-review-h03: The function signature does not document that it requires a reusable sequence such as a list or tuple rather than a one-shot iterator.
- code-review-h03: The code lacks input validation against negative counts, non-numeric types, and `None` values.
- code-review-h04: A skill named auto-memory-check is being invoked.
- code-review-h05: `bucket = _hits.setdefault(key, [])` gets a shared reference to the list.
- code-review-h05: `int(time.time())` truncates timestamps to whole seconds.
- code-review-h05: Truncating to whole seconds makes the 60-second window fuzzy, ranging from about 59 to about 61 seconds.
- code-review-h05: The fixed-window imprecision is a minor issue.
- code-review-h05: The limiter is not a precise sliding window.
- code-review-h05: Using `time.monotonic()` would require consistent use across all callers because monotonic time is not epoch-based.
- code-review-h05: A `collections.deque` with `popleft()` while entries are stale would be both correct and cheaper.
- code-review-h05: A deque would compose better with a fix that stops appending once over a hard cap.
- code-review-h05: The magic numbers with no rationale is a problem the user previously flagged.
- code-review-h05: The concurrency race and the unbounded burst growth are the two issues to fix before production traffic.
- code-review-h05: The multi-process issue is the one most likely to bite silently in deployment even though the code looks correct in isolation.
- code-review-h06: The code calls config.update(json.load(f)) to merge values from a JSON file into the config.
- code-review-h06: Values loaded from the JSON file can have real types such as int.
- code-review-h06: Values read from os.environ are always strings.
- code-review-h06: Environment variable overrides silently change the types of config values.
- code-review-h06: The timeout value could end up as the int 30 or the string "45" depending on which layer set it last.
- code-review-h06: Callers performing arithmetic on timeout, such as sleep(timeout) or timeout + margin, will work in some deployments and crash in others.
- code-review-h06: Setting DEBUG=false in the environment makes config["debug"] the string "false".
- code-review-h06: A non-empty string such as "false" is truthy in Python.
- code-review-h06: The check if config["debug"]: will evaluate as true even when the operator set DEBUG=false.
- code-review-h06: The debug boolean-string bug can appear to work in testing and silently misbehave in production.
- code-review-h06: The loop performs config[key] = os.environ[key.upper()] for every key in config.
- code-review-h06: The override loop includes keys that were added by the JSON file.
- code-review-h06: The override loop applies even when the existing value is a dict or a list.
- code-review-h06: If a config file contains a nested value like {"database": {...}}, setting DATABASE in the environment replaces the whole nested structure with a single string.
- code-review-h06: The env override code has no type-awareness.
- code-review-h06: The code uses except Exception: pass around the config file load.
- code-review-h06: The bare except swallows FileNotFoundError, which was probably the intended case.
- code-review-h06: The bare except also swallows json.JSONDecodeError, PermissionError, and UnicodeDecodeError.
- code-review-h06: A malformed config file is a real operational problem.
- code-review-h06: A deploy with a broken config file will silently run on defaults with no log output.
- code-review-h06: The code has no logging anywhere.
- code-review-h06: Silently swallowing a parse error in an existing file is hard to justify and warrants at least a log line.
- code-review-h06: The precedence order is defaults, then file, then environment.
- code-review-h06: Environment overriding file overriding defaults is a standard convention.
- code-review-h06: The precedence order is likely deliberate and fine to keep, but needs documenting.
- code-review-h06: The default config path is the relative path "config.json".
- code-review-h06: Resolution of the relative default path depends on the caller's current working directory.
- code-review-h06: Whether the relative path is deliberate or accidental cannot be determined without seeing the calling services.
- code-review-h06: There is no schema validation on the JSON file, so arbitrary keys merge in unchecked.
- code-review-h06: There is no casting of env values against the type of the existing default.
- code-review-h06: Casting env values to the type of the existing default would fix both the type-change bug and the boolean-string bug.
- code-review-h06: The function has no way to signal to the caller that config loading failed.
- code-review-h06: Everything degrades silently to defaults, which may not match what depending services expect on startup.
- code-review-h06: The fallback-to-defaults-on-missing-file behavior appears intentional and reasonable.
- code-review-h06: The string-typing of env overrides appears accidental rather than intended.
- code-review-h06: The blanket exception swallowing that also hides malformed JSON appears accidental rather than intended.
- code-review-h06: The string-typing and blanket exception swallowing are the issues to fix first, especially the boolean footgun.
- code-review-h06: The boolean footgun can cause a debug flag to do the opposite of what someone typed.
- debugging-h01: An alternative fix is a factory function that takes `name` and returns a lambda.
- debugging-h01: Both fixes work because they create a new variable scoped to each iteration or call.
- debugging-h02: If filenames always follow the exact snap-<N>.db pattern, the key can be simplified to int(s.split('-')[1].split('.')[0]).
- debugging-h02: int(s.split('-')[1].split('.')[0]) avoids using a regular expression.
- debugging-h03: decimal.js is a decimal library.
- debugging-h04: When input strings sometimes include an offset and sometimes do not, validating or normalizing at the boundary is preferable to guessing the zone.
- debugging-h06: Latency stayed elevated for about another hour after the rollback.
- debugging-h06: A rollback deploys new code but does not necessarily recycle running processes or pods.
- debugging-h06: A connection, thread, or memory leak on running instances clears only when instances restart or connections time out.
- debugging-h06: A roughly one-hour capacity stabilization time matches typical ASG cooldown and stabilization windows.
- debugging-h06: Aggressive retries and open circuit breakers can take time to settle even after the triggering code is removed.
- debugging-h06: Region-specific configuration differences can cause only one region to exercise a bad code path.
- explanation-h01: Idempotency is treated as a prerequisite for automatic retry logic in HTTP clients, load balancers, and API gateways.
- explanation-h01: Idempotent is not the same as safe.
- explanation-h01: Safe means the method has no side effects at all.
- explanation-h01: GET and HEAD are safe methods.
- explanation-h01: Idempotency keys usually expire after some window, such as 24 hours, so storage does not grow forever.
- explanation-h01: Servers typically need to handle a duplicate request arriving while the first request is still processing, by returning a conflict/try-later response or blocking until done.
- explanation-h01: The idempotency key pattern is common in payment APIs such as Stripe and PayPal because double-charging is the worst-case failure mode.
- explanation-h02: Scanning every row in a table is O(n).
- explanation-h02: Using a B-tree index, the database walks the tree from root to leaf making O(log n) comparisons to locate matching rows.
- explanation-h02: Because index keys are sorted, a B-tree index supports range scans and ordered retrieval without a separate sort step.
- explanation-h02: B-tree indexes help queries that sort by the indexed column.
- explanation-h02: Deletes can trigger node merges and rebalancing.
- explanation-h02: Each index causes extra disk I/O and WAL/log writes beyond the table's own row change.
- explanation-h02: An insert gets no query-side benefit from indexes because an insert is not a lookup.
- explanation-h02: You should index columns that are frequently filtered, sorted, or joined on.
- explanation-h02: You should avoid over-indexing tables with heavy write traffic.
- explanation-h03: Offset pagination is stateless and easy to reason about.
- explanation-h03: Cursor pagination uses a request of the form GET /orders?limit=20&after=order_123.
- explanation-h03: For a typical 'list orders' endpoint, cursor pagination is usually the better default.
- explanation-h04: If the connection is encrypted, establishing it requires TLS negotiation, which adds several more round-trips and cryptographic operations.
- explanation-h04: Postgres forks a process per connection.
- explanation-h04: A request that could be served in 5ms might take 50-100ms because of connection setup for a single query.
- explanation-h04: Postgres defaults to a limit of 100 concurrent connections.
- explanation-h04: Each open database connection consumes real memory and CPU on the server even when idle.
- explanation-h04: When all pooled connections are busy, new requests wait for one to free up rather than opening additional connections.
- explanation-h04: Making requests wait instead of opening extra connections protects the database from being overwhelmed.
- explanation-h04: Requests queuing or timing out under load is the signal that it is time to look at pool size.
- explanation-h05: Adding a queue trades the requirement that the email service be up for the requirement that the queue be up.
- explanation-h05: Adding a queue introduces new complexity: retries, dead-letter handling, and idempotency.
- explanation-h05: Queues typically deliver messages at-least-once.
- explanation-h05: At-least-once delivery is why idempotency is needed.
- explanation-h06: Splitting is likely to make deploys slower and riskier in the short term unless the actual bottleneck is something microservices specifically fix.
- explanation-h06: Microservices can help when the problem is a slow test suite, unclear ownership causing merge conflicts, or a monolith where any change requires a full redeploy of unrelated code.
- explanation-h06: Microservices help in those cases by letting teams deploy independently.
- explanation-h06: Staying monolithic means deploys stay coupled and the blast radius stays large.
- explanation-h06: Premature service boundaries are expensive to redraw later.
- explanation-h06: The last 10-20 incidents should be reviewed to determine whether they are coupling-related or process-related.
- explanation-h06: A few days of pipeline and incident data will reveal which failure mode the team actually has.
- summarization-h01: All other v2 endpoint calls must be migrated to their /v3/ equivalents before November 30.
- summarization-h02: Sender reputation was ruled out as a cause.
- summarization-h02: Once the provider responds, their trace should be correlated against internal delivery logs for the 2 missing report IDs.
- summarization-h02: No action is needed from the customer right now.
- summarization-h02: The customer should be contacted proactively if the provider has not responded within the 2-business-day window.
- summarization-h03: The third check applies if queue depth still grows while workers are alive.
- summarization-h03: Adding workers when the database is the bottleneck makes the problem worse.
- summarization-h04: A tool named "bash" is being invoked.
- summarization-h04: The tool invocation includes a "command" parameter.
- summarization-h04: The command runs `cat` on the file /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-9pi3l86u/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-dgijk4db/memory/MEMORY.md
- summarization-h04: The command redirects standard error to /dev/null with `2>/dev/null`.
- summarization-h04: The command echoes "NONE" if the `cat` command fails.
- summarization-h04: The tool invocation includes a "description" parameter with the value "Check memory index".
- summarization-h04: The parameters are given in JSON format.
- summarization-h05: Storage usage was tracked monthly.
- summarization-h05: A large customer campaign is expected next quarter.

Added facts (styled only):

- code-review-h01: Passing a negative value for people produces a negative share.
- code-review-h01: A negative or non-numeric `total` passes through the function without raising a clear error.
- code-review-h01: The suggested fix converts `total` to `Decimal` via `Decimal(str(total))`.
- code-review-h01: The suggested fix returns a list of floats converted from Decimal values.
- code-review-h02: Code that iterates items elsewhere while this function runs can break.
- code-review-h02: If items is null, undefined, or not an array, the function throws instead of failing predictably.
- code-review-h02: If now is not the same type as expires, the comparison silently gives the wrong result.
- code-review-h02: Comparing a Date against a timestamp is an example of a type mismatch between now and expires.
- code-review-h03: Without closing, the file stays open until the process exits or the garbage collector reclaims it.
- code-review-h03: The caller has no way to recover from malformed data or report which line failed.
- code-review-h03: `open("data.txt")` raises `FileNotFoundError` when the file is missing.
- code-review-h03: The `FileNotFoundError` carries no context about what the script was trying to do.
- code-review-h03: If `numbers` is already a list, `list(numbers)` copies it for no reason.
- code-review-h04: The context being sought concerns how the user prefers code reviews to be structured.
- code-review-h04: The assistant's memory is stored in a directory on the filesystem.
- code-review-h04: The memory directory path is /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-9pi3l86u/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-dgijk4db/memory/
- code-review-h04: The memory directory's contents can be listed with the shell command ls.
- code-review-h04: The assistant ran a Bash command to list the contents of the memory directory.
- code-review-h05: Lost appends from concurrent access can cause some requests to be dropped unfairly.
- code-review-h05: Most web frameworks do not guarantee single-threaded access.
- code-review-h05: Monotonic time is not usable across processes in shared storage such as Redis.
- code-review-h05: Counting rejected requests against the caller is standard rate limiter behavior.
- code-review-h05: Counting rejected requests prevents a client from retrying its way to a window reset.
- code-review-h06: The speaker will check memory for relevant prior guidance before reviewing.
- debugging-h01: `functools.partial` is an alternative solution.
- debugging-h01: `functools.partial` freezes the value at creation time.
- debugging-h01: `partial(print, "handling " + name)` can be used to create the handlers.
- debugging-h03: The sum `0.6000000000000001` is correct for practical purposes.
- debugging-h03: Dividing a total in integer cents by 100 converts it back to currency units.
- debugging-h04: `datetime` and `timezone` are importable from the `datetime` module.
- debugging-h04: `(datetime.now(timezone.utc) - created_at).total_seconds()` computes the age of `created_at` in seconds.
- debugging-h04: `created.tzinfo is None` tests whether a datetime is offset-naive.
- debugging-h04: `.replace(tzinfo=timezone.utc)` should be applied only when `created.tzinfo is None` if the input string might already include an offset.
- debugging-h05: Slow receiver response is the most likely cause of the duplicate webhook deliveries.
- debugging-h05: A receiver can process a webhook successfully but take longer than 30 seconds to respond.
- debugging-h05: The sender's timeout is 30 seconds.
- debugging-h05: When the sender times out, it assumes failure and retries even though the first delivery succeeded.
- debugging-h05: A receiver may send a 2xx response that never reaches the sender due to a dropped connection or proxy reset.
- debugging-h05: A lost response causes the sender to retry a request that already succeeded.
- debugging-h05: A load balancer or gateway with a timeout shorter than the sender's 30 seconds can return its own error to the sender.
- debugging-h05: In a timeout mismatch case, the receiver keeps processing and later returns 200.
- debugging-h05: A receiver bug can perform a side effect, such as a database write, before a later step fails and returns a non-2xx.
- debugging-h05: A partial-failure bug causes retries to produce a real duplicate side effect rather than only a duplicate delivery.
- debugging-h05: A sender-side retry bug is less likely given the steady rate of about 0.5%.
- debugging-h05: The duplicate rate is approximately 0.5%.
- debugging-h05: A race condition dispatching two retries per failure would look identical from the receiver's side.
- debugging-h05: Duplicate pairs can be sampled from the receiver's logs and compared by timestamp for the same delivery or event ID.
- debugging-h05: A timestamp gap near 30 seconds indicates a timeout-driven retry, pointing to causes 1 through 3.
- debugging-h05: A timestamp gap near zero points to parallel dispatch, cause 5.
- debugging-h05: A receiver first-delivery response latency close to or over 30 seconds confirms slow receiver response as the cause.
- debugging-h05: A load balancer or API gateway timeout value under 30 seconds confirms the timeout mismatch cause.
- debugging-h05: Connection resets or truncated responses in the receiver's access logs point to the lost-response cause.
- debugging-h05: Finding a side effect in the receiver's handler that runs before a later step can return a non-2xx confirms the partial-failure cause.
- debugging-h05: The sender logs for the affected window are missing.
- debugging-h05: The window of missing sender logs cannot be reconstructed.
- debugging-h05: Durable logging recording delivery ID, response status, and round-trip latency for every send should be added going forward.
- debugging-h05: Whether webhooks already carry a stable delivery ID should be confirmed.
- debugging-h05: If webhooks carry a stable delivery ID, the customer should be advised to dedupe on it.
- debugging-h05: Deduping on a stable delivery ID removes the customer-visible symptom regardless of the underlying cause.
- debugging-h06: The incident involved a latency doubling in one of three regions.
- debugging-h06: A config or feature flag that did not roll back cleanly is a likely cause.
- debugging-h06: If a flag or config change persists after a code rollback, latency stays high until something else resets it, such as a TTL, restart, or cache expiry.
- debugging-h06: A rolling restart that landed unevenly across regions is a likely cause.
- debugging-h06: If the deploy and rollback both roll out region by region, a node in the affected region could have stayed in a bad state longer than nodes elsewhere.
- debugging-h06: Bad node states include garbage collection, cold JIT, and index warm-up.
- debugging-h06: Comparing the three regions' deploy and rollback timestamps is a way to narrow down the cause.
- debugging-h06: If the regions did not roll back at the same time, a lag in one region explains both the localization and the delayed recovery.
- debugging-h06: A code-only rollback does not revert config, feature flag, or infrastructure changes that shipped alongside the code.
- debugging-h06: If the same region shows the same latency doubling under close observation, that confirms the deploy is the cause.
- explanation-h01: Retrying is the only practical recovery from an unknown request outcome.
- explanation-h01: Idempotent does not mean an operation returns the same response every time.
- explanation-h01: A DELETE might return 200 OK the first time and 404 Not Found the second time.
- explanation-h01: Some services combine idempotency keys with conditional requests, such as an If-Match header carrying a resource version.
- explanation-h01: A conditional request makes a write apply only if the resource has not changed since the client last read it.
- explanation-h01: Conditional requests protect against concurrent writes, a different problem from retries.
- explanation-h01: Conditional requests work alongside idempotency keys toward the goal of predictable behavior under retries.
- explanation-h04: Opening a connection requires the client to resolve the database host.
- explanation-h04: Under load, the database spends CPU and memory on connection setup instead of on queries.
- explanation-h04: A traffic burst in which each request opens its own connection can hit the database's connection limit and cause requests to be rejected, even when the actual query load is light.
- explanation-h04: Pool settings should be revisited only if you see connection-related errors or the database reports it is near its connection limit.
- explanation-h05: A queue protects against traffic spikes.
- explanation-h05: A queue absorbs bursts that would otherwise overwhelm the email service.
- explanation-h05: If the email service is down often or for long periods, the queue backlog grows.
- explanation-h05: A growing backlog requires planning for storage, retry limits, and dead-letter handling.
- explanation-h05: If traffic is low, throughput is not a driver for the change either way.
- explanation-h05: Incident history or logs can show the email service's downtime frequency and duration.
- explanation-h05: Whether email delivery is meant to be synchronous or fire-and-forget should be determined.
- explanation-h05: Synchronous email delivery means the order service needs to know the delivery worked.
- explanation-h05: Fire-and-forget email delivery means the order service does not need to know the delivery worked.
- explanation-h05: If email delivery does not need to block the order flow, a queue is a reasonable default even without hard numbers.
- explanation-h05: A queue decouples the services at a contained cost.
- explanation-h05: If email delivery needs to block the order flow, a queue changes the failure semantics.
- explanation-h05: Blocking email delivery with a queue requires a way to signal delivery failure back to the order flow.
- explanation-h05: The changed failure semantics should be weighed against the reliability gain.
- explanation-h06: A microservices split often adds risk that is harder to see.
- explanation-h06: Long CI runs are likely caused by a slow or unparallelized test suite.
- explanation-h06: Long CI runs can be fixed without splitting by parallelizing tests, caching builds, and cutting flaky tests.
- explanation-h06: Risky deploys are likely caused by tight coupling between modules.
- explanation-h06: Risky deploys can be addressed by modularizing the monolith's internals first.
- explanation-h06: Manual gates are likely caused by approval steps and manual QA.
- explanation-h06: Manual gates can be addressed by automating checks and adding feature flags.
- explanation-h06: A team blocked on each other is likely caused by a shared release train and merge conflicts.
- explanation-h06: Teams blocking each other can be addressed with trunk-based development and smaller pull requests.
- explanation-h06: If the bottleneck is one of these causes, a microservices split does not address it.
- explanation-h06: Microservices earn their cost when parts of the system need independent scaling.
- explanation-h06: A team of six is one team, not several.
- explanation-h06: Staying monolithic involves enforcing module boundaries and dependency rules inside the codebase.
- explanation-h06: If module boundaries are not actually enforced, coupling creeps back.
- explanation-h06: If service boundaries do not match real ownership boundaries, the result is a distributed monolith.
- explanation-h06: The recommendation is to spend a week measuring deploy pipeline stages: build, test, review, and deploy.
- explanation-h06: If the data points to coupling and a slow test suite, those should be fixed inside the monolith first.
- explanation-h06: Microservices should be revisited only upon hitting a real scaling or team-boundary problem that a modular monolith cannot solve.
- summarization-h02: The third scheduled report started arriving again after the customer's IT team whitelisted the sending domain.
- summarization-h02: The domain whitelisting fixed delivery for one of the three reports.
- summarization-h02: If the trace shows the two failing emails as delivered, the customer should be asked to check server-side filtering or a mailbox rule beyond spam.
- summarization-h02: If the trace shows delivery failures, the failure details should be shared with the customer's IT team.
- summarization-h04: The memory contained nothing relevant to this task.
- summarization-h04: The task is a one-off summary task.
- summarization-h04: The QA breakdown is ordered by risk.
- summarization-h04: The work under review is an invoice numbering rework.
- summarization-h04: The rework introduces a breaking change to the public API.
- summarization-h04: The `invoice_number` field can now be null for draft invoices.
- summarization-h04: `invoice_number` is populated once an invoice is finalized.
- summarization-h04: The rework includes a migration that backfills a legal-entity prefix onto existing invoices.
- summarization-h04: A migration can fail partway through and has rollback behavior.
- summarization-h04: Invoice numbers are allocated at finalization rather than at creation.
- summarization-h04: Invoice numbers are sequential and unique per legal entity.
- summarization-h04: Multiple drafts in the same legal entity can be finalized concurrently.
- summarization-h04: Drafts created before the release already have numbers allocated to them.
- summarization-h04: Pre-existing drafts retain their already-allocated numbers through finalization.
- summarization-h04: The new scheme uses a per-entity number sequence.
- summarization-h04: Two different legal entities can have invoices with the same numeric suffix but different prefixes.
- summarization-h04: Entity transfer or reassignment scenarios may or may not exist in the system.
- summarization-h04: Invoice numbers are rendered on generated PDF templates.
- summarization-h04: The rework includes a search index rebuild.
- summarization-h04: Invoices can be searched by invoice number.
- summarization-h04: Invoice numbers existed in an unprefixed form before the rework.
- summarization-h04: Duplicate invoice numbers within a legal entity should be flagged immediately.
- summarization-h04: A finalized invoice missing a number should be flagged immediately.
- summarization-h05: The speaker checked memory for relevant information before summarizing.
- summarization-h05: No relevant memory was found for this task.

### plain-language

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-h01 | 27 | 19 | 0.704 | 30 | 9 |
| code-review-h02 | 23 | 15 | 0.652 | 25 | 5 |
| code-review-h03 | 25 | 20 | 0.8 | 23 | 5 |
| code-review-h04 | 2 | 0 | 0.0 | 33 | 33 |
| code-review-h05 | 44 | 0 | 0.0 | 7 | 7 |
| code-review-h06 | 38 | 0 | 0.0 | 7 | 7 |
| debugging-h01 | 10 | 8 | 0.8 | 13 | 4 |
| debugging-h02 | 11 | 9 | 0.818 | 15 | 0 |
| debugging-h03 | 13 | 11 | 0.846 | 18 | 3 |
| debugging-h04 | 11 | 9 | 0.818 | 13 | 1 |
| debugging-h05 | 1 | 1 | 1.0 | 25 | 25 |
| debugging-h06 | 19 | 0 | 0.0 | 6 | 6 |
| explanation-h01 | 31 | 23 | 0.742 | 45 | 5 |
| explanation-h02 | 24 | 12 | 0.5 | 17 | 3 |
| explanation-h03 | 28 | 24 | 0.857 | 24 | 1 |
| explanation-h04 | 25 | 18 | 0.72 | 22 | 1 |
| explanation-h05 | 11 | 8 | 0.727 | 23 | 10 |
| explanation-h06 | 18 | 13 | 0.722 | 22 | 8 |
| summarization-h01 | 16 | 15 | 0.938 | 17 | 2 |
| summarization-h02 | 18 | 13 | 0.722 | 17 | 5 |
| summarization-h03 | 15 | 14 | 0.933 | 17 | 3 |
| summarization-h04 | 7 | 0 | 0.0 | 19 | 19 |
| summarization-h05 | 16 | 14 | 0.875 | 21 | 3 |
| summarization-h06 | 14 | 14 | 1.0 | 14 | 0 |

Median fraction: 0.734 over 24 scored pairs.

Median additions: 5.0 over 24 scored pairs.

Lost facts:

- code-review-h01: The expression `share * (people - 1)` uses the rounded per-person share instead of `total`.
- code-review-h01: Using the rounded share in that expression can compound floating-point error for larger `people` counts.
- code-review-h01: With `total=100` and `people=7`, the last share comes out odd.
- code-review-h01: An example of that imprecision is a value of `33.33999999999999` instead of `33.34`.
- code-review-h01: The float equality check mostly works here because it only decides whether to apply a correction.
- code-review-h01: Using `float` for currency is the root problem in this code.
- code-review-h01: Python's `round()` uses banker's rounding, also called round-half-to-even.
- code-review-h01: Banker's rounding can surprise people who expect standard round-half-up behavior for money.
- code-review-h02: Decrementing `i` after a splice fixes the skipping bug.
- code-review-h02: The function also returns the same array it mutated.
- code-review-h02: The term "expired" often implies a `<=` comparison.
- code-review-h02: If an item lacks an `expires` property, `undefined < now` evaluates to `false`.
- code-review-h02: An item missing `expires` is silently kept rather than flagged or erroring.
- code-review-h02: The function uses `var` instead of `let`.
- code-review-h02: Using `var` is not a functional bug in this function because no closure captures `i`.
- code-review-h02: `var` is loose scoping style that makes bugs easy to introduce as a function grows.
- code-review-h03: Without closing, the file descriptor stays open indefinitely.
- code-review-h03: The unclosed file is opened inside a generator expression, whose lifetime and closure are not obvious.
- code-review-h03: `int()` tolerates surrounding whitespace.
- code-review-h03: The function signature does not document that it requires a reusable sequence such as a list or tuple rather than a one-shot iterator.
- code-review-h03: The code lacks input validation against negative counts, non-numeric types, and `None` values.
- code-review-h04: The speaker will check for relevant memory before reviewing.
- code-review-h04: A skill named auto-memory-check is being invoked.
- code-review-h05: Every call appends to the bucket before checking the limit, including calls that are denied.
- code-review-h05: A client sending high-QPS requests keeps adding entries to `_hits[key]` for the full 60-second window.
- code-review-h05: The size of the hits list is bounded by request volume, not by `limit`.
- code-review-h05: The filter performs a full O(n) rescan on every call.
- code-review-h05: The append-before-check behavior turns a burst or DoS attempt into a self-inflicted CPU and memory DoS on the limiter.
- code-review-h05: The unbounded burst growth is almost certainly not deliberate.
- code-review-h05: The sequence `setdefault` -> `append` -> rebuild-and-reassign is not atomic.
- code-review-h05: `bucket = _hits.setdefault(key, [])` gets a shared reference to the list.
- code-review-h05: `bucket.append(now)` mutates the list in place.
- code-review-h05: `_hits[key] = [t for t in bucket ...]` replaces the entry with a new list object.
- code-review-h05: If another thread appends between one thread's append and its reassignment, that append lands on the old list object and is discarded.
- code-review-h05: The race condition causes hits to be silently dropped, undercounting requests.
- code-review-h05: The undercounting lets more than `limit` requests through under load.
- code-review-h05: The race condition is a genuine bug for any multi-threaded server, such as threaded WSGI or gunicorn.
- code-review-h05: No lock is used anywhere in the code.
- code-review-h05: Keys are never removed from `_hits`, even when their bucket becomes empty.
- code-review-h05: Every distinct key that ever hits the function occupies an entry in `_hits` forever.
- code-review-h05: An attacker cycling through many fake keys can grow `_hits` without limit.
- code-review-h05: `int(time.time())` truncates timestamps to whole seconds.
- code-review-h05: Truncating to whole seconds makes the 60-second window fuzzy, ranging from about 59 to about 61 seconds.
- code-review-h05: The fixed-window imprecision is a minor issue.
- code-review-h05: The limiter is not a precise sliding window.
- code-review-h05: The code uses wall-clock time via `time.time()` instead of monotonic time.
- code-review-h05: `time.time()` can jump due to NTP correction or manual clock changes.
- code-review-h05: A backward clock jump makes `now - 60` smaller, which can make already-expired entries look valid again and stretch the effective window.
- code-review-h05: `time.monotonic()` would avoid the clock-jump problem.
- code-review-h05: Using `time.monotonic()` would require consistent use across all callers because monotonic time is not epoch-based.
- code-review-h05: `_hits` is a plain in-process dict/global.
- code-review-h05: Under multiple worker processes, each process has its own independent counter.
- code-review-h05: With multiple workers, the actual effective limit is `limit` times the worker count, not `limit`.
- code-review-h05: There is no indication anywhere that this is a single-instance-only limiter.
- code-review-h05: Rebuilding the whole list with a comprehension on every call is O(n), where n is the number of hits in the last 60 seconds.
- code-review-h05: A `collections.deque` with `popleft()` while entries are stale would be both correct and cheaper.
- code-review-h05: A deque would compose better with a fix that stops appending once over a hard cap.
- code-review-h05: The append-then-check ordering gives correct semantics: it allows exactly `limit` requests per window and blocks the (limit+1)th.
- code-review-h05: The append-then-check ordering is not an off-by-one error and looks intentional.
- code-review-h05: The code uses `limit=20` and a 60-second window.
- code-review-h05: There is no way to tell whether the 20/60 values are SLA-driven, capacity-driven, or arbitrary.
- code-review-h05: The magic numbers with no rationale is a problem the user previously flagged.
- code-review-h05: The recommendation is to document the limit values or move them to config before trusting them in production.
- code-review-h05: As written, nobody could tell whether 20 requests per 60 seconds is conservative or dangerously loose.
- code-review-h05: The concurrency race and the unbounded burst growth are the two issues to fix before production traffic.
- code-review-h05: The concurrency race and unbounded burst growth are real correctness and availability issues, not style nits.
- code-review-h05: The multi-process issue is the one most likely to bite silently in deployment even though the code looks correct in isolation.
- code-review-h06: The code calls config.update(json.load(f)) to merge values from a JSON file into the config.
- code-review-h06: Values loaded from the JSON file can have real types such as int.
- code-review-h06: Values read from os.environ are always strings.
- code-review-h06: Environment variable overrides silently change the types of config values.
- code-review-h06: The timeout value could end up as the int 30 or the string "45" depending on which layer set it last.
- code-review-h06: Callers performing arithmetic on timeout, such as sleep(timeout) or timeout + margin, will work in some deployments and crash in others.
- code-review-h06: Setting DEBUG=false in the environment makes config["debug"] the string "false".
- code-review-h06: A non-empty string such as "false" is truthy in Python.
- code-review-h06: The check if config["debug"]: will evaluate as true even when the operator set DEBUG=false.
- code-review-h06: The debug boolean-string bug can appear to work in testing and silently misbehave in production.
- code-review-h06: The loop performs config[key] = os.environ[key.upper()] for every key in config.
- code-review-h06: The override loop includes keys that were added by the JSON file.
- code-review-h06: The override loop applies even when the existing value is a dict or a list.
- code-review-h06: If a config file contains a nested value like {"database": {...}}, setting DATABASE in the environment replaces the whole nested structure with a single string.
- code-review-h06: The env override code has no type-awareness.
- code-review-h06: The code uses except Exception: pass around the config file load.
- code-review-h06: The bare except swallows FileNotFoundError, which was probably the intended case.
- code-review-h06: The bare except also swallows json.JSONDecodeError, PermissionError, and UnicodeDecodeError.
- code-review-h06: A malformed config file is a real operational problem.
- code-review-h06: A deploy with a broken config file will silently run on defaults with no log output.
- code-review-h06: The code has no logging anywhere.
- code-review-h06: Silently swallowing a parse error in an existing file is hard to justify and warrants at least a log line.
- code-review-h06: The precedence order is defaults, then file, then environment.
- code-review-h06: Environment overriding file overriding defaults is a standard convention.
- code-review-h06: The precedence order is likely deliberate and fine to keep, but needs documenting.
- code-review-h06: The default config path is the relative path "config.json".
- code-review-h06: Resolution of the relative default path depends on the caller's current working directory.
- code-review-h06: Whether the relative path is deliberate or accidental cannot be determined without seeing the calling services.
- code-review-h06: There is no schema validation on the JSON file, so arbitrary keys merge in unchecked.
- code-review-h06: There is no casting of env values against the type of the existing default.
- code-review-h06: Casting env values to the type of the existing default would fix both the type-change bug and the boolean-string bug.
- code-review-h06: The function has no way to signal to the caller that config loading failed.
- code-review-h06: Everything degrades silently to defaults, which may not match what depending services expect on startup.
- code-review-h06: The fallback-to-defaults-on-missing-file behavior appears intentional and reasonable.
- code-review-h06: The string-typing of env overrides appears accidental rather than intended.
- code-review-h06: The blanket exception swallowing that also hides malformed JSON appears accidental rather than intended.
- code-review-h06: The string-typing and blanket exception swallowing are the issues to fix first, especially the boolean footgun.
- code-review-h06: The boolean footgun can cause a debug flag to do the opposite of what someone typed.
- debugging-h01: An alternative fix is a factory function that takes `name` and returns a lambda.
- debugging-h01: Both fixes work because they create a new variable scoped to each iteration or call.
- debugging-h02: If filenames always follow the exact snap-<N>.db pattern, the key can be simplified to int(s.split('-')[1].split('.')[0]).
- debugging-h02: int(s.split('-')[1].split('.')[0]) avoids using a regular expression.
- debugging-h03: Floating-point numbers in JavaScript use IEEE 754 double precision.
- debugging-h03: decimal.js is a decimal library.
- debugging-h04: When input strings sometimes include an offset and sometimes do not, validating or normalizing at the boundary is preferable to guessing the zone.
- debugging-h04: Boundary handling options include rejecting naive timestamps or requiring input to always include an offset.
- debugging-h06: Latency did not drop when the deploy was rolled back.
- debugging-h06: Latency stayed elevated for about another hour after the rollback.
- debugging-h06: Latency recovered on its own without further intervention.
- debugging-h06: The latency pattern rules out a bad code path as the sole cause.
- debugging-h06: The latency pattern points to a stateful side effect that outlived the deploy.
- debugging-h06: The incident was isolated to a single region.
- debugging-h06: A rollback deploys new code but does not necessarily recycle running processes or pods.
- debugging-h06: A connection, thread, or memory leak on running instances clears only when instances restart or connections time out.
- debugging-h06: A region-specific DB replica, cache cluster, or search index can become overloaded and need time to drain a backlog or catch up on replication lag, independent of application code.
- debugging-h06: A deploy can trigger a scale-down or instance churn in a region.
- debugging-h06: A roughly one-hour capacity stabilization time matches typical ASG cooldown and stabilization windows.
- debugging-h06: Cache poisoning or a cold cache self-heals as TTLs expire or entries get overwritten.
- debugging-h06: Aggressive retries and open circuit breakers can take time to settle even after the triggering code is removed.
- debugging-h06: Regional infrastructure problems such as noisy neighbors, network path issues, or partial outages can correlate with a deploy by timing alone.
- debugging-h06: Feature flags, environment variables, and instance types can differ between regions.
- debugging-h06: Region-specific configuration differences can cause only one region to exercise a bad code path.
- debugging-h06: The user's dashboards retain only 24 hours of data.
- debugging-h06: The incident window is no longer viewable in the dashboards.
- debugging-h06: Raw logs and traces may be retained longer than dashboard data in log storage such as S3, Loki, or Datadog, or in APM trace sampling.
- explanation-h01: Not retrying a failed request risks leaving the operation undone.
- explanation-h01: Retrying blindly risks performing the operation twice, such as charging a card twice, creating duplicate orders, or sending two emails.
- explanation-h01: Idempotency is treated as a prerequisite for automatic retry logic in HTTP clients, load balancers, and API gateways.
- explanation-h01: Idempotent is not the same as safe.
- explanation-h01: Safe means the method has no side effects at all.
- explanation-h01: Idempotency keys usually expire after some window, such as 24 hours, so storage does not grow forever.
- explanation-h01: Servers typically need to handle a duplicate request arriving while the first request is still processing, by returning a conflict/try-later response or blocking until done.
- explanation-h01: The idempotency key pattern is common in payment APIs such as Stripe and PayPal because double-charging is the worst-case failure mode.
- explanation-h02: B-trees typically have high fan-out, so the tree is shallow.
- explanation-h02: A B-tree is typically 3-4 levels deep even for millions of rows.
- explanation-h02: Because index keys are sorted, a B-tree index supports range scans and ordered retrieval without a separate sort step.
- explanation-h02: B-tree indexes help range queries such as filtering order_date BETWEEN two dates.
- explanation-h02: B-tree indexes help queries that sort by the indexed column.
- explanation-h02: Node splits can cascade up the tree and require rebalancing.
- explanation-h02: Deletes can trigger node merges and rebalancing.
- explanation-h02: Each index causes extra disk I/O and WAL/log writes beyond the table's own row change.
- explanation-h02: An insert gets no query-side benefit from indexes because an insert is not a lookup.
- explanation-h02: In that case you pay the index's write cost without getting the read benefit.
- explanation-h02: You should index columns that are frequently filtered, sorted, or joined on.
- explanation-h02: You should avoid over-indexing tables with heavy write traffic.
- explanation-h03: Offset pagination is stateless and easy to reason about.
- explanation-h03: Cursor pagination requires a stable sort key and encoding/decoding of the cursor.
- explanation-h03: Offset pagination fits cases where exact page counts matter more than perfect consistency.
- explanation-h03: Offset pagination should be chosen only when arbitrary page jumping is specifically needed and its staleness and performance issues are acceptable.
- explanation-h04: If the connection is encrypted, establishing it requires TLS negotiation, which adds several more round-trips and cryptographic operations.
- explanation-h04: Establishing a database connection requires session setup, in which the database allocates memory, spawns a backend process or thread, and initializes session state.
- explanation-h04: Postgres forks a process per connection.
- explanation-h04: A request that could be served in 5ms might take 50-100ms because of connection setup for a single query.
- explanation-h04: Postgres defaults to a limit of 100 concurrent connections.
- explanation-h04: When all pooled connections are busy, new requests wait for one to free up rather than opening additional connections.
- explanation-h04: Making requests wait instead of opening extra connections protects the database from being overwhelmed.
- explanation-h05: Adding a queue introduces new complexity: retries, dead-letter handling, and idempotency.
- explanation-h05: Queues typically deliver messages at-least-once.
- explanation-h05: At-least-once delivery is why idempotency is needed.
- explanation-h06: Splitting is likely to make deploys slower and riskier in the short term unless the actual bottleneck is something microservices specifically fix.
- explanation-h06: Microservices can help when the problem is a slow test suite, unclear ownership causing merge conflicts, or a monolith where any change requires a full redeploy of unrelated code.
- explanation-h06: Premature service boundaries are expensive to redraw later.
- explanation-h06: The last 10-20 incidents should be reviewed to determine whether they are coupling-related or process-related.
- explanation-h06: For a six-person team, the failure mode is very likely process or tooling rather than something a service split fixes.
- summarization-h01: All other v2 endpoint calls must be migrated to their /v3/ equivalents before November 30.
- summarization-h02: Sender reputation was ruled out as a cause.
- summarization-h02: Once the provider responds, their trace should be correlated against internal delivery logs for the 2 missing report IDs.
- summarization-h02: No action is needed from the customer right now.
- summarization-h02: The customer should be followed up with once RLY-4812 resolves.
- summarization-h02: The customer should be contacted proactively if the provider has not responded within the 2-business-day window.
- summarization-h03: The third check applies if queue depth still grows while workers are alive.
- summarization-h04: A tool named "bash" is being invoked.
- summarization-h04: The tool invocation includes a "command" parameter.
- summarization-h04: The command runs `cat` on the file /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-9pi3l86u/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-dgijk4db/memory/MEMORY.md
- summarization-h04: The command redirects standard error to /dev/null with `2>/dev/null`.
- summarization-h04: The command echoes "NONE" if the `cat` command fails.
- summarization-h04: The tool invocation includes a "description" parameter with the value "Check memory index".
- summarization-h04: The parameters are given in JSON format.
- summarization-h05: March's storage data was not broken down by type.
- summarization-h05: A large customer campaign is expected next quarter.

Added facts (styled only):

- code-review-h01: Because of float imprecision, `round()` and the `!=` comparison can behave unpredictably.
- code-review-h01: A fairer approach spreads the leftover cents across several people, for example by adding one cent to the first N people until the total matches.
- code-review-h01: The suggested fix distributes the remainder one cent at a time to the first few people rather than to the last person.
- code-review-h01: The suggested implementation raises ValueError with the message "people must be a positive integer" when `people <= 0`.
- code-review-h01: The suggested implementation raises ValueError with the message "total must not be negative" when `total < 0`.
- code-review-h01: The suggested implementation computes `total_cents` as `round(total * 100)`.
- code-review-h01: The suggested implementation uses `divmod(total_cents, people)` to get a base amount and a remainder.
- code-review-h01: The suggested implementation adds one cent to each of the first `remainder` entries.
- code-review-h01: The suggested implementation returns each amount divided by 100.
- code-review-h02: `removeExpired` does not check that `items` is an array.
- code-review-h02: If `null` or `undefined` is passed as `items`, the function throws rather than failing clearly.
- code-review-h02: If `now` is `undefined`, every comparison evaluates to `false`.
- code-review-h02: With `now` as `undefined`, nothing is removed and no error is raised.
- code-review-h02: A guard clause would make the `undefined` `now` failure visible instead of silent.
- code-review-h03: If an error occurs partway through, the file handle stays open until the garbage collector cleans it up.
- code-review-h03: If the file does not exist, `open()` will raise `FileNotFoundError`.
- code-review-h03: Three passes over a plain list is wasteful.
- code-review-h03: Total, count, and maximum can be computed in a single pass.
- code-review-h03: The suggested fix skips blank lines.
- code-review-h04: The statement `logging.info("login attempt: %s", request)` writes the full request to the log file.
- code-review-h04: The logged request includes the plain-text password.
- code-review-h04: Anyone who can read the logs can see user passwords.
- code-review-h04: The code compares passwords with `user["password"] == request["password"]`.
- code-review-h04: Comparing passwords directly means they are stored in plain text rather than hashed.
- code-review-h04: If a user database of plain-text passwords leaks, every password is exposed.
- code-review-h04: bcrypt and argon2 are proper password-hashing libraries.
- code-review-h04: Using `==` to compare passwords can leak timing information.
- code-review-h04: Timing leaks can help an attacker guess a password one character at a time.
- code-review-h04: `hmac.compare_digest` is a constant-time comparison function.
- code-review-h04: The function does not limit failed login attempts.
- code-review-h04: Without a limit on failed login attempts, unlimited password guessing (brute force) is possible.
- code-review-h04: Python removes `assert` statements when code runs with the `-O` optimize flag.
- code-review-h04: With `assert` removed, requests lacking a username or password would skip the check and later crash with a `KeyError`.
- code-review-h04: Input should be validated with a normal `if` statement that raises an explicit error instead of `assert`.
- code-review-h04: If `request` is `None` or not a dictionary, the check `"username" in request` raises a `TypeError`.
- code-review-h04: The code assumes `request["username"]` and `request["password"]` are strings.
- code-review-h04: Unexpected types such as `None` or a list could cause confusing errors later in the code.
- code-review-h04: The response text is "bad username or password".
- code-review-h04: A generic error message is good practice because it avoids telling an attacker which part was wrong.
- code-review-h04: The log line reveals the username and password, undoing the protection of the generic error message.
- code-review-h04: The function has no account lockout or anomaly detection.
- code-review-h04: Most production systems track failed login attempts per user or per IP address.
- code-review-h04: The function has no docstring and no type hints.
- code-review-h04: Adding a docstring and type hints such as `def login(request: dict, users: dict) -> dict:` would clarify expected input and output shapes.
- code-review-h04: The proposed safer version imports `hmac` and `logging`.
- code-review-h04: The proposed version returns `{"ok": False, "error": "missing username or password"}` when username or password is absent.
- code-review-h04: The proposed version logs only the username.
- code-review-h04: The proposed version uses `users.get(request["username"])` to look up the user.
- code-review-h04: The proposed version compares `user["password_hash"]` with `hash_password(request["password"])` using `hmac.compare_digest`.
- code-review-h04: The proposed version returns `{"ok": True, "token": user["token"]}` on success.
- code-review-h04: The key changes are logging only the username, using constant-time comparison, and comparing password hashes instead of plain text.
- code-review-h04: The proposed version assumes `hash_password` and the stored `password_hash` values use a proper algorithm such as bcrypt.
- code-review-h05: The speaker intends to check their memory for relevant context on the project before proceeding.
- code-review-h05: A tool named 'bash' is invoked.
- code-review-h05: The bash tool's input includes a 'command' field and a 'description' field.
- code-review-h05: The command runs 'cat' on the file /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-9pi3l86u/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-dgijk4db/memory/MEMORY.md
- code-review-h05: The command redirects standard error to /dev/null with '2>/dev/null'.
- code-review-h05: The command echoes 'NONE' if the cat command fails.
- code-review-h05: The tool call's description is 'Check memory index'.
- code-review-h06: The speaker intends to check their memory for relevant context before reviewing.
- code-review-h06: A bash tool is invoked.
- code-review-h06: The bash command runs `cat` on a MEMORY.md file.
- code-review-h06: The MEMORY.md file path is /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-9pi3l86u/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-dgijk4db/memory/MEMORY.md
- code-review-h06: The command redirects stderr to /dev/null.
- code-review-h06: The command echoes "no memory file" if the cat command fails.
- code-review-h06: The tool call's description field is "Check memory index".
- debugging-h01: `functools.partial` is an alternative fix.
- debugging-h01: `functools.partial` binds the argument immediately.
- debugging-h01: `partial(lambda n: print("handling " + n), name)` is a valid way to construct the handlers.
- debugging-h01: Both the default-argument fix and the `functools.partial` fix capture the value of `name` at creation time instead of letting the lambda look it up later.
- debugging-h03: `reduce((sum, p) => sum + p, 0)` sums the values of an array.
- debugging-h03: Cents are converted to dollars by dividing by 100.
- debugging-h03: Conversion from cents to dollars should happen only when displaying the value to the user.
- debugging-h04: An offset-aware datetime carries UTC time zone information.
- debugging-h05: The webhook sender times out at 30 seconds and then retries.
- debugging-h05: A receiver that responds slower than the 30-second timeout can process a request successfully and still cause the sender to retry, producing a duplicate.
- debugging-h05: A slow (rather than down) receiver is the most common cause of silent webhook duplicates.
- debugging-h05: A duplicate can occur when the receiver sends a 2xx response but the connection drops before the sender reads it.
- debugging-h05: Network blips, load balancer restarts, and TLS renegotiation issues can cause a response to be lost after processing.
- debugging-h05: The sender retries whenever it does not receive a clean response.
- debugging-h05: Transient 502, 503, or 504 responses from a load balancer can trigger a retry.
- debugging-h05: An app crash on one instance or a rate limiter can produce non-2xx responses that trigger a retry.
- debugging-h05: A non-2xx condition lasting only a few hundred milliseconds is enough to trigger a retry under the sender's stated retry policy.
- debugging-h05: If the receiver endpoint sits behind a load balancer with multiple instances, a retry can land on a different instance than the original request.
- debugging-h05: Two backend instances receiving the same event can process it independently, creating a duplicate.
- debugging-h05: If the webhook sender reads from an at-least-once queue, two send attempts can occur without any timeout or error.
- debugging-h05: The observed duplicate rate is consistently about 1 in 200.
- debugging-h05: A consistent duplicate rate indicates a systematic cause rather than a rare random network fluke.
- debugging-h05: Possible systematic causes include a fixed slow code path, a percentile of requests hitting a cache miss, or steady baseline flakiness in the receiver's infrastructure.
- debugging-h05: Sender logs for the past window are not available.
- debugging-h05: Two deliveries carrying the same delivery or event ID confirm that a retry occurred.
- debugging-h05: Two deliveries with different IDs indicate an upstream bug creating duplicate events rather than a delivery retry.
- debugging-h05: Useful receiver-side logs include timestamp received, time to respond, and response code sent.
- debugging-h05: A latency slice near 1-in-200 at or above 30 seconds would support the timeout theory.
- debugging-h05: Useful sender-side logging fields are request ID, response code, response latency, and retry flag.
- debugging-h05: Load balancer, proxy, or CDN logs can reveal connection resets or multiple backend instances handling one logical request.
- debugging-h05: Many third-party webhook providers retain a delivery history or dashboard for an endpoint.
- debugging-h05: A provider's delivery history can show response codes and timing for a window where your own logs were not retained.
- debugging-h05: If duplicate rate correlates with receiver response time across multiple customers, that strongly confirms the slow-receiver cause.
- debugging-h06: The Read tool was invoked.
- debugging-h06: The Read tool call specified a file_path parameter.
- debugging-h06: The file path read is /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-9pi3l86u/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-dgijk4db/memory/MEMORY.md
- debugging-h06: The file being read is named MEMORY.md.
- debugging-h06: The MEMORY.md file is located in a directory named 'memory'.
- debugging-h06: The memory directory is under a project directory path beginning with 'style-config-pairs-9pi3l86u'.
- explanation-h01: OPTIONS only asks about supported actions and makes no change.
- explanation-h01: There are two main techniques for making POST safe to retry.
- explanation-h01: An operation can sometimes be designed so that repeating it naturally has no extra effect, without needing a key.
- explanation-h01: 'Set the counter to this exact value' can be used instead of 'increment the counter'.
- explanation-h01: Using a client-supplied resource ID with PUT (create or replace the order with a given ID) is an alternative to POST.
- explanation-h02: A B-tree index is analogous to the index at the back of a book, which points to the right page instead of requiring reading every page.
- explanation-h02: On a large table, using an index can turn a multi-second scan into a query that finishes in milliseconds.
- explanation-h02: An index would help the UPPER(customer_name) query only if it were built on UPPER(customer_name) directly, or if the same transformation were applied on both sides.
- explanation-h03: In cursor pagination, the server returns a cursor pointing to the next position.
- explanation-h04: Using a pool makes queries run faster.
- explanation-h05: A queue, or a consumer reading from it, can retry failed messages instead of the order service handling that logic.
- explanation-h05: A queue provides retries without extra code in the order service.
- explanation-h05: A queue smooths traffic by absorbing bursts when order volume spikes, instead of overwhelming the email service.
- explanation-h05: If the email service is down often, the reliability gain from a queue is large.
- explanation-h05: If order volume is low, a simple retry-with-backoff in the order service might solve the same problem with far less complexity.
- explanation-h05: If order volume is high or bursty, a queue's buffering matters more.
- explanation-h05: Queue failure modes include growing backlogs, message loss if not configured for durability, and added latency before an email goes out.
- explanation-h05: Someone must monitor the queue, size it, and handle dead-letter messages that fail repeatedly.
- explanation-h05: Before deciding, one should determine how the business currently handles failed emails.
- explanation-h05: If outages or volume are meaningful, the queue is likely worth the added complexity.
- explanation-h06: If most deploy time is spent in a slow test suite or a manual approval step, splitting the codebase will not fix it.
- explanation-h06: Tangled code in which one team's change breaks another team's feature is a coupling problem.
- explanation-h06: Splitting into services helps with coupling only if the split lines up with the team's real boundaries.
- explanation-h06: A team of six engineers likely cannot run more than two or three services well.
- explanation-h06: If services share the same database, coupling has not been removed, only hidden behind network calls.
- explanation-h06: If the test suite is the bottleneck, it will keep growing until it is fixed directly.
- explanation-h06: Coupled code keeps causing surprise breakages even with careful review.
- explanation-h06: Deploy risk stays high without a fast, safe way to roll back a single feature.
- summarization-h01: No code changes beyond the endpoint URL are needed for the export endpoint.
- summarization-h01: Support needs to review legacy quarterly billing plan accounts before those users switch to v3.
- summarization-h02: The third affected report began arriving after the customer's IT team whitelisted the sending domain.
- summarization-h02: The planned follow-up after the trace returns is to check whether the two undelivered reports share an attribute the working report lacks.
- summarization-h02: A different recipient domain and a larger attachment size are examples of attributes the two stuck reports might share.
- summarization-h02: Nothing from this task is worth saving to memory.
- summarization-h02: The state of this ticket belongs in the ticket system rather than in memory.
- summarization-h03: If fewer than 4 workers are running, proceed to step 3.
- summarization-h03: Step 3 is to restart the worker pool.
- summarization-h03: Step 4 is to check database latency.
- summarization-h04: Invoices previously received an invoice number when they were created.
- summarization-h04: Invoices now receive a number only when they are finalized.
- summarization-h04: Draft invoices no longer consume invoice numbers.
- summarization-h04: Existing drafts keep the invoice numbers they already have.
- summarization-h04: Invoice numbers previously came from a single global sequence.
- summarization-h04: Each legal entity now has its own invoice numbering sequence.
- summarization-h04: A one-time migration adds the entity prefix to all existing invoice numbers.
- summarization-h04: The PDF template now displays the new prefixed invoice number.
- summarization-h04: The search index was rebuilt to match the new invoice numbers.
- summarization-h04: The public API's `invoice_number` field keeps the same shape.
- summarization-h04: The public API's `invoice_number` field can now be null for draft invoices.
- summarization-h04: The possibility of a null `invoice_number` is a breaking change for API consumers.
- summarization-h04: Migration correctness is the highest-risk area to test.
- summarization-h04: The migration is hard to undo.
- summarization-h04: Draft invoices return null for `invoice_number` through the public API.
- summarization-h04: Finalized invoices return a non-null `invoice_number` through the public API.
- summarization-h04: Existing drafts created before this release are not renumbered.
- summarization-h04: The recommended test priority order is: migration correctness, API handling of null, number allocation timing, per-entity sequence behavior, PDF template display, then search index accuracy.
- summarization-h04: The migration should be tested on a full production-like data set rather than only a small sample.
- summarization-h05: The memory directory was checked for context.
- summarization-h05: Nothing in the memory directory applies to this summary.
- summarization-h05: The summary is based only on the memo.

### technical-simplified

| Pair | Facts | Survived | Fraction | Styled facts | Additions |
|---|---|---|---|---|---|
| code-review-h01 | 27 | 14 | 0.519 | 17 | 4 |
| code-review-h02 | 23 | 10 | 0.435 | 20 | 2 |
| code-review-h03 | 25 | 20 | 0.8 | 20 | 3 |
| code-review-h04 | 2 | 1 | 0.5 | 27 | 26 |
| code-review-h05 | 44 | 21 | 0.477 | 33 | 11 |
| debugging-h01 | 10 | 8 | 0.8 | 10 | 0 |
| debugging-h02 | 11 | 8 | 0.727 | 13 | 2 |
| debugging-h03 | 13 | 11 | 0.846 | 9 | 0 |
| debugging-h04 | 11 | 9 | 0.818 | 11 | 2 |
| debugging-h05 | 1 | 1 | 1.0 | 29 | 29 |
| debugging-h06 | 19 | 16 | 0.842 | 30 | 12 |
| explanation-h01 | 31 | 22 | 0.71 | 32 | 1 |
| explanation-h02 | 24 | 10 | 0.417 | 16 | 2 |
| explanation-h03 | 28 | 24 | 0.857 | 20 | 0 |
| explanation-h04 | 25 | 14 | 0.56 | 26 | 6 |
| explanation-h05 | 11 | 6 | 0.545 | 22 | 10 |
| explanation-h06 | 18 | 8 | 0.444 | 26 | 9 |
| summarization-h01 | 16 | 14 | 0.875 | 14 | 0 |
| summarization-h02 | 18 | 14 | 0.778 | 19 | 4 |
| summarization-h04 | 7 | 0 | 0.0 | 20 | 20 |
| summarization-h05 | 16 | 0 | 0.0 | 2 | 2 |

Median fraction: 0.71 over 21 scored pairs.

Median additions: 3 over 21 scored pairs.

Lost facts:

- code-review-h01: Using the rounded share in that expression can compound floating-point error for larger `people` counts.
- code-review-h01: The last person's amount may drift by more than a cent instead of the intended ±0.01 correction.
- code-review-h01: With `total=100` and `people=7`, the last share comes out odd.
- code-review-h01: The corrected `amounts[-1]` is not re-rounded.
- code-review-h01: An example of that imprecision is a value of `33.33999999999999` instead of `33.34`.
- code-review-h01: The float equality check mostly works here because it only decides whether to apply a correction.
- code-review-h01: Passing `people` as a float such as `2.5` makes `[share] * people` raise a `TypeError`.
- code-review-h01: A list cannot be multiplied by a non-integer.
- code-review-h01: Using `float` for currency is the root problem in this code.
- code-review-h01: Currency should be handled with `Decimal` (using `ROUND_HALF_UP` or similar) or with integer cents.
- code-review-h01: Python's `round()` uses banker's rounding, also called round-half-to-even.
- code-review-h01: Banker's rounding can surprise people who expect standard round-half-up behavior for money.
- code-review-h01: If the discrepancy exceeds one cent, the last person's share becomes visibly unfair rather than off by just a cent.
- code-review-h02: For the input `[{expires:1}, {expires:1}, {expires:10}]` with `now=5`, only the first expired item is removed.
- code-review-h02: In that example, the second expired item is skipped because it shifted into the just-checked index.
- code-review-h02: Iterating backwards with `for (let i = items.length - 1; i >= 0; i--)` fixes the skipping bug.
- code-review-h02: Decrementing `i` after a splice fixes the skipping bug.
- code-review-h02: Avoiding splice-in-loop entirely and using `filter` fixes the skipping bug.
- code-review-h02: A `filter` or single-pass compaction is both correct and O(n).
- code-review-h02: With the condition `expires < now`, items expiring exactly at `now` are kept rather than removed.
- code-review-h02: The term "expired" often implies a `<=` comparison.
- code-review-h02: If an item lacks an `expires` property, `undefined < now` evaluates to `false`.
- code-review-h02: An item missing `expires` is silently kept rather than flagged or erroring.
- code-review-h02: Using `var` is not a functional bug in this function because no closure captures `i`.
- code-review-h02: The suggested rewrite is `function removeExpired(items, now) { return items.filter(item => item.expires >= now); }`.
- code-review-h02: The suggested rewrite fixes the correctness and performance issues and avoids mutating the caller's array.
- code-review-h03: Without closing, the file descriptor stays open indefinitely.
- code-review-h03: The unclosed file is opened inside a generator expression, whose lifetime and closure are not obvious.
- code-review-h03: `int()` tolerates surrounding whitespace.
- code-review-h03: The function signature does not document that it requires a reusable sequence such as a list or tuple rather than a one-shot iterator.
- code-review-h03: The code lacks input validation against negative counts, non-numeric types, and `None` values.
- code-review-h04: A skill named auto-memory-check is being invoked.
- code-review-h05: A client sending high-QPS requests keeps adding entries to `_hits[key]` for the full 60-second window.
- code-review-h05: The size of the hits list is bounded by request volume, not by `limit`.
- code-review-h05: The filter performs a full O(n) rescan on every call.
- code-review-h05: The append-before-check behavior turns a burst or DoS attempt into a self-inflicted CPU and memory DoS on the limiter.
- code-review-h05: The unbounded burst growth is almost certainly not deliberate.
- code-review-h05: `bucket = _hits.setdefault(key, [])` gets a shared reference to the list.
- code-review-h05: `bucket.append(now)` mutates the list in place.
- code-review-h05: `_hits[key] = [t for t in bucket ...]` replaces the entry with a new list object.
- code-review-h05: If another thread appends between one thread's append and its reassignment, that append lands on the old list object and is discarded.
- code-review-h05: Truncating to whole seconds makes the 60-second window fuzzy, ranging from about 59 to about 61 seconds.
- code-review-h05: The fixed-window imprecision is a minor issue.
- code-review-h05: `time.time()` can jump due to NTP correction or manual clock changes.
- code-review-h05: `time.monotonic()` would avoid the clock-jump problem.
- code-review-h05: Using `time.monotonic()` would require consistent use across all callers because monotonic time is not epoch-based.
- code-review-h05: There is no indication anywhere that this is a single-instance-only limiter.
- code-review-h05: Rebuilding the whole list with a comprehension on every call is O(n), where n is the number of hits in the last 60 seconds.
- code-review-h05: A `collections.deque` with `popleft()` while entries are stale would be both correct and cheaper.
- code-review-h05: A deque would compose better with a fix that stops appending once over a hard cap.
- code-review-h05: The append-then-check ordering gives correct semantics: it allows exactly `limit` requests per window and blocks the (limit+1)th.
- code-review-h05: The magic numbers with no rationale is a problem the user previously flagged.
- code-review-h05: The concurrency race and the unbounded burst growth are the two issues to fix before production traffic.
- code-review-h05: The concurrency race and unbounded burst growth are real correctness and availability issues, not style nits.
- code-review-h05: The multi-process issue is the one most likely to bite silently in deployment even though the code looks correct in isolation.
- debugging-h01: An alternative fix is a factory function that takes `name` and returns a lambda.
- debugging-h01: Both fixes work because they create a new variable scoped to each iteration or call.
- debugging-h02: Lexicographic comparison stops at the first differing character and does not consider the rest of the number.
- debugging-h02: If filenames always follow the exact snap-<N>.db pattern, the key can be simplified to int(s.split('-')[1].split('.')[0]).
- debugging-h02: int(s.split('-')[1].split('.')[0]) avoids using a regular expression.
- debugging-h03: IEEE 754 double precision cannot represent most decimal fractions exactly.
- debugging-h03: decimal.js is a decimal library.
- debugging-h04: When input strings sometimes include an offset and sometimes do not, validating or normalizing at the boundary is preferable to guessing the zone.
- debugging-h04: Boundary handling options include rejecting naive timestamps or requiring input to always include an offset.
- debugging-h06: A rollback deploys new code but does not necessarily recycle running processes or pods.
- debugging-h06: A roughly one-hour capacity stabilization time matches typical ASG cooldown and stabilization windows.
- debugging-h06: Aggressive retries and open circuit breakers can take time to settle even after the triggering code is removed.
- explanation-h01: Not retrying a failed request risks leaving the operation undone.
- explanation-h01: Idempotency is treated as a prerequisite for automatic retry logic in HTTP clients, load balancers, and API gateways.
- explanation-h01: Idempotent is not the same as safe.
- explanation-h01: Safe means the method has no side effects at all.
- explanation-h01: GET and HEAD are safe methods.
- explanation-h01: The client generates a unique idempotency key, usually a UUID, for the logical operation once before the first attempt.
- explanation-h01: Idempotency keys usually expire after some window, such as 24 hours, so storage does not grow forever.
- explanation-h01: Servers typically need to handle a duplicate request arriving while the first request is still processing, by returning a conflict/try-later response or blocking until done.
- explanation-h01: The idempotency key pattern is common in payment APIs such as Stripe and PayPal because double-charging is the worst-case failure mode.
- explanation-h02: B-trees typically have high fan-out, so the tree is shallow.
- explanation-h02: A B-tree is typically 3-4 levels deep even for millions of rows.
- explanation-h02: Scanning every row in a table is O(n).
- explanation-h02: Using a B-tree index, the database walks the tree from root to leaf making O(log n) comparisons to locate matching rows.
- explanation-h02: Because index keys are sorted, a B-tree index supports range scans and ordered retrieval without a separate sort step.
- explanation-h02: B-tree indexes help range queries such as filtering order_date BETWEEN two dates.
- explanation-h02: B-tree indexes help queries that sort by the indexed column.
- explanation-h02: If a leaf node is full it must split.
- explanation-h02: Node splits can cascade up the tree and require rebalancing.
- explanation-h02: Deletes can trigger node merges and rebalancing.
- explanation-h02: Each index causes extra disk I/O and WAL/log writes beyond the table's own row change.
- explanation-h02: An insert gets no query-side benefit from indexes because an insert is not a lookup.
- explanation-h02: You should index columns that are frequently filtered, sorted, or joined on.
- explanation-h02: You should avoid over-indexing tables with heavy write traffic.
- explanation-h03: Offset pagination is simple to implement using LIMIT/OFFSET in SQL.
- explanation-h03: Offset pagination is stateless and easy to reason about.
- explanation-h03: Cursor pagination requires slightly more implementation work than offset pagination.
- explanation-h03: Cursor pagination requires a stable sort key and encoding/decoding of the cursor.
- explanation-h04: If the connection is encrypted, establishing it requires TLS negotiation, which adds several more round-trips and cryptographic operations.
- explanation-h04: Postgres forks a process per connection.
- explanation-h04: A request that could be served in 5ms might take 50-100ms because of connection setup for a single query.
- explanation-h04: Postgres defaults to a limit of 100 concurrent connections.
- explanation-h04: Each open database connection consumes real memory and CPU on the server even when idle.
- explanation-h04: A connection pool opens a set of connections at startup, either up front or lazily as needed, and keeps them alive.
- explanation-h04: Most web frameworks and database drivers include connection pooling built in or available as a one-line config.
- explanation-h04: Developers usually do not need to hand-roll a connection pool.
- explanation-h04: When all pooled connections are busy, new requests wait for one to free up rather than opening additional connections.
- explanation-h04: Making requests wait instead of opening extra connections protects the database from being overwhelmed.
- explanation-h04: Requests queuing or timing out under load is the signal that it is time to look at pool size.
- explanation-h05: Adding a queue introduces new complexity: retries, dead-letter handling, and idempotency.
- explanation-h05: Queues typically deliver messages at-least-once.
- explanation-h05: At-least-once delivery is why idempotency is needed.
- explanation-h05: If email service outages are rare and brief, a simple retry-with-backoff on the existing HTTP call could capture most of the reliability gain.
- explanation-h05: Running a queue carries operational overhead that retry-with-backoff avoids.
- explanation-h06: Microservices can help when the problem is a slow test suite, unclear ownership causing merge conflicts, or a monolith where any change requires a full redeploy of unrelated code.
- explanation-h06: Microservices help in those cases by letting teams deploy independently.
- explanation-h06: Staying monolithic means deploys stay coupled and the blast radius stays large.
- explanation-h06: After splitting, a single logical change can require coordinated deploys across multiple repositories.
- explanation-h06: After splitting, debugging becomes cross-service tracing instead of reading a stack trace.
- explanation-h06: Premature service boundaries are expensive to redraw later.
- explanation-h06: The deploy pipeline should be instrumented for build time, test time, review-to-merge time, and deploy-to-verify time before deciding.
- explanation-h06: The last 10-20 incidents should be reviewed to determine whether they are coupling-related or process-related.
- explanation-h06: A few days of pipeline and incident data will reveal which failure mode the team actually has.
- explanation-h06: For a six-person team, the failure mode is very likely process or tooling rather than something a service split fixes.
- summarization-h01: On June 1, Reporting API v3 becomes available at the /v3/ path.
- summarization-h01: All other v2 endpoint calls must be migrated to their /v3/ equivalents before November 30.
- summarization-h02: Sender reputation was ruled out as a cause.
- summarization-h02: No action is needed from the customer right now.
- summarization-h02: The customer should be followed up with once RLY-4812 resolves.
- summarization-h02: The customer should be contacted proactively if the provider has not responded within the 2-business-day window.
- summarization-h04: A tool named "bash" is being invoked.
- summarization-h04: The tool invocation includes a "command" parameter.
- summarization-h04: The command runs `cat` on the file /var/folders/tt/jh9lk8gs6_sfn5fhz4rp7pch0000gn/T/style-config-pairs-9pi3l86u/projects/-private-var-folders-tt-jh9lk8gs6-sfn5fhz4rp7pch0000gn-T-style-pairs-dgijk4db/memory/MEMORY.md
- summarization-h04: The command redirects standard error to /dev/null with `2>/dev/null`.
- summarization-h04: The command echoes "NONE" if the `cat` command fails.
- summarization-h04: The tool invocation includes a "description" parameter with the value "Check memory index".
- summarization-h04: The parameters are given in JSON format.
- summarization-h05: Storage usage grew from 40 TB to 58 TB over the past twelve months.
- summarization-h05: The 40 TB starting figure was a measured value.
- summarization-h05: Storage usage was tracked monthly.
- summarization-h05: Storage growth was roughly linear except for a spike in March.
- summarization-h05: The March spike is believed, but not confirmed, to have been driven by new audio uploads.
- summarization-h05: March's storage data was not broken down by type.
- summarization-h05: The cluster limit is 80 TB.
- summarization-h05: Extrapolating the linear trend puts reaching the 80 TB cluster limit in about fourteen months.
- summarization-h05: The fourteen-month figure is a projection, not a certainty.
- summarization-h05: A large customer campaign is expected next quarter.
- summarization-h05: The expected campaign could accelerate storage growth.
- summarization-h05: Past customer campaigns have had mixed effects on storage growth.
- summarization-h05: There is no model for the upcoming campaign's impact.
- summarization-h05: Archive-tier compression might recover roughly 8 TB.
- summarization-h05: The 8 TB compression estimate comes from a single bucket sample.
- summarization-h05: The single bucket sample may not be representative of the full archive.

Added facts (styled only):

- code-review-h01: If `total` or `people` is not a number, the original function fails with an unclear error.
- code-review-h01: The corrected version raises a ValueError when `people` is less than or equal to 0.
- code-review-h01: The corrected version removes the unsafe float comparison.
- code-review-h01: The corrected version always rounds the last share to 2 decimal places.
- code-review-h02: var creates function-scoped variables.
- code-review-h02: If items is null or undefined, the function throws an error at items.length.
- code-review-h03: If the file does not exist, `open()` raises `FileNotFoundError`.
- code-review-h03: The code does not handle `ValueError` from bad input or `FileNotFoundError` from a missing file.
- code-review-h03: Stripping each line with `int(line.strip())` before conversion avoids the trailing-newline failure.
- code-review-h04: Nothing in the memory directory applies to this task.
- code-review-h04: The function compares passwords in plain text.
- code-review-h04: Password comparison should use a salted hash such as bcrypt or argon2.
- code-review-h04: The function uses `==` to compare passwords.
- code-review-h04: Comparison with `==` is not constant-time.
- code-review-h04: Non-constant-time password comparison exposes a timing attack.
- code-review-h04: `hmac.compare_digest` performs a comparison suitable for secrets and should be used instead of `==`.
- code-review-h04: Using a password-hash library is preferable to using `hmac.compare_digest` directly.
- code-review-h04: The log statement writes the full request to the log.
- code-review-h04: The full request can include the password.
- code-review-h04: Secrets should not be logged.
- code-review-h04: The error message does not reveal whether the username exists.
- code-review-h04: The current error message behavior is correct and should be kept.
- code-review-h04: `assert` is not correct for input validation.
- code-review-h04: Python removes assert statements when code is run with the `-O` flag.
- code-review-h04: Input validation should use an explicit check that raises an error or returns a clear response.
- code-review-h04: If `request` is not a dictionary, or if its values are not strings, the function can raise an unexpected error.
- code-review-h04: The input types should be validated.
- code-review-h04: The function does not limit login attempts.
- code-review-h04: The lack of login attempt limits leaves the function open to brute-force attacks.
- code-review-h04: Rate limiting should be added.
- code-review-h04: The function mixes validation, logging, authentication, and response building.
- code-review-h04: The function should be split into smaller functions for clarity and testing.
- code-review-h04: The function has no type hints.
- code-review-h04: The function has no docstring.
- code-review-h04: Type hints and a docstring should be added so other developers can use the function correctly.
- code-review-h05: If the system clock jumps forward, the bucket clears early and a client can bypass the limit.
- code-review-h05: A client near a one-second boundary can send close to double the limit within about one real second.
- code-review-h05: The code performs no input validation on `limit`.
- code-review-h05: A negative or zero `limit` works by accident rather than by design, because the check `len(...) <= limit` still runs.
- code-review-h05: The window check `t > now - 60` excludes a hit that is exactly 60 seconds old.
- code-review-h05: The exclusion of a hit exactly 60 seconds old is a valid choice, but it was never recorded as intended.
- code-review-h05: The 60-second window and the default limit of 20 appear to be a deliberate 'requests per minute' rule.
- code-review-h05: Storing rejected hits is correct because a rejected request should still count against the client.
- code-review-h05: If rejected requests did not count, a client could spam rejected requests for free.
- code-review-h05: In-memory-only state fits a small, single-process service.
- code-review-h05: In-memory-only state is a reasonable trade-off but breaks the multi-process case.
- debugging-h02: The snapshot_number function returns int(re.search(r"\d+", name).group()).
- debugging-h02: The example computes latest as sorted(snapshots, key=snapshot_number)[-1].
- debugging-h04: `datetime` and `timezone` are imported from the `datetime` module.
- debugging-h04: Subtracting two datetimes and calling `.total_seconds()` on the result gives the age in seconds.
- debugging-h05: The most likely cause of the duplicate webhooks is a timeout or connection problem rather than a design flaw in the retry logic.
- debugging-h05: The sender times out at 30 seconds.
- debugging-h05: A sender timeout can occur while the receiver is still processing the first request.
- debugging-h05: The receiver can return success after the sender has already queued a retry.
- debugging-h05: A network fault can break the connection after the receiver processes the webhook but before the response reaches the sender.
- debugging-h05: In the network-fault case, the receiver sees one request and the sender sees none, so the sender retries.
- debugging-h05: The receiver may return a transient non-2xx status, for example during its own deploy, even though it already recorded the webhook.
- debugging-h05: The sender's retry or queue logic may contain a bug.
- debugging-h05: A job visibility timeout shorter than the HTTP timeout plus the receiver's processing time is an example of such a bug.
- debugging-h05: A visibility-timeout bug can cause a duplicate send even without a timeout or a bad response.
- debugging-h05: Exact webhook IDs and timestamps for the duplicate deliveries can be obtained from the one customer that has receiver-side counts.
- debugging-h05: Only one customer has receiver-side counts of the duplicate deliveries.
- debugging-h05: Delivery-attempt records should be checked in the database, not just in logs.
- debugging-h05: Many systems keep attempt metadata separately from logs.
- debugging-h05: Attempt metadata stored apart from logs can survive log rotation.
- debugging-h05: The customer can be asked for the receiver's response time and status code for each duplicate webhook ID.
- debugging-h05: Asking for the receiver's response time and status code works only if the customer logs inbound requests.
- debugging-h05: Other customers can be asked to check for duplicates.
- debugging-h05: Duplicates occurring on only some customers indicate a network or receiver issue.
- debugging-h05: Duplicates occurring on all customers indicate a bug in the sender.
- debugging-h05: The retry and queue code should be reviewed for a duplicate-send bug that does not depend on timeouts or response codes.
- debugging-h05: Detailed logging should be enabled now.
- debugging-h05: The logging should record the retry reason, response time, response status, and whether the cause was a timeout or a non-2xx response.
- debugging-h05: The logged data should be retained for a longer period.
- debugging-h05: An idempotency key should be added to each webhook.
- debugging-h05: Customers should be told to deduplicate by the idempotency key.
- debugging-h05: Adding an idempotency key does not find the cause but prevents harm from the duplicate.
- debugging-h05: A gap between the two deliveries for a given webhook ID close to 30 seconds is strong evidence for the timeout cause.
- debugging-h05: A gap far from 30 seconds points more to a network reset or a code bug on the sender side.
- debugging-h06: A deploy can trigger a bad query pattern that degrades a downstream dependency.
- debugging-h06: The deploy could have increased resource use only in one region due to different traffic or instance sizing.
- debugging-h06: New instances take time to start, and unhealthy instances take time to drain from the load balancer.
- debugging-h06: A single faulty host in that region is a possible cause.
- debugging-h06: Health checks can remove a faulty host from rotation after about an hour, making the timing coincide with the deploy by chance.
- debugging-h06: Infrastructure event logs include autoscaling events, cache flush events, and load balancer health-check changes.
- debugging-h06: There are three regions, one of which was affected.
- debugging-h06: The deploy in question happened on Tuesday.
- debugging-h06: The code diff should be checked for changes to caching, connection handling, or query patterns.
- debugging-h06: Reproducing the traffic pattern in staging with production-like data is recommended before retrying the deploy.
- debugging-h06: Cache hit rate, pool usage, and downstream latency should be watched during the staging reproduction.
- debugging-h06: If the cause is a cache or pool issue, a second deploy without a fix can cause the same problem again.
- explanation-h01: OPTIONS returns supported methods and does not change state.
- explanation-h02: A B-tree index stores raw column values, not the results of functions applied to those values.
- explanation-h02: An index on customer_name does not store the result of UPPER(customer_name).
- explanation-h04: Each connection setup step often takes tens of milliseconds.
- explanation-h04: The maximum number of connections most databases allow is often a few hundred.
- explanation-h04: A pool can be thought of as a set of open phone lines to the database.
- explanation-h04: Without a pool, each request dials a new line, waits for the call to connect, then hangs up right after.
- explanation-h04: With a pool, the lines stay open and each request picks up a free line, uses it, then returns it for the next request.
- explanation-h04: For one small application, a pool of 5 to 10 connections is often enough.
- explanation-h05: The reliability benefit of a queue does not depend on traffic volume.
- explanation-h05: The reliability benefit of a queue does not depend on downtime frequency.
- explanation-h05: Even a small amount of downtime causes failed HTTP calls in the current setup.
- explanation-h05: If the queue goes down, both services can fail.
- explanation-h05: A queue system should be chosen for its own reliability guarantees.
- explanation-h05: If a queue does not persist messages to disk, a queue crash can lose data.
- explanation-h05: Message persistence should be verified before committing to a queue.
- explanation-h05: A queue causes emails to arrive later rather than right away.
- explanation-h05: The delivery delay should be confirmed as acceptable to the business.
- explanation-h05: A queue adds a system to monitor, scale, and patch.
- explanation-h06: A slow test suite in a monolith remains slow in each microservice after a split.
- explanation-h06: After a split, a slow test suite must be run many times, once per service.
- explanation-h06: A split to microservices only helps if the cause of the problem is coupling.
- explanation-h06: If teams can already deploy one module without a full rebuild and full retest of the monolith, they get part of the benefit of a split without doing one.
- explanation-h06: A monolith codebase can grow harder to change over time if module boundaries stay unclear.
- explanation-h06: If test time is the slowest step, parallel test runs or a faster test suite can fix it.
- explanation-h06: If a manual release is the slowest step, automating it can fix it.
- explanation-h06: A split should only be considered if tight coupling between modules is found to be the true blocker.
- explanation-h06: Even when coupling is the blocker, one service should be split out first as a trial before committing further.
- summarization-h02: On Monday, the customer reported that scheduled reports stopped arriving.
- summarization-h02: On Tuesday, the customer sent three report ids.
- summarization-h02: On Wednesday, the customer confirmed nothing was in spam.
- summarization-h02: The team will follow up with the provider if no response comes within two business days.
- summarization-h04: The QA test list is ordered by risk.
- summarization-h04: This release includes a change to the public API.
- summarization-h04: In the API response, invoice_number is null for draft invoices.
- summarization-h04: A null invoice_number value can break API consumer code that expects a string.
- summarization-h04: API consumers are supposed to be notified of the invoice_number change.
- summarization-h04: The release includes a migration that adds an entity prefix to all existing invoice numbers.
- summarization-h04: The migration leaves invoice numbers otherwise unchanged apart from the added prefix.
- summarization-h04: Each legal entity has its own invoice number sequence.
- summarization-h04: Two different legal entities can have the same invoice number without conflict.
- summarization-h04: Invoice numbers must be unique within a single legal entity.
- summarization-h04: An invoice receives its number only when a user finalizes it.
- summarization-h04: Draft invoices do not consume an invoice number.
- summarization-h04: Draft invoices created before this release keep their original number when finalized after the release.
- summarization-h04: The PDF template displays the prefixed invoice number.
- summarization-h04: The PDF applies to both old and new invoices.
- summarization-h04: Invoices can be searched by their new prefixed number.
- summarization-h04: Old, pre-migration invoice numbers remain searchable.
- summarization-h04: Invoices from different legal entities can be finalized concurrently.
- summarization-h04: Multiple invoices can be finalized in fast sequence.
- summarization-h04: The migration is expected to run against a large data set without failing or timing out.
- summarization-h05: The speaker will check memory for relevant context before answering.
- summarization-h05: A cloud search was performed.

## Hedging survival

The judge lists the claims that the unstyled answer presents with uncertainty, then judges each claim in the styled answer: hedged (the uncertainty survives in some form), certain (the claim survives but reads as a fact — the failure this check targets), or absent (the claim is gone, a completeness loss). Survival is hedged / (hedged + certain). The claims that became certain appear verbatim below the table.

### actionable-clarity

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-h01 | 6 | 0 | 0 | 6 | n/a |
| code-review-h02 | 2 | 1 | 1 | 0 | 0.5 |
| code-review-h03 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-h04 | 0 | 0 | 0 | 0 | n/a |
| code-review-h05 | 7 | 1 | 0 | 6 | 1.0 |
| debugging-h01 | 0 | 0 | 0 | 0 | n/a |
| debugging-h02 | 0 | 0 | 0 | 0 | n/a |
| debugging-h03 | 0 | 0 | 0 | 0 | n/a |
| debugging-h04 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-h05 | 0 | 0 | 0 | 0 | n/a |
| debugging-h06 | 9 | 6 | 0 | 3 | 1.0 |
| explanation-h01 | 6 | 3 | 1 | 2 | 0.75 |
| explanation-h02 | 4 | 2 | 2 | 0 | 0.5 |
| explanation-h03 | 4 | 1 | 3 | 0 | 0.25 |
| explanation-h04 | 3 | 2 | 0 | 1 | 1.0 |
| explanation-h05 | 4 | 2 | 1 | 1 | 0.667 |
| explanation-h06 | 3 | 2 | 1 | 0 | 0.667 |
| summarization-h01 | 0 | 0 | 0 | 0 | n/a |
| summarization-h02 | 0 | 0 | 0 | 0 | n/a |
| summarization-h03 | 0 | 0 | 0 | 0 | n/a |
| summarization-h04 | 0 | 0 | 0 | 0 | n/a |
| summarization-h05 | 5 | 5 | 0 | 0 | 1.0 |
| summarization-h06 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 58 over 23 judged pairs: 29 hedged, 10 certain, 19 absent.

Median survival: 0.75 over 13 scored pairs.

Claims that became certain:

- code-review-h02: Silently keeping items that lack an `expires` field (since `undefined < now` is `false`) is not necessarily wrong, but it's worth being intentional about.
- code-review-h03: Because the code doesn't `.strip()` lines, trailing whitespace-only lines could cause avoidable failures (though `int()` does tolerate surrounding whitespace, empty lines still fail).
- explanation-h01: POST is the common case for operations that might have side effects, such as creating an order or charging a payment.
- explanation-h02: Deletes can trigger node merges/rebalancing too.
- explanation-h02: Wrapping a column in a function usually prevents the planner from using a plain index on that column, so the query falls back to a full table scan.
- explanation-h03: With cursor pagination, encoding/decoding the cursor and needing a stable sort key is slightly more implementation work.
- explanation-h03: For an orders-listing API with high write volume, offset pagination risks users seeing duplicate or missing orders as they page through.
- explanation-h03: For a typical "list orders" endpoint, cursor pagination is usually the better default.
- explanation-h05: Generally, a queue decouples the order service from the email service's uptime, so if email is down, orders keep succeeding and messages just wait instead of failing or blocking.
- explanation-h06: If the problem is a slow test suite, unclear ownership causing merge conflicts, or a monolith where any change requires a full redeploy of unrelated code, microservices can help by letting teams deploy independently.

### clarity-flow

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-h01 | 6 | 1 | 1 | 4 | 0.5 |
| code-review-h02 | 2 | 2 | 0 | 0 | 1.0 |
| code-review-h03 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-h04 | 0 | 0 | 0 | 0 | n/a |
| code-review-h05 | 7 | 0 | 3 | 4 | 0.0 |
| code-review-h06 | 9 | 4 | 1 | 4 | 0.8 |
| debugging-h01 | 0 | 0 | 0 | 0 | n/a |
| debugging-h02 | 0 | 0 | 0 | 0 | n/a |
| debugging-h03 | 0 | 0 | 0 | 0 | n/a |
| debugging-h04 | 1 | 0 | 0 | 1 | n/a |
| debugging-h05 | 0 | 0 | 0 | 0 | n/a |
| debugging-h06 | 9 | 5 | 1 | 3 | 0.833 |
| explanation-h01 | 6 | 2 | 2 | 2 | 0.5 |
| explanation-h02 | 4 | 1 | 3 | 0 | 0.25 |
| explanation-h03 | 4 | 2 | 1 | 1 | 0.667 |
| explanation-h04 | 3 | 3 | 0 | 0 | 1.0 |
| explanation-h05 | 4 | 0 | 2 | 2 | 0.0 |
| explanation-h06 | 3 | 2 | 1 | 0 | 0.667 |
| summarization-h01 | 0 | 0 | 0 | 0 | n/a |
| summarization-h02 | 0 | 0 | 0 | 0 | n/a |
| summarization-h03 | 0 | 0 | 0 | 0 | n/a |
| summarization-h04 | 0 | 0 | 0 | 0 | n/a |
| summarization-h05 | 5 | 5 | 0 | 0 | 1.0 |
| summarization-h06 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 67 over 24 judged pairs: 30 hedged, 16 certain, 21 absent.

Median survival: 0.667 over 14 scored pairs.

Claims that became certain:

- code-review-h01: The function should probably raise `ValueError` for `people <= 0`.
- code-review-h03: Because the code doesn't `.strip()` lines, trailing whitespace-only lines could cause avoidable failures (though `int()` does tolerate surrounding whitespace, empty lines still fail).
- code-review-h05: Wall-clock time via time.time() can jump due to NTP correction or a manual clock change.
- code-review-h05: A backward clock jump can make already-expired entries look valid again and stretch the effective window.
- code-review-h05: There is no way to know whether limit=20 and the 60-second window are meaningful (SLA-driven or capacity-driven) or just made up.
- code-review-h06: Silently swallowing a parse error in an existing config file is almost certainly worth at least a log line, even if the original author didn't want it to raise.
- debugging-h06: The elevated latency points toward some stateful side effect that outlived the deploy, isolated to one region.
- explanation-h01: PATCH often expresses a delta (e.g. "increment count by 1"), which is not safe to repeat.
- explanation-h01: The unique idempotency key generated by the client is usually a UUID.
- explanation-h02: If a leaf node is full it must split, and that split can cascade up the tree, requiring rebalancing.
- explanation-h02: Deletes can trigger node merges/rebalancing too.
- explanation-h02: Wrapping a column in a function usually prevents the planner from using a plain index on that column, so the query falls back to a full table scan.
- explanation-h03: For an orders-listing API with high write volume, offset pagination risks users seeing duplicate or missing orders as they page through.
- explanation-h05: Generally, a queue decouples the order service from the email service's uptime, so if email is down, orders keep succeeding and messages just wait instead of failing or blocking.
- explanation-h05: Without traffic or downtime numbers, it's hard to say whether this is worth it.
- explanation-h06: If the problem is a slow test suite, unclear ownership causing merge conflicts, or a monolith where any change requires a full redeploy of unrelated code, microservices can help by letting teams deploy independently.

### classic-concise

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-h01 | 6 | 0 | 1 | 5 | 0.0 |
| code-review-h02 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-h03 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-h04 | 0 | 0 | 0 | 0 | n/a |
| code-review-h05 | 7 | 1 | 2 | 4 | 0.333 |
| code-review-h06 | 9 | 6 | 3 | 0 | 0.667 |
| debugging-h01 | 0 | 0 | 0 | 0 | n/a |
| debugging-h02 | 0 | 0 | 0 | 0 | n/a |
| debugging-h03 | 0 | 0 | 0 | 0 | n/a |
| debugging-h04 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-h05 | 0 | 0 | 0 | 0 | n/a |
| debugging-h06 | 9 | 8 | 0 | 1 | 1.0 |
| explanation-h01 | 6 | 3 | 0 | 3 | 1.0 |
| explanation-h02 | 4 | 1 | 2 | 1 | 0.333 |
| explanation-h03 | 4 | 1 | 3 | 0 | 0.25 |
| explanation-h04 | 3 | 1 | 0 | 2 | 1.0 |
| explanation-h05 | 4 | 1 | 3 | 0 | 0.25 |
| explanation-h06 | 3 | 2 | 0 | 1 | 1.0 |
| summarization-h01 | 0 | 0 | 0 | 0 | n/a |
| summarization-h02 | 0 | 0 | 0 | 0 | n/a |
| summarization-h03 | 0 | 0 | 0 | 0 | n/a |
| summarization-h04 | 0 | 0 | 0 | 0 | n/a |
| summarization-h05 | 5 | 5 | 0 | 0 | 1.0 |
| summarization-h06 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 67 over 24 judged pairs: 33 hedged, 16 certain, 18 absent.

Median survival: 0.667 over 15 scored pairs.

Claims that became certain:

- code-review-h01: The function should probably raise `ValueError` for `people <= 0`.
- code-review-h02: Silently keeping items that lack an `expires` field (since `undefined < now` is `false`) is not necessarily wrong, but it's worth being intentional about.
- code-review-h03: Because the code doesn't `.strip()` lines, trailing whitespace-only lines could cause avoidable failures (though `int()` does tolerate surrounding whitespace, empty lines still fail).
- code-review-h05: The unbounded burst growth (appending to the bucket before checking the limit, including for denied calls) is almost certainly not deliberate.
- code-review-h05: There is no way to know whether limit=20 and the 60-second window are meaningful (SLA-driven or capacity-driven) or just made up.
- code-review-h06: `timeout` might be `30`, `"45"`, or `30` again depending on which layer set it last.
- code-review-h06: Silently swallowing a parse error in an existing config file is almost certainly worth at least a log line, even if the original author didn't want it to raise.
- code-review-h06: The relative default path `"config.json"` could be deliberate (callers control config location via their working directory) or accidental fragility — impossible to tell without seeing the calling services.
- explanation-h02: B-tree nodes typically have high fan-out, so the tree is shallow — typically 3-4 levels even for millions of rows.
- explanation-h02: Wrapping a column in a function usually prevents the planner from using a plain index on that column, so the query falls back to a full table scan.
- explanation-h03: With cursor pagination, encoding/decoding the cursor and needing a stable sort key is slightly more implementation work.
- explanation-h03: For an orders-listing API with high write volume, offset pagination risks users seeing duplicate or missing orders as they page through.
- explanation-h03: For a typical "list orders" endpoint, cursor pagination is usually the better default.
- explanation-h05: Generally, a queue decouples the order service from the email service's uptime, so if email is down, orders keep succeeding and messages just wait instead of failing or blocking.
- explanation-h05: Queues typically deliver at-least-once, so you take on idempotency concerns.
- explanation-h05: Without traffic or downtime numbers, it's hard to say whether this is worth it.

### developer-docs

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-h01 | 6 | 2 | 2 | 2 | 0.5 |
| code-review-h02 | 2 | 0 | 0 | 2 | n/a |
| code-review-h03 | 1 | 0 | 0 | 1 | n/a |
| code-review-h04 | 0 | 0 | 0 | 0 | n/a |
| code-review-h05 | 7 | 0 | 5 | 2 | 0.0 |
| code-review-h06 | 9 | 0 | 0 | 9 | n/a |
| debugging-h01 | 0 | 0 | 0 | 0 | n/a |
| debugging-h02 | 0 | 0 | 0 | 0 | n/a |
| debugging-h03 | 0 | 0 | 0 | 0 | n/a |
| debugging-h04 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-h05 | 0 | 0 | 0 | 0 | n/a |
| debugging-h06 | 9 | 5 | 0 | 4 | 1.0 |
| explanation-h01 | 6 | 2 | 2 | 2 | 0.5 |
| explanation-h02 | 4 | 2 | 2 | 0 | 0.5 |
| explanation-h03 | 4 | 0 | 3 | 1 | 0.0 |
| explanation-h04 | 3 | 1 | 2 | 0 | 0.333 |
| explanation-h05 | 4 | 2 | 1 | 1 | 0.667 |
| explanation-h06 | 3 | 2 | 0 | 1 | 1.0 |
| summarization-h01 | 0 | 0 | 0 | 0 | n/a |
| summarization-h02 | 0 | 0 | 0 | 0 | n/a |
| summarization-h03 | 0 | 0 | 0 | 0 | n/a |
| summarization-h04 | 0 | 0 | 0 | 0 | n/a |
| summarization-h05 | 5 | 5 | 0 | 0 | 1.0 |
| summarization-h06 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 67 over 24 judged pairs: 25 hedged, 17 certain, 25 absent.

Median survival: 0.584 over 12 scored pairs.

Claims that became certain:

- code-review-h01: Because the corrected `amounts[-1]` isn't re-rounded, it can end up with more than 2 decimal places due to float imprecision (e.g. `33.33999999999999` instead of `33.34`).
- code-review-h01: The function should probably raise `ValueError` for `people <= 0`.
- code-review-h05: The unbounded burst growth (appending to the bucket before checking the limit, including for denied calls) is almost certainly not deliberate.
- code-review-h05: Wall-clock time via time.time() can jump due to NTP correction or a manual clock change.
- code-review-h05: A backward clock jump can make already-expired entries look valid again and stretch the effective window.
- code-review-h05: The append-then-check ordering looks intentional, since it allows exactly `limit` requests per window and blocks the (limit+1)th rather than being off-by-one.
- code-review-h05: There is no way to know whether limit=20 and the 60-second window are meaningful (SLA-driven or capacity-driven) or just made up.
- explanation-h01: PATCH often expresses a delta (e.g. "increment count by 1"), which is not safe to repeat.
- explanation-h01: POST is the common case for operations that might have side effects, such as creating an order or charging a payment.
- explanation-h02: Deletes can trigger node merges/rebalancing too.
- explanation-h02: Wrapping a column in a function usually prevents the planner from using a plain index on that column, so the query falls back to a full table scan.
- explanation-h03: The cursor's pointer column is usually an indexed, unique, monotonic column like `id` or `created_at+id`.
- explanation-h03: With cursor pagination, encoding/decoding the cursor and needing a stable sort key is slightly more implementation work.
- explanation-h03: For an orders-listing API with high write volume, offset pagination risks users seeing duplicate or missing orders as they page through.
- explanation-h04: Since most web frameworks and DB drivers include pooling built in (or as a one-line config), you likely don't need to hand-roll one.
- explanation-h04: For a small app, the default pool settings are usually fine.
- explanation-h05: Generally, a queue decouples the order service from the email service's uptime, so if email is down, orders keep succeeding and messages just wait instead of failing or blocking.

### plain-language

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-h01 | 6 | 0 | 3 | 3 | 0.0 |
| code-review-h02 | 2 | 1 | 0 | 1 | 1.0 |
| code-review-h03 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-h04 | 0 | 0 | 0 | 0 | n/a |
| code-review-h05 | 7 | 0 | 0 | 7 | n/a |
| code-review-h06 | 9 | 0 | 0 | 9 | n/a |
| debugging-h01 | 0 | 0 | 0 | 0 | n/a |
| debugging-h02 | 0 | 0 | 0 | 0 | n/a |
| debugging-h03 | 0 | 0 | 0 | 0 | n/a |
| debugging-h04 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-h05 | 0 | 0 | 0 | 0 | n/a |
| debugging-h06 | 9 | 0 | 0 | 9 | n/a |
| explanation-h01 | 6 | 2 | 1 | 3 | 0.667 |
| explanation-h02 | 4 | 1 | 1 | 2 | 0.5 |
| explanation-h03 | 4 | 2 | 2 | 0 | 0.5 |
| explanation-h04 | 3 | 1 | 1 | 1 | 0.5 |
| explanation-h05 | 4 | 2 | 1 | 1 | 0.667 |
| explanation-h06 | 3 | 3 | 0 | 0 | 1.0 |
| summarization-h01 | 0 | 0 | 0 | 0 | n/a |
| summarization-h02 | 0 | 0 | 0 | 0 | n/a |
| summarization-h03 | 0 | 0 | 0 | 0 | n/a |
| summarization-h04 | 0 | 0 | 0 | 0 | n/a |
| summarization-h05 | 5 | 5 | 0 | 0 | 1.0 |
| summarization-h06 | 3 | 3 | 0 | 0 | 1.0 |

Claims: 67 over 24 judged pairs: 21 hedged, 10 certain, 36 absent.

Median survival: 0.667 over 12 scored pairs.

Claims that became certain:

- code-review-h01: Because the corrected `amounts[-1]` isn't re-rounded, it can end up with more than 2 decimal places due to float imprecision (e.g. `33.33999999999999` instead of `33.34`).
- code-review-h01: It's possible for the discrepancy absorbed by the last person to be more than one cent, in which case that person's share becomes visibly unfair rather than just off by a cent.
- code-review-h01: The function should probably raise `ValueError` for `people <= 0`.
- code-review-h03: Because the code doesn't `.strip()` lines, trailing whitespace-only lines could cause avoidable failures (though `int()` does tolerate surrounding whitespace, empty lines still fail).
- explanation-h01: POST is the common case for operations that might have side effects, such as creating an order or charging a payment.
- explanation-h02: Wrapping a column in a function usually prevents the planner from using a plain index on that column, so the query falls back to a full table scan.
- explanation-h03: With cursor pagination, encoding/decoding the cursor and needing a stable sort key is slightly more implementation work.
- explanation-h03: For an orders-listing API with high write volume, offset pagination risks users seeing duplicate or missing orders as they page through.
- explanation-h04: For a small app, the default pool settings are usually fine.
- explanation-h05: Generally, a queue decouples the order service from the email service's uptime, so if email is down, orders keep succeeding and messages just wait instead of failing or blocking.

### technical-simplified

| Pair | Claims | Hedged | Certain | Absent | Survival |
|---|---|---|---|---|---|
| code-review-h01 | 6 | 0 | 2 | 4 | 0.0 |
| code-review-h02 | 2 | 0 | 1 | 1 | 0.0 |
| code-review-h03 | 1 | 0 | 1 | 0 | 0.0 |
| code-review-h04 | 0 | 0 | 0 | 0 | n/a |
| code-review-h05 | 7 | 2 | 2 | 3 | 0.5 |
| debugging-h01 | 0 | 0 | 0 | 0 | n/a |
| debugging-h02 | 0 | 0 | 0 | 0 | n/a |
| debugging-h03 | 0 | 0 | 0 | 0 | n/a |
| debugging-h04 | 1 | 1 | 0 | 0 | 1.0 |
| debugging-h05 | 0 | 0 | 0 | 0 | n/a |
| debugging-h06 | 9 | 7 | 1 | 1 | 0.875 |
| explanation-h01 | 6 | 3 | 0 | 3 | 1.0 |
| explanation-h02 | 4 | 0 | 3 | 1 | 0.0 |
| explanation-h03 | 4 | 2 | 1 | 1 | 0.667 |
| explanation-h04 | 3 | 1 | 0 | 2 | 1.0 |
| explanation-h05 | 4 | 0 | 2 | 2 | 0.0 |
| explanation-h06 | 3 | 2 | 0 | 1 | 1.0 |
| summarization-h01 | 0 | 0 | 0 | 0 | n/a |
| summarization-h02 | 0 | 0 | 0 | 0 | n/a |
| summarization-h04 | 0 | 0 | 0 | 0 | n/a |
| summarization-h05 | 5 | 0 | 0 | 5 | n/a |

Claims: 55 over 21 judged pairs: 18 hedged, 13 certain, 24 absent.

Median survival: 0.584 over 12 scored pairs.

Claims that became certain:

- code-review-h01: Because the corrected `amounts[-1]` isn't re-rounded, it can end up with more than 2 decimal places due to float imprecision (e.g. `33.33999999999999` instead of `33.34`).
- code-review-h01: The function should probably raise `ValueError` for `people <= 0`.
- code-review-h02: Silently keeping items that lack an `expires` field (since `undefined < now` is `false`) is not necessarily wrong, but it's worth being intentional about.
- code-review-h03: Because the code doesn't `.strip()` lines, trailing whitespace-only lines could cause avoidable failures (though `int()` does tolerate surrounding whitespace, empty lines still fail).
- code-review-h05: A backward clock jump can make already-expired entries look valid again and stretch the effective window.
- code-review-h05: There is no way to know whether limit=20 and the 60-second window are meaningful (SLA-driven or capacity-driven) or just made up.
- debugging-h06: The elevated latency points toward some stateful side effect that outlived the deploy, isolated to one region.
- explanation-h02: B-tree nodes typically have high fan-out, so the tree is shallow — typically 3-4 levels even for millions of rows.
- explanation-h02: If a leaf node is full it must split, and that split can cascade up the tree, requiring rebalancing.
- explanation-h02: Wrapping a column in a function usually prevents the planner from using a plain index on that column, so the query falls back to a full table scan.
- explanation-h03: The cursor's pointer column is usually an indexed, unique, monotonic column like `id` or `created_at+id`.
- explanation-h05: Generally, a queue decouples the order service from the email service's uptime, so if email is down, orders keep succeeding and messages just wait instead of failing or blocking.
- explanation-h05: Without traffic or downtime numbers, it's hard to say whether this is worth it.

## Call timing

A stored call row holds two times: duration_ms is the model
time that the CLI reports, and wall_ms is the wall clock of
the subprocess. The difference is the startup cost of one CLI
call.

Calls: 554, measured: 554.
Mean duration: 12655 ms. Mean wall: 16545 ms. Mean startup: 3890 ms.

## Harness spend

A stored call row holds the token counts of its call: the
uncached input, cache-write input, cache-read input, and
output tokens. The cache-read share is the cache-read total
over the whole input total.

Calls: 554, measured: 554.
Input tokens: 1108 uncached, 1065928 cache write, 1135309 cache read. Output tokens: 524481.
Cache-read share: 0.516.
Cache writes by lifetime: 1065928 at 5 minutes, 0 at 1 hour.

## Warnings

- actionable-clarity/code-review-h06: the pair failed the gate, excluded
- technical-simplified/summarization-h03: the pair failed the gate, excluded
- technical-simplified/code-review-h06: the pair failed the gate, excluded
- technical-simplified/summarization-h06: the pair failed the gate, excluded
