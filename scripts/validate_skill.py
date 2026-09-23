#!/usr/bin/env python3
"""
Validation script for Lean Startup agent skill.
Verifies YAML frontmatter, markdown code blocks, tables, and internal links.
"""

import glob
import os
import re
import sys

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    md_files = glob.glob(os.path.join(repo_root, "*.md"))
    
    if not md_files:
        print("Error: No markdown files found.")
        sys.exit(1)
        
    print(f"Found {len(md_files)} markdown files in {repo_root}")
    failed = False
    
    # 1. Check SKILL.md frontmatter
    skill_file = os.path.join(repo_root, "SKILL.md")
    if not os.path.exists(skill_file):
        print("Error: SKILL.md missing!")
        sys.exit(1)
        
    with open(skill_file, "r", encoding="utf-8") as f:
        skill_lines = f.readlines()
        
    if skill_lines[0].strip() != "---":
        print("Error: SKILL.md does not start with YAML frontmatter delimiter (---).")
        failed = True
    else:
        has_closing = False
        fm_content = []
        for line in skill_lines[1:]:
            if line.strip() == "---":
                has_closing = True
                break
            fm_content.append(line)
        if not has_closing:
            print("Error: SKILL.md has unclosed frontmatter delimiter.")
            failed = True
        else:
            fm_text = "".join(fm_content)
            if "name: lean-startup" not in fm_text:
                print("Error: SKILL.md frontmatter missing 'name: lean-startup'.")
                failed = True
            if "description:" not in fm_text:
                print("Error: SKILL.md frontmatter missing 'description'.")
                failed = True

    # 2. Check each markdown file
    for filepath in sorted(md_files):
        fname = os.path.basename(filepath)
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        in_code = False
        open_line = 0
        for i, line in enumerate(lines, 1):
            if line.startswith("```"):
                in_code = not in_code
                if in_code:
                    open_line = i
                    
            # Check table rows outside code
            if not in_code:
                s = line.strip()
                if s.startswith("|") and not s.endswith("|"):
                    print(f"Error in {fname}:{i} -> Malformed table row (missing trailing pipe): {s}")
                    failed = True
                    
            # Check relative links
            for text, link in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", line):
                if not link.startswith("http") and not link.startswith("#") and not link.startswith("mailto:"):
                    target_path = os.path.join(repo_root, link.split("#")[0])
                    if not os.path.exists(target_path):
                        print(f"Error in {fname}:{i} -> Broken relative link: [{text}]({link})")
                        failed = True

        if in_code:
            print(f"Error in {fname} -> Unclosed code fence starting at line {open_line}")
            failed = True
            
    if failed:
        print("\n❌ Validation FAILED.")
        sys.exit(1)
        
    print("\n✅ All validations passed cleanly!")
    sys.exit(0)

if __name__ == "__main__":
    main()
