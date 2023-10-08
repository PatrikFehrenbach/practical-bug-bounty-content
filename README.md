# 🚀 Welcome to the Practical Bug Bounty Content Repository! 🐞

This repository is meticulously crafted to serve as a home for structured content tailored for the course. With a carefully organized hierarchical folder structure, it ensures effortless navigation, accessibility, and seamless contribution. Dive in and explore the bounty of knowledge awaiting you! 📚✨

# Practical Bug Bounty Course Content 🎓

**Module 1: Basics 🕵️‍♂️**
- **Submodule: Writing a Report 📝**
  - **Topic: Report Writing 📑**
    - 🎥 Video: HTTP Request Smuggling - False Positives by PinkDraconian
    - 🎥 Video: Q: How to write a BUG BOUNTY report that actually gets paid?
    - 📌 Note: The Importance of Report Writing in Bug Bounty
    - 🔗 Additional Link: [Reporting Tips: Using Markdown](https://www.zerocopter.com/blog-en/reporting-tips-using-markdown-to-make-your-report-look-better)
    - 🔗 Additional Link: [Reporting tips: setting the severity of a report with the CVSS calculator](https://www.zerocopter.com/blog-en/reporting-tips-setting-the-severity-of-a-report-with-the-cvss-calculator)
  - **Topic: Understanding CVSS 🎯**
    - 🎥 Video: What is CVSS? | Common Vulnerability Scoring System
    - 📝 Explore the intricacies of the Common Vulnerability Scoring System (CVSS)
    - 🧠 Dive deep into the world of vulnerability scoring and severity assessment
  - ...

**Module 2: Advanced Techniques 🔍**
- **Submodule: Exploitation Strategies 💻**
  - ...

# Folder Structure 📂

- Each `module` is a directory that unlocks a new level of expertise.
- Within each `module`, you'll find `submodules`, gateways to specialized knowledge.
- Every `submodule` hosts various `topics`, where secrets of the trade are unveiled.
- In each `topic` directory, you'll discover:
  - `info.json`: Your map to the topic's key details.
  - `videos.json`: A treasure trove of video references, guiding you through the topic.
  - `notes.md`: Textual gems and insights, ensuring you grasp the essence.
  - `links.json`: Portals to external wisdom, expanding your horizons further.


### [Check our Targeted Topics to cover 😉](https://github.com/krishanthan4/practical-bug-bounty-content/blob/main/course-topics.md)
**Your input matters! Contribute to the listed topics 👆. If a new module is necessary, please Add it**

🌟 How to Generate New Content
Creating exciting and valuable content is as easy as a few simple steps. Let's dive into the magical world of content creation! ✨📚

1.Navigate to the desired location in the folder structure.
2.Modify existing files or add new files as required. Ensure you follow the structure mentioned above.
3.Once you've added or modified content, navigate to the repository root and run the converter script:

```python
python3 folder_to_json_converter.py
```

🪄 This script will traverse the folder structure, collecting data, and generating a Django-compatible JSON dump.

# 🌠 Examples
## 🚀 Detailed Example: Generating an Entire Module

In this adventure, we'll create a new module called `Web Security`, a submodule named `XSS Attacks`, and a topic named `Reflected XSS`. Let's embark on this epic quest! 🛡️🎯

### 1. Creating a New Module

- **Feel like a content architect**.
- Navigate to the root content directory and conjure up a directory named `Web Security`.

### 2. Adding a Submodule

- Continue your creative journey within the `Web Security` directory.
- Craft a directory named `XSS Attacks`.

### 3. Adding a Topic

- Venture deeper into the `XSS Attacks` directory.
- Imagine you're unearthing hidden treasures as you create a directory named `Reflected XSS`.

### 4. Adding Metadata to the Topic

- Inside the Reflected XSS directory, pen down a file named `info.json`.
- Enchant `info.json` with this content:
```json
{
  "description": "An introduction to RRemember to run the converter script after making changes to generate an updated JSON dump.eflected XSS attacks."
}
```

### 5. Adding Videos to the Topic

Within the Reflected XSS directory, weave a file named `videos.json`.
Craft `videos.json` with the following magic:
```json
[
  {
    "title": "Understanding Reflected XSS",
    "url": "https://youtube.com/examplelink1"
  }
]
```

### 6. Adding Notes to the Topic

- Summon a file named `notes.md` in the same directory.
- Pen down your knowledge, like an ancient scroll:

```md
# Reflected XSS

Reflected XSS attacks are a type of XSS where the injected script is reflected off a web server.
```
### 7. Adding External Links

- Create a file named `links.json`.
- Populate it with these gems:

```json
[
  {
    "url": "https://security.example.com/reflected-xss",
    "description": "Deep dive into Reflected XSS"
  }
]
```

### Adding a New Module

1. Create a new directory in the root folder with the module name.
2. Inside the module directory, you can add submodules as directories.
3. Each submodule can then have topics, and so on.

### Modifying a Topic

1. Navigate to the desired topic directory.
2. Open `info.json` to modify metadata, `videos.json` to add or modify videos, `notes.md` to edit notes, and `links.json` to update external links.

Please remember to execute the converter script after each modification to produce an up-to-date JSON dump.

Thank you for your valuable contributions to our Bug Bounty Plateform! Your expertise has played a crucial role in shaping this knowledge base. Together, we are making a difference in the cybersecurity world. Happy bug hunting! 🌟🔐✨
