# Raven-Storm 工具包

<img src="https://img.shields.io/badge/Python-3.8-blue"> <img src="https://img.shields.io/badge/Status-Beta-orange"> <img src="https://img.shields.io/badge/Version-4-red"> <img src="https://img.shields.io/badge/Licence-MIT-yellowgreen"> <a href="https://taguar258.github.io/Raven-Storm/INSTALLATION"><img src="https://img.shields.io/badge/Download-Now-green"></a>

**Raven-Storm 是一个强大的 DDoS 工具包，适用于渗透测试，包含多个协议的攻击模块，使用 Python(3.8) 编写。**

轻松击垮 WiFi 接入点、网络中的设备、服务器、服务和蓝牙设备。

Raven（缩写）旨在帮助您**测试、理解并从压力测试攻击中学习**。

Raven 可以**应对强大的服务器**，并且**可以针对非典型目标进行优化**。

Raven 可以满足您的需求，即使是**干扰 WiFi 网络或蓝牙设备**。

_我已将此仓库归档，因为我目前不想继续开发它。_

![MOSHED](https://user-images.githubusercontent.com/36562445/90558504-77d7ca80-e19c-11ea-9dd5-6ba902934866.gif)

## 它有什么不同

- [x] Raven-Storm 包含创建快捷方式和更高效工作的工具。
- [x] Raven 在关闭主机和服务器方面**高效且强大**。
- [x] Raven-Storm 的目标是**测试**和理解。
- [x] Raven 允许您将客户端连接在一起以创建僵尸网络。
- [x] 支持不同协议，例如 UDP/TCP、ICMP、HTTP、L2CAP、ARP 和 IEEE。

## 安装

只需输入以下命令即可在 Linux 上安装 Raven-Storm。

```bash
curl -s https://raw.githubusercontent.com/Taguar258/Raven-Storm/master/install.sh | sudo bash -s
```

<a style="color: grey" href="https://taguar258.github.io/Raven-Storm/INSTALLATION"><b>点击这里查看更详细的安装指南。</b></a>


<a style="color: grey" href="https://github.com/Taguar258/Raven-Storm/blob/master/README.md#info-and-warning"><b>使用条款</b></a>

<a style="color: grey" href="https://github.com/Taguar258/Raven-Storm/blob/master/LICENSE">许可证</a>

<a style="color: grey" href="https://github.com/Taguar258/Raven-Storm/projects/1">项目状态/待办事项</a>

<a style="color: grey" href="https://github.com/Taguar258/CLIF/">CLIF 框架</a>

## 使用哪个模块

| 方法 | 模块 |
| ------- | --- |
| ping | l3 |
| udp/tcp 服务 | l4 |
| 网站 | l7 |
| 本地设备 | arp |
| 蓝牙 | bl |
| wifi | wifi |
| 僵尸网络 | server |

_如果 L7 失败，请尝试使用 L4 攻击。_

<!--![Screenshot_20190405_181220](https://user-images.githubusercontent.com/36562445/55641522-60c65180-57ce-11e9-8c65-084edc2bfb45.jpg)--> 
![Preview1](https://user-images.githubusercontent.com/36562445/98484349-152c2300-220f-11eb-84a0-1c3c57415d64.png)

![Preview2](https://user-images.githubusercontent.com/36562445/98694260-8552ba00-2371-11eb-9e20-fd5432c90849.png)
<!--![Screenshot_20190405_181220](https://user-images.githubusercontent.com/36562445/63696325-bdc4b180-c81a-11e9-89b8-a7ce24df08ca.png)-->

## 示例

![Gif](https://user-images.githubusercontent.com/36562445/98694347-a0252e80-2371-11eb-95ec-925e8c98948f.gif)
<!--![render1581110570685](https://user-images.githubusercontent.com/36562445/74067207-f9ce8600-49f8-11ea-9d54-97a056169cf7.gif)-->

## 如何运行 DDoS 攻击

_您大概已经知道 DoS 和 DDoS 的区别：_
_DoS 攻击由单个机器执行，DDoS 攻击由多个机器执行。_

_但我们如何使用 Raven-Storm 执行 DDoS 攻击？_


要连接多个 Raven-Storm 实例，您需要先打开一个主机。
只需执行命令 `server` 并定义自定义密码，以防止他人干扰。
运行后，您将收到一个 URL，在执行 `ddos` 命令时可连接该 URL。


## 信息与警告

__Raven-Storm 工具包的创建者（Taguar258）不对造成的损害承担任何责任。用户须自行承担责任，无论是：滥用 Raven-Storm 用于非法目的，还是 Raven-Storm 导致的意外损害。
创建者并未打算将 Raven-Storm 用作非法用途，也不支持任何对该工具的非法滥用。
使用本软件即表示您同意自行承担因 Raven-Storm 以任何方式造成的损害的全部责任。
如果用户没有对所包含的攻击有经验，创建者不希望其使用 Raven-Storm。
每次攻击都会造成暂时性损害，但长期损害绝对可能发生。
Raven-Storm 不应建议用户执行非法活动。__

__本软件按“原样”提供，不提供任何形式的明示或暗示担保，包括但不限于对适销性、特定用途适用性和非侵权性的担保。在任何情况下，作者或版权持有人均不对因使用本软件或与本软件相关的交易而产生的任何索赔、损害或其他责任承担责任，无论是合同诉讼、侵权行为还是其他原因。__

**MIT Taguar258 2020**

