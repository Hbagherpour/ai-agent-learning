# Exercise 00: See the agent loop

This is a prerequisite exercise, not a model-powered AI agent. The decisions
are scripted so you can see how the surrounding program works before adding AI.
No packages, API key, or paid service are needed. Use Python 3.10 or newer.

## Run it

Open a terminal in this folder and run:

```bash
python loop_demo.py
```

On Windows, if `python` is not found, try `py loop_demo.py`.

Expected output:

```text
Goal: Find the total of 12 and 8.
Step 1: decision = tool
Tool: add; result: 20
Step 2: decision = finish
The total is 20.
```

## What each part means

| Code | Role |
| --- | --- |
| `choose_action` | Decides whether to call a tool or finish. Here it follows fixed rules. |
| `add` | The tool that performs the calculation. |
| `tools` | Lists the tools the program can call. |
| `observations` | Holds tool results for this run. This is temporary state. |
| `run_demo` | Runs the decision/action/result cycle. |
| `max_steps` | Prevents the cycle from continuing indefinitely. |

In `tool(**action["arguments"])`, `**` passes the dictionary entries as named
arguments. With the example dictionary, this is equivalent to `add(a=12, b=8)`.
An f-string such as `f"Tool: {action['name']}"` inserts a value into text.

## Your small experiment

1. Run the script unchanged.
2. Change `12` and `8` in the arguments dictionary to `25` and `17`.
3. Update the printed goal to match, then run again. Expect `42`.
4. Explain why the program takes two steps: calculation, then final answer.

Optional: change `run_demo()` at the bottom to `run_demo(max_steps=1)`.
It will calculate the total, then raise an error because it has no step left
to choose the final answer. Restore it when done.

## Where AI will enter

In the calculator-agent project, a model will choose actions from the user's
request and the tool results. Python will still execute the tools. We will add
validation before executing model-generated arguments.

## Check your understanding

What happens if the decision maker keeps requesting tools and never chooses
`finish`? Which line of reasoning explains why the step limit matters?
