import setuptools
with open("README.md", 'r', encoding='utf-8') as f:
    long_desc = f.read()
    
__version__ = "0.0.0"
REPO_NAME = 'Text-Summarization-End-To-End'
AUTHOR_USER_NAME = 'AnilKumar-06'
SRC_REPO = 'textSummerizer'
AUTHER_EMAIL = 'anilmt06@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author_email=AUTHER_EMAIL,
    description="A small python package for text summerization",
    long_description=long_desc,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)