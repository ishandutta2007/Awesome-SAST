import os
import subprocess

repo_dir = r'C:\Users\ishan\Documents\Projects\Awesome-SAST'
readme_path = os.path.join(repo_dir, 'README.md')
assets_dir = os.path.join(repo_dir, 'assets')
os.makedirs(assets_dir, exist_ok=True)

with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

def run_git(msg):
    cmd = f'git add . && git commit -m "{msg}" && git push'
    subprocess.run(cmd, shell=True, cwd=repo_dir)

# Step 1: Open-source projects with star badges and sorted
open_source_start = content.find('### Dedicated SAST & Code Analysis Tools')
open_source_end = content.find('### Additional Strong Open-Source Options')

new_os_section = '''### Dedicated SAST & Code Analysis Tools

- **[ESLint](https://github.com/eslint/eslint)** (with security plugins) [![Stars](https://img.shields.io/github/stars/eslint/eslint?style=social&color=white)](https://github.com/eslint/eslint/stargazers)  
  Pluggable linting utility for JavaScript and JSX with security rule sets.

- **[Trivy](https://github.com/aquasecurity/trivy)** [![Stars](https://img.shields.io/github/stars/aquasecurity/trivy?style=social&color=white)](https://github.com/aquasecurity/trivy/stargazers)  
  Comprehensive security scanner with SAST-like capabilities for code and dependencies.

- **[SonarQube Community Edition](https://github.com/SonarSource/sonarqube)** [![Stars](https://img.shields.io/github/stars/SonarSource/sonarqube?style=social&color=white)](https://github.com/SonarSource/sonarqube/stargazers)  
  Leading open-source code quality and security analysis platform with continuous inspection.

- **[Semgrep](https://github.com/semgrep/semgrep)** [![Stars](https://img.shields.io/github/stars/semgrep/semgrep?style=social&color=white)](https://github.com/semgrep/semgrep/stargazers)  
  Lightweight, fast, and highly customizable static analysis tool with community rules for many languages.

- **[Gosec](https://github.com/securego/gosec)** [![Stars](https://img.shields.io/github/stars/securego/gosec?style=social&color=white)](https://github.com/securego/gosec/stargazers)  
  Golang security checker with static analysis for common vulnerabilities.

- **[CodeQL](https://github.com/github/codeql)** [![Stars](https://img.shields.io/github/stars/github/codeql?style=social&color=white)](https://github.com/github/codeql/stargazers)  
  Open-source semantic code analysis engine used by GitHub for finding vulnerabilities.

- **[Brakeman](https://github.com/presidentbeef/brakeman)** [![Stars](https://img.shields.io/github/stars/presidentbeef/brakeman?style=social&color=white)](https://github.com/presidentbeef/brakeman/stargazers)  
  Static analysis security scanner for Ruby on Rails applications.

- **[Bandit](https://github.com/PyCQA/bandit)** [![Stars](https://img.shields.io/github/stars/PyCQA/bandit?style=social&color=white)](https://github.com/PyCQA/bandit/stargazers)  
  Python-specific static security analyzer with a focus on common vulnerabilities.

- **[PMD](https://github.com/pmd/pmd)** [![Stars](https://img.shields.io/github/stars/pmd/pmd?style=social&color=white)](https://github.com/pmd/pmd/stargazers)  
  Source code analyzer for Java, JavaScript, and other languages with security rules.

- **[SpotBugs](https://github.com/spotbugs/spotbugs)** [![Stars](https://img.shields.io/github/stars/spotbugs/spotbugs?style=social&color=white)](https://github.com/spotbugs/spotbugs/stargazers)  
  Successor to FindBugs for Java bytecode static analysis.
'''

if open_source_start != -1 and open_source_end != -1:
    content = content[:open_source_start] + new_os_section + '\n' + content[open_source_end:]
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    run_git('Added github stars and sorted the opensource based on that')

# Step 2: Banner
svg_banner = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4facfe" />
      <stop offset="100%" stop-color="#00f2fe" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#bg)" rx="15" />
  <text x="50%" y="50%" font-family="Arial, sans-serif" font-size="48" font-weight="bold" fill="white" text-anchor="middle" dominant-baseline="middle">Awesome SAST</text>
  <text x="50%" y="75%" font-family="Arial, sans-serif" font-size="24" fill="white" text-anchor="middle">Static Application Security Testing Ecosystem</text>
</svg>'''
with open(os.path.join(assets_dir, 'banner.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_banner)

content = '![Awesome SAST Banner](./assets/banner.svg)\n\n' + content
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
run_git('added banner')

# Step 3: Emojis
content = content.replace('## Table of Contents', '## 📑 Table of Contents')
content = content.replace('## SaaS Products', '## ☁️ SaaS Products')
content = content.replace('## Open-Source GitHub Projects', '## 🔓 Open-Source GitHub Projects')
content = content.replace('## How to Contribute', '## 🤝 How to Contribute')
content = content.replace('## Disclaimer', '## ⚠️ Disclaimer')
content = content.replace('### Core Platforms (SAST Tools)', '### 🏢 Core Platforms (SAST Tools)')
content = content.replace('### Dedicated SAST & Code Analysis Tools', '### 🔍 Dedicated SAST & Code Analysis Tools')
content = content.replace('### Additional Strong Open-Source Options', '### ⭐ Additional Strong Open-Source Options')

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
run_git('added emojis')

# Step 4: SEO Optimised
content = content.replace('# Awesome-SAST', '# Awesome SAST - The Ultimate Curated List of Static Application Security Testing Tools')
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
run_git('seo optimised')

# Step 5: Badges to left
left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a> '
content = content.replace('# Awesome SAST - The Ultimate Curated List of Static Application Security Testing Tools\n', '# Awesome SAST - The Ultimate Curated List of Static Application Security Testing Tools\n\n' + left_badges)
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
run_git('badges to left added')

# Step 6: Badges to right
right_badge = ' <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'
# Insert right after left badges
content = content.replace(left_badges, left_badges + right_badge + '\n')
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
run_git('badges to right added')

# Step 7: Star history
star_history = '''
## 📈 Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-SAST&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-SAST&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-SAST&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-SAST&type=date&legend=bottom-right" />
</picture>
</a>
</div>
'''
content = content + star_history
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
run_git('star history added')

# Step 8: Replace chartrepos with chart?repos
content = content.replace('chartrepos', 'chart?repos')
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
run_git('fixed star plot')

# Step 9: Replace sindresorhus awesome
content = content.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
run_git('invalid awesome link fixed')
