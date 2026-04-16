from google import genai
from dotenv import load_dotenv
import os

# Loading environment variable

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')

# initializing a client

client = genai.Client(api_key=api_key)
modelname = 'gemini-2.5-flash-lite'

def for_issue(files):

    prompt = """
You are an expert code debugger. Your job is to identify all issues in the code and report them in Bengali. Do NOT provide any solutions or fixes.
## Your Tasks:
1. **Syntax Errors** - Which line has what mistake
2. **Logic Problems** - Where unexpected results might occur
3. **Runtime Errors** - Which inputs will cause the program to crash
4. **Performance Issues** - Where the code will be slow
5. **Best Practice Violations** - Code style or convention problems

## Output Format:
For each issue:
- **লাইন নম্বর**: [number]
- **ইস্যু**: [what the problem is]
- **কেন সমস্যা**: [brief reason]

## Important:
- Only identify problems, do NOT provide solutions
- Always mention line numbers
- Always respond in Bengali
- If no issues found, say "✓ কোনো ইস্যু পাওয়া যায়নি"
"""

    try:
        response = client.models.generate_content(
        model= modelname,
        contents=[files, prompt]
    )

        return response.text
    except Exception as e:
        return e


def for_code_solution(files):
    prompt = """
You are an expert programming mentor. Your job is to provide solutions for code issues with proper explanations in Bengali. You will receive a code with identified issues.

## Your Tasks:

For each issue provided:
1. **সমাধান** - Provide the corrected code snippet
2. **ব্যাখ্যা** - Explain WHY this solution works
3. **কীভাবে কাজ করে** - Step-by-step breakdown of the fix

## Output Format:

For each issue:
- **ইস্যু #[number]**: [brief issue description]
- **সংশোধিত কোড**:
- **কেন এটা কাজ করবে**: [detailed explanation]
- **মূল পয়েন্ট**: [key takeaway in 1-2 lines]

## Important:
- Focus on explaining WHY the solution works, not just WHAT to change
- Use beginner-friendly Bengali language
- Provide code examples for each fix
- Explain the logic behind the solution
- Always respond in Bengali
"""

    try:
        response = client.models.generate_content(
        model= modelname,
        contents=[files, prompt]
    )

        return response.text
    except Exception as e:
        return e

def solution_for_hints(files):
    prompt = """
Always respond in Bengali
You are an expert code debugger. Your job is to identify all issues in the code and report them in Bengali. Do NOT provide any solutions or fixes.
## Your Tasks:
1. **Syntax Errors** - Which line has what mistake
2. **Logic Problems** - Where unexpected results might occur
3. **Runtime Errors** - Which inputs will cause the program to crash
4. **Performance Issues** - Where the code will be slow
5. **Best Practice Violations** - Code style or convention problems

role:
your are a great code error explainer.

## Output Format:
For each issue:
- only solution step by step with text and no code

## Important:
- Only identify problems, do NOT provide solutions
- Always mention line numbers
- Always respond in Bengali
- If no issues found, say "✓ কোনো ইস্যু পাওয়া যায়নি"
"""
    try:
        response = client.models.generate_content(
        model= modelname,
        contents=[files, prompt]
    )

        return response.text
    except Exception as e:
        return e


