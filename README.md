# arb

An arbtitrage calculator that looks for arbitrage opportunities between sports books. To use it get an api key from here: https://the-odds-api.com/

In main.py find API_KEY = "Your key here" and enter your api key there. From here, you can run it using python main.py.

You can use the following parameters to edit the outputs:

1. -k: this is looking for your odds api key. If you didn't put it in main.py you will have to put it here.
2. -r: Allows you to select your region. The regions are as follows: "eu", "us", "au", "uk"
3. -c: Profit cutoff. Gives the minimum profit margin for the arbitrage to be printed
4. -b: Gives the total amount of money the user has to allocate for any arbitrage opportunity.

Example run will look something like this: python main.py -r us -c 10 -b 200

This example will give you every arbitrage opportunity in the united states, with a minimum profit of $10 and a maximum allocation of $200.

