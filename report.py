
# Decorator to format report output
def report_formatter(func):
    def wrapper(*args, **kwargs):
        print("=" * 50)
        print("        DYNAMIC REPORT GENERATOR")
        print("=" * 50)
        func(*args, **kwargs)
        print("=" * 50)
    return wrapper


class Report:
    # Class variable
    template = "General Report"

    # Constructor
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Class Method
    @classmethod
    def change_template(cls, new_template):
        cls.template = new_template

    # Magic Method (__str__)
    def __str__(self):
        return f"Template : {Report.template}\nTitle    : {self.title}\nContent  : {self.content}"

    # Magic Method (__len__)
    def __len__(self):
        return len(self.content)


# Decorated Function
@report_formatter
def generate_report(report):
    print(report)
    print("Content Length:", len(report), "characters")


# Main Program
title = input("Enter Report Title: ")
content = input("Enter Report Content: ")

report = Report(title, content)

print("\nCurrent Template:", Report.template)

choice = input("Do you want to change the template? (yes/no): ")

if choice.lower() == "yes":
    new_template = input("Enter New Template Name: ")
    Report.change_template(new_template)

print()
generate_report(report)