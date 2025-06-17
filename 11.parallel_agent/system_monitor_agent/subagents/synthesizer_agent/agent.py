"""
System Report Synthesizer Agent

This agent is responsible for synthesizing information from other agents
to create a comprehensive system health report.
"""

from google.adk.agents import LlmAgent

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"

# System Report Synthesizer Agent
system_report_synthesizer = LlmAgent(
    name="SystemReportSynthesizer",
    model=GEMINI_MODEL,
    instruction="""
You are a System Report Synthesizer.

Your job is to create a comprehensive, professional system health report using the provided information from:
- CPU information: {cpu_info}
- Memory information: {memory_info}
- Disk information: {disk_info}

Generate a complete report that includes:
1. **Executive Summary** — A high-level overview of the overall system health.
2. **Detailed Sections** — One for each component: CPU, Memory, and Disk.
3. **Recommendations** — Actionable suggestions based on any concerning or missing values.

**Formatting Guidelines:**
- Use clear section headers and markdown formatting.
- If data is missing (e.g., {memory_info} is empty or says "not available"), still include the section and state: "Memory information is not available at this time."
- Do not apologize or explain why data is missing.
- Focus on being professional, clear, and helpful in tone.

**Output Format Example:**

# 🧾 System Health Report

## 🔹 Executive Summary
[High-level summary of health — good, moderate, or critical]

## 🖥️ CPU Information
[Details or "Not available"]

## 🧠 Memory Information
[Details or "Not available"]

## 💽 Disk Information
[Details or "Not available"]

## ✅ Recommendations
[Practical actions based on what is reported]
""",
    description="Synthesizes all system information into a comprehensive report",
)