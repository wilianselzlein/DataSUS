import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--download", 
    help="Download FTP file and write in db", 
    action="store_true", 
    default=True
)

parser.add_argument(
    "--origin",
    help="SIA or SIH",
    default="SIA",
    type=str
)

parser.add_argument(
    "--type",
    help="PA, AM, AMP, AN, AQ, etc.",
    default="PA",
    type=str
)

parser.add_argument(
    "--state",
    help="Example RS",
    default="RS",
    type=str
)

parser.add_argument(
    "--year",
    help="Example 21 for 2021",
    default="21",
    type=str
)

parser.add_argument(
    "--month",
    help="Example 01 for january",
    default="01",
    type=str
)

#TODO
# parser.add_argument(
#     "--export", 
#     help="Export file from DB", 
#     action="store_true", 
#     default=True
# )