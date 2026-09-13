# Script - Aula 7, Money and Inflation

Narration exactly as sent to text-to-speech. Durations are measured from the
synthesised audio and live in `beats.json`; nothing here is timed by hand.

Length is uncapped by request: this is the whole lecture, not a slice.

## Act I - Why money demand exists, and the number inside it

### BeatOne - The miss

*275 words, about 110 s at 150 words per minute.*

Here is a central bank with a simple job. It wants inflation of two per cent a year. Its economy is growing at three per cent. It knows the relationship between money and prices, it controls the money supply exactly, and it sets money growth at three and a half per cent a year.

Inflation comes out at half a per cent.

It missed its target by one and a half percentage points. And notice what did not happen. There was no financial crisis. No oil shock. No war. Nobody lost control of the printing press. The bank hit its money growth target precisely, to the decimal.

So it did everything right, and it still missed. What did it get wrong?

The answer is a single number. Not a model, not a regime, not a judgement call. One number, which the bank had to assume because it cannot be observed directly, and which it assumed wrongly.

By the end of this video you will know what that number is, why its correct value is one half rather than one, and why getting it wrong costs exactly one and a half points of inflation in an economy growing at three per cent.

We are going to get there the long way, because the number is not arbitrary. It falls out of a question that sounds unrelated. Why would anyone hold money at all? Money pays no interest. Bonds do. Savings accounts do. Holding cash is, on its face, a choice to be poorer. And yet everyone does it.

Answer that question properly and the number appears, with its value, and with a reason. Let's start there.

### BeatTwo - The sawtooth

*333 words, about 133 s at 150 words per minute.*

Take a household that will spend some amount over the course of a year. Call the quantity of goods it buys Y, and the price of those goods p, so in money terms it spends p times Y over the year.

It does not spend it all at once. It spends evenly, a little every day.

Every payment has to be made with money. But that does not mean the household needs to hold the whole year's spending in cash on the first of January. It can keep most of its wealth in something that pays interest, and go to the bank when it needs more money.

Going to the bank does not have to mean walking into a branch. It can be a cash machine. It can be selling a bond in a brokerage account and moving the proceeds into a chequing account. What matters is that each trip costs something: a fee, or time, or simply the mental effort of dealing with it. Call that fixed cost F, and let it be the same for every trip.

So the household has one choice to make. How many times a year to go to the bank. Call that number N.

Watch what its money holdings look like across the year. Each time it goes to the bank it brings its balance up to the year's spending divided by N. Then the balance slides down in a straight line as it spends, until it reaches zero, and it goes again.

That is a sawtooth. Two trips a year, and each tooth is half the year's spending, sliding to nothing.

Now make it four trips. The teeth are half as tall, and there are twice as many of them.

Look at the average height. The balance falls linearly from its peak to zero, so the average is exactly half the peak. Average money holdings are the year's spending divided by two N.

More trips, smaller balances. That is the first half of a trade-off.

### BeatThree - The trade-off, solved

*390 words, about 156 s at 150 words per minute.*

So why not go to the bank every day, and hold almost no money at all?

Because the trips cost F each. Go N times and you pay F, N times over. In money terms that is p times F times N. That cost rises in a straight line as the number of trips increases. More trips, more cost, with no limit.

Now the other side. Holding money costs something too, and it is not a fee, it is a foregone return. The money sitting in your pocket could have been a bond earning the nominal interest rate i. So every unit of value you hold as money costs you i. And we know how much you hold on average: the year's spending over two N. So the interest you give up is i times the year's spending over two N.

That cost falls as the number of trips rises, and it falls as a hyperbola. Steeply at first, then flattening, approaching zero without ever reaching it.

Add the two together. A line rising and a hyperbola falling give a U shape. There is a minimum, and the household sits at the bottom of it.

Let's find it. Take the total cost, differentiate with respect to N, and set the derivative to zero. The first order condition reads: p times F, minus i times p times Y over two, divided by N squared, equals zero.

Solve for N. The optimal number of trips is the square root of the quantity i times Y, over two F.

Read that before we move on, because it already says something. The number of trips rises with the interest rate: when holding money is expensive, you go to the bank more often. And it falls with F: when trips are expensive, you go less often. Both are what you would expect, which is a good sign that the algebra is describing the world.

Now substitute it back. Put the optimal number of trips into average money holdings, and divide through by the price level to get real money balances, which is to say the quantity of goods your money could buy.

What comes out is this. Real money balances equal the square root of Y times F, over two times i.

That is money demand. Not assumed. Derived, from a household minimising a cost.

### BeatFour - The elasticity is one half

*308 words, about 123 s at 150 words per minute.*

Now look hard at that square root, because the number we have been promising is sitting inside it.

Real money demand is proportional to the square root of income. Not to income. To its square root.

Put that on logarithmic axes and it is a straight line with slope one half. That slope is the income elasticity of money demand. It answers the question: if income rises by one per cent, by what per cent does money demand rise? The answer is half a per cent.

Here is what that means concretely. Double your income and you do not double your cash. You multiply it by the square root of two, which is about one point four one. Forty one per cent more cash for one hundred per cent more income.

Why? Because you have another margin available. When your spending doubles you do not have to carry twice as much cash. You can go to the bank more often instead. And the model says you do exactly that, because the optimal number of trips also rises with the square root of income. There are economies of scale in managing cash, and one half is their measure.

Now contrast that with the guess almost everyone makes first. The older Cambridge formulation says money demand is simply proportional to income. Hold some fixed fraction of your income as cash. That makes the elasticity one, not one half.

These are not two settings of a dial. They are two different claims about how households behave. One says cash management has economies of scale. The other says it does not. Baumol and Tobin derived the first from a cost minimisation. The second was an assumption.

One half against one. That is the number our central bank had to guess at. We now know where it comes from and what it means.

### BeatFive - What counts as money

*473 words, about 189 s at 150 words per minute.*

We have been saying the word money for five minutes without defining it. That was deliberate. A definition handed over before you want it is a definition you forget. Now you want it, because the model we just built has a quantity of money in it, and somebody has to measure that quantity.

So what is money? The standard answer gives three functions. It is a store of value: you can hold it and use it later. It is a unit of account: we quote prices in it. And it is a medium of exchange: it changes hands when people pay for things.

Only the third one is doing real work. Plenty of things store value. Plenty of things could serve as a unit of account. What makes money money is that it is handed over in payment, and the reason that matters is the double coincidence of wants. Without money, to trade I must find someone who has exactly what I want and who wants exactly what I have. That is a demanding coincidence and it usually fails. With money, I take payment for what I sell knowing that others will take the same money for what I want to buy.

For something to work as money it needs several properties. It has to be hard to counterfeit, or the seller spends every transaction wondering. It has to be easy to carry, because transactions happen everywhere. It has to be durable, which is why coffee beans make better money than strawberries. It has to be divisible, so you can pay the exact price and make change. And it has to be commonly accepted, which is sometimes a social convention and sometimes written into law.

Now here is the consequence, and it is the reason measurement is awkward. Those properties are satisfied by degrees, not yes or no. There is no sharp line between money and not money. So there is no single correct measure of how much money an economy has.

What exists instead is a ladder. At the bottom, physical currency alone. Add demand deposits, the chequing accounts you can write a cheque against, and you have the measure that matters for transactions. Add savings deposits, small time deposits and money market fund shares, and you have a broader one. Each rung is slightly less usable in a transaction than the one below it.

And off to one side sits a different object: the monetary base, which is physical currency plus the reserves that commercial banks keep at the central bank. It is not a smaller version of the transactions measure. It is the part of money the central bank issues directly. Which raises the obvious question, and it is the one for the next three beats. If the central bank only issues the base, how does it control anything else?

## Act II - Where money actually comes from

### BeatSix - Where money comes from

*455 words, about 182 s at 150 words per minute.*

To answer that, you need to look at a bank's balance sheet, because deposits are a bank's liability and deposits are most of the money.

On the left, the bank's assets. Loans it has made. Government bonds it holds. And one that will matter to us: reserves, which are simply deposits the bank itself keeps at the central bank. The central bank is a bank for banks. Reserves are an asset for the commercial bank and a liability for the central bank, and typically they pay no interest or very little.

On the right, the bank's liabilities. Mostly deposits. And underneath, net worth, which is just assets minus liabilities.

Now, if reserves pay nothing, why hold them? Two reasons, and their relative weight has changed over history. The first is to meet unexpected withdrawals, because most bank assets are long term and hard to sell quickly, while reserves convert to cash immediately. That mattered more before deposit insurance made runs rare. The second reason is the one that binds today: regulation requires it. Banks must hold reserves equal to some fraction of their deposits.

Hold on to that, because everything in the next beat depends on banks wanting to hold as few reserves as the rule allows.

Now watch the central bank change the money supply, the traditional way. It buys government bonds from a commercial bank, and it pays by creating reserves and crediting them to that bank. Those reserves did not exist a moment ago. That is an open market operation, so called because the central bank is trading in the open market like anyone else.

The bank now holds more reserves than the rule requires. It has excess reserves earning nothing, so it lends them out. It writes a loan, the borrower deposits the proceeds, and deposits have just increased.

Now correct the story everyone gets wrong here. The reserves did not leave. They are still sitting on a balance sheet. What happened is that the banking system took advantage of having slack against its reserve requirement and expanded loans and deposits until the slack was gone. And notice that nobody's net worth changed anywhere in this sequence. Assets and liabilities were swapped around, and no one got richer. If your arithmetic makes somebody richer, your arithmetic is wrong.

One more step. Some fraction of those new deposits gets withdrawn as cash. The bank asks the central bank for notes, and the central bank hands them over and debits the bank's reserves. So part of the new money leaks out of the deposit system and into wallets.

And now the process repeats, smaller, because the deposits that remain still carry a reserve requirement. Which is exactly the structure of a geometric series.

### BeatSeven - The multiplier

*408 words, about 163 s at 150 words per minute.*

Let's sum it.

Each round is the previous round scaled down by a factor. Two things shrink it. A fraction of new deposits has to be held as reserves, so that much cannot be lent again. And a fraction of new money walks out as cash, which leaves the deposit system entirely.

Call the reserve fraction theta and the cash fraction gamma. Then each round is the one before it multiplied by one minus theta, times one minus gamma.

A geometric series with a ratio less than one sums to a finite number. Stack the rounds on screen and watch them converge: the first round is the full injection, the second is a fraction of it, the third a fraction of that, and the total settles.

When you do the algebra, the ratio of the change in the transactions measure of money to the change in the monetary base is one over the quantity theta plus gamma minus theta gamma.

That is the money multiplier. Say the denominator carefully, because it is easy to garble: theta plus gamma minus theta gamma.

It is called a multiplier because the central bank moves the base, which it controls directly, and the transactions measure of money moves by the base times this number.

Now look at what it depends on, because the difference between its two arguments matters more than the formula. Theta, the reserve ratio, is largely a policy choice: the central bank sets the legal requirement. Gamma, the fraction of money people want to carry as cash, is not a policy choice at all. It moves with payment technology and with public confidence in banks.

So one argument is an instrument and the other is behaviour. That asymmetry is why we can say, loosely, that the central bank controls the money supply, and it is also why that statement needs an asterisk. What the central bank controls directly is the base. It controls the broader measure only through a multiplier it does not fully own.

One note on notation, because you will see this written differently. Your topic rules file writes the multiplier with the currency to deposit ratio, as one plus that ratio over the reserve ratio plus that ratio. The book writes it with gamma as the cash share of the money stock. Both are right under their own definitions and they give different numbers for the same economy. Pick one, say which, and stay with it.

### BeatEight - Where the multiplier breaks

*373 words, about 149 s at 150 words per minute.*

Every step of that derivation rested on one assumption, and it was stated out loud: banks hold the minimum reserves the rule allows, because reserves earn nothing while loans earn something.

So ask what happens when that stops being true.

Suppose the interest rate falls to zero. Or suppose the central bank starts paying interest on reserves at something close to the market rate. Now reserves are no longer the worst asset a bank can hold. A bank handed new reserves has no particular reason to lend them out. It can simply keep them.

And if the new reserves are simply kept, the chain we just built never starts. Round two never happens. Changes in the monetary base stop passing through to the money people actually transact with.

This is not a thought experiment. Look at the United States from late two thousand and eight. Nominal interest rates fell to almost zero, and at around the same time the Federal Reserve began paying interest on excess reserves. Reserves became an attractive asset, and banks began holding them in enormous quantity.

Here is what happened to the two series. The monetary base rose almost fivefold. The transactions measure of money rose far less. And the multiplier between them fell from about two to below one.

Below one. A multiplier that is less than one is a strange object if you think of it as an amplifier. It means the economy ended up with less transactional money than the base that supposedly supports it, because so much of the base was sitting idle as reserves rather than circulating as deposits.

Now be careful about what this does and does not overturn. It does not refute the accounting. It refutes a behavioural assumption, and with it the idea that the central bank has reliable indirect control of the money stock through the base. That is one of the practical reasons modern central banks talk about an interest rate rather than a quantity of money, and we will see the other reason in a few beats.

What it means for everything that follows is this. When a model says the central bank chooses the money supply, that is a modelling convenience. Keep a note in the margin.

## Act III - The equilibrium, and the law

### BeatNine - What adjusts

*369 words, about 148 s at 150 words per minute.*

Money demand is one side of the market and the money supply is the other. Now let's close it.

Equilibrium in the money market means the money that the central bank and the banking system created is exactly the money that people are willing to hold. Voluntarily. Nobody is forced to hold money.

Write it down. The money supply equals real money demand, which depends on income and the nominal interest rate, multiplied by the price level.

Now ask the question the whole chapter turns on. The central bank raises the money supply. The left hand side goes up. What on the right hand side moves to restore the equality?

There are exactly three candidates, and only three. The price level can rise, because higher prices mean the same real transactions need more money. The nominal interest rate can fall, because that makes money cheaper to hold, so people hold more of it. Or income can rise, because that means more transactions to carry out.

Three arrows. Look at them, because which one moves is the most consequential question in monetary economics, and this chapter answers it by assumption rather than by argument.

Here is the assumption, and it has a name: the classical view. Real quantities are settled by real forces. Technology, preferences, endowments. Money does not enter that determination at all. So income is fixed by things that have nothing to do with the money supply, and the real interest rate is fixed the same way.

Two arrows grey out.

What is left is the price level. And notice this is not an extra assumption bolted on at the end. It is simply what remains when the other two doors are shut. That is the whole content of the phrase money is neutral: it can move nominal things, and there is nothing nominal left for it to move except the price level.

Be honest about the status of this. We have not proved that money is neutral. We assumed that real variables are determined by real forces, and neutrality followed. Everything for the rest of this video is a consequence of that assumption, and in the last beat we will take it away and watch what breaks.

### BeatTen - The law

*479 words, about 192 s at 150 words per minute.*

Now let the economy grow, and find the inflation rate.

Income grows at rate g. The money supply grows at rate mu. The real interest rate is constant. We want to know what inflation has to be.

Start from the equilibrium condition and differentiate both sides with respect to time.

The left side gives the rate of change of the money supply. The right side is a product of two things, and one of them, money demand, itself depends on two moving arguments. So the derivative has three pieces. The response of money demand to income, times the rate of change of income. Plus the response of money demand to the interest rate, times the rate of change of the interest rate. Both of those multiplied by the price level. Plus money demand itself, times the rate of change of the price level.

Now divide every term by the equilibrium condition. This is the step that does the work, so watch it: dividing a rate of change by a level turns it into a growth rate. Levels disappear and growth rates appear.

On the left, the growth rate of the money supply. That is mu.

On the right, three terms. The first one contains the response of money demand to income, multiplied by income, divided by money demand. That combination is an elasticity: the percentage change in money demand for a one per cent change in income. It is exactly the number we derived from the square root. Call it eta. So the first term is eta times g.

The second term involves the rate of change of the nominal interest rate.

The third is the growth rate of the price level, which is inflation.

Now kill the middle term, and notice why we are entitled to. If inflation is constant, then the nominal interest rate is the real rate plus a constant, so it is constant too, so its rate of change is zero. The whole term vanishes.

What remains is clean. Mu equals eta times g, plus inflation.

Rearrange, and there is the law of this lecture. Inflation equals mu minus eta times g.

Read it twice. Inflation is money growth, minus the income elasticity of money demand, times output growth.

And check the logic closed properly: we assumed inflation was constant in order to drop a term, and the formula returns a constant, because mu, eta and g are all constants. The conjecture verifies itself.

Two things to understand before we use it. First, why growth lowers inflation: a growing economy makes more transactions, so it wants more real money, so it absorbs new money that would otherwise have bid up prices. Second, why eta is in there at all: eta is the exchange rate between growth and absorbable money. The larger it is, the more money growth the real economy can soak up for free.

### BeatEleven - Back to the miss

*361 words, about 144 s at 150 words per minute.*

Now we can return to the opening and see exactly what happened.

Inflation equals money growth minus the elasticity times output growth.

Our central bank wanted inflation of two per cent. Its economy grows at three per cent. And it believed the elasticity was one half, because it believed Baumol and Tobin.

So it solved for money growth: the inflation target, plus the elasticity times the growth rate. Two, plus one half of three. Three and a half per cent. Had its belief been right, it would have hit two per cent exactly.

But suppose the truth is the Cambridge version, and the true elasticity is one.

Run the same formula with the truth. Inflation equals three and a half, minus one times three. Half a per cent.

There is the miss. Not two per cent but half a per cent, one and a half points below target.

And look where those one and a half points came from. The bank assumed one half; the truth was one; so it was wrong by one half. Multiply that error by the growth rate of three per cent and you get one and a half points.

The inflation error equals the error in the elasticity, multiplied by the growth rate of the economy. That is the entire story of the opening, in one line.

Notice the direction, because it is not obvious. Underestimating the elasticity means underestimating how much extra money a growing economy wants to hold. The economy absorbed more of the new money than the bank expected, so less of it was left to bid prices up. The error shows up as inflation coming in too low, not too high.

And notice what this costs a central bank that targets a monetary aggregate. Perfect control of the money stock does not buy you control of inflation. You also need a number you cannot observe directly, and that financial innovation keeps moving underneath you. Put that next to what we saw in two thousand and eight, where the link from the base to the money stock came apart, and you have most of the practical case for targeting an interest rate instead.

### BeatTwelve - Two experiments

*432 words, about 173 s at 150 words per minute.*

The law tells you about steady growth. Now do two experiments that are not about steady growth, because the second one is the subtlest thing in the chapter.

Experiment one. The economy sits in a steady state with a constant money supply and therefore a constant price level. At some moment the central bank raises the money supply once, unexpectedly, permanently, and then holds it at the new level forever.

Before, the price level was the money supply divided by real money demand. After, we are back in a constant money supply steady state, with a bigger numerator and the same denominator. So take the ratio: the new price level over the old equals the new money supply over the old.

Prices jump, once, in exact proportion. On screen, a flat line that steps up and stays flat. Nothing real happens. That is neutrality in its cleanest form.

And the mechanism is worth saying out loud, because it is better than the algebra. Everyone suddenly holds more money than they want, so everyone tries to spend it down. But they cannot all succeed, because somebody has to hold the money. Everyone realises this at once, so money loses value, and money losing value is precisely what a higher price level means.

Experiment two. Now the economy is growing its money supply at some rate, with inflation equal to that rate. At some moment the central bank permanently raises the growth rate.

The naive answer is that inflation rises to the new growth rate. And the book's verdict on that answer is exact: it is not wrong, but it is incomplete.

Follow the chain. If inflation is now higher, then the nominal interest rate is higher, because it is the real rate plus inflation. A higher nominal rate raises the opportunity cost of holding money, so desired real balances fall. People want to hold less real money than before.

But here is the catch. The level of the money supply did not change at that moment. Only its growth rate changed. So if real balances must fall, and the nominal quantity of money has not fallen, what clears the market?

The price level has to jump.

So the correct answer has two parts: inflation rises to the new growth rate, and on top of that the price level makes a one-off jump at the instant of the announcement. On screen, a line with a kink and a step, not just a kink.

That distinction is a favourite examination question, and you can now see why the naive answer is incomplete rather than wrong.

### BeatThirteen - The identity that cannot fail

*422 words, about 169 s at 150 words per minute.*

There is an equation in monetary economics more famous than anything we have derived, and it is time to deal with it.

It says the money stock multiplied by velocity equals the price level multiplied by output. Money times velocity equals nominal output.

Velocity is the number of times a unit of money is used in a period. The textbook example makes it concrete: two dollars in an economy, six transactions of one dollar each over a year, so nominal output is six, the money stock is two, and each dollar changed hands three times. Velocity is three.

Now here is what matters, and it is the single most examinable sentence in this lecture. That equation is a definition. It is true because of the way velocity is defined: velocity is nominal output divided by the money stock. So the equation holds for any data, from any country, in any century, whatever the underlying economics happens to be.

An equation that cannot fail cannot be evidence for anything. You cannot test it. You cannot violate it. Learning that it holds teaches you nothing.

So what does it take to make it a theory? One assumption: that velocity is constant, or at least stable. Add that, and the price level becomes proportional to the money stock, and you have what is called the quantity theory of money. Identity plus a behavioural assumption equals theory. The assumption is where all the content lives.

And now we can interrogate that assumption, because we derived a theory of money demand forty minutes ago.

Use the equilibrium condition to replace the real money stock in the quantity equation and rearrange. What comes out is that velocity equals output divided by real money demand. Which means any theory of money demand is automatically a theory of velocity. They are not independent objects.

So substitute our money demand. Velocity equals output divided by the square root of output times F over twice the interest rate. Simplify, and velocity equals the square root of twice the interest rate times output, over F.

Look at what that says. Velocity rises with the nominal interest rate. It rises with output. It falls with the cost of a trip to the bank. It is not a constant, and it moves exactly when interest rates move, which is exactly when monetary policy is doing something.

So the assumption that converts the famous identity into a theory is contradicted by the model of money demand we built. Not approximately. In precisely the dimension that matters.

## Act IV - Measurement and evidence

### BeatFourteen - Measuring it

*408 words, about 163 s at 150 words per minute.*

We have been saying inflation without measuring it. Measuring it turns out to be the same problem we met in the very first lecture of this course, wearing different clothes.

Inflation is a generalised increase in the level of prices. If every price rose by the same percentage there would be nothing to discuss. The problem is that different prices move by different amounts, and some move in opposite directions. So what is the overall change?

The answer requires choosing a basket: a specific list of quantities of specific goods. Then you measure what that basket costs over time, and the total cost is a price index. Different ways of choosing and updating the basket give different indices, and there is no neutral choice.

Here are the two that matter. The first is the deflator implied by the national accounts: nominal output divided by real output, times one hundred. It weights each good by its share of production.

Work the arithmetic from the lecture. An economy produces wheat and computers. At base year prices the later year's output is worth two thousand five hundred and fifty. At current prices it is worth one thousand eight hundred and sixty. The deflator is the second divided by the first, times one hundred, which is about seventy three. The index started at one hundred, so prices fell by about twenty seven per cent.

The second index weights goods by how much they are consumed rather than produced, using a survey to fix the basket. Here is the lecture's example. Three goods: two cars at one hundred rising to one hundred and fifteen, twenty kilos of caviar at four falling to three, and ten litres of champagne at two rising to four. Total the basket at the old prices: three hundred. Total it at the new prices: three hundred and thirty. So the index goes from one hundred to one hundred and ten, and inflation is ten per cent.

Stop on something in that example. One of the three prices fell. Caviar went from four to three. Inflation of ten per cent is entirely compatible with individual prices falling, because inflation is a statement about an index, never about every price.

And because the two indices weight differently, they can disagree. The cleanest case: a country that produces oil and exports most of it. An oil price rise shows up strongly in the production-weighted index and much less in the consumption-weighted one.

### BeatFifteen - Nominal and real

*381 words, about 152 s at 150 words per minute.*

One more piece of measurement before the evidence, and it is the one students get wrong under time pressure.

A loan is simple enough. A lender hands over a dollar today and gets back one plus the interest rate tomorrow. But we usually care about goods, not dollars.

Work the lecture's example. A one year loan charges eleven per cent. Everyone expects inflation of two per cent over that year, so a price index of one hundred becomes one hundred and two. Someone lends one hundred dollars.

At the start, one hundred dollars buys exactly one basket of goods. At the end, the lender receives one hundred and eleven dollars. But that does not buy one point one one baskets, because prices rose in the meantime. It buys one hundred and eleven divided by one hundred and two, which is about one point zero eight eight baskets.

So for every good the lender gave up, they get back about one point zero eight eight goods. The extra eight point eight per cent is the real interest rate: real because it is counted in goods rather than in currency.

Do it in general and you get the exact relation: one plus the real rate equals one plus the nominal rate, divided by one plus inflation. And for small inflation that is approximately the real rate equals the nominal rate minus inflation. That is the Fisher equation.

Two warnings. First, the subtraction is an approximation. It is fine at two per cent and it is badly wrong in a hyperinflation, where you need the ratio. Second, you do not know the real interest rate at the time you lend, because you do not know what inflation will be. So distinguish the real rate you expected when the loan was made from the real rate that turned out. Before and after. Ex ante and ex post.

And one cross-reference worth holding, because it ties the course together. Every interest rate in the consumption and general equilibrium material earlier in this course was a real rate, because those models traded goods across time. But money demand needs the nominal rate, because the nominal rate is what you forfeit by holding cash. Real rates for intertemporal decisions; the nominal rate for the opportunity cost of money.

### BeatSixteen - Does the world agree

*533 words, about 213 s at 150 words per minute.*

All of that is theory. Does the world agree?

Here is the test the textbook puts in this chapter. Take every country you can get data for. For each one, compute the average growth rate of broad money over three decades, and the average rate of inflation over the same period. Then plot one dot per country: money growth across, inflation up.

If inflation really is money growth minus something modest, these dots should lie close to a line with a slope of one.

Here are one hundred and fifty nine countries, from the World Bank's data.

And it looks like nothing. There is barely a relationship at all. Fit a line through it and the slope is zero point zero six. Essentially flat. The correlation is zero point one seven. On this picture money growth tells you almost nothing about inflation, and the theory we just spent forty minutes deriving appears to be refuted.

Before accepting that, look at the shape of the cloud. Almost every country is crushed into the bottom left corner, while the horizontal axis runs out to nearly four thousand per cent. Something is stretching this picture.

It is one dot. One country, sitting at an average money growth of three thousand eight hundred and seventy nine per cent. Sierra Leone.

Let's look at its actual series, year by year. Nineteen ninety, seventy four per cent. And then through the nineties and the two thousands, every single year lands between seven and seventy six per cent. Its median year is twenty three per cent.

Every year except two. In two thousand and one the series reads one hundred and thirty one thousand per cent. And in two thousand and fifteen it reads minus ninety nine point nine per cent.

A jump of that size, followed by a fall of almost exactly one hundred per cent, is not an economy. It is the signature of a currency being redenominated, or of the units of the series changing. One year of bad data, and it dragged one country's thirty year average up by a factor of more than a hundred and sixty.

So remove the handful of averages that are implausible on their face, and watch what the cloud does.

The correlation goes from zero point one seven to zero point seven five. The fitted slope goes from zero point zero six to one point zero six.

Slope one. Inflation almost exactly proportional to money growth, across a hundred and forty eight countries and three decades, which is precisely what the theory predicted.

There are two lessons here and the second one is free. The theory survives. And a single unexamined observation can hide a law with a slope of one behind an apparent slope of zero.

One honest qualification. The relationship is tightest among the high inflation countries, and loosest among the low inflation ones. That is what you should expect: velocity does move, as we proved, but in an economy printing money at a violent rate the movement in velocity is small next to the movement in money. The quantity theory is a poor description of the mechanism and an excellent approximation at long horizons and large magnitudes.

### BeatSeventeen - Brazil

*382 words, about 153 s at 150 words per minute.*

Let's come closer to home, with two Brazilian series.

In blue, the IPCA: inflation accumulated over twelve months, from the year two thousand to today. In yellow, the Selic target, the policy interest rate set by the central bank.

Watch them move together. When inflation climbs, the policy rate climbs above it. When inflation falls, the rate follows it down. That is the Fisher relation made visible. The nominal interest rate is approximately the real rate plus inflation, which means a nominal interest rate is never a number you can read on its own. It always contains an inflation forecast.

Look at the range those two series cover. The Selic target has been as high as twenty six and a half per cent and as low as two per cent in this period. That is not a small dial.

Now connect it back to where we started. In the model we built, the nominal interest rate is not merely a return on bonds. It is the opportunity cost of holding money. A Selic of fourteen per cent means that every unit of value you choose to keep as cash rather than as an interest bearing asset costs you fourteen per cent a year.

So go back to the trade-off from the beginning of this video. A high nominal rate means more trips to the bank, smaller real balances, and real resources burned on managing cash. Time, attention, fees. The square root we derived in the first ten minutes is the reason a high Selic is costly in a way that has nothing to do with borrowing.

One thing I am not going to show you, and I want to say why rather than quietly omit it. I would like to put a Brazilian monetary aggregate on this chart, so you could see money growth and inflation together for one country. The central bank publishes several candidate series, and I could not establish which one is which: the data endpoint returns numbers without names, and the metadata service is down. Picking one and calling it the money stock would have been a guess presented as a fact. So the cross-country evidence in the previous beat comes from a source that names its own series, and this chart shows only what I could verify.

## Act V - What inflation costs, and where the model stops

### BeatEighteen - Seigniorage

*502 words, about 201 s at 150 words per minute.*

Why would any government want inflation? Historically, because inflation raises revenue. And the mechanism is a quirk in the central bank's balance sheet.

When the central bank expands the monetary base, it acquires assets and issues liabilities in equal amount. That sounds like a non-event. But the assets it acquires, government bonds, pay interest, while the liabilities it issues, currency and reserves, typically do not. And the central bank is a branch of the government.

So expanding the monetary base is a way for the government to obtain a loan it never has to repay and on which it pays no interest.

Write the government's budget constraint to see where it enters. On one side, what the government must pay: this period's spending, plus principal and interest on the debt it already owes. On the other, what it has available: tax revenue, new borrowing, and the increase in the monetary base. Rearrange it and the point is unmissable: the monetary base sits in the budget in exactly the place debt sits, except that it carries no interest.

Now the question that makes this more than accounting. Who is actually paying? The government buys real goods with newly created money, and nobody writes a cheque. So where does the burden fall?

It falls on everyone holding money. Expanding the base raises the money supply and then the price level, and anyone holding money while it loses value has handed some of their purchasing power to the government, exactly as if they had been taxed. That is why seigniorage is also called the inflation tax.

And once you see it as a tax you can ask the question you would ask of any tax. What is the base, and what is the rate? The rate is the rate at which money loses value. The base is real money balances: the stock of purchasing power people are holding in the form of money.

Which sets up the limit, and it is the most elegant result in the chapter. To raise a lot of revenue the government must expand the base fast. Expanding fast means high inflation. High inflation means a high nominal interest rate. And a high nominal interest rate, by the very model we derived, means people hold smaller real balances.

The tax base shrinks precisely because the rate went up.

So plot revenue against inflation and you do not get a rising line. You get a hump. Past some inflation rate, raising inflation further collects less, because the base is eroding faster than the rate is climbing. It is a Laffer curve, in inflation. Hyperinflations are what the far side of that hump looks like, and the textbook leaves the closed form as exercise eleven point six, which uses a money demand function built for exactly this purpose.

One footnote so you do not overstate it. A growing economy wants growing real balances, so a government can collect some seigniorage at zero inflation. Seigniorage and the inflation tax are closely related, not identical.

### BeatNineteen - What inflation costs

*481 words, about 192 s at 150 words per minute.*

If inflation is a tax, what damage does it do? The chapter gives four costs, and the first one we have already derived without realising it.

Cost one comes straight out of the trip-cost model. Higher inflation means a higher nominal interest rate, which means people hold smaller balances, which means more trips to the bank, and every trip costs F. Multiply the optimal number of trips by the cost per trip and you get the total: the square root of the nominal rate times income times F over two. Substitute the Fisher equation and the nominal rate becomes the real rate plus inflation, so the cost rises with inflation directly.

This is called the shoe leather cost, from the image of wearing out your shoes walking to the bank, and it is easy to dismiss as trivial. Do not. The textbook's author describes his father, during the Argentine inflation of the late nineteen eighties, going to the bank twice a day, at noon and after work, to hold exactly enough cash for that day and no more. That is hours of a person's life, every day, spent on a problem that does not exist at low inflation.

And it suggests a remedy. If the damage comes from the opportunity cost of holding money, abolish the opportunity cost: drive the nominal interest rate to zero. That is the Friedman rule. But look at what it requires. A zero nominal rate with a positive real rate means inflation equal to minus the real rate. It requires deflation. The textbook is careful to call this a theoretical extreme, valuable for its logic rather than as a policy proposal.

Cost two: menu costs. Changing posted prices consumes real resources. Restaurants reprint menus, shops reprint signs, and the higher inflation is, the more often they must. Now notice the conflict, because this is the interesting part. Minimising menu costs points to zero inflation, not to the deflation the Friedman rule demands. The two costs point at two different optimal inflation rates, and the chapter does not pretend to resolve it. And even zero inflation would not eliminate menu costs, because individual prices still move while the index stands still.

Cost three: relative price uncertainty. You do not check every price of every good. You carry a rough sense of what a unit of currency buys, and you judge the prices in front of you against it. High inflation corrodes that sense, and the image for it is the best line in the chapter: it is like trying to take measurements with a ruler that keeps changing size. Producers face the same problem when setting their own prices.

Cost four: banks earn seigniorage too, because deposits pay less than market rates, and higher inflation widens that margin. The result is excessive entry into banking: real resources drawn into an industry by a wedge that inflation created.

### BeatTwenty - Neutral, not superneutral, and where this stops

*491 words, about 196 s at 150 words per minute.*

We are nearly done, and there is one confusion left to clear, because it is the most common error on this material.

This lecture is usually summarised as showing that money does not matter. That summary is wrong in a precise way.

There are two different claims. The first concerns the level of the money stock: change it once and nothing real happens, prices simply move in proportion. That claim is true here, and we proved it. It is called neutrality.

The second concerns the growth rate: keep money growing faster forever and still nothing real happens. That claim is called superneutrality, and it is stronger. And this lecture refutes it.

Watch the chain, because every link is something we derived. Faster money growth raises inflation. Higher inflation raises the nominal interest rate, by Fisher. A higher nominal rate raises the opportunity cost of holding money, so households hold smaller real balances. Smaller balances mean more trips to the bank. And trips consume real resources.

So the very same model in which money is neutral is a model in which sustained inflation has real costs. That is not a contradiction. It is the difference between changing a level and changing a rate, and being able to state it cleanly is worth a mark in any examination.

Now the honest limit of everything you have seen. All of it rested on one assumption: that prices are free to move. That assumption is what closed two of the three arrows, what made the price level the variable that adjusts, and what made money neutral in the first place.

Take it away and the structure changes completely. Suppose the price level cannot move in the short run. Look again at the equilibrium condition: the money supply still has to equal money demand, and something still has to give. But the price level is frozen. The only candidates left are the interest rate and output. Output. Money would stop being neutral and start having real effects.

This chapter has no mechanism for that. It genuinely does not. And when you are asked what happens when prices are fixed, the correct answer is to say so, and to name where the mechanism comes from, rather than to recite the classical result in a world where its assumption has been removed. The mechanism is the sticky price model, and it is the next two lectures.

So here is the frame to remember. Inflation equals money growth minus the elasticity times output growth. The elasticity is one half, because there are economies of scale in managing cash. Get it wrong by one half in an economy growing at three per cent, and you will miss your inflation target by one and a half points. And behind the formula, a hundred and forty eight countries over thirty years agreeing with it, once you look closely enough at your data to throw out the year that was not an economy.

---

**Total: 8256 words, about 55.0 minutes at 150 words per minute.**
