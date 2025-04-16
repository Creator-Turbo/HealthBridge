from setuptools import setup, find_packages

setup(
    name="HealthBridge",  # Replace with your project name
    version="0.0.1",  # Version number
    author="Bablu kumar pandey",
    author_email="bablupandey446@gmail.com",
    description="HealthBridge: A telemedical services platform",
    long_description=open("README.md", encoding="utf-8").read() ,  # Reads the project description from README.md
    long_description_content_type="text/markdown",
    url="https://github.com/Creator-Turbo/HealthBridge",  
    packages=find_packages(),  
    include_package_data=True,
install_requires=[
    "sentence-transformers>=2.2,<3.0",
    "langchain>=0.1.0,<0.2.0",
    "flask>=2.2,<3.0",
    "pypdf>=3.0,<4.0",
    "python-dotenv>=1.0,<2.0",
    "pinecone-client>=3.0,<4.0",
    "langchain-pinecone>=0.0.3,<0.1",
    "langchain-community>=0.0.3,<0.1",
    "langchain-huggingface>=0.0.3,<0.1",
    "pymongo",
    "protobuf==4.24.3",
    "google==3.0.0",
    "googleapis-common-protos>=1.56.0"
]
,

)
