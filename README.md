# pyflood
This is a simple flood game programmed in Python and using the TkInter GUI library, for the purpose of learning the Python language (myself) and for the purpose of teaching my son how to code. 

I have applied the following concepts:
- Object Orientation & Inheritance
- The Forest Fire flood fill algorithm
- the MVC (Model-View-Controller) pattern 
- the PubSub (Publisher-Subscriber) pattern 
- the Singleton pattern (for a simple logger)

The Forest Fire algorithm is a simple (non recursive) flood fill algorithm. It is described (in pseudo language) here: https://en.wikipedia.org/wiki/Flood_fill

For the PubSub pattern (aka Observable pattern) I have borrowed the helpful instructions given here: https://www.protechtraining.com/blog/post/tutorial-the-observer-pattern-in-python-879

For the Singleton pattern I have applied the mechanism of delegating to a private nested inner class described here: https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html

You can freely use and distribute this for your own educational purposes. Let me know what you think, and have fun!