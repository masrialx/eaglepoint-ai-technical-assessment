
```markdown
# EaglePoint AI – Full-Stack Developer Technical Assessment

**Candidate:** Masri  
**Email:** your-email@example.com  
**Date:** November 28, 2025  

This repository contains my complete submission for the EaglePoint AI Technical Assessment.  
I have implemented the following tasks using **Python 3**:

- Task 1 – Smart Text Analyzer  
- Task 3 – Rate Limiter  

Both solutions are fully functional, well-documented, tested, and follow clean code principles.

---

## Repository Structure

```
eaglepoint-ai-technical-assessment/
├── task1_smart_text_analyzer/
│   ├── analyzer.py          # Main script for text analysis
│   ├── example_input.txt    # Sample text file for testing
│   └── documentation.md     # In-depth explanation of approach & decisions
├── task3_rate_limiter/
│   ├── rate_limiter.py      # Rate limiter implementation + demo
│   └── documentation.md     # Detailed write-up for Task 3
└── README.md                # This file
```

---

## Task 1 – Smart Text Analyzer

### Features
- Total word count
- Average word length (rounded to 2 decimal places)
- Longest word(s) – handles ties correctly
- Word frequency map (case-insensitive)

### How to Run
```bash
cd task1_smart_text_analyzer
python analyzer.py
```

The script reads from `example_input.txt` by default and prints results to the console.

→ Full explanation, thought process, edge cases, and optimization reasoning are in [`task1_smart_text_analyzer/documentation.md`](./task1_smart_text_analyzer/documentation.md).

---

## Task 3 – Rate Limiter

### Features
- 5 requests per 60-second sliding window per user
- Thread-safe implementation
- Automatic cleanup of old entries
- Clear block/allow feedback

### How to Run (Demo)
```bash
cd task3_rate_limiter
python rate_limiter.py
```

The script runs a simulated load for several user IDs so you can instantly see the limiter in action.

→ Complete design decisions, alternatives considered, time complexity, and testing notes are in [`task3_rate_limiter/documentation.md`](./task3_rate_limiter/documentation.md).

---

## General Notes

- Written and tested with **Python 3.11+**
- No external dependencies — runs with the standard library only
- Code is extensively commented and follows PEP 8
- All edge cases documented and handled

Thank you for the opportunity! I'm happy to answer any questions or add additional features/tasks.

Best regards,  
Masri
```

Just copy-paste the entire block above into your `README.md` — it will render beautifully on GitHub.

Would you also like me to write a polished submission message for the Google Form (with direct links to the repo and both task folders)? Just say the word! 🚀
