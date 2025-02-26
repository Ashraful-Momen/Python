# Python Regular Expressions: Complete Guide with Examples

## Introduction and Importing

```python
# Import the re module
import re

# Basic usage
pattern = r"hello"  # r prefix creates a raw string (recommended for regex)
text = "hello world"
match = re.search(pattern, text)
if match:
    print("Pattern found!")  # Pattern found!
```

## Basic Functions

```python
import re

text = "The rain in Spain falls mainly in the plain."

# re.search() - Find first occurrence (returns Match object or None)
match = re.search(r"rain", text)
print(match.group())  # 'rain'
print(match.span())   # (4, 8) - start and end positions

# re.match() - Check if pattern matches at the beginning of the string
beginning_match = re.match(r"The", text)  # Returns Match object
not_at_beginning = re.match(r"rain", text)  # Returns None

# re.fullmatch() - Check if pattern matches the entire string
full_match = re.fullmatch(r"The rain in Spain falls mainly in the plain\.", text)  # Match object
partial = re.fullmatch(r"The rain", text)  # None (only matches part of the string)

# re.findall() - Find all occurrences (returns list of strings)
all_occurrences = re.findall(r"in", text)
print(all_occurrences)  # ['in', 'in', 'in', 'in']

# re.finditer() - Find all occurrences (returns iterator of Match objects)
for match in re.finditer(r"in", text):
    print(f"Found 'in' at position {match.start()}")
    # Found 'in' at position 5
    # Found 'in' at position 12
    # Found 'in' at position 28
    # Found 'in' at position 38

# re.split() - Split string by pattern
split_text = re.split(r" ", "hello world python")
print(split_text)  # ['hello', 'world', 'python']

# re.sub() - Replace pattern with string
replaced = re.sub(r"rain", "snow", text)
print(replaced)  # The snow in Spain falls mainly in the plain.

# re.subn() - Replace pattern and return tuple (new_string, count)
replaced, count = re.subn(r"in", "ON", text)
print(f"Replaced {count} occurrences: {replaced}")
# Replaced 4 occurrences: The raON ON SpaON falls maONly ON the plaON.
```

## Compilation and Flags

```python
import re

# Compile pattern for better performance when reusing
pattern = re.compile(r"python", re.IGNORECASE)
print(pattern.search("Python is great").group())  # 'Python'
print(pattern.search("PYTHON").group())          # 'PYTHON'

# Available flags
text = """First line
Second LINE
THIRD line"""

# re.IGNORECASE or re.I - Case-insensitive matching
print(re.findall(r"line", text, re.IGNORECASE))  
# ['line', 'LINE', 'line']

# re.MULTILINE or re.M - ^ and $ match start/end of each line
print(re.findall(r"^.+", text, re.MULTILINE))  
# ['First line', 'Second LINE', 'THIRD line']

# re.DOTALL or re.S - Dot matches everything including newlines
print(re.search(r"First.*THIRD", text, re.DOTALL).group())  
# 'First line\nSecond LINE\nTHIRD'

# re.VERBOSE or re.X - Allows comments and whitespace in pattern
phone_pattern = re.compile(r"""
    \((\d{3})\)     # Area code
    [ ]             # Space
    (\d{3})         # First 3 digits
    -               # Dash
    (\d{4})         # Last 4 digits
""", re.VERBOSE)
print(phone_pattern.search("Call (123) 456-7890").groups())  
# ('123', '456', '7890')

# Combining flags with bitwise OR |
combined = re.compile(r"python", re.IGNORECASE | re.MULTILINE)
```

## Character Classes and Sets

```python
import re

text = "The price is $23.45 and the temperature is 72°F"

# . - Any character except newline
print(re.findall(r"p..", text))  # ['pri', 'per']

# \d - Digit [0-9]
print(re.findall(r"\d+", text))  # ['23', '45', '72']

# \D - Non-digit
print(re.findall(r"\D+", text))  # ['The price is $', '.', ' and the temperature is ', '°F']

# \w - Word character [a-zA-Z0-9_]
print(re.findall(r"\w+", text))  # ['The', 'price', 'is', '23', '45', 'and', 'the', 'temperature', 'is', '72', 'F']

# \W - Non-word character
print(re.findall(r"\W+", text))  # [' ', ' ', ' $', '.', ' ', ' ', ' ', ' ', '°']

# \s - Whitespace (space, tab, newline, etc.)
print(re.findall(r"\s+", text))  # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# \S - Non-whitespace
print(re.findall(r"\S+", text))  # ['The', 'price', 'is', '$23.45', 'and', 'the', 'temperature', 'is', '72°F']

# [abc] - Any character from the set (a, b, or c)
print(re.findall(r"[aeiou]", text))  # ['e', 'i', 'e', 'i', 'a', 'e', 'e', 'e', 'a', 'u', 'e', 'i']

# [^abc] - Any character not in the set
print(re.findall(r"[^aeiou\s]+", text))  # ['Th', 'pr', 'c', ' ', '$23.45', 'nd', 'th', 't', 'mp', 'r', 't', 'r', ' ', '72°F']

# [a-z] - Any character in the range
print(re.findall(r"[a-z]+", text))  # ['he', 'price', 'is', 'and', 'the', 'temperature', 'is']

# \b - Word boundary
print(re.findall(r"\bis\b", text))  # ['is', 'is']

# \B - Not a word boundary
print(re.findall(r"\B\w\B", text))  # ['h', 'r', 'i', 'c', 'n', 'h', 'e', 'm', 'p', 'e', 'r', 'a', 't', 'u', 'r']
```

## Quantifiers and Repetition

```python
import re

text = "The year 2023 has 365 days, and February has 28 or 29 days."

# * - 0 or more occurrences
print(re.findall(r"\d*", text))  # ['', '', '', '', '', '', '', '', '', '', '2023', '', '', '', '365', ''...]

# + - 1 or more occurrences
print(re.findall(r"\d+", text))  # ['2023', '365', '28', '29']

# ? - 0 or 1 occurrence
print(re.search(r"Febr?uary", text).group())  # 'February'
print(re.search(r"Febr?uary", "Feburary").group())  # 'Feburary'

# {n} - Exactly n occurrences
print(re.findall(r"\d{2}", text))  # ['20', '23', '36', '28', '29']

# {n,} - n or more occurrences
print(re.findall(r"\d{3,}", text))  # ['2023', '365']

# {n,m} - Between n and m occurrences
print(re.findall(r"\d{2,3}", text))  # ['202', '365', '28', '29']

# Greedy vs. Non-greedy
html = "<div>Content</div><div>More</div>"
print(re.findall(r"<div>.*</div>", html))  # ['<div>Content</div><div>More</div>'] (greedy)
print(re.findall(r"<div>.*?</div>", html))  # ['<div>Content</div>', '<div>More</div>'] (non-greedy)
```

## Groups and Capturing

```python
import re

# Basic capturing groups
match = re.search(r"(\d{2})-(\d{2})-(\d{4})", "Date: 01-15-2023")
if match:
    print(match.group())   # '01-15-2023' (full match)
    print(match.group(1))  # '01' (first group)
    print(match.group(2))  # '15' (second group)
    print(match.group(3))  # '2023' (third group)
    print(match.groups())  # ('01', '15', '2023') (all groups as tuple)

# Named groups (?P<name>...)
date_pattern = r"(?P<month>\d{2})-(?P<day>\d{2})-(?P<year>\d{4})"
match = re.search(date_pattern, "Date: 01-15-2023")
if match:
    print(match.group('month'))  # '01'
    print(match.group('day'))    # '15'
    print(match.group('year'))   # '2023'
    print(match.groupdict())     # {'month': '01', 'day': '15', 'year': '2023'}

# Non-capturing groups (?:...)
phone_match = re.search(r"(?:\+1-)?(\d{3})-(\d{3})-(\d{4})", "+1-123-456-7890")
if phone_match:
    print(phone_match.groups())  # ('123', '456', '7890') - doesn't include +1- prefix

# Backreferences \number or \g<name>
# Find repeated words
repeat_pattern = r"\b(\w+)\s+\1\b"
print(re.findall(repeat_pattern, "The the cat sat on the mat"))  # ['The']

# Named backreferences
html_pattern = r"<(?P<tag>[a-z0-9]+)>.*?</(?P=tag)>"
print(re.findall(html_pattern, "<div>Content</div><span>Text</span>"))  
# ['div', 'span']
```

## Assertions and Lookarounds

```python
import re

text = "Python is cool. JavaScript is also cool. TypeScript too."

# ^ - Start of string/line
print(re.search(r"^Python", text).group())  # 'Python'

# $ - End of string/line
print(re.search(r"too\.$", text).group())  # 'too.'

# \b - Word boundary
print(re.findall(r"\bis\b", text))  # ['is', 'is']

# \B - Not word boundary
print(re.findall(r"\B\w\B", text))  # ['y', 't', 'h', 'o', 'c', 'o', 'o', 'a', 'v', 'a', 'c', 'r', 'i', 'p', 't'...]

# Positive lookahead (?=...) - Match if followed by pattern
print(re.findall(r"\w+(?= is)", text))  # ['Python', 'JavaScript']

# Negative lookahead (?!...) - Match if not followed by pattern
print(re.findall(r"\w+(?! is)", text))  # ['cool', 'also', 'cool', 'TypeScript', 'too']

# Positive lookbehind (?<=...) - Match if preceded by pattern
print(re.findall(r"(?<=is )\w+", text))  # ['cool', 'also']

# Negative lookbehind (?<!...) - Match if not preceded by pattern
print(re.findall(r"(?<!is )\w+", text))  # ['Python', 'is', 'JavaScript', 'is', 'cool', 'TypeScript', 'too']
```

## Substitution and Replacement

```python
import re

# Basic substitution
text = "The color of the car is red."
replaced = re.sub(r"red", "blue", text)
print(replaced)  # The color of the car is blue.

# Using captured groups in replacement
date = "2023-01-15"
formatted_date = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\2/\3/\1", date)
print(formatted_date)  # 01/15/2023

# Using named groups in replacement
date_pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
formatted_date = re.sub(date_pattern, r"\g<month>/\g<day>/\g<year>", date)
print(formatted_date)  # 01/15/2023

# Using a function for replacement
def celsius_to_fahrenheit(match):
    celsius = float(match.group(1))
    fahrenheit = celsius * 9/5 + 32
    return f"{fahrenheit:.1f}°F"

temperatures = "Today's temperatures: 25°C in the morning, 30°C at noon."
converted = re.sub(r"(\d+(?:\.\d+)?)°C", celsius_to_fahrenheit, temperatures)
print(converted)  # Today's temperatures: 77.0°F in the morning, 86.0°F at noon.

# Case conversion
# \L - Convert to lowercase until \E
# \U - Convert to uppercase until \E
# \E - End case conversion
# Note: Python re module doesn't directly support these, use function instead

def case_converter(match):
    word = match.group(1)
    return word.upper()

text = "hello world python"
print(re.sub(r"\b(\w+)\b", case_converter, text))  # HELLO WORLD PYTHON
```

## Working with Match Objects

```python
import re

match = re.search(r"(\w+)@(\w+)\.(\w+)", "Contact us at info@example.com or support@company.org")

if match:
    print(match.group())     # 'info@example.com' (entire match)
    print(match.group(0))    # 'info@example.com' (same as group())
    print(match.group(1))    # 'info' (first group)
    print(match.group(2, 3)) # ('example', 'com') (multiple groups)
    print(match.groups())    # ('info', 'example', 'com') (all groups)
    
    print(match.start())     # 13 (start position of entire match)
    print(match.end())       # 28 (end position of entire match)
    print(match.span())      # (13, 28) (start and end positions)
    
    print(match.start(1))    # 13 (start position of first group)
    print(match.end(1))      # 17 (end position of first group)
    print(match.span(1))     # (13, 17) (start and end positions of first group)
    
    print(match.string)      # 'Contact us at info@example.com or support@company.org' (input string)
    print(match.re)          # re.compile('(\\w+)@(\\w+)\\.(\\w+)') (compiled pattern)
    print(match.lastindex)   # 3 (index of last matched capturing group)
    print(match.pos)         # 0 (position where search started)
    print(match.endpos)      # 57 (position where search ended)
```

## Common Regex Patterns

```python
import re

# Email validation
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
print(re.match(email_pattern, "user@example.com"))  # Match object
print(re.match(email_pattern, "invalid@email"))     # None

# URL validation
url_pattern = r"https?://(?:www\.)?[-a-zA-Z0-9@:%._+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_+.~#?&/=]*)"
print(re.match(url_pattern, "https://www.example.com"))  # Match object
print(re.match(url_pattern, "invalid-url"))             # None

# Date validation (YYYY-MM-DD)
date_pattern = r"^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
print(re.match(date_pattern, "2023-01-15"))  # Match object
print(re.match(date_pattern, "2023-13-42"))  # None

# Strong password validation
# At least 8 chars, one uppercase, one lowercase, one number, one special char
password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
print(re.match(password_pattern, "Passw0rd!"))   # Match object
print(re.match(password_pattern, "password"))    # None

# Phone number validation (US)
phone_pattern = r"^\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})$"
print(re.match(phone_pattern, "(123) 456-7890"))  # Match object
print(re.match(phone_pattern, "123-456-7890"))    # Match object
print(re.match(phone_pattern, "12345"))           # None

# IP address validation (IPv4)
ipv4_pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
print(re.match(ipv4_pattern, "192.168.1.1"))        # Match object
print(re.match(ipv4_pattern, "256.256.256.256"))    # None

# Credit card number validation (simplified)
cc_pattern = r"^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|6(?:011|5[0-9]{2})[0-9]{12})$"
print(re.match(cc_pattern, "4111111111111111"))  # Match object (Visa)
print(re.match(cc_pattern, "5500000000000004"))  # Match object (MasterCard)
print(re.match(cc_pattern, "1234567890"))        # None

# Extracting HTML tags
html = "<div class='container'><p>Paragraph text</p></div>"
print(re.findall(r"<([a-z0-9]+)(?:\s[^>]*)?>(.*?)</\1>", html))
# [('div', "<p>Paragraph text</p>"), ('p', 'Paragraph text')]
```

## Advanced Techniques

### Working with Multiline Text

```python
import re

multiline_text = """First line
Second line with a number 42
Third line
Last line with another number 123"""

# Find lines containing numbers
number_lines = re.findall(r"^.*\d+.*$", multiline_text, re.MULTILINE)
print(number_lines)  # ['Second line with a number 42', 'Last line with another number 123']

# Match text between specific markers
content = """<start>
This is the content
we want to extract
</start>"""

between_markers = re.search(r"<start>(.*?)</start>", content, re.DOTALL)
print(between_markers.group(1).strip())
# This is the content
# we want to extract
```

### Parsing and Extracting Data

```python
import re

# Extract all email addresses
text = "Contact john.doe@example.com or jane@company.org for information."
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)  # ['john.doe@example.com', 'jane@company.org']

# Extract key-value pairs
config = """
# Configuration file
name = John Doe
email = john@example.com
age = 30
# End of basic info
"""

# Using named groups for better organization
kv_pattern = r"^(?P<key>\w+)\s*=\s*(?P<value>.+)$"
settings = {}
for line in config.splitlines():
    match = re.match(kv_pattern, line.strip())
    if match:
        settings[match.group('key')] = match.group('value')
print(settings)  # {'name': 'John Doe', 'email': 'john@example.com', 'age': '30'}

# Parsing CSV-like data
csv_line = "John,Doe,42,New York"
fields = re.split(r",\s*", csv_line)
print(fields)  # ['John', 'Doe', '42', 'New York']

# More complex CSV parsing (handling quoted fields)
complex_csv = 'Name,"Doe, John",42,"New York, NY"'
pattern = r',\s*(?=(?:[^"]*"[^"]*")*[^"]*$)'
fields = re.split(pattern, complex_csv)
print(fields)  # ['Name', '"Doe, John"', '42', '"New York, NY"']
```

### Performance Optimization

```python
import re
import time

# Example 1: Precompiling patterns for better performance
def measure_time(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"Execution time: {(end - start) * 1000:.2f} ms")
    return result

text = "Python" * 10000

# Not precompiled - slower
def search_not_compiled():
    return len(re.findall(r"Python", text))

# Precompiled - faster
pattern = re.compile(r"Python")
def search_compiled():
    return len(pattern.findall(text))

measure_time(search_not_compiled)  # Slower
measure_time(search_compiled)      # Faster

# Example 2: Avoid catastrophic backtracking
safe_pattern = re.compile(r"[a-z]+")  # Efficient
risky_pattern = re.compile(r"([a-z]+)*")  # Potential backtracking issues

# Example 3: Using more specific patterns
text = "The quick brown fox jumps over the lazy dog."

# Less efficient - needs to check entire string character by character
re.search(r".*fox", text)

# More efficient - can stop once it finds 'fox'
re.search(r"fox", text)
```

### Working with Unicode

```python
import re

# Unicode matching with re.UNICODE flag
text = "Python es divertido. 这很有趣. ممتع جدا."

# Match letters from any language
print(re.findall(r"\w+", text, re.UNICODE))
# ['Python', 'es', 'divertido', '这很有趣', 'ممتع', 'جدا']

# Unicode categories
# \p{Letter} - any kind of letter from any language
# \p{Uppercase_Letter} - uppercase letter
# \p{Lowercase_Letter} - lowercase letter
# \p{Digit} - any ASCII digit
# \p{Punctuation} - any punctuation character
# Note: Python's re doesn't directly support \p{}, use alternative below

# For better Unicode support, use the regex module instead of re
# pip install regex
import regex

# Using Unicode properties
all_letters = regex.findall(r"\p{Letter}+", text)
print(all_letters)  # ['Python', 'es', 'divertido', '这很有趣', 'ممتع', 'جدا']

# Match specific scripts
print(regex.findall(r"\p{Script=Han}+", text))  # ['这很有趣']
print(regex.findall(r"\p{Script=Arabic}+", text))  # ['ممتع', 'جدا']
print(regex.findall(r"\p{Script=Latin}+", text))  # ['Python', 'es', 'divertido']
```

### Debugging Regex

```python
import re

# Using re.DEBUG flag to see how the pattern is interpreted
pattern = re.compile(r"[a-z]+\d+", re.DEBUG)
# Output shows internal regex engine parsing

# Debugging with re.VERBOSE flag for readable patterns
phone_regex = re.compile(r"""
    \(          # Opening parenthesis
    (\d{3})     # Area code
    \)          # Closing parenthesis
    [ -]?       # Optional space or dash
    (\d{3})     # First 3 digits
    [-]         # Dash
    (\d{4})     # Last 4 digits
""", re.VERBOSE)

match = phone_regex.search("Call (123) 456-7890 today")
if match:
    print(match.groups())  # ('123', '456', '7890')

# Print partial matches to debug
def debug_regex(pattern, text):
    regex = re.compile(pattern)
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    
    match = regex.search(text)
    if match:
        print(f"Match found: {match.group()}")
        print(f"Groups: {match.groups()}")
        print(f"Position: {match.span()}")
    else:
        # Try to find where matching fails
        for i in range(len(text) + 1):
            partial = text[:i]
            if regex.search(partial):
                print(f"Partial match up to index {i-1}: {partial}")
            else:
                if i > 0 and regex.search(partial[:-1]):
                    print(f"Matching fails at index {i-1}: '{partial[-1]}'")
                    break
        print("No match found")

# Example usage
debug_regex(r"^\d{2}-\d{2}-\d{4}$", "12-34-20z5")
# Pattern: ^\d{2}-\d{2}-\d{4}$
# Text: 12-34-20z5
# Partial match up to index 8: 12-34-20
# Matching fails at index 8: 'z'
# No match found
```

## Using the regex Module (Extended Features)

```python
# pip install regex
import regex

# 1. Unicode category properties \p{} (not in standard re)
text = "Python 3.9 - €20.00 😀"
print(regex.findall(r"\p{Letter}+", text))  # ['Python']
print(regex.findall(r"\p{Number}+", text))  # ['3', '9', '20', '00']
print(regex.findall(r"\p{Currency_Symbol}", text))  # ['€']
print(regex.findall(r"\p{Emoji}", text))  # ['😀']

# 2. Possessive quantifiers (atomic grouping)
# Standard greedy: (?>...) - match once and never backtrack
print(regex.search(r'(?>a+)a', 'aaa'))  # None (possessive a+ consumes all 'a's)

# 3. Variable-width lookbehind (re only supports fixed-width)
print(regex.findall(r'(?<=\d{2,4})', '123abc'))  # [''] (matches after 123)

# 4. Named groups with alternation without duplication
pattern = regex.compile(r'(?<first>foo)|(?<first>bar)')
match = pattern.match('foo')
print(match.group('first'))  # 'foo'

# 5. Recursive patterns
# Match nested parentheses
nested = regex.compile(r'\((?:[^()]++|(?R))*\)')
print(nested.search('(simple)').group())  # '(simple)'
print(nested.search('(nested (example))').group())  # '(nested (example))'

# 6. Set operations
# Character class set operations: & (intersection), - (difference), ~ (negation)
vowels_and_digits = regex.findall(r'[aeiou\d]', 'a1e2i3o4u5')
print(vowels_and_digits)  # ['a', '1', 'e', '2', 'i', '3', 'o', '4', 'u', '5']

vowels_only = regex.findall(r'[aeiou--\d]', 'a1e2i3o4u5')
print(vowels_only)  # ['a', 'e', 'i', 'o', 'u']
```

## Practical Examples

### Tokenizing Text

```python
import re

def tokenize(text):
    # Remove punctuation and split into words
    words = re.findall(r'\b\w+\b', text.lower())
    return words

text = "Hello, world! This is a sample text with some punctuation, numbers (123), and mixed-case Words."
tokens = tokenize(text)
print(tokens)
# ['hello', 'world', 'this', 'is', 'a', 'sample', 'text', 'with', 'some', 'punctuation', 'numbers', '123', 'and', 'mixed', 'case', 'words']
```

### Data Extraction and Validation

```python
import re

# Extract specific information from text
report = """
Patient ID: P12345
Name: John Smith
Age: 45
Test Results:
- Cholesterol: 185 mg/dL (normal range: <200 mg/dL)
- Blood Pressure: 120/80 mmHg
- Blood Sugar: 92 mg/dL (normal range: 70-100 mg/dL)
"""

# Extract patient information using named groups
patient_info = re.search(r'Patient ID: (?P<id>\w+)\s+Name: (?P<name>[\w\s]+)\s+Age: (?P<age>\d+)', report)
==============================================================
# ...continued from previous code
if patient_info:
    print(patient_info.groupdict())
    # {'id': 'P12345', 'name': 'John Smith', 'age': '45'}

# Extract test results using regular expressions
test_results = re.findall(r'- (\w+(?:\s\w+)?): ([\d/]+)\s*(\w+(?:/\w+)?)', report)
print(test_results)
# [('Cholesterol', '185', 'mg/dL'), ('Blood Pressure', '120/80', 'mmHg'), ('Blood Sugar', '92', 'mg/dL')]

# Validate data format
def validate_date(date_str):
    pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$'
    return bool(re.match(pattern, date_str))

print(validate_date("12/31/2023"))  # True
print(validate_date("13/01/2023"))  # False (invalid month)
=================================================
#Log File Analysis:
-------------------
import re

log_data = """
[2023-01-15 08:45:32] INFO: Application started
[2023-01-15 08:46:12] WARNING: High memory usage detected (85%)
[2023-01-15 08:47:55] ERROR: Database connection failed
[2023-01-15 08:48:10] INFO: Retrying database connection
[2023-01-15 08:48:15] INFO: Database connection established
"""

# Extract log entries with timestamps, level, and message
log_pattern = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] (\w+): (.+)'
log_entries = re.findall(log_pattern, log_data)
print(log_entries)
# [('2023-01-15 08:45:32', 'INFO', 'Application started'),
#  ('2023-01-15 08:46:12', 'WARNING', 'High memory usage detected (85%)'),
#  ...etc]

# Filter for specific log levels
error_logs = [entry for entry in log_entries if entry[1] == 'ERROR']
print(error_logs)
# [('2023-01-15 08:47:55', 'ERROR', 'Database connection failed')]

# Parse log data into structured format
structured_logs = []
for timestamp, level, message in log_entries:
    structured_logs.append({
        'timestamp': timestamp,
        'level': level,
        'message': message
    })
print(structured_logs[0])
# {'timestamp': '2023-01-15 08:45:32', 'level': 'INFO', 'message': 'Application started'}
#--------------------------------------------------------------------------------
#HTML Parsing and Scraping

import re

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Sample Page</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p class="intro">This is an introductory paragraph.</p>
    <ul>
        <li><a href="https://example.com">Example Link</a></li>
        <li><a href="https://google.com">Google</a></li>
        <li><a href="https://github.com">GitHub</a></li>
    </ul>
    <p>Another paragraph with <b>bold text</b> and <i>italic text</i>.</p>
</body>
</html>
"""

# Extract title
title = re.search(r'<title>(.*?)</title>', html_content, re.DOTALL)
print(title.group(1))  # "Sample Page"

# Extract all links
links = re.findall(r'<a href="(https?://.*?)">(.*?)</a>', html_content)
print(links)
# [('https://example.com', 'Example Link'), 
#  ('https://google.com', 'Google'), 
#  ('https://github.com', 'GitHub')]

# Extract paragraphs
paragraphs = re.findall(r'<p(?:\s+[^>]*)?>(.*?)</p>', html_content, re.DOTALL)
print(paragraphs)
# ['This is an introductory paragraph.', 
#  'Another paragraph with <b>bold text</b> and <i>italic text</i>.']

# Remove all HTML tags to get plain text
def strip_html_tags(text):
    return re.sub(r'<[^>]+>', '', text)

plain_text = strip_html_tags(html_content)
print(plain_text.strip())
# Sample Page
# Welcome to My Website
# This is an introductory paragraph.
# Example Link
# Google
# GitHub
# Another paragraph with bold text and italic text.


#-------------------------------------------
#Working with Files and Path Validation
import re

# Validate and parse file paths
file_path = "C:\\Users\\username\\Documents\\report-2023.xlsx"

# Parse Windows path components
win_path_pattern = r'([A-Za-z]:\\)((?:[^\\]+\\)*)([^\\]+)\.([^\\\.]+)'
win_match = re.match(win_path_pattern, file_path)

if win_match:
    drive = win_match.group(1)  # 'C:\\'
    directory = win_match.group(2)  # 'Users\\username\\Documents\\'
    filename = win_match.group(3)  # 'report-2023'
    extension = win_match.group(4)  # 'xlsx'
    
    print(f"Drive: {drive}")
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")
    print(f"Extension: {extension}")

# Parse Unix path components
unix_path = "/home/username/documents/report-2023.txt"
unix_path_pattern = r'(/(?:.*/)*)([^/]+)\.([^/\.]+)'
unix_match = re.match(unix_path_pattern, unix_path)

if unix_match:
    directory = unix_match.group(1)  # '/home/username/documents/'
    filename = unix_match.group(2)  # 'report-2023'
    extension = unix_match.group(3)  # 'txt'
    
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")
    print(f"Extension: {extension}")
#-------------------------------------------
#Text Processing and Analysis

import re

# Sentence tokenization
text = "Hello! This is a sample text. It contains multiple sentences. Are you ready? Let's go!"

sentences = re.split(r'(?<=[.!?])\s+', text)
print(sentences)
# ['Hello!', 'This is a sample text.', 'It contains multiple sentences.', 'Are you ready?', "Let's go!"]

# Word frequency analysis
def word_frequency(text):
    # Convert to lowercase and find all words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count frequencies
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    return freq

sample_text = "The quick brown fox jumps over the lazy dog. The dog barks, but the fox is already gone."
frequencies = word_frequency(sample_text)
print(frequencies)
# {'the': 4, 'quick': 1, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 
#  'dog': 2, 'barks': 1, 'but': 1, 'is': 1, 'already': 1, 'gone': 1}

# Find most common words
sorted_words = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
print(f"Most common words: {sorted_words[:3]}")
# Most common words: [('the', 4), ('fox', 2), ('dog', 2)]

#-------------------------------------------
#Data Cleaning and Normalization

import re

# Standardize phone numbers
phone_numbers = [
    "(123) 456-7890",
    "123-456-7890",
    "123.456.7890",
    "+1 123 456 7890",
    "1234567890"
]

def normalize_phone(phone):
    # Remove all non-digit characters
    digits_only = re.sub(r'\D', '', phone)
    
    # Format as XXX-XXX-XXXX
    if len(digits_only) == 10:
        return f"{digits_only[:3]}-{digits_only[3:6]}-{digits_only[6:]}"
    elif len(digits_only) == 11 and digits_only[0] == '1':
        return f"{digits_only[1:4]}-{digits_only[4:7]}-{digits_only[7:]}"
    else:
        return "Invalid phone number"

for phone in phone_numbers:
    print(f"{phone} -> {normalize_phone(phone)}")
# (123) 456-7890 -> 123-456-7890
# 123-456-7890 -> 123-456-7890
# 123.456.7890 -> 123-456-7890
# +1 123 456 7890 -> 123-456-7890
# 1234567890 -> 123-456-7890

# Clean and normalize text
def normalize_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    
    # Remove special characters
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove leading/trailing whitespace
    text = text.strip()
    
    return text

messy_text = "  Hello,   World! This is some  messy text with; punctuation.   "
clean_text = normalize_text(messy_text)
print(clean_text)  # "hello world this is some messy text with punctuation"

#-------------------------------------------
#Advanced Regex Projects
##Building a Simple Markdown Parser

import re

def parse_markdown(text):
    # Process headers
    text = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    
    # Process bold and italic
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    
    # Process lists
    text = re.sub(r'^\- (.*?)$', r'<li>\1</li>', text, flags=re.MULTILINE)
    # Wrap list items in <ul> tags
    text = re.sub(r'(<li>.*?</li>)\n(?!<li>)', r'<ul>\1</ul>\n', text, flags=re.DOTALL)
    
    # Process links
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)
    
    # Process paragraphs
    text = re.sub(r'^(?!<[a-z]).+$', r'<p>\g<0></p>', text, flags=re.MULTILINE)
    
    return text

markdown_text = """
# Sample Markdown

This is a **bold text** and *italic text*.

## List Example
- Item 1
- Item 2
- Item 3

Visit [Google](https://www.google.com)
"""

html_output = parse_markdown(markdown_text)
print(html_output)

#----------------------------------------
#Creating a Custom Configuration Parser

import re

def parse_config(config_text):
    # Initialize data structure
    config = {
        'global': {},
        'sections': {}
    }
    
    current_section = 'global'
    
    # Define patterns
    section_pattern = r'^\[([^\]]+)\]$'
    kv_pattern = r'^([^=]+)=(.*)$'
    comment_pattern = r'^#.*$'
    
    # Process each line
    for line in config_text.split('\n'):
        line = line.strip()
        
        # Skip empty lines and comments
        if not line or re.match(comment_pattern, line):
            continue
        
        # Check if it's a section header
        section_match = re.match(section_pattern, line)
        if section_match:
            current_section = section_match.group(1)
            if current_section not in config['sections']:
                config['sections'][current_section] = {}
            continue
        
        # Process key-value pairs
        kv_match = re.match(kv_pattern, line)
        if kv_match:
            key = kv_match.group(1).strip()
            value = kv_match.group(2).strip()
            
            # Handle quoted strings
            if (value.startswith('"') and value.endswith('"')) or \
               (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]
            # Handle numbers
            elif re.match(r'^-?\d+$', value):
                value = int(value)
            elif re.match(r'^-?\d+\.\d+$', value):
                value = float(value)
            # Handle booleans
            elif value.lower() in ('true', 'yes', 'on'):
                value = True
            elif value.lower() in ('false', 'no', 'off'):
                value = False
            
            # Store the key-value pair in the appropriate section
            if current_section == 'global':
                config['global'][key] = value
            else:
                config['sections'][current_section][key] = value
    
    return config

sample_config = """
# Global settings
debug=true
log_level="info"

[database]
host=localhost
port=5432
user="admin"
password="secret"

[application]
name="My App"
version=2.1
max_connections=100
"""

config = parse_config(sample_config)
print(config)
