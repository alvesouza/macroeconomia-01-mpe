---
tags: [video, aula-02, explainer, script]
date: 2026-09-21
slug: aula-02-solow
---

# Narration — Aula 2: Growth Facts and the Mechanics of Solow

Spoken register: every symbol said in words. `[pause]` marks a silence realised as held frame
time in `scenes.py`. Sources: Kurlat (2020) ch. 3 and §4.1–4.2, printed pp. 47–61; data from
`data/registry.json`.

---

## BeatOpen - 80 s

Brazil invests about eighteen per cent of everything it produces. Gross capital formation,
averaged over the last two decades, from the World Bank.

The United States invests about twenty-one per cent.

[pause]

Three percentage points apart. And an American is four times richer than a Brazilian.

[pause]

Now, by the end of this video you will be able to take those two investment rates, put them
into the most famous model in all of macroeconomics, turn the handle, and watch it tell you —
with a completely straight face — that Brazil ought to be ninety-two per cent as rich as the
United States.

Not twenty-six per cent. Ninety-two.

[pause]

The model is not broken. It is the model we are going to build, line by line, and it is right
about a great many things. But it is out by a factor of three and a half on the single most
important question in the subject, which is why some countries are rich and others are not.

Watching precisely where it fails is more instructive than watching it succeed. Because the
thing that makes it fail is the same assumption that makes everything else in it work.

## BeatVeryLongRun - 100 s

Start with the fact that needs explaining, and it is stranger than it looks.

Here is output per person in the United Kingdom, going back centuries. It is on a log scale,
so a straight line means a constant growth *rate*, and the slope is that rate.

How do we know anything about the year fourteen hundred? Indirectly. Skeletal heights.
Livestock counts. Crop yields. Iron output. And one powerful anchor: any society that did not
starve was living above subsistence, which is on the order of four hundred dollars a year at
today's prices — roughly today's extreme poverty line.

[pause]

Two things jump out.

Before eighteen hundred, Britain was above subsistence, and growing — but slowly. Kurlat is
careful here: this is contested. Some economic historians read the pre-industrial series as
essentially flat, stuck near subsistence.

And then, in the nineteenth century, the line bends upward. The growth rate itself changes.
That is the Industrial Revolution, and it is worth saying plainly that there is no settled
answer as to what caused it, or why it happened in Britain first.

[pause]

Every country has gone through some version of that bend, from a starting point not far above
subsistence — but at wildly different dates. And here is the part to carry with you: what
orders countries by income today is mostly the **date of the take-off**, not the growth rate
afterwards. Countries that started growing early are rich. That is almost the whole story of
the cross-country distribution.

## BeatKaldor - 170 s

In nineteen fifty-seven Nicholas Kaldor looked at the data for developed economies and pulled
out a handful of what he called *remarkable historical constancies*. A growth model is judged
by whether it reproduces them, so let us get them exactly right, with the American numbers
attached.

**Fact one. The growth rate of output per person is constant.** A straight line fits the US
from eighteen hundred to twenty sixteen. The rate is about one and a half per cent a year.

Now, one and a half per cent sounds like nothing. Compound it over two hundred and sixteen
years and output per person is about twenty-seven times higher. Check it with the arithmetic
from the last session: one point zero one five, raised to two hundred and sixteen, is about
twenty-five. The book's twenty-seven implies one and a half three. The two statements agree
to the rounding, and that is the sort of check you should run on every number a textbook
hands you.

[pause]

**Fact two. The ratio of capital to output is constant.** In the United States it sits near
three point two. Read that as: the total stock of capital America has accumulated is what the
economy produces in a bit over three years.

And a measurement caveat that matters. Nobody observes the capital stock. It is *built* —
by taking investment and cumulating it, subtracting depreciation as you go. That is the
perpetual inventory method, and notice what it is: it is the accumulation identity of this
very model, run forwards from a guess. The same depreciation rate appears in the data
construction and in the theory.

[pause]

**Fact three. The shares of labour and capital in national income are constant.** Split income
into wages on one side and profits, rents, interest and depreciation on the other. The
American labour share sat very stably at about sixty-five per cent until roughly the year two
thousand, and has since fallen by about three percentage points.

There is a genuine measurement problem hiding in there, and it is worth knowing because it is
why different papers report different labour shares. What do you do with **proprietors'
income** — the earnings of someone who owns and works in their own small business? Is that a
return to their labour, or to their capital? It is both, and the accounts cannot separate
them. The usual fix is to throw the whole category out, which quietly assumes the split inside
that sector matches the rest of the economy. Kurlat calls that "not entirely satisfactory",
which is the polite version.

## BeatFactFour - 150 s

And then there is a fourth fact: the average rate of return on capital is constant.

Here is the nice thing about it. It is not an independent fact at all. It follows from the two
we already have, in two lines of arithmetic.

The return on capital is, by definition, capital income divided by the capital stock.

[pause]

Now do something that looks like it achieves nothing: divide the top and the bottom by GDP.

The numerator becomes capital income over GDP — which is the capital **share**. Constant, by
fact three.

The denominator becomes the capital stock over GDP — which is the capital-output ratio.
Constant, by fact two.

A ratio of two constants is a constant. That is the whole proof.

[pause]

And it gives us a formula worth keeping: the return on capital is one minus the labour share,
divided by the capital-output ratio.

Put the American numbers in. One minus nought point six five is nought point three five.
Divide by three point two. About eleven per cent.

[pause]

One necessary caveat, and it is the sort of thing that separates a right answer from a
nearly-right one. That eleven per cent is **gross** of depreciation, because the capital
income we measured includes the depreciation allowance. Net of a depreciation rate of about
five per cent, the return is nearer **six** per cent. Six is the number that belongs in a
calibration, and it is the number that will reappear as the real interest rate when we build
general equilibrium in session six.

[pause]

And Kurlat states fact four separately anyway, even though it carries no independent
information. Why bother?

Because the *path* of the return on capital is what an enormous amount of growth theory is
really about. If capital accumulates and its marginal product falls — which is exactly what
diminishing returns says must happen — then the return on capital should be falling too. The
fact that it has not fallen, across two centuries of colossal capital accumulation, is a real
puzzle, and it is one of the things technological progress is called upon to resolve in the
next session.

So keep it in view. It is not an extra fact. It is a constraint, hiding as a redundancy.

## BeatScatter - 155 s

One last fact, and it is the one the model will ultimately fail.

Take every country, plot its growth rate since nineteen sixty against how rich it was in
nineteen sixty. What shape should that be?

[pause]

Here is the actual picture. And the striking thing is that it is *asymmetric*.

The countries that started rich are all bunched together, growing at rates close to one
another, somewhere in the middle of the range. Low variance, no drama.

The countries that started poor are sprayed everywhere. South Korea and Botswana grew fast
enough to close most of the gap. Congo and Madagascar grew slowly, or negatively, and fell
further behind. Same starting income, utterly different outcomes.

[pause]

So what does this refute?

It refutes **absolute convergence** — the claim that poor countries grow faster than rich ones,
full stop. If that were true this picture would be a downward-sloping line. It is a cloud.

What survives is a weaker and much more interesting claim, called **conditional convergence**:
that each country converges towards *its own* destination, and grows faster the further below
that destination it currently sits. Countries differ enormously in how much they save, how
fast their populations grow, and how well their institutions work — so they have different
destinations, and there is no reason for the poor ones to be catching up in general.

Hold on to that distinction. It is one of the most reliable ways to get an exam question
wrong, and by the end of this video we will have derived it rather than asserted it.

[pause]

There is a second way to look at the same data, and it is worth knowing because it answers a
different question.

Instead of plotting growth against initial income, plot the whole *distribution* of country
incomes relative to the United States, and watch that distribution over time. If poor
countries were catching up, the distribution would be collapsing towards a point.

It is not collapsing. If anything it has spread, and some economists argue it has become
bimodal — a cluster of rich countries, a cluster of poor ones, and a thinning middle.

Two pictures, two questions. The scatter asks whether poor countries grow faster. The
distribution asks whether the world is becoming more equal. You want both in an exam answer
about convergence, because they can disagree.

## BeatCRS - 155 s

Now we build the model. Kurlat lists eight assumptions and says we will see the role each one
plays later on. Let us do that as we go, because knowing which result rests on which
assumption is exactly what makes the model usable when an exam question perturbs one of them.

Output is made from capital and labour by some production function F.

**Assumption one: constant returns to scale.** Scale both inputs by any factor lambda, and
output scales by the same lambda.

What does it buy? The entire per-worker version of the model, which is the only reason any of
this is tractable. There is exactly one step in the derivation that uses it, and without that
step output per worker is not a function of capital per worker alone — the model would not
close in one variable.

What does it mean economically? **Replication.** If you can build a second identical factory
and staff it with a second identical workforce, you get twice the output. That is a plausible
claim about an entire economy and a much less plausible claim about a single firm with one
irreplaceable manager. The aggregate is where it is defensible.

[pause]

**Assumption two: marginal products are positive.** More capital, more output. More labour,
more output.

**Assumption three: marginal products are diminishing.** The second machine adds less than the
first.

Remember assumption three, because it is the engine of this entire model. It is why
accumulating capital cannot sustain growth forever. It is why a country far below its
destination grows fast. And it is what will ultimately fail us in the last act.

[pause]

**Assumption four: the Inada conditions.** As capital goes to zero, its marginal product goes
to infinity. As capital goes to infinity, its marginal product goes to zero.

Kurlat's gloss is exactly right: with almost no capital, a little capital is extraordinarily
useful. With an enormous amount of capital, more is nearly useless, because there is nobody
left to operate the extra machines.

And here is the technical point that almost everyone glides over, and that Kurlat explicitly
flags: **Inada does not follow from diminishing returns, and diminishing returns does not
follow from Inada.** They are separate assumptions, and in the fourth act we will see that
they buy two completely different halves of one theorem.

## BeatCobbDouglas - 125 s

Let us make this concrete with the functional form the whole course uses: output equals
capital to the power alpha, times labour to the power one minus alpha. Cobb and Douglas,
nineteen twenty-eight.

Kurlat says it is easy to verify that this satisfies all four assumptions, and then does not
verify it. Let us verify it, because the last check is the one that matters.

[pause]

**Constant returns.** Replace capital with lambda-capital and labour with lambda-labour.
Lambda to the alpha, times lambda to the one minus alpha, is lambda to the power one. Pull it
out, and you are left with lambda times the original. Constant returns to scale. Done.

**Positive marginal products.** Differentiate with respect to capital: alpha times capital to
the alpha minus one, times labour to the one minus alpha. Tidy that up and it is simply alpha
times output over capital. Positive, as long as alpha is between zero and one. And by the
same move, the marginal product of labour is one minus alpha, times output over labour.

**Diminishing.** Differentiate again. You pick up a factor of alpha minus one — which is
negative, because alpha is less than one. So the second derivative is negative. Diminishing
returns, and notice it came entirely from alpha being below one.

[pause]

**And Inada.** Write the marginal product of capital in terms of capital per worker: it is
alpha times k to the power alpha minus one. Now that exponent is negative. So as k goes to
zero, we are raising a vanishing number to a negative power, and it explodes to infinity. And
as k goes to infinity, it collapses to zero.

All four. And every single one of them turned on the same fact — that alpha is strictly
between zero and one.

[pause]

Which raises the obvious question. Alpha has been a letter so far. What *is* it?

## BeatEuler - 135 s

Alpha is not an arbitrary label. It is a number you can read straight off a national accounts
table, and here is why.

Suppose factor markets are competitive, so each factor is paid its marginal product. We prove
that properly in session three; take it for now.

Then total payments to capital are the marginal product of capital, times the amount of
capital. We computed that marginal product a moment ago: alpha times output over capital.
Multiply by capital, and the capital cancels.

Total capital income is alpha times output. So **alpha is the capital share of income**. And
by the identical computation, labour's share is one minus alpha.

[pause]

Now notice something remarkable. Those two shares add up to exactly one. Paying both factors
their marginal products exhausts output precisely — no more, no less. There is nothing left
over, and nothing missing.

That is not a coincidence of Cobb-Douglas. It is a theorem, and it is worth proving because it
underpins the zero-profit condition we will use for the rest of the course.

**Euler's theorem.** Take the constant-returns condition: F of lambda-K and lambda-L equals
lambda times F. Differentiate both sides with respect to lambda. On the left, the chain rule
gives the marginal product of capital times K, plus the marginal product of labour times L. On
the right, just F. Now set lambda equal to one.

Marginal product of capital, times capital, plus marginal product of labour, times labour,
equals total output. Exactly.

[pause]

So constant returns to scale is what guarantees that a competitive firm makes exactly zero
profit. Not approximately. Exactly.

And now put the number in. Kaldor fact three told us the labour share is about sixty-five per
cent. So alpha — the capital share — is about **nought point three five**.

Think about what just happened. A parameter in an abstract production function turned out to
be a number sitting in a national accounts table. Two completely different literatures, one
number. That is a model doing something right.

## BeatSavingRate - 170 s

Four assumptions left, and they are the ones that close the model.

**Assumption five: the population grows at a constant, exogenous rate n.** Kurlat flags that
this is, and I quote, "actually a very big deal", and he is right. For most of human history
population growth was *not* exogenous — it responded to living standards, the way an animal
population does. Exercise four point five, on page seventy-three, is the Malthus exercise, and
its punchline inverts this entire model: with endogenous fertility, a productivity improvement
raises the number of people rather than the income of each one, and living standards return to
subsistence. That is not a curiosity. That is the model of the pre-eighteen-hundred segment
we looked at ten minutes ago — the other ninety-nine per cent of human history.

There is also an assumption hiding inside assumption five: everybody alive works. So labour
and population are the same variable, and per worker means per capita. The distinction
matters enormously in data, and it waits until session five.

[pause]

**Assumption six: the economy is closed, with no government.** So output is just consumption
plus investment.

**Assumption seven: the saving rate is an exogenous constant s.**

Kurlat separates the next two steps deliberately, and you should too. First: in a closed
economy, saving — output minus consumption — *is* investment. That is an identity. It is not a
behavioural claim, and nothing can make it false.

Second: saving equals s times output. *That* is the behavioural assumption, and it is the one
the rest of this course spends its time dismantling. From session four onwards, s stops being
a parameter and becomes a decision — a function of the interest rate, of impatience, and of
expected future income.

[pause]

One footnote worth reproducing, because students routinely assume saving equals investment
requires no government, and it does not. Put a government in, collecting taxes tau and
spending G. National saving is private saving, output minus taxes minus consumption, plus
public saving, taxes minus spending. Add them. **The taxes cancel.** You are left with output
minus consumption minus government spending, which is investment.

Saving equals investment in any closed economy, whatever the government does. What government
spending changes is the *level* of saving, not the identity.

**Assumption eight: capital depreciates at a constant rate delta.** So next period's capital
is what survived, one minus delta times today's, plus what was built.

That last line is the same stock-and-flow identity from the end of session one — and the same
equation the statisticians use to construct the capital stock we were quoting as fact two.
## BeatPerWorker - 90 s

We now have everything, and the model has one moving part. Let us find it.

Define output per worker, y, as output divided by labour. And capital per worker, k, as
capital divided by labour.

Now watch three steps, of which only the middle one is doing any work.

[pause]

Step one: replace output with the production function. Output per worker is F of K and L, all
over L.

Step two — and this is the substantive one — apply constant returns to scale with lambda equal
to one over L. Scaling both arguments by one over L scales the output by one over L, so
dividing by L is the same as putting one over L inside the function. F of K over L, and L over
L. Which is F of k, and one.

Step three is a definition. Call that little f of k.

[pause]

So output per worker is a function of capital per worker alone. That is the whole payoff of
constant returns, and it is the only place we use it.

For Cobb-Douglas, little f of k is simply k to the alpha. And it inherits everything: its
slope is positive, its second derivative is negative, its slope goes to infinity at zero and
to zero at infinity. Every property we verified, now in one variable.

## BeatLawOfMotion - 150 s

Now for the central derivation of this session. How does capital per worker move over time?

We want the change in k from this period to the next. Write it out.

[pause]

Line one, definition: the change is k next period minus k this period.

Line two: k next period is, by definition, capital next period divided by **labour** next
period. Keep your eye on that subscript — it is where everything goes wrong.

Line three: use the accumulation identity to replace capital next period. What survived,
one minus delta times K, plus what was invested.

Line four: use the saving assumption to replace investment with s times output.

[pause]

So far, so mechanical. Now the step that has to be done carefully.

We have a numerator in aggregate terms and a denominator that is labour *next* period. We want
everything per worker, this period. So multiply and divide by labour this period.

Now the numerator, divided by this period's labour, is exactly what we want — it is one minus
delta, times k, plus s times little f of k, all in per-worker terms.

And what is left over is the ratio of this period's labour to next period's labour. By
assumption five, next period's labour is one plus n times this period's. So that ratio is one
over one plus n.

[pause]

And there it is. The change in capital per worker equals one minus delta times k, plus s times
f of k, all divided by one plus n — minus k.

That is the **exact** law of motion. Not an approximation. Every symbol of it is implied by
the assumptions we wrote down, and it is what you would program if you were simulating this
economy.

[pause]

Look at what the one plus n is doing down there. It is a dilution term. Next period there are
more workers sharing the same pile of machines, so even if the pile grew, the pile *per
worker* may not have. Population growth dilutes capital in exactly the way that water dilutes
a solution, and that division is how it enters.

Forgetting it is trap number two in the course notes, and now you can see precisely what you
would be forgetting.

## BeatApproximation - 120 s

Now, nobody writes the equation in that form. Let us see why, and what it costs.

Put everything over the common denominator, one plus n. The k at the end becomes one plus n,
times k, over one plus n.

Collect the numerator. One minus delta, times k, plus s f of k, minus one plus n times k.
The k terms combine: minus delta k, minus n k.

So the change in capital per worker equals s times f of k, minus delta plus n, times k — all
divided by one plus n.

[pause]

And there is the famous equation, hiding under a division. Drop the one plus n and you have
the form every textbook prints: **the change in capital per worker is actual investment,
minus break-even investment.**

Two consequences, and both matter.

**First, and this is the important one: the approximation is exact at the steady state.**
Dividing by one plus n, which is a positive number, cannot move a zero. Whatever n is, the two
expressions vanish at exactly the same value of k.

So the one plus n affects the **speed** at which the economy travels, and never its
destination. That is why it is safe to use the simple form for every comparative static we are
about to do — and why forgetting it gives you the right steady state and the wrong path.

[pause]

**Second, the error is a clean fraction.** The difference between the two expressions is n over
one plus n, times the change itself. With n at one per cent, the simple form overstates each
period's movement by about one per cent of that movement.

Negligible in one year. Over a fifty-year transition it accumulates into a visibly faster
path. Worth knowing it is there; not worth carrying the term around.

## BeatContinuous - 160 s

There is a second route to the same equation, and you need it because exam questions mix the
two conventions freely.

Work in continuous time. Capital per worker is capital divided by labour, both functions of
time. Differentiate using the quotient rule.

[pause]

The derivative of K over L is: K-dot times L, minus K times L-dot, all over L squared.

Split that into two terms. The first is K-dot over L. The second is K over L, times L-dot over
L — which is k times the population growth rate n.

So k-dot equals K-dot over L, minus n k.

Now replace K-dot. In continuous time the accumulation identity is simply: capital changes by
investment minus depreciation. So K-dot is s times output, minus delta K. Divide by L, and it
is s times f of k, minus delta k.

[pause]

Put them together, and: **k-dot equals s f of k, minus delta plus n, times k.**

Now look at that, and look back at what we called the approximation a minute ago. They are
the same equation. Identical.

That is the reconciliation, and it is worth stating clearly: what Kurlat presents as an
approximation to a difference equation is Romer's differential equation exactly. The one over
one plus n is the entire difference between the discrete convention and the continuous one.

So: use continuous time for anything analytic — every proof in the next act is cleaner in it.
Use discrete time for anything you simulate or match to annual data. And always say which one
you are in.

[pause]

One more thing worth noticing about the continuous-time route, because it is a general
technique rather than a trick for this model.

What we did was take a ratio — capital divided by labour — and differentiate it. And the
result had a very particular shape: the growth rate of the ratio is the growth rate of the
numerator, minus the growth rate of the denominator.

That is the rule from the last session, appearing again. The minus n k term in our equation is
not some special feature of capital. It is the denominator growing, and it would appear in
exactly the same way for any per-worker variable you cared to track.

Which is why, when we introduce technological progress next session and start measuring things
per *efficiency unit* rather than per worker, the same term reappears with g added to it. Same
algebra, different denominator.

## BeatGrowthRate - 135 s

One more rearrangement, and it is the one that shows you what the model is really about.

Take the continuous-time equation and divide the whole thing by k.

On the left you get k-dot over k — the **growth rate** of capital per worker. On the right, s
times f of k over k, minus the quantity delta plus n.

[pause]

Now think about what that right-hand side looks like as a function of k.

The second term is a constant. The first term, for Cobb-Douglas, is s times k to the power
alpha minus one — and that exponent is negative, so the term is **strictly decreasing** in k.

So the growth rate of capital per worker is a falling curve, crossing a flat line.

[pause]

That picture *is* conditional convergence. Not a metaphor for it — it is the thing itself. The
poorer the economy, the smaller its k, the higher that curve, the faster it grows. As it
accumulates, growth falls monotonically towards zero.

And one free corollary, which you will use constantly. For Cobb-Douglas, output per worker is
k to the alpha. So the growth rate of output per worker is **alpha times** the growth rate of
capital per worker.

Output always grows more slowly than capital during a transition, and the factor is exactly
the capital share. With alpha a third, capital growing at three per cent means output growing
at one.

[pause]

And this form is also what the empirical literature actually estimates.

A growth regression takes the growth rate of a country's output and puts it on the left-hand
side, with the country's income level on the right, and asks whether the coefficient is
negative. This equation is the theoretical object that regression is trying to recover.

So the falling curve is not just a nice way to see convergence. It is the model's prediction,
in exactly the form the data can be confronted with. We derive the confrontation properly in
session three — and, as you might now suspect, it does not go well for the basic model.

## BeatDiagram - 110 s

Let us draw the picture the entire session lives in.

Horizontal axis: capital per worker. Vertical axis: output and investment per worker, in the
same units.

First the production function, f of k. It rises, it is concave — steep at the start, flattening
out. That flattening is diminishing returns, drawn.

[pause]

Now actual investment, which is s times f of k. That is the same curve, scaled down by the
saving rate. Same shape, same flattening, just lower.

And now the line that makes the model work: break-even investment, delta plus n, times k.
A straight line through the origin.

[pause]

Why is that the right name, and why those two terms added together?

Break-even investment is what you must invest just to hold capital per worker *still*. And
there are exactly two reasons it moves without you: machines wear out, at rate delta. And new
workers arrive, at rate n, who must be equipped with machines of their own or the average
falls.

Delta k replaces what broke. n k equips the newcomers. Both drain the same pool, so they add.

[pause]

And notice the consequence: **delta and n enter identically.** In this model a rise in the
depreciation rate and an equal rise in the population growth rate are literally the same
experiment. The model cannot tell them apart, and neither can you, from anything it predicts.

Now look at the two shapes. A concave curve starting steep, and a straight line. Near zero the
curve is above the line, so investment beats break-even and capital grows. Far out, the curve
has flattened and the line has not, so break-even beats investment and capital shrinks.

Somewhere in between, they cross.

## BeatClosedForm - 120 s

Let us find that crossing exactly.

A steady state is a positive k at which the change is zero. So s times f of k equals delta plus
n, times k.

With Cobb-Douglas, f of k is k to the alpha, so: s k to the alpha equals delta plus n, times k.

[pause]

Divide both sides by k. On the left, k to the alpha divided by k is k to the alpha minus one.

So k to the alpha minus one equals delta plus n, over s.

Flip both sides — remembering that flipping turns the exponent alpha minus one into one minus
alpha:

**k at the steady state equals s over delta plus n, all raised to the power one over one minus
alpha.**

And since output per worker is k to the alpha, output at the steady state is the same bracket
raised to **alpha over one minus alpha**. Consumption is one minus s, times that.

[pause]

Now do not memorise those exponents. Read them.

One over one minus alpha, with alpha a third, is one point five. So doubling the saving rate
multiplies steady-state capital by two to the one point five — about two point eight.

Alpha over one minus alpha, with alpha a third, is one half. So that same doubling multiplies
steady-state **output** by two to the one half. About one point four.

[pause]

Capital nearly triples; output rises by forty per cent. Why the difference? Diminishing
returns. You piled on the machines and each one did less than the last.

That number — one half — is the single most important elasticity in this session. It is how
much richer a country gets when it saves proportionally more. Remember it, because in the last
act we are going to point it at Brazil, and it is going to fail.

## BeatExistence - 155 s

Kurlat argues that the economy converges by pointing at the diagram: above the crossing the
curve is below the line, so capital falls; below it, the reverse. That is correct, and it is
not a proof.

A picture does not rule out the curve and the line crossing three times. A picture does not
rule out the economy leaping over the crossing point and diverging. Let us supply what the
picture assumes, because this is where those two separate assumptions finally do their
separate jobs.

[pause]

Define excess investment, phi of k, as actual investment minus break-even investment. A steady
state is a positive root of phi.

**Existence first.** Look at phi divided by k — that is s times f of k over k, minus delta plus
n.

As k goes to zero: what is the limit of f of k over k? Since f of zero is zero, that is a
zero-over-zero, and L'Hôpital says it equals the limit of f prime. Which, by the **first Inada
condition**, is infinity.

So near zero, phi over k is enormous and positive. Excess investment is positive.

[pause]

As k goes to infinity: the limit of f of k over k is again the limit of f prime, which by the
**second Inada condition** is zero. So phi over k tends to minus delta plus n. Negative.

Now: phi is continuous. It is positive somewhere. It is negative somewhere else. By the
intermediate value theorem, it is zero somewhere in between.

**Existence is exactly the two Inada conditions.** Not diminishing returns — Inada. That is
what they were for.

[pause]

It is worth pausing on how much work that theorem just did, because it is easy to miss.

We did not assume a steady state exists. We did not assume the diagram looks the way it looks.
We assumed something about the *slope of the production function at two extremes* — infinitely
steep at zero, flat at infinity — and existence followed from continuity alone.

That is the shape of a good economic proof: an assumption about behaviour at the boundaries,
plus a theorem from analysis, gives you a result about the interior.

And it tells you exactly what to check if someone hands you a production function you have not
seen before. Do not squint at the diagram. Check the two limits.

## BeatUniqueness - 155 s

But existence is not enough. We need to know there is only *one* crossing, or "the steady
state" is not a well-defined object.

The claim: f of k over k is strictly decreasing.

Differentiate it with the quotient rule. The derivative is f prime of k, times k, minus f of
k — all over k squared.

The denominator is positive. So the sign is the sign of that numerator: f prime times k, minus
f of k.

[pause]

And here is the geometric fact that settles it. For a strictly concave function through the
origin, the **chord from the origin lies above the tangent**. Which says exactly that f of k
is greater than f prime of k times k.

If you want it without the picture: f of k minus f of zero is the integral of f prime from
zero to k. And since f prime is strictly decreasing, every value of f prime inside that
integral is *larger* than f prime at the endpoint k. So the integral exceeds k times f prime
of k.

Either way, the numerator is negative. So f of k over k falls, strictly, everywhere.

[pause]

And now finish. Actual investment over capital, s times f of k over k, is strictly decreasing.
Break-even over capital, delta plus n, is a constant. A strictly decreasing function crosses a
constant **at most once**.

**Uniqueness is exactly diminishing returns.**

So there it is: Inada gives you at least one crossing, concavity gives you at most one.
Together, exactly one. Two assumptions, two halves of one theorem — and that is why Kurlat was
careful to say neither implies the other.

[pause]

There is a way to see the same thing that is worth carrying, because it generalises.

Average product is f of k over k — output per unit of capital. Marginal product is f prime of
k — the output from one more unit. For a concave function through the origin, the average
always exceeds the marginal, because every earlier unit was more productive than the last one.

And that is precisely the inequality we just proved. The average product exceeds the marginal
product; therefore the average product is falling; therefore it crosses any constant once.

Average above marginal, average falling. The same relationship you meet in a cost curve, doing
the same job here.

## BeatAK - 115 s

Let us see what happens when you take diminishing returns away. This is the most instructive
thing in the session.

Suppose output per worker were simply proportional to capital per worker: f of k equals a
times k. A straight line. Positive marginal product, so assumption two holds. But the second
derivative is zero — **no diminishing returns**, and no Inada conditions either.

[pause]

Now excess investment is s a k, minus delta plus n, times k. Factor out the k: it is s a, minus
delta plus n, all times k.

Look at that. It is proportional to k. It is a straight line through the origin.

And a straight line through the origin has **no positive root**. The two lines we are trying to
cross are now both straight lines through the origin — so either one is always above the other,
or they lie on top of each other. There is no crossing.

[pause]

So what happens? If s a exceeds delta plus n, capital per worker grows at a constant rate,
forever. No steady state, no convergence, no limit. And if s a is less than delta plus n, the
economy shrinks to nothing.

That is the **AK model**, and it is the simplest model of endogenous growth. Notice what it
does that Solow cannot: in the AK model, raising the saving rate raises the growth rate
**permanently**.

[pause]

Which tells you something important about the result we are heading towards. When I say in a
few minutes that saving more cannot raise long-run growth, that is not a deep truth about the
universe. It is a consequence of assumption four point three — diminishing returns — and
nothing else. Drop that one assumption and the conclusion reverses completely.

## BeatStability - 140 s

We know the crossing exists and is unique. Does the economy actually get there?

**In continuous time, here is the proof.** We just showed that s times f of k over k is
strictly decreasing, and by definition it equals delta plus n exactly at the steady state.

So if k is below the steady state, that expression is **above** delta plus n, which means
k-dot is positive: capital rises.

And if k is above, it is below, so k-dot is negative: capital falls.

[pause]

So capital per worker moves monotonically towards the steady state and is bounded by it. A
monotone bounded sequence converges. And whatever it converges to must be a rest point, of
which there is exactly one.

That is a complete proof, and notice what the picture was quietly supplying: **capital never
overshoots.** In continuous time it cannot.

[pause]

In discrete time that is not automatic, and it is worth thirty seconds. The map is k next
period equals a function G of k today. Convergence needs the slope of G at the steady state to
be less than one **in absolute value** — a negative slope below minus one would oscillate and
explode.

Differentiate: G prime is one minus delta, plus s f prime of k, all over one plus n. Every term
is positive, so G is increasing — the path cannot oscillate at all.

And at the steady state, that slope works out to be less than one precisely when **alpha times
delta plus n is less than delta plus n** — which holds for any alpha below one. Assumption
three again, doing the work again.

[pause]

Finally, the speed. Linearise around the steady state and deviations decay at a rate of **one
minus alpha, times delta plus n**.

Put the numbers in: two thirds, times six per cent, is **four per cent a year**. Which means a
half-life of about **seventeen years**.

Seventeen years to close half the remaining gap. Hold that number — in the last act it is going
to change what "the model converges" actually means for a country.
## BeatCompStatics - 135 s

Now we can ask the question the model was built for. What happens if a country saves more?

We could just differentiate the closed form, but let us do it the general way, because it works
for any production function.

The steady state is defined by excess investment being zero. Differentiate that condition
implicitly with respect to s.

[pause]

You get: the change in steady-state capital, with respect to s, equals f of k — divided by
minus the slope of phi at the steady state.

And we computed that slope in the last beat: it is minus one minus alpha, times delta plus n.
Negative. So with the minus sign in front, the whole thing is **positive**.

More saving, more capital per worker in the long run. As you would expect — but now derived,
and with a magnitude attached.

[pause]

Do the same for population growth and for depreciation. Both give you the same expression:
minus k, over one minus alpha times delta plus n. **Negative**, and — look carefully —
**identical to each other**. Exactly as the diagram told us. To this model, n and delta are the
same parameter wearing two names.

[pause]

Now in elasticity form, which is how to actually remember them. Straight from the closed form:
a one per cent rise in the saving rate raises steady-state capital by one over one minus alpha
per cent, and steady-state output by **alpha over one minus alpha** per cent. Our one half.

And here is the table. Saving up: capital up, output up. Population growth up: both down.
Depreciation up: both down.

[pause]

And then the final column, which is the entire point of this act. **Long-run growth of output
per worker.** Saving up: zero. Population growth up: zero. Depreciation up: zero.

Zero in every row. Whatever you do to the parameters of this model, the long-run growth rate of
output per worker is zero. Always. You can change where the economy ends up. You cannot change
the fact that it ends up somewhere and stops.

## BeatTransition - 150 s

"Zero in the long run" invites an obvious objection: so nothing happens? Of course something
happens. Let us compute exactly what.

The economy is sitting at its steady state. At some date, the saving rate rises permanently,
from s-nought to s-one.

[pause]

**On impact.** Capital is a **stock**. It is the accumulated result of the entire past, and it
cannot jump. So on the day of the change, capital per worker is exactly what it was yesterday.

Output is a function of capital, so output does not jump either.

But investment jumps immediately — the same output, a bigger slice saved. So k-dot leaps from
zero to s-one minus s-nought, times f of k. Capital starts growing at once, at a rate
proportional to how much the saving rate rose.

And one thing *does* jump, discretely and downwards: **consumption**. Consumption is one minus
s, times output, and s just rose while output did not. The country is immediately poorer in
consumption terms. That is the price of the transition, paid on day one.

[pause]

**During the transition.** The growth rate of output per worker is alpha times the growth rate
of capital, which is alpha times the bracket we plotted earlier. It starts positive. And
because f of k over k is strictly decreasing, it falls — monotonically — back to zero.

So growth **spikes, and decays**. At rate lambda: the four per cent a year we derived, with its
seventeen-year half-life.

[pause]

**In the new steady state.** Growth is zero again. But the level is permanently higher, by
alpha over one minus alpha, times the log of the ratio of the saving rates.

[pause]

And now the identity that makes the whole distinction precise. Integrate the growth rate over
the entire transition, from the moment of the change to infinity. What do you get?

You get exactly the permanent change in the log level.

**The area under the growth spike is the level gain.** That is what a level effect *is*: a
finite area under a temporary bump in the growth rate. A rate effect would be a permanent shift
in the growth rate, and the area under *that* is infinite.

They are not two ways of describing the same thing. One integral converges and the other does
not.

## BeatNumbers - 105 s

Let us put numbers on it, because "a level effect" sounds small and abstract until you price
it.

Alpha, one third. Depreciation, five per cent. Population growth, one per cent. And the saving
rate rises permanently from twenty per cent to twenty-five — a substantial, politically
difficult increase.

[pause]

The level gain is one half, times the log of one point two five. That is nought point one one
two, which in levels is about **eleven and a half per cent** more output per worker. Forever.

The half-life is seventeen years, so it takes about thirty-five years to get three quarters of
the way there.

And the peak growth rate — the highest the growth rate ever reaches, on the very first day — is
about **half a per cent a year**, decaying from there.

[pause]

So here is the honest answer to "should a country save more?", inside this model.

Yes. It ends up permanently richer, by about a tenth. It pays for that with an immediate fall
in consumption, and it waits a generation to collect. And at no point does its growth rate rise
by even one full percentage point.

That is a real gain, and it is nothing like the thing people mean when they talk about a
country that "grew fast for thirty years". Eleven per cent is what accumulation buys. Korea
went up by a factor of ten.

[pause]

Whether that trade — less consumption now, more output later — is even worth making, the model
has so far not said. Which brings us to the one entry in the table I left blank.

## BeatConsumption - 100 s

I signed capital and output. I did not sign consumption, and that was deliberate.

Steady-state consumption is one minus s, times f of k at the steady state. And s appears twice,
pulling in opposite directions. A higher s raises capital, so it raises f of k — more output to
divide. But it also takes a bigger slice of that output for investment.

Which wins?

[pause]

Differentiate. The change in steady-state consumption with respect to s is: minus f of k, plus
one minus s, times f prime, times the change in capital with respect to s.

Substitute the expression we derived two beats ago, use the steady-state condition to
eliminate s, and it all simplifies to a criterion of startling cleanliness:

**Steady-state consumption rises with saving if and only if the marginal product of capital
exceeds delta plus n.**

[pause]

Look at what that says. Invest more only while the extra machine produces more than it costs to
keep the capital stock intact. Exactly the condition any sensible person would write down.

And now notice something genuinely strange about where it came from. This model contains **no
optimising agent**. Nobody in it maximises anything. The saving rate is a parameter handed down
from outside. And yet we have just derived a welfare criterion — because steady-state
consumption happens to be a well-defined function of that parameter, and we can ask where it
peaks.

That inequality has a name. It is the **Golden Rule**, and chasing it down is where session
three begins.

## BeatBrazil - 145 s

So we have a complete model. It has a unique steady state, it is globally stable, and we can
sign every comparative static. Let us point it at the question it was built for.

Why is Brazil poorer than the United States?

[pause]

The model's answer is available to us. Steady-state output depends on the saving rate and on
delta plus n, through that elasticity of one half. So take the ratio of the two countries'
steady states, and everything else cancels.

Brazil invests eighteen point three per cent of GDP, averaged over the last two decades. The
United States, twenty-one point three.

[pause]

Divide. Brazil's investment rate is about eighty-six per cent of America's. Now raise that to
the power one half — because output responds by the **square root**, that is what an elasticity
of a half means.

The square root of nought point eight six is nought point nine three.

Add population growth: Brazil's is slightly higher, at nought point eight six per cent against
nought point seven eight. Put that in too, and the prediction moves to nought point nine two.

[pause]

**The model predicts that Brazilian income per head should be ninety-two per cent of American
income per head.**

The measured figure is **twenty-five point seven per cent**.

[pause]

The model is out by a factor of three and a half. Not fifteen per cent. Not a bit. Three and a
half times.

And you can run it backwards to see how bad this is. What investment rate would Brazil need
for saving alone to explain the gap? Invert the closed form, and the answer is **one point four
per cent of GDP**. Brazil would have to invest essentially nothing, for decades, to be as poor
as Brazil actually is.

[pause]

So capital accumulation does not explain why countries are poor. And notice that this is not a
failure of arithmetic, or of calibration, or of data. It is the elasticity. One half is a small
number, and it is small **because of diminishing returns** — the very assumption that gave us
existence, uniqueness, stability and convergence.

The assumption that makes the model work is the assumption that makes it fail.

## BeatClose - 105 s

So here is where we stand.

We built a model from eight assumptions. We derived its law of motion line by line. We proved
its steady state exists — that was Inada. We proved it is unique — that was diminishing
returns. We proved the economy gets there, monotonically, at about four per cent a year.

And we showed that within it, saving more is a level effect and never a rate effect. That the
area under the growth spike is finite, and equals the permanent gain in the log level.

[pause]

Then we pointed it at two countries, and it missed by a factor of three and a half.

[pause]

Hold this frame. The diagram you can already draw — two curves, one crossing — and beside it
two dots. Where the model puts Brazil, at ninety-two per cent of the United States. And where
Brazil is, at twenty-six.

The distance between those dots is what session three is about.

Because there are only two ways out. Either the differences in saving rates are somehow much
larger than they look — and we have just checked that they are not — or something *else*
differs across countries, something that is not capital at all, and that does most of the
explaining.

And there is a second failure we have not even addressed. Kaldor's very first fact was that
output per person grows at a constant positive rate, forever. This model's steady state has it
growing at **zero**. The model fails its own first target.

Both problems have one answer, and it is the same answer. Next session: technology.
