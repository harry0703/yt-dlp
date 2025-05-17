from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="yt-dlp",  # 包名
    version="0.1.0",  # 版本号，根据你的项目实际情况修改
    author="harry0703",  # 作者名
    author_email="harryliuwx888@gmail.com",  # 替换为你的邮箱
    description="A youtube-dl fork with additional features and fixes",  # 简短描述
    long_description=long_description,  # 详细描述（通常从README.md读取）
    long_description_content_type="text/markdown",  # 描述内容的类型
    url="https://github.com/harry0703/yt-dlp",  # 项目主页
    packages=find_packages(include=["yt_dlp", "yt_dlp.*"]),  # 包含的包
    python_requires=">=3.9",  # Python版本要求
    install_requires=[  # 依赖项
        "mutagen>=1.45.1",
        "pycryptodome>=3.18.0",
        "websockets>=10.0",
        "brotli>=1.0.9",
    ],
    entry_points={  # 可执行命令
        "console_scripts": [
            "yt-dlp=yt_dlp:main",
        ],
    },
    classifiers=[  # 分类信息
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Video",
        "Topic :: Utilities",
    ],
)
