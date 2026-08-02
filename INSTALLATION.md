# Raven-Storm

<a style="color: white;" href="https://github.com/Taguar258/Raven-Storm/blob/master/INSTALLATION.md#lazy-installer">高级</a> - <a style="color: white;" href="https://github.com/Taguar258/Raven-Storm/blob/master/INSTALLATION.md#or-start-your-unix-terminal-and-type-in-following">专家</a> - <a style="color: white;" href="https://github.com/Taguar258/Raven-Storm/blob/master/INSTALLATION.md#other-operating-systems">其他操作系统</a> - <a style="color: white;" href="https://github.com/Taguar258/Raven-Storm/blob/master/INSTALLATION.md#uninstall">卸载</a>

## 懒人安装器
(高级)

要安装 Raven-Storm，请输入以下命令：

(您可能需要先安装 curl)

```curl -s https://raw.githubusercontent.com/Taguar258/Raven-Storm/master/install.sh | sudo bash -s```

![render1604868703436](https://user-images.githubusercontent.com/36562445/98484164-d0ec5300-220d-11eb-8fe5-0c9d4d2103e6.gif)

## 或者打开您的 Unix 终端并输入以下内容

(专家)

```sudo pkg/pacman/apt-get/brew install git python3 nmap python3-setuptools bluez dsniff iputils-ping aircrack-ng```

```git clone https://github.com/Taguar258/Raven-Storm/```

```cd Raven-Storm```

```sudo bash install_to_bin.sh```

```sudo rst```

## 其他操作系统

(基于 Unix 的系统，如 Linux 和 macOS/OSX，可原生运行 Raven-Storm。)
(如果您想在 Windows 上使用 Raven-Storm，只需执行下面列出的步骤，但请注意它不会像 Unix 系统上一样稳定运行，并且并非所有模块都可用。)

只需安装 Python 3.8 并下载本仓库。

然后您需要安装依赖项（requirements.txt）并运行 main.py。

0. 安装 Python（3.8）（3.6 也应可用）。(在 Windows 上，请确保勾选“添加到 PATH”。)

1. 下载压缩包

2. 解压

3. 在 Raven-Storm 文件夹中打开终端。(在 Windows 上，您应该可以按住 Shift 键右键点击文件夹，然后选择“在 PowerShell 中打开（管理员）”。)

4. 安装依赖项。

`pip install -r requirements.txt`

5. 运行 Raven-Storm。

`python main.py`

(您可能需要在 python 和 pip 后面直接加上数字 3。)

## 卸载

只需执行以下命令：

```
sudo bash /usr/share/Raven-Storm/uninstall.sh
```
