---
tags: [video, aula-03, explainer, script]
date: 2026-09-21
slug: aula-03-technology-and-tfp
---

# Narration — Aula 3: Technology, and What Solow Cannot Explain

Sources: Kurlat (2020) §4.3–4.5 and ch. 5, printed pp. 61–100; data from `data/registry.json`.

---

## BeatOpen - 95 s

Last session ended with a failure. The Solow model, fed Brazil's investment rate, predicted
that Brazil should be ninety-two per cent as rich as the United States. It is twenty-six.

So let us take the model's side for a moment, and ask what would have to be true for it to be
right.

[pause]

If the only difference between the two countries is capital, then capital must be **scarce** in
Brazil. And scarce things earn more. Diminishing returns says exactly how much more: run the
production function backwards, and the rental rate on Brazilian capital should be twelve and a
half times the American rate.

Convert that to an interest rate, and the model is telling us that lending in Brazil should pay
**one hundred and thirty-eight per cent a year**.

[pause]

Not thirteen point eight. A hundred and thirty-eight.

And if that were remotely true, every dollar of investable capital on the planet would already
be in Brazil, and would have been for decades.

[pause]

So this session does two things. First it repairs the model — because there is a real repair,
and it delivers long-run growth at last. And then it puts the repaired model on trial and
convicts it, because the second failure does not have a fix inside the model at all.

That conviction is the most useful result in the whole of growth theory, and we are going to
reach it as a verdict rather than as an opinion.

## BeatGoldenSetup - 80 s

Before the repair, we have one piece of unfinished business from last session.

We found that steady-state consumption rises with the saving rate if and only if the marginal
product of capital exceeds delta plus n. We noticed that this was strange — a model with no
optimising agent in it had produced something that looked like a welfare criterion. And then we
stopped.

Let us finish it.

[pause]

Every saving rate generates a steady state. In that steady state, what does a worker consume?
Output, minus whatever investment is needed to stand still. So consumption is f of k, minus
delta plus n, times k.

Notice I have written that without any s in it at all. That is deliberate. I used the
steady-state condition — saving equals break-even investment — to substitute s away.

[pause]

And that makes the problem much cleaner. Instead of choosing a saving rate and tracing through
to a capital stock, choose the capital stock directly. We are allowed to, because the map from
s to steady-state k is strictly increasing: every k corresponds to exactly one s, and the other
way round.

So the question becomes: over all possible steady states, which one gives the highest
consumption per worker?

## BeatGoldenFOC - 100 s

Maximise. Differentiate consumption with respect to k and set it to zero.

The derivative of f of k is f prime of k. The derivative of the break-even term is just delta
plus n. So the first-order condition is:

**f prime of k equals delta plus n.**

[pause]

Check it really is a maximum. The second derivative of consumption is the second derivative of
f — which is negative, by assumption four point three. Diminishing returns again, now
guaranteeing that this stationary point is a peak rather than a trough, and that it is the only
one.

And the Inada conditions guarantee the peak is interior: at k near zero the slope of consumption
is infinite and positive; far out it is minus delta plus n, negative. So the maximum is strictly
inside, not at a corner.

[pause]

Now read the condition, because it is one of the most intuitive things in macroeconomics.

One more unit of capital produces f prime of k, every period, forever. And it costs delta plus n
every period to keep it there — delta to replace what wears out, n to equip the extra workers
who arrive.

**At the optimum, the last machine exactly earns its own upkeep.**

Push past that point and each additional machine costs more to maintain than it produces. The
economy is then working — genuinely working, sacrificing consumption — to sustain capital that
does not pay for itself. That is not a matter of taste. That is waste.

## BeatSGold - 135 s

Now let us find the saving rate that gets us there, because that is what a policymaker would
actually control.

Under Cobb-Douglas, f prime of k is alpha times k to the alpha minus one. Set that equal to
delta plus n, solve for k, and you get the Golden Rule capital stock: alpha over delta plus n,
raised to one over one minus alpha.

And from last session we already know the steady-state capital stock for any saving rate: s over
delta plus n, raised to exactly the same power.

[pause]

Set them equal. The exponents match, the denominators match — and what is left standing is
startling in its simplicity.

**The Golden Rule saving rate equals alpha.**

[pause]

Now that is a strange-looking result. Alpha is a property of the production function. Where did
delta and n go?

Here is a second derivation that explains it rather than just confirming it.

In any steady state, investment is delta plus n, times k. And output is f of k. So the share of
output being invested — which is just s — is that ratio.

Now impose the Golden Rule condition: delta plus n *is* f prime of k at that point. Substitute
it in. The investment share becomes f prime of k, times k, over f of k.

And we know what that object is. It is the elasticity of output with respect to capital — which,
by Euler's theorem and competitive factor markets, is the **capital share of income**. Alpha.

[pause]

So the Golden Rule says: **save exactly capital's share of income.** Not more, not less. And
that is why delta and n vanished — they affect how much capital that saving rate buys, but not
the rate itself.

Put the number in. Alpha is about nought point three five, so the Golden Rule saving rate is
thirty-five per cent. The US investment rate is about twenty. So the United States is **below**
the Golden Rule.

Which sounds like a criticism. It is not, and the next beat is why.

## BeatAsymmetry - 145 s

The two sides of that peak are not symmetric, and the asymmetry is the whole substance of the
section.

**Start above the peak** — a country saving more than alpha, with more capital than the Golden
Rule. There, f prime of k is *less* than delta plus n.

Cut the saving rate. What happens?

[pause]

On impact, consumption jumps **up** — less output is being set aside, and output has not moved
yet.

During the transition, capital falls towards its new, lower steady state. Output falls with it.
But required investment falls *faster* — and it must, precisely because f prime of k is below
delta plus n across the entire range the economy travels.

And in the new steady state, consumption is **higher** than where it started.

[pause]

So consumption is higher immediately, and higher at every single date afterwards. Nobody waits.
No generation pays.

That is a Pareto improvement, and notice what we did not need to establish it: no utility
function, no discount rate, no comparison of your welfare against your grandchildren's. The
economy was simply **dynamically inefficient** — accumulating capital that could never pay for
its own upkeep. Anyone can diagnose that.

[pause]

**Now start below the peak**, which is where actual economies sit. Here f prime of k is greater
than delta plus n.

Raise the saving rate. On impact, consumption falls, discretely. During the transition it
recovers, and eventually overtakes. In the new steady state it is higher.

So some generations lose and later ones gain.

[pause]

And that is a **trade-off, not an inefficiency**. Whether it is worth making depends entirely on
how you weigh the present against the future — and the Solow model contains no object that
answers that question. There is no utility function in it. There is no discount factor. There is
nobody choosing anything.

The line worth memorising: **over-accumulation is a mistake anyone can diagnose;
under-accumulation is a preference.**

And that gap is precisely why session four exists. Put a discount rate into the model and
"should we save more?" becomes a well-posed question — with the *modified* Golden Rule as its
answer, which sits strictly below this one, because impatience now has a price.

## BeatDynamicTest - 75 s

So: is any real economy above the Golden Rule? It sounds like it would need a capital stock
estimate to check, and capital stocks are exactly what we do not trust.

It does not.

[pause]

Dynamic inefficiency means f prime of k is less than delta plus n. Multiply both sides by k.
Multiplying an inequality by a positive number is free.

On the left: f prime of k, times k — which is capital's total income.

On the right: delta plus n, times k — which is exactly break-even investment.

[pause]

So the test becomes: **is capital income smaller than investment?** And both of those are line
items in the national accounts. No production function, no capital stock estimate, nothing to
argue about.

In US data, capital income is around thirty-five per cent of GDP and investment is around
twenty. Capital income comfortably exceeds investment. The United States is below the Golden
Rule, and so is every developed economy anyone has checked.

[pause]

Which is a reassuring result and a slightly deflating one. The single welfare verdict this model
can deliver entirely on its own turns out never to bind in practice.

## BeatFirmProblem - 120 s

Now we decentralise. Everything so far has been an aggregate resource constraint with a
mechanical saving rule — no firms, no prices, nobody deciding anything.

Put in a competitive firm. It rents capital at a rental rate, hires labour at a wage, takes both
as given, and chooses how much of each to use to maximise profit: output, minus the rental bill,
minus the wage bill.

[pause]

Differentiate with respect to capital and set to zero: **the rental rate equals the marginal
product of capital.** Differentiate with respect to labour: **the wage equals the marginal
product of labour.**

That is the entire content of competitive factor markets.

And notice something worth flagging: under constant returns, the firm's *scale* is completely
undetermined. Only the ratio of capital to labour is pinned down. That is precisely why a
"representative firm" is a legitimate device here — and why it would not be under increasing
returns.

[pause]

Now put both in per-worker terms, because that is the form we use. Output is L times f of k.

Differentiate that with respect to capital. The L outside and the one-over-L from the chain rule
cancel, and you get simply **f prime of k**.

Differentiate with respect to labour, and this one needs the product rule. The first piece gives
f of k. The second gives L times f prime, times the derivative of K over L with respect to L —
which is minus K over L squared. Tidy it up, and the wage is **f of k, minus k times f prime of
k**.

[pause]

Look at what those two expressions have in common: both depend on k, and on **nothing else**.

That is constant returns again, and it has a striking implication. In this model, a country's
wage is a statement about its capital per worker and about nothing else whatsoever.

## BeatZeroProfit - 80 s

Now substitute those factor prices back into the profit expression.

Profit is output, minus the marginal product of capital times capital, minus the marginal
product of labour times labour.

And by Euler's theorem — which we proved last session — that is exactly **zero**.

[pause]

Not approximately zero. Not zero in the long run after firms enter and compete the profits away.
Identically zero, at every value of k, always.

Constant returns to scale plus competitive factor pricing **forces** profit to zero. It is not
an assumption we added; it is a consequence of two we already had.

[pause]

Check it in per-worker terms, because this is the version worth reproducing on paper.

Capital income per worker is f prime of k, times k. Labour income per worker is the wage, f of k
minus k f prime of k. Add them.

The k f prime terms cancel, and you are left with f of k. Which is y. Output per worker.

[pause]

Capital income plus labour income exhausts output exactly. That identity is the backbone of
session six, where the household owns the firm — and profit income is zero there precisely
because of this line.

## BeatAlphaEquilibrium - 145 s

Now we can finally say what alpha is, properly.

The capital share of income is the rental rate times capital, over output — which is f prime of
k, times k, over f of k. And the labour share is one minus that.

For a general production function, those shares **move as k moves**. A country in transition
would see its factor shares drift.

[pause]

For Cobb-Douglas, they do not. Substitute: f prime is alpha k to the alpha minus one, times k,
over k to the alpha. Everything cancels. The capital share is **alpha**, at every level of
capital, in steady state and out of it.

And that is the real empirical argument for Cobb-Douglas, and it is worth being precise about
the direction of the logic.

Kaldor fact three says factor shares are constant in the data. Economies are not always in
steady state. So we need a functional form that delivers constant shares **without** requiring
the economy to be at rest. Cobb-Douglas is that form. Almost any other constant-returns function
would make the share drift along a transition.

[pause]

So the chain runs: observe a stable sixty-five per cent labour share, adopt Cobb-Douglas, set
alpha to nought point three five.

Notice what that is **not**. It is not an estimate from a regression. It is read off a national
accounts identity. And that matters enormously, because in the last act we are going to use this
same alpha to *test* the model. If we had estimated alpha from the same data we then use to test
the model, the test would be circular.

[pause]

One honest caveat. With a more general CES production function, the capital share is constant
only in the Cobb-Douglas case. If capital and labour substitute more easily than Cobb-Douglas
allows, the capital share **rises** as the capital-output ratio rises — which is one of the
leading explanations for the fall in the labour share after two thousand that we saw in session
two. So the recent breakdown of Kaldor fact three is evidence against the very functional form
we just adopted. The model's convenience is bought at a price, and current data is starting to
charge it.

## BeatInterestRate - 105 s

One more price, and it is the one the rest of the course runs on.

A household has a unit of output and two ways to carry it into next period. It can lend it at
interest rate r, and get back one plus r. Or it can buy a unit of capital, rent it out for the
rental rate, and then sell what is left after depreciation — getting the rental rate, plus one
minus delta.

If both options exist and both are used, they must pay the same. Otherwise everyone does one of
them.

[pause]

So: one plus r equals the rental rate, plus one minus delta.

Cancel the ones, and:

**The interest rate is the marginal product of capital, net of depreciation.**

[pause]

Three consequences, all of which get used later.

**First**, the Golden Rule restated. The condition was f prime of k equals delta plus n.
Subtract delta from both sides, and it becomes: **r equals n.** The real interest rate equals the
population growth rate. And dynamic inefficiency is r less than n — which is the form the
condition takes in session six and throughout the overlapping-generations literature. An economy
whose interest rate sits below its growth rate is over-accumulating.

**Second**, poor countries should have high interest rates. Low capital, high marginal product,
high r. Hold on to that one — in twenty minutes it is going to be the hypothesis we kill.

**Third**, the interest rate falls monotonically as an economy develops, because f is concave.
Development is, among other things, a story about the return on capital declining.
## BeatEfficiencyUnits - 120 s

Now the repair.

Kurlat opens this section by conceding the problem outright, and I will quote him because the
candour is the point: *"If we want to understand the growth of GDP per capita in the US over the
last two hundred and fifty years, the model we have studied so far doesn't have a lot of
promise: it predicts that in the long run there will be no growth."*

[pause]

So put technology in. Output is now a function of capital and of A times L, where A is the level
of technology.

Read that placement carefully, because it is doing something specific. A multiplies **labour**.
The gloss is that better technology is equivalent to having more workers — one worker with twice
the technology is two workers with the old technology. In a few minutes we will see that this
placement is forced, not chosen.

And assumption four point nine: A grows at a constant, exogenous rate g.

[pause]

Now define **efficiency units of labour**: A times L. If L workers operate with technology A,
they produce what A-L workers would produce with technology one.

Then define everything per efficiency unit. Output per efficiency unit, capital per efficiency
unit — written with tildes.

Kurlat attaches a warning here, and it is worth repeating because it prevents the most common
error in this session: *"These are not variables we are actually interested in, but it's a
convenient way to rescale the model."*

Nobody cares about output per efficiency unit. It is scaffolding. The answer to any question is
about output per **worker**, and we will have to translate back at the end.

And by constant returns — the same three steps as before, with A-L in place of L — output per
efficiency unit is f of capital per efficiency unit.

## BeatTildeLaw - 160 s

Now the law of motion, in the new units.

The change in capital per efficiency unit is next period's capital, over next period's
efficiency units, minus this period's.

[pause]

Substitute the accumulation identity on top, as before. And on the bottom, next period's
efficiency units are one plus g, times one plus n, times this period's — because A grows at g
and L grows at n.

So the whole thing becomes: one minus delta, times k-tilde, plus s times f of k-tilde, all over
one plus g times one plus n — minus k-tilde.

[pause]

Put it over the common denominator and collect, exactly as we did last session. The numerator
becomes s f of k-tilde, minus a bracket, times k-tilde. And that bracket is one plus g, times
one plus n, minus one minus delta.

Expand it. The ones cancel. What survives is **delta, plus n, plus g, plus n times g**.

[pause]

That last cross term is second order, and let us see how second. With n at one per cent and g at
one and a half, n times g is nought point zero zero zero one five. The break-even rate itself is
about nought point zero six five. So the cross term is about **two tenths of one per cent** of
the thing it is sitting inside.

Drop it — and drop the outer one plus g, one plus n, exactly as we dropped one plus n last
session — and there it is:

**The change in capital per efficiency unit is s times f of k-tilde, minus delta plus n plus g,
times k-tilde.**

[pause]

The same equation as before, with **g added to the break-even rate**.

And the economics of that new term is exactly the economics of the old ones. Capital must now
also be built to keep up with the *effective* labour force — which grows at n plus g, not n,
because technological progress is equivalent to more workers arriving. Machines have to be
provided for them too.

Forgetting that g is one of the standard traps, and now you can see precisely what it is you
would be forgetting.

[pause]

The steady state has the identical closed form, with delta plus n plus g in the denominator. And
every proof from last session goes through **verbatim** — existence, uniqueness, global
stability. None of those arguments ever used the value of the break-even constant. They only
used that it was positive.

## BeatBGP - 125 s

Now translate back, because nobody cares about efficiency units.

In steady state, capital and output per efficiency unit are constant. But output per **worker**
is A times output per efficiency unit. A grows at g, and the tilde variable does not grow at all.

So output per worker grows at **g**. Forever.

[pause]

Here is the full table, and it is worth knowing cold, because half the errors in this session
are reading the wrong row.

Per efficiency unit — capital, output, consumption: growth rate **zero**.

Per worker — capital, output, consumption: growth rate **g**.

The aggregates — total capital, total output, total consumption: **n plus g**.

Labour: n. Technology: g.

And the ratios — the capital-output ratio, the factor shares, the interest rate: **constant**.

The wage: grows at **g**.

[pause]

That is Kurlat's Proposition four point three, and it is the headline of the entire session:
**output per capita grows at the rate of technological progress, and at nothing else.**

Not the saving rate. Not population growth. Not depreciation. Those still set the **level** of
the path — every comparative static from last session survives intact as a level effect — but the
slope is g alone.

[pause]

And check the wage row, because it is a good test of whether the table is understood. The wage
is now A times a constant. So real wages grow at g, and the labour share stays put.

Both of those are Kaldor facts. The model now delivers them — which it could not do before.

One statement that catches almost everybody: on this path, output per **efficiency unit** is
constant, not growing at g. It is output per **worker** that grows. And there is no steady state
in per-worker terms at all any more — only a path rising forever at g. Saying "k converges to
k-star" is simply false once g is positive. What converges is k-tilde.

## BeatUzawa - 155 s

Now, why does A multiply labour? Why not capital? Why not the whole function?

There are three conceivable places to put it. Multiplying labour — called labour-augmenting, or
Harrod-neutral. Multiplying capital — capital-augmenting. Or multiplying the whole production
function — Hicks-neutral.

The answer, due to Uzawa in nineteen sixty-one, is that only the first one is consistent with a
balanced growth path. And the argument is short enough to give.

[pause]

Suppose the economy has a balanced path. On it, capital and output grow at the same rate — call
it gamma — because the capital-output ratio is constant. And labour grows at n.

So the production function has to satisfy, at every single date: output today, times e to the
gamma t, equals F of capital-today-times-e-to-the-gamma-t, and labour-today-times-e-to-the-n-t.

[pause]

Now use constant returns to pull e to the gamma t out of the first argument — and out of the
front.

What is left is: initial output equals F of initial capital, and initial labour times e to the
power gamma minus n, times t.

[pause]

Look at that equation. On the left, a fixed number. On the right, an expression that must be
that same fixed number at every date t. So all of the time dependence has to be absorbable into
the **labour argument** — which is precisely to say that technology multiplies L, and grows at
gamma minus n.

That is the theorem. If a balanced growth path exists, technical progress is labour-augmenting.

[pause]

And now the exception everybody meets first, which is why this rarely comes up in practice.

Under Cobb-Douglas, the three forms are **indistinguishable**. Take A times K to the alpha, L to
the one minus alpha. Push the A inside the labour term by raising it to one over one minus
alpha. Or push it inside the capital term by raising it to one over alpha. Same function.

So with Cobb-Douglas, choosing where to put A is a choice of **units**. Kurlat says exactly
this in a footnote.

With any other constant-returns function, it is a real restriction, and only the
labour-augmenting form admits a balanced path. That is why the general statement of the model
puts A next to L — and why growth accounting, which we do in the last act, is allowed to use a
Hicks-neutral residual: because it assumes Cobb-Douglas, where it makes no difference.

## BeatDisappointing - 75 s

Before we test it, one moment of honesty about what we have just built.

We wanted to explain why output per person grows. Our answer is: because A grows. And why does A
grow? Because we assumed it does, at a constant exogenous rate.

[pause]

Kurlat does not dress this up, and the quotation is worth having: *"it is rather disappointing to
have to make this assumption. Ideally, one would like to have a deeper understanding of why
there is technological progress and what determines how fast it takes place."*

[pause]

So here is the fair summary of the Solow model with technology. It explains capital accumulation
completely — the transition, the steady state, the convergence speed, the comparative statics,
all of it derived and proved. And it explains growth **not at all**. It takes the one thing it
was built to explain and assumes it.

Making g itself an outcome is endogenous growth theory, which is later chapters and outside this
course.

And it is worth noticing that we are about to discover a *second* thing the model assumes rather
than explains. That one will turn out to matter even more.

## BeatCalibration - 125 s

Now we put numbers on the model and test it. And Kurlat's chapter five is an unusually direct
piece of model-testing for a textbook — it states a hypothesis, tests it three ways, and rejects
it.

First, the calibration. Five parameters, each read off one separate fact.

[pause]

Alpha is nought point three five, from the sixty-five per cent labour share.

g is one and a half per cent, from US growth per capita since eighteen hundred — and it is
legitimate to read g straight off that, because Proposition four point three says the growth
rate of output per worker *is* g.

n is one per cent, US population growth since nineteen fifty.

Delta is four per cent, blended from the official estimates: about two per cent for buildings,
fifteen for equipment, thirty for computers.

And s is twenty per cent, the recent US investment rate. Kurlat is careful here — the model
assumes a closed economy where saving equals investment, and the US is not closed and has been
investing more than it saves, financed by a trade deficit. Match investment and you get twenty;
match saving and you get a little less.

[pause]

Now here is the moment worth stopping on. Those five numbers came from five separate facts.
Nothing forces them to agree with a sixth.

But the model predicts the capital-output ratio: it is s over delta plus n plus g. Put the
numbers in. Nought point two, over nought point zero six five.

**Three point zero eight.**

And the measured US capital-output ratio, Kaldor fact two, is **three point two**.

[pause]

Five independently calibrated parameters reproduce a sixth fact to within four per cent.

That is the Solow model's best moment, and it deserves to be said plainly before the rest of
this session takes the model apart. It is a real success and it is not an accident.

## BeatConjecture - 75 s

Now the hypothesis on trial. Kurlat states it as a numbered conjecture, which is the right way
to state something you intend to test.

**Conjecture five point one: technology levels are the same across countries, and the
differences in GDP per capita are the result of differences in capital per worker.**

[pause]

Take that seriously for a moment, because it is not a straw man. It is coherent. It is
consistent with everything we have built. And if it were true it would be extraordinarily good
news.

Why? Because capital is a thing you can **accumulate**. A poor country under this conjecture is
not missing knowledge or institutions or anything hard to transfer — it is simply short of
machines. Save more, or let foreign capital in, and the gap closes. Poverty becomes an
engineering problem.

[pause]

Kurlat's verdict, stated before the evidence: *"we'll see that this conjecture is decisively
rejected by the evidence."*

Three tests follow. They use different data and they fail in different ways, which is what makes
the rejection so hard to argue with. Any one of them alone could be explained away. Together they
cannot.

## BeatTest1 - 175 s

**Test one: convergence.**

If all countries share a production function and a saving rate and differ only in capital, then
a poor country is just a rich country at an earlier point on the same path. And it should grow
faster.

Let us derive exactly how much faster, rather than assert it.

[pause]

Growth of output per worker is the change in f of k, over f of k. Now approximate the numerator
to first order: it is f prime of k, times the change in k. That is a Taylor step and it is the
only approximation in the derivation.

Substitute the change in k from the law of motion — Kurlat sets n and g to zero here just to
keep the algebra clean, and the argument survives without that.

You get: s times f prime of k, minus delta, times f prime of k times k over f of k.

And that last fraction is the capital share, alpha. So growth equals **s f prime of k, minus
delta alpha**.

[pause]

Read it. Growth depends on capital **only through f prime of k** — which is decreasing.

So under the conjecture, the richer country has more capital, a lower marginal product, and must
grow **more slowly**. At every point on the path, not just near the steady state. That is a sharp,
testable prediction.

[pause]

And the test is the scatter we drew in session two: growth against initial income, across
countries. There is no strong negative relation. **Failed.**

[pause]

But Kurlat raises two qualifications, and an honest treatment keeps both.

**First, population weighting.** Weight each country by its population and the data *do* show
convergence, increasingly so since nineteen eighty. The reason is not subtle: China and India
started poor and grew fast, and between them they are a third of humanity.

Is weighting right? If you are testing a universal claim about economies, a small country is as
informative an experiment as a large one. But not all economic forces operate at the national
level — perhaps each of India's states should count separately. There is no clean answer, and the
honest conclusion is that "does the world converge" is partly a question about your unit of
observation.

**Second, convergence within groups.** Among US states from nineteen twenty-nine, and among
Western European countries, poorer units genuinely did grow faster. Strongly.

So the conjecture may hold *within* a set of places sharing technology and institutions, while
failing *across* such sets. Capital abundance may explain why one American state is richer than
another without explaining why the United States is richer than Paraguay.

## BeatSpeed - 145 s

And there is a quantitative version of test one that is even more damaging. How **fast** should
convergence be?

We derived a convergence rate in session two from the stability argument. Let us do it properly
now, by log-linearisation — which is the method the empirical literature actually uses.

[pause]

Start from the growth rate of capital per efficiency unit: s times k-tilde to the alpha minus
one, minus delta plus n plus g.

Define x as the log deviation of k-tilde from its steady state. Then k-tilde to the alpha minus
one is its steady-state value times e to the alpha minus one, times x.

And at the steady state, s times k-tilde to the alpha minus one is exactly delta plus n plus g.

So the growth rate becomes delta plus n plus g, times the quantity e to the alpha minus one x,
minus one.

[pause]

Now expand that exponential to first order around x equals zero. E to the something small, minus
one, is just that something. So we get x-dot equals minus one minus alpha, times delta plus n
plus g, times x.

That is a differential equation whose solution is exponential decay at rate lambda:

**lambda equals one minus alpha, times delta plus n plus g.**

[pause]

Evaluate it. Nought point six five, times nought point zero six five. **Four point two per cent
a year**, and a half-life of about sixteen years.

Now, what do the data say? Convergence regressions consistently find about **two** per cent —
half the model's prediction, with a half-life of thirty-five years rather than sixteen.

[pause]

And here is the interesting way to state the discrepancy. Ask what alpha would have to be for
the model to predict two per cent. Solve: one minus alpha equals nought point zero two over
nought point zero six five. Alpha would have to be about **nought point six nine**.

Roughly twice the capital share in the national accounts.

Hold on to that number. It is going to reappear, from a completely different direction, in about
ten minutes — and when two independent failures both ask for the same wrong parameter, that is a
clue rather than a coincidence.

## BeatTest2 - 65 s

**Test two: predicted levels.**

This one is blunt. Do not look at growth rates at all. Take measured capital stocks across
countries, put them through the common production function, and ask what output it predicts.

[pause]

Kurlat's figure is stark. Predicted output per person is systematically **above** actual output
per person — and the gap gets **larger the poorer the country**.

For the poorest countries, the model predicts about **ten thousand dollars** per person. The
actual figure is closer to **one thousand**.

[pause]

A factor of ten, in the wrong direction, concentrated exactly where the conjecture most needs to
succeed.

That is not a calibration quibble you can argue away with a different delta. Poor countries
produce far, far less than the capital they demonstrably have should allow.

**Failed.**

And notice this test needed capital stock data — which is the weakest data in the exercise. So a
sceptic could still push back. Which is why the third test is the one that matters.

## BeatLucas - 180 s

**Test three**, and it is the one you should remember, because it needs **no capital data at
all**. Only relative incomes and the capital share.

Interest rates are observable. And we proved in Act Two that the rental rate on capital is f
prime of k.

[pause]

Suppose country A is x times richer per person than country B. Under the conjecture, the only
difference is capital, so from the production function that income ratio is the capital ratio
raised to alpha.

Now we want the ratio of marginal products. The marginal product is alpha times k to the alpha
minus one. So the ratio of rental rates is the capital ratio raised to alpha minus one.

Combine those two and eliminate the capital ratio, which we do not know and do not want.

**The rental rate ratio equals the income ratio, raised to the power alpha minus one, over
alpha.**

[pause]

That exponent, at alpha equals nought point three five, is minus one point eight six.

Kurlat's own example: Mexican income per person is about nought point three of the US level. So
the Mexican rental rate should be nought point three to the minus one point eight six — about
**nine point four times** the American rate.

[pause]

Now let us run it on our own numbers.

Brazilian income per head is twenty-five point seven per cent of American. Put that through the
same formula and the Brazilian rental rate should be **twelve and a half times** the American
one.

The American rental rate, from the calibration, is eleven point four per cent. Multiply. Subtract
depreciation.

**A Brazilian interest rate of one hundred and thirty-eight per cent a year.**

And for India, at twelve per cent of US income, the formula demands a rental rate **fifty-two
times** the American one.

[pause]

Nothing remotely like that exists anywhere. And the corollary is worse than the level itself: if
capital genuinely earned twelve times more in Brazil, capital would pour in until the rates
equalised. It does not. Capital mostly flows between rich countries.

That is the **Lucas paradox**, and it is the most quotable failure of the capital hypothesis
precisely because it needs almost no data. **Failed.**

[pause]

Why is the exponent so violent? Because alpha is small. With a small capital share, explaining a
large output gap through capital alone requires an **enormous** capital gap — and diminishing
returns then prices that scarce capital extravagantly.

And notice: raise alpha towards nought point seven and the exponent falls to minus nought point
four three, which would give a rental ratio of about one point six. Believable.

There is that number again. Two independent failures, both asking for a capital share of about
seventy per cent instead of thirty-five.
## BeatResidual - 150 s

Three tests, three failures. Income differences across countries are not mainly differences in
capital.

So what is left? Whatever makes a given quantity of capital and labour produce more or less
output. Measuring that is growth accounting, and it is a piece of machinery you will use for the
rest of your career, so let us derive it rather than quote it.

[pause]

Start from a production function with technology as a **separate argument** — not committing to
where it sits. Output is F of capital, labour, and A.

Totally differentiate with respect to time. Output's derivative is: the marginal product of
capital times capital's derivative, plus the marginal product of labour times labour's
derivative, plus the derivative with respect to A times A's derivative.

[pause]

Now divide everything by output, and multiply and divide each term by the variable it involves,
so that every piece becomes a growth rate.

Look at what the coefficients turn into.

The coefficient on capital growth is the marginal product of capital, times capital, over output
— which is the **capital share**.

The coefficient on labour growth is the **labour share**.

[pause]

And that is the step that makes this whole thing implementable, so it is worth seeing clearly
what just happened. Those coefficients are elasticities of the production function — objects we
cannot observe. But by Act Two of this video, competitive factor markets make them equal to
factor **shares** — which are line items in the national accounts.

That is why growth accounting can be done at all. It rests entirely on competitive factor
pricing.

[pause]

With Cobb-Douglas the shares are alpha and one minus alpha, so:

**Output growth equals A-growth, plus alpha times capital growth, plus one minus alpha times
labour growth.**

Subtract labour growth from both sides and it becomes even cleaner in per-worker terms: growth
of output per worker equals A-growth, plus alpha times growth of capital per worker.

[pause]

And now the crucial move: we solve it for the thing we cannot see.

**A-growth equals output growth, minus alpha times capital growth, minus one minus alpha times
labour growth.**

That is the **Solow residual**. And notice exactly what it is. Nothing about A was measured.
Nothing about A was observed. A is *defined* as whatever makes the identity balance.

## BeatIgnorance - 95 s

Which brings us to the single most important caveat in this session.

The residual is called total factor productivity, and it gets described as "technology". It is
not technology. It is everything the identity could not account for.

[pause]

Here is what is actually inside it.

Genuine technical progress — yes, some of it.

**Mismeasured inputs.** Capital that sits idle in a recession still counts as capital. Workers
who try harder count the same as workers who do not. Machines that got better count as the same
machines.

**Composition.** Move workers from a low-productivity sector to a high-productivity one and
measured TFP rises, without anything anywhere becoming more productive.

**Allocation.** The same inputs, distributed better across firms.

**Institutions, distortions, corruption, misallocation** — all of it lands here.

And **every error** in alpha, in the capital series, in the labour series.

[pause]

Abramovitz's phrase, which Kurlat echoes, is that the residual is *"a measure of our
ignorance"*. That is not modesty. It is a definition.

Two consequences worth carrying.

First, measured TFP is strongly **procyclical** — it falls in recessions and rises in booms. As a
statement about technology that is absurd; technology does not regress in a recession. Most of it
is unmeasured capital utilisation.

[pause]

Second, and more important here: when you write down that a poor country has low TFP, you have
not explained anything. You have named a residual. Calling it "technology" is a decision about
vocabulary, not a finding about the world.

## BeatDevAccounting - 105 s

Now, there are two different exercises that use nearly identical algebra, and confusing them is
common because nothing in the mathematics stops you.

**Growth accounting** asks: why did *this country* grow? One country, many dates, growth rates.

**Development accounting** asks: why is *this country* poorer than that one? Many countries, one
date, levels.

Let us do the second, since that is the question this whole session is about.

[pause]

Write output per worker as A times k to the alpha. Take the ratio of two countries. Take logs.

The observed income gap equals **alpha times the log capital gap**, plus **the log TFP gap**.

Two terms. The first we can measure. The second is the residual again.

[pause]

Work an example, with the round numbers Kurlat uses. A country at one tenth of US income per
worker, with fifteen per cent of US capital per worker.

Capital's contribution is nought point one five, raised to nought point three five — which is
nought point five one five. So capital alone would make this country about half as rich as the
US.

But it is one **tenth** as rich. So TFP has to supply the rest: nought point one, divided by
nought point five one five, is nought point one nine.

[pause]

In log terms, which is how these are reported: capital accounts for about **twenty-nine per
cent** of the gap, and TFP for **seventy-one**.

So: capital explains a factor of two out of a factor of ten. TFP explains the other factor of
five.

That is the standard headline. And it is about to move by twenty percentage points.

## BeatKYform - 145 s

Because there is a real problem with the decomposition we just did, and it is worth understanding
rather than memorising.

**Capital is endogenous.** A country with high productivity is a profitable place to invest, so
it accumulates more capital. Which means that when we attribute part of its income advantage to
"capital", we are crediting capital with something that productivity caused.

The two terms are not independent, so splitting them is misleading.

[pause]

The fix is to decompose using the capital-**output** ratio instead of capital per worker.

Here is the algebra. Output per worker is A times k to the alpha. Write k as K over Y, times Y
over L — that is, the capital-output ratio times output per worker.

So y equals A, times the capital-output ratio to the alpha, times y to the alpha.

Collect the y terms: y to the one minus alpha equals A times the capital-output ratio to the
alpha.

Raise both sides to one over one minus alpha:

**Output per worker equals A to the one over one minus alpha, times the capital-output ratio to
alpha over one minus alpha.**

[pause]

Why is this better? Because along a balanced growth path the capital-output ratio is **constant**
and does not respond to technology in the long run. We proved that two acts ago. So the two terms
in this decomposition are much closer to genuinely independent.

The exponent on the capital term is now alpha over one minus alpha — nought point five four,
larger than before. But it is applied to a ratio that varies far **less** across countries.
Capital-output ratios are broadly similar everywhere; capital-labour ratios are not.

[pause]

Run the same example. Take the country's capital-output ratio at eighty per cent of the US
level.

Capital's share of the log gap is now **five point two per cent**. Not twenty-nine. Five.

TFP takes **ninety-five per cent**.

[pause]

So the honest summary is not "TFP explains about seventy per cent". It is: under the
decomposition whose two terms are closest to independent, TFP carries almost all of it — and the
answer moves by twenty points on a modelling choice a careless reader would never notice.

Always say which decomposition you used.

## BeatHumanCapital - 150 s

There is one obvious objection left, and it deserves a proper answer rather than a dismissal.

Labour is not homogeneous. An American worker has perhaps twelve years of schooling; a worker in
a very poor country perhaps four. Calling them both "one unit of labour" is absurd. Put human
capital in, and maybe the residual shrinks.

[pause]

So write output as A, times capital to the alpha, times h times L, all to the one minus alpha —
where h is human capital per worker.

Now, how do you measure h? This is the part worth knowing, because it is not arbitrary.

It comes from **Mincer wage regressions**. The empirical regularity, found in essentially every
country anyone has looked at, is that log wages rise roughly linearly in years of schooling, with
a return of about six to ten per cent per year of schooling.

And here is the argument that turns that into a productivity measure: in competitive labour
markets, workers are paid their marginal product. So if an extra year of school raises your wage
by ten per cent, it raised your productivity by ten per cent.

Therefore **h is e to the phi times S** — exponential in years of schooling.

[pause]

Run the numbers. Four years of schooling against twelve, with a ten per cent return. The
difference is eight years, so the ratio is e to the minus nought point eight — about **nought
point four five**.

And its contribution to income is that raised to one minus alpha, which is nought point five
nine.

So human capital explains a factor of about one point seven, out of a tenfold gap. **Real, and
nowhere near sufficient.**

[pause]

One exponent trap, and it is a common slip worth a sentence. In the capital-per-worker form, h
enters raised to one minus alpha. In the capital-output-ratio form, the same algebra we did a
moment ago gives h an exponent of **one**.

Carry the wrong one across and you understate human capital by a third.

Put everything together: in the per-worker form, physical and human capital jointly account for
about half the gap. In the preferred capital-output form, about forty per cent — leaving sixty
for TFP. That second figure is the standard result in the literature.

## BeatClose - 145 s

So where does that leave us?

We repaired the model. Technology was added, and output per worker now grows forever, at the rate
g — which the model assumes rather than explains.

Then we put the repaired model on trial, and it failed three independent tests. Convergence does
not look the way it must. Predicted output levels are wrong by a factor of ten among the poor.
And the implied interest rates are absurd — a hundred and thirty-eight per cent for Brazil.

What survives is a residual. And the residual is most of the answer.

[pause]

So where do productivity differences come from? The honest answer is that this model does not
say, and here are the candidates that the literature offers.

**Misallocation** — the same technology, used badly. If capital and labour are spread across
firms in a way that does not equate marginal products, aggregate productivity falls even with
identical technology in every firm. Estimates suggest moving China and India to US allocative
efficiency would raise their productivity by thirty to sixty per cent.

**Institutions** — property rights, contract enforcement, corruption.

**Barriers to adoption** — knowledge is non-rival and ought to spread freely. Something stops it.

**The quality of human capital** rather than its quantity — years of schooling are not learning,
and test scores differ across countries far more than enrolment does.

And **measurement** — some of the residual is simply not real.

[pause]

Here is the frame to hold.

One bar: the income gap between a poor country and the United States, split into its parts.
Drawn once under each decomposition. Capital shrinks from twenty-nine per cent of the gap to
five, and the productivity block swells to fill almost all of it.

Underneath, one line: *the residual is what we cannot explain — and its size depends on a choice
you have to declare.*

[pause]

That is the honest verdict on this session. The Solow model localises the problem with real
precision. It proves that the answer is not capital — which is a genuine, non-obvious,
hard-won result. And then it names what is left and hands it over.

Next session we stop taking the saving rate as given, and ask where it comes from.
