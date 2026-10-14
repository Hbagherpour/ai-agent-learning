# AI Agent Learning

A guided Python learning path from first principles to tested AI agent applications,
with a focus on financial markets and content creation.

Complete one project at a time: understand the concept, build it, make a small
change yourself, check the behavior, and explain what you built before progressing.

## Learning path

| Project | What we will build | What we will learn |
| --- | --- | --- |
| 00 — Agent loop | A scripted calculator demonstration | Decisions, tools, observations, tool-name validation, and stopping limits |
| 01 — Simple AI assistant | A conversational assistant in Python | Model API calls, prompts, conversation history, error handling, and usage costs |
| 02 — Financial calculator agent | An agent that chooses tools to calculate returns, moving averages, and volatility | Tool calling, argument validation, and checking calculations |
| 03 — Financial news agent | An agent that retrieves news, summarizes developments, and explains possible market implications with source links | Information retrieval, source quality, publication dates, and separating facts from interpretation |
| 04 — S&P 500 analysis agent | An agent that retrieves historical data, calculates performance and risk metrics, and explains charts | Market data tools, Python analysis, chart generation, and reliable numerical answers |
| 05 — LinkedIn content agent | An agent that turns project results or sourced market analysis into a LinkedIn draft | Writing instructions, grounding claims in evidence, revision, and human review |
| 06 — Financial document Q&A agent | An agent that answers questions about provided reports and cites relevant passages | Document processing, retrieval, and answering from supporting evidence |
| 07 — Daily market briefing workflow | A system that combines news, S&P 500 analysis, and a reviewable LinkedIn draft | Connecting agents and workflows, saved state, scheduling, and failure handling |
| 08 — Reliable agent service | A tested application built around one of the financial agents | Evaluation, logging, security, cost limits, and deployment |
| 09 — Research team of agents | News, data-analysis, and review agents that produce a combined report | Agent coordination and measuring whether multiple agents improve the result |

The roadmap describes planned projects, not a list of completed applications.
Exercise 00 is the starting demonstration. Future projects will be added in
separate folders as we work through the lessons.

## Project approach

- Start with plain Python and add libraries when they help with a concept we understand.
- Build Project 01 as an assistant baseline before letting a model choose tools.
- Let Python tools calculate financial metrics; let the model choose tools and explain results.
- Include source links and dates in news analysis, and distinguish reported facts from interpretation.
- Treat news context as possible explanation, rather than proof of what caused a market move.
- Create LinkedIn drafts for review. Publishing is a separate capability that requires explicit approval.
- Give each completed project runnable code, a README, setup instructions, example inputs and outputs, limitations, and checks appropriate to its behavior.
- Keep API keys and other secrets out of the repository.

## Example goals

**Financial news agent:** “Summarize the major market developments for a selected
date, link to the sources, and explain their possible implications.”

**S&P 500 analysis agent:** “How did the S&P 500 perform over the selected period,
and what were its volatility and maximum drawdown?”

**LinkedIn content agent:** “Turn this project's verified findings into a clear
LinkedIn draft that I can review and edit.”

## Getting started

Start with [Exercise 00: the agent loop](00-agent-loop/README.md).

Run the demonstration from the repository root:

```bash
python 00-agent-loop/loop_demo.py
```

On Windows, use `py` instead of `python` if needed.

The demonstration uses scripted decisions and needs no API key.
Model-powered projects require a provider setup. Choose that setup and understand
any usage charges before making paid API calls.
