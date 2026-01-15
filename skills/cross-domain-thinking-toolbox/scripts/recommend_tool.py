#!/usr/bin/env python3
"""
Cross-Domain Thinking Tool Recommender

Analyzes problem descriptions and recommends appropriate thinking tools
from the 25 professional mental models.
"""

from typing import Dict, List, Tuple
import json
import sys

# Thinking tool database with tags and use cases
TOOLS = {
    "artist": {
        "tags": ["creative", "innovation", "unique", "novelty", "stuck", "blocked"],
        "use_when": ["need creative ideas", "stuck in conventional thinking", "seeking novelty"],
        "question": "What makes this unique and interesting?",
    },
    "economist": {
        "tags": ["behavior", "incentive", "policy", "system", "predict", "response"],
        "use_when": ["predicting behavior", "designing systems", "changing policies"],
        "question": "How do people respond to incentives?",
    },
    "engineer": {
        "tags": ["predict", "calculate", "model", "quantify", "forecast", "data"],
        "use_when": ["need predictions", "quantify outcomes", "data-driven decisions"],
        "question": "Can I model and calculate this?",
    },
    "entrepreneur": {
        "tags": ["uncertainty", "experiment", "test", "rapid", "mvp", "iterate"],
        "use_when": ["uncertain environment", "need to test quickly", "startup scenarios"],
        "question": "What works if I try many things?",
    },
    "doctor": {
        "tags": ["diagnose", "symptom", "root cause", "troubleshoot", "debug", "cause"],
        "use_when": ["troubleshooting", "finding root cause", "debugging issues"],
        "question": "What's the diagnosis from symptoms?",
    },
    "journalist": {
        "tags": ["fact", "verify", "source", "research", "confirm", "truth"],
        "use_when": ["validating information", "research", "avoiding misinformation"],
        "question": "Have I verified from independent sources?",
    },
    "scientist": {
        "tags": ["test", "hypothesis", "experiment", "validate", "belief", "evidence"],
        "use_when": ["testing beliefs", "validating assumptions", "optimization experiments"],
        "question": "Does this withstand controlled testing?",
    },
    "mathematician": {
        "tags": ["prove", "rigor", "logic", "error", "formal", "verify"],
        "use_when": ["rigorous decisions", "finding logical errors", "programming"],
        "question": "Can I prove this rigorously?",
    },
    "programmer": {
        "tags": ["automate", "pattern", "process", "repeat", "efficient", "simplify"],
        "use_when": ["optimizing processes", "reducing errors", "efficiency"],
        "question": "What patterns can I automate?",
    },
    "architect": {
        "tags": ["visualize", "future", "scale", "plan", "prototype", "model"],
        "use_when": ["planning", "large projects", "visualizing outcomes"],
        "question": "What will this look like at full scale?",
    },
    "salesperson": {
        "tags": ["motivation", "understand", "need", "negotiation", "customer", "want"],
        "use_when": ["understanding motivations", "negotiation", "product design"],
        "question": "What do people really want beneath stated needs?",
    },
    "soldier": {
        "tags": ["procedure", "discipline", "prevent", "error", "checklist", "safety"],
        "use_when": ["preventing errors", "high-stakes situations", "safety-critical work"],
        "question": "What procedure must I follow exactly?",
    },
    "chess_master": {
        "tags": ["simulate", "predict", "strategy", "scenario", "future", "anticipate"],
        "use_when": ["strategy", "planning", "competitive situations"],
        "question": "What happens next if I simulate this?",
    },
    "designer": {
        "tags": ["intuitive", "communicate", "ux", "design", "interface", "guide"],
        "use_when": ["UX design", "communication", "presentation"],
        "question": "Does this intuitively suggest how to use it?",
    },
    "teacher": {
        "tags": ["explain", "learn", "knowledge", "teach", "transfer", "understand"],
        "use_when": ["explanations", "documentation", "onboarding", "mentoring"],
        "question": "How do I build knowledge in a learner's mind?",
    },
    "anthropologist": {
        "tags": ["culture", "immerse", "understand", "group", "inside", "cross-cultural"],
        "use_when": ["cross-cultural understanding", "user research", "organizational change"],
        "question": "Can I understand this group from inside?",
    },
    "psychologist": {
        "tags": ["behavior", "predict", "cognitive", "bias", "attention", "human"],
        "use_when": ["understanding reactions", "persuasion", "relationships"],
        "question": "Does my model predict actual behavior?",
    },
    "critic": {
        "tags": ["analyze", "build", "synthesize", "critique", "extend", "improve"],
        "use_when": ["analysis", "research", "creative work"],
        "question": "How can I build on others' work?",
    },
    "philosopher": {
        "tags": ["extreme", "assumption", "logic", "flaw", "principle", "intuition"],
        "use_when": ["finding logical flaws", "testing policies", "examining beliefs"],
        "question": "What happens when I push this idea to extremes?",
    },
    "accountant": {
        "tags": ["ratio", "metric", "efficiency", "analyze", "compare", "performance"],
        "use_when": ["performance analysis", "efficiency", "diagnosis"],
        "question": "What ratios reveal hidden truths?",
    },
    "politician": {
        "tags": ["perceive", "believe", "communicate", "stakeholder", "appearance", "credibility"],
        "use_when": ["communication", "leadership", "change management"],
        "question": "What will people believe about this?",
    },
    "novelist": {
        "tags": ["story", "narrative", "structure", "communicate", "present", "coherent"],
        "use_when": ["communication", "presentations", "pitches"],
        "question": "Does my story make coherent sense?",
    },
    "actor": {
        "tags": ["emotion", "feel", "authentic", "present", "confidence", "genuine"],
        "use_when": ["performance", "presentations", "emotional management"],
        "question": "Can I actually feel the state I need?",
    },
    "plumber": {
        "tags": ["examine", "investigate", "hands-on", "direct", "disassemble", "look"],
        "use_when": ["debugging", "investigation", "hands-on problems"],
        "question": "What would I find by examining directly?",
    },
    "hacker": {
        "tags": ["underlying", "abstraction", "system", "layer", "deep", "edge"],
        "use_when": ["system understanding", "debugging", "optimization"],
        "question": "What's really happening underneath?",
    },
}


def recommend_tools(problem, max_results=5):
    """
    Recommend thinking tools based on problem description.

    Args:
        problem: Description of the problem or situation
        max_results: Maximum number of tools to return

    Returns:
        List of (tool_name, score) tuples sorted by relevance
    """
    problem_lower = problem.lower()
    words = set(problem_lower.split())

    scores = {}

    for tool_name, tool_info in TOOLS.items():
        score = 0

        # Check tags
        for tag in tool_info["tags"]:
            if tag in problem_lower:
                score += 3
            elif tag in words:
                score += 2

        # Check use_when phrases
        for phrase in tool_info["use_when"]:
            if phrase in problem_lower:
                score += 4

        if score > 0:
            scores[tool_name] = score

    # Sort by score and return top results
    sorted_tools = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_tools[:max_results]


def format_recommendation(tool_name, score):
    """Format a single tool recommendation."""
    tool_info = TOOLS[tool_name]
    return """
### {}

Score: {}

Core Question: {}

Use When: {}
""".format(tool_name.title(), score, tool_info["question"], ", ".join(tool_info["use_when"]))


def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python recommend_tool.py 'your problem description'")
        print("\nExample:")
        print('  python recommend_tool.py "I need to understand why my team is unmotivated"')
        sys.exit(1)

    problem = " ".join(sys.argv[1:])
    recommendations = recommend_tools(problem)

    if not recommendations:
        print("No specific tool match found. Try a different description or consult SKILL.md for all 25 tools.")
        return

    print("\nProblem: {}\n".format(problem))
    print("Recommended Thinking Tools:\n")

    for tool_name, score in recommendations:
        print(format_recommendation(tool_name, score))


if __name__ == "__main__":
    main()
