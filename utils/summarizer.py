def combine_summaries(agent_outputs):
    combined = "\n\n".join(agent_outputs)
    return f"--- FINAL PRODUCT STORY ---\n\n{combined}"
