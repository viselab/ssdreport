README for Excel Report Generation Playbook
Overview
This Ansible playbook is designed to automate the process of generating an Excel report based on SSSD (System Security Services Daemon) configuration across multiple web servers. The playbook is divided into four main sections, each responsible for a specific task in the workflow of report generation and distribution.

Sections of the Playbook
1. Setup Environment for Excel Report Generation
This section prepares the environment on the target web servers for report generation. It includes tasks to determine the RHEL (Red Hat Enterprise Linux) version and install the appropriate Python interpreter and pip based on the version.

Determine RHEL version: Identifies the RHEL version to decide the installation path.
Install Python3 and pip for RHEL 7 using yum: Installs Python3 and pip on RHEL 7 systems.
Install Python3 and pip for RHEL 8 or later using dnf: Installs Python3 and pip on RHEL 8 or later systems.
2. Check SSSD Configuration and Collect Data
This section checks the SSSD configuration on each web server and collects relevant data.

Check SSSD configuration: Checks for the simple_allow_groups configuration in the SSSD configuration file.
Assicurati che il file temporaneo esista (Ensure the temporary file exists): Creates a temporary file on the local machine to store SSSD data.
Write SSSD data to a temp file on localhost: Writes the collected SSSD configuration data to the temporary file.
3. Generate Excel Report on Localhost
After collecting the data, this section processes the data on the localhost and generates an Excel report.

Read SSSD data from temp file: Reads the data from the temporary file.
Decode SSSD data from base64: Decodes the data from base64 encoding.
Split SSSD data into lines and remove empty lines: Processes the data to prepare for report generation.
Generate Excel report for SSSD configuration using Python script: Generates an Excel report using the collected and processed data.
4. Commit Excel Reports to Git Repository
The final section handles the version control of the generated report by committing it to a Git repository.

Add Excel reports to Git: Stages the Excel report files for commit.
Commit Excel reports to Git: Commits the staged files with a predefined commit message.
Push Excel reports to Git: Pushes the commit to the main branch of the remote repository.
Prerequisites
Ansible installed on the control node.
Python3 and pip installed on the web servers (handled by the playbook).
Git configured on the machine where the reports are generated.
Usage
To execute this playbook, run the following command from your Ansible control node:

sh
Copy code
ansible-playbook path/to/excel_report_generation_playbook.yml
Ensure that you have the necessary inventory setup for your web servers under the web_servers group and that your control node has access to these servers.

Conclusion
This playbook automates the process of checking SSSD configurations, collecting data, generating an Excel report, and maintaining the report in a Git repository, thus streamlining the process and ensuring consistency across multiple web servers.
