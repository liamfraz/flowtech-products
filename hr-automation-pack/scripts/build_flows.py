"""
Build all 5 HR Automation flow template ZIPs.
Each ZIP contains a single definition.json importable into Power Automate.
"""
import json
import zipfile
import os

BASE = "/Users/liamfrazer/Documents/flowtech/products/hr-automation-pack/flows"

# ── Flow 1: New Employee Onboarding ──────────────────────────────────────────
flow1 = {
    "$schema": "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
        "$connections": {"defaultValue": {}, "type": "Object"}
    },
    "triggers": {
        "When_a_new_item_is_created_in_HR_Onboarding_list": {
            "type": "ApiConnection",
            "inputs": {
                "host": {"connection": {"name": "@parameters('$connections')['sharepointonline']['connectionId']"}},
                "method": "get",
                "path": "/datasets/@{encodeURIComponent('https://yourtenant.sharepoint.com/sites/HR')}/tables/@{encodeURIComponent('HR-Onboarding-Requests')}/onnewitems"
            },
            "recurrence": {"frequency": "Minute", "interval": 5}
        }
    },
    "actions": {
        "Try_Block": {
            "type": "Scope",
            "actions": {
                "Create_Onboarding_Task_List_in_SharePoint": {
                    "type": "ApiConnection",
                    "runAfter": {},
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['sharepointonline']['connectionId']"}},
                        "method": "post",
                        "path": "/datasets/@{encodeURIComponent('https://yourtenant.sharepoint.com/sites/HR')}/tables/@{encodeURIComponent('Onboarding-Tasks')}/items",
                        "body": {
                            "Title": "Onboarding: @{triggerBody()?['EmployeeFullName']}",
                            "EmployeeName": "@{triggerBody()?['EmployeeFullName']}",
                            "StartDate": "@{triggerBody()?['StartDate']}",
                            "Department": "@{triggerBody()?['Department']}",
                            "Manager": "@{triggerBody()?['ManagerEmail']}",
                            "Status": "Not Started"
                        }
                    }
                },
                "Create_IT_Setup_Task": {
                    "type": "ApiConnection",
                    "runAfter": {"Create_Onboarding_Task_List_in_SharePoint": ["Succeeded"]},
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['sharepointonline']['connectionId']"}},
                        "method": "post",
                        "path": "/datasets/@{encodeURIComponent('https://yourtenant.sharepoint.com/sites/HR')}/tables/@{encodeURIComponent('Onboarding-Tasks')}/items",
                        "body": {
                            "Title": "IT: Provision laptop + M365 account for @{triggerBody()?['EmployeeFullName']}",
                            "AssignedTo": "IT Team",
                            "DueDate": "@{addDays(triggerBody()?['StartDate'], -3)}",
                            "Status": "Not Started",
                            "Category": "IT Setup"
                        }
                    }
                },
                "Create_HR_Induction_Task": {
                    "type": "ApiConnection",
                    "runAfter": {"Create_IT_Setup_Task": ["Succeeded"]},
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['sharepointonline']['connectionId']"}},
                        "method": "post",
                        "path": "/datasets/@{encodeURIComponent('https://yourtenant.sharepoint.com/sites/HR')}/tables/@{encodeURIComponent('Onboarding-Tasks')}/items",
                        "body": {
                            "Title": "HR: Complete induction paperwork for @{triggerBody()?['EmployeeFullName']}",
                            "AssignedTo": "HR Team",
                            "DueDate": "@{triggerBody()?['StartDate']}",
                            "Status": "Not Started",
                            "Category": "HR Admin"
                        }
                    }
                },
                "Create_Manager_Welcome_Task": {
                    "type": "ApiConnection",
                    "runAfter": {"Create_HR_Induction_Task": ["Succeeded"]},
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['sharepointonline']['connectionId']"}},
                        "method": "post",
                        "path": "/datasets/@{encodeURIComponent('https://yourtenant.sharepoint.com/sites/HR')}/tables/@{encodeURIComponent('Onboarding-Tasks')}/items",
                        "body": {
                            "Title": "Manager: 1:1 meeting with @{triggerBody()?['EmployeeFullName']} on Day 1",
                            "AssignedTo": "@{triggerBody()?['ManagerEmail']}",
                            "DueDate": "@{triggerBody()?['StartDate']}",
                            "Status": "Not Started",
                            "Category": "Manager Action"
                        }
                    }
                },
                "Send_Teams_Welcome_Message_to_Manager": {
                    "type": "ApiConnection",
                    "runAfter": {"Create_Manager_Welcome_Task": ["Succeeded"]},
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['teams']['connectionId']"}},
                        "method": "post",
                        "path": "/v1.0/teams/chats/messages",
                        "body": {
                            "recipient": {"groupId": "YOUR_TEAMS_GROUP_ID", "channelId": "YOUR_CHANNEL_ID"},
                            "messageBody": "<h2>New Team Member Starting Soon!</h2><p><strong>@{triggerBody()?['EmployeeFullName']}</strong> joins <strong>@{triggerBody()?['Department']}</strong> on <strong>@{triggerBody()?['StartDate']}</strong>.</p><p>Onboarding tasks have been created in SharePoint. Please review and complete your assigned items before their start date.</p><p>Questions? Contact HR at hr@yourdomain.com.au</p>"
                        }
                    }
                },
                "Send_Welcome_Email_to_New_Employee": {
                    "type": "ApiConnection",
                    "runAfter": {"Send_Teams_Welcome_Message_to_Manager": ["Succeeded"]},
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['office365']['connectionId']"}},
                        "method": "post",
                        "path": "/v2/Mail",
                        "body": {
                            "To": "@{triggerBody()?['PersonalEmail']}",
                            "Subject": "Welcome to the team, @{triggerBody()?['EmployeeFirstName']}!",
                            "Body": "<html><body><p>Hi @{triggerBody()?['EmployeeFirstName']},</p><p>We're excited to have you joining us on <strong>@{triggerBody()?['StartDate']}</strong>.</p><p>Your manager <strong>@{triggerBody()?['ManagerName']}</strong> will be in touch shortly with first-day details.</p><p>Your onboarding checklist will be waiting for you on Day 1. If you have any questions before then, reply to this email.</p><p>Looking forward to meeting you!</p><p>Human Resources Team</p></body></html>",
                            "IsHtml": True
                        }
                    }
                }
            }
        },
        "Catch_Block": {
            "type": "Scope",
            "runAfter": {"Try_Block": ["Failed", "TimedOut"]},
            "actions": {
                "Notify_HR_of_Error": {
                    "type": "ApiConnection",
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['office365']['connectionId']"}},
                        "method": "post",
                        "path": "/v2/Mail",
                        "body": {
                            "To": "hr@yourdomain.com.au",
                            "Subject": "FLOW ERROR: Onboarding flow failed for @{triggerBody()?['EmployeeFullName']}",
                            "Body": "<p>The onboarding flow encountered an error. Please process this onboarding manually.</p><p>Employee: @{triggerBody()?['EmployeeFullName']}</p><p>Start Date: @{triggerBody()?['StartDate']}</p><p>Error: @{result('Try_Block')}</p>",
                            "IsHtml": True
                        }
                    }
                }
            }
        }
    }
}

# ── Flow 2: Leave Request Approval ────────────────────────────────────────────
flow2 = {
    "$schema": "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
        "$connections": {"defaultValue": {}, "type": "Object"}
    },
    "triggers": {
        "When_a_new_response_is_submitted_Leave_Request_Form": {
            "type": "ApiConnection",
            "inputs": {
                "host": {"connection": {"name": "@parameters('$connections')['microsoftforms']['connectionId']"}},
                "method": "get",
                "path": "/datasets/YOUR_FORM_ID/tables/YOUR_FORM_ID/onnewitems"
            },
            "recurrence": {"frequency": "Minute", "interval": 5}
        }
    },
    "actions": {
        "Try_Block": {
            "type": "Scope",
            "actions": {
                "Get_Form_Response_Details": {
                    "type": "ApiConnection",
                    "runAfter": {},
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['microsoftforms']['connectionId']"}},
                        "method": "get",
                        "path": "/datasets/YOUR_FORM_ID/tables/YOUR_FORM_ID/items/@{triggerBody()?['id']}"
                    }
                },
                "Start_and_Wait_For_Manager_Approval": {
                    "type": "ApiConnection",
                    "runAfter": {"Get_Form_Response_Details": ["Succeeded"]},
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['approvals']['connectionId']"}},
                        "method": "post",
                        "path": "/approvalRequests/sync",
                        "body": {
                            "approvalType": "Basic",
                            "title": "Leave Request: @{body('Get_Form_Response_Details')?['r3']} (@{body('Get_Form_Response_Details')?['r6']} to @{body('Get_Form_Response_Details')?['r7']})",
                            "assignedTo": "@{body('Get_Form_Response_Details')?['managerEmail']}",
                            "details": "Employee @{body('Get_Form_Response_Details')?['r3']} has requested @{body('Get_Form_Response_Details')?['r4']} leave from @{body('Get_Form_Response_Details')?['r6']} to @{body('Get_Form_Response_Details')?['r7']} (@{body('Get_Form_Response_Details')?['r5']} days). Reason: @{body('Get_Form_Response_Details')?['r8']}",
                            "requestor": "@{body('Get_Form_Response_Details')?['r2']}"
                        }
                    }
                },
                "Check_Approval_Outcome": {
                    "type": "If",
                    "runAfter": {"Start_and_Wait_For_Manager_Approval": ["Succeeded"]},
                    "expression": {
                        "and": [{"equals": ["@body('Start_and_Wait_For_Manager_Approval')?['outcome']", "Approve"]}]
                    },
                    "actions": {
                        "Add_to_HR_Leave_Calendar": {
                            "type": "ApiConnection",
                            "inputs": {
                                "host": {"connection": {"name": "@parameters('$connections')['office365']['connectionId']"}},
                                "method": "post",
                                "path": "/v2/datasets/calendars/tables/events/items",
                                "body": {
                                    "subject": "LEAVE: @{body('Get_Form_Response_Details')?['r3']} — @{body('Get_Form_Response_Details')?['r4']}",
                                    "start": "@{body('Get_Form_Response_Details')?['r6']}",
                                    "end": "@{body('Get_Form_Response_Details')?['r7']}",
                                    "isAllDay": True,
                                    "body": "Approved leave for @{body('Get_Form_Response_Details')?['r3']}. Type: @{body('Get_Form_Response_Details')?['r4']}. Approved by: @{body('Get_Form_Response_Details')?['managerEmail']}."
                                }
                            }
                        },
                        "Update_SharePoint_Leave_Register": {
                            "type": "ApiConnection",
                            "runAfter": {"Add_to_HR_Leave_Calendar": ["Succeeded"]},
                            "inputs": {
                                "host": {"connection": {"name": "@parameters('$connections')['sharepointonline']['connectionId']"}},
                                "method": "post",
                                "path": "/datasets/@{encodeURIComponent('https://yourtenant.sharepoint.com/sites/HR')}/tables/@{encodeURIComponent('Leave-Register')}/items",
                                "body": {
                                    "Title": "@{body('Get_Form_Response_Details')?['r3']}",
                                    "LeaveType": "@{body('Get_Form_Response_Details')?['r4']}",
                                    "StartDate": "@{body('Get_Form_Response_Details')?['r6']}",
                                    "EndDate": "@{body('Get_Form_Response_Details')?['r7']}",
                                    "Days": "@{body('Get_Form_Response_Details')?['r5']}",
                                    "Status": "Approved",
                                    "ApprovedBy": "@{body('Get_Form_Response_Details')?['managerEmail']}"
                                }
                            }
                        },
                        "Email_Employee_Approved": {
                            "type": "ApiConnection",
                            "runAfter": {"Update_SharePoint_Leave_Register": ["Succeeded"]},
                            "inputs": {
                                "host": {"connection": {"name": "@parameters('$connections')['office365']['connectionId']"}},
                                "method": "post",
                                "path": "/v2/Mail",
                                "body": {
                                    "To": "@{body('Get_Form_Response_Details')?['r2']}",
                                    "Subject": "Leave Request APPROVED: @{body('Get_Form_Response_Details')?['r6']} to @{body('Get_Form_Response_Details')?['r7']}",
                                    "Body": "<html><body><p>Hi @{body('Get_Form_Response_Details')?['r3']},</p><p>Your leave request has been <strong>approved</strong>.</p><ul><li><strong>Type:</strong> @{body('Get_Form_Response_Details')?['r4']}</li><li><strong>From:</strong> @{body('Get_Form_Response_Details')?['r6']}</li><li><strong>To:</strong> @{body('Get_Form_Response_Details')?['r7']}</li><li><strong>Duration:</strong> @{body('Get_Form_Response_Details')?['r5']} days</li></ul><p>This has been recorded in the HR leave calendar. Please ensure your handover is complete before your leave begins.</p><p>HR Team</p></body></html>",
                                    "IsHtml": True
                                }
                            }
                        }
                    },
                    "else": {
                        "actions": {
                            "Email_Employee_Declined": {
                                "type": "ApiConnection",
                                "inputs": {
                                    "host": {"connection": {"name": "@parameters('$connections')['office365']['connectionId']"}},
                                    "method": "post",
                                    "path": "/v2/Mail",
                                    "body": {
                                        "To": "@{body('Get_Form_Response_Details')?['r2']}",
                                        "Subject": "Leave Request DECLINED: @{body('Get_Form_Response_Details')?['r6']} to @{body('Get_Form_Response_Details')?['r7']}",
                                        "Body": "<html><body><p>Hi @{body('Get_Form_Response_Details')?['r3']},</p><p>Unfortunately your leave request has been <strong>declined</strong>.</p><p>Please speak with your manager @{body('Get_Form_Response_Details')?['managerEmail']} to discuss alternative dates.</p><p>HR Team</p></body></html>",
                                        "IsHtml": True
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "Catch_Block": {
            "type": "Scope",
            "runAfter": {"Try_Block": ["Failed", "TimedOut"]},
            "actions": {
                "Notify_HR_of_Error": {
                    "type": "ApiConnection",
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['office365']['connectionId']"}},
                        "method": "post",
                        "path": "/v2/Mail",
                        "body": {
                            "To": "hr@yourdomain.com.au",
                            "Subject": "FLOW ERROR: Leave request approval failed",
                            "Body": "<p>The leave request approval flow failed. Please process this leave request manually.</p><p>Error details: @{result('Try_Block')}</p>",
                            "IsHtml": True
                        }
                    }
                }
            }
        }
    }
}

# ── Flow 3: Monthly Timesheet Reminder ────────────────────────────────────────
flow3 = {
    "$schema": "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
        "$connections": {"defaultValue": {}, "type": "Object"},
        "TeamsChannelId": {"defaultValue": "YOUR_CHANNEL_ID", "type": "String"},
        "TeamsGroupId": {"defaultValue": "YOUR_GROUP_ID", "type": "String"},
        "ReminderDayOfMonth": {"defaultValue": 25, "type": "Int"}
    },
    "triggers": {
        "Recurrence_Monthly_Timesheet_Reminder": {
            "type": "Recurrence",
            "recurrence": {
                "frequency": "Month",
                "interval": 1,
                "startTime": "2024-01-25T09:00:00",
                "timeZone": "AUS Eastern Standard Time",
                "schedule": {"monthDays": [25]}
            }
        }
    },
    "actions": {
        "Try_Block": {
            "type": "Scope",
            "actions": {
                "Get_Current_Month_Name": {
                    "type": "Compose",
                    "runAfter": {},
                    "inputs": "@{formatDateTime(utcNow(), 'MMMM yyyy')}"
                },
                "Post_Timesheet_Reminder_to_Teams_Channel": {
                    "type": "ApiConnection",
                    "runAfter": {"Get_Current_Month_Name": ["Succeeded"]},
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['teams']['connectionId']"}},
                        "method": "post",
                        "path": "/v1.0/teams/@{parameters('TeamsGroupId')}/channels/@{parameters('TeamsChannelId')}/messages",
                        "body": {
                            "body": {
                                "contentType": "html",
                                "content": "<h2>Timesheet Reminder — @{outputs('Get_Current_Month_Name')}</h2><p>Hi team,</p><p>A friendly reminder that <strong>timesheets for @{outputs('Get_Current_Month_Name')} are due by end of month</strong>.</p><p>Please ensure your timesheet is submitted and approved before <strong>the 31st</strong>. Late submissions delay payroll processing.</p><ul><li>Log in to the timesheet system via the SharePoint HR portal</li><li>Submit all hours worked this month</li><li>Ensure your manager approves your submission</li></ul><p>If you have any questions, contact Payroll at payroll@yourdomain.com.au.</p><p>Thanks,<br/>HR Team</p>"
                            }
                        }
                    }
                },
                "Send_Timesheet_Reminder_Email_to_All_Staff": {
                    "type": "ApiConnection",
                    "runAfter": {"Post_Timesheet_Reminder_to_Teams_Channel": ["Succeeded"]},
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['office365']['connectionId']"}},
                        "method": "post",
                        "path": "/v2/Mail",
                        "body": {
                            "To": "all-staff@yourdomain.com.au",
                            "Subject": "Action Required: Timesheet Submission Due — @{outputs('Get_Current_Month_Name')}",
                            "Body": "<html><body><p>Hi everyone,</p><p>This is your monthly reminder to submit your timesheet for <strong>@{outputs('Get_Current_Month_Name')}</strong>.</p><p><strong>Deadline: End of this month</strong></p><p>Please log in to the HR portal on SharePoint to submit your hours. Your manager will receive a notification to approve once submitted.</p><p>Late timesheets cause payroll delays — thank you for submitting on time.</p><p>HR & Payroll Team</p></body></html>",
                            "IsHtml": True
                        }
                    }
                }
            }
        },
        "Catch_Block": {
            "type": "Scope",
            "runAfter": {"Try_Block": ["Failed", "TimedOut"]},
            "actions": {
                "Notify_HR_of_Error": {
                    "type": "ApiConnection",
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['office365']['connectionId']"}},
                        "method": "post",
                        "path": "/v2/Mail",
                        "body": {
                            "To": "hr@yourdomain.com.au",
                            "Subject": "FLOW ERROR: Monthly timesheet reminder failed to send",
                            "Body": "<p>The monthly timesheet reminder flow encountered an error. Please send the reminder manually.</p>",
                            "IsHtml": True
                        }
                    }
                }
            }
        }
    }
}

# ── Flow 4: Performance Review Reminder Sequence ──────────────────────────────
flow4 = {
    "$schema": "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
        "$connections": {"defaultValue": {}, "type": "Object"}
    },
    "triggers": {
        "Recurrence_Check_Upcoming_Reviews_Daily": {
            "type": "Recurrence",
            "recurrence": {
                "frequency": "Day",
                "interval": 1,
                "startTime": "2024-01-01T08:00:00",
                "timeZone": "AUS Eastern Standard Time"
            }
        }
    },
    "actions": {
        "Try_Block": {
            "type": "Scope",
            "actions": {
                "Get_All_Employees_with_Upcoming_Reviews": {
                    "type": "ApiConnection",
                    "runAfter": {},
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['sharepointonline']['connectionId']"}},
                        "method": "get",
                        "path": "/datasets/@{encodeURIComponent('https://yourtenant.sharepoint.com/sites/HR')}/tables/@{encodeURIComponent('Performance-Reviews')}/items",
                        "queries": {
                            "$filter": "ReviewStatus eq 'Scheduled'",
                            "$orderby": "ReviewDate asc"
                        }
                    }
                },
                "For_Each_Employee": {
                    "type": "Foreach",
                    "runAfter": {"Get_All_Employees_with_Upcoming_Reviews": ["Succeeded"]},
                    "foreach": "@body('Get_All_Employees_with_Upcoming_Reviews')?['value']",
                    "actions": {
                        "Calculate_Days_Until_Review": {
                            "type": "Compose",
                            "inputs": "@int(div(sub(ticks(items('For_Each_Employee')?['ReviewDate']), ticks(utcNow())), 864000000000))"
                        },
                        "Check_30_Day_Reminder": {
                            "type": "If",
                            "runAfter": {"Calculate_Days_Until_Review": ["Succeeded"]},
                            "expression": {"and": [{"equals": ["@outputs('Calculate_Days_Until_Review')", 30]}]},
                            "actions": {
                                "Send_30_Day_Reminder_Email": {
                                    "type": "ApiConnection",
                                    "inputs": {
                                        "host": {"connection": {"name": "@parameters('$connections')['office365']['connectionId']"}},
                                        "method": "post",
                                        "path": "/v2/Mail",
                                        "body": {
                                            "To": "@{items('For_Each_Employee')?['ManagerEmail']}",
                                            "CC": "@{items('For_Each_Employee')?['EmployeeEmail']}",
                                            "Subject": "30-Day Reminder: Performance Review for @{items('For_Each_Employee')?['EmployeeName']} on @{items('For_Each_Employee')?['ReviewDate']}",
                                            "Body": "<html><body><p>Hi @{items('For_Each_Employee')?['ManagerName']},</p><p>This is a <strong>30-day advance notice</strong> that the performance review for <strong>@{items('For_Each_Employee')?['EmployeeName']}</strong> is scheduled for <strong>@{items('For_Each_Employee')?['ReviewDate']}</strong>.</p><p><strong>Action required in the next 30 days:</strong></p><ul><li>Complete the self-assessment form in SharePoint</li><li>Gather performance evidence and KPI data for the review period</li><li>Block out time in both calendars for the review meeting</li></ul><p>Access the review form: <a href='https://yourtenant.sharepoint.com/sites/HR/Lists/Performance-Reviews'>HR SharePoint Portal</a></p><p>HR Team</p></body></html>",
                                            "IsHtml": True
                                        }
                                    }
                                }
                            },
                            "else": {"actions": {}}
                        },
                        "Check_14_Day_Reminder": {
                            "type": "If",
                            "runAfter": {"Check_30_Day_Reminder": ["Succeeded"]},
                            "expression": {"and": [{"equals": ["@outputs('Calculate_Days_Until_Review')", 14]}]},
                            "actions": {
                                "Send_14_Day_Reminder_Email": {
                                    "type": "ApiConnection",
                                    "inputs": {
                                        "host": {"connection": {"name": "@parameters('$connections')['office365']['connectionId']"}},
                                        "method": "post",
                                        "path": "/v2/Mail",
                                        "body": {
                                            "To": "@{items('For_Each_Employee')?['ManagerEmail']}",
                                            "CC": "@{items('For_Each_Employee')?['EmployeeEmail']}",
                                            "Subject": "2-Week Reminder: Performance Review for @{items('For_Each_Employee')?['EmployeeName']} — @{items('For_Each_Employee')?['ReviewDate']}",
                                            "Body": "<html><body><p>Hi @{items('For_Each_Employee')?['ManagerName']},</p><p><strong>2 weeks to go</strong> until the performance review for <strong>@{items('For_Each_Employee')?['EmployeeName']}</strong> on <strong>@{items('For_Each_Employee')?['ReviewDate']}</strong>.</p><p><strong>Please ensure by end of this week:</strong></p><ul><li>Self-assessment form completed and submitted</li><li>KPI results documented in the review form</li><li>Calendar invite confirmed with the employee</li></ul><p>HR Team</p></body></html>",
                                            "IsHtml": True
                                        }
                                    }
                                }
                            },
                            "else": {"actions": {}}
                        },
                        "Check_7_Day_Reminder": {
                            "type": "If",
                            "runAfter": {"Check_14_Day_Reminder": ["Succeeded"]},
                            "expression": {"and": [{"equals": ["@outputs('Calculate_Days_Until_Review')", 7]}]},
                            "actions": {
                                "Send_7_Day_Reminder_Email": {
                                    "type": "ApiConnection",
                                    "inputs": {
                                        "host": {"connection": {"name": "@parameters('$connections')['office365']['connectionId']"}},
                                        "method": "post",
                                        "path": "/v2/Mail",
                                        "body": {
                                            "To": "@{items('For_Each_Employee')?['ManagerEmail']}",
                                            "CC": "@{items('For_Each_Employee')?['EmployeeEmail']}",
                                            "Subject": "URGENT: Performance Review in 7 Days — @{items('For_Each_Employee')?['EmployeeName']} (@{items('For_Each_Employee')?['ReviewDate']})",
                                            "Body": "<html><body><p>Hi @{items('For_Each_Employee')?['ManagerName']},</p><p>Final reminder — the performance review for <strong>@{items('For_Each_Employee')?['EmployeeName']}</strong> is <strong>7 days away</strong> (@{items('For_Each_Employee')?['ReviewDate']}).</p><p><strong>Final pre-review checklist:</strong></p><ul><li>Self-assessment submitted (employee)</li><li>Manager notes and ratings entered in SharePoint</li><li>Goals for next period drafted</li><li>Meeting room / video call booked</li></ul><p>If you need to reschedule, contact HR immediately at hr@yourdomain.com.au.</p><p>HR Team</p></body></html>",
                                            "IsHtml": True
                                        }
                                    }
                                },
                                "Post_Teams_Alert_to_HR": {
                                    "type": "ApiConnection",
                                    "runAfter": {"Send_7_Day_Reminder_Email": ["Succeeded"]},
                                    "inputs": {
                                        "host": {"connection": {"name": "@parameters('$connections')['teams']['connectionId']"}},
                                        "method": "post",
                                        "path": "/v1.0/teams/YOUR_HR_GROUP_ID/channels/YOUR_HR_CHANNEL_ID/messages",
                                        "body": {
                                            "body": {
                                                "contentType": "html",
                                                "content": "<p><strong>7-Day Alert:</strong> Performance review for <strong>@{items('For_Each_Employee')?['EmployeeName']}</strong> with manager <strong>@{items('For_Each_Employee')?['ManagerName']}</strong> is due on <strong>@{items('For_Each_Employee')?['ReviewDate']}</strong>. Please confirm preparations are complete.</p>"
                                            }
                                        }
                                    }
                                }
                            },
                            "else": {"actions": {}}
                        }
                    }
                }
            }
        },
        "Catch_Block": {
            "type": "Scope",
            "runAfter": {"Try_Block": ["Failed", "TimedOut"]},
            "actions": {
                "Notify_HR_of_Error": {
                    "type": "ApiConnection",
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['office365']['connectionId']"}},
                        "method": "post",
                        "path": "/v2/Mail",
                        "body": {
                            "To": "hr@yourdomain.com.au",
                            "Subject": "FLOW ERROR: Performance review reminder sequence failed",
                            "Body": "<p>The performance review reminder flow failed. Please check the SharePoint list manually for upcoming reviews.</p>",
                            "IsHtml": True
                        }
                    }
                }
            }
        }
    }
}

# ── Flow 5: Offboarding Checklist ─────────────────────────────────────────────
flow5 = {
    "$schema": "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
        "$connections": {"defaultValue": {}, "type": "Object"}
    },
    "triggers": {
        "When_a_new_item_is_created_in_Offboarding_Requests": {
            "type": "ApiConnection",
            "inputs": {
                "host": {"connection": {"name": "@parameters('$connections')['sharepointonline']['connectionId']"}},
                "method": "get",
                "path": "/datasets/@{encodeURIComponent('https://yourtenant.sharepoint.com/sites/HR')}/tables/@{encodeURIComponent('Offboarding-Requests')}/onnewitems"
            },
            "recurrence": {"frequency": "Minute", "interval": 5}
        }
    },
    "actions": {
        "Try_Block": {
            "type": "Scope",
            "actions": {
                "Create_IT_Offboarding_Task_Revoke_Access": {
                    "type": "ApiConnection",
                    "runAfter": {},
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['sharepointonline']['connectionId']"}},
                        "method": "post",
                        "path": "/datasets/@{encodeURIComponent('https://yourtenant.sharepoint.com/sites/HR')}/tables/@{encodeURIComponent('Offboarding-Tasks')}/items",
                        "body": {
                            "Title": "IT: Revoke M365 access for @{triggerBody()?['EmployeeFullName']} on @{triggerBody()?['LastDay']}",
                            "AssignedTo": "IT Team",
                            "DueDate": "@{triggerBody()?['LastDay']}",
                            "Status": "Not Started",
                            "Category": "IT",
                            "EmployeeName": "@{triggerBody()?['EmployeeFullName']}",
                            "Priority": "High"
                        }
                    }
                },
                "Create_IT_Offboarding_Task_Recover_Equipment": {
                    "type": "ApiConnection",
                    "runAfter": {"Create_IT_Offboarding_Task_Revoke_Access": ["Succeeded"]},
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['sharepointonline']['connectionId']"}},
                        "method": "post",
                        "path": "/datasets/@{encodeURIComponent('https://yourtenant.sharepoint.com/sites/HR')}/tables/@{encodeURIComponent('Offboarding-Tasks')}/items",
                        "body": {
                            "Title": "IT: Collect laptop, phone, and access cards from @{triggerBody()?['EmployeeFullName']}",
                            "AssignedTo": "IT Team",
                            "DueDate": "@{triggerBody()?['LastDay']}",
                            "Status": "Not Started",
                            "Category": "IT",
                            "EmployeeName": "@{triggerBody()?['EmployeeFullName']}"
                        }
                    }
                },
                "Create_HR_Offboarding_Task_Exit_Interview": {
                    "type": "ApiConnection",
                    "runAfter": {"Create_IT_Offboarding_Task_Recover_Equipment": ["Succeeded"]},
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['sharepointonline']['connectionId']"}},
                        "method": "post",
                        "path": "/datasets/@{encodeURIComponent('https://yourtenant.sharepoint.com/sites/HR')}/tables/@{encodeURIComponent('Offboarding-Tasks')}/items",
                        "body": {
                            "Title": "HR: Conduct exit interview with @{triggerBody()?['EmployeeFullName']}",
                            "AssignedTo": "HR Team",
                            "DueDate": "@{addDays(triggerBody()?['LastDay'], -3)}",
                            "Status": "Not Started",
                            "Category": "HR",
                            "EmployeeName": "@{triggerBody()?['EmployeeFullName']}"
                        }
                    }
                },
                "Create_HR_Offboarding_Task_Final_Pay": {
                    "type": "ApiConnection",
                    "runAfter": {"Create_HR_Offboarding_Task_Exit_Interview": ["Succeeded"]},
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['sharepointonline']['connectionId']"}},
                        "method": "post",
                        "path": "/datasets/@{encodeURIComponent('https://yourtenant.sharepoint.com/sites/HR')}/tables/@{encodeURIComponent('Offboarding-Tasks')}/items",
                        "body": {
                            "Title": "HR/Payroll: Process final pay, leave payout, and separation documents for @{triggerBody()?['EmployeeFullName']}",
                            "AssignedTo": "HR Team",
                            "DueDate": "@{triggerBody()?['LastDay']}",
                            "Status": "Not Started",
                            "Category": "HR",
                            "EmployeeName": "@{triggerBody()?['EmployeeFullName']}"
                        }
                    }
                },
                "Create_Manager_Offboarding_Task_Knowledge_Transfer": {
                    "type": "ApiConnection",
                    "runAfter": {"Create_HR_Offboarding_Task_Final_Pay": ["Succeeded"]},
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['sharepointonline']['connectionId']"}},
                        "method": "post",
                        "path": "/datasets/@{encodeURIComponent('https://yourtenant.sharepoint.com/sites/HR')}/tables/@{encodeURIComponent('Offboarding-Tasks')}/items",
                        "body": {
                            "Title": "Manager: Arrange knowledge transfer and handover with @{triggerBody()?['EmployeeFullName']}",
                            "AssignedTo": "@{triggerBody()?['ManagerEmail']}",
                            "DueDate": "@{addDays(triggerBody()?['LastDay'], -5)}",
                            "Status": "Not Started",
                            "Category": "Manager",
                            "EmployeeName": "@{triggerBody()?['EmployeeFullName']}"
                        }
                    }
                },
                "Send_Offboarding_Summary_Teams_Message": {
                    "type": "ApiConnection",
                    "runAfter": {"Create_Manager_Offboarding_Task_Knowledge_Transfer": ["Succeeded"]},
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['teams']['connectionId']"}},
                        "method": "post",
                        "path": "/v1.0/teams/YOUR_HR_GROUP_ID/channels/YOUR_HR_CHANNEL_ID/messages",
                        "body": {
                            "body": {
                                "contentType": "html",
                                "content": "<h3>Offboarding Initiated: @{triggerBody()?['EmployeeFullName']}</h3><p>Last day: <strong>@{triggerBody()?['LastDay']}</strong> | Department: @{triggerBody()?['Department']} | Manager: @{triggerBody()?['ManagerEmail']}</p><p>Offboarding tasks have been created in SharePoint for IT, HR, and the line manager. Please check your assigned tasks and complete them before the last day.</p>"
                            }
                        }
                    }
                },
                "Send_Farewell_Preparation_Email_to_Manager": {
                    "type": "ApiConnection",
                    "runAfter": {"Send_Offboarding_Summary_Teams_Message": ["Succeeded"]},
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['office365']['connectionId']"}},
                        "method": "post",
                        "path": "/v2/Mail",
                        "body": {
                            "To": "@{triggerBody()?['ManagerEmail']}",
                            "CC": "hr@yourdomain.com.au",
                            "Subject": "Offboarding Process Started: @{triggerBody()?['EmployeeFullName']} (Last Day: @{triggerBody()?['LastDay']})",
                            "Body": "<html><body><p>Hi @{triggerBody()?['ManagerName']},</p><p>The offboarding process has been initiated for <strong>@{triggerBody()?['EmployeeFullName']}</strong>, whose last day is <strong>@{triggerBody()?['LastDay']}</strong>.</p><p><strong>Your required actions (assigned in SharePoint):</strong></p><ul><li>Arrange knowledge transfer and document handover by @{addDays(triggerBody()?['LastDay'], -5)}</li><li>Ensure all work-in-progress is transitioned to other team members</li><li>Remove the employee from any distribution lists or shared mailboxes you manage</li></ul><p>IT and HR have been notified and have their respective tasks. If you have any questions, contact hr@yourdomain.com.au.</p><p>HR Team</p></body></html>",
                            "IsHtml": True
                        }
                    }
                }
            }
        },
        "Catch_Block": {
            "type": "Scope",
            "runAfter": {"Try_Block": ["Failed", "TimedOut"]},
            "actions": {
                "Notify_HR_of_Error": {
                    "type": "ApiConnection",
                    "inputs": {
                        "host": {"connection": {"name": "@parameters('$connections')['office365']['connectionId']"}},
                        "method": "post",
                        "path": "/v2/Mail",
                        "body": {
                            "To": "hr@yourdomain.com.au",
                            "Subject": "FLOW ERROR: Offboarding flow failed for @{triggerBody()?['EmployeeFullName']}",
                            "Body": "<p>The offboarding flow encountered an error. Please create offboarding tasks manually.</p><p>Employee: @{triggerBody()?['EmployeeFullName']}</p><p>Last Day: @{triggerBody()?['LastDay']}</p><p>Error: @{result('Try_Block')}</p>",
                            "IsHtml": True
                        }
                    }
                }
            }
        }
    }
}

# ── Write ZIPs ────────────────────────────────────────────────────────────────
flows = [
    ("01-employee-onboarding", "01-New-Employee-Onboarding", flow1),
    ("02-leave-request-approval", "02-Leave-Request-Approval", flow2),
    ("03-timesheet-reminder", "03-Monthly-Timesheet-Reminder", flow3),
    ("04-performance-review-reminders", "04-Performance-Review-Reminders", flow4),
    ("05-offboarding-checklist", "05-Offboarding-Checklist", flow5),
]

for folder, zip_name, flow_def in flows:
    out_path = os.path.join(BASE, folder, "flow-template.zip")
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("definition.json", json.dumps(flow_def, indent=2))
        zf.writestr("manifest.json", json.dumps({
            "schema": "1.0",
            "details": {
                "displayName": zip_name.replace("-", " "),
                "description": f"Power Automate HR template: {zip_name}",
                "environment": {"name": "YOUR_ENVIRONMENT_ID"}
            },
            "resources": {"definition": "definition.json"}
        }, indent=2))
    print(f"Created: {out_path}")

print("All 5 flow templates built.")
