import re
email = input("Enter e-mail address: ")

email_check = re.compile(r"\S+\@+\S+\.+\S{2,}")

if email_check.match(email):
    print("email address format correct")
else:
    print("email address format incorrect")
    exit(1)

email_groups = re.search(
    r"^(?P<username>[^@]+)@(?P<provider>[^.]+)\.(?P<tld>.+)$",
    email,
)

if email_groups:
    print(email_groups.group("username"))
    print(email_groups.group("provider"))
    print(email_groups.group("tld"))