# Practical Bug Bounty Content

Welcome to the Practical Bug Bounty Content repository. This repository is designed to house structured content for the course, organized in a hierarchical folder structure for ease of use and contribution.


# Practical Bug Bounty Course Content

- **Module 1: Basics**
  - **Submodule: Writing a Report**
    - Topic: Report Writing
      - Video: HTTP Request Smuggling - False Positives by PinkDraconian
      - Video: Q: How to write a BUG BOUNTY report that actually gets paid?
      - Note: The Importance of Report Writing in Bug Bounty
      - Additional Link: [Reporting Tips: Using Markdown](https://www.zerocopter.com/blog-en/reporting-tips-using-markdown-to-make-your-report-look-better)
      - Additional Link: [Reporting tips: setting the severity of a report with the CVSS calculator](https://www.zerocopter.com/blog-en/reporting-tips-setting-the-severity-of-a-report-with-the-cvss-calculator)
    - Topic: Understanding CVSS
      - Video: What is CVSS? | Common Vulnerability Scoring System
    - ...
  - **Submodule: Scope**
    - ...
- **Module 2: ...**
  - ...


## Folder Structure

- Each `module` is a directory.
- Within each `module`, there are `submodules`, which are also directories.
- Each `submodule` contains `topics`, which are again directories.
- Each `topic` directory can have:
  - `info.json`: Contains metadata about the topic.
  - `videos.json`: Contains a list of video references associated with the topic.
  - `notes.md`: Contains any textual notes or additional information about the topic.
  - `links.json`: Contains a list of external links related to the topic.

## How to Generate New Content

1. Navigate to the desired location in the folder structure.
2. Modify existing files or add new files as required. Ensure you follow the structure mentioned above.
3. Once you've added or modified content, navigate to the repository root and run the converter script:

python3 folder_to_json_converter.py

This script will traverse the folder structure, collect the data, and generate a Django-compatible JSON dump.

## Examples

## Detailed Example: Generating an Entire Module

In this example, we will create a new module named `Web Security`, a submodule named `XSS Attacks`, and a topic named `Reflected XSS`.

### 1. Creating a New Module

To create a new module:

- Navigate to the root content directory.
- Create a directory named `Web Security`.

### 2. Adding a Submodule

Within the `Web Security` directory:

- Create a directory named `XSS Attacks`.

### 3. Adding a Topic

Inside the `XSS Attacks` directory:

- Create a directory named `Reflected XSS`.

### 4. Adding Metadata to the Topic

Inside the `Reflected XSS` directory:

- Create a file named `info.json`.
- Add the following content to `info.json`:

```json
{
  "description": "An introduction to Reflected XSS attacks."
}
```
### 5. Adding Videos to the Topic

- Still within the Reflected XSS directory, create a file named `videos.json`.
- Add the following content to `videos.json`:

```json
[
  {
    "title": "Understanding Reflected XSS",
    "url": "https://youtube.com/examplelink1"
  }
]
```

### 6. Adding Notes to the Topic

- Create a file named `notes.md` in the same directory.
- Add your notes. For example:

```markdown
# Reflected XSS

Reflected XSS attacks are a type of XSS where the injected script is reflected off a web server
``` 
### 7. Adding External Links

- Create a file named `links.json`.
- Add the following content:

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

Remember to run the converter script after making changes to generate an updated JSON dump.
