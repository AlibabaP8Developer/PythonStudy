pyspark安装
```javascript
pip install pyspark
```

问题：
Mac：zsh: command not found: pip
解决：
对于 macOS/Linux 用户：
```javascript
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

WARNING: The scripts pip, pip3 and pip3.9 are installed in '/Users/lizhenghang/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  NOTE: The current PATH contains path(s) starting with `~`, which may not be expanded by all applications.
    
打开终端并输入以下命令：
export PATH="$PATH:/Users/lizhenghang/Library/Python/3.9/bin"
现在，再次尝试在终端中运行 pip install pyspark 命令，应该可以正常工作了
```
