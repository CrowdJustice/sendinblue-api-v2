# SendinBlue Python Library

This is the SendinBlue Python library. It implements the various exposed APIs that you can read more about on https://apidocs.sendinblue.com.

SendinBlue API's use HTTP Authentication through an api key. You can create your api key from [API Console](https://my.sendinblue.com/advanced/apikey), after you sign up for an account with SendinBlue. You must use latest version 2.0, access key, for accessing APIs.

You will need to install the following module

* requests

Compatibility:

 - Python 2.7/ Python 3.x

## Quickstart
Learn how to send email campaigns from your application using SendinBlue API.

You must sign up for SendinBlue account for using APIs. All our APIs require HTTP authentication using access key, which are accessible from your [API Console](https://my.sendinblue.com/advanced/apikey).

The following guides give you a start and understanding of how to use our API.

 * [Get all your campaigns](https://apidocs.sendinblue.com/how-to-get-all-you-campaigns/)
 * [Send transactional emails](https://apidocs.sendinblue.com/tutorial-sending-transactional-email/)
 * [Setup your webhooks](https://apidocs.sendinblue.com/how-to-setup-webhooks/)


1. You will need to first get the Access key from [SendinBlue](https://www.sendinblue.com).

2. Our library supports a timeout value, default is 30 Secs, which you can pass as 3rd parameter in Mailin class Object.

3. Assuming that you have cloned this git repo, or downloaded mailin.py . You can use this small sample script to get started
```python
from mailin import Mailin
m = Mailin("https://api.sendinblue.com/v2.0","access key",5)	#Optional parameter: Timeout in Secs
data = { "type":"classic",
	"status":"queued",
	"page":1,
	"page_limit":10
}
campaigns = m.get_campaigns_v2(data)
```
4. To explore more, you should visit the [SendinBlue API documentation](https://apidocs.sendinblue.com).

Support and Feedback
====================

Be sure to visit the SendinBlue official [documentation website](https://apidocs.sendinblue.com) for additional information about our API.

If you find a bug, please submit the issue in [Github](https://github.com/mailin-api/mailin-api-python/issues) directly.

As always, if you need additional assistance, drop us a note [here](https://apidocs.sendinblue.com/support/)

## Available functions

List of API calls that you can make, you can click to read more about it. Please do note that the order of parameters are important.

### Campaign calls

 * [get_account](https://apidocs.sendinblue.com/account/#1)() - Get your account information
 * [get_smtp_details](https://apidocs.sendinblue.com/account/#7)() - Get your SMTP account information
 * [create_child_account](https://apidocs.sendinblue.com/account/#2)(data) - Create a Reseller child account
 * [update_child_account](https://apidocs.sendinblue.com/account/#3)(data) - Update a Reseller child account
 * [delete_child_account](https://apidocs.sendinblue.com/account/#4)(data) - Delete a Reseller child account
 * [get_reseller_child](https://apidocs.sendinblue.com/account/#5)(data) - Get Reseller child accounts
 * [add_remove_child_credits](https://apidocs.sendinblue.com/account/#6)(data) - Add/Remove Reseller child credits
 * [get_campaigns_v2](https://apidocs.sendinblue.com/campaign/#1)(data) - Get list of all campaigns or of specific type or status or both
 * [get_campaign_v2](https://apidocs.sendinblue.com/campaign/#1)(data) - Get specific campaign object
 * [create_campaign](https://apidocs.sendinblue.com/campaign/#2)(data) - Create a campaign
 * [delete_campaign](https://apidocs.sendinblue.com/campaign/#3)(data) - Delete a campaign
 * [update_campaign](https://apidocs.sendinblue.com/campaign/#4)(data) - Update campaign information
 * [campaign_report_email](https://apidocs.sendinblue.com/campaign/#5)(data) - Sending reports to specific emails
 * [campaign_recipients_export](https://apidocs.sendinblue.com/campaign/#6)(data) - Export recipients of a campaign
 * [send_bat_email](https://apidocs.sendinblue.com/campaign/#7)(data) - Send a test Email (bat)
 * [create_trigger_campaign](https://apidocs.sendinblue.com/campaign/#8)(data) - Create a trigger campaign
 * [update_trigger_campaign](https://apidocs.sendinblue.com/campaign/#9)(data) - Update trigger campaign information
 * [share_campaign](https://apidocs.sendinblue.com/campaign/#10)(data) - Get campaign share link
 * [update_campaign_status](https://apidocs.sendinblue.com/campaign/#11)(data) - Modify a campaign status
 * [get_folders](https://apidocs.sendinblue.com/folder/#1)(data) - Get list of all the folder details.
 * [get_folder](https://apidocs.sendinblue.com/folder/#2)(data) - Get all the folder details for folder with id <id>
 * [create_folder](https://apidocs.sendinblue.com/folder/#3)(data) - Create a folder
 * [delete_folder](https://apidocs.sendinblue.com/folder/#4)(data) - Delete folder with folder id <id>
 * [update_folder](https://apidocs.sendinblue.com/folder/#5)(data) - Update folder with folder id <id>
 * [get_lists](https://apidocs.sendinblue.com/list/#1)(data) - Get all the lists
 * [get_list](https://apidocs.sendinblue.com/list/#2)(data) - Get information about a list
 * [create_list](https://apidocs.sendinblue.com/list/#3)(data) - Create a list
 * [delete_list](https://apidocs.sendinblue.com/list/#4)(data) - Delete a list
 * [update_list](https://apidocs.sendinblue.com/list/#5)(data) - Updating a list
 * [add_users_list](https://apidocs.sendinblue.com/list/#6)(data) - Add users to a list
 * [delete_users_list](https://apidocs.sendinblue.com/list/#7)(data) - Delete users from a list
 * [get_attributes](https://apidocs.sendinblue.com/attribute/#1)() - Listing all attributes
 * [get_attribute](https://apidocs.sendinblue.com/attribute/#2)(data) - Listing a certain type attributes
 * [create_attribute](https://apidocs.sendinblue.com/attribute/#3)(data) - Creating attributes
 * [delete_attribute](https://apidocs.sendinblue.com/attribute/#4)(data) - Deleting attributes of the given type
 * [get_user](https://apidocs.sendinblue.com/user/#2)(data) - Get information about a user/email
 * [create_update_user](https://apidocs.sendinblue.com/user/#1)(data) - Create/Update a user information
 * [delete_user](https://apidocs.sendinblue.com/user/#3)(data) - Deleting user from db is not permitted but this action will unlink him from all lists
 * [import_users](https://apidocs.sendinblue.com/user/#4)(data) - Import users/emails
 * [export_users](https://apidocs.sendinblue.com/user/#5)(data) - Export users/emails
 * [get_processes](https://apidocs.sendinblue.com/process/#1)(data) - Get information about all background processes
 * [get_process](https://apidocs.sendinblue.com/process/#2)(data) - Get information about a specific process
 * [get_senders](https://apidocs.sendinblue.com/sender-management/#1)(data) - Get information about all/specific senders
 * [create_sender](https://apidocs.sendinblue.com/sender-management/#2)(data) - Create a sender
 * [delete_sender](https://apidocs.sendinblue.com/sender-management/#3)(data) - Delete a sender
 * [update_sender](https://apidocs.sendinblue.com/sender-management/#4)(data) - Update a sender

### SMTP calls

 * [get_report](https://apidocs.sendinblue.com/report/)(data) - Retrieve information for all report events
 * [get_statistics](https://apidocs.sendinblue.com/statistics/)(data) - Get aggregate statistics about emails sent
 * [get_webhooks](https://apidocs.sendinblue.com/webhooks/#1)(data) - Get list of all registered webhooks or of specific type
 * [get_webhook](https://apidocs.sendinblue.com/webhooks/#2)(data) - Get information about a webhook
 * [create_webhook](https://apidocs.sendinblue.com/webhooks/#3)(data) - Registering a webhook
 * [delete_webhook](https://apidocs.sendinblue.com/webhooks/#5)(data) - Deleting a webhook
 * [update_webhook](https://apidocs.sendinblue.com/webhooks/#4)(data) - Editing a webhook
 * [delete_bounces](https://apidocs.sendinblue.com/bounces/)(data) - Deleting bounces
 * [send_email](https://apidocs.sendinblue.com/tutorial-sending-transactional-email/)(data) - Sending out a transactional email
 * [send_transactional_template](https://apidocs.sendinblue.com/template/)(data) - Send templates created on SendinBlue, through SendinBlue smtp.
 * [create_template](https://apidocs.sendinblue.com/template/#2)(data) - Create a template 
 * [update_template](https://apidocs.sendinblue.com/template/#3)(data) - Update template information

### SMS calls

 * [send_sms](https://apidocs.sendinblue.com/mailin-sms/#1)(data) - Sending a SMS
 * [create_sms_campaign](https://apidocs.sendinblue.com/mailin-sms/#2)(data) - Create a SMS campaign
 * [update_sms_campaign](https://apidocs.sendinblue.com/mailin-sms/#3)(data) - Update a SMS campaign
 * [send_bat_sms](https://apidocs.sendinblue.com/mailin-sms/#4)(data) - Send a test SMS campaign

## Install

To install the `mailin` module you can run `python setup.py install` in the root of the distribution.

### Dependencies

To just install the dependencies run `pip install -r requirements.txt`