#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 12:56:03 2026

@author: nan
"""

import json
import random

# Load chatbot data from intents.json
with open("intents.json", "r") as file:
    data = json.load(file)

print("===== AI Personality Prediction Chatbot =====")
print("Hello! Welcome to the chatbot 😊\n")

traits = []

# Ask questions
for item in data["questions"]:

    print(item["question"])

    # Display options
    options = list(item["options"].keys())
    print("Options:", ", ".join(options))

    # Get user answer
    answer = input("Your answer: ").strip()

    # Save associated trait
    if answer in item["options"]:
        traits.append(item["options"][answer])
    else:
        print("Unknown answer. No trait added.\n")

    print()

# Count personality traits
trait_count = {}

for trait in traits:
    if trait in trait_count:
        trait_count[trait] += 1
    else:
        trait_count[trait] = 1

# Sort traits by frequency
sorted_traits = sorted(
    trait_count.items(),
    key=lambda x: x[1],
    reverse=True
)

# Final personality prediction
print("===== Personality Prediction Result =====\n")

top_traits = [trait[0] for trait in sorted_traits]

if "independent" in top_traits:
    print("- You value freedom and personal space.")

if "kind" in top_traits:
    print("- You are emotionally supportive and caring.")

if "intelligent" in top_traits:
    print("- You enjoy deep thinking and learning.")

if "creative" in top_traits:
    print("- You have strong imagination and creativity.")

if "calm" in top_traits:
    print("- You handle situations in a peaceful way.")

if "adventurous" in top_traits:
    print("- You enjoy exploring new experiences.")

print("\nMain Personality Traits:")
print(", ".join(top_traits))

print("\nFinal Analysis:")
print("You appear to have a unique combination of emotional and psychological traits.")
print("Your responses suggest patterns in how you think, feel, and interact with the world.")

print("\nDisclaimer:")
print("This chatbot is for educational and entertainment purposes only.")