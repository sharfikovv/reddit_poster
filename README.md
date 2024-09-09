## Reddit Post Scheduler

This repository contains a Python script designed to automate the scheduling and posting of content to subreddits. The script allows you to set a list of titles, images, and flairs for your posts, making it easy to manage and plan your content.

### Key Features:
- **Image Uploading**: Images are automatically reuploaded to Imgur, ensuring smooth posting without direct image links.
- **Time Randomization**: Post times are randomized by ±15 minutes to avoid being immediately flagged as spam by Reddit's algorithms.
- **Credential Management**: Reddit credentials are stored in a separate configuration file keeping them organized.
- **Libraries Used**: The script utilizes the following Python libraries: `praw` for Reddit API interaction, `schedule` for timing tasks, `prawcore` for core Reddit API functionality, and `datetime` for managing post schedules.

### Important Notice:
This script must be used responsibly and in compliance with Reddit’s terms of service. It is **not** intended for purposes that violate Reddit's policies, including but not limited to:
- **Spam**
- **Advertising**
- **Scams**
- **Any other prohibited activities**

Misuse of this script can lead to account suspension or permanent bans from Reddit. Always ensure your actions are in line with Reddit’s guidelines.

### Setup Instructions:
1. Clone this repository.
2. Install the required Python libraries:
   ```
   pip install praw schedule prawcore datetime
   ```
3. Set up your titles, images, flairs and schedule by using files that included in the repo.
4. Run the script to start scheduling your posts.

This tool is perfect for users who need to manage multiple posts across various subreddits without manual intervention, provided it is used ethically and within Reddit’s rules.