#!/usr/bin/python
def department(employee_id, level=1):
    if employee_id == '001':
        if level == 1:
            print("工程销售-销售顾问")
        elif level == 2:
            print("工程销售-销售主管")
        else:
            print("工程销售-非销售")
    elif employee_id == "002":
        if level == 1:
            print("工程客服-客服专员")
        elif level == 2:
            print("工程客服-客服主管")
        else:
            print("工程客服-非客服")
    else:
        print("非工程信息部门")

department('002', level=3)
