"""A scripted demonstration of an agent loop; no AI model or API required."""


def add(a, b):
    """A tool: do one specific calculation and return its result."""
    return a + b


def choose_action(observations):
    """A scripted decision maker. A later project will use an AI model here."""
    if not observations:
        return {"type": "tool", "name": "add", "arguments": {"a": 12, "b": 8}}
    return {"type": "finish", "answer": f"The total is {observations[-1]}."}


def run_demo(max_steps=3):
    if max_steps < 1:
        raise ValueError("max_steps must be at least 1")

    tools = {"add": add}
    observations = []
    print("Goal: Find the total of 12 and 8.")

    for step in range(1, max_steps + 1):
        action = choose_action(observations)
        print(f"Step {step}: decision = {action['type']}")

        if action["type"] == "finish":
            print(action["answer"])
            return action["answer"]

        tool = tools[action["name"]]
        result = tool(**action["arguments"])
        observations.append(result)
        print(f"Tool: {action['name']}; result: {result}")

    raise RuntimeError("Stopped: step limit reached before a final answer.")


if __name__ == "__main__":
    run_demo()
