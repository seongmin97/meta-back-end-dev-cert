## Software Collaboration
- Continuous Integration (CI): This practice involves automatically integrating code changes from multiple contributors into a shared repository several times a day. Automated tests are run to ensure that new code changes do not break existing functionality.
- Continuous Delivery (CD): This extends CI by ensuring that the software can be reliably released at any time. It involves automating the deployment process so that code changes can be pushed to production with minimal manual intervention. However, it still requires manual approval for the final deployment.
- Continuous Deployment: This takes it a step further by automating the deployment process entirely, meaning that every change that passes automated tests is automatically deployed to production without manual approval.

## Command Line
- Handling error
  - The number 2 represents standard error, and you can redirect errors to a file using 2> followed by the filename. You can also combine standard output and error using 2>&1.
  - `ls -l /usr/bin 2> error.txt`
  - `ls -l /usr/bin > error_output.txt 2>&`
- Pipe
- Grep

## Git
