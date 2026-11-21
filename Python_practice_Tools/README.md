**History of all the tools that I'll build along learning python**

Hey, everyone, this is the README file for all the Tool I'll build in this folder.


# 1st Tool :- File approval system according to extension and size.

I didn't have to put in much effort to build this tool. I was able to create it quite easily using some of my previous practice, along with a few built-in functions and string methods.

My main goal was to practise what I had learned in the previous lectures, so I used a combination of expressions and methods to build this tool.

These are all just basic fundamentals, and I used them to create this small tool while practising what I had learned.


# Second Tool :- Taxi charges calculator

Before building this small taxi fare calculator, I had created a similar tool for calculating e-commerce purchase bills. However, in that project, I used `return` statements almost everywhere, which made the code look quite messy and cluttered. So, I decided not to include that project here.

Instead, I shared my code with AI through Google AI Labs, got feedback and guidance, and then specifically asked it to teach me how to write cleaner code.

After some more practice and careful thinking, I wrote this new taxi fare calculator. Although you'll still notice several beginner-level aspects in the code, I gave it my best effort, and I'll keep improving as I learn more.

**About This Tool:**

This tool calculates taxi fares in USD. It includes:

- Night charges.
- Booking fees.
- Discounts on every 5th ride (5th, 10th, 15th, and so on).


# 3rd Tool :- Shoping cart calculator using list

I built this tool to calculate the total of a shopping cart. It takes a list of item prices from the user as input, removes invalid prices such as negative and zero values, and then calculates the total cost along with the number of valid items added to the cart.

While building this tool, I faced a few challenges.

The first issue was that values received through `input()` are strings, not lists. So, I initially thought about how to convert that input into a list. I took a wrong approach at first, but based on my understanding at the time, it seemed like the right thing to do.

I wrapped the input in parentheses and added `list` before it, thinking that would solve the problem. However, I got an error.

Instead of giving up, I looked more closely at the error and tried to understand what was going wrong. After some research, I found that `ast.literal_eval()` could help me convert the input into a Python list.

But I made another mistake: I used the method without importing `ast`, so it wasn't working. After thinking about it a little more, I finally figured out the issue and solved it!

There is still one limitation: the user has to enter the prices inside square brackets (`[]`), otherwise `ast.literal_eval()` may fail. However, the core logic works correctly.

As I learn more functions like `map()` and other built-in methods, I'll try to improve this tool further.

**Also, this is my first task involving Python lists, so it was a good learning experience for me!**


# 4th Tool :- Expense tracker (total, hgihest, and average expenses)

This tool took me a little more time to build. I created an Expense Tracker that takes expenses from the user one by one and stops when the user types `done`.

It stores all the expenses in a list and calculates the total amount spent, saving it in a variable called `total_expenses`.

After that, it finds the highest expense and stores it in `highest_expense`. Finally, it calculates the average expense and stores it in another variable.

At first, I got a little stuck trying to figure out how to find the highest value from the list. I initially thought about creating a loop and using conditionals to solve this.

However, while testing my code and searching for a solution on Google, I discovered that Python has a built-in function called `max()` that can do this much more easily.

So, I used `max()` and finally managed to complete the tool!

It was another good learning experience, and I'm gradually getting more comfortable with Python lists, loops, conditionals, and built-in functions.