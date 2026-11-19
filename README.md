# Hello Everyone, I'm Mohit Verma!

I've previously learned the basics of HTML, CSS, and JavaScript. I've documented what I've learned and my progress in my JavaScript practice repository.

However, as I continued learning JavaScript and reached DOM manipulation, I realised that JavaScript was a bit more complex than I expected.

One of my mistakes was not practising enough. I got stuck in what we call **"Tutorial Hell"** — a situation where you keep watching tutorials but don't actually practise what you learn.

This happened to me twice. Unfortunately, I couldn't maintain a consistent practice routine. Over time, I also realised that I was more interested in logic building and problem-solving than UI/UX design.

So, I decided to change my learning path and focus on backend development.

I had already invested a lot of time in JavaScript, but now I've decided to put that effort into learning Python. Moving forward, I plan to learn DSA and FastAPI using Python as well.

## About This Repository

In this repository, I'll document my Python learning journey, build and practise with different tools, and explore how AI can help me learn more effectively.

Here's what I'm currently using:

- **CS50P (Introduction to Programming with Python):** I'm learning Python through this course.
- **Google AI Lab:** I'm using AI to guide my learning, explore new concepts, get tasks, and practise through hands-on problem-solving.

As of **18 November 2026**, I've already completed some parts of Lecture 0 and Lecture 1 and have done a little practice as well.

## What You'll Find Here

I'll try to keep this repository simple, organised, and well-documented.

- Python concepts and learning progress.
- Practice problems and their solutions.
- Different tools I build along the way.
- The logic behind each tool.
- How each tool works and what I've learned while building it.

Feel free to explore the repository, try out some of the simple tools, and follow along with my progress.

I'll do my best to document everything properly and keep improving along the way.

*Thank you for visiting my repository!*


**History of all the tools that I'll build along learning python**


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