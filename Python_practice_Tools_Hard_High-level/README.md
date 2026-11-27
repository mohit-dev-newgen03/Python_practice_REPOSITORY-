# Hello Everyone!

This is my new repository, where I'll be documenting my Python learning journey through bigger projects and tools.

So far, I've completed around three to four lectures of **CS50P (Introduction to Programming with Python)**. Based on everything I've learned from these lectures, I've built a bigger tool that I'll be pushing to this repository as `main.py`.

Along with the code, I'll also document the entire development process in this README, including the challenges I faced, the problems I encountered, and what I learned while building the tool.

As I progress through the course and move on to more advanced topics, I'll continue building bigger and more useful tools and projects based on my learnings. I'll keep adding those projects to this repository as well.

The main goal of this repository is to track my progress, apply what I learn through practical projects, and gradually improve my programming and problem-solving skills.

Feel free to explore this repository and follow along with my journey!

**Thank you for visiting!**



# Tool 1 : resilient e-commerce order processor with exception handling and batch analytics

This project was a bit challenging because I first had to understand the task assigned by AI, especially how different functions were supposed to work together and how to integrate them properly.

While coding, I faced several challenges. One of the main ones was understanding exception handling, particularly how to raise a ValueError inside a try block, catch it using except, and return None when an error occurred. I also researched whether I should put my entire code inside a single try block. Eventually, I realised that this could also catch unexpected errors like TypeError, making debugging harder. So, I kept only the specific operations inside the try block and used an else block for the remaining logic.

Another challenge was checking whether an item was food or not. Initially, I thought I needed a separate condition to identify food items, but later I realised that simply checking not food was enough to apply additional charges to non-food items.

I also made a logical mistake in my for loop, where I wasn't properly storing the processed result. I fixed this by saving it in a separate cleared_string variable. Finally, I encountered a small bug because I forgot to print a function's returned result after calling it.

Overall, this project helped me understand exception handling, conditional logic, function integration, string processing, and debugging. Most importantly, I learned how to research problems, understand errors, and solve them independently instead of relying on ready-made solutions.