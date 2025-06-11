import json
from typing import List, Dict



def generate_supporting_plaintiff_prompt(case_summary, similar_cases, ipc_sections_with_desc, evidence_types, opposing_arguments):
    return f"""
You are a seasoned trial lawyer representing the **plaintiff** in a serious legal case. You are now delivering your **opening argument** in court to support your client’s claim.

Use the following inputs:
- **Case Summary**: {case_summary}
- **Similar Cases**: {similar_cases}
- **IPC Sections with Descriptions**: {ipc_sections_with_desc}
- **Evidence Types Which this type of cases mostly need**: {evidence_types}

🧠 Think like a persuasive, ethical lawyer. Draw from precedent, law, and logic. If evidence seems weak, emphasize emotional appeals, victim rights, or judicial responsibility.

**IMPORTANT**: 
✅ Return only **ONE** item as an array with exactly one object.  
❌ Do not include more than one point or multiple JSON entries.  
✅ Output **must** follow the exact JSON format below.

[
  {{
    "point": "Insert your argument point here",
    "evidence": ["Insert key supporting evidence here"],
    "demand": "Insert demand for judgment or penalty"
  }}
]
"""


def generate_continue_supporting_prompt(case_summary, similar_cases, ipc_sections_with_desc, evidence_types, opposing_arguments):
    return f"""
You are continuing your argument as the **plaintiff’s lawyer**, now responding to the opposing side.

Inputs:
- **Case Summary**: {case_summary}
- **Similar Cases**: {similar_cases}
- **IPC Sections with Descriptions**: {ipc_sections_with_desc}
- **Evidence Types Which this type of cases mostly need**: {evidence_types}
- **Opposing Arguments**: {opposing_arguments}

👨‍⚖️ Use this opportunity to refute, reinforce, or raise urgency. If needed, request supplementary evidence, re-investigation, or emotionally appeal.

**IMPORTANT**: 
✅ Return only **ONE** item as an array with exactly one object.  
❌ Do not include more than one point or multiple JSON entries.  
✅ Output **must** follow the exact JSON format below.

[
  {{
    "point": "Reinforcement or new supporting point",
    "evidence": ["Evidence that refutes opposition or adds new weight"],
    "demand": "Final plea or renewed request to the judge"
  }}
]
"""

