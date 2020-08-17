import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="randomChar",
    version="0.1.5",
    author="Franklin Ikeh",
    author_email="ikehfranklind3c0d3r@gmail.com",
    tests_require=["pytest"],
    py_modules=["randomchar"],
    description="Simpler random string generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fr4nkl1n-1k3h/randomChar",
    keywords=["random, strings, characters, tools, module, generator"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        # Indicates who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
    ],
    python_requires=">=3.6, <4",
    project_urls={  # Optional
        "Bug Reports": "https://github.com/fr4nkl1n-1k3h/randomchar/issues",
        "Source": "https://github.com/fr4nkl1n-1k3h/randomchar/",
    },
)
